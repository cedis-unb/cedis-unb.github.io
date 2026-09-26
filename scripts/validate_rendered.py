#!/usr/bin/env python3
"""Validate invariants in generated HTML output."""

from __future__ import annotations

import json
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


class BreadcrumbParser(HTMLParser):
    """Extract visible breadcrumb labels from rendered HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.items: list[str] = []
        self._in_breadcrumb_nav = False
        self._in_item = False
        self._skip_item = False
        self._capture_text = False
        self._text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        if tag == "nav" and attr_map.get("aria-label") in {"Breadcrumb", "Trilha de navegação"}:
            self._in_breadcrumb_nav = True
            return
        if not self._in_breadcrumb_nav:
            return
        if tag == "li":
            self._in_item = True
            self._skip_item = attr_map.get("aria-hidden") == "true"
            self._text_parts = []
            return
        if self._in_item and not self._skip_item and tag in {"a", "span"}:
            self._capture_text = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "nav" and self._in_breadcrumb_nav:
            self._in_breadcrumb_nav = False
            return
        if not self._in_breadcrumb_nav:
            return
        if tag in {"a", "span"}:
            self._capture_text = False
            return
        if tag == "li" and self._in_item:
            if not self._skip_item:
                label = normalize_label("".join(self._text_parts))
                if label:
                    self.items.append(label)
            self._in_item = False
            self._skip_item = False
            self._capture_text = False
            self._text_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_breadcrumb_nav and self._in_item and not self._skip_item and self._capture_text:
            self._text_parts.append(data)


def normalize_label(value: str) -> str:
    return " ".join(unescape(value).split()).strip()


def read_text(root: Path, relative_path: str, issues: list[str]) -> str:
    path = root / relative_path
    if not path.is_file():
        issues.append(f"missing generated file: {relative_path}")
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def require_contains(text: str, needle: str, relative_path: str, issues: list[str]) -> None:
    if needle not in text:
        issues.append(f"{relative_path}: expected to find '{needle}'")


def require_any(
    text: str,
    needles: tuple[str, ...],
    relative_path: str,
    label: str,
    issues: list[str],
) -> None:
    if not any(needle in text for needle in needles):
        options = " | ".join(needles)
        issues.append(f"{relative_path}: expected {label} ({options})")


def validate_opportunities(root: Path, issues: list[str]) -> None:
    checks = (
        (
            "pt/oportunidades/index.html",
            "Oportunidades abertas",
            "Arquivo",
            "Não há oportunidades abertas no momento.",
        ),
        (
            "opportunities/index.html",
            "Open opportunities",
            "Archive",
            "There are no open opportunities at the moment.",
        ),
    )

    for relative_path, open_heading, archive_heading, empty_state in checks:
        text = read_text(root, relative_path, issues)
        if not text:
            continue
        require_contains(text, open_heading, relative_path, issues)
        require_contains(text, archive_heading, relative_path, issues)
        require_any(
            text,
            (empty_state, 'data-opportunity-card="true"'),
            relative_path,
            "an empty state or at least one rendered opportunity card",
            issues,
        )


def validate_researcher_cards(root: Path, issues: list[str]) -> None:
    for relative_path in (
        "categories/researcher/index.html",
        "pt/categories/researcher/index.html",
    ):
        text = read_text(root, relative_path, issues)
        if not text:
            continue
        if "min read" in text or "min de leitura" in text:
            issues.append(f"{relative_path}: researcher listing must not expose reading-time metadata")


def validate_aria_controls(root: Path, issues: list[str]) -> None:
    for html_path in root.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="replace")
        controls = re.findall(r'\baria-controls="([^"]+)"', text)
        if not controls:
            continue
        ids = set(re.findall(r'\bid="([^"]+)"', text))
        for control_id in controls:
            if control_id not in ids:
                issues.append(f"{html_path.relative_to(root)}: aria-controls references missing id '{control_id}'")


def extract_breadcrumb_json_labels(text: str) -> list[str]:
    for raw_json in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, flags=re.S):
        if '"BreadcrumbList"' not in raw_json:
            continue
        payload = json.loads(unescape(raw_json))
        return [normalize_label(item.get("name", "")) for item in payload.get("itemListElement", [])]
    return []


def validate_breadcrumbs(root: Path, issues: list[str]) -> None:
    for html_path in root.rglob("*.html"):
        text = html_path.read_text(encoding="utf-8", errors="replace")
        if 'aria-label="Breadcrumb"' not in text and 'aria-label="Trilha de navegação"' not in text:
            continue

        parser = BreadcrumbParser()
        parser.feed(text)
        labels = parser.items
        if not labels:
            issues.append(f"{html_path.relative_to(root)}: breadcrumb nav rendered without visible labels")
            continue

        for previous, current in zip(labels, labels[1:]):
            if previous.casefold() == current.casefold():
                issues.append(
                    f"{html_path.relative_to(root)}: duplicate consecutive breadcrumb labels '{previous}' and '{current}'"
                )

        json_labels = extract_breadcrumb_json_labels(text)
        if json_labels and labels != json_labels:
            issues.append(
                f"{html_path.relative_to(root)}: visible breadcrumb {labels} does not match JSON-LD {json_labels}"
            )


def validate_structural_alternates(root: Path, issues: list[str]) -> None:
    alternates = (
        ("pt/oportunidades/index.html", "https://cedis.unb.br/opportunities/"),
        ("opportunities/index.html", "https://cedis.unb.br/pt/oportunidades/"),
        ("pt/junte-se/index.html", "https://cedis.unb.br/join/"),
        ("join/index.html", "https://cedis.unb.br/pt/junte-se/"),
        ("pt/mapa/index.html", "https://cedis.unb.br/map/"),
        ("map/index.html", "https://cedis.unb.br/pt/mapa/"),
    )

    for relative_path, alternate_url in alternates:
        text = read_text(root, relative_path, issues)
        if not text:
            continue
        require_contains(text, alternate_url, relative_path, issues)


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path("docs").resolve()
    issues: list[str] = []

    validate_opportunities(root, issues)
    validate_researcher_cards(root, issues)
    validate_aria_controls(root, issues)
    validate_breadcrumbs(root, issues)
    validate_structural_alternates(root, issues)

    if issues:
        for issue in issues:
            print(f"ERRO: {issue}", file=sys.stderr)
        return 1

    print(f"Rendered HTML OK: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))