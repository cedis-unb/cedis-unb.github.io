# 04 — Plano de migração

**Arquitetura-alvo:** Tailwind CSS 4 + `@tailwindcss/postcss` + Hugo Pipes (mantém).
**Modalidade:** branch local não publicada `dev/tailwind-v4-vite-local`.
**Duração estimada:** 3 dias de trabalho ativo + 2 dias de estabilização = 5 dias.
**Pré-requisito:** autorização explícita para executar cada fase.

## Fase 0 — Preparação

### 0.1 — Confirmação stakeholder

**Objetivo:** validar que a migração pode ocorrer agora.

**Ações:**

- Apresentar a este documento e ao `00-resumo-executivo.md`.
- Confirmar impacto aceitável em navegadores <Safari 16.4/<Chrome 111 (verificar Google Analytics real).
- Definir janela de estabilização (ex.: 3 dias sem deploy planejado).

**Comandos previstos:** nenhum.

**Critério de conclusão:** aprovação registrada em issue ou email.

**Reversão:** não aplicável.

### 0.2 — Backup pré-migração

**Objetivo:** garantir ponto de restauração.

**Ações:**

- Criar tag anotada `pre-tailwind-v4-YYYYMMDD` apontando para `main` atual.
- Confirmar que a tag é local até autorização explícita para push.

**Comandos previstos:**

```bash
git tag -a pre-tailwind-v4-$(date +%Y%m%d) -m "Snapshot antes da migração Tailwind 4"
git tag --list "pre-tailwind-v4-*"
```

**Risco:** nenhum (tag é read-only apontador).

**Reversão:** `git tag -d pre-tailwind-v4-YYYYMMDD`

## Fase 1 — Linha de base

### 1.1 — Métricas de referência

**Objetivo:** capturar estado atual para comparação pós-migração.

**Ações:**

- Rodar `npm run build` limpo.
- Capturar tamanho de CSS e HTML em `docs/`.
- Rodar `npx pa11y-ci --config .pa11yci.json --json > tmp/pa11y-pre.json`.
- Rodar `npx lhci autorun --config=lighthouserc.json` — salvar em `tmp/lhci-pre/`.
- Screenshot puppeteer de 10+ rotas (PT/EN × light/dark) → `tmp/baseline/screenshots/`.
- Salvar `du -sh docs/ resources/ assets/images/` para comparar footprint.

**Arquivos afetados:** nenhum no repo — só saídas em `tmp/` (gitignored).

**Comandos previstos:**

```bash
# Todos são apenas consulta ou geram arquivos em tmp/
mkdir -p tmp/baseline/screenshots
npm run build
du -sh docs/ resources/ assets/images/ > tmp/baseline/sizes.txt
find docs/css -name "*.css" -exec ls -la {} \; > tmp/baseline/css-sizes.txt
npx pa11y-ci --config .pa11yci.json --json > tmp/baseline/pa11y-pre.json
npx lhci autorun --config=lighthouserc.json
mv .lighthouseci tmp/baseline/lhci-pre 2>/dev/null || true
node tmp/capture-baseline-screenshots.js  # script auxiliar a criar
```

**Risco:** nenhum — só leituras.

**Critério de conclusão:** `tmp/baseline/` contém pa11y JSON, lhci report e screenshots.

**Reversão:** `rm -rf tmp/baseline/` (dados descartáveis).

## Fase 2 — Criação da branch local

### 2.1 — Verificação preventiva

**Ações:**

- `git status` e `git branch -vv` — confirmar working tree limpo em `main`.
- `git remote -v` — confirmar apenas `origin` esperado.
- `cat .git/config` — verificar que nenhum push automático está configurado.

**Comandos previstos:**

```bash
git status --short
git branch -vv
git remote -v
grep -A5 "\[branch" .git/config | head -20
```

### 2.2 — Criação da branch

**Ações:**

- Criar branch a partir de `main` atualizada.
- **Não** configurar upstream.

**Comandos previstos:**

```bash
git switch main
# NÃO EXECUTAR git pull sem autorização explícita — main pode estar à frente do local
# Se autorizado: git pull --ff-only
git switch --create dev/tailwind-v4-vite-local
git branch -vv    # confirma que nova branch NÃO tem upstream
```

**Critério de conclusão:** `git branch -vv` mostra `dev/tailwind-v4-vite-local` sem upstream `[origin/...]`.

