#!/usr/bin/env python3
"""Diagnóstico read-only das 5 fontes de registro de pessoas do CEDIS.

Referência: análise arquitetural do registro de colaboradores (passo 1 do
roadmap de unificação). Este script NÃO altera nenhum arquivo — apenas
inspeciona e emite relatório.

Fontes analisadas:
  1. content/people/*.md com profile_level: researcher|advisor_only
     — docentes CEDIS + advisors externos (13 esperados)
     [antes do Gap #1 vinha de data/advisors.yaml]
  2. content/people/*.md          — perfis "full" (7-8 esperados)
  3. content/people/collaborators/*.md — perfis "médios" (10 esperados)
  4. data/people.yaml             — orientações (~237 entradas)
  5. data/productions.yaml        — authors[] livres e tags[] com slugs

Detecta:
  - Slugs duplicados entre fontes (mesmo slug em advisors + .md + people.yaml)
  - Entradas em people.yaml que também têm .md individual (candidatos a
    consolidação/deduplicação)
  - Slugs órfãos usados em tags[] de productions.yaml sem nenhum registro
    correspondente
  - Nomes livres em authors[] de productions.yaml sem alias registrado
  - Colisões potenciais por similaridade de nome (ex.: Milena vs Mylena)
  - Pessoas com múltiplas entradas em people.yaml (uma por orientação —
    candidatas a merge com sub-array supervisions[])

Uso:
    python3 scripts/normalize_people_slugs.py                # stdout
    python3 scripts/normalize_people_slugs.py --report FILE  # + markdown

Sem efeito colateral: read-only por design.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("ERRO: PyYAML não instalado. Rode 'pip install pyyaml'.", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
CONTENT_PEOPLE = REPO_ROOT / "content" / "people"


# ---------- helpers ----------

def slugify(name: str) -> str:
    """Slug canônico: sem acento, minúsculo, underscore, sem stopwords comuns."""
    n = unicodedata.normalize("NFKD", name)
    n = "".join(c for c in n if not unicodedata.combining(c))
    n = n.lower()
    n = re.sub(r"[^a-z0-9]+", "_", n).strip("_")
    return n


PARTICLES = {"de", "da", "do", "das", "dos", "e", "del", "della", "van", "von"}


def _strip_accents(s: str) -> str:
    n = unicodedata.normalize("NFKD", s)
    return "".join(c for c in n if not unicodedata.combining(c))


def canonicalize_author(name: str) -> str:
    """Normaliza um nome livre de autor (ABNT ou natural) para comparação.

    'LACERDA, A. R. T.' -> 'a r t lacerda'
    'Sergio Antônio Andrade de Freitas' -> 'sergio antonio andrade de freitas'
    """
    n = _strip_accents(name).lower()
    # Formato ABNT "SOBRENOME, INICIAIS" -> reverte
    if "," in n:
        parts = [p.strip() for p in n.split(",")]
        if len(parts) == 2:
            n = f"{parts[1]} {parts[0]}"
    n = re.sub(r"[^a-z0-9\s]+", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    return n


def abnt_forms(full_name: str) -> set[str]:
    """Gera formas ABNT canônicas de um nome completo — para servirem como aliases.

    'Sergio Antônio Andrade de Freitas' produz:
      {'s a a freitas', 's a a de freitas', 'sergio a a freitas', ...}

    Retorna sempre em formato canonicalizado (minúsculas, sem acento,
    espaços simples), pronto para servir de chave em known_name_map.
    """
    if not full_name:
        return set()
    # Se vier em ABNT ('SOBRENOME, INICIAIS/NOMES'), reverte primeiro
    # para que a ordem natural seja preservada nas formas geradas.
    n = _strip_accents(full_name).lower()
    if "," in n:
        parts = [p.strip() for p in n.split(",")]
        if len(parts) == 2:
            n = f"{parts[1]} {parts[0]}"
    n = re.sub(r"[^a-z\s]+", " ", n)
    parts = [p for p in n.split() if p]
    if len(parts) < 2:
        return set()

    # separa "particles" (de/da/do/dos/etc) — mas iniciais de 1 letra
    # nunca são particles (evita filtrar 'e' de 'Edna D.' erroneamente)
    core_parts = [p for p in parts if len(p) == 1 or p not in PARTICLES]
    if len(core_parts) < 2:
        return set()

    last = core_parts[-1]
    given = core_parts[:-1]  # nomes/sobrenomes intermediários exceto o último

    forms = set()
    # forma canônica natural completa
    forms.add(canonicalize_author(full_name))

    # ABNT: iniciais separadas por espaço + sobrenome
    initials = " ".join(g[0] for g in given)
    forms.add(f"{initials} {last}".strip())

    # Variante: primeiro nome cheio + iniciais dos meios + sobrenome
    if len(given) >= 2:
        first = given[0]
        mids = " ".join(g[0] for g in given[1:])
        forms.add(f"{first} {mids} {last}".strip())

    # Variante: só o primeiro + último (comum em citações informais)
    forms.add(f"{given[0]} {last}")

    # Variante sem "de/da/do" mesmo tendo particles no meio
    return {re.sub(r"\s+", " ", f).strip() for f in forms if f}


def similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


# ---------- loaders ----------

def load_advisors() -> dict:
    """Retorna dict {slug: {name}} para pessoas com profile_level de
    docente/advisor externo. Substitui a leitura de data/advisors.yaml
    que foi removido no Gap #1 (2026-07-24).

    Formato mantido igual ao antigo advisors.yaml pra retrocompat com o
    restante do script (só usa .keys() e .name)."""
    out = {}
    for md in CONTENT_PEOPLE.glob("*.pt.md"):
        m = re.match(r"^([a-zA-Z0-9_\-]+)\.pt\.md$", md.name)
        if not m or m.group(1) == "all":
            continue
        slug = m.group(1)
        try:
            text = md.read_text(encoding="utf-8")
            fmm = re.match(r"^---\n(.*?)\n---", text, re.S)
            if not fmm:
                continue
            fm = yaml.safe_load(fmm.group(1)) or {}
        except Exception:
            continue
        level = fm.get("profile_level", "")
        if level not in ("researcher", "advisor_only"):
            continue
        out[slug] = {"name": fm.get("title", "")}
    return out


def load_people_yaml() -> list:
    with open(DATA_DIR / "people.yaml") as f:
        data = yaml.safe_load(f)
    return data.get("people", []) or []


def load_productions() -> list:
    with open(DATA_DIR / "productions.yaml") as f:
        data = yaml.safe_load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        # tenta detectar a única lista principal
        for v in data.values():
            if isinstance(v, list):
                return v
    return []


def load_person_md_files() -> dict:
    """Retorna {slug: {path, lang, frontmatter}} para content/people/*.md
    e content/people/collaborators/*.md."""
    out = {}
    for base in ("", "collaborators"):
        folder = CONTENT_PEOPLE / base if base else CONTENT_PEOPLE
        if not folder.exists():
            continue
        for md in folder.glob("*.md"):
            fname = md.name
            if fname.startswith("_") or fname.startswith("all"):
                continue
            # pattern: <slug>.<lang>.md
            m = re.match(r"^([a-zA-Z0-9_\-]+)\.(pt|en)\.md$", fname)
            if not m:
                continue
            slug, lang = m.group(1), m.group(2)
            try:
                text = md.read_text(encoding="utf-8")
            except Exception:
                continue
            fm = {}
            fmm = re.match(r"^---\n(.*?)\n---", text, re.S)
            if fmm:
                try:
                    fm = yaml.safe_load(fmm.group(1)) or {}
                except Exception:
                    fm = {}
            entry = out.setdefault(slug, {"languages": {}, "location": base or "root"})
            entry["languages"][lang] = {"path": str(md.relative_to(REPO_ROOT)), "frontmatter": fm}
    return out


# ---------- analyses ----------

def analyze():
    advisors = load_advisors()
    people_yaml = load_people_yaml()
    productions = load_productions()
    md_pages = load_person_md_files()

    # ---- Índice unificado slug -> [fontes] ----
    sources_by_slug = defaultdict(list)  # slug -> [(source, extra)]

    for slug, info in advisors.items():
        sources_by_slug[slug].append(("advisors.yaml", info.get("name", "")))

    for slug, info in md_pages.items():
        langs = ",".join(sorted(info["languages"].keys()))
        loc = info["location"]
        # tenta título de qualquer idioma disponível
        title = ""
        for lang in ("pt", "en"):
            if lang in info["languages"]:
                fm = info["languages"][lang]["frontmatter"]
                title = fm.get("title", "") or title
                if title:
                    break
        sources_by_slug[slug].append((f"content/people/{loc}", f"{title} [{langs}]"))

    people_yaml_by_slug = defaultdict(list)
    for i, p in enumerate(people_yaml):
        name = p.get("name", "")
        if not name:
            continue
        s = slugify(name)
        people_yaml_by_slug[s].append((i, p))

    for slug, entries in people_yaml_by_slug.items():
        names_seen = sorted({e[1].get("name", "") for e in entries})
        sources_by_slug[slug].append((
            f"data/people.yaml ({len(entries)}×)",
            " | ".join(names_seen),
        ))

    # ---- Análise 1: slugs em múltiplas fontes ----
    multi_source = {s: srcs for s, srcs in sources_by_slug.items() if len(srcs) > 1}

    # ---- Análise 2: entradas em people.yaml que têm .md ----
    overlap_yaml_md = {}
    for slug in people_yaml_by_slug:
        if slug in md_pages:
            overlap_yaml_md[slug] = {
                "yaml_count": len(people_yaml_by_slug[slug]),
                "yaml_indices": [e[0] for e in people_yaml_by_slug[slug]],
                "md_location": md_pages[slug]["location"],
                "md_langs": sorted(md_pages[slug]["languages"].keys()),
            }

    # ---- Análise 3: pessoas com >1 entrada em people.yaml ----
    duplicated_in_yaml = {
        slug: len(entries) for slug, entries in people_yaml_by_slug.items() if len(entries) > 1
    }

    # ---- Análise 4: slugs em tags[] de productions sem registro ----
    known_slugs = set(advisors.keys()) | set(md_pages.keys()) | set(people_yaml_by_slug.keys())
    tag_slug_counter = Counter()
    for item in productions:
        if not isinstance(item, dict):
            continue
        for t in (item.get("tags") or []):
            tag_slug_counter[t] += 1

    # Heurística: slug com prefixo típico de pessoa (nome_sobrenome, sem "project_")
    # e não é um tópico conhecido. Filtramos slugs que parecem ser pessoa mas não têm registro.
    def looks_like_person(slug: str) -> bool:
        if slug.startswith("project_"):
            return False
        parts = slug.split("_")
        if len(parts) < 2:
            return False
        # tópicos conhecidos multi-word que NÃO são pessoas
        NON_PERSON_MULTI = {
            "active_learning", "digital_transformation", "learning_analytics",
            "machine_learning", "green_software", "social_software", "soft_skills",
            "software_architecture", "software_development_tools", "software_product_line",
            "software_products", "software_quality", "software_requirements",
            "verification_validation_testing", "scientific_initiation", "master_student",
            "phd_candidate",
        }
        if slug in NON_PERSON_MULTI:
            return False
        return True

    orphan_tag_slugs = {
        s: c for s, c in tag_slug_counter.items()
        if looks_like_person(s) and s not in known_slugs
    }

    # ---- Análise 5: nomes livres em authors[] sem correspondência ----
    known_name_map = {}  # canonical -> slug
    def register_name(slug, name):
        if not name:
            return
        c = canonicalize_author(name)
        if c and c not in known_name_map:
            known_name_map[c] = slug
        # também registra formas ABNT alternativas — resolve automaticamente
        # variações "FREITAS, S. A. A." → sergio_freitas
        for alt in abnt_forms(name):
            if alt and alt not in known_name_map:
                known_name_map[alt] = slug

    for slug, info in advisors.items():
        register_name(slug, info.get("name", ""))
    for slug, info in md_pages.items():
        for lang in ("pt", "en"):
            if lang in info["languages"]:
                fm = info["languages"][lang]["frontmatter"]
                register_name(slug, fm.get("title", ""))
    for slug, entries in people_yaml_by_slug.items():
        for _, p in entries:
            register_name(slug, p.get("name", ""))

    author_appearances = Counter()  # canonical -> count
    author_originals = defaultdict(set)  # canonical -> {original strings}
    for item in productions:
        if not isinstance(item, dict):
            continue
        for a in (item.get("authors") or []):
            c = canonicalize_author(a)
            if not c:
                continue
            author_appearances[c] += 1
            author_originals[c].add(a)

    unregistered_authors = {}  # canonical -> {count, samples}
    matched_via_alias = {}
    for canonical, count in author_appearances.items():
        matched_slug = known_name_map.get(canonical)

        # Se não bateu direto, tenta expandir o nome do AUTOR em suas formas
        # ABNT — resolve casos onde o registrado é uma forma curta
        # ("Edna Canedo") e o autor cita a forma longa ("Edna Dias Canedo").
        if not matched_slug:
            sample_original = next(iter(author_originals[canonical]))
            for alt in abnt_forms(sample_original):
                if alt in known_name_map:
                    matched_slug = known_name_map[alt]
                    break

        if matched_slug:
            matched_via_alias[canonical] = {
                "slug": matched_slug,
                "count": count,
                "samples": sorted(author_originals[canonical]),
            }
            continue
        unregistered_authors[canonical] = {
            "count": count,
            "samples": sorted(author_originals[canonical]),
        }

    # ---- Análise 6: possíveis colisões de nome (similaridade > 0.85) ----
    similar_pairs = []
    slugs_list = sorted(known_slugs)
    for i, a in enumerate(slugs_list):
        for b in slugs_list[i + 1:]:
            if abs(len(a) - len(b)) > 4:
                continue
            r = similar(a, b)
            if r >= 0.85 and a != b:
                similar_pairs.append((a, b, r))

    # ---- Análise 7: possíveis colisões de nome nos autores livres ----
    author_similar = []
    canonicals = list(author_appearances.keys())
    known_canonicals = list(known_name_map.keys())
    checked = set()
    for a in canonicals:
        for b in known_canonicals:
            if a == b:
                continue
            key = (a, b) if a < b else (b, a)
            if key in checked:
                continue
            checked.add(key)
            if abs(len(a) - len(b)) > 6:
                continue
            r = similar(a, b)
            if r >= 0.88:
                author_similar.append((a, b, r, known_name_map[b]))

    return {
        "counts": {
            "advisors": len(advisors),
            "md_pages": len(md_pages),
            "md_root": sum(1 for p in md_pages.values() if p["location"] == "root"),
            "md_collaborators": sum(1 for p in md_pages.values() if p["location"] == "collaborators"),
            "people_yaml_entries": len(people_yaml),
            "people_yaml_unique_slugs": len(people_yaml_by_slug),
            "productions": len(productions),
            "unique_author_names": len(author_appearances),
            "registered_via_alias": len(matched_via_alias),
            "unregistered_authors": len(unregistered_authors),
            "tag_slugs_total": len(tag_slug_counter),
            "orphan_tag_slugs": len(orphan_tag_slugs),
        },
        "multi_source": multi_source,
        "overlap_yaml_md": overlap_yaml_md,
        "duplicated_in_yaml": duplicated_in_yaml,
        "orphan_tag_slugs": orphan_tag_slugs,
        "unregistered_authors": unregistered_authors,
        "similar_pairs": similar_pairs,
        "author_similar": author_similar,
        "matched_via_alias_sample": dict(list(matched_via_alias.items())[:20]),
    }


# ---------- report ----------

def emit_console(result: dict) -> None:
    c = result["counts"]
    print("=" * 78)
    print("DIAGNÓSTICO: registro de pessoas / colaboradores CEDIS")
    print("=" * 78)
    print()
    print(f"Fontes:")
    print(f"  advisors.yaml               : {c['advisors']} orientadores")
    print(f"  content/people/*.md         : {c['md_root']} páginas (root)")
    print(f"  content/people/collab*.md   : {c['md_collaborators']} páginas (collaborators)")
    print(f"  data/people.yaml            : {c['people_yaml_entries']} entradas "
          f"({c['people_yaml_unique_slugs']} slugs únicos)")
    print(f"  data/productions.yaml       : {c['productions']} itens")
    print(f"  nomes únicos em authors[]   : {c['unique_author_names']}")
    print(f"    ├─ com alias registrado   : {c['registered_via_alias']}")
    print(f"    └─ ÓRFÃOS (sem registro)  : {c['unregistered_authors']}")
    print(f"  slugs em tags[] total       : {c['tag_slugs_total']}")
    print(f"    └─ ÓRFÃOS parecem pessoa  : {c['orphan_tag_slugs']}")
    print()

    print("-" * 78)
    print("1) Slugs em MÚLTIPLAS fontes (candidatos a consolidação)")
    print("-" * 78)
    if not result["multi_source"]:
        print("  (nenhum)")
    else:
        for slug in sorted(result["multi_source"].keys()):
            srcs = result["multi_source"][slug]
            print(f"\n  {slug}:")
            for source, extra in srcs:
                print(f"      • {source:38s} → {extra}")

    print()
    print("-" * 78)
    print("2) Entradas em data/people.yaml que TÊM .md individual")
    print("-" * 78)
    if not result["overlap_yaml_md"]:
        print("  (nenhum)")
    else:
        for slug, info in sorted(result["overlap_yaml_md"].items()):
            print(f"  {slug:24s}  yaml×{info['yaml_count']} at rows "
                  f"{info['yaml_indices']}  |  .md em {info['md_location']} "
                  f"({','.join(info['md_langs'])})")

    print()
    print("-" * 78)
    print("3) Pessoas com >1 entrada em data/people.yaml (candidatas a merge)")
    print("-" * 78)
    if not result["duplicated_in_yaml"]:
        print("  (nenhuma)")
    else:
        for slug, n in sorted(result["duplicated_in_yaml"].items(), key=lambda x: -x[1]):
            print(f"  {slug:32s}  {n}× entradas")

    print()
    print("-" * 78)
    print("4) Slugs em tags[] de productions.yaml que parecem pessoa mas SEM registro")
    print("-" * 78)
    if not result["orphan_tag_slugs"]:
        print("  (nenhum)")
    else:
        for slug, count in sorted(result["orphan_tag_slugs"].items(), key=lambda x: -x[1]):
            print(f"  {slug:32s}  aparece em {count} produção(ões)")

    print()
    print("-" * 78)
    print("5) Colisões similares entre slugs conhecidos (ratio ≥ 0.85)")
    print("-" * 78)
    if not result["similar_pairs"]:
        print("  (nenhuma)")
    else:
        for a, b, r in sorted(result["similar_pairs"], key=lambda x: -x[2]):
            print(f"  {a:28s}  ~  {b:28s}  ratio={r:.2f}")

    print()
    print("-" * 78)
    print("6) Nomes em authors[] próximos de slug conhecido (ratio ≥ 0.88)")
    print("     Podem indicar variação de escrita → adicionar como alias")
    print("-" * 78)
    if not result["author_similar"]:
        print("  (nenhum)")
    else:
        for a, b, r, slug in sorted(result["author_similar"], key=lambda x: -x[2])[:40]:
            print(f"  \"{a}\" ~ \"{b}\" [slug={slug}] ratio={r:.2f}")

    print()
    print("-" * 78)
    print(f"7) Autores em productions.yaml ÓRFÃOS (sem match direto) — top 40 por freq")
    print("-" * 78)
    orphans = sorted(result["unregistered_authors"].items(), key=lambda x: -x[1]["count"])
    if not orphans:
        print("  (nenhum)")
    else:
        for canonical, info in orphans[:40]:
            samples = list(info["samples"])[:2]
            sample_str = " | ".join(samples)
            if len(info["samples"]) > 2:
                sample_str += f"  (+{len(info['samples']) - 2} variações)"
            print(f"  {info['count']:3d}× {sample_str}")
        if len(orphans) > 40:
            print(f"  ... e mais {len(orphans) - 40} nomes órfãos")

    print()
    print("=" * 78)
    print("FIM — este relatório é read-only. Nenhum arquivo foi alterado.")
    print("=" * 78)


def emit_markdown(result: dict, path: Path) -> None:
    lines = []
    c = result["counts"]
    lines.append("# Diagnóstico: registro de pessoas / colaboradores CEDIS\n")
    lines.append("> Gerado por `scripts/normalize_people_slugs.py` (read-only).\n")
    lines.append("\n## Contagens gerais\n\n")
    lines.append("| Fonte | Valor |\n|---|---:|\n")
    lines.append(f"| `data/advisors.yaml` | {c['advisors']} orientadores |\n")
    lines.append(f"| `content/people/*.md` | {c['md_root']} páginas |\n")
    lines.append(f"| `content/people/collaborators/*.md` | {c['md_collaborators']} páginas |\n")
    lines.append(f"| `data/people.yaml` (entradas) | {c['people_yaml_entries']} |\n")
    lines.append(f"| `data/people.yaml` (slugs únicos) | {c['people_yaml_unique_slugs']} |\n")
    lines.append(f"| `data/productions.yaml` (itens) | {c['productions']} |\n")
    lines.append(f"| Nomes únicos em `authors[]` | {c['unique_author_names']} |\n")
    lines.append(f"| — com alias registrado | {c['registered_via_alias']} |\n")
    lines.append(f"| — órfãos (sem registro) | **{c['unregistered_authors']}** |\n")
    lines.append(f"| Slugs em `tags[]` total | {c['tag_slugs_total']} |\n")
    lines.append(f"| — órfãos parecendo pessoa | **{c['orphan_tag_slugs']}** |\n")

    def section(title, body):
        lines.append(f"\n## {title}\n\n")
        lines.append(body)

    # 1
    body = ""
    if not result["multi_source"]:
        body = "_(nenhum)_\n"
    else:
        for slug in sorted(result["multi_source"].keys()):
            body += f"\n### `{slug}`\n\n"
            for src, extra in result["multi_source"][slug]:
                body += f"- **{src}** → {extra}\n"
    section("1. Slugs em múltiplas fontes", body)

    # 2
    body = ""
    if not result["overlap_yaml_md"]:
        body = "_(nenhum)_\n"
    else:
        body = "| Slug | Entradas em people.yaml | Linhas | Localização .md | Idiomas |\n"
        body += "|---|---:|---|---|---|\n"
        for slug, info in sorted(result["overlap_yaml_md"].items()):
            body += (
                f"| `{slug}` | {info['yaml_count']} | "
                f"{info['yaml_indices']} | {info['md_location']} | "
                f"{', '.join(info['md_langs'])} |\n"
            )
    section("2. Entradas em people.yaml que também têm .md individual", body)

    # 3
    body = ""
    if not result["duplicated_in_yaml"]:
        body = "_(nenhuma)_\n"
    else:
        body = "| Slug | Nº entradas |\n|---|---:|\n"
        for slug, n in sorted(result["duplicated_in_yaml"].items(), key=lambda x: -x[1]):
            body += f"| `{slug}` | {n} |\n"
    section("3. Pessoas com múltiplas entradas em people.yaml", body)

    # 4
    body = ""
    if not result["orphan_tag_slugs"]:
        body = "_(nenhum)_\n"
    else:
        body = "| Slug | Produções que o usam |\n|---|---:|\n"
        for slug, count in sorted(result["orphan_tag_slugs"].items(), key=lambda x: -x[1]):
            body += f"| `{slug}` | {count} |\n"
    section("4. Slugs órfãos em tags[] de productions.yaml", body)

    # 5
    body = ""
    if not result["similar_pairs"]:
        body = "_(nenhuma)_\n"
    else:
        body = "| Slug A | Slug B | Ratio |\n|---|---|---:|\n"
        for a, b, r in sorted(result["similar_pairs"], key=lambda x: -x[2]):
            body += f"| `{a}` | `{b}` | {r:.2f} |\n"
    section("5. Colisões similares entre slugs conhecidos", body)

    # 6
    body = ""
    if not result["author_similar"]:
        body = "_(nenhum)_\n"
    else:
        body = "| Nome (authors) | Nome registrado | Slug alvo | Ratio |\n|---|---|---|---:|\n"
        for a, b, r, slug in sorted(result["author_similar"], key=lambda x: -x[2])[:40]:
            body += f"| {a} | {b} | `{slug}` | {r:.2f} |\n"
    section("6. Nomes livres próximos de slug conhecido (candidatos a alias)", body)

    # 7
    body = ""
    orphans = sorted(result["unregistered_authors"].items(), key=lambda x: -x[1]["count"])
    if not orphans:
        body = "_(nenhum)_\n"
    else:
        body = "| Freq | Amostra de escrita |\n|---:|---|\n"
        for canonical, info in orphans[:60]:
            samples = list(info["samples"])[:2]
            s = " / ".join(samples)
            if len(info["samples"]) > 2:
                s += f" _(+{len(info['samples']) - 2} variações)_"
            body += f"| {info['count']} | {s} |\n"
        if len(orphans) > 60:
            body += f"\n_… e mais {len(orphans) - 60} autores órfãos_\n"
    section("7. Autores em productions.yaml sem registro (top 60)", body)

    path.write_text("".join(lines), encoding="utf-8")


# ---------- main ----------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--report", type=str, help="Caminho para salvar relatório Markdown")
    args = ap.parse_args()

    result = analyze()
    emit_console(result)

    if args.report:
        path = Path(args.report)
        emit_markdown(result, path)
        print(f"\n📝 Relatório Markdown salvo em: {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
