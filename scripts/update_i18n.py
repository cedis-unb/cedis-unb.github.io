#!/usr/bin/env python3
"""Sincroniza labels de i18n com IDs em data/areas.yaml e data/projects.yaml.

Para cada `area.id` e cada `project.id`, garante que exista uma entrada
com o nome localizado em i18n/pt.yaml e i18n/en.yaml. Preserva formatação
e ordem via ruamel.yaml.

Uso:
    python3 scripts/update_i18n.py              # aplica (default)
    python3 scripts/update_i18n.py --check      # não escreve; falha se
                                                # divergente (para CI)
    python3 scripts/update_i18n.py --dry-run    # mostra o que mudaria,
                                                # sem escrever
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    from ruamel.yaml import YAML
except ImportError:
    print("ERRO: ruamel.yaml não instalado (pip install ruamel.yaml).", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
I18N_PATHS: dict[str, Path] = {
    "pt": REPO_ROOT / "i18n" / "pt.yaml",
    "en": REPO_ROOT / "i18n" / "en.yaml",
}


def _make_yaml() -> YAML:
    y = YAML()
    y.preserve_quotes = True
    y.indent(mapping=2, sequence=4, offset=2)
    return y


def compute_updates(
    areas_data: dict, projects_data: dict, i18n_data: dict, lang: str
) -> dict[str, str]:
    """Retorna {id: new_label} apenas para chaves faltando ou divergentes."""
    updates: dict[str, str] = {}
    for area in areas_data.get("areas", []) or []:
        aid = area.get("id")
        name = (area.get("name") or {}).get(lang)
        if aid and name and i18n_data.get(aid) != name:
            updates[aid] = name
    for project in projects_data.get("projects", []) or []:
        pid = project.get("id")
        name = (project.get("name") or {}).get(lang)
        if pid and name and i18n_data.get(pid) != name:
            updates[pid] = name
    return updates


def sync(check_only: bool = False, dry_run: bool = False) -> int:
    """Executa sync. Retorna 0 se em sync (ou sync aplicado); 1 se
    check_only e divergente."""
    yaml_ = _make_yaml()
    areas_data = yaml_.load((DATA_DIR / "areas.yaml").read_text(encoding="utf-8")) or {}
    projects_data = yaml_.load((DATA_DIR / "projects.yaml").read_text(encoding="utf-8")) or {}

    total_changes = 0
    for lang, path in I18N_PATHS.items():
        i18n_data = (
            yaml_.load(path.read_text(encoding="utf-8")) if path.exists() else {}
        ) or {}
        updates = compute_updates(areas_data, projects_data, i18n_data, lang)
        if not updates:
            continue
        total_changes += len(updates)
        for key, value in updates.items():
            action = "add" if key not in i18n_data else "upd"
            print(f"[{lang}] {action}: {key} = {value!r}")
            if not (check_only or dry_run):
                i18n_data[key] = value
        if not (check_only or dry_run):
            with path.open("w", encoding="utf-8") as f:
                yaml_.dump(i18n_data, f)

    if check_only and total_changes:
        print(f"i18n desatualizado ({total_changes} entrada(s)). Rode sem --check.")
        return 1
    if total_changes == 0:
        print("i18n já está sincronizado com areas.yaml e projects.yaml.")
    else:
        verb = "seriam" if dry_run else "foram"
        print(f"{total_changes} entrada(s) {verb} sincronizada(s).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="não escreve; falha se divergente")
    parser.add_argument("--dry-run", action="store_true", help="mostra sem escrever")
    args = parser.parse_args()
    return sync(check_only=args.check, dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
