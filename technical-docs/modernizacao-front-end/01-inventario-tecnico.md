# 01 — Inventário técnico

Levantamento factual do estado do repositório em 2026-07-25, exclusivamente por comandos de consulta.

## Git

- **Branch atual:** `main`
- **HEAD:** `13bd3e105` — `Rebuild do site publicado após refactor de design`
- **Upstream:** `origin/main` (`https://github.com/cedis-unb/cedis-unb.github.io.git`)
- **Working tree:** limpo (0 modificações não commitadas)
- **Remotes:** único remoto `origin`
- **Hooks Git ativos:** 0 (só 14 `.sample` do template padrão do `git init`)
- **`git branch -vv`** confirma que `main` é a única branch local, e ela rastreia `origin/main`

## Publicação

- **`publishDir`:** `docs` (definido em `hugo.yaml:558`)
- **Mecanismo:** GitHub Pages servindo diretamente de `docs/` na branch `main` (repo `cedis-unb/cedis-unb.github.io`)
- **`baseURL`:** `https://cedis.unb.br/`
- **CI:** `.github/workflows/site-ci.yml` executa build + validações + testes; **não faz deploy**. O deploy é implícito: qualquer commit em `main` que altere `docs/` publica.
- **`paths-ignore` no CI:** `docs/**` e `.tool-versions` (para evitar CI redundante em commits que apenas regeneram `docs/`).
- **Também presente:** `.github/workflows/codeql.yml` — CodeQL para JavaScript.
- **Netlify/Cloudflare/Vercel:** não configurados (`.netlify`, `.vercel` ignorados no `.gitignore`; nada indicativo de uso).
- **`cloudflare.md`** existe na raiz — nota de configuração histórica, sem efeito operacional.

## Ambiente

| Item | Versão | Origem |
|---|---|---|
| Node.js (local) | v24.14.1 | `mise` (`.tool-versions:1` = `nodejs 24.14.1`) |
| npm | 11.18.0 | bundled com Node 24 |
| Hugo | v0.164.0+extended+withdeploy (darwin/arm64) | Homebrew |
| Node.js (CI) | 24 | `site-ci.yml:32` (`NODE_VERSION: '24'`) |
| Hugo (CI) | 0.164.0 | `site-ci.yml:31` |
| Python | 3.12.13 (mise) | usado por scripts em `scripts/` |

## Estrutura de diretórios

```
.
├── .github/workflows/     # site-ci.yml, codeql.yml
├── .lighthouseci/         # placeholder para reports
├── archetypes/            # (padrão Hugo)
├── assets/                # CSS + JS + images processados por Hugo Pipes
│   ├── css/
│   │   ├── main.css       # entrada Tailwind (@tailwind base/components/utilities)
│   │   ├── style.css      # saída compilada Tailwind (via `npx tailwindcss`)
│   │   ├── overrides.css  # hacks globais + @media print (122 linhas)
│   │   └── profile.css    # regras de #profile-content (807 linhas, criado 2026-07-25)
│   ├── js/
│   │   └── darkmode.js
│   └── images/            # featured/, global/, pages/, posts/ (72M antes, 7M depois)
├── content/               # 1558 arquivos .md em pt/en (posts, projects, products, people, publications, areas, opportunities, junte-se)
├── data/                  # areas.yaml, people.yaml, productions.yaml, projects.yaml
├── docs/                  # publishDir — SITE PUBLICADO (GitHub Pages)
├── i18n/                  # pt.yaml, en.yaml
├── layouts/               # 68 templates HTML
│   ├── _default/          # single, list, alumni, history, join, quiz, publications, etc.
│   ├── areas/, people/, projects/, products/, publications/, opportunities/, posts/
│   ├── partials/          # nav, footer, head, breadcrumbs, card-image, etc.
│   └── shortcodes/        # postsByCategoriesTags, filterPeople, publications, impact, tags, imgc, etc.
├── node_modules/          # (ignorado pelo git)
├── public/                # (ignorado pelo git — usado pelo CI, não pelo dev local)
├── resources/             # (ignorado pelo git — cache Hugo Pipes)
├── schemas/               # JSON schemas para validação de content/data
├── scripts/               # Python — build_publications.py, validate_content.py, validate_i18n.py, update_i18n.py
├── static/                # assets copiados verbatim: CNAME, favicon/, files/, images auxiliares
├── themes/                # NÃO EXISTE
├── tmp/                   # (ignorado pelo git — scripts descartáveis, dados de auditoria)
├── .browserslistrc        # NÃO EXISTE
├── .gitignore
├── .pa11yci.json          # 15 URLs para pa11y-ci
├── .tool-versions         # nodejs 24.14.1
├── CONVENTIONS.md         # regras editoriais + design system (§11 adicionado 2026-07-25)
├── PLANO-AUDITORIA-2026.md
├── PLANO-DESIGN.md        # (criado 2026-07-25)
├── ROADMAP.md
├── SECURITY.md
├── README.md
├── hugo.yaml              # config Hugo (615+ linhas — enableGitInfo, publishDir, i18n, module.hugoVersion, etc.)
├── lighthouserc.json      # 8 URLs para lighthouse-ci
├── lychee.toml            # link checker
├── package.json           # 11 devDependencies + 5 dependencies
├── package-lock.json
├── postcss.config.js      # {tailwindcss, autoprefixer}
├── tailwind.config.js     # 121 linhas — accent (com 550), primary, secondary, typography theme
└── theme.toml             # herança TailBliss (Apache-2.0)
```

