"""Gera content/defesas/<id>.<lang>.md a partir de data/defesas.yaml.

Sprint 2 do PLANO-DEFESAS-2026.md.

Padrão idêntico a scripts/build_publications.py:
    - 1 arquivo MD por (defesa × idioma) com frontmatter mínimo.
    - Body vazio — layout renderiza tudo lendo site.Data.defesas via
      partials/defesa-body.html.
    - Aliases herdam do news_slug legado (posts defesa-*.md continuam
      redirecionando via alias 301).

Uso:
    python3 scripts/build_defesas.py            # gera content/defesas/
    python3 scripts/build_defesas.py --check    # falha se dessincronizado
"""
from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFESAS_DATA = ROOT / "data" / "defesas.yaml"
OUT_DIR = ROOT / "content" / "defesas"
LANGS = ("pt", "en")


def _load() -> list[dict]:
    data = yaml.safe_load(DEFESAS_DATA.read_text(encoding="utf-8")) or []
    if not isinstance(data, list):
        raise SystemExit(f"{DEFESAS_DATA}: esperava lista raiz")
    return data


def _title_for(entry: dict, lang: str) -> str:
    t = entry.get("title") or {}
    val = t.get(lang) or t.get("pt") or t.get("en") or entry["id"]
    return str(val).replace('"', '\\"')


def _aliases_for(entry: dict, lang: str) -> list[str]:
    """Aliases 301 para preservar URLs dos posts legados.

    Retorna [] enquanto os posts .md existirem — Hugo prioriza a página
    existente sobre alias, então o alias silenciosamente perde. O Sprint 5
    do PLANO-DEFESAS-2026 deleta os posts e reativa esses aliases.
    """
    return []


def _frontmatter(entry: dict, lang: str) -> str:
    title = _title_for(entry, lang)
    aliases = _aliases_for(entry, lang)
    scheduled = entry.get("scheduled_date") or ""
    lines: list[str] = ["---"]
    lines.append(f'title: "{title}"')
    # `date` no frontmatter é usado por Hugo para publicação; usar
    # scheduled_date fará Hugo esconder defesas upcoming (data futura) por
    # default. Fixamos date=1970-01-01 e mantemos scheduled_date em Params
    # para ordenação/renderização. Alternativa seria buildFuture: true, mas
    # ele afeta todo o site e traz risco de expor drafts.
    lines.append(f'date: 1970-01-01T00:00:00Z')
    lines.append(f'scheduled_date: {scheduled}')
    lines.append(f'draft: false')
    lines.append(f'language: {lang}')
    lines.append(f'translationKey: "defesa-{entry["id"]}"')
    lines.append(f'canonical_source: data/defesas.yaml')
    lines.append(f'defesa_id: "{entry["id"]}"')
    if aliases:
        lines.append("aliases:")
        for a in aliases:
            lines.append(f"  - {a}")
    lines.append("---")
    return "\n".join(lines)


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return
    path.write_text(content, encoding="utf-8")


def build(out_dir: Path) -> int:
    entries = _load()
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # _index para a section (lista) — em ambos idiomas.
    for lang in LANGS:
        idx_path = out_dir / (f"_index.{lang}.md")
        idx_title = "Defesas" if lang == "pt" else "Defenses"
        idx_fm = "\n".join([
            "---",
            f'title: "{idx_title}"',
            f'language: {lang}',
            'translationKey: defesas-index',
            "---",
        ])
        _write(idx_path, idx_fm + "\n")

    count = 0
    for e in entries:
        slug = e["id"]
        for lang in LANGS:
            path = out_dir / f"{slug}.{lang}.md"
            _write(path, _frontmatter(e, lang) + "\n")
            count += 1
    return count


def _snapshot(root: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    if not root.exists():
        return files
    for p in sorted(root.rglob("*")):
        if p.is_file():
            files[p.relative_to(root).as_posix()] = p.read_bytes()
    return files


def check() -> int:
    with tempfile.TemporaryDirectory(prefix="cedis-defesas-") as tmp:
        expected = Path(tmp) / "defesas"
        build(expected)
        exp = _snapshot(expected)
        cur = _snapshot(OUT_DIR)
    missing = sorted(set(exp) - set(cur))
    extra = sorted(set(cur) - set(exp))
    changed = sorted(p for p in set(exp) & set(cur) if exp[p] != cur[p])
    if not (missing or extra or changed):
        print("content/defesas está sincronizado com data/defesas.yaml.")
        return 0
    print("content/defesas está divergente de data/defesas.yaml.")
    for label, paths in (("faltando", missing), ("extra", extra), ("alterado", changed)):
        if paths:
            sample = ", ".join(paths[:6])
            suffix = "" if len(paths) <= 6 else f" ... (+{len(paths) - 6})"
            print(f"- {label}: {len(paths)} arquivo(s): {sample}{suffix}")
    print("Rode: python3 scripts/build_defesas.py")
    return 1


def _cli() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="não escreve, só compara")
    args = ap.parse_args()
    if args.check:
        return check()
    n = build(OUT_DIR)
    print(f"Geradas {n} páginas de defesa em {OUT_DIR}.")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