**Reversão:** `git switch main && git branch -D dev/tailwind-v4-vite-local`.

**Salvaguarda:** adicionar hook local `pre-push` que rejeite push desta branch, opcional. Ver `07-plano-de-rollback.md`.

## Fase 3 — Atualização de ambiente Node

### 3.1 — Confirmação Node

**Ações:**

- Já em Node 24.14.1 local (via mise, `.tool-versions`).
- CI já usa `NODE_VERSION: '24'`.

**Comandos previstos:**

```bash
node --version   # esperado: v24.x
npm --version    # esperado: 11.x
```

**Nada a mudar em Fase 3.** Documentar no ADR (ver `08`).

## Fase 4 — Atualização conservadora de dependências (Nível 1)

Antes da migração v4, aplicar patches/minors da linha 3.x para reduzir superfície de bugs entre correções e migração.

### 4.1 — Patches seguros

**Ações:** atualizar dentro do range `^` já declarado.

**Comandos previstos:**

```bash
# Ver diff exato antes:
npm outdated
# Executar:
npm update
# Verificar que package.json NÃO mudou (só package-lock):
git diff package.json package-lock.json
# Testar:
npm test
npm run build
```

**Pacotes afetados (esperado):**

- `@tailwindcss/typography` 0.5.19 → 0.5.20
- `alpinejs` 3.15.11 → 3.15.12 (órfão, sem efeito real)
- `autoprefixer` 10.4.22 → 10.5.4
- `browserslist` 4.28.2 → 4.28.7
- `caniuse-lite` 1.0.30001791 → 1.0.30001806
- `postcss` 8.5.19 → 8.5.23
- `markdown-it-emoji` 3.0.0 → 3.1.0

**Critério de conclusão:** `npm test` passa; build gera CSS idêntico em bytes ou diff só de datas.

**Reversão:** `git checkout package-lock.json && npm ci`.

## Fase 5 — Migração Tailwind (Nível 3)

### 5.1 — Rodar upgrade tool

**Ações:**

- Executar migração automatizada oficial.

**Comandos previstos:**

```bash
npx @tailwindcss/upgrade@latest
# A ferramenta:
# - Instala tailwindcss@4
# - Instala @tailwindcss/postcss
# - Atualiza main.css (@tailwind → @import)
# - Renomeia shadow-sm → shadow-xs, rounded → rounded-sm, etc.
# - Converte bg-opacity-* → cor/opacity
# - Converte flex-shrink-* → shrink-*
# - Atualiza tailwind.config.js para usar @tailwindcss/postcss
# - Pode oferecer conversão para CSS-first (@theme) — recusar nesta fase
```

**Arquivos afetados esperados:**

- `package.json`, `package-lock.json` (deps)
- `assets/css/main.css` (`@tailwind` → `@import`)
- `postcss.config.js` (`tailwindcss` → `@tailwindcss/postcss`)
- Todos `.html` com classes que sofreram rename (81 shadow-sm, 25 flex-shrink, 2 text-opacity, etc.)
- `tailwind.config.js` pode ser referenciado via `@config` no CSS

**Risco:** alto — mudança em massa.

**Critério de conclusão:** ferramenta termina sem erro; `git status` mostra as mudanças esperadas.

**Reversão:** `git checkout .` no working tree + `git checkout package-lock.json && npm ci`.

### 5.2 — Ajuste manual pós-upgrade

**Ações:**

- Auditar borders sem cor explícita e adicionar cor onde ficarem invisíveis.
- Verificar `focus:outline-none` → decidir se manter (a11y) ou trocar por `outline-hidden`.
- Verificar `ring` bare → `ring-3` onde era intencional 3px.
- Confirmar remoção de `autoprefixer`, `browserslist`, `caniuse-lite` do `package.json`.

**Comandos previstos:**

```bash
grep -rn " border\b" layouts/ | grep -v "border-[a-z0-9]" | head -30
grep -rn "focus:outline-none" layouts/ | head
grep -rn "\bring\b" layouts/ | grep -v "ring-[0-9]\|ring-[a-z]" | head
npm uninstall autoprefixer browserslist caniuse-lite postcss-cli
# postcss em si pode ser removido? Verificar: Hugo Pipes usa postCSS,
# mas com @tailwindcss/postcss ainda precisa do runner postcss:
npm ls postcss  # ver se ainda é dependência transitiva
```

**Critério de conclusão:** build limpo; visual manual OK; deps órfãs removidas.

