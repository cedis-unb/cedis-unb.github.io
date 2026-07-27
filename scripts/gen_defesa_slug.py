"""Geração de slug canônico para defesas (data/defesas.yaml).

Contrato:
    gen_slug(student_names: list[str], scheduled_date: str) -> str

Regra (§3 de PLANO-DEFESAS-2026.md):
    - 1 aluno: <primeiro-nome>-<último-sobrenome>-<AAAA>-<MM>-<DD>
    - dupla (TCC): <nome1>-<nome2>-<AAAA>-<MM>-<DD>
      (usa primeiro nome de cada aluno)
    - normalização: minúsculo, sem acentos, hífens, remove partículas
      pt-br (de|da|do|dos|das) no meio do nome.

Uso:
    from scripts.gen_defesa_slug import gen_slug
    slug = gen_slug(["Emanuel Oliveira"], "2025-12-11")
    # 'emanuel-oliveira-2025-12-11'

    slug = gen_slug(
        ["Henrique Azevedo Batalha", "Marina Márcia Costa de Souza"],
        "2026-07-04",
    )
    # 'henrique-marina-2026-07-04'

Colisões: em caso raro (mesmo primeiro-último nome + mesma data), o
chamador deve sufixar `-2`, `-3`, ... `disambiguate_slugs()` faz isso
sobre uma lista.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Iterable

_PARTICLES = {"de", "da", "do", "dos", "das", "e"}
_DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")


def _strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def _clean_token(tok: str) -> str:
    tok = _strip_accents(tok).lower()
    tok = re.sub(r"[^a-z0-9]+", "", tok)
    return tok


def _split_name(full: str) -> list[str]:
    """Retorna tokens do nome (sem partículas, minúsculos, sem acentos)."""
    parts = re.split(r"\s+", full.strip())
    out: list[str] = []
    for p in parts:
        cleaned = _clean_token(p)
        if not cleaned:
            continue
        if cleaned in _PARTICLES:
            continue
        out.append(cleaned)
    return out


def _first_last(full: str) -> tuple[str, str]:
    tokens = _split_name(full)
    if not tokens:
        raise ValueError(f"nome vazio após normalização: {full!r}")
    first = tokens[0]
    last = tokens[-1] if len(tokens) > 1 else tokens[0]
    return first, last


def _first_only(full: str) -> str:
    tokens = _split_name(full)
    if not tokens:
        raise ValueError(f"nome vazio após normalização: {full!r}")
    return tokens[0]


def _extract_date(scheduled_date: str) -> str:
    """Extrai 'YYYY-MM-DD' de um ISO date/datetime, ou de string parcial."""
    if not scheduled_date:
        raise ValueError("scheduled_date obrigatório")
    m = _DATE_RE.match(str(scheduled_date))
    if not m:
        raise ValueError(f"scheduled_date fora do formato ISO: {scheduled_date!r}")
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"


def gen_slug(student_names: Iterable[str], scheduled_date: str) -> str:
    """Gera slug canônico da defesa.

    Args:
        student_names: 1 ou 2 nomes completos (dupla = TCC).
        scheduled_date: 'YYYY-MM-DD' ou ISO datetime.
    Returns:
        slug canônico. Ex.: 'emanuel-oliveira-2025-12-11'.
    """
    names = [n for n in student_names if n and n.strip()]
    if not names:
        raise ValueError("student_names vazio")
    if len(names) > 2:
        raise ValueError(
            f"máximo 2 alunos por defesa (dupla TCC); recebeu {len(names)}"
        )
    date = _extract_date(scheduled_date)
    if len(names) == 1:
        first, last = _first_last(names[0])
        base = f"{first}-{last}"
    else:
        a = _first_only(names[0])
        b = _first_only(names[1])
        base = f"{a}-{b}"
    return f"{base}-{date}"


def disambiguate_slugs(slugs: list[str]) -> list[str]:
    """Se dois slugs colidem, sufixa -2, -3, ... na ordem em que aparecem.

    Preserva a primeira ocorrência intacta.
    """
    seen: dict[str, int] = {}
    out: list[str] = []
    for s in slugs:
        n = seen.get(s, 0)
        seen[s] = n + 1
        out.append(s if n == 0 else f"{s}-{n + 1}")
    return out


def _self_test() -> None:
    """Testes-âncora executados quando o módulo é chamado como script."""
    cases = [
        # (nomes, data, esperado)
        (["Emanuel Oliveira"], "2025-12-11", "emanuel-oliveira-2025-12-11"),
        (
            ["Henrique Azevedo Batalha", "Marina Márcia Costa de Souza"],
            "2026-07-04",
            "henrique-marina-2026-07-04",
        ),
        (
            ["Sergio Antônio Andrade de Freitas"],
            "2005-06-15",
            "sergio-freitas-2005-06-15",
        ),
        (["Israel Thalles Dutra dos Santos"], "2026-07-04", "israel-santos-2026-07-04"),
        (
            ["Ian Lucca Soares Mesquita", "Christian Hirsch Santos"],
            "2026-07-11",
            "ian-christian-2026-07-11",
        ),
        # datetime ISO com T e offset
        (
            ["Lucas Pereira Gomes Linard"],
            "2026-06-30T14:00:00-03:00",
            "lucas-linard-2026-06-30",
        ),
    ]
    for names, date, expected in cases:
        got = gen_slug(names, date)
        assert got == expected, f"gen_slug({names}, {date}) → {got!r} != {expected!r}"

    # disambiguate: mesmo slug repetido → sufixo
    slugs = [
        "joao-silva-2024-06-15",
        "joao-silva-2024-06-15",
        "outro-2024-06-15",
        "joao-silva-2024-06-15",
    ]
    disamb = disambiguate_slugs(slugs)
    assert disamb == [
        "joao-silva-2024-06-15",
        "joao-silva-2024-06-15-2",
        "outro-2024-06-15",
        "joao-silva-2024-06-15-3",
    ], f"disambiguate errado: {disamb}"

    # erros esperados
    try:
        gen_slug([], "2024-06-15")
    except ValueError:
        pass
    else:
        raise AssertionError("esperava ValueError para lista vazia")

    try:
        gen_slug(["A", "B", "C"], "2024-06-15")
    except ValueError:
        pass
    else:
        raise AssertionError("esperava ValueError para 3 alunos")

    try:
        gen_slug(["Ana Silva"], "sem data válida")
    except ValueError:
        pass
    else:
        raise AssertionError("esperava ValueError para data inválida")

    print("gen_defesa_slug: todos os testes-âncora passaram.")


if __name__ == "__main__":
    _self_test()
