#!/usr/bin/env python3
"""Cria o par PT/EN de uma Perspectiva (opinião técnica assinada).

Perspectivas são escritas numa língua só. O site exige par PT/EN para todo
.md em content/ (validate_i18n.py), e o seletor de idioma precisa de um
destino. Este script gera os dois arquivos de uma vez:

  - <slug>.<lang>.md        texto original, com corpo a preencher
  - <slug>.<outra>.md       stub: noindex, resumo na outra língua e o aviso
                            de idioma original (renderizado pelo template)

Uso:
  python3 scripts/new_perspectiva.py --slug ia-na-sala-de-aula \
      --title "O que aprendi usando IA na sala de aula" \
      --authors sergio_freitas,george_marsicano \
      --summary "Três semestres, dois erros e uma regra." \
      --title-other "What I learned using AI in the classroom" \
      --summary-other "Three semesters, two mistakes and one rule." \
      [--lang pt] [--areas ai,education] [--date 2026-11-05]

Depois: escreva o corpo do arquivo original e rode `npm test`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTION = ROOT / "content" / "perspectivas"
LANGS = ("pt", "en")
DEFAULT_IMAGE = "../assets/images/pages/media-CEDIS.webp"


def yaml_str(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def yaml_list(values: list[str]) -> str:
    if not values:
        return " []"
    return "\n" + "\n".join(f"- {v}" for v in values)


def frontmatter(*, title: str, date: str, lang: str, slug: str, orig: str,
                authors: list[str], areas: list[str], summary: str,
                stub: bool) -> str:
    lines = [
        "---",
        f"title: {yaml_str(title)}",
        f"date: {date}T09:00:00-03:00",
        "draft: false",
        f"language: {lang}",
        f"translationKey: perspectiva_{slug.replace('-', '_')}",
        f"original_language: {orig}",
        f"authors:{yaml_list(authors)}",
        f"areas:{yaml_list(areas)}",
        "related_ids: []",
        "tags: []",
        f"summary: {yaml_str(summary)}",
        f"featured_image: {yaml_str(DEFAULT_IMAGE)}",
    ]
    if stub:
        lines.append("noindex: true")
    lines.append("---")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", required=True, help="kebab-case, vira o nome do arquivo e a URL")
    ap.add_argument("--title", required=True, help="título no idioma original")
    ap.add_argument("--authors", required=True, help="slugs de pessoa separados por vírgula (ex.: sergio_freitas,george_marsicano)")
    ap.add_argument("--summary", required=True, help="resumo de 1-3 linhas no idioma original")
    ap.add_argument("--title-other", help="título na outra língua (default: igual ao original)")
    ap.add_argument("--summary-other", help="resumo na outra língua (default: igual ao original)")
    ap.add_argument("--lang", choices=LANGS, default="pt", help="idioma original (default pt)")
    ap.add_argument("--areas", default="", help="slugs de área separados por vírgula")
    ap.add_argument("--date", default=dt.date.today().isoformat(), help="YYYY-MM-DD (default hoje)")
    args = ap.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        print("erro: --slug deve ser kebab-case ASCII (ex.: ia-na-sala-de-aula)", file=sys.stderr)
        return 2
    authors = [a.strip() for a in args.authors.split(",") if a.strip()]
    areas = [a.strip() for a in args.areas.split(",") if a.strip()]
    for a in authors + areas:
        if not re.fullmatch(r"[a-z0-9_]+", a):
            print(f"erro: slug inválido '{a}' (use snake_case ASCII)", file=sys.stderr)
            return 2

    other = "en" if args.lang == "pt" else "pt"
    orig_path = SECTION / f"{args.slug}.{args.lang}.md"
    stub_path = SECTION / f"{args.slug}.{other}.md"
    for p in (orig_path, stub_path):
        if p.exists():
            print(f"erro: {p.relative_to(ROOT)} já existe; não sobrescrevo", file=sys.stderr)
            return 1

    SECTION.mkdir(parents=True, exist_ok=True)
    common = dict(date=args.date, slug=args.slug, orig=args.lang, authors=authors, areas=areas)
    orig_path.write_text(
        frontmatter(title=args.title, lang=args.lang, summary=args.summary, stub=False, **common)
        + "\n<!-- Escreva o texto aqui. Headings a partir de ## . -->\n",
        encoding="utf-8",
    )
    stub_path.write_text(
        frontmatter(title=args.title_other or args.title, lang=other,
                    summary=args.summary_other or args.summary, stub=True, **common)
        + "\n" + (args.summary_other or args.summary) + "\n",
        encoding="utf-8",
    )
    print(f"criado: {orig_path.relative_to(ROOT)}  (original — escreva o corpo)")
    print(f"criado: {stub_path.relative_to(ROOT)}  (stub {other}, noindex)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
