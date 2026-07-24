#!/usr/bin/env python3
"""Move slugs-de-pessoa de tags[] para novo campo people[] em productions.yaml.

Referência: passo 10 do roadmap de unificação de registro de colaboradores.

Motivação: hoje o mesmo array tags[] mistura tópicos (gamification, ai),
projetos (project_cc, dfcris) e pessoas (sergio_freitas, cristiane_ramos).
Isso causa fallback "Tags" nas páginas de taxonomia /tags/<slug>/ e
sobrecarga semântica. A separação em people[] permite:
  - Filtros mais claros (autor vs tópico)
  - Templates iteram só sobre o campo apropriado
  - Diagnóstico de dados mais preciso

Determinação de "slug é de pessoa": qualquer slug que aparece como nome
de arquivo em content/people/*.md OU como campo `slug:` em data/people.yaml.

Comportamento:
  --dry-run : mostra o que seria alterado (default)
  --apply   : reescreve data/productions.yaml
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict, OrderedDict
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("ERRO: PyYAML não instalado.", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
PRODUCTIONS = REPO_ROOT / "data" / "productions.yaml"
PEOPLE_DIR = REPO_ROOT / "content" / "people"
PEOPLE_YAML = REPO_ROOT / "data" / "people.yaml"


def build_known_person_slugs() -> set[str]:
    slugs = set()
    # content/people/*.md
    for f in PEOPLE_DIR.glob("*.md"):
        m = re.match(r"^([a-zA-Z0-9_\-]+)\.(pt|en)\.md$", f.name)
        if m and m.group(1) != "all":
            slugs.add(m.group(1))
    # data/people.yaml
    py = yaml.safe_load(PEOPLE_YAML.read_text(encoding="utf-8")) or {}
    for entry in (py.get("people") or []):
        s = entry.get("slug")
        if s:
            slugs.add(s)
    return slugs


class OrderedDumper(yaml.SafeDumper):
    pass


def _repr_odict(dumper, data):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())


OrderedDumper.add_representer(OrderedDict, _repr_odict)


def process(apply: bool) -> int:
    known = build_known_person_slugs()
    print(f"[known person slugs] {len(known)} slugs (.md + people.yaml)\n")

    data = yaml.safe_load(PRODUCTIONS.read_text(encoding="utf-8"))
    if isinstance(data, list):
        items = data
        wrapper = None
    elif isinstance(data, dict):
        wrapper = None
        for k, v in data.items():
            if isinstance(v, list):
                items = v
                wrapper = k
                break
        else:
            print("ERRO: estrutura de productions.yaml não reconhecida", file=sys.stderr)
            return 2
    else:
        print("ERRO: raiz não é list nem dict", file=sys.stderr)
        return 2

    print(f"[productions] {len(items)} itens\n")

    moved = defaultdict(int)  # slug -> ocorrências movidas
    productions_touched = 0

    new_items = []
    for prod in items:
        if not isinstance(prod, dict):
            new_items.append(prod)
            continue
        tags = prod.get("tags") or []
        people = prod.get("people") or []
        # Já é lista? Faz cópia
        people = list(people) if people else []

        remaining_tags = []
        touched = False
        for tag in tags:
            if tag in known:
                if tag not in people:
                    people.append(tag)
                moved[tag] += 1
                touched = True
            else:
                remaining_tags.append(tag)

        # Reconstroi mantendo ordem de chaves
        new_prod = OrderedDict()
        for k, v in prod.items():
            if k == "tags":
                new_prod["tags"] = remaining_tags
                if people:
                    new_prod["people"] = people
            elif k == "people":
                pass  # já tratado junto com tags
            else:
                new_prod[k] = v

        # Se nunca teve tags mas ganhou people, insere
        if people and "tags" not in prod:
            new_prod["people"] = people

        if touched:
            productions_touched += 1

        new_items.append(new_prod)

    print(f"Productions modificadas: {productions_touched}/{len(items)}")
    print(f"\nTop 20 slugs movidos (por ocorrências):")
    for slug, count in sorted(moved.items(), key=lambda x: -x[1])[:20]:
        print(f"  {count:3d}× {slug}")

    total_moves = sum(moved.values())
    print(f"\nTotal: {total_moves} tags → people em {len(moved)} slugs distintos")

    if not apply:
        print("\n💡 Nada foi alterado. Rode com --apply.")
        return 0

    # Escrita
    if wrapper is None:
        out = new_items
    else:
        out = {wrapper: new_items}

    yaml_text = yaml.dump(
        out,
        Dumper=OrderedDumper,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=200,
    )
    PRODUCTIONS.write_text(yaml_text, encoding="utf-8")
    print(f"\n✓ data/productions.yaml reescrito com campo people[].")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    return process(args.apply)


if __name__ == "__main__":
    sys.exit(main())
