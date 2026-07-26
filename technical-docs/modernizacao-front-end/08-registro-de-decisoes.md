# 08 — Registro de decisões arquiteturais (ADRs)

Cada decisão segue o formato: Contexto → Alternativas → Decisão → Justificativa → Consequências → Riscos → Possibilidade de revisão.

## ADR-001 — Migrar para Tailwind CSS 4

- **Data:** proposto 2026-07-25 (execução pendente de autorização)
- **Status:** proposto

### Contexto

Site CEDIS em Tailwind CSS 3.4.19 (linha 3.x, patch mais recente). Tailwind 4.3.3 estável, com engine reescrito (Oxide, Rust), sintaxe CSS-first opcional, dispensa PostCSS e Autoprefixer, requer Node ≥20 e navegadores modernos (Safari 16.4+, Chrome 111+, Firefox 128+). O tema base original (TailBliss) já migrou.

### Alternativas

1. Manter Tailwind 3 indefinidamente
2. Migrar para Tailwind 4

### Decisão

**Migrar para Tailwind 4** com autorização explícita, em branch local.

### Justificativa

- Tailwind 3.4 é fim-de-vida próximo (fixes de segurança tendem a cessar).
- Migração é bem documentada e há ferramenta oficial (`npx @tailwindcss/upgrade`).
- Ambiente já pronto (Node 24 no CI).
- Remove 3-4 dependências (autoprefixer, browserslist, caniuse-lite, postcss-cli).
- Alinha com o ecossistema atual.

### Consequências

- Nova sintaxe de opacidade `<color>/<n>` (v3 support continua para compat).
- Renames automáticos aplicáveis: `shadow-sm` → `shadow-xs`, etc.
- Border color default = `currentColor` (exige revisão manual).
- Dispensa PostCSS + Autoprefixer.
- Requer navegadores modernos.

### Riscos

R2, R3, R4, R5, R11 (ver `05-matriz-de-riscos.md`).

### Revisão futura

Reavaliar em 12 meses se Tailwind 5 for anunciado.

## ADR-002 — Não adotar Vite nesta migração

- **Data:** proposto 2026-07-25
- **Status:** proposto

### Contexto

TailBliss atual usa `@tailwindcss/vite`. Ecossistema recomenda Vite quando há JS complexo. Este site é 100% estático via Hugo, sem SPA, sem chunk splitting, sem TypeScript, Alpine.js carregado via CDN.

### Alternativas

1. Adotar `@tailwindcss/vite` como TailBliss.
2. Manter Hugo Pipes com `@tailwindcss/postcss`.
3. Adotar integração nativa Hugo `css.TailwindCSS` (ver ADR-003).

### Decisão

**Não adotar Vite** — em qualquer variante.

### Justificativa

- Hugo Pipes já resolve toda a demanda atual: fingerprint, integrity, minify, WebP resize, concat.
- Reintroduzir Vite exigiria reescrever `layouts/partials/head.html` para ler manifest.json.
- Perde-se `.Data.Integrity` do Hugo Pipes.
- Dev-server duplo (Vite 5173 + Hugo 1313) aumenta complexidade sem retorno para site estático.
- HMR de Tailwind em Hugo `--disableFastRender` já é suficiente para o volume de mudanças típicas.
- Rollback de Vite é caro (reescrita).

### Consequências

- Segue-se dependente de Hugo Pipes (que é robusto e estável desde v0.100).
- Se algum dia surgir necessidade concreta (SPA, TypeScript bundling), reabrir ADR.

### Riscos

Nenhum — evita risco R13 (perda de Fingerprint+Integrity).

### Revisão futura

Reavaliar se aparecer requisito de SPA, TypeScript com type-checking em build, ou plugins Vite sem equivalente Hugo.

## ADR-003 — Preferir `@tailwindcss/postcss` sobre `css.TailwindCSS` (nativo Hugo) — decisão preliminar

- **Data:** proposto 2026-07-25
- **Status:** proposto — **a validar após avaliação da 4ª alternativa**

### Contexto

Hugo 0.164 introduziu função `css.TailwindCSS` que integra nativamente com Tailwind 4 via `@tailwindcss/cli`. Elimina PostCSS pipeline. Requer:

- Instalar `@tailwindcss/cli` + `tailwindcss@4`
- Habilitar `[build.buildStats] enable = true` no `hugo.yaml`
- Adicionar `@source "hugo_stats.json"` ao `main.css`
- Usar `templates.Defer` em partial que gera link CSS (para sites multilíngue)
- Substituir `resources.Get "css/main.css" | postCSS` por `resources.Get "css/main.css" | css.TailwindCSS`

### Alternativas