**Reversão:** `git checkout .` + `npm ci` restaura estado da tag pré-migração.

### 5.3 — Remover dependência órfã de alpinejs (opcional)

**Ações:** dado que Alpine é servido via CDN, a devDependency npm nunca é usada.

**Comandos previstos:**

```bash
npm uninstall alpinejs
```

**Risco:** se algum dia decidirmos empacotar Alpine, precisa reinstalar. Baixo.

**Reversão:** `npm install --save-dev alpinejs`.

## Fase 5.4 — Migração Alt 4 (Hugo native `css.TailwindCSS`) — se Alt 4 escolhida

Substitui a Fase 5.1-5.3 tradicional se decidirmos adotar a integração nativa Hugo.

### 5.4.1 — Instalar Tailwind 4 CLI

```bash
npm uninstall tailwindcss                              # v3
npm install --save-dev tailwindcss@4 @tailwindcss/cli@4 @tailwindcss/typography@0.5.20
npm uninstall autoprefixer browserslist caniuse-lite postcss-cli
# postcss pode continuar como transitive; não desinstalar manualmente
```

### 5.4.2 — Reescrever `main.css`

Novo conteúdo:

```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";
@source "hugo_stats.json";
/* opcional — se manter tailwind.config.js: */
@config "../../tailwind.config.js";
```

Se quisermos manter `overrides.css` e `profile.css` separados, incluir via `@import` no `main.css`:

```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";
@source "hugo_stats.json";
@config "../../tailwind.config.js";
@import "./overrides.css";
@import "./profile.css";
```

Alternativa (preferida): manter 3 arquivos separados, cada um processado independentemente por `css.TailwindCSS` — cada um vira `<link>` no head.

### 5.4.3 — Habilitar buildStats em `hugo.yaml`

```yaml
build:
  useResourceCacheWhen: fallback
  buildStats:
    enable: true
  cachebusters:
    - source: '(postcss|tailwind)\.config\.(js|mjs|cjs)'
      target: '(css|styles|scss|sass)'
```

### 5.4.4 — Adicionar `hugo_stats.json` ao `.gitignore`

Editar `.gitignore` para incluir:

```
hugo_stats.json
```

### 5.4.5 — Atualizar `hugo.yaml module.hugoVersion`

Já é `min: "0.104.0"`. Atualizar para `min: "0.161.0"` (requisito de `css.TailwindCSS`):

```yaml
module:
  hugoVersion:
    extended: true
    min: "0.161.0"
```

### 5.4.6 — Reescrever `layouts/partials/head.html`

Substituir o bloco atual (linhas 70-84):

```go-html-template
{{ with (templates.Defer (dict "key" "global")) }}
  {{ with resources.Get "css/main.css" }}
    {{ $opts := dict "minify" (not hugo.IsDevelopment) }}
    {{ with . | css.TailwindCSS $opts }}
      {{ if hugo.IsDevelopment }}
        <link rel="stylesheet" href="{{ .RelPermalink }}">
      {{ else }}
        {{ with . | fingerprint }}
          <link rel="stylesheet" href="{{ .RelPermalink }}"
                integrity="{{ .Data.Integrity }}" crossorigin="anonymous">
        {{ end }}
      {{ end }}
    {{ end }}
  {{ end }}
{{ end }}

{{/* profile.css como bloco independente para permitir substituição futura */}}
{{ with (templates.Defer (dict "key" "profile")) }}
  {{ with resources.Get "css/profile.css" }}
    {{ $opts := dict "minify" (not hugo.IsDevelopment) }}
    {{ with . | css.TailwindCSS $opts }}
      {{ if hugo.IsDevelopment }}
        <link rel="stylesheet" href="{{ .RelPermalink }}">
      {{ else }}
        {{ with . | fingerprint }}
          <link rel="stylesheet" href="{{ .RelPermalink }}"
                integrity="{{ .Data.Integrity }}" crossorigin="anonymous">
        {{ end }}
      {{ end }}
    {{ end }}
  {{ end }}
{{ end }}
```

Idem para `overrides.css`.

### 5.4.7 — Remover `postcss.config.js`

```bash
rm postcss.config.js
```

Ou manter vazio como marcador.

### 5.4.8 — Ajustar scripts npm

```diff
- "watch:tw": "tailwindcss -i ./assets/css/main.css -o ./assets/css/style.css --watch",
  "watch:hugo": "hugo server -d .hugo-server --disableFastRender",
```