## Configurações Hugo relevantes

- `hugo.yaml:550` — `enableGitInfo: true` (usa git para lastmod)
- `hugo.yaml:558` — `publishDir: "docs"`
- `hugo.yaml:615-617` — `module: { hugoVersion: { extended: true, min: "0.104.0" } }`
- Sem `theme:` — layouts são todos custom (não puxa TailBliss como tema Hugo)
- Sem `go.mod` — não usa Hugo modules com pacotes externos

## Scripts (package.json)

```json
"scripts": {
  "update-i18n":        "python3 scripts/update_i18n.py",
  "build:publications": "python3 scripts/build_publications.py",
  "check:publications": "python3 scripts/build_publications.py --check",
  "prestart":           "npm run build:publications",
  "start":              "concurrently npm:watch:*",
  "watch:tw":           "tailwindcss -i ./assets/css/main.css -o ./assets/css/style.css --watch",
  "watch:hugo":         "hugo server -d .hugo-server --disableFastRender",
  "build":              "npm run build:publications && hugo --minify --cleanDestinationDir && pagefind --site docs",
  "audit:a11y":         "pa11y-ci --config .pa11yci.json",
  "audit:lighthouse":   "lhci autorun --config=lighthouserc.json",
  "test":               "npm run check:publications && python3 scripts/validate_content.py && python3 scripts/validate_i18n.py"
}
```

## Dependências

### `devDependencies` (11)

| Pacote | Declarado | Instalado | Latest | Node req | Uso |
|---|---|---|---|---|---|
| `@lhci/cli` | `^0.15.1` | `0.15.1` | `0.15.1` | — | audit:lighthouse |
| `@tailwindcss/typography` | `^0.5.19` | `0.5.19` | `0.5.20` | — | plugin — 100+ classes prose |
| `alpinejs` | `^3.15.11` | `3.15.11` | `3.15.12` | — | **órfã** — Alpine vem via CDN |
| `autoprefixer` | `^10.4.22` | `10.4.22` | `10.5.4` | `^10 \|\| ^12 \|\| >=14` | plugin PostCSS |
| `browserslist` | `^4.28.2` | `4.28.2` | `4.28.7` | — | usada por autoprefixer com defaults |
| `caniuse-lite` | `^1.0.30001791` | `1.0.30001791` | `1.0.30001806` | — | banco de dados do browserslist |
| `concurrently` | `^9.2.1` | `9.2.4` | `10.0.4` | `>=18` (9.x) / `>=22` (10.x) | script `start` (watch:tw + watch:hugo) |
| `pa11y-ci` | `^4.1.1` | `4.1.1` | `4.1.1` | `>=20` | audit:a11y |
| `postcss` | `^8.5.6` | `8.5.19` | `8.5.23` | `^10 \|\| ^12 \|\| >=14` | plugin base do Hugo Pipes postCSS |
| `postcss-cli` | `^11.0.1` | `11.0.1` | `11.0.1` | `>=18` | não invocado por nenhum script |
| `tailwindcss` | `^3.4.19` | `3.4.19` | `4.3.3` | `>=14.0.0` (3.x) / `>=20` (4.x) | plugin PostCSS + CLI |