1. **Alt 2 do doc 03:** Tailwind 4 + `@tailwindcss/postcss` + Hugo Pipes tradicional
2. **Alt 4 do doc 03:** Tailwind 4 + `css.TailwindCSS` (integração nativa Hugo)

### Decisão preliminar

**Preferir Alt 4 (integração nativa Hugo) SE:**

- `hugo_stats.json` cobrir todas as classes usadas (incluindo condicionais i18n)
- `templates.Defer` funcionar corretamente com nosso setup PT/EN
- Não houver perda de fingerprint/integrity/minify

Caso contrário, cair para Alt 2 (PostCSS).

### Justificativa (por Alt 4 se viável)

- Uma dependência a menos: PostCSS não é necessário.
- Menos passos de pipeline (Hugo → Tailwind → CSS direto).
- Melhor integração com hot reload de Hugo em desenvolvimento.
- Já é o pipeline recomendado pela documentação oficial do Hugo desde v0.161.

### Riscos específicos da Alt 4

- Se `hugo_stats.json` gerado em build só de um idioma → CSS incompleto para o outro.
- Comportamento diferente entre `hugo` e `hugo server` para stats.
- Menor rodagem em produção (é feature recente).

### Consequências

- Adiciona: `@tailwindcss/cli`, `tailwindcss@4`, `@tailwindcss/typography`
- Remove: `postcss`, `autoprefixer`, `browserslist`, `caniuse-lite`, `postcss-cli`
- Adiciona ao `hugo.yaml`: `[build.buildStats] enable = true`
- Adiciona a `main.css`: `@import "tailwindcss"; @plugin "@tailwindcss/typography"; @source "hugo_stats.json";`
- Adiciona `hugo_stats.json` ao `.gitignore`
- Reescreve `head.html` para usar `css.TailwindCSS` (com `templates.Defer` para multilíngue)

### Revisão futura

Reavaliar em spike de 4h antes da migração real. Se `hugo_stats.json` + `templates.Defer` provarem-se estáveis, adotar Alt 4. Se instáveis, cair para Alt 2 com custo idêntico de migração.

## ADR-004 — Manter `@tailwindcss/typography`

- **Data:** proposto 2026-07-25
- **Status:** proposto

### Contexto

Plugin `@tailwindcss/typography` provê classes `prose`, `prose-invert`, `prose-h*`, `prose-a`, etc. Site CEDIS tem >129 usos em templates para renderizar Markdown de perfis, notícias, publicações, projetos.

### Alternativas

1. Manter plugin
2. Substituir por CSS custom (`profile.css` já faz parcialmente para `#profile-content`)
3. Remover completamente

### Decisão

**Manter.**

### Justificativa

- Plugin oficial, mantido, compatível com Tailwind 4 (v0.5.20).
- 129 usos ativos com múltiplos modificadores (`prose-a`, `prose-h*`, `prose-invert`, `prose-zinc`, `prose-strong`, `prose-p`, `prose-li`).
- Substituir por CSS custom exigiria escrever ~500 linhas de tipografia + manter para dark mode + preservar comportamento responsivo.
- TailBliss removeu porque simplificou stack; CEDIS tem conteúdo acadêmico rico (mestrados, doutorados, artigos) que justifica.

### Consequências

- Uma dependência extra mantida (`@tailwindcss/typography@0.5.20`).
- Migração Tailwind 4: sintaxe `@plugin` no CSS-first ou `plugins: [...]` no JS config.

### Riscos

Nenhum novo.

### Revisão futura

Reavaliar se plugin for descontinuado ou se conteúdo Markdown for eliminado do site.

## ADR-005 — Alpine.js: manter CDN, remover devDependency órfã

- **Data:** proposto 2026-07-25
- **Status:** proposto (decisão auxiliar à migração)

### Contexto

`alpinejs@3.15.11` declarado em `devDependencies` do `package.json`. **Nunca é empacotado** nem servido via Hugo Pipes. É apenas informativo. Alpine real vem via CDN em `footer.html:2` — `alpinejs@3.x.x` (auto-atualiza patch).

### Alternativas

1. Manter status quo (CDN + devDep órfã)
2. Remover devDep órfã, manter CDN
3. Bundlear Alpine via Hugo Pipes ou `js.Build`
4. Pinar Alpine no CDN (`alpinejs@3.15.12` em vez de `3.x.x`)

### Decisão

**Combinar #2 + #4:** remover devDep órfã E pinar versão no CDN.

### Justificativa

- devDep sem uso é ruído.
- CDN pinada evita surpresa de patch quebrado.

### Consequências

- `package.json` fica mais limpo.
- Perde flexibilidade de auto-atualizar patches.

### Riscos

- Novo patch de segurança de Alpine 3.x não chega automaticamente — auditar 1x/trimestre.

