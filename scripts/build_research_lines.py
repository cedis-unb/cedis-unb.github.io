#!/usr/bin/env python3
"""Gera content/research-lines/<slug>.<lang>.md a partir de data/research_lines.yaml.

Mesmo padrão de scripts/build_defesas.py e build_publications.py:
    - 1 arquivo MD por (linha × idioma) com frontmatter mínimo;
    - body vazio — layouts/research-lines/single.html renderiza tudo lendo
      site.Data.research_lines via partial research-line-index;
    - `draft: true` para linhas com status `draft`, o que tira a página do
      build, do sitemap, da busca e das coleções do Hugo; `active` e
      `archived` são renderizadas (arquivada recebe selo no layout);
    - _index.<lang>.md recebe `build.render: never` + `build.list: never`
      enquanto não houver nenhuma linha active, para que a seção não
      exista publicamente antes da primeira linha promovida.

Pré-visualização local de rascunhos (nunca commitar stubs nesse estado):
    HUGO_CEDIS_PREVIEW_LINES=1 python3 scripts/build_research_lines.py
    hugo server ...               # ou: npm run start:lines-preview
    Nesse modo os rascunhos saem com draft: false e o _index carrega
    `research_lines_preview: true`, que os templates usam para exibi-los com
    selo "Rascunho". `--check` (npm test) acusa "divergente" até rodar o
    build sem a variável.

Uso:
    python3 scripts/build_research_lines.py            # gera content/research-lines/
    python3 scripts/build_research_lines.py --check    # falha se dessincronizado
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "research_lines.yaml"
OUT_DIR = ROOT / "content" / "research-lines"
LANGS = ("pt", "en")
STATUSES = ("draft", "active", "archived")
PREVIEW = os.environ.get("HUGO_CEDIS_PREVIEW_LINES") == "1"


def _load() -> tuple[dict, list[dict]]:
    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise SystemExit(f"{DATA_PATH}: esperava mapeamento raiz com 'research_lines'")
    lines = data.get("research_lines") or []
    if not isinstance(lines, list):
        raise SystemExit(f"{DATA_PATH}: 'research_lines' deve ser lista")
    for entry in lines:
        for key in ("id", "slug", "status", "name"):
            if key not in entry:
                raise SystemExit(f"{DATA_PATH}: linha sem campo obrigatório '{key}': {entry}")
        if entry["status"] not in STATUSES:
            raise SystemExit(f"{DATA_PATH}::{entry['id']}: status inválido '{entry['status']}'")
    return data.get("section") or {}, lines


def _localized(value: object, lang: str, fallback: str) -> str:
    if isinstance(value, dict):
        text = value.get(lang) or value.get("pt") or value.get("en") or fallback
    else:
        text = value or fallback
    return str(text).replace('"', '\\"')


def _frontmatter(entry: dict, lang: str) -> str:
    title = _localized(entry.get("name"), lang, entry["id"])
    summary = _localized(entry.get("summary"), lang, "")
    is_draft = entry["status"] == "draft"
    lines: list[str] = ["---"]
    lines.append(f'title: "{title}"')
    # Data fixa: a ordenação e a exibição vêm do YAML, não do frontmatter.
    lines.append("date: 1970-01-01T00:00:00Z")
    lines.append(f"draft: {'true' if (is_draft and not PREVIEW) else 'false'}")
    lines.append(f"language: {lang}")
    lines.append(f'translationKey: "{entry["id"]}"')
    lines.append(f'id: "{entry["id"]}"')
    lines.append(f"research_line_status: {entry['status']}")
    lines.append("generated_by: scripts/build_research_lines.py")
    lines.append("canonical_source: data/research_lines.yaml")
    if summary:
        lines.append(f'summary: "{summary}"')
        lines.append(f'description: "{summary}"')
    lines.append("---")
    return "\n".join(lines) + "\n"


def _index_frontmatter(section: dict, lang: str, has_active: bool) -> str:
    title = _localized(section.get("title"), lang, "Research lines" if lang == "en" else "Linhas de pesquisa")
    description = _localized(section.get("description"), lang, "")
    lines: list[str] = ["---"]
    lines.append(f'title: "{title}"')
    lines.append("date: 1970-01-01T00:00:00Z")
    lines.append(f"language: {lang}")
    lines.append('translationKey: "research-lines-index"')
    lines.append("generated_by: scripts/build_research_lines.py")
    lines.append("canonical_source: data/research_lines.yaml")
    if description:
        lines.append(f'description: "{description}"')
    if PREVIEW:
        # Pré-visualização local: os templates leem este param para incluir
        # rascunhos (com selo). Nunca chega à produção: --check acusa divergência.
        lines.append("research_lines_preview: true")
    elif not has_active:
        # Sem linha ativa a seção não é renderizada nem listada (sitemap, RSS).
        lines.append("build:")
        lines.append("  render: never")
        lines.append("  list: never")
    lines.append("---")
    return "\n".join(lines) + "\n"


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8")


def build(out_dir: Path) -> tuple[int, int]:
    section, entries = _load()
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    has_active = any(e["status"] == "active" for e in entries)
    for lang in LANGS:
        _write(out_dir / f"_index.{lang}.md", _index_frontmatter(section, lang, has_active))

    count = 0
    slugs: set[str] = set()
    for entry in entries:
        slug = entry["slug"]
        if slug in slugs:
            raise SystemExit(f"{DATA_PATH}: slug duplicado '{slug}'")
        slugs.add(slug)
        for lang in LANGS:
            _write(out_dir / f"{slug}.{lang}.md", _frontmatter(entry, lang))
            count += 1
    active = sum(1 for e in entries if e["status"] == "active")
    return count, active


def _snapshot(root: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    if not root.exists():
        return files
    for p in sorted(root.rglob("*")):
        if p.is_file():
            files[p.relative_to(root).as_posix()] = p.read_bytes()
    return files


def check() -> int:
    with tempfile.TemporaryDirectory(prefix="cedis-research-lines-") as tmp:
        expected = Path(tmp) / "research-lines"
        build(expected)
        exp = _snapshot(expected)
        cur = _snapshot(OUT_DIR)
    missing = sorted(set(exp) - set(cur))
    extra = sorted(set(cur) - set(exp))
    changed = sorted(p for p in set(exp) & set(cur) if exp[p] != cur[p])
    if not (missing or extra or changed):
        print("content/research-lines está sincronizado com data/research_lines.yaml.")
        return 0
    print("content/research-lines está divergente de data/research_lines.yaml.")
    for label, paths in (("faltando", missing), ("extra", extra), ("alterado", changed)):
        if paths:
            sample = ", ".join(paths[:6])
            suffix = "" if len(paths) <= 6 else f" ... (+{len(paths) - 6})"
            print(f"- {label}: {len(paths)} arquivo(s): {sample}{suffix}")
    print("Rode: python3 scripts/build_research_lines.py")
    return 1


def _cli() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--check", action="store_true", help="não escreve, só compara")
    args = ap.parse_args()
    if args.check:
        return check()
    n, active = build(OUT_DIR)
    suffix = " [PRÉ-VISUALIZAÇÃO: não commitar; rode de novo sem HUGO_CEDIS_PREVIEW_LINES]" if PREVIEW else ""
    print(f"Geradas {n} páginas de linha de pesquisa em {OUT_DIR} ({active} ativa(s)).{suffix}")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
