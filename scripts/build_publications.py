#!/usr/bin/env python3
"""Gera paginas canonicas de publicacoes a partir de data/productions.yaml.

O script e deterministico e controla apenas content/publications/. A fonte
canonica continua sendo data/productions.yaml; as paginas geradas existem para
dar URL propria, SEO, Pagefind e navegacao por tipo.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import tempfile
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "productions.yaml"
PEOPLE_FILE = ROOT / "data" / "people.yaml"
PEOPLE_DIR = ROOT / "content" / "people"
OUT_DIR = ROOT / "content" / "publications"
GENERATED_BY = "scripts/build_publications.py"
CANONICAL_SOURCE = "data/productions.yaml"

LANGS = ("pt", "en")

GROUPS = {
    "scientific": {
        "pt": "Publicacoes cientificas",
        "en": "Scientific publications",
        "description": {
            "pt": "Artigos, livros, capitulos e trabalhos em eventos cientificos do CEDIS.",
            "en": "Articles, books, chapters, and conference papers by CEDIS.",
        },
    },
    "tcc": {
        "pt": "TCCs",
        "en": "Undergraduate theses",
        "description": {
            "pt": "Trabalhos de conclusao de curso orientados por pesquisadores do CEDIS.",
            "en": "Undergraduate theses supervised by CEDIS researchers.",
        },
    },
    "thesis": {
        "pt": "Dissertacoes e teses",
        "en": "Dissertations and theses",
        "description": {
            "pt": "Dissertacoes de mestrado e teses de doutorado associadas ao CEDIS.",
            "en": "Master's dissertations and doctoral theses associated with CEDIS.",
        },
    },
    "specialization": {
        "pt": "Especializacoes",
        "en": "Specialization works",
        "description": {
            "pt": "Trabalhos de especializacao orientados por pesquisadores do CEDIS.",
            "en": "Specialization works supervised by CEDIS researchers.",
        },
    },
    "registrations": {
        "pt": "Registros de software",
        "en": "Software registrations",
        "description": {
            "pt": "Registros de programa de computador e ativos tecnologicos do CEDIS.",
            "en": "Software registrations and technological assets from CEDIS.",
        },
    },
    "zenodo": {
        "pt": "Materiais no Zenodo",
        "en": "Zenodo materials",
        "description": {
            "pt": "Materiais com registro associado no Zenodo.",
            "en": "Materials with associated Zenodo records.",
        },
    },
    "didactic": {
        "pt": "Cursos e materiais didaticos",
        "en": "Courses and teaching materials",
        "description": {
            "pt": "Cursos, oficinas e materiais didaticos produzidos pelo CEDIS.",
            "en": "Courses, workshops, and teaching materials produced by CEDIS.",
        },
    },
}

TYPE_GROUP = {
    "article": "scientific",
    "book": "scientific",
    "book chapter": "scientific",
    "book_section": "scientific",
    "conference": "scientific",
    "workshop": "scientific",
    "tcc": "tcc",
    "dissertation": "thesis",
    "phd": "thesis",
    "specialization": "specialization",
    "registro": "registrations",
    "didactic": "didactic",
}

SCHEMA_TYPES = {
    "article": "ScholarlyArticle",
    "conference": "ScholarlyArticle",
    "workshop": "ScholarlyArticle",
    "book": "Book",
    "book chapter": "Chapter",
    "book_section": "Chapter",
    "tcc": "Thesis",
    "dissertation": "Thesis",
    "phd": "Thesis",
    "specialization": "Thesis",
    "registro": "SoftwareSourceCode",
}


def ascii_slug(value: str, fallback: str = "item") -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value).strip("-").lower()
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:90].strip("-") or fallback


def text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def title_for(item: dict[str, Any], lang: str) -> str:
    title = item.get("title") or {}
    if isinstance(title, dict):
        return text(title.get(lang) or title.get("en") or title.get("pt"))
    return text(title)


def summary_for(item: dict[str, Any], lang: str) -> str:
    summary = item.get("summary") or {}
    if isinstance(summary, dict):
        return text(summary.get(lang) or summary.get("en") or summary.get("pt"))
    return text(summary)


def localized_resource(value: Any, lang: str) -> str:
    if isinstance(value, dict):
        return text(value.get(lang) or value.get("en") or value.get("pt"))
    return text(value)


def base_year(value: Any) -> str:
    match = re.match(r"^([0-9]{4})", text(value))
    return match.group(1) if match else "0000"


def has_zenodo(item: dict[str, Any]) -> bool:
    zr = item.get("zenodo_record")
    if isinstance(zr, dict):
        return any(text(v) for v in zr.values())
    return bool(text(zr))


def publication_group(item: dict[str, Any]) -> str:
    pub_type = text(item.get("type"))
    if pub_type == "didactic":
        return "didactic"
    return TYPE_GROUP.get(pub_type, "scientific")


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text_value = path.read_text(encoding="utf-8")
    if not text_value.startswith("---"):
        return {}
    parts = text_value.split("---", 2)
    if len(parts) < 3:
        return {}
    data = yaml.safe_load(parts[1])
    return data if isinstance(data, dict) else {}


def load_people_index() -> list[dict[str, str]]:
    people: list[dict[str, str]] = []

    seen: set[str] = set()
    for path in sorted(PEOPLE_DIR.glob("*.pt.md")):
        pid = path.name.removesuffix(".pt.md")
        if pid == "all":
            continue
        item = parse_frontmatter(path)
        name = text(item.get("title"))
        if name:
            people.append({"id": pid, "name": name, "url": f"/people/{pid}"})
            seen.add(pid)

    data = yaml.safe_load(PEOPLE_FILE.read_text(encoding="utf-8")).get("people", [])
    for item in data:
        name = text(item.get("name"))
        pid = text(item.get("slug")) or ascii_slug(name).replace("-", "_")
        if not name or pid in seen:
            continue
        people.append({"id": pid, "name": name, "url": ""})
        seen.add(pid)
    return people


def match_person(author: str, people_index: list[dict[str, str]], ids_in_item: set[str]) -> dict[str, str] | None:
    author_norm = normalize_name(author)
    author_tokens = set(author_norm.split())
    for person in people_index:
        if person["id"] in ids_in_item:
            person_tokens = set(normalize_name(person["name"]).split())
            slug_tokens = set(normalize_name(person["id"].replace("_", " ")).split())
            overlap = author_tokens & (person_tokens | slug_tokens)
            if len(overlap) >= 2:
                return person
    for person in people_index:
        person_tokens = normalize_name(person["name"]).split()
        if len(person_tokens) >= 2 and all(token in author_norm.split() for token in (person_tokens[0], person_tokens[-1])):
            return person
    return None


def structured_authors(item: dict[str, Any], people_index: list[dict[str, str]]) -> list[dict[str, str]]:
    ids_in_item = set(item.get("people") or []) | set(item.get("tags") or []) | set(item.get("advisors") or [])
    authors = []
    for author in item.get("authors") or []:
        entry = {"name": text(author)}
        match = match_person(text(author), people_index, ids_in_item)
        if match:
            entry["id"] = match["id"]
            if match["url"]:
                entry["url"] = match["url"]
        authors.append(entry)
    return authors


def bibtex_for(item: dict[str, Any], lang: str, slug: str) -> str:
    pub_type = text(item.get("type"))
    bibtype = {
        "article": "article",
        "conference": "inproceedings",
        "workshop": "inproceedings",
        "book": "book",
        "book chapter": "incollection",
        "book_section": "incollection",
        "phd": "phdthesis",
        "dissertation": "mastersthesis",
        "specialization": "mastersthesis",
        "tcc": "mastersthesis",
        "registro": "misc",
    }.get(pub_type, "misc")
    fields = []
    authors = " and ".join(text(a) for a in item.get("authors") or [] if text(a))
    if authors:
        fields.append(("author", authors))
    fields.append(("title", title_for(item, lang)))
    if item.get("year"):
        fields.append(("year", text(item.get("year"))))
    if pub_type in {"conference", "workshop"} and text(item.get("journal_event")):
        fields.append(("booktitle", text(item.get("journal_event"))))
    if pub_type == "article" and text(item.get("journal_event")):
        fields.append(("journal", text(item.get("journal_event"))))
    if pub_type in {"book chapter", "book_section"} and text(item.get("book_title")):
        fields.append(("booktitle", text(item.get("book_title"))))
    for key, bib_key in (("volume", "volume"), ("pages", "pages"), ("publisher", "publisher"), ("location", "address")):
        if text(item.get(key)):
            fields.append((bib_key, text(item.get(key))))
    identifier = text(item.get("doi_isbn"))
    if identifier:
        fields.append(("doi" if identifier.startswith("10.") and "/" in identifier else "isbn", identifier))
    body = ",\n".join(f"  {key} = {{{value}}}" for key, value in fields)
    return f"@{bibtype}{{{slug},\n{body}\n}}"


def make_item_payload(item: dict[str, Any], index: int, people_index: list[dict[str, str]], used: set[str]) -> dict[str, Any]:
    year = base_year(item.get("year"))
    title = title_for(item, "pt") or title_for(item, "en") or f"publicacao-{index + 1}"
    first_author = text((item.get("authors") or ["cedis"])[0])
    digest = hashlib.sha1((title + first_author + text(item.get("year")) + str(index)).encode("utf-8")).hexdigest()[:8]
    slug = ascii_slug(f"{year}-{first_author}-{title}")
    if slug in used:
        slug = f"{slug}-{digest}"
    used.add(slug)

    group = publication_group(item)
    tags = [text(t) for t in item.get("tags") or [] if text(t)]
    advisors = [text(t) for t in item.get("advisors") or [] if text(t)]
    return {
        "index": index,
        "slug": slug,
        "id": f"publication_{slug.replace('-', '_')}",
        "group": group,
        "year": year,
        "raw_year": item.get("year"),
        "type": text(item.get("type")),
        "schema_type": SCHEMA_TYPES.get(text(item.get("type")), "CreativeWork"),
        "tags": tags,
        "advisors": advisors,
        "authors": structured_authors(item, people_index),
        "item": item,
        "has_zenodo": has_zenodo(item),
    }


def frontmatter(payload: dict[str, Any], lang: str) -> str:
    item = payload["item"]
    title = title_for(item, lang)
    summary = summary_for(item, lang)
    if not summary:
        authors = ", ".join(a["name"] for a in payload["authors"])
        type_label = text(item.get("type")) or "publication"
        summary = f"{type_label.title()} de {authors} ({payload['raw_year']})." if lang == "pt" else f"{type_label.title()} by {authors} ({payload['raw_year']})."

    fm = {
        "title": title,
        "date": f"{payload['year']}-01-01T00:00:00-03:00",
        "draft": False,
        "language": lang,
        "translationKey": payload["id"],
        "generated_by": GENERATED_BY,
        "canonical_source": CANONICAL_SOURCE,
        "id": payload["id"],
        "publication_index": payload["index"],
        "publication_group": payload["group"],
        "publication_type": payload["type"],
        "schema_type": payload["schema_type"],
        "year": payload["raw_year"],
        "authors": [a["name"] for a in payload["authors"]],
        "authors_structured": payload["authors"],
        "tags": payload["tags"],
        "advisors": payload["advisors"],
        "doi_isbn": text(item.get("doi_isbn")),
        "source_title": text(item.get("journal_event") or item.get("book_title")),
        "publisher": text(item.get("publisher")),
        "location": text(item.get("location")),
        "pages": text(item.get("pages")),
        "volume": text(item.get("volume")),
        "external_url": text(item.get("url")),
        "spotify_podcast": localized_resource(item.get("spotify_podcast"), lang),
        "github_repo": localized_resource(item.get("github_repo"), lang),
        "zenodo_record": localized_resource(item.get("zenodo_record"), lang),
        "summary": summary,
        "bibtex": bibtex_for(item, lang, payload["slug"]),
        "aliases": [f"/publications/{payload['slug']}/"],
    }
    return yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()


def body(payload: dict[str, Any], lang: str) -> str:
    summary = summary_for(payload["item"], lang)
    if summary:
        heading = "Resumo" if lang == "pt" else "Abstract"
        return f"## {heading}\n\n{summary}\n"
    return ""


def write_page(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_indexes(payloads: list[dict[str, Any]], out_dir: Path) -> None:
    for lang in LANGS:
        root_fm = {
            "title": "Publicações" if lang == "pt" else "Publications",
            "date": "2021-12-18T03:10:36.000Z",
            "draft": False,
            "language": lang,
            "translationKey": "publications",
            "generated_by": GENERATED_BY,
            "canonical_source": CANONICAL_SOURCE,
            "description": "Publicações do CEDIS" if lang == "pt" else "CEDIS publications",
            "featured_image": "../assets/images/featured/image_Publications.png",
            "authorimage": "../assets/images/global/author.webp",
            "aliases": ["/publications/"] if lang == "pt" else [],
        }
        write_page(
            out_dir / f"_index.{lang}.md",
            "---\n" + yaml.safe_dump(root_fm, allow_unicode=True, sort_keys=False).strip() + "\n---\n",
        )

        for group, meta in GROUPS.items():
            count = sum(1 for p in payloads if p["group"] == group or (group == "zenodo" and p["has_zenodo"]))
            group_fm = {
                "title": meta[lang],
                "date": "2026-07-20T00:00:00-03:00",
                "draft": False,
                "language": lang,
                "translationKey": f"publications_{group}",
                "generated_by": GENERATED_BY,
                "canonical_source": CANONICAL_SOURCE,
                "publication_filter": group,
                "description": meta["description"][lang],
                "summary": f"{count} registros catalogados." if lang == "pt" else f"{count} catalogued records.",
            }
            write_page(
                out_dir / group / f"_index.{lang}.md",
                "---\n" + yaml.safe_dump(group_fm, allow_unicode=True, sort_keys=False).strip() + "\n---\n",
            )


def build_publication_pages(out_dir: Path) -> int:
    data = yaml.safe_load(DATA_FILE.read_text(encoding="utf-8"))
    items = data.get("items", [])
    people_index = load_people_index()
    used: set[str] = set()
    payloads = [make_item_payload(item, i, people_index, used) for i, item in enumerate(items)]

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    write_indexes(payloads, out_dir)
    for payload in payloads:
        for lang in LANGS:
            path = out_dir / payload["group"] / payload["year"] / f"{payload['slug']}.{lang}.md"
            write_page(path, f"---\n{frontmatter(payload, lang)}\n---\n{body(payload, lang)}")

    return len(payloads) * len(LANGS)


def snapshot(root: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    if not root.exists():
        return files
    for path in sorted(root.rglob("*")):
        if path.is_file():
            files[path.relative_to(root).as_posix()] = path.read_bytes()
    return files


def check_publication_pages() -> int:
    with tempfile.TemporaryDirectory(prefix="cedis-publications-") as tmp:
        expected_dir = Path(tmp) / "publications"
        build_publication_pages(expected_dir)
        expected = snapshot(expected_dir)
        current = snapshot(OUT_DIR)

    missing = sorted(set(expected) - set(current))
    extra = sorted(set(current) - set(expected))
    changed = sorted(path for path in set(expected) & set(current) if expected[path] != current[path])

    if not missing and not extra and not changed:
        print("content/publications está sincronizado com data/productions.yaml.")
        return 0

    print("content/publications está divergente de data/productions.yaml.")
    for label, paths in (("faltando", missing), ("extra", extra), ("alterado", changed)):
        if paths:
            sample = ", ".join(paths[:10])
            suffix = "" if len(paths) <= 10 else f" ... (+{len(paths) - 10})"
            print(f"- {label}: {len(paths)} arquivo(s): {sample}{suffix}")
    print("Rode: python3 scripts/build_publications.py")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera ou valida content/publications/ a partir de data/productions.yaml.")
    parser.add_argument("--check", action="store_true", help="não escreve arquivos; falha se content/publications/ estiver desatualizado")
    args = parser.parse_args()

    if args.check:
        return check_publication_pages()

    generated = build_publication_pages(OUT_DIR)
    print(f"Geradas {generated} paginas de publicacao em {OUT_DIR.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
