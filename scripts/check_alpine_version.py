#!/usr/bin/env python3
"""Guarantee that the Alpine.js runtime and the locked package agree.

Alpine is loaded from a CDN in layouts/partials/footer.html, so npm never
places it on the page. Nothing but this check ties the two together, and they
have drifted before (runtime 3.15.11 / package.json ^3.15.11 / lock 3.15.12).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FOOTER = Path("layouts/partials/footer.html")
PACKAGE = Path("package.json")
LOCK = Path("package-lock.json")
CDN_RE = re.compile(r"cdn\.jsdelivr\.net/npm/alpinejs@([0-9][^/]*)/")


def main() -> int:
    issues: list[str] = []

    footer = FOOTER.read_text(encoding="utf-8")
    runtime_versions = CDN_RE.findall(footer)
    if not runtime_versions:
        issues.append(f"{FOOTER}: nenhuma tag <script> do Alpine via cdn.jsdelivr.net encontrada")
    elif len(set(runtime_versions)) > 1:
        issues.append(f"{FOOTER}: versões divergentes do Alpine no runtime: {sorted(set(runtime_versions))}")

    declared = json.loads(PACKAGE.read_text(encoding="utf-8")).get("devDependencies", {}).get("alpinejs")
    if not declared:
        issues.append(f"{PACKAGE}: alpinejs não está em devDependencies")
    elif not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", declared):
        issues.append(
            f"{PACKAGE}: alpinejs deve estar pinado numa versão exata (encontrado {declared!r}); "
            "o runtime é uma URL fixa de CDN e não acompanha faixas semver"
        )

    locked = json.loads(LOCK.read_text(encoding="utf-8")).get("packages", {}).get("node_modules/alpinejs", {}).get("version")
    if not locked:
        issues.append(f"{LOCK}: node_modules/alpinejs ausente")

    versions = {"runtime": runtime_versions[0] if runtime_versions else None, "package.json": declared, "package-lock.json": locked}
    if all(versions.values()) and len(set(versions.values())) > 1:
        detail = ", ".join(f"{name}={version}" for name, version in versions.items())
        issues.append(f"versões do Alpine divergentes: {detail}")

    if issues:
        for issue in issues:
            print(f"ERRO: {issue}", file=sys.stderr)
        return 1

    print(f"Alpine {locked} coerente entre runtime, package.json e package-lock.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
