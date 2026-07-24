#!/usr/bin/env python3
"""Auto-derivação de coautores órfãos de data/productions.yaml.

Referência: passo 8 do roadmap de unificação de registro de colaboradores.

Para cada nome em authors[] de productions.yaml que NÃO tem correspondência
com registros existentes (advisors + content/people/*.md + data/people.yaml),
gera um stub .md em content/people/<slug>.{pt,en}.md com:
  - profile_level: derived
  - layout: derived
  - aliases_authors: [variações do nome vistas em authors[]]
  - matched_productions: lista pré-computada de {title, year, type} onde
    a pessoa aparece — permite ao template renderizar sem tocar productions.yaml

Clusterização: variações do mesmo nome (ABNT vs natural) são agrupadas
via abnt_forms. Uma pessoa = um cluster = um stub .md.

Prioridade de nome de exibição: forma natural (não-ABNT) mais completa.

Idempotência: sobrescreve stubs derivados existentes. NUNCA sobrescreve
arquivos que não têm `profile_level: derived` no frontmatter (proteção
para perfis reais).

Comportamento:
  --dry-run              : mostra o plano (default)
  --apply                : escreve/atualiza stubs
  --min-appearances N    : só cria stub se pessoa aparece em >= N produções (default: 1)
  --clean                : remove stubs derivados que ninguém mais aparece (limpa órfãos)
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_people_slugs import (  # noqa: E402
    canonicalize_author,
    abnt_forms,
    slugify,
    load_advisors,
    load_people_yaml,
    load_productions,
    load_person_md_files,
)


REPO_ROOT = Path(__file__).resolve().parent.parent
PEOPLE_DIR = REPO_ROOT / "content" / "people"


# ---------- helpers ----------

def build_known_map() -> dict:
    """canonical name -> slug, a partir das 3 fontes canônicas."""
    known = {}
    advisors = load_advisors()
    for slug, info in advisors.items():
        n = info.get("name", "")
        if n:
            known.setdefault(canonicalize_author(n), slug)
            for f in abnt_forms(n):
                known.setdefault(f, slug)
    for slug, info in load_person_md_files().items():
        for lang in ("pt", "en"):
            if lang in info["languages"]:
                fm = info["languages"][lang]["frontmatter"]
                n = fm.get("title", "")
                if n:
                    known.setdefault(canonicalize_author(n), slug)
                    for f in abnt_forms(n):
                        known.setdefault(f, slug)
    for entry in load_people_yaml():
        n = entry.get("name", "")
        s = entry.get("slug") or slugify(n)
        if n:
            known.setdefault(canonicalize_author(n), s)
            for f in abnt_forms(n):
                known.setdefault(f, s)
    return known


def display_name(variants: set[str]) -> str:
    """Escolhe a variação mais 'natural' para exibição.

    Prioriza: sem vírgula (não-ABNT) > mais tokens > menos maiúsculas.
    """
    ranked = sorted(
        variants,
        key=lambda v: (
            0 if "," in v else 1,          # sem vírgula primeiro
            len(v.split()),                 # mais tokens primeiro
            -sum(1 for c in v if c.isupper()),  # menos maiúsculas primeiro
        ),
        reverse=True,
    )
    return ranked[0]


def cluster_orphans(orphan_authors: dict) -> dict:
    """Agrupa variações de nome do mesmo indivíduo via abnt_forms.

    Input: {canonical_form: {'variants': [str], 'productions': [dict]}}
    Output: {cluster_slug: {'variants': set, 'productions': [dict], 'display': str}}
    """
    form_to_cluster = {}  # any form → cluster_id
    clusters = defaultdict(lambda: {"variants": set(), "productions": []})
    next_id = 0

    for canon, data in orphan_authors.items():
        # Compute all forms of any variant seen
        all_forms = {canon}
        for v in data["variants"]:
            all_forms |= abnt_forms(v)
            all_forms.add(canonicalize_author(v))

        # Find existing cluster
        cluster_id = None
        for f in all_forms:
            if f in form_to_cluster:
                cluster_id = form_to_cluster[f]
                break

        if cluster_id is None:
            cluster_id = next_id
            next_id += 1

        for f in all_forms:
            form_to_cluster[f] = cluster_id

        clusters[cluster_id]["variants"] |= data["variants"]
        clusters[cluster_id]["productions"].extend(data["productions"])

    # Dedup productions per cluster (same prod_idx)
    out = {}
    for cid, cdata in clusters.items():
        seen_idx = set()
        unique_prods = []
        for p in cdata["productions"]:
            if p["idx"] not in seen_idx:
                seen_idx.add(p["idx"])
                unique_prods.append(p)
        display = display_name(cdata["variants"])
        slug = slugify(display)
        # Guard contra colisão de slug entre clusters
        while slug in out:
            slug = slug + "_2"
        out[slug] = {
            "variants": cdata["variants"],
            "productions": unique_prods,
            "display": display,
        }
    return out


# ---------- stub io ----------

def is_derived_stub(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")[:800]
    return bool(re.search(r"^profile_level:\s*derived\s*$", text, re.M))


def is_real_profile(slug: str) -> bool:
    """True se existe .md pra este slug que NÃO é derived stub."""
    for suffix in (".pt.md", ".en.md"):
        p = PEOPLE_DIR / f"{slug}{suffix}"
        if p.exists() and not is_derived_stub(p):
            return True
    return False


class OrderedDumper(yaml.SafeDumper):
    pass


def _repr_odict(dumper, data):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())


OrderedDumper.add_representer(OrderedDict, _repr_odict)


def render_stub(slug: str, cluster: dict, lang: str) -> str:
    """Renderiza o texto do stub .md em português ou inglês."""
    variants = sorted(cluster["variants"])
    prods = cluster["productions"]
    display = cluster["display"]

    # Body copy simples localizada
    if lang == "pt":
        n = len(prods)
        prod_word = "produção" if n == 1 else "produções"
        body = (
            f"\nAutor(a) citado(a) em **{n} {prod_word}** do CEDIS.\n\n"
            f"Perfil detalhado ainda não disponível — as informações abaixo foram\n"
            f"derivadas automaticamente das produções onde o nome aparece como coautor.\n\n"
            f"É você e quer um perfil completo? [Contate o CEDIS](/junte-se/).\n"
        )
        summary = f"Coautor(a) citado(a) em {n} {prod_word} do CEDIS."
    else:
        n = len(prods)
        prod_word = "publication" if n == 1 else "publications"
        body = (
            f"\nCited as co-author in **{n} {prod_word}** by CEDIS.\n\n"
            f"Detailed profile not yet available — the information below was\n"
            f"automatically derived from the works where this name appears.\n\n"
            f"Is that you and want a full profile? [Contact CEDIS](/join/).\n"
        )
        summary = f"Co-author cited in {n} {prod_word} by CEDIS."

    fm = OrderedDict()
    fm["author"] = "CEDIS"
    fm["title"] = display
    fm["profile_level"] = "derived"
    fm["layout"] = "derived"
    fm["slug"] = slug
    fm["language"] = lang
    fm["summary"] = summary
    fm["authorimage"] = "../assets/images/global/author.webp"
    if variants:
        fm["aliases_authors"] = variants
    # matched_productions — lista já resolvida (título por lang, year, type)
    prod_entries = []
    for p in prods:
        entry = OrderedDict()
        title = p.get("title") or {}
        if isinstance(title, dict):
            t = title.get(lang) or title.get("pt") or title.get("en") or ""
        else:
            t = str(title)
        entry["title"] = t
        if p.get("year"):
            entry["year"] = p["year"]
        if p.get("type"):
            entry["type"] = p["type"]
        prod_entries.append(entry)
    fm["matched_productions"] = prod_entries

    fm_yaml = yaml.dump(
        fm,
        Dumper=OrderedDumper,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=200,
    )
    return f"---\n{fm_yaml}---\n{body}"


# ---------- main pipeline ----------

def process(apply: bool, min_appearances: int, clean: bool) -> int:
    known = build_known_map()
    productions = load_productions()

    print(f"[known map] {len(known)} formas canônicas indexadas")
    print(f"[productions] {len(productions)} itens\n")

    # Coleta órfãos
    orphan_by_canon = defaultdict(lambda: {"variants": set(), "productions": []})
    for i, prod in enumerate(productions):
        if not isinstance(prod, dict):
            continue
        for author in prod.get("authors", []) or []:
            if not author:
                continue
            canon = canonicalize_author(author)
            if not canon:
                continue
            if canon in known:
                continue
            forms = abnt_forms(author)
            if any(f in known for f in forms):
                continue
            orphan_by_canon[canon]["variants"].add(author)
            orphan_by_canon[canon]["productions"].append({
                "idx": i,
                "title": prod.get("title"),
                "year": prod.get("year"),
                "type": prod.get("type"),
            })

    print(f"[orphans] {len(orphan_by_canon)} formas canônicas órfãs (pré-cluster)")

    clusters = cluster_orphans(orphan_by_canon)
    print(f"[clusters] {len(clusters)} pessoas derivadas após clusterização")

    # Filtra por min_appearances
    filtered = {
        s: c for s, c in clusters.items()
        if len(c["productions"]) >= min_appearances
    }
    print(f"[filtered ≥{min_appearances}] {len(filtered)} pessoas passam threshold\n")

    # Sanity: guarda contra colisão com perfis reais
    to_write = {}
    skipped_real = []
    for slug, cluster in filtered.items():
        if is_real_profile(slug):
            skipped_real.append((slug, cluster["display"]))
            continue
        to_write[slug] = cluster

    if skipped_real:
        print(f"⚠  {len(skipped_real)} colisões com perfis reais — pulando:")
        for s, d in skipped_real[:10]:
            print(f"    · {s}: '{d}'")

    # Distribuição de contagem
    counts = defaultdict(int)
    for c in to_write.values():
        n = len(c["productions"])
        if n == 1: counts["1"] += 1
        elif n <= 3: counts["2-3"] += 1
        elif n <= 10: counts["4-10"] += 1
        else: counts["11+"] += 1
    print(f"\n[distribuição] pessoas por qtde de publicações:")
    for k in ("1", "2-3", "4-10", "11+"):
        print(f"    {k:5s}: {counts[k]}")

    # Amostras topo
    top = sorted(to_write.items(), key=lambda x: -len(x[1]["productions"]))[:15]
    print(f"\n[top 15 por publicações]:")
    for slug, c in top:
        print(f"    {len(c['productions']):3d}× {c['display']}  →  {slug}")

    # Clean pass: identifica stubs derivados existentes que não estão em to_write
    stale_stubs = []
    if PEOPLE_DIR.exists():
        for f in PEOPLE_DIR.glob("*.md"):
            m = re.match(r"^([a-zA-Z0-9_\-]+)\.(pt|en)\.md$", f.name)
            if not m:
                continue
            slug, _ = m.group(1), m.group(2)
            if is_derived_stub(f) and slug not in to_write:
                stale_stubs.append(f)

    if stale_stubs:
        print(f"\n[stale] {len(stale_stubs)} stubs derivados sem match atual "
              f"(remover com --clean):")
        for f in stale_stubs[:10]:
            print(f"    · {f.relative_to(REPO_ROOT)}")

    if not apply:
        print("\n💡 Nada foi alterado. Rode com --apply para escrever stubs.")
        return 0

    written = 0
    for slug, cluster in to_write.items():
        for lang in ("pt", "en"):
            path = PEOPLE_DIR / f"{slug}.{lang}.md"
            if path.exists() and not is_derived_stub(path):
                continue  # perfil real
            path.write_text(render_stub(slug, cluster, lang), encoding="utf-8")
            written += 1
    print(f"\n✓ {written} arquivos de stub gravados/atualizados.")

    if clean and stale_stubs:
        for f in stale_stubs:
            f.unlink()
        print(f"✓ {len(stale_stubs)} stubs stale removidos.")

    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--min-appearances", type=int, default=1)
    ap.add_argument("--clean", action="store_true",
                    help="Remove stubs derivados sem match atual")
    args = ap.parse_args()
    return process(args.apply, args.min_appearances, args.clean)


if __name__ == "__main__":
    sys.exit(main())
