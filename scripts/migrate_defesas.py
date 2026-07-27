"""Migração inicial: data/productions.yaml → data/defesas.yaml.

Sprint 1 do PLANO-DEFESAS-2026.md.

O que faz:
    1. Lê data/productions.yaml e filtra itens type ∈ {tcc, dissertation, phd,
       specialization}.
    2. Gera 1 entrada em data/defesas.yaml por publicação, com defesa_id
       canônico (scripts/gen_defesa_slug.py), state derivado (deposited)
       e production_id ligando de volta.
    3. Adiciona defesa_id em cada item migrado de productions.yaml e
       *não* remove defense_date ainda (fica para etapa posterior do
       Sprint 1 quando build_publications.py também for atualizado).
    4. Adiciona entradas para os 4 tcc1-*.pt.md + 1 qualificacao-*.pt.md
       recém-criados (sem production_id).
    5. Faz best-effort de parse de banca dos posts padronizados
       (padrão §3.7 histórico) para popular committee[]. Posts fora do
       padrão ficam com committee: [].
    6. Emite tmp/migrate-defesas-report.json com casos que precisam
       revisão manual (data aproximada, sem orientador, sem match de
       post, parse de banca falhou, etc.).

Uso:
    python3 scripts/migrate_defesas.py         # escreve data/defesas.yaml + atualiza productions.yaml
    python3 scripts/migrate_defesas.py --dry   # não escreve, só relatório

Idempotente: rodar 2× produz o mesmo output (slugs estáveis).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

# Uso ruamel.yaml para preservar comentários/ordem quando possível.
try:
    from ruamel.yaml import YAML
    _HAS_RUAMEL = True
except ImportError:
    _HAS_RUAMEL = False

sys.path.insert(0, str(Path(__file__).parent))
from gen_defesa_slug import disambiguate_slugs, gen_slug  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PRODUCTIONS = ROOT / "data" / "productions.yaml"
DEFESAS_OUT = ROOT / "data" / "defesas.yaml"
POSTS_DIR = ROOT / "content" / "posts"
PEOPLE_DIR = ROOT / "content" / "people"
PROJECTS_YAML = ROOT / "data" / "projects.yaml"
PRODUCTS_DIR = ROOT / "content" / "products"
TMP_REPORT = ROOT / "tmp" / "migrate-defesas-report.json"

DEFESA_TYPES_FROM_PROD = {"tcc", "dissertation", "phd", "specialization"}

# Corte histórico: defesas anteriores a esse ano permanecem em productions.yaml
# como itens legados, mas NÃO viram entradas em data/defesas.yaml. Decidido em
# 2026-07-27 com Sergio (o modelo novo cobre apenas o CEDIS pós-2008).
MIN_DEFESA_YEAR = 2008

# Filtro de instituição — apenas defesas realizadas na UnB (BDM, repositório
# institucional ou programas próprios) entram no modelo novo. Defesas
# externas (UFES, PUC-PR etc.) continuam em productions.yaml sem defesa_id.
UNB_PROGRAM_PREFIXES = ("curso_ppca", "curso_esw", "curso_ppgee", "curso_ppgi",
                        "curso_cc_unb", "curso_espunb")

# Docentes CEDIS — apenas defesas orientadas por eles são consideradas defesas
# do CEDIS. Advisors externos (marilia_miranda, edna_canedo etc.) não contam
# como titulares para o modelo de defesas do CEDIS.
CEDIS_ADVISORS = {
    "sergio_freitas",
    "cristiane_ramos",
    "andre_lanna",
    "george_marsicano",
    "ricardo_ajax",
    "daniel_sundfeld",
    "fabiana_mendes",
}


def _is_defesa_unb(item: dict) -> bool:
    publisher = str(item.get("publisher") or "").lower()
    if "universidade de bras" in publisher:
        return True
    url = str(item.get("url") or "").lower()
    if "bdm.unb.br" in url or "repositorio.unb.br" in url:
        return True
    program = str(item.get("program") or "")
    if any(program.startswith(pref) for pref in UNB_PROGRAM_PREFIXES):
        return True
    return False


def _has_cedis_advisor(item: dict) -> bool:
    advisors = item.get("advisors") or []
    return any(a in CEDIS_ADVISORS for a in advisors)

# TCC1 e qualificação: type do YAML novo → filename pattern PT
NON_PRODUCTION_MARKS = {
    "tcc1": ["tcc1-*.pt.md"],
    "qualification": ["qualificacao-*.pt.md"],
}


def _load_yaml(path: Path) -> Any:
    if _HAS_RUAMEL:
        yml = YAML(typ="safe")
        return yml.load(path.read_text(encoding="utf-8"))
    import yaml as pyyaml
    return pyyaml.safe_load(path.read_text(encoding="utf-8"))


def _dump_yaml(data: Any, path: Path) -> None:
    if _HAS_RUAMEL:
        yml = YAML()
        yml.width = 200
        yml.indent(mapping=2, sequence=4, offset=2)
        yml.default_flow_style = False
        yml.allow_unicode = True
        with path.open("w", encoding="utf-8") as f:
            yml.dump(data, f)
        return
    import yaml as pyyaml
    with path.open("w", encoding="utf-8") as f:
        pyyaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, width=200)


def _norm_year(year: Any) -> int | None:
    """Aceita year como int ou '2026/1' / '2025/2' (semestre). Retorna ano int."""
    if year is None or year == "":
        return None
    if isinstance(year, int):
        return year
    s = str(year)
    m = re.match(r"^(\d{4})", s)
    return int(m.group(1)) if m else None


def _norm_date(dd: Any, year: Any) -> tuple[str, bool]:
    """Retorna (scheduled_iso, date_approximate).

    Regras:
        - dd válido YYYY-MM-DD (ou datetime.date) → usa direto, exact
        - dd YYYY-MM → usa YYYY-MM-15, approx
        - dd YYYY → usa YYYY-06-15, approx
        - dd vazio + year (int|'2026/1') → usa <year>-06-15, approx
                                          (semestre → 06-15 é meio termo)
        - nada → raise
    """
    year_int = _norm_year(year)
    if dd is None or dd == "":
        if not year_int:
            raise ValueError("sem defense_date e sem year")
        return f"{year_int}-06-15T00:00:00-03:00", True
    s = str(dd)
    if isinstance(dd, datetime):
        return dd.strftime("%Y-%m-%dT00:00:00-03:00"), False
    # datetime.date
    if hasattr(dd, "isoformat") and not isinstance(dd, str):
        iso = dd.isoformat()
        return f"{iso}T00:00:00-03:00", False
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return f"{s}T00:00:00-03:00", False
    if re.match(r"^\d{4}-\d{2}$", s):
        return f"{s}-15T00:00:00-03:00", True
    if re.match(r"^\d{4}$", s):
        return f"{s}-06-15T00:00:00-03:00", True
    raise ValueError(f"defense_date fora do formato conhecido: {dd!r}")


def _load_prod_items() -> list[dict]:
    data = _load_yaml(PRODUCTIONS)
    if isinstance(data, dict) and "items" in data:
        return data["items"]
    return data


def _extract_production_slug(item: dict) -> str | None:
    """Slug canônico do item em productions.yaml.

    Usa o padrão de build_publications: <year>-<slug do primeiro autor>-<slug do
    título>. Como não vamos implementar hash aqui, usamos identidade posicional
    de refora: index no productions.yaml original. Vamos preencher production_id
    do items index-relative como fallback ('prod:<n>') — o script real do sprint
    seguinte substitui pelo slug estável de build_publications.
    """
    # Placeholder: usa year+primeiro autor+primeiras palavras do título.
    year = item.get("year")
    authors = item.get("authors") or []
    author = authors[0] if authors else ""
    title = ""
    if isinstance(item.get("title"), dict):
        title = item["title"].get("pt") or item["title"].get("en") or ""
    if not (year and author):
        return None
    from gen_defesa_slug import _clean_token, _split_name

    author_slug = "-".join(_split_name(author)[:2]) or "autor"
    title_words = [_clean_token(w) for w in re.split(r"\s+", title)[:6] if _clean_token(w)]
    title_slug = "-".join(w for w in title_words if w)[:80]
    return f"{year}-{author_slug}-{title_slug}"


def _find_post(defense_slug_hint: str, students: list[str], year: int) -> str | None:
    """Tenta casar com content/posts/defesa-<first>-<last>-<year>.pt.md.

    Retorna slug sem sufixo `.pt.md`, ou None.
    """
    if not students or not year:
        return None
    from gen_defesa_slug import _first_last

    first, last = _first_last(students[0])
    candidate = f"defesa-{first}-{last}-{year}"
    if (POSTS_DIR / f"{candidate}.pt.md").exists():
        return candidate
    # Variações comuns: sem sobrenome final, ou primeiro+segundo
    tokens = re.split(r"\s+", students[0])
    if len(tokens) >= 2:
        from gen_defesa_slug import _clean_token
        cleaned = [_clean_token(t) for t in tokens if _clean_token(t) and _clean_token(t) not in {"de","da","do","dos","das","e"}]
        if len(cleaned) >= 2:
            # tentar primeiro+segundo sobrenome
            alt = f"defesa-{cleaned[0]}-{cleaned[1]}-{year}"
            if (POSTS_DIR / f"{alt}.pt.md").exists() and alt != candidate:
                return alt
    return None


_TITLE_STRIP = re.compile(
    r"^\s*(?:O\s+|A\s+)?(?:Prof(?:essor)?\.?)?[ªº]?\s*(?:Dr\.?[ªº]?\s*|Msc\.?\s*|Ma\.?\s*)?",
    re.IGNORECASE,
)


def _clean_prof_name(s: str) -> str:
    """Remove títulos ('O Prof. Dr.', 'A Prof.ª Dr.ª', 'Dr.') deixando só o nome."""
    s = _TITLE_STRIP.sub("", s).strip()
    s = s.rstrip(",.;:")
    return s


# Cache carregado on-demand.
_PEOPLE_NAME_TO_SLUG: dict[str, str] | None = None


def _load_people_map() -> dict[str, str]:
    """Mapeia nome normalizado (accent-stripped lowercase) → slug."""
    global _PEOPLE_NAME_TO_SLUG
    if _PEOPLE_NAME_TO_SLUG is not None:
        return _PEOPLE_NAME_TO_SLUG
    import yaml as pyyaml
    m: dict[str, str] = {}
    from gen_defesa_slug import _strip_accents
    for f in PEOPLE_DIR.glob("*.pt.md"):
        slug = f.name.replace(".pt.md", "")
        text = f.read_text(encoding="utf-8")
        fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not fm:
            continue
        try:
            data = pyyaml.safe_load(fm.group(1)) or {}
        except Exception:
            continue
        name = data.get("title") or data.get("name")
        if not isinstance(name, str):
            continue
        key = _strip_accents(name).lower().strip()
        m[key] = slug
        # Também: primeiro + último nome como chave alternativa
        tokens = [t for t in re.split(r"\s+", key) if t]
        if len(tokens) >= 2:
            short = f"{tokens[0]} {tokens[-1]}"
            m.setdefault(short, slug)
    _PEOPLE_NAME_TO_SLUG = m
    return m


def _slug_for_name(name: str) -> str | None:
    """Retorna slug de perfil quando o nome bate com algum content/people/*.md.

    Match tolerante a acentos. Também tenta primeiro+último nome.
    """
    from gen_defesa_slug import _strip_accents
    if not name:
        return None
    people = _load_people_map()
    key = _strip_accents(name).lower().strip()
    if key in people:
        return people[key]
    # tenta primeiro+último
    tokens = [t for t in re.split(r"\s+", key) if t and t not in {"de","da","do","dos","das"}]
    if len(tokens) >= 2:
        short = f"{tokens[0]} {tokens[-1]}"
        if short in people:
            return people[short]
    return None


# --- Vínculos: projeto, produtos, publicações ---

_PROJECT_IDS: set[str] | None = None


def _load_project_ids() -> set[str]:
    global _PROJECT_IDS
    if _PROJECT_IDS is not None:
        return _PROJECT_IDS
    import yaml as pyyaml
    if not PROJECTS_YAML.exists():
        _PROJECT_IDS = set()
        return _PROJECT_IDS
    data = pyyaml.safe_load(PROJECTS_YAML.read_text(encoding="utf-8"))
    ids: set[str] = set()
    if isinstance(data, dict):
        data = data.get("items") or data.get("projects") or []
    if isinstance(data, list):
        for it in data:
            if isinstance(it, dict) and it.get("id"):
                ids.add(str(it["id"]))
    _PROJECT_IDS = ids
    return ids


def _infer_project(tags: list[str]) -> str | None:
    """Se alguma tag do item é um id de projeto conhecido, retorna esse id."""
    ids = _load_project_ids()
    for t in tags or []:
        if t in ids:
            return t
    return None


_PRODUCT_INDEX: dict[str, dict] | None = None


def _load_product_index() -> dict[str, dict]:
    """Mapa: slug de produto → dict com metadados (project, publications, tags)."""
    global _PRODUCT_INDEX
    if _PRODUCT_INDEX is not None:
        return _PRODUCT_INDEX
    import yaml as pyyaml
    idx: dict[str, dict] = {}
    for f in PRODUCTS_DIR.glob("*.pt.md"):
        slug = f.name.replace(".pt.md", "")
        text = f.read_text(encoding="utf-8")
        fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not fm:
            continue
        try:
            data = pyyaml.safe_load(fm.group(1)) or {}
        except Exception:
            continue
        idx[slug] = {
            "project": data.get("project"),
            "publications": data.get("publications") or [],
            "tags": data.get("tags") or [],
            "categories": data.get("categories") or [],
        }
    _PRODUCT_INDEX = idx
    return idx


def _infer_related_products(production_id: str, tags: list[str]) -> list[str]:
    """Best-effort: produtos que listam essa publicação em publications[],
    ou compartilham projeto e tags. Retorna slugs."""
    idx = _load_product_index()
    hits: list[str] = []
    for slug, meta in idx.items():
        if production_id and production_id in (meta.get("publications") or []):
            hits.append(slug)
    return hits


# Captura o parágrafo inteiro que contém a frase da banca.
# Delimitado por \n\n (fim de parágrafo Markdown) porque frases usam "Prof."
# e "Dr." — ponto não é bom delimitador.
_BANCA_PARAGRAPH_RE = re.compile(
    r"A\s+defesa\s+(?:aconteceu|ocorreu)[^\n]*?"
    r"(?P<paragraph>A\s+banca(?:\s+examinadora)?\s+foi\s+(?:presidida|composta)[^\n]*)",
    re.IGNORECASE,
)

# Sequência de títulos: 1 a 3 ocorrências de Prof./Dr./Ma./Msc./Ph.D. + espaço.
# `{1,3}` em vez de `+` — evita ambiguidade de backtracking que fazia "Dr"
# escapar do TITLE_SEQ para o grupo `name` em construções "pelo Prof. Dr.".
# Aceita ª/º (feminino) e pontos opcionais.
_TITLE_SEQ = (
    r"(?:(?:Prof(?:essor)?|Dr|Msc|Ma|Ph\.?D)\.?[ªº]?\s+){1,3}"
)

# Orientador: "presidida|composta pel[oa] orientador[a], <Títulos> Nome (Aff),?"
_ADVISOR_RE = re.compile(
    r"(?:presidida|composta)\s+pel[oa]\s+orientador(?:a)?,?\s+"
    + _TITLE_SEQ
    + r"(?!(?:Prof(?:essor)?|Dr|Msc|Ma|Ph\.?D)\b)"
    + r"(?P<name>[A-ZÀ-Úa-zA-ZÀ-ÿ][^,()]+?)"
    + r"(?:\s*\((?P<aff>[^)]+)\))?"
    + r"(?:,|;)",
    re.IGNORECASE,
)

# Cada membro examinador: "pel[oa]s? <Títulos> Nome (Aff)?"
# `(?!...)` impede backtracking do TITLE_SEQ deixar títulos escaparem para name.
# Lookahead final aceita `.` sozinho (sem espaço), pois pode ser fim de sentença.
_MEMBER_RE = re.compile(
    r"pel[oa]s?\s+"
    + _TITLE_SEQ
    + r"(?!(?:Prof(?:essor)?|Dr|Msc|Ma|Ph\.?D)\b)"
    + r"(?P<name>[A-ZÀ-Úa-zA-ZÀ-ÿ][^,()]+?)"
    + r"(?:\s*\((?P<aff>[^)]+)\))?"
    + r"(?=\s*(?:[,;.]|\s+e\s+pel|$))",
    re.IGNORECASE,
)

# Frase extra: "A Prof.ª Dr.ª X, co-orientadora do trabalho, também participou..."
_EXTRA_PARTICIPANT_RE = re.compile(
    r"A\s+(?:Prof(?:essor)?\.?[ªº]?\s*(?:Dr\.?[ªº]?\s*)?)"
    r"(?P<name>[A-ZÀ-Ú][^,]+?),\s*"
    r"(?P<role_text>[^,]+?),\s*"
    r"tamb[ée]m",
    re.IGNORECASE,
)


def _parse_banca(post_slug: str) -> tuple[list[dict], bool]:
    """Retorna (committee, parse_ok).

    Best-effort: se o post existir e casar com padrões históricos (§3.7),
    extrai orientador + examinadores + afiliações. Caso contrário,
    retorna ([], False).
    """
    if not post_slug:
        return [], False
    path = POSTS_DIR / f"{post_slug}.pt.md"
    if not path.exists():
        return [], False
    text = path.read_text(encoding="utf-8")
    # Colapsa shortcode {{< link-interno "/path" "Rótulo" >}} → "Rótulo".
    text = re.sub(
        r'{{<\s*link-interno\s+"[^"]+"\s+"([^"]+)"\s*>}}',
        r"\1",
        text,
    )
    m = _BANCA_PARAGRAPH_RE.search(text)
    if not m:
        return [], False

    paragraph = m.group("paragraph")
    committee: list[dict] = []

    def _add(name: str, aff: str | None, role: str) -> None:
        if not name:
            return
        already = {c["name"] for c in committee}
        if name in already:
            return
        slug = _slug_for_name(name)
        entry = {"role": role}
        if slug:
            entry["slug"] = slug
        else:
            entry["name"] = name
            if aff:
                entry["affiliation"] = aff
        committee.append(entry if slug is None else {**entry, "name": name, "affiliation": aff})
        # Se slug existir, mantemos name/affiliation também para não perder dado
        # até que o template comece a resolver pelo slug (Sprint 2).

    advisor_m = _ADVISOR_RE.search(paragraph)
    if advisor_m:
        _add(
            _clean_prof_name(advisor_m.group("name")),
            (advisor_m.group("aff") or "").strip() or None,
            "advisor",
        )
    for mm in _MEMBER_RE.finditer(paragraph):
        _add(
            _clean_prof_name(mm.group("name")),
            (mm.group("aff") or "").strip() or None,
            "examiner",
        )

    # frase extra opcional (co-orientadora, etc.) — busca no texto inteiro
    em = _EXTRA_PARTICIPANT_RE.search(text)
    if em:
        name = _clean_prof_name(em.group("name"))
        role_text = em.group("role_text").lower()
        role = (
            "co_advisor"
            if "co-orient" in role_text or "coorient" in role_text
            else "examiner"
        )
        _add(name, None, role)

    return committee, bool(committee)


def _build_defesa_entry(
    item: dict,
    production_id: str,
    slug: str,
    news_slug: str | None,
    committee: list[dict],
    date_approx: bool,
    scheduled_iso: str,
) -> dict:
    students = [{"name": a, "slug": None} for a in (item.get("authors") or [])]
    advisors = item.get("advisors") or []
    advisor = advisors[0] if advisors else None
    co_advisors = advisors[1:] if len(advisors) > 1 else []
    tags = list(item.get("tags") or [])
    entry: dict = {
        "id": slug,
        "type": item["type"],
        "program": item.get("program") or None,
        "scheduled_date": scheduled_iso,
        "held_date": scheduled_iso.split("T")[0],
        "title": item.get("title") or {"pt": "", "en": ""},
        "summary": item.get("summary") or {"pt": "", "en": ""},
        "students": students,
        "advisor": advisor,
        "co_advisors": co_advisors or None,
        "committee": committee or [],
        "location": {"room": None, "city": "Brasília", "remote_url": None},
        "tags": tags,
        "project": _infer_project(tags),
        "related_products": _infer_related_products(production_id, tags),
        "related_publications": [],  # sem inferência automática (Sprint futuro)
        "production_id": production_id,
        "news_slug": news_slug,
        "narrative": {"pt": None, "en": None},
        "status_override": None,
    }
    if date_approx:
        entry["date_approximate"] = True
    return entry


def _tcc1_qualif_entry(post_path: Path, kind: str) -> dict:
    """Constrói entrada para tcc1-* ou qualificacao-* já existente."""
    text = post_path.read_text(encoding="utf-8")
    import yaml as pyyaml
    fm_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    fm = pyyaml.safe_load(fm_match.group(1)) if fm_match else {}
    date_iso = str(fm.get("date", ""))
    # Parse date; produz scheduled_iso normalizada
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", date_iso)
    if not m:
        year_m = re.match(r"^(\d{4})", date_iso)
        year = int(year_m.group(1)) if year_m else datetime.now().year
        scheduled_iso = f"{year}-06-15T00:00:00-03:00"
    else:
        scheduled_iso = f"{m.group(1)}T00:00:00-03:00"
    # slug da defesa = extraído do filename (- ano)
    stem = post_path.stem.replace(".pt", "")
    # Ex.: 'tcc1-israel-santos-2026' → students & data já conhecidos por convenção
    # Vamos usar título + resumo do frontmatter.
    return {
        "kind_marker": kind,
        "post_pt": post_path.name,
        "frontmatter": fm,
        "scheduled_iso": scheduled_iso,
        "slug_from_post": stem,
    }


def migrate(dry: bool = False) -> dict:
    report: dict = {
        "totals": {},
        "date_approximate": [],
        "no_advisor": [],
        "no_post_match": [],
        "banca_parse_ok": [],
        "banca_parse_failed": [],
        "tcc1_qualif_added": [],
    }

    items = _load_prod_items()

    def _in_scope(it: dict) -> bool:
        return (
            it.get("type") in DEFESA_TYPES_FROM_PROD
            and (_norm_year(it.get("year")) or 0) >= MIN_DEFESA_YEAR
            and _is_defesa_unb(it)
            and _has_cedis_advisor(it)
        )

    prod_defesas_indexes = [i for i, it in enumerate(items) if _in_scope(it)]
    report["totals"]["productions_source"] = len(prod_defesas_indexes)
    report["totals"]["skipped_pre_2008"] = sum(
        1 for it in items
        if it.get("type") in DEFESA_TYPES_FROM_PROD
        and (_norm_year(it.get("year")) or 0) < MIN_DEFESA_YEAR
    )
    report["totals"]["skipped_non_unb"] = sum(
        1 for it in items
        if it.get("type") in DEFESA_TYPES_FROM_PROD
        and (_norm_year(it.get("year")) or 0) >= MIN_DEFESA_YEAR
        and not _is_defesa_unb(it)
    )
    report["totals"]["skipped_non_cedis_advisor"] = sum(
        1 for it in items
        if it.get("type") in DEFESA_TYPES_FROM_PROD
        and (_norm_year(it.get("year")) or 0) >= MIN_DEFESA_YEAR
        and _is_defesa_unb(it)
        and not _has_cedis_advisor(it)
    )
    report["in_scope_indexes"] = list(prod_defesas_indexes)

    # PASSO 1: gerar slugs e entradas provisórias
    provisional: list[dict] = []
    provisional_slugs: list[str] = []
    for idx in prod_defesas_indexes:
        item = items[idx]
        year = item.get("year") or 0
        authors = item.get("authors") or []
        if not authors:
            report["no_advisor"].append(
                {"idx": idx, "why": "sem authors", "title": (item.get("title") or {}).get("pt", "")[:80]}
            )
            continue
        try:
            scheduled_iso, approx = _norm_date(item.get("defense_date"), year)
        except ValueError as e:
            report["no_advisor"].append(
                {"idx": idx, "why": str(e), "title": (item.get("title") or {}).get("pt", "")[:80]}
            )
            continue
        slug = gen_slug(authors[:2], scheduled_iso)
        provisional_slugs.append(slug)
        provisional.append(
            {
                "idx": idx,
                "item": item,
                "slug_raw": slug,
                "scheduled_iso": scheduled_iso,
                "date_approximate": approx,
            }
        )

    # Desambiguar colisões
    disamb = disambiguate_slugs(provisional_slugs)
    for prov, slug in zip(provisional, disamb):
        prov["slug"] = slug

    defesas_list: list[dict] = []
    for prov in provisional:
        item = prov["item"]
        idx = prov["idx"]
        slug = prov["slug"]
        scheduled_iso = prov["scheduled_iso"]
        approx = prov["date_approximate"]

        if approx:
            report["date_approximate"].append({"slug": slug, "year": item.get("year")})
        advisors = item.get("advisors") or []
        if not advisors:
            report["no_advisor"].append(
                {"slug": slug, "why": "advisors vazio", "authors": item.get("authors")}
            )

        news_slug = _find_post(slug, item.get("authors") or [], item.get("year") or 0)
        if not news_slug:
            report["no_post_match"].append(
                {"slug": slug, "authors": item.get("authors"), "year": item.get("year")}
            )
        committee, parse_ok = _parse_banca(news_slug) if news_slug else ([], False)
        if news_slug and parse_ok:
            report["banca_parse_ok"].append(slug)
        elif news_slug:
            report["banca_parse_failed"].append(slug)

        production_id = _extract_production_slug(item) or f"prod:{idx}"
        entry = _build_defesa_entry(
            item=item,
            production_id=production_id,
            slug=slug,
            news_slug=news_slug,
            committee=committee,
            date_approx=approx,
            scheduled_iso=scheduled_iso,
        )
        defesas_list.append(entry)

    # PASSO 2: tcc1 e qualificação
    for kind, patterns in NON_PRODUCTION_MARKS.items():
        for pattern in patterns:
            for p in sorted(POSTS_DIR.glob(pattern)):
                info = _tcc1_qualif_entry(p, kind)
                report["tcc1_qualif_added"].append({"kind": kind, "post": p.name})
                # Reaproveitamos frontmatter tanto quanto pudermos.
                fm = info["frontmatter"]
                title = {
                    "pt": fm.get("title", ""),
                    "en": None,
                }
                summary = {
                    "pt": fm.get("summary", ""),
                    "en": None,
                }
                # Slug canônico: NON-STANDARD — mantemos slug do post PT como id
                # (mais fácil de rastrear até termos data específica; scheduled_date
                # aproximado do frontmatter).
                entry = {
                    "id": info["slug_from_post"],
                    "type": kind,  # tcc1 | qualification
                    "program": None,
                    "scheduled_date": info["scheduled_iso"],
                    "held_date": info["scheduled_iso"].split("T")[0],
                    "title": title,
                    "summary": summary,
                    "students": [],  # a preencher manualmente (nome está no título)
                    "advisor": None,
                    "co_advisors": None,
                    "committee": [],
                    "location": {"room": None, "city": "Brasília", "remote_url": None},
                    "tags": list(fm.get("tags") or []),
                    "production_id": None,
                    "news_slug": info["slug_from_post"],
                    "narrative": {"pt": None, "en": None},
                    "status_override": None,
                    "date_approximate": True,
                    "needs_manual_review": True,
                }
                defesas_list.append(entry)

    # Ordena por scheduled_date desc (mais recente primeiro) — apenas convenção
    defesas_list.sort(key=lambda e: e["scheduled_date"], reverse=True)
    report["totals"]["defesas_generated"] = len(defesas_list)

    # PASSO 3: escreve outputs
    if not dry:
        TMP_REPORT.parent.mkdir(exist_ok=True)
        DEFESAS_OUT.parent.mkdir(exist_ok=True)
        _dump_yaml(defesas_list, DEFESAS_OUT)

        # Atualiza productions.yaml: adiciona defesa_id nos itens dentro do
        # escopo e REMOVE defesa_id de itens que estão fora do escopo (pré-2008,
        # fora da UnB, sem advisor CEDIS). Sem essa limpeza, o validator
        # reclamaria de defesa_id apontando pra entradas inexistentes.
        prod_data = _load_yaml(PRODUCTIONS)
        prod_items = prod_data if isinstance(prod_data, list) else prod_data["items"]
        in_scope_idx = set(prod_defesas_indexes)
        for prov in provisional:
            prod_items[prov["idx"]]["defesa_id"] = prov["slug"]
        for i, it in enumerate(prod_items):
            if (
                it.get("type") in DEFESA_TYPES_FROM_PROD
                and i not in in_scope_idx
                and it.get("defesa_id")
            ):
                del it["defesa_id"]
        _dump_yaml(prod_data, PRODUCTIONS)

    TMP_REPORT.parent.mkdir(exist_ok=True)
    TMP_REPORT.write_text(json.dumps(report, indent=2, default=str, ensure_ascii=False), encoding="utf-8")
    return report


def _cli() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true", help="não escreve, só relatório")
    args = ap.parse_args()
    report = migrate(dry=args.dry)
    print(f"\n=== migrate_defesas: relatório ===")
    print(f"  productions fonte:      {report['totals']['productions_source']}")
    print(f"  defesas geradas:        {report['totals'].get('defesas_generated', 0)}")
    print(f"  data aproximada:        {len(report['date_approximate'])}")
    print(f"  sem orientador:         {len(report['no_advisor'])}")
    print(f"  sem post correspondente:{len(report['no_post_match'])}")
    print(f"  banca parseada ok:      {len(report['banca_parse_ok'])}")
    print(f"  banca parse falhou:     {len(report['banca_parse_failed'])}")
    print(f"  tcc1/qualif adicionados:{len(report['tcc1_qualif_added'])}")
    print(f"\nrelatório completo:      {TMP_REPORT}")
    if not args.dry:
        print(f"data/defesas.yaml:       escrito ({report['totals'].get('defesas_generated', 0)} entradas)")
        print(f"data/productions.yaml:   atualizado (adicionou defesa_id)")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
