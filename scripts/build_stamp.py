#!/usr/bin/env python3
"""Identificador do build publicado.

Escreve docs/build.txt e fornece o valor usado na <meta name="cedis-build">
da capa, para conferir num pedido só se o que está no ar corresponde ao que
se espera.

O carimbo NÃO pode conter o SHA do próprio commit que o publica — um arquivo
não referencia o commit que o contém. O que ele nomeia é o commit de FONTE a
partir do qual o docs/ foi gerado, e por isso registra também se a árvore
estava suja no momento do build: com `dirty=yes` o SHA sozinho não identifica
a saída, e é melhor que isso fique visível a que fique implícito.

Ordem correta de publicação (ver CONVENTIONS.md §12.8):
    1. commitar as fontes
    2. npm run build
    3. commitar docs/
Assim `source` é exatamente o commit de fonte publicado e `dirty` é `no`.

Uso:
    python3 scripts/build_stamp.py            escreve docs/build.txt
    python3 scripts/build_stamp.py --value    imprime o valor curto
"""

from __future__ import annotations

import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def git(*args: str) -> str:
    return subprocess.run(("git", *args), capture_output=True, text=True, check=False).stdout.strip()


def stamp() -> tuple[str, bool]:
    sha = git("rev-parse", "HEAD") or "unknown"
    # --porcelain ignora arquivos não rastreados que estejam no .gitignore;
    # docs/ é rastreado, então uma regeneração anterior não commitada conta
    # como suja, que é o comportamento desejado.
    dirty = bool(git("status", "--porcelain"))
    return sha, dirty


def short(sha: str, dirty: bool) -> str:
    return f"{sha[:10]}{'-dirty' if dirty else ''}"


def main(argv: list[str]) -> int:
    sha, dirty = stamp()

    if "--value" in argv:
        print(short(sha, dirty))
        return 0

    out = Path("docs/build.txt")
    if not out.parent.is_dir():
        print(f"ERRO: {out.parent} não existe — rode o Hugo antes do carimbo.", file=sys.stderr)
        return 1

    built = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out.write_text(
        "# Identificador do build publicado. `source` é o commit de FONTE que\n"
        "# gerou este docs/, nao o commit que o publica.\n"
        f"source={sha}\n"
        f"short={short(sha, dirty)}\n"
        f"dirty={'yes' if dirty else 'no'}\n"
        f"built={built}\n",
        encoding="utf-8",
    )
    print(f"docs/build.txt: source={sha[:10]} dirty={'yes' if dirty else 'no'} built={built}")
    if dirty:
        print(
            "AVISO: a arvore tinha alteracoes nao commitadas no momento do build.\n"
            "       Commite as fontes ANTES de `npm run build` para o carimbo\n"
            "       identificar exatamente o que foi publicado.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
