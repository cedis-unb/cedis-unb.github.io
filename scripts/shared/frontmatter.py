"""Parse do frontmatter YAML de arquivos .md do site.

Consolida a variante duplicada em validate_content.py, validate_i18n.py e
build_publications.py. O contrato retorna sempre (fm, body) para cobrir
ambos os casos; wrappers convenientes ficam a cargo do chamador.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

_FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)


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


def split_frontmatter_raw(text: str) -> tuple[str, str]:
    """Divide texto bruto em (frontmatter_yaml_str, body).

    Diferente de parse_frontmatter, mantém o YAML como string — útil quando
    o chamador precisa editar linhas do frontmatter preservando ordem/
    formatação (ex.: apply_profile_level.py, consolidate_collaborators.py).

    Levanta ValueError se o arquivo não começa com '---\\n...\\n---'.
    """
    m = _FM_RE.match(text)
    if not m:
        raise ValueError("sem frontmatter YAML delimitado por '---'")
    return m.group(1), m.group(2)


def read_frontmatter_yaml_str(path: Path) -> str | None:
    """Retorna a string YAML do frontmatter de um .md, ou None se faltando.

    Para call sites que só precisam parsear com ``yaml.safe_load`` depois.
    Substitui o padrão duplicado ``re.match(r"^---\\n(.*?)\\n---", ...)``
    em normalize_people_slugs.py, apply_people_slugs.py, migrate_defesas.py.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else None
