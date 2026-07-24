#!/usr/bin/env python3
"""Valida integridade dos dados do site CEDIS.

Referência: issue I02 do PLANO-AUDITORIA-2026.md e docs-src/data-model.md.

Roda em dois modos:
  - warn (default) — reporta problemas mas termina com exit 0. Ideal para
    o CI durante a transição da Fase 3.
  - strict — problemas críticos fazem exit != 0. Ativar via CEDIS_VALIDATE_STRICT=1.

Executa duas classes de verificação:
  1. Schema — valida cada entidade contra o JSON Schema correspondente
     em schemas/. Usa jsonschema se disponível; cai em validação manual
     mínima se o pacote não estiver instalado.
  2. Integridade referencial — checa que IDs citados em relações
     existam nas fontes canônicas (content/people, people.yaml, areas.yaml).

Uso:
    python3 scripts/validate_content.py                    # warn
    CEDIS_VALIDATE_STRICT=1 python3 scripts/validate_content.py  # strict

O relatório é escrito em stdout e (se CEDIS_VALIDATE_REPORT for setado)
também em Markdown no caminho indicado.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print(
        "ERRO: PyYAML não instalado. Rode 'pip install pyyaml' antes de invocar.",
        file=sys.stderr,
    )
    sys.exit(2)

try:
    from jsonschema import Draft202012Validator  # type: ignore
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CONTENT_DIR = ROOT / "content"
SCHEMAS_DIR = ROOT / "schemas"

STRICT = os.environ.get("CEDIS_VALIDATE_STRICT", "").lower() in ("1", "true", "yes")
REPORT_PATH = os.environ.get("CEDIS_VALIDATE_REPORT")
PROJECT_STATUSES = {"active", "ongoing", "closed"}
PRODUCT_STATUSES = {"active", "prototype", "archived", "beta"}
EXCLUDED_PROJECT_IDS = {
    # Projetos externos ou institucionais de terceiros em que integrantes do
    # CEDIS participaram, mas que não devem compor o rol de projetos CEDIS.
    "project_app_parkinson",
    "project_automacao_servicos",
    "project_biocloud",
    "project_capacidade_produtiva",
    "project_cloud_iot",
    "project_conab_desempenho",
    "project_framework_mcom",
    "project_hase",
    "project_human_factors_cybersecurity",
    "project_metricas_software",
    "project_td",
    "project_td_2021",
}
STRUCTURAL_TAGS = {
    "active",
    "inactive",
    "closed",
    "project",
    "products",
    "people",
    "researcher",
    "knowledge_areas",
    "app",
}


class Issue:
    __slots__ = ("severity", "category", "location", "message")

    def __init__(self, severity: str, category: str, location: str, message: str):
        self.severity = severity  # "warning" | "error"
        self.category = category
        self.location = location
        self.message = message

    def __str__(self) -> str:
        return f"[{self.severity.upper():<7}] {self.category} :: {self.location} — {self.message}"


ISSUES: list[Issue] = []


def warn(category: str, location: str, message: str) -> None:
    ISSUES.append(Issue("warning", category, location, message))


def error(category: str, location: str, message: str) -> None:
    ISSUES.append(Issue("error", category, location, message))


def load_yaml(path: Path) -> object:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_schema(name: str) -> dict:
    path = SCHEMAS_DIR / f"{name}.schema.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_against_schema(instance: object, schema: dict, location: str) -> None:
    """Chama jsonschema se disponível; senão, faz check mínimo de required."""
    normalized_instance = normalize_for_schema(instance)
    if HAS_JSONSCHEMA:
        validator = Draft202012Validator(schema)
        for err in sorted(validator.iter_errors(normalized_instance), key=lambda e: list(e.path)):
            path = "/".join(str(p) for p in err.absolute_path) or "<root>"
            warn("schema", f"{location}#{path}", err.message)
        return

    # Fallback minimalista: verifica só os required do primeiro nível.
    if not isinstance(normalized_instance, dict):
        return
    for req in schema.get("required", []):
        if req not in normalized_instance:
            warn("schema", location, f"campo obrigatório ausente: '{req}'")


def normalize_for_schema(value: object) -> object:
    if isinstance(value, dt.datetime):
        return value.isoformat()
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: normalize_for_schema(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalize_for_schema(v) for v in value]
    return value


def as_list(value: object) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def validate_language_id(fm: dict, location: str) -> None:
    lang = fm.get("language")
    if lang is None:
        return
    if lang not in {"pt", "en"}:
        warn("language", location, f"language inválido: '{lang}' (use 'pt' ou 'en'; 'pt' representa pt-BR)")


def page_id(path: Path, fm: dict) -> str:
    if fm.get("id"):
        return str(fm["id"]).strip()
    stem = path.stem
    if stem.endswith(".pt") or stem.endswith(".en"):
        stem = stem[:-3]
    return stem.lower()


def project_id_from_page(path: Path, fm: dict, known_project_ids: set[str]) -> str:
    if fm.get("id"):
        return str(fm["id"]).strip()
    for value in as_list(fm.get("categories")) + as_list(fm.get("tags")):
        if isinstance(value, str) and value.strip() in known_project_ids:
            return value.strip()
    return page_id(path, fm)


def parse_iso_date(value: object) -> dt.date | None:
    if value in (None, ""):
        return None
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    text = str(value).strip()
    match = re.match(r"^([0-9]{4}-[0-9]{2}-[0-9]{2})", text)
    if not match:
        return None
    try:
        return dt.date.fromisoformat(match.group(1))
    except ValueError:
        return None


def parse_frontmatter(md_path: Path) -> dict | None:
    """Extrai o bloco YAML entre '---' do início do arquivo."""
    try:
        text = md_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        warn("io", str(md_path.relative_to(ROOT)), f"não pude ler: {e}")
        return None
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        warn("yaml", str(md_path.relative_to(ROOT)), f"frontmatter inválido: {e}")
        return None
    return fm if isinstance(fm, dict) else None


def collect_area_ids(areas_data: dict) -> set[str]:
    areas = areas_data.get("areas", []) if isinstance(areas_data, dict) else []
    return {a["id"] for a in areas if isinstance(a, dict) and "id" in a}


def collect_data_project_ids(projects_data: dict) -> set[str]:
    projects = projects_data.get("projects", []) if isinstance(projects_data, dict) else []
    return {p["id"] for p in projects if isinstance(p, dict) and "id" in p}


def validate_areas(areas_data: dict, person_ids: set[str]) -> None:
    schema = load_schema("area")
    areas = areas_data.get("areas", [])
    seen: set[str] = set()
    for area in areas:
        if not isinstance(area, dict):
            continue
        aid = area.get("id", "<no-id>")
        location = f"data/areas.yaml::{aid}"
        if aid in seen:
            error("areas", location, "id duplicado")
        seen.add(aid)
        validate_against_schema(area, schema, location)
        for researcher_id in area.get("researchers", []) or []:
            if researcher_id not in person_ids:
                warn("xref", location, f"researcher '{researcher_id}' não existe em content/people nem data/people.yaml")


def validate_people(people_data: dict, advisor_ids: set[str]) -> None:
    schema = load_schema("person")
    people = people_data.get("people", [])
    if not isinstance(people, list):
        error("people", "data/people.yaml", "'people' deve ser lista")
        return
    seen_slugs: set[str] = set()
    for i, person in enumerate(people):
        if not isinstance(person, dict):
            continue
        location = f"data/people.yaml::[{i}] {person.get('name', '?')}"
        validate_against_schema(person, schema, location)
        slug = person.get("slug")
        if not isinstance(slug, str) or not slug.strip():
            error("people", location, "campo obrigatório ausente: 'slug'")
        elif not re.match(r"^[a-z0-9_]+$", slug):
            error("people", location, f"slug fora do padrão snake_case: '{slug}'")
        elif slug in seen_slugs:
            error("people", location, f"slug duplicado em data/people.yaml: '{slug}'")
        else:
            seen_slugs.add(slug)

        supervision_units = person.get("supervisions")
        if isinstance(supervision_units, list) and supervision_units:
            units = supervision_units
        else:
            units = [person]
        for unit_idx, unit in enumerate(units):
            if not isinstance(unit, dict):
                continue
            unit_location = location if unit is person else f"{location}.supervisions[{unit_idx}]"
            for adv_id in unit.get("advisors", []) or []:
                if adv_id not in advisor_ids:
                    warn("xref", unit_location, f"advisor '{adv_id}' não existe como researcher/advisor_only em content/people")


def validate_productions(prod_data: dict, advisor_ids: set[str], person_ids: set[str]) -> None:
    schema = load_schema("publication")
    items = prod_data.get("items", [])
    if not isinstance(items, list):
        error("productions", "data/productions.yaml", "'items' deve ser lista")
        return
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            continue
        title = item.get("title", {})
        title_short = title.get("pt", title.get("en", "?"))[:60] if isinstance(title, dict) else "?"
        location = f"data/productions.yaml::[{i}] {title_short}"
        validate_against_schema(item, schema, location)
        for adv_id in item.get("advisors", []) or []:
            if adv_id not in advisor_ids:
                warn("xref", location, f"advisor '{adv_id}' não existe como researcher/advisor_only em content/people")
        for person_id in item.get("people", []) or []:
            if person_id not in person_ids:
                warn("xref", location, f"people '{person_id}' não existe em content/people nem data/people.yaml")


def validate_data_projects(projects_data: dict, person_ids: set[str]) -> None:
    projects = projects_data.get("projects", []) if isinstance(projects_data, dict) else []
    seen: set[str] = set()
    if not isinstance(projects, list):
        error("projects", "data/projects.yaml", "'projects' deve ser lista")
        return
    for project in projects:
        if not isinstance(project, dict):
            continue
        pid = project.get("id", "<no-id>")
        location = f"data/projects.yaml::{pid}"
        if pid in EXCLUDED_PROJECT_IDS:
            error("projects", location, "projeto excluído do rol CEDIS não deve aparecer em data/projects.yaml")
        if pid in seen:
            error("projects", location, "id duplicado")
        seen.add(pid)
        status = project.get("status")
        if status and status not in PROJECT_STATUSES and status != "active":
            warn("enum", location, f"status legado inválido: '{status}'")
        for researcher_id in project.get("researchers", []) or []:
            if researcher_id not in person_ids:
                warn("xref", location, f"researcher '{researcher_id}' não existe em content/people nem data/people.yaml")


def validate_content_section(section: str, schema_name: str) -> list[tuple[Path, dict]]:
    """Valida todos os .md em content/<section>/. Retorna lista de (path, frontmatter)."""
    schema = load_schema(schema_name)
    section_dir = CONTENT_DIR / section
    results: list[tuple[Path, dict]] = []
    if not section_dir.exists():
        return results
    for md_path in sorted(section_dir.rglob("*.md")):
        if md_path.name.startswith("_index."):
            continue
        fm = parse_frontmatter(md_path)
        if fm is None:
            continue
        rel = md_path.relative_to(ROOT).as_posix()
        validate_language_id(fm, rel)
        validate_against_schema(fm, schema, rel)
        for tag in fm.get("tags", []) or []:
            if not isinstance(tag, str):
                warn("tags", rel, f"tag não-string: {tag!r}")
                continue
            if tag.strip() == "":
                warn("tags", rel, "tag vazia")
        results.append((md_path, fm))
    return results


def collect_content_ids(entries: list[tuple[Path, dict]], known_project_ids: set[str] | None = None) -> set[str]:
    ids: set[str] = set()
    for path, fm in entries:
        if known_project_ids is None:
            ids.add(page_id(path, fm))
        else:
            ids.add(project_id_from_page(path, fm, known_project_ids))
    return ids


def collect_people_page_ids() -> set[str]:
    ids: set[str] = set()
    people_dir = CONTENT_DIR / "people"
    if not people_dir.exists():
        return ids
    for md_path in people_dir.rglob("*.md"):
        fm = parse_frontmatter(md_path) or {}
        ids.add(page_id(md_path, fm))
    return ids


def collect_data_people_slugs(people_data: dict) -> set[str]:
    people = people_data.get("people", []) if isinstance(people_data, dict) else []
    return {
        str(person["slug"]).strip()
        for person in people
        if isinstance(person, dict) and isinstance(person.get("slug"), str) and person.get("slug").strip()
    }


def collect_advisor_page_ids() -> set[str]:
    ids: set[str] = set()
    people_dir = CONTENT_DIR / "people"
    if not people_dir.exists():
        return ids
    for md_path in people_dir.rglob("*.md"):
        fm = parse_frontmatter(md_path) or {}
        profile_level = fm.get("profile_level")
        categories = set(as_list(fm.get("categories")))
        if profile_level in {"researcher", "advisor_only"} or "researcher" in categories:
            ids.add(page_id(md_path, fm))
    return ids


def validate_project_pages(
    project_entries: list[tuple[Path, dict]],
    person_ids: set[str],
    area_ids: set[str],
    project_ids: set[str],
    product_ids: set[str],
) -> None:
    by_lang: dict[str, set[str]] = defaultdict(set)
    for path, fm in project_entries:
        rel = path.relative_to(ROOT).as_posix()
        pid = project_id_from_page(path, fm, project_ids)
        if pid in EXCLUDED_PROJECT_IDS:
            error("projects", rel, "projeto excluído do rol CEDIS não deve existir em content/projects")
        lang = fm.get("language")
        by_lang[pid].add(str(lang))
        if fm.get("id") != pid:
            warn("schema", rel, f"id canônico ausente ou divergente; esperado '{pid}'")
        status = fm.get("status")
        if status not in PROJECT_STATUSES:
            warn("enum", rel, f"status de projeto inválido: '{status}'")
        start_date = parse_iso_date(fm.get("start_date"))
        end_date = parse_iso_date(fm.get("end_date"))
        if start_date and end_date and start_date > end_date:
            error("date", rel, "start_date é posterior a end_date")
        for researcher_id in as_list(fm.get("researchers")):
            if researcher_id not in person_ids:
                warn("xref", rel, f"researcher '{researcher_id}' não existe em content/people nem data/people.yaml")
        for area_id in as_list(fm.get("areas")):
            if area_id not in area_ids:
                warn("xref", rel, f"area '{area_id}' não existe em areas.yaml")
        for product_id in as_list(fm.get("products")):
            if product_id not in product_ids:
                warn("xref", rel, f"product '{product_id}' não existe em content/products")

    for pid, langs in by_lang.items():
        if langs != {"pt", "en"}:
            warn("i18n", f"content/projects::{pid}", f"par de idioma incompleto: {sorted(langs)}")


def validate_product_pages(
    product_entries: list[tuple[Path, dict]],
    person_ids: set[str],
    area_ids: set[str],
    project_ids: set[str],
) -> None:
    by_lang: dict[str, set[str]] = defaultdict(set)
    for path, fm in product_entries:
        rel = path.relative_to(ROOT).as_posix()
        pid = page_id(path, fm)
        lang = fm.get("language")
        by_lang[pid].add(str(lang))
        if fm.get("id") != pid:
            warn("schema", rel, f"id canônico ausente ou divergente; esperado '{pid}'")
        status = fm.get("status")
        if status not in PRODUCT_STATUSES:
            warn("enum", rel, f"status de produto inválido: '{status}'")
        project_id = fm.get("project")
        if project_id in EXCLUDED_PROJECT_IDS:
            error("xref", rel, f"project '{project_id}' foi excluído do rol CEDIS")
        if project_id and project_id not in project_ids:
            warn("xref", rel, f"project '{project_id}' não existe em content/projects")
        for researcher_id in as_list(fm.get("responsible")):
            if researcher_id not in person_ids:
                warn("xref", rel, f"responsible '{researcher_id}' não existe em content/people nem data/people.yaml")
        for area_id in as_list(fm.get("areas")):
            if area_id not in area_ids:
                warn("xref", rel, f"area '{area_id}' não existe em areas.yaml")

    for pid, langs in by_lang.items():
        if langs != {"pt", "en"}:
            warn("i18n", f"content/products::{pid}", f"par de idioma incompleto: {sorted(langs)}")


def validate_opportunity_pages(
    opportunity_entries: list[tuple[Path, dict]],
    person_ids: set[str],
    project_ids: set[str],
) -> None:
    by_key: dict[str, set[str]] = defaultdict(set)
    for path, fm in opportunity_entries:
        rel = path.relative_to(ROOT).as_posix()
        if path.name.startswith("_index."):
            continue
        oid = str(fm.get("id") or page_id(path, fm))
        by_key[oid].add(str(fm.get("language")))
        status = fm.get("status")
        if status not in {"open", "closed", "expired"}:
            warn("enum", rel, f"status de oportunidade inválido: '{status}'")
        if not parse_iso_date(fm.get("deadline")):
            warn("date", rel, "deadline ausente ou inválido")
        project_id = fm.get("project")
        if project_id in EXCLUDED_PROJECT_IDS:
            error("xref", rel, f"project '{project_id}' foi excluído do rol CEDIS")
        if project_id and project_id not in project_ids:
            warn("xref", rel, f"project '{project_id}' não existe em content/projects")
        for responsible_id in as_list(fm.get("responsible")):
            if responsible_id not in person_ids:
                warn("xref", rel, f"responsible '{responsible_id}' não existe em content/people nem data/people.yaml")
    for oid, langs in by_key.items():
        if langs != {"pt", "en"}:
            warn("i18n", f"content/opportunities::{oid}", f"par de idioma incompleto: {sorted(langs)}")


def validate_generated_publication_pages() -> list[tuple[Path, dict]]:
    entries: list[tuple[Path, dict]] = []
    section_dir = CONTENT_DIR / "publications"
    if not section_dir.exists():
        return entries
    sync = subprocess.run(
        [sys.executable, "scripts/build_publications.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if sync.returncode != 0:
        message = (sync.stdout or sync.stderr).strip().splitlines()[0] if (sync.stdout or sync.stderr).strip() else "content/publications divergente"
        warn("generated", "content/publications", message)
    by_key: dict[str, set[str]] = defaultdict(set)
    required = ("title", "date", "language", "translationKey", "generated_by", "canonical_source")
    page_required = ("id", "year", "authors", "publication_group", "publication_type")
    for md_path in sorted(section_dir.rglob("*.md")):
        fm = parse_frontmatter(md_path)
        if fm is None:
            continue
        rel = md_path.relative_to(ROOT).as_posix()
        for req in required:
            if req not in fm:
                warn("schema", rel, f"campo obrigatório ausente: '{req}'")
        if fm.get("generated_by") != "scripts/build_publications.py":
            warn("generated", rel, "generated_by inválido ou ausente")
        if fm.get("canonical_source") != "data/productions.yaml":
            warn("generated", rel, "canonical_source inválido ou ausente")
        if not md_path.name.startswith("_index."):
            for req in page_required:
                if req not in fm:
                    warn("schema", rel, f"campo obrigatório ausente: '{req}'")
            if fm.get("publication_type") not in {"article", "book", "book chapter", "book_section", "conference", "didactic", "dissertation", "phd", "registro", "specialization", "tcc", "workshop"}:
                warn("enum", rel, f"publication_type inválido: '{fm.get('publication_type')}'")
        by_key[str(fm.get("translationKey") or page_id(md_path, fm))].add(str(fm.get("language")))
        entries.append((md_path, fm))
    for key, langs in by_key.items():
        if langs != {"pt", "en"}:
            warn("i18n", f"content/publications::{key}", f"par de idioma incompleto: {sorted(langs)}")
    return entries


def validate_structural_page(path: Path, schema_name: str) -> list[tuple[Path, dict]]:
    fm = parse_frontmatter(path)
    if fm is None:
        return []
    validate_against_schema(fm, load_schema(schema_name), path.relative_to(ROOT).as_posix())
    return [(path, fm)]


def validate_translation_keys(all_frontmatters: list[tuple[Path, dict]]) -> None:
    """Toda página com translationKey deve ter par (pt+en) declarando a mesma chave."""
    by_key: dict[str, list[tuple[Path, dict]]] = defaultdict(list)
    for path, fm in all_frontmatters:
        key = fm.get("translationKey")
        if not key:
            continue
        by_key[key].append((path, fm))

    for key, entries in by_key.items():
        langs = {fm.get("language") for _, fm in entries}
        if "pt" not in langs:
            for path, _ in entries:
                warn("i18n", str(path.relative_to(ROOT)), f"translationKey '{key}' sem versão pt")
        if "en" not in langs:
            for path, _ in entries:
                warn("i18n", str(path.relative_to(ROOT)), f"translationKey '{key}' sem versão en")


def validate_excluded_project_references() -> None:
    """Bloqueia reintrodução de projetos externos no rol CEDIS."""
    fields = ("id", "project")
    list_fields = ("categories", "tags", "related_ids", "projects")
    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        fm = parse_frontmatter(md_path)
        if fm is None:
            continue
        rel = md_path.relative_to(ROOT).as_posix()
        for field in fields:
            value = fm.get(field)
            if value in EXCLUDED_PROJECT_IDS:
                error("projects", rel, f"{field} referencia projeto excluído do rol CEDIS: '{value}'")
        for field in list_fields:
            for value in as_list(fm.get(field)):
                if value in EXCLUDED_PROJECT_IDS:
                    error("projects", rel, f"{field} contém projeto excluído do rol CEDIS: '{value}'")


def write_report() -> None:
    if not REPORT_PATH:
        return
    path = Path(REPORT_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("# Relatório do validador de conteúdo CEDIS\n\n")
        by_cat = defaultdict(list)
        for issue in ISSUES:
            by_cat[issue.category].append(issue)
        for cat in sorted(by_cat.keys()):
            f.write(f"## {cat} ({len(by_cat[cat])})\n\n")
            for issue in by_cat[cat]:
                f.write(f"- **{issue.severity}** · `{issue.location}` — {issue.message}\n")
            f.write("\n")


def main() -> int:
    areas_data = load_yaml(DATA_DIR / "areas.yaml") or {}
    people_data = load_yaml(DATA_DIR / "people.yaml") or {}
    prod_data = load_yaml(DATA_DIR / "productions.yaml") or {}
    projects_data = load_yaml(DATA_DIR / "projects.yaml") or {}

    area_ids = collect_area_ids(areas_data)
    data_project_ids = collect_data_project_ids(projects_data)
    person_ids = collect_people_page_ids() | collect_data_people_slugs(people_data)
    advisor_ids = collect_advisor_page_ids()

    validate_areas(areas_data, person_ids)
    validate_people(people_data, advisor_ids)
    validate_productions(prod_data, advisor_ids, person_ids)
    validate_data_projects(projects_data, person_ids)

    all_fms: list[tuple[Path, dict]] = []
    project_entries: list[tuple[Path, dict]] = []
    product_entries: list[tuple[Path, dict]] = []
    for section, schema_name in (
        ("projects", "project"),
        ("products", "product"),
    ):
        entries = validate_content_section(section, schema_name)
        all_fms.extend(entries)
        if section == "projects":
            project_entries = entries
        else:
            product_entries = entries

    project_ids = data_project_ids | collect_content_ids(project_entries, data_project_ids)
    product_ids = collect_content_ids(product_entries)
    validate_project_pages(project_entries, person_ids, area_ids, project_ids, product_ids)
    validate_product_pages(product_entries, person_ids, area_ids, project_ids)
    all_fms.extend(validate_generated_publication_pages())

    opportunity_entries = validate_content_section("opportunities", "opportunity")
    all_fms.extend(opportunity_entries)
    validate_opportunity_pages(opportunity_entries, person_ids, project_ids)

    for path, schema_name in (
        (CONTENT_DIR / "parceiros.pt.md", "partner"),
        (CONTENT_DIR / "parceiros.en.md", "partner"),
        (CONTENT_DIR / "reconhecimentos.pt.md", "recognition"),
        (CONTENT_DIR / "reconhecimentos.en.md", "recognition"),
    ):
        if path.exists():
            all_fms.extend(validate_structural_page(path, schema_name))
    # Pessoas e áreas: valida frontmatter contra schema mínimo. Perfis derivados
    # e orientadores externos são stubs técnicos; não têm data editorial própria.
    for section in ("people", "areas"):
        for md_path in sorted((CONTENT_DIR / section).rglob("*.md")):
            fm = parse_frontmatter(md_path)
            if fm is None:
                continue
            rel = md_path.relative_to(ROOT).as_posix()
            validate_language_id(fm, rel)
            required = ["title", "language"]
            if section != "people" or fm.get("profile_level") not in {"derived", "advisor_only"}:
                required.append("date")
            for req in required:
                if req not in fm:
                    warn("schema", rel, f"campo obrigatório ausente: '{req}'")
            for tag in fm.get("tags", []) or []:
                if isinstance(tag, str) and tag.strip() == "":
                    warn("tags", rel, "tag vazia")
            all_fms.append((md_path, fm))

    validate_translation_keys(all_fms)
    validate_excluded_project_references()

    # Relatório
    errors = [i for i in ISSUES if i.severity == "error"]
    warnings = [i for i in ISSUES if i.severity == "warning"]

    for issue in ISSUES:
        print(issue)

    print()
    print(f"Total: {len(errors)} erros, {len(warnings)} warnings.")

    write_report()

    if STRICT and errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