### `dependencies` (5)

| Pacote | Declarado | Instalado | Uso |
|---|---|---|---|
| `braces` | `>=3.0.3` | `3.0.3` | pinned para segurança (transitive) |
| `cross-spawn` | `^7.0.6` | `7.0.6` | pinned para segurança (transitive) |
| `markdown-it-emoji` | `^3.0.0` | `3.0.0` | não invocado explicitamente — herança |
| `pagefind` | `^1.5.2` | `1.5.2` | busca (via `pagefind --site docs`) |

### `overrides`

- `cross-spawn: ^7.0.6` (segurança)
- `tmp: ^0.2.6` (segurança)
- `uuid: ^11.1.1` (segurança)

### `npm audit`

`found 0 vulnerabilities`

## Processo de construção

**Fluxo em desenvolvimento (`npm start`):**
1. `prestart` roda `build_publications.py`
2. `concurrently` roda em paralelo:
   - `watch:tw` — tailwindcss CLI regenera `assets/css/style.css` a cada alteração
   - `watch:hugo` — `hugo server -d .hugo-server --disableFastRender`

**Fluxo em CI (`npm run build`):**
1. `build_publications.py`
2. `hugo --minify --cleanDestinationDir` → escreve para `docs/` (publishDir)
   - Hugo Pipes processa `assets/css/style.css` e `overrides.css` e `profile.css` via `postCSS` (usa `postcss.config.js` do repo, aplicando tailwindcss + autoprefixer)
   - Fingerprint e integrity hash em CSS
   - Processa imagens em WebP via `resources.Get + .Resize/.Fit`
3. `pagefind --site docs` — indexa o site para busca

Nota: `watch:tw` compila via CLI Tailwind independente; o pipeline PostCSS do Hugo ALSO roda Tailwind em cima de `style.css`. Isso significa que Tailwind é executado 2x em desenvolvimento — uma pelo CLI local (que atualiza `style.css` em disco), outra pelo Hugo Pipes ao servir. Overhead pequeno, mas duplicidade.

## Processo de publicação

1. Desenvolvedor roda `npm run build` localmente → atualiza `docs/`
2. Faz `git add docs/` (e demais mudanças de source)
3. Commit + push para `origin/main`
4. GitHub Pages detecta commit em `main` com mudanças em `docs/` e publica.

**Não há workflow de deploy explícito.** `site-ci.yml` faz apenas build+validate; a publicação em si é via mecanismo GitHub Pages built-in.

## Arquivos de configuração

- `hugo.yaml` — configuração Hugo (i18n, menus, params, permalinks, module.hugoVersion)
- `tailwind.config.js` — 121 linhas: darkMode `'class'`, colors (primary/secondary/accent com escalas 50-900, `accent.550: #C5272F` adicionado 2026-07-25), typography theme customizado, animations customizadas, plugins `[require('@tailwindcss/typography')]`
- `postcss.config.js` — 6 linhas: `plugins: { tailwindcss: {}, autoprefixer: {} }`
- `.pa11yci.json` — 15 URLs, WCAG2AA, timeout 45s
- `lighthouserc.json` — 8 URLs, desktop preset, thresholds performance 0.8/accessibility 0.9/seo 0.9/best-practices 0.9, LCP ≤ 2500ms, CLS ≤ 0.1
- `lychee.toml` — link checker (rodado em CI)
- `schemas/*.json` — JSON schemas para validate_content.py
- `.tool-versions` — `nodejs 24.14.1`
- `theme.toml` — herança de TailBliss (metadata do tema original)
- `postcss.config.js` — plugins PostCSS

## Segredos / arquivos sensíveis

- Nenhum `.env*` encontrado (comando `find . -name ".env*" -not -path "./node_modules/*"`)
- Workflows não usam `secrets.*` — só `github.workspace` e `matrix.language`
- Nenhum token/key/credential encontrado em busca de padrões comuns
- `cloudflare.md` é nota de configuração histórica, sem valores sensíveis

