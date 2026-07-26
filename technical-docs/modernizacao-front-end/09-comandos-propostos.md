# 09 — Comandos propostos

**IMPORTANTE:** este documento lista comandos previstos para futuras fases. **Nenhum comando de modificação foi executado nesta auditoria.** Comandos de consulta (read-only) foram executados durante a auditoria e estão marcados como tal.

## Categoria A — Comandos de consulta (não modificam nada)

Podem ser executados livremente durante análise:

```bash
# Git — inspeção
git status --short
git branch -vv
git remote -v
git log --oneline -20
git diff --stat
git diff
git tag --list
git ls-remote origin

# Node/npm — inspeção
node --version
npm --version
npm ls --depth=0
npm outdated
npm audit
npm audit --production
npm ls postcss
npm explain <pkg>
npm view <pkg> version
npm view <pkg> engines

# Hugo — inspeção
hugo version
hugo env
hugo config
hugo config mounts
hugo config | grep -iE "build|stats|deployment|publishdir"
hugo mod graph
hugo mod verify              # seguro — só verifica hashes
hugo --help
hugo deploy --dryRun         # seguro para AUDITAR se targets aparecerem por engano; NÃO executa deploy
# Build para diretório temporário (NÃO altera docs/):
hugo --minify --cleanDestinationDir -d /tmp/cedis-test-build
# Dev server (não escreve em disco):
hugo server -d .hugo-server --disableFastRender --port 1313

# Sistema de arquivos — inspeção
find . -maxdepth 3 -name "*.yaml" -not -path "./node_modules/*"
du -sh assets/ docs/ resources/ node_modules/
ls -la assets/css/
grep -rn "padrão" layouts/
python3 tmp/audit_v2.py    # script de auditoria de classes Tailwind

# Testes (não modificam, só leem)
npm test                              # validate_content + validate_i18n + check:publications
npx pa11y-ci --config .pa11yci.json
npx lhci autorun --config=lighthouserc.json
```

## Categoria B — Comandos que modificam arquivos (requerem autorização explícita)

### Git

```bash
# Criar branch local sem upstream
git switch --create dev/tailwind-v4-vite-local

# Deletar branch local (após rollback)
git branch -D dev/tailwind-v4-vite-local

# Criar tag de backup
git tag -a pre-tailwind-v4-YYYYMMDD -m "Snapshot antes da migração Tailwind 4"

# Deletar tag
git tag -d pre-tailwind-v4-YYYYMMDD

# Reverter mudanças no working tree
git checkout .                             # NOTA: descarta mudanças não commitadas
git checkout <file>                        # reverte arquivo específico
git checkout <sha> -- <path>               # restaura path de um commit específico

# Cherry-pick de commit específico
git cherry-pick <sha>

# Revert de merge
git revert -m 1 <merge-sha>
```

### npm — dependências

```bash
# Atualização conservadora (patches minor dentro do range ^)
npm update

# Reinstalação do lock canônico
npm ci

# Instalação de nova dependência
npm install --save-dev @tailwindcss/postcss@4.3.3
npm install --save-dev @tailwindcss/cli@4.3.3     # se Alt 4 escolhida
npm install --save-dev tailwindcss@4.3.3
npm install --save-dev @tailwindcss/typography@0.5.20

# Desinstalação
npm uninstall autoprefixer browserslist caniuse-lite postcss-cli
npm uninstall alpinejs                             # órfã (Alpine via CDN)

# Migração automatizada Tailwind
npx @tailwindcss/upgrade@latest
```

### Hugo — comandos que ALTERAM arquivos

```bash
# Build padrão que escreve em publishDir (docs/) — CUIDADO
hugo --minify --cleanDestinationDir                # ALTERA docs/ (rastreado pelo git)

# Build seguro para verificação (NÃO altera docs/)
hugo --minify --cleanDestinationDir -d /tmp/cedis-test

# Hugo module vendor — cria/atualiza pastas
hugo mod vendor        # NÃO executar — pode alterar go.mod, _vendor/

# Hugo mod get — atualiza módulos
hugo mod get -u        # NÃO executar
```

### Sistema de arquivos

```bash
# Substituição em massa (careful — pode quebrar código)
python3 tmp/apply_fixes.py    # script auditado, faz substituições específicas

# Regenerar assets Tailwind
npx tailwindcss -i ./assets/css/main.css -o ./assets/css/style.css
```

## Categoria C — Comandos de teste

Não modificam código, mas geram artefatos em `tmp/` ou disparam server local:

```bash
# Executar suite de validação
npm test

# Executar pa11y-ci (site tem que estar rodando na 4173)
hugo server -d .hugo-server --disableFastRender --port 4173 --bind 127.0.0.1 --minify &
sleep 5
npx pa11y-ci --config .pa11yci.json
npx pa11y-ci --config .pa11yci.json --json > tmp/pa11y-report.json

# Executar Lighthouse CI
npx lhci autorun --config=lighthouserc.json

# Verificar links (rodado em CI via GH Actions)
# Localmente exigiria instalar lychee separadamente

# Puppeteer smoke tests (script auxiliar)
node tmp/capture-baseline-screenshots.js

# Script de auditoria de classes Tailwind
python3 tmp/audit_v2.py
python3 tmp/audit_more.py
```

