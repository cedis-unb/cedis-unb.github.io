"""Normalização de strings — remoção de acentos e geração de slugs.

Consolida o padrão NFKD usado em normalize_people_slugs.py,
apply_people_slugs.py e build_publications.py.

Nota: gen_defesa_slug.py tem regras próprias (hifens + partículas PT) e
não usa este módulo — ele gera IDs de defesa, um domínio distinto.
"""
from __future__ import annotations

import re
import unicodedata


def strip_accents(s: str) -> str:
    """Remove marcas diacríticas via decomposição NFKD."""
    n = unicodedata.normalize("NFKD", s)
    return "".join(c for c in n if not unicodedata.combining(c))


def slugify_snake(name: str) -> str:
    """Slug canônico snake_case: sem acento, minúsculo, [a-z0-9_]+.

    Coincide com scripts/normalize_people_slugs.py::slugify.
    """
    n = strip_accents(name).lower()
    return re.sub(r"[^a-z0-9]+", "_", n).strip("_")