## Alpine.js — situação real

- Declarado em `package.json` como devDependency (`^3.15.11`)
- **Nunca é empacotado nem incluído via Hugo Pipes** (grep em `layouts/` e `assets/` confirma)
- **Carregado via CDN** em `layouts/partials/footer.html:2`:
  ```html
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
  ```
- URL usa `3.x.x` (auto-atualiza para o latest 3.x — hoje `3.15.12`)
- **Consequência:** a dependência npm é órfã e pode ser removida. Ou, alternativamente, migrada para bundle local (necessário para CSP restrita).

## Outros JS externos via CDN

- `layouts/_default/map.html:174` — D3.js 7.9.0
- `layouts/partials/footer.html:3` — `/pagefind/pagefind.js` (local, do pagefind CLI)
- `layouts/partials/footer.html:5` — `{{ $js.RelPermalink }}` (assets/js/darkmode.js processado por Hugo Pipes)

## Matriz de ambientes

| Ambiente | Hugo | Node.js | npm | SO | Arquitetura | Build |
|---|---|---|---|---|---|---|
| **Desenvolvimento local** (Sergio) | v0.164.0+extended+withdeploy | v24.14.1 | 11.18.0 | macOS Darwin 25.5.0 | arm64 (Apple Silicon) | `npm run start` → `concurrently` (tailwindcss watch + hugo server) |
| **CI (GitHub Actions)** | 0.164.0 (extended: true, via `peaceiris/actions-hugo@v3`) | 24 (via `actions/setup-node@v4`) | bundled (~10.x) | ubuntu-latest | x86_64 | `.github/workflows/site-ci.yml` — `npm ci` + `hugo --gc --minify --destination public` + `pagefind` + validações |
| **Produção** (GitHub Pages) | não roda Hugo (serve `docs/` já gerado) | não aplica | não aplica | infra GitHub | não aplica | serve estático de `docs/` na branch `main` |
| **Outros devs** | não identificado — obter via `hugo version` no ambiente deles | não identificado | não identificado | não identificado | não identificado | mesmos scripts npm/hugo, mas versões podem divergir |

**Divergências potenciais:** o único ambiente com validação estrita de versão é o CI (`HUGO_VERSION: '0.164.0'` em `site-ci.yml:31`). Devs locais dependem de `mise` ler `.tool-versions` (que só fixa Node, não Hugo). Recomendação: adicionar Hugo ao `.tool-versions` para forçar versão local:
```
nodejs 24.14.1
hugo 0.164.0
```

Isso é uma **sugestão para futura fase**, não executada nesta auditoria.

## Configuração Hugo relevante para migração Tailwind 4

Extraído de `hugo config` (comando de consulta):

```toml
[build]
  useresourcecachewhen = 'fallback'

  [[build.cachebusters]]
    source = '(postcss|tailwind)\.config\.(js|mjs|cjs)'
    target = '(css|styles|scss|sass)'
```

Isso significa que **cachebuster já está configurado** para invalidar cache CSS quando `tailwind.config.js` ou `postcss.config.js` mudarem. Para Alt 4, ao adicionar `[build.buildStats] enable = true`, a config ficaria:

```toml
[build]
  useresourcecachewhen = 'fallback'

  [buildStats]
    enable = true
    # opções: disableIDs, disableClasses, disableTags (default false)

  [[build.cachebusters]]
    source = '(postcss|tailwind)\.config\.(js|mjs|cjs)'
    target = '(css|styles|scss|sass)'

  [[build.cachebusters]]
    source = 'assets/.*\.(js|ts|jsx|tsx)'
    target = 'js'
```

**`[deployment]` já existe** com `invalidatecdn = true`, `maxdeletes = 256`, `workers = 10` — **mas SEM `targets:`**. Isso significa que `hugo deploy` hoje é no-op. Nenhuma providência necessária desde que ninguém adicione `targets:` sem autorização.

## Capability `withdeploy` — situação real

O binário Hugo local é `withdeploy` (compilado com suporte a `hugo deploy`). Isso permite comandos como:

