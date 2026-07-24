#!/usr/bin/env python3
"""Injeta `profile_level` no frontmatter dos arquivos content/people/*.md.

Referência: passo 3 do roadmap de unificação de registro de colaboradores.

Classificação declarativa (não muda comportamento hoje — prepara para
condicionais futuros nos templates):

  - `researcher`     — professor/pesquisador com produção contínua.
                       Detecção: `categories` contém "researcher".
  - `card_with_page` — colaborador com bio curta.
                       Detecção default para os demais casos.

Comportamento:
  --dry-run : mostra classificação e o que seria alterado (default)
  --apply   : injeta `profile_level:` (idempotente — não sobrescreve
              se já existir e for igual)

Não altera nenhum outro campo. `.en.md` e `.pt.md` do mesmo slug
recebem o mesmo `profile_level`.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("ERRO: PyYAML não instalado.", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
PEOPLE_DIR = REPO_ROOT / "content" / "people"


def classify(categories: list) -> str:
    if not categories:
        return "card_with_page"
    if "researcher" in categories:
        return "researcher"
    return "card_with_page"


def split_frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("sem frontmatter YAML delimitado por '---'")
    return m.group(1), m.group(2)


def inject_profile_level(fm_str: str, level: str) -> tuple[str, str]:
    """Retorna (novo_fm_str, action).

    action: 'insert' | 'update' | 'noop'
    """
    fm = yaml.safe_load(fm_str) or {}
    current = fm.get("profile_level")

    if current == level:
        return fm_str, "noop"

    lines = fm_str.split("\n")
    # remove eventual chave antiga
    lines = [l for l in lines if not re.match(r"^profile_level\s*:", l)]

    # insere após a linha `title:` se existir, senão no início
    insert_at = 0
    for i, l in enumerate(lines):
        if re.match(r"^title\s*:", l):
            insert_at = i + 1
            break
    lines.insert(insert_at, f"profile_level: {level}")

    action = "update" if current else "insert"
    return "\n".join(lines), action


def process_file(path: Path, apply: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    try:
        fm_str, body = split_frontmatter(text)
    except ValueError as e:
        return {"ok": False, "path": str(path.relative_to(REPO_ROOT)), "reason": str(e)}

    fm = yaml.safe_load(fm_str) or {}
    cats = fm.get("categories") or []
    level = classify(cats)

    new_fm, action = inject_profile_level(fm_str, level)

    if apply and action != "noop":
        path.write_text(f"---\n{new_fm}\n---\n{body}", encoding="utf-8")

    return {
        "ok": True,
        "path": str(path.relative_to(REPO_ROOT)),
        "level": level,
        "action": action,
        "current": fm.get("profile_level"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true", help="Executa (default: dry-run)")
    args = ap.parse_args()

    files = sorted(PEOPLE_DIR.glob("*.md"))
    # ignora _index e all
    files = [f for f in files if not f.name.startswith("_") and not f.stem.split(".")[0] == "all"]

    if not files:
        print("Nenhum arquivo elegível.")
        return 0

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"[{mode}] Processando {len(files)} arquivo(s) em {PEOPLE_DIR.relative_to(REPO_ROOT)}\n")

    results = [process_file(f, args.apply) for f in files]

    counts = {"insert": 0, "update": 0, "noop": 0, "fail": 0}
    per_level = {"researcher": [], "card_with_page": []}

    for r in results:
        if not r["ok"]:
            counts["fail"] += 1
            print(f"  ✗ FAIL  {r['path']}: {r['reason']}")
            continue
        counts[r["action"]] += 1
        per_level[r["level"]].append(r["path"])

    print("Por nível:")
    for lvl, paths in per_level.items():
        print(f"\n  {lvl} ({len(paths)}):")
        for p in paths:
            print(f"    · {p}")

    print(f"\nResumo: inseridos={counts['insert']}, atualizados={counts['update']}, "
          f"já-corretos={counts['noop']}, falhas={counts['fail']}")

    if not args.apply:
        print("\n💡 Nada foi alterado. Rode com --apply para executar.")

    return 0 if counts["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
