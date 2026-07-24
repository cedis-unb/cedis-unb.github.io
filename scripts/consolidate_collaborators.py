#!/usr/bin/env python3
"""Move content/people/collaborators/*.md → content/people/*.md preservando
URLs antigas via `aliases`.

Referência: passo 2 do roadmap de unificação de registro de colaboradores.
Consolidação estrutural — o diretório `/collaborators/` deixa de existir
como distinção de conteúdo (o nível é declarado por `profile_level` no
frontmatter, futuramente).

Comportamento:
  --dry-run : mostra o que seria feito, não altera nada (default)
  --apply   : executa a migração

Para cada arquivo em content/people/collaborators/<slug>.<lang>.md:
  1. Adiciona `aliases: - /people/collaborators/<slug>/` no frontmatter
     (idempotente — não duplica se já existir).
  2. Grava em content/people/<slug>.<lang>.md.
  3. Remove o arquivo original.

Ao final, remove o diretório collaborators/ se ficar vazio.

Templates de layout: nada a mudar. layouts/projects/single.html:154-162 e
layouts/areas/single.html:56-64 já fazem lookup em /people/<slug> primeiro
e caem em /people/collaborators/<slug> como fallback — a busca nova vai
resolver direto.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("ERRO: PyYAML não instalado.", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "content" / "people" / "collaborators"
DST_DIR = REPO_ROOT / "content" / "people"


def split_frontmatter(text: str) -> tuple[str, str]:
    """Retorna (frontmatter_yaml_str, body). Assume delimitador '---\\n'."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("Arquivo sem frontmatter YAML delimitado por '---'")
    return m.group(1), m.group(2)


def inject_alias(frontmatter_str: str, alias: str) -> tuple[str, bool]:
    """Adiciona `alias` a `aliases:` no frontmatter. Retorna (novo_texto, mudou)."""
    fm = yaml.safe_load(frontmatter_str) or {}
    aliases = fm.get("aliases") or []
    if not isinstance(aliases, list):
        aliases = [aliases]
    if alias in aliases:
        return frontmatter_str, False
    aliases.append(alias)
    fm["aliases"] = aliases

    # Preservar ordem original de campos + inserir aliases numa posição
    # razoável (após title/date se existir). Reconstruir manualmente por
    # simplicidade — round-trip com PyYAML perde ordem/comentários; mas o
    # frontmatter destes .md é pequeno e regular.
    out_lines = []
    inserted = False
    for line in frontmatter_str.split("\n"):
        # remove qualquer bloco `aliases:` antigo — vamos reescrever no fim
        if re.match(r"^aliases:\s*($|\[)", line):
            continue
        if line.startswith("- ") and out_lines and out_lines[-1].startswith("aliases:"):
            # linha de item de lista sob aliases antigo — pular
            continue
        out_lines.append(line)

    # Reescreve `aliases:` no formato canônico ao fim do frontmatter
    out_lines.append("aliases:")
    for a in aliases:
        out_lines.append(f"  - {a}")

    return "\n".join(out_lines), True


def migrate_file(src: Path, dst_dir: Path, apply: bool) -> dict:
    text = src.read_text(encoding="utf-8")
    fm_str, body = split_frontmatter(text)

    # Deriva slug do nome do arquivo: <slug>.<lang>.md
    m = re.match(r"^([a-zA-Z0-9_\-]+)\.(pt|en)\.md$", src.name)
    if not m:
        return {"ok": False, "src": str(src), "reason": "nome fora do padrão"}
    slug, lang = m.group(1), m.group(2)

    alias = f"/people/collaborators/{slug}/"
    new_fm_str, changed = inject_alias(fm_str, alias)

    dst = dst_dir / src.name
    if dst.exists():
        return {"ok": False, "src": str(src), "dst": str(dst),
                "reason": "arquivo de destino já existe"}

    new_text = f"---\n{new_fm_str}\n---\n{body}"

    action = "MOVE+INJECT" if changed else "MOVE (alias já existia)"

    if apply:
        dst.write_text(new_text, encoding="utf-8")
        src.unlink()

    return {"ok": True, "src": str(src.relative_to(REPO_ROOT)),
            "dst": str(dst.relative_to(REPO_ROOT)), "action": action,
            "alias": alias}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true",
                    help="Executa a migração (default: dry-run)")
    args = ap.parse_args()

    if not SRC_DIR.exists():
        print(f"Nada a fazer: {SRC_DIR} não existe.")
        return 0

    files = sorted(SRC_DIR.glob("*.md"))
    if not files:
        print(f"Nada a fazer: {SRC_DIR} vazio.")
        return 0

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"[{mode}] Migrando {len(files)} arquivo(s) de {SRC_DIR.relative_to(REPO_ROOT)}\n")

    results = [migrate_file(f, DST_DIR, args.apply) for f in files]

    ok = [r for r in results if r["ok"]]
    fail = [r for r in results if not r["ok"]]

    for r in ok:
        print(f"  ✓ {r['action']:26s} {r['src']} → {r['dst']}")
        print(f"      alias: {r['alias']}")

    for r in fail:
        print(f"  ✗ FAIL  {r['src']}: {r['reason']}")

    print(f"\n{len(ok)} sucesso(s), {len(fail)} falha(s).")

    if args.apply and not fail:
        # remove diretório se vazio
        try:
            SRC_DIR.rmdir()
            print(f"✓ Diretório removido: {SRC_DIR.relative_to(REPO_ROOT)}")
        except OSError:
            print(f"⚠ Diretório {SRC_DIR.relative_to(REPO_ROOT)} não está vazio (ainda contém arquivos).")

    if not args.apply:
        print("\n💡 Nada foi alterado. Rode com --apply para executar.")

    return 0 if not fail else 1


if __name__ == "__main__":
    sys.exit(main())