- `hugo deploy` — envia `docs/` para S3/GCS/Azure conforme `[deployment.targets]`
- `hugo deploy --force`
- `hugo deploy --dryRun` (seguro para auditoria)

**Como NÃO existe `[deployment.targets]` em `hugo.yaml`**, executar `hugo deploy` hoje resulta em:

```
Error: no cloud storage targets are configured
```

**Risco:** se algum dia alguém adicionar targets (S3 bucket, GCS bucket) sem revisão de segurança, um `hugo deploy` teria efeito imediato em infraestrutura de terceiros.

**Providência:**
- Adicionar `hugo deploy` a `09-comandos-propostos.md` como Categoria F (proibido sem autorização) — feito.
- Documentar em CONVENTIONS.md que `[deployment.targets]` só pode ser adicionado após revisão de segurança.

## Fluxo atual detalhado de CSS

```
assets/css/main.css                  (entrada — @tailwind directives)
    │
    ├── watch:tw local (npm run start)
    │     │
    │     ▼
    │   tailwindcss CLI aplica base+components+utilities
    │     │
    │     ▼
    │   assets/css/style.css        (150KB, no disco, versionado? verificar)
    │
    │   [em dev — Hugo server lê style.css atualizado]
    │   [em CI — sem watch:tw, hugo lê style.css do último commit... mas style.css é atualizado antes]
    │
Hugo Pipes em head.html:
    resources.Get "css/style.css"
        │
        ▼
    | postCSS (aplica postcss.config.js: tailwindcss + autoprefixer)
        │
        ▼
    | minify (produção)
        │
        ▼
    | fingerprint (produção)
        │
        ▼
    | resources.PostProcess (produção)
        │
        ▼
    docs/css/style.min.<hash>.css   (fingerprintado, com integrity hash)

    └── link stylesheet em <head>

Paralelo — profile.css:
    resources.Get "css/profile.css"
        │
        ▼
    (mesmo pipeline: postCSS + minify + fingerprint + PostProcess)
        │
        ▼
    docs/css/profile.min.<hash>.css

Paralelo — overrides.css:
    (mesmo pipeline)
        │
        ▼
    docs/css/overrides.min.<hash>.css
```

**Observação:** o duplo processamento (Tailwind CLI local + PostCSS no Hugo) executa Tailwind 2x em dev, mas 1x em CI. `style.css` versionado no repo é obsoleto assim que main.css mudar sem watch:tw. Em Alt 4 essa duplicação some.

## Fluxo proposto para Alt 4 (Hugo native Tailwind)

```
assets/css/main.css                  (entrada — @import "tailwindcss"; @plugin ...; @source "hugo_stats.json")
    │
    ▼
Hugo (durante build):
    1. Renderiza todos os templates para gerar hugo_stats.json (raiz do projeto)
    2. templates.Defer atrasa a compilação CSS para depois
    3. resources.Get "css/main.css"
    4. | css.TailwindCSS opts  (opts = { minify: true (prod), optimize: true (prod) })
        │   internamente:
        │     - lê main.css
        │     - resolve @import (tailwindcss)
        │     - resolve @source (hugo_stats.json)
        │     - resolve @plugin (@tailwindcss/typography)
        │     - gera CSS final via @tailwindcss/cli
    5. | fingerprint (produção)
        │
        ▼
    docs/css/main.<hash>.css        (fingerprintado, com integrity hash)

    └── link stylesheet em <head>
```

Um único arquivo CSS final (`main.<hash>.css`) substitui os 3 atuais (`style`, `overrides`, `profile`) — os `@import` internos concatenam tudo. Ou mantém separados via 3 chamadas `css.TailwindCSS` com 3 arquivos de entrada.

## Sinais para futuras decisões

- Todo o site é estático, renderizado em build (sem SPA, sem SSR runtime)
- Alpine.js é o único framework JS runtime, e é usado para interações menores (accordion, menu, filter)
- CSS total minificado: 149 KB (`style.min.css` 126KB + `profile.min.css` 22KB + `overrides.min.css` 1.5KB)
- Imagens: `assets/images/featured/` = 7,1 MB após otimização de 2026-07-25 (era 72 MB antes)
- `docs/` total: ~280 MB (dominado por WebP derivadas)