## Categoria D — Comandos de construção

```bash
# Build completo (mesmo do CI local)
npm run build
# = python3 scripts/build_publications.py
# + hugo --minify --cleanDestinationDir
# + pagefind --site docs

# Build só do Hugo (sem publications rebuild, sem pagefind)
hugo --minify --cleanDestinationDir

# Watch em desenvolvimento
npm run start
# = concurrently:
#   watch:tw   (tailwindcss -i main.css -o style.css --watch)
#   watch:hugo (hugo server -d .hugo-server --disableFastRender)

# Watch só hugo (útil se editar CSS diretamente)
hugo server -d .hugo-server --disableFastRender
```

## Categoria E — Comandos Git específicos da migração

```bash
# Preparação
git switch main
# git pull --ff-only     # SÓ COM AUTORIZAÇÃO EXPLÍCITA (pode trazer commits alheios)
git tag -a pre-tailwind-v4-$(date +%Y%m%d) -m "Snapshot antes da migração"

# Criar branch dev
git switch --create dev/tailwind-v4-vite-local
git branch -vv           # confirma sem upstream

# Durante migração (na branch dev)
git add <arquivos>
git commit -m "..."
git log --oneline --graph -10

# Comparação
git diff main...dev/tailwind-v4-vite-local
git diff --stat main...dev/tailwind-v4-vite-local
git log main..dev/tailwind-v4-vite-local --oneline

# Rollback
git switch main
git branch -D dev/tailwind-v4-vite-local
```

## Categoria F — Comandos PROIBIDOS sem autorização explícita

```bash
# NUNCA sem autorização escrita
git push
git push -u origin <branch>
git push origin main
git push --force
git push --force-with-lease
git push origin --tags
git push origin :refs/heads/<branch>       # deleta branch remota
gh pr create
gh pr merge
gh release create

# Auto-atualizações agressivas
npm audit fix
npm audit fix --force
npm install                                # sem -D/-E vira patch de package.json
npm-check-updates -u
npm upgrade

# Modificação de config global
npm config set ...
git config --global ...
git config user.email ...

# Skip de hooks (perigoso)
git commit --no-verify
git push --no-verify

# Amend em commit já pushado
git commit --amend                         # OK se commit ainda não foi pushado; PERIGO se foi
git rebase -i main                         # reescreve história — só antes de push
git reset --hard                           # descarta mudanças sem confirmação
git clean -fd                              # deleta arquivos não rastreados

# Deploy direto Hugo
hugo deploy                                # sem targets configurados hoje = no-op, mas listado por precaução
hugo deploy --force
hugo deploy --dryRun                       # este é seguro (dry run), mas listado para consciência

# Scripts npm que podem publicar
npm run deploy                             # se algum dia existir
npm run publish                            # idem
npm publish                                # publicar pacote npm (não é este caso, mas listado)

# Hugo mod que altera go.mod/vendor
hugo mod vendor
hugo mod get -u
hugo mod init
hugo mod tidy

# Comandos destrutivos de arquivo
rm -rf docs/                               # deleta site publicado
rm -rf assets/                             # deleta fontes CSS/imagens
find . -name "*.png" -delete               # apaga imagens em massa
git reset --hard <sha>                     # perde commits
git checkout <sha> -- .                    # sobrescreve tudo
```

## Categoria G — Comandos de verificação pós-fase

Use após cada fase da migração para confirmar não-regressão:

```bash
# Após instalação de novas deps
npm ls --depth=0
npm audit
diff package.json <(git show HEAD:package.json)      # ver diff no formato Diff

# Após rodar upgrade tool
git diff --stat
git diff assets/css/main.css
git diff tailwind.config.js
git diff postcss.config.js
python3 tmp/audit_v2.py                              # confirma classes válidas

# Após build
du -sh docs/
find docs/css -name "*.css" -exec ls -la {} \;
diff -q docs/index.html /tmp/cedis-baseline-index.html
curl -sI http://127.0.0.1:4173/ | grep -i "content-type\|content-length"

# Antes de merge para main
git log --oneline main..dev/tailwind-v4-vite-local
git diff --stat main...dev/tailwind-v4-vite-local | tail -3
```

## Uso responsável desta lista

- **Categoria A** livre durante análise — não altera nada.
- **Categoria B, C, D, E** requerem autorização explícita **por sessão** (não vale autorização blanket).
- **Categoria F** NUNCA sem autorização escrita específica e sem plano de reversão.
- Após executar qualquer comando de Categoria B ou superior, rodar `git status` e reportar o estado.

## Aliases perigosos possíveis

Verificar se `.gitconfig` local tem aliases perigosos:

```bash
git config --list | grep alias
# Exemplos perigosos: pushf, wipe, blast, obliterate
```

Se qualquer alias com `push -f`, `reset --hard`, `clean -fd` estiver configurado, remover antes de iniciar migração.

## Hooks Git

Nenhum hook ativo hoje (só `.sample` do template). Considerar instalar hook `pre-push` para bloquear push da branch dev — ver `07-plano-de-rollback.md > Salvaguarda 1`.
