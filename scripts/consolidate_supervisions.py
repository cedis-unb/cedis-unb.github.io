#!/usr/bin/env python3
"""Consolida entradas duplicadas em data/people.yaml usando `supervisions[]`.

Referência: passo 4b do roadmap de unificação de registro de colaboradores.

Detecção de duplicatas: entradas com o MESMO `slug:`. Para cada grupo,
mantém a primeira como "principal" e move as demais para dentro do
sub-array `supervisions:` da principal. Os campos por orientação (title,
program, advisors, tags, year, categories, summary, url) ficam DENTRO
das entries de supervisions. Os campos identitários (name, slug) ficam
apenas no nível principal.

Formato pré:
    - name: Mylena…
      slug: mylena_faria
      categories: [people, scientific_initiation]
      title: {...}
      program: ...
      advisors: [...]
      tags: [...]
      year: 2024

    - name: Mylena…
      slug: mylena_faria
      categories: [...]
      title: {...}
      ...

Formato pós:
    - name: Mylena…
      slug: mylena_faria
      supervisions:
        - categories: [people, scientific_initiation]
          title: {...}
          program: ...
          advisors: [...]
          tags: [...]
          year: 2024
        - categories: [...]
          title: {...}
          ...

Comportamento:
  --dry-run : mostra o plano (default)
  --apply   : reescreve data/people.yaml
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict, OrderedDict
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("ERRO: PyYAML não instalado.", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
PEOPLE_YAML = REPO_ROOT / "data" / "people.yaml"


# Campos que ficam NO NÍVEL PRINCIPAL (identidade da pessoa)
IDENTITY_FIELDS = {"name", "slug", "profile_level"}

# Todos os demais campos existentes viram parte de cada supervision.


def consolidate(entries: list) -> tuple[list, dict]:
    """Retorna (nova_lista_de_entradas, stats)."""
    by_slug = OrderedDict()  # slug -> [entries]
    stats = {"input": len(entries), "groups": 0, "collapsed": 0}

    for e in entries:
        slug = e.get("slug") or e.get("name") or "<unknown>"
        by_slug.setdefault(slug, []).append(e)

    new_entries = []
    for slug, group in by_slug.items():
        if len(group) == 1:
            new_entries.append(group[0])
            continue

        stats["groups"] += 1
        stats["collapsed"] += len(group)

        # entrada principal — herda name/slug/profile_level da primeira
        principal = OrderedDict()
        first = group[0]
        for f in ("name", "slug", "profile_level"):
            if f in first:
                principal[f] = first[f]

        # supervisions — cada entrada vira dict com todos campos não-identidade
        supervisions = []
        for e in group:
            sup = OrderedDict()
            for k, v in e.items():
                if k not in IDENTITY_FIELDS:
                    sup[k] = v
            supervisions.append(sup)

        principal["supervisions"] = supervisions
        new_entries.append(principal)

    stats["output"] = len(new_entries)
    return new_entries, stats


class _OrderedDumper(yaml.SafeDumper):
    pass


def _represent_odict(dumper, data):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())


_OrderedDumper.add_representer(OrderedDict, _represent_odict)


def process(apply: bool) -> int:
    text = PEOPLE_YAML.read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    entries = data.get("people", []) or []

    print(f"[people.yaml] {len(entries)} entradas de entrada\n")

    new_entries, stats = consolidate(entries)

    # Relatório
    print(f"Grupos consolidados: {stats['groups']}")
    print(f"Entradas removidas: {stats['collapsed'] - stats['groups']}")
    print(f"Total resultante: {stats['output']}\n")

    print("Detalhe dos grupos consolidados:")
    seen_output = OrderedDict()
    for e in new_entries:
        if "supervisions" in e:
            seen_output[e.get("slug", "?")] = len(e["supervisions"])
    for slug, n in seen_output.items():
        print(f"  · {slug}: {n} supervisions")

    if not apply:
        print("\n💡 Nada foi alterado. Rode com --apply para reescrever.")
        return 0

    # Escreve novo YAML — reescrita completa (perde comentários originais,
    # que já eram poucos neste arquivo). Backup implícito: git diff.
    new_data = {"people": new_entries}
    new_text = yaml.dump(
        new_data,
        Dumper=_OrderedDumper,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=200,
    )
    PEOPLE_YAML.write_text(new_text, encoding="utf-8")
    print(f"\n✓ data/people.yaml reescrito ({stats['output']} entradas).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    return process(args.apply)


if __name__ == "__main__":
    sys.exit(main())
