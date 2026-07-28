"""Parse do frontmatter YAML de arquivos .md do site.

Consolida a variante duplicada em validate_content.py, validate_i18n.py e
build_publications.py. O contrato retorna sempre (fm, body) para cobrir
ambos os casos; wrappers convenientes ficam a cargo do chamador.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def parse_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str]:
    """Extrai o bloco YAML delimitado por '---' no início de um .md.

    Retorna (frontmatter_dict, body). Se o arquivo não tem frontmatter,
    retorna (None, text). Se o YAML é inválido, propaga yaml.YAMLError —
    o chamador decide se converte em warning ou aborta.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    fm = yaml.safe_load(parts[1])
    return (fm if isinstance(fm, dict) else None), parts[2]


def parse_frontmatter_dict(path: Path) -> dict[str, Any] | None:
    """Wrapper que descarta o body — para chamadores que só usam o fm."""
    fm, _ = parse_frontmatter(path)
    return fm
