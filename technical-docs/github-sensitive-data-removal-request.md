# GitHub Sensitive Data Removal Request — Machine-Learning-main.zip

**Status:** pronto para envio manual pelo owner do repo em https://support.github.com/contact/private-information
**Criado em:** 2026-08-25
**Contexto:** documento auxiliar para acompanhar a limpeza do arquivo `Machine-Learning-main.zip` que continha strings de senha em código R e Python.

---

## Por que abrir o request

Fizemos `git filter-repo` local (2026-08-25) removendo o arquivo de todo o histórico e força-push (`+ d2f654fef8...753cde4678 main -> main (forced update)`), além de deletar branches remotas que ainda referenciavam o objeto (`main-remote-backup-20250902-160023`, dependabot/*). O commit alerta `#dependabot/51` reporta apenas a vulnerabilidade `extract-zip` do `pa11y-ci` — não está relacionado.

Contudo, o GitHub mantém caches de blobs em:
- URLs diretas: `raw.githubusercontent.com/cedis-unb/cedis-unb.github.io/<sha>/static/files/Machine-Learning-main.zip`
- Página web: `github.com/cedis-unb/cedis-unb.github.io/blob/<sha>/static/files/Machine-Learning-main.zip`
- Downloads via API: `api.github.com/repos/cedis-unb/cedis-unb.github.io/git/blobs/<sha>`
- Objetos referenciados por PRs, forks e Actions caches

Esses continuam acessíveis mesmo após force-push, até que o time do GitHub Support os purgue explicitamente.

---

## Passos

1. Acesse **https://support.github.com/contact/private-information** (precisa estar logado como owner do `cedis-unb`)
2. Selecione categoria **"Sensitive data in a public repository"**
3. Preencha o formulário com o conteúdo abaixo

---

## Conteúdo do request (copie/cole)

### Repository
`https://github.com/cedis-unb/cedis-unb.github.io`

### Nature of the sensitive data
Database password strings ("Omadheoc77" and "Andre203") that were hardcoded in R and Python files inside a ZIP file (`Machine-Learning-main.zip`, ~8 MB) served publicly by the repository's static site.

The passwords appeared in `DBaccess.R` files and in `Extrai_palavras.v2.parte {0..10}.py` scripts, connecting to a PostgreSQL instance (`postgres@localhost:5432/oasisbr`). The affected credentials have been rotated at the database side; nevertheless the strings must be purged from GitHub caches so they cannot be reused for reconnaissance.

### Actions we've already taken
- **2026-08-25**: sanitized in-place — replaced both strings with placeholder `SENHA` (matching the pattern of the other 14 `DBaccess.R` files in the ZIP that already used the placeholder). Committed on branch `main`.
- **2026-08-25**: ran `git filter-repo --invert-paths` removing 4 paths from the entire history:
  - `static/Machine-Learning-main.zip`
  - `static/files/Machine-Learning-main.zip`
  - `docs/Machine-Learning-main.zip`
  - `docs/files/Machine-Learning-main.zip`
- **2026-08-25**: force-pushed rewritten `main` to origin (`+ d2f654fef8...753cde4678 main -> main (forced update)`).
- **2026-08-25**: deleted remote branches that still contained the old history: `main-remote-backup-20250902-160023`, `dependabot/github_actions/actions/setup-node-7`, `dependabot/github_actions/actions/upload-artifact-7`, `dependabot/github_actions/github/codeql-action-4.37.4`, `dependabot/npm_and_yarn/alpinejs-3.16.2`.
- Verified locally: `find . -name "*Machine-Learning-main*"` returns nothing, `git log --all -- **Machine-Learning-main*` is empty, `git ls-remote --heads origin` shows only `main`.

### URLs to purge from GitHub cache
Please purge from raw.githubusercontent.com, blob view, API blobs, and any downloadable archives (tarball/zipball) that referenced these paths in past commits. Original commit SHAs that introduced or modified the file (from `git log --all` before the rewrite):

- `a3e0b4e616` (2024-06-07) — "Add files via upload"
- `3d9b76f51c` (2024-06-07) — "files"
- `343034cd05` (2024-06-07) — "Files"
- `1fa3c1b661` (2026-08-25) — "chore: dedup productions.yaml, sanitiza ZIP público, ajustes da auditoria" (this one already had the sanitized version, but the file itself must be purged too)

Paths (all four served the same content at different points):
- `static/Machine-Learning-main.zip`
- `static/files/Machine-Learning-main.zip`
- `docs/Machine-Learning-main.zip`
- `docs/files/Machine-Learning-main.zip`

Public URLs that were serving the content:
- `https://cedis.unb.br/files/Machine-Learning-main.zip` (via GitHub Pages)
- `https://cedis.unb.br/Machine-Learning-main.zip`

### Additional
Please also invalidate any GitHub Actions cache entries referencing these paths, and confirm removal from any indexed forks (as of the request date the repository had no known active forks).

Thank you.

---

## Depois do envio

- Guarde o número do ticket (`SUPPORT-XXXXXXX`) e cole aqui: `___________________`
- Prazo típico de resposta do GitHub Support: 2–5 dias úteis
- Após confirmação de purge, verifique que as URLs acima retornam 404