### Revisão futura

Reavaliar se surgir CSP restritiva (obrigaria bundle local).

## ADR-006 — Node.js 24 como padrão

- **Data:** de facto (já ativo)
- **Status:** ratificado

### Contexto

`.tool-versions` fixa `nodejs 24.14.1`. CI usa `NODE_VERSION: '24'`. Tailwind 4 requer ≥20, Vite ≥20.19.

### Decisão

**Manter Node 24 como padrão.** Não migrar para Node 22 (o prompt sugeriu 22 mas o repo já usa 24).

### Justificativa

- Já é o ambiente ativo em CI e local.
- Node 24 é LTS ativa; suporte até 2027.

### Consequências

- Nenhuma — status quo.

### Riscos

Nenhum.

### Revisão futura

Migrar para próxima LTS quando 24 atingir maintenance.

## ADR-007 — Descartar Autoprefixer, Browserslist, caniuse-lite

- **Data:** proposto 2026-07-25
- **Status:** proposto (parte da migração)

### Contexto

Tailwind 4 gerencia prefixos e polyfills internamente via `@property` e `color-mix()`. Autoprefixer torna-se desnecessário. Browserslist e caniuse-lite servem apenas ao Autoprefixer neste projeto.

### Alternativas

1. Manter para segurança
2. Remover

### Decisão

**Remover** as três (autoprefixer, browserslist, caniuse-lite) e também `postcss-cli` (nunca invocado por scripts). `postcss` em si pode continuar como transitive se `@tailwindcss/postcss` depender.

### Justificativa

- Redução de 4 devDependencies + suas transitives.
- Menos CVEs a rastrear.

### Consequências

- Browsers muito antigos (Safari <16.4, Chrome <111) perdem prefixes mesmo que aceitem CSS moderno — irrelevante porque Tailwind 4 já não os suporta oficialmente.

### Riscos

R15 (baixo — usuários já não têm suporte v4 mesmo).

### Revisão futura

N/A.

## ADR-008 — Manter `publishDir: docs` (deploy via GitHub Pages a partir de `docs/` no `main`)

- **Data:** de facto (já ativo)
- **Status:** ratificado

### Contexto

Atualmente site publicado via GitHub Pages servindo diretamente `docs/` na branch `main`. Cada commit em main que toca `docs/` publica.

### Alternativas

1. Manter (GitHub Pages built-in)
2. Migrar para GitHub Actions com deploy dedicado
3. Migrar para Netlify/Cloudflare Pages

### Decisão

**Manter** por enquanto — fora do escopo desta migração.

### Justificativa

- Migração de deploy é decisão independente.
- Não afeta a decisão de Tailwind 4.

### Consequências

- Convivemos com o risco R1 (push acidental publica).

### Riscos

R1 mitigado por hook local + branch dev sem upstream.

### Revisão futura

Considerar migrar deploy para GitHub Actions em ciclo separado.

## ADR-009 — Formato de commits durante migração

- **Data:** proposto 2026-07-25
- **Status:** proposto

### Contexto

Migração toca muitos arquivos. Commit único vs commits atômicos por fase.

### Alternativas

1. Commit único (fácil rollback via revert)
2. Commits atômicos por fase (fácil bisect e review)

### Decisão

**Commits atômicos por fase**, seguindo o mesmo padrão do refactor de design de 2026-07-25 (6 commits — CSS, imagens, cards, bugs, docs, docs/).

### Justificativa

- Já é o padrão do repo (ver commits `c2c183183` a `13bd3e105`).
- Permite git bisect por fase.
- Facilita revert cirúrgico.

### Consequências

- Requer disciplina para não misturar mudanças entre fases.

### Riscos

Nenhum novo.

### Revisão futura

N/A.

## ADR-010 — Não configurar `hugo deploy`

- **Data:** proposto 2026-07-25
- **Status:** proposto

### Contexto

Binário Hugo local instalado com capability `withdeploy`. `hugo.yaml` tem seção `[deployment]` com `invalidatecdn`, `maxdeletes`, `workers` — MAS **sem `targets:`** configurados. Rodar `hugo deploy` hoje não faria nada operacional.

### Decisão

**Manter sem `targets:` configurados.** Adicionar `hugo deploy` (e variantes) à lista de comandos proibidos sem autorização, por precaução.

### Justificativa

- Sem targets, `hugo deploy` é no-op.
- Melhor prevenir configuração acidental futura que possa criar caminho para deploy sem revisão.

### Consequências

- Nenhuma mudança operacional.

### Riscos

Nenhum ativo. R (potencial) se alguém adicionar `targets:` sem revisão de segurança.

### Revisão futura

Se surgir necessidade concreta de S3/GCS/Azure, criar ADR próprio.
