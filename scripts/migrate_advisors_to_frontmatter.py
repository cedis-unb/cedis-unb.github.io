#!/usr/bin/env python3
"""[HISTÓRICO — NÃO EXECUTAR] Migração one-shot do passo 9.

Copiava contato (email/lattes/orcid) e áreas de data/advisors.yaml para
o frontmatter dos .md em content/people/. Executado em 2026-07-23.

**Este script não funciona mais**: data/advisors.yaml foi removido no
Gap #1 (2026-07-24). Contato e áreas agora vivem apenas no frontmatter
dos .md e são consumidos via `partial "people-lookup"`.

Mantido no repositório como referência histórica do refactor.
Se precisar reproduzir a migração, restaure `data/advisors.yaml` de
`git show HEAD~N:data/advisors.yaml` antes de rodar.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import OrderedDict
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("ERRO: PyYAML não instalado.", file=sys.stderr)
    sys.exit(2)


# Guard-rail: falhar cedo se advisors.yaml não existir mais
if not (Path(__file__).resolve().parent.parent / "data" / "advisors.yaml").exists():
    print("ERRO: data/advisors.yaml não existe. Este script é histórico "
          "e só funciona antes do Gap #1 (2026-07-24). Ver docstring.",
          file=sys.stderr)
    sys.exit(3)


REPO_ROOT = Path(__file__).resolve().parent.parent
ADVISORS_YAML = REPO_ROOT / "data" / "advisors.yaml"
PEOPLE_DIR = REPO_ROOT / "content" / "people"


def split_frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("sem frontmatter YAML delimitado por '---'")
    return m.group(1), m.group(2)


class OrderedDumper(yaml.SafeDumper):
    pass


def _repr_odict(dumper, data):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())


OrderedDumper.add_representer(OrderedDict, _repr_odict)


def inject_fields(fm_str: str, contact: dict, areas: list) -> tuple[str, str]:
    """Insere/atualiza `contact:` e `areas:` no frontmatter. Retorna
    (novo_fm, action) onde action ∈ {'insert', 'update', 'noop'}."""
    fm = yaml.safe_load(fm_str) or {}

    existing_contact = fm.get("contact") or {}
    existing_areas = fm.get("areas") or []

    changed = False
    if existing_contact != contact:
        changed = True
    if list(existing_areas) != list(areas):
        changed = True

    if not changed:
        return fm_str, "noop"

    # Reconstroi frontmatter mantendo ordem, removendo entradas antigas
    lines = fm_str.split("\n")
    out = []
    skip_block = False
    for line in lines:
        # Detecta início de bloco `contact:` ou `areas:` antigos — remove-os
        if re.match(r"^contact\s*:\s*($|\{)", line) or re.match(r"^areas\s*:\s*($|\[)", line):
            skip_block = True
            continue
        if skip_block:
            # continuar pulando até encontrar linha que não seja item aninhado
            if re.match(r"^[a-zA-Z_]", line):
                skip_block = False
            else:
                continue
        out.append(line)

    # Anexa contact + areas novos após `title:` se possível, senão ao fim
    insert_at = len(out)
    for i, l in enumerate(out):
        if re.match(r"^summary\s*:", l) or re.match(r"^authorimage\s*:", l):
            insert_at = i + 1
            break

    contact_yaml = yaml.dump(
        {"contact": contact},
        Dumper=OrderedDumper,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).rstrip("\n")
    areas_yaml = yaml.dump(
        {"areas": areas},
        Dumper=OrderedDumper,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).rstrip("\n")

    new_block = contact_yaml.split("\n") + areas_yaml.split("\n")
    out = out[:insert_at] + new_block + out[insert_at:]

    action = "update" if existing_contact or existing_areas else "insert"
    return "\n".join(out), action


def find_md_for_advisor(advisor_slug: str) -> list[tuple[Path, str]]:
    """Retorna [(path, lang)] dos .md que correspondem ao slug do advisor.

    Primeiro tenta match direto pelo nome do arquivo. Se não achar,
    varre content/people/*.md procurando quem tem o slug do advisor
    em `categories` — cobre casos de rename entre slugs antigos e canônicos.
    """
    direct = []
    for lang in ("pt", "en"):
        p = PEOPLE_DIR / f"{advisor_slug}.{lang}.md"
        if p.exists():
            direct.append((p, lang))
    if direct:
        return direct

    # Fallback: procura por categoria
    matches = []
    for f in PEOPLE_DIR.glob("*.md"):
        m = re.match(r"^([a-zA-Z0-9_\-]+)\.(pt|en)\.md$", f.name)
        if not m:
            continue
        try:
            text = f.read_text(encoding="utf-8")
            fm_str, _ = split_frontmatter(text)
            fm = yaml.safe_load(fm_str) or {}
            cats = fm.get("categories") or []
            if advisor_slug in cats:
                matches.append((f, m.group(2)))
        except Exception:
            continue
    return matches


def process(apply: bool) -> int:
    advisors = yaml.safe_load(ADVISORS_YAML.read_text(encoding="utf-8")).get("advisors", {}) or {}

    print(f"[advisors.yaml] {len(advisors)} advisors\n")

    counts = {"insert": 0, "update": 0, "noop": 0, "no_md": 0}
    per_slug = {}

    for slug, info in advisors.items():
        contact = OrderedDict()
        if info.get("email"): contact["email"] = info["email"]
        if info.get("lattes"): contact["lattes"] = info["lattes"]
        if info.get("orcid"): contact["orcid"] = info["orcid"]
        areas = info.get("areas") or []

        per_slug[slug] = {"contact": contact, "areas": areas, "actions": {}}

        md_files = find_md_for_advisor(slug)
        if not md_files:
            counts["no_md"] += 1
            continue

        for path, lang in md_files:
            text = path.read_text(encoding="utf-8")
            fm_str, body = split_frontmatter(text)
            new_fm, action = inject_fields(fm_str, dict(contact), areas)
            per_slug[slug]["actions"][f"{path.stem.split('.')[0]}[{lang}]"] = action
            counts[action] += 1
            if apply and action != "noop":
                path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")

    print("Resultado por slug:")
    for slug, data in per_slug.items():
        acts = data["actions"]
        if not acts:
            status = "sem .md (advisor sem página)"
        else:
            status = " · ".join(f"{k}={v}" for k, v in acts.items())
        print(f"  {slug:30s} → {status}")

    print(f"\nResumo: {counts}")

    if not apply:
        print("\n💡 Nada foi alterado. Rode com --apply.")

    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    return process(args.apply)


if __name__ == "__main__":
    sys.exit(main())