E simplificar:

```diff
- "start": "concurrently npm:watch:*",
+ "start": "npm run watch:hugo",
```

Isso permite remover `concurrently` (o CLI Tailwind não é mais executado separadamente — Hugo chama internamente via `css.TailwindCSS`).

### 5.4.9 — Deletar `assets/css/style.css`

Não é mais necessário (Hugo lê `main.css` diretamente).

```bash
git rm assets/css/style.css
```

### 5.4.10 — Validar

```bash
hugo server                    # dev: HMR deve funcionar
hugo --minify --cleanDestinationDir -d /tmp/cedis-alt4    # prod: build limpo
```

Verificar `docs/css/main.<hash>.css` gerado, com integrity hash correto.

**Critério de conclusão:**

- Build limpo
- CSS servido com integrity hash
- Alpine.js segue funcionando (CDN não afetado)
- `hugo_stats.json` gerado em raiz do projeto durante build (não commitado)
- Grep pós-build: todas classes usadas em templates aparecem no CSS gerado
- PT e EN renderizam idêntico

**Reversão:**

```bash
git checkout .   # tudo
npm ci           # restaura node_modules
```

## Fase 6 — Vite (SE decidido)

**Recomendação atual: não adotar.** Ver `03-comparacao-de-arquiteturas.md`.

**Se autorizado no futuro:**

- Adicionar `vite`, `@tailwindcss/vite`.
- Criar `vite.config.ts` com plugin Tailwind e build target `assets/css/`.
- Reescrever `layouts/partials/head.html` para ler `dist/.vite/manifest.json`.
- Substituir scripts `watch:tw` e o `postCSS` no Hugo Pipes.
- Rodar dev-server duplo (Vite + Hugo).

**Nesta migração: SKIP Fase 6.**

## Fase 7 — Adaptação do Hugo

Como Alt 2 mantém Hugo Pipes intacto, mudanças mínimas:

### 7.1 — Verificar `head.html`

**Ações:**

- Ler `layouts/partials/head.html:70-84`.
- Confirmar que `resources.Get "css/main.css" | postCSS | ...` continua correto (agora usa `@tailwindcss/postcss` internamente via `postcss.config.js`).
- Se removemos `style.css` (Tailwind CLI compila para lá, mas em v4 podemos usar apenas main.css como entrada), atualizar `head.html`.

**Comandos previstos:**

```bash
grep -n "style.css\|main.css\|overrides.css\|profile.css" layouts/partials/head.html
```

**Decisão:** em v4, se `main.css` já contém `@import "tailwindcss"`, o Tailwind CLI/PostCSS gera todo o CSS. Podemos:

- **Opção A**: manter `watch:tw` compilando `main.css → style.css` e continuar servindo `style.css`.
- **Opção B**: eliminar `style.css` intermediário; Hugo Pipes lê `main.css` diretamente e gera tudo (mais simples).

Recomendação: **Opção B** — remove duplicação de execução Tailwind. Requer atualizar `head.html` para ler `main.css` em vez de `style.css`.

### 7.2 — Ajustar scripts npm

**Ações:** remover `watch:tw` se optado por Opção B.

**Diff previsto em `package.json`:**

```diff
- "watch:tw": "tailwindcss -i ./assets/css/main.css -o ./assets/css/style.css --watch",
```

`concurrently` continua rodando apenas `watch:hugo`. Simplificação: substituir `concurrently` por `npm run watch:hugo` direto e remover `concurrently` das devDependencies. Bônus para simplificação.

## Fase 8 — Revisão das classes

### 8.1 — Executar auditoria automatizada

**Ações:**

- Rerodar `tmp/audit_v2.py` (existente) no repo pós-migração para verificar que não há novas classes silenciosamente inválidas.

**Comandos previstos:**

```bash
python3 tmp/audit_v2.py > tmp/post-migration-audit.txt
diff tmp/pre-migration-audit.txt tmp/post-migration-audit.txt
```

### 8.2 — Revisão visual

**Ações:**

- Rodar `hugo server`.
- Puppeteer script captura 10+ rotas × PT/EN × light/dark → `tmp/post/screenshots/`.
- Comparar visualmente com baseline (Fase 1).

**Critério:** diferenças aceitas explicitamente OU corrigidas.

## Fase 9-13 — Testes

### 9. Testes visuais (Fase 8.2 acima)

### 10. Testes funcionais

