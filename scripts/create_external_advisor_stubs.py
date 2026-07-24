#!/usr/bin/env python3
"""[HISTÓRICO — NÃO EXECUTAR] Passo prévio do Gap #1 (2026-07-24).

Criava .md stubs para os 6 advisors externos que existiam em
data/advisors.yaml sem página própria. Executado uma vez antes de
`data/advisors.yaml` ser deletado.

**Este script não funciona mais**: advisors.yaml foi removido no Gap #1.
Os 6 stubs criados por ele estão em `content/people/` com
`profile_level: advisor_only`:
  andrea_cabello, berilhes_garcia, edna_canedo,
  marilia_miranda, claudia_ochoa, celia_higawa

Mantido no repositório como referência histórica.
Se precisar adicionar novos advisors externos, crie o .md manualmente
seguindo o padrão dos existentes (não precisa mais deste script).
"""

from __future__ import annotations

import argparse
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
          "e só funciona antes do Gap #1. Crie novos stubs manualmente.",
          file=sys.stderr)
    sys.exit(3)


REPO_ROOT = Path(__file__).resolve().parent.parent
ADVISORS_YAML = REPO_ROOT / "data" / "advisors.yaml"
PEOPLE_DIR = REPO_ROOT / "content" / "people"

# Slugs que NÃO devem ganhar stub (já cobertos por outros mecanismos)
SKIP = {
    "sergio_freitas", "cristiane_ramos", "andre_lanna",
    "george_marsicano", "fabiana_mendes", "ricardo_ajax",
    "daniel_sundfeld",
}


class OrderedDumper(yaml.SafeDumper):
    pass


def _repr_odict(dumper, data):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())


OrderedDumper.add_representer(OrderedDict, _repr_odict)


def render_stub(slug: str, info: dict, lang: str) -> str:
    name = info.get("name", "")
    lattes = info.get("lattes")
    orcid = info.get("orcid")
    email = info.get("email")
    areas = info.get("areas") or []

    fm = OrderedDict()
    fm["author"] = "CEDIS"
    fm["title"] = name
    fm["profile_level"] = "advisor_only"
    fm["layout"] = "derived"
    fm["slug"] = slug
    fm["language"] = lang
    if lang == "pt":
        fm["summary"] = f"Colaborador(a) externo(a) em orientações e projetos do CEDIS."
    else:
        fm["summary"] = f"External collaborator in CEDIS supervisions and projects."
    fm["authorimage"] = "../assets/images/global/author.webp"

    contact = OrderedDict()
    if email: contact["email"] = email
    if lattes: contact["lattes"] = lattes
    if orcid: contact["orcid"] = orcid
    if contact: fm["contact"] = contact
    if areas: fm["areas"] = areas
    fm["matched_productions"] = []  # placeholder — advisor_only não lista pubs

    fm_yaml = yaml.dump(
        fm,
        Dumper=OrderedDumper,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=200,
    )

    if lang == "pt":
        body = (
            "\nColaborador(a) externo(a) que atua em co-orientações e projetos\n"
            "conjuntos com pesquisadores do CEDIS.\n"
        )
    else:
        body = (
            "\nExternal collaborator active in co-supervisions and joint\n"
            "projects with CEDIS researchers.\n"
        )

    return f"---\n{fm_yaml}---\n{body}"


def process(apply: bool) -> int:
    advisors = yaml.safe_load(ADVISORS_YAML.read_text(encoding="utf-8")).get("advisors", {}) or {}

    to_create = []
    skipped = []
    for slug, info in advisors.items():
        if slug in SKIP:
            skipped.append(slug)
            continue
        # Já tem .md?
        has_md = any((PEOPLE_DIR / f"{slug}.{l}.md").exists() for l in ("pt", "en"))
        if has_md:
            skipped.append(f"{slug} (já tem .md)")
            continue
        to_create.append((slug, info))

    print(f"[advisors.yaml] {len(advisors)} advisors")
    print(f"[skip] {len(skipped)}: {skipped}\n")
    print(f"[criar] {len(to_create)} stubs (× 2 idiomas = {len(to_create)*2} arquivos):")
    for slug, info in to_create:
        print(f"  · {slug} — {info.get('name','?')}")

    if not apply:
        print("\n💡 Nada foi alterado. Rode com --apply.")
        return 0

    written = 0
    for slug, info in to_create:
        for lang in ("pt", "en"):
            path = PEOPLE_DIR / f"{slug}.{lang}.md"
            if path.exists():
                continue
            path.write_text(render_stub(slug, info, lang), encoding="utf-8")
            written += 1
    print(f"\n✓ {written} stubs criados.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    return process(args.apply)


if __name__ == "__main__":
    sys.exit(main())
