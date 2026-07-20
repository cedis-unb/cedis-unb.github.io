#!/usr/bin/env python3
"""Valida paridade PT/EN e campos estruturais de i18n.

Foco da Fase 4/I08: garantir que paginas obrigatorias tenham par de idioma,
translationKey estavel e campos estruturais coerentes. O script evita comparar
conteudo textual livre, mas falha em lacunas que quebram navegacao, SEO ou
relacionamentos.
"""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
REPORT_PATH = os.environ.get("CEDIS_I18N_REPORT")

REQUIRED_TRANSLATION_KEYS = {
    "content/about",
    "content/history",
    "content/parceiros",
    "content/reconhecimentos",
    "content/infra",
    "content/indicadores",
    "content/contact",
    "content/imprensa",
    "content/privacy",
    "content/accessibility",
    "content/junte-se/_index",
    "content/opportunities/_index",
    "content/publications/_index",
}

STRUCTURAL_FIELDS = ("featured_image", "status", "id", "layout")
LANGS = {"pt", "en"}


class Issue:
    def __init__(self, severity: str, location: str, message: str) -> None:
        self.severity = severity
        self.location = location
        self.message = message

    def __str__(self) -> str:
        return f"[{self.severity.upper():<7}] {self.location} — {self.message}"


def parse_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    fm = yaml.safe_load(parts[1])
    return (fm if isinstance(fm, dict) else None), parts[2]


def base_key(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    rel = re.sub(r"\.(pt|en)\.md$", "", rel)
    return rel


def language_from_path(path: Path, fm: dict[str, Any]) -> str | None:
    lang = fm.get("language")
    if lang in LANGS:
        return str(lang)
    match = re.search(r"\.(pt|en)\.md$", path.name)
    return match.group(1) if match else None


def is_generated_publication(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return rel.startswith("content/publications/") and "_index." not in path.name


def write_report(issues: list[Issue]) -> None:
    if not REPORT_PATH:
        return
    path = Path(REPORT_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("# Relatório de paridade PT/EN\n\n")
        if not issues:
            f.write("Nenhuma lacuna encontrada.\n")
            return
        for issue in issues:
            f.write(f"- **{issue.severity}** · `{issue.location}` — {issue.message}\n")


def main() -> int:
    issues: list[Issue] = []
    pages: list[tuple[Path, dict[str, Any], str, str]] = []
    by_key: dict[str, dict[str, tuple[Path, dict[str, Any], str]]] = defaultdict(dict)
    by_translation_key: dict[str, dict[str, tuple[Path, dict[str, Any], str]]] = defaultdict(dict)

    for path in sorted(CONTENT_DIR.rglob("*.md")):
        if is_generated_publication(path):
            continue
        fm, body = parse_frontmatter(path)
        if fm is None:
            continue
        lang = language_from_path(path, fm)
        rel_key = base_key(path)
        if lang not in LANGS:
            issues.append(Issue("error", path.relative_to(ROOT).as_posix(), "idioma ausente ou inválido"))
            continue
        pages.append((path, fm, lang, body))
        by_key[rel_key][lang] = (path, fm, body)
        if fm.get("translationKey"):
            by_translation_key[str(fm["translationKey"])][lang] = (path, fm, body)

    for required in sorted(REQUIRED_TRANSLATION_KEYS):
        entries = by_key.get(required)
        if not entries:
            issues.append(Issue("error", required, "página institucional obrigatória ausente"))
            continue
        for lang in LANGS:
            if lang not in entries:
                issues.append(Issue("error", required, f"versão {lang} ausente"))
        for lang, (path, fm, _) in entries.items():
            if not fm.get("translationKey"):
                issues.append(Issue("error", path.relative_to(ROOT).as_posix(), "translationKey obrigatório ausente"))

    for key, langs in sorted(by_key.items()):
        if key.startswith("content/posts/editais/"):
            # editais legados permanecem como anexos em PT; oportunidades
            # estruturadas bilingues sao a fonte canonica da Fase 4.
            continue
        if set(langs.keys()) != LANGS:
            issues.append(Issue("error", key, f"par PT/EN incompleto: {sorted(langs.keys())}"))

    for key, langs in sorted(by_translation_key.items()):
        if set(langs.keys()) != LANGS:
            location = next(iter(langs.values()))[0].relative_to(ROOT).as_posix()
            issues.append(Issue("error", location, f"translationKey '{key}' sem par PT/EN completo"))
            continue
        pt_path, pt_fm, pt_body = langs["pt"]
        en_path, en_fm, en_body = langs["en"]
        for field in STRUCTURAL_FIELDS:
            if (pt_fm.get(field) or "") != (en_fm.get(field) or ""):
                issues.append(Issue("error", f"{pt_path.relative_to(ROOT)} / {en_path.relative_to(ROOT)}", f"campo estrutural divergente: {field}"))
        if re.search(r"\]\(/en/", pt_body):
            issues.append(Issue("error", pt_path.relative_to(ROOT).as_posix(), "link interno aponta para /en/ em página PT"))
        if re.search(r"\]\(/pt/", en_body):
            issues.append(Issue("error", en_path.relative_to(ROOT).as_posix(), "link interno aponta para /pt/ em página EN"))

    for issue in issues:
        print(issue)
    print()
    print(f"Total: {sum(1 for i in issues if i.severity == 'error')} erros.")
    write_report(issues)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