- `npm test` (validações Python).
- Navegar manualmente: busca (pagefind), menu, filtros, quiz, mapa (D3), accordion de perfil.

### 11. Testes de acessibilidade

- `npx pa11y-ci` → comparar `pa11y-post.json` com baseline.
- Meta: 0 regressões, se possível ganhos em contraste.

### 12. Testes de desempenho

- `npx lhci autorun` → comparar com baseline.
- Meta: performance mobile ≥ 90 em rotas críticas; LCP ≤ 2500ms.

### 13. Bundle size

```bash
du -sh docs/ resources/ assets/images/
find docs/css -name "*.css" -exec ls -la {} \;
```

Meta: CSS total minificado ≤ baseline.

## Fase 14 — Validação PT/EN

- Verificar rotas /pt/ e /en/ com paridade de comportamento.
- Verificar seletor de idioma funcional.

Testes específicos:

- `/pt/people/sergio_freitas/` e `/en/people/sergio_freitas/` — comparar layout.
- `/pt/projects/` e `/en/projects/`.
- `/pt/publications/scientific/2025/` e equivalente em EN.

## Fase 15 — Decisão de integração

### 15.1 — Revisão de código

**Ações:**

- Verificar `git diff main...dev/tailwind-v4-vite-local` completo.
- Solicitar revisão humana obrigatória (não auto-approve).

### 15.2 — Se aprovado

**Ações:**

- **Autorização explícita necessária** antes de qualquer push.
- Rebase interativo se necessário para separar em commits atômicos.
- Publicar em `origin/main` via PR ou merge direto (a decidir).

**Comandos previstos (SÓ COM AUTORIZAÇÃO):**

```bash
git switch main
git merge --ff-only dev/tailwind-v4-vite-local  # ou --no-ff dependendo da política
git push origin main
```

### 15.3 — Se rejeitado

- Ir para Fase 16.

## Fase 16 — Reversão ou descarte

### 16.1 — Descartar branch

**Comandos previstos:**

```bash
git switch main
git branch -D dev/tailwind-v4-vite-local
# NÃO é necessário force-delete no remoto — a branch nunca foi pushada.
```

### 16.2 — Voltar ao estado pré-migração

- Working tree em `main` = `HEAD` do `pre-tailwind-v4-YYYYMMDD` (tag).
- `npm ci` para restaurar node_modules alinhados com package-lock atual.
- `docs/` no `main` continua íntegro (nunca foi tocado durante migração local).

### 16.3 — Remover tag se desejado

**Comandos previstos:**

```bash
git tag -d pre-tailwind-v4-YYYYMMDD
```

## Resumo do plano

| Fase | Duração estimada | Autorização exigida? |
|---|---|---|
| 0 Preparação | 1h | Sim (stakeholder) |
| 1 Baseline | 30min | Sim (rodar scripts) |
| 2 Branch local | 5min | Sim (criar branch) |
| 3 Node | 0 (já OK) | Não |
| 4 Deps conservadoras | 1h | Sim (`npm update`) |
| 5 Tailwind v4 | 4-8h | Sim (`npx upgrade` + manual) |
| 6 Vite | SKIP | Sim (se algum dia) |
| 7 Hugo | 1-2h | Sim (edits head.html) |
| 8 Revisão classes | 1h | Sim |
| 9-13 Testes | 4-8h | Sim (rodar) |
| 14 PT/EN | 1h | Não |
| 15 Decisão | 1h | Sim (merge) |
| 16 Reversão/descarte | 15min | Sim (branch -D) |

**Total: 5 dias ativos.** Pausa entre 8 e 15 permite tempo para bugs emergirem.

## Comandos proibidos nesta fase (auditoria)

- `git switch --create` (criação de branch)
- `git checkout -b` (idem)
- `git pull` (pode trazer commits de outros)
- `git push` (qualquer variante)
- `git commit`
- `npm install`, `npm update`, `npm uninstall`, `npm ci --production`
- `npm audit fix`
- `rm`, `mv` em qualquer arquivo funcional
- `npx @tailwindcss/upgrade`
- Modificar `package.json`, `package-lock.json`, `postcss.config.js`, `tailwind.config.js`, `head.html`, `main.css`
- Qualquer coisa em `docs/`, `assets/`, `content/`, `data/`, `hugo.yaml`, `.github/`

**Todos os comandos acima estão listados em `09-comandos-propostos.md` para futura execução, não nesta fase.**
