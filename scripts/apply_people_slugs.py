#!/usr/bin/env python3
"""Adiciona `slug:` explícito a cada entrada de `data/people.yaml`.

Referência: passo 4a do roadmap de unificação de registro de colaboradores.

Estratégia de resolução do slug (em ordem de prioridade):
  1. Match exato do nome canônico contra slug de content/people/*.md
  2. Match via formas ABNT (via módulo normalize_people_slugs)
  3. Match "primeiro nome + último sobrenome" contra slug de .md
  4. Similaridade ≥ 0.86 contra title dos .md
  5. Fallback: slug longo derivado do nome completo (underscore)

Se múltiplos .md matcham (ambíguo), usa o slug longo do fallback e
adiciona à lista de ambíguos no relatório.

Zero impacto em templates: `slug:` é apenas leitura futura pelo
partial people-lookup (passo 5). Nenhum consumidor atual quebra.

Comportamento:
  --dry-run : mostra plano (default)
  --apply   : escreve data/people.yaml com `slug:` injetado
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("ERRO: PyYAML não instalado.", file=sys.stderr)
    sys.exit(2)

# reusa lógica ABNT do diagnóstico
sys.path.insert(0, str(Path(__file__).resolve().parent))
from normalize_people_slugs import canonicalize_author, abnt_forms, slugify  # noqa: E402


REPO_ROOT = Path(__file__).resolve().parent.parent
PEOPLE_YAML = REPO_ROOT / "data" / "people.yaml"
PEOPLE_DIR = REPO_ROOT / "content" / "people"

PARTICLES = {"de", "da", "do", "das", "dos", "e", "del", "della", "van", "von", "junior", "jr", "filho", "neto"}


def load_md_slugs() -> dict:
    """Retorna {md_slug: {title_pt, title_en}} para os .md existentes."""
    out = {}
    for md in PEOPLE_DIR.glob("*.md"):
        m = re.match(r"^([a-zA-Z0-9_\-]+)\.(pt|en)\.md$", md.name)
        if not m:
            continue
        slug, lang = m.group(1), m.group(2)
        if slug == "all":
            continue
        txt = md.read_text(encoding="utf-8")
        fmm = re.match(r"^---\n(.*?)\n---", txt, re.S)
        if not fmm:
            continue
        try:
            fm = yaml.safe_load(fmm.group(1)) or {}
        except Exception:
            continue
        out.setdefault(slug, {"pt": None, "en": None})
        out[slug][lang] = fm.get("title") or ""
    return out


def short_slug(name: str) -> str:
    """Gera slug 'primeiro + último sobrenome' (padrão comum dos .md)."""
    n = unicodedata.normalize("NFKD", name)
    n = "".join(c for c in n if not unicodedata.combining(c)).lower()
    n = re.sub(r"[^a-z\s]+", " ", n).strip()
    parts = [p for p in n.split() if p and (len(p) == 1 or p not in PARTICLES)]
    if len(parts) < 2:
        return slugify(name)
    return f"{parts[0]}_{parts[-1]}"


def resolve_slug(name: str, md_slugs: dict, md_canonicals: dict) -> tuple[str, str, list[str]]:
    """Retorna (slug, resolucao, matches_ambiguos).

    resolucao: 'md_exact' | 'md_abnt' | 'md_short' | 'md_similar' | 'long_fallback'
    """
    if not name:
        return "unknown", "empty_name", []

    canon = canonicalize_author(name)

    # 1) match exato no canônico
    exact = [slug for slug, cans in md_canonicals.items() if canon in cans]
    if len(exact) == 1:
        return exact[0], "md_exact", []
    if len(exact) > 1:
        return slugify(name), "long_fallback", exact

    # 2) match via formas ABNT
    abnt = abnt_forms(name)
    abnt_hit = set()
    for slug, cans in md_canonicals.items():
        if cans & abnt:
            abnt_hit.add(slug)
    if len(abnt_hit) == 1:
        return next(iter(abnt_hit)), "md_abnt", []
    if len(abnt_hit) > 1:
        return slugify(name), "long_fallback", sorted(abnt_hit)

    # 3) match primeiro+último sobrenome
    candidate = short_slug(name)
    if candidate in md_slugs:
        return candidate, "md_short", []

    # 4) fuzzy similarity ≥ 0.86 contra titles
    scored = []
    for slug, cans in md_canonicals.items():
        for c in cans:
            r = SequenceMatcher(None, canon, c).ratio()
            if r >= 0.86:
                scored.append((r, slug))
    if scored:
        scored.sort(reverse=True)
        top_score = scored[0][0]
        top_slugs = list({s for r, s in scored if r == top_score})
        if len(top_slugs) == 1:
            return top_slugs[0], "md_similar", []
        return slugify(name), "long_fallback", top_slugs

    # 5) fallback: slug longo
    return slugify(name), "long_fallback", []


def build_md_canonicals(md_slugs: dict) -> dict:
    """Para cada slug de .md, um set de formas canônicas do title (todos idiomas)."""
    out = {}
    for slug, titles in md_slugs.items():
        cans = set()
        for lang in ("pt", "en"):
            t = titles.get(lang) or ""
            if t:
                cans.add(canonicalize_author(t))
                cans |= abnt_forms(t)
        out[slug] = cans
    return out


def process(apply: bool) -> int:
    md_slugs = load_md_slugs()
    md_canonicals = build_md_canonicals(md_slugs)

    print(f"[.md carregados] {len(md_slugs)} slugs em content/people/")
    for s in sorted(md_slugs.keys()):
        print(f"  · {s}")
    print()

    text = PEOPLE_YAML.read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    entries = data.get("people", []) or []
    print(f"[people.yaml] {len(entries)} entradas\n")

    # Resolve slug para cada entrada
    resolutions = []
    for entry in entries:
        name = entry.get("name", "")
        slug, resolution, ambiguous = resolve_slug(name, md_slugs, md_canonicals)
        resolutions.append({
            "name": name,
            "slug": slug,
            "resolution": resolution,
            "ambiguous": ambiguous,
            "entry": entry,
        })

    # Sumários
    by_resolution = {}
    for r in resolutions:
        by_resolution.setdefault(r["resolution"], []).append(r)

    print("Resolução por método:")
    for method, rs in sorted(by_resolution.items(), key=lambda x: -len(x[1])):
        print(f"  {method:16s}  {len(rs)}")
    print()

    # Amostra de matches com .md (validação humana)
    print("Amostra: entradas que mapearam para slug de .md (top 20):")
    md_matches = [r for r in resolutions if r["resolution"].startswith("md_")]
    for r in md_matches[:20]:
        print(f"  \"{r['name']}\" → {r['slug']}  ({r['resolution']})")
    print(f"  ... total {len(md_matches)} matches com .md")
    print()

    # Casos ambíguos
    amb = [r for r in resolutions if r["ambiguous"]]
    print(f"Casos ambíguos (múltiplos .md matcham): {len(amb)}")
    for r in amb:
        print(f"  \"{r['name']}\" ambíguo entre {r['ambiguous']} → usando {r['slug']}")
    print()

    # Duplicatas de slug canônico
    from collections import Counter
    counts = Counter(r["slug"] for r in resolutions)
    dups = {s: n for s, n in counts.items() if n > 1}
    print(f"Slugs canônicos com múltiplas entradas (candidatos a supervisions[]): {len(dups)}")
    for s, n in sorted(dups.items(), key=lambda x: -x[1]):
        names = sorted({r["name"] for r in resolutions if r["slug"] == s})
        print(f"  {s}  ({n}×): {names}")
    print()

    if not apply:
        print("💡 Nada foi alterado. Rode com --apply para injetar `slug:` no YAML.")
        return 0

    # Injetar `slug:` no início de cada entrada — reescrita textual do YAML
    # para preservar ordem/comentários. Estratégia: para cada `- name: X`
    # inserir a linha `  slug: <slug>` na linha seguinte (se não existir).
    lines = text.split("\n")
    new_lines = []
    i = 0
    idx_entry = 0

    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        # heurística: início de entrada é `- name:`
        if re.match(r"^-\s+name:\s", line):
            # próxima linha existente é slug?
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if not re.match(r"^\s+slug:\s", next_line):
                slug = resolutions[idx_entry]["slug"]
                new_lines.append(f"  slug: {slug}")
            else:
                # substitui slug existente
                slug = resolutions[idx_entry]["slug"]
                new_lines.append(f"  slug: {slug}")
                i += 1  # pula linha antiga
            idx_entry += 1

        i += 1

    new_text = "\n".join(new_lines)
    PEOPLE_YAML.write_text(new_text, encoding="utf-8")
    print(f"✓ data/people.yaml atualizado — {idx_entry} entradas com slug injetado.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    return process(args.apply)


if __name__ == "__main__":
    sys.exit(main())
