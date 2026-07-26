# 00 — Resumo executivo

**Auditoria e plano de modernização do front-end do site CEDIS**
**Data:** 2026-07-25
**Escopo:** avaliar viabilidade e custo de migração de Tailwind CSS 3.4.19 → Tailwind CSS 4.x, com opção de adoção de Vite.
**Estado do repo no momento da auditoria:** branch `main` em `13bd3e105`, working tree limpo, remoto `origin` = GitHub repo público.

## Situação atual

| Item | Estado |
|---|---|
| Node.js local + CI | **24.14.1** (CI usa `NODE_VERSION: '24'`) — Node 22 **não é o alvo** |
| Hugo | 0.164.0+extended+withdeploy |
| Tailwind CSS | 3.4.19 (patch atual da linha 3.x) |
| Bundler CSS | PostCSS 8.5.19 + Autoprefixer 10.4.22 via Hugo Pipes |
| Vite | não usado |
| Alpine.js | 3.15.11 declarado em `package.json`, mas **carregado via CDN `alpinejs@3.x.x`** em `layouts/partials/footer.html:2` (dependência de dev é órfã) |
| Publicação | GitHub Pages a partir de `docs/` (versionado em cada commit em `main`) |
| CI | `.github/workflows/site-ci.yml` — build + validate + pa11y + lighthouse + lychee; **não faz deploy** |
| Vulnerabilidades | 0 (`npm audit`: found 0 vulnerabilities) |
| Segredos expostos | 0 (nenhum `.env`, workflows não referenciam secrets além do `github.workspace`) |

## Principais achados

1. **Ambiente já está pronto para Tailwind 4** — Node 24 (v4 exige ≥20), sem preprocessadores CSS, sem uso de `@screen`/`@variants`, sem `theme()` em CSS.

2. **72+ classes Tailwind construídas dinamicamente via `printf` em templates Hugo** — concentradas em `layouts/people/single.html` (18 instâncias), inseridas em `$content` via `replaceRE`. Tailwind 3 detecta porque cada literal aparece intacto no HTML fonte; Tailwind 4 mantém a mesma capacidade **se os arquivos estiverem em `content` (v3) ou `@source` (v4)**. Risco baixo se a mesma configuração for preservada, mas é um multiplicador de custo se decidirmos migrar essas chamadas para partials tipados.

3. **`text-opacity-40` em `layouts/index.html:737,738`** — removido em Tailwind 4. Precisa virar `text-primary-600/40`.

4. **25 usos de `flex-shrink-0`** — em v4 é `shrink-0`.

5. **81 usos de `shadow-sm`** — em v4 esse valor virou `shadow-xs` (2px em vez de 4px). Se mantidos como estão, elementos ficam com sombra maior (a v3 shadow-sm = 2px passou a se chamar shadow-xs em v4; shadow-sm em v4 = 4px, valor antes de `shadow`). **Ferramenta `npx @tailwindcss/upgrade` faz o rename automaticamente.**

6. **`shortcodes/imgc.html:89`** tem classe dinâmica `imgB-{{ $imgBd5 }}` (hash MD5). Se essa classe existe apenas para ser referenciada de dentro do CSS/JS gerado pelo próprio shortcode (variável CSS via data-attribute? ver `03`), não é problema; se for utility Tailwind esperando gerar variantes, quebra.

7. **`assets/css/main.css` linhas 6-21 tem `font-family: …;` fora de qualquer seletor** — CSS inválido, ignorado silenciosamente hoje. Bug pré-existente, sem relação com o refactor.

8. **Alpine 3.x carregado via CDN pinado em `3.x.x`** (auto-atualiza para o patch mais recente). A dependência npm `alpinejs@3.15.11` é órfã — nunca é empacotada nem servida pelo Hugo Pipes. Pode ser removida das devDependencies OU migrada para bundle local (necessário para CSP restritivo futuro).

9. **PostCSS + Autoprefixer podem ser removidos em v4** — v4 gerencia vendor prefixes internamente via `@property` e `color-mix()`. Isso remove 4 dependências (postcss, postcss-cli, autoprefixer, browserslist, e transitivamente caniuse-lite).

10. **`@tailwindcss/typography` continua compatível com v4** e é usado em 100+ lugares (`prose`, `prose-a`, `prose-h*`, `prose-invert`, `prose-zinc`, `prose-strong`, `prose-p`, `prose-li`). **Manter.**

## Riscos críticos

| # | Risco | Gravidade |
|---|---|---|
| R1 | Perda visual em elementos com `shadow-sm` se a migração automática não for aplicada corretamente | Alta |
| R2 | Site quebrado se `text-opacity-40` for renderizado sem substituto (2 elementos no `<svg>` decorativo da home) | Média |
| R3 | Hugo Pipes hoje resolve `postCSS` a `overrides.css` e `profile.css`; migrar para Vite exige refatorar pipeline de CSS (não é apenas trocar plugin) | Alta |
| R4 | Navegadores institucionais desatualizados (Safari <16.4, Chrome <111) perdem suporte visual em Tailwind 4 | Média — depende do público real |
| R5 | Deploy via `docs/` committed: qualquer commit em `main` que toque `docs/` publica no site | Alta se combinar com pushes acidentais durante a migração |
| R6 | Alpine.js via CDN pinado em `3.x.x` pode receber patch quebrado sem aviso; sem lock local | Baixa (histórico de estabilidade de Alpine 3) |

## Recomendação geral

**Favorável com condicionantes.** A migração para Tailwind 4 é viável, o ambiente está preparado (Node 24, sem PostCSS specials), o principal risco (classes dinâmicas) já é conhecido, e o TailBliss (tema base original) já fez essa migração. **Não recomendamos adotar Vite neste momento** — o pipeline Hugo Pipes atual é simples, integrado, sem manifest indireto; adotar Vite reintroduz complexidade sem benefício claro para um site estático servido de `docs/`.

Arquitetura recomendada:

**Tailwind 4 + @tailwindcss/postcss + Hugo Pipes (sem Vite)**

- Mantém pipeline Hugo Pipes existente (`resources.Get "css/main.css" | postCSS`).
- Substitui plugin PostCSS: `tailwindcss` → `@tailwindcss/postcss`.
- Remove `autoprefixer`, `browserslist`, `caniuse-lite` (não necessários em v4).
- Substitui `@tailwind base/components/utilities` em `main.css` por `@import "tailwindcss"`.
- Migra `tailwind.config.js` para `@theme` em CSS-first (opcional; JS config funciona via `@config`).
- Roda `npx @tailwindcss/upgrade` para o rename automático (shadow-sm → shadow-xs, text-opacity-40 → text-primary-600/40, flex-shrink → shrink etc).
- Preserva `@tailwindcss/typography` (continua compatível).

## Decisão sobre migrar

**Migrar agora — condicionado a:**

- Rodar a migração inteiramente em branch local **não publicada** (`dev/tailwind-v4-vite-local` conforme prompt).
- Estabelecer linha de base pa11y + lighthouse ANTES da migração (comparar antes/depois).
- Realizar validação visual manual em ≥10 rotas em PT/EN e light/dark.
- Aceitar que navegadores muito antigos (Safari <16.4, Chrome <111) podem apresentar degradação — verificar público real do CEDIS via GA antes de aprovar.
- **Não** adotar Vite nesta migração. Vite pode ser considerado em ciclo futuro se houver necessidade concreta (ex.: HMR local mais rápido, chunk splitting de JS).

## Condições necessárias antes da implementação

- [ ] Autorização explícita para criar branch local `dev/tailwind-v4-vite-local`.
- [ ] Autorização explícita para modificar `package.json` e `package-lock.json`.
- [ ] Autorização explícita para rodar `npx @tailwindcss/upgrade`.
- [ ] Linha de base Lighthouse + pa11y capturada.
- [ ] Backup do estado atual (tag git `pre-tailwind-v4-YYYYMMDD`).
- [ ] Definição de janela de teste (≥ 3 dias sem deploy).
- [ ] Confirmação de que nenhum documento oficial do CEDIS depende de Safari <16.4 (verificação com stakeholder).

Nenhuma dessas condições foi executada nesta auditoria.

## Parecer complementar — arquitetura Hugo native

Após pesquisa adicional sobre `css.TailwindCSS`, `hugo_stats.json` e `templates.Defer`, a recomendação evoluiu.

**Arquitetura preferida atualizada:**

**Tailwind 4 integrado nativamente ao Hugo** (Alt 4 do doc 03):

- `hugo v0.164.0+extended` (já temos) — suporta `css.TailwindCSS` desde v0.161
- `tailwindcss@4 + @tailwindcss/cli@4 + @tailwindcss/typography@0.5.20`
- `[build.buildStats] enable = true` em `hugo.yaml`
- `main.css`: `@import "tailwindcss"; @plugin "@tailwindcss/typography"; @source "hugo_stats.json"; @config "../../tailwind.config.js";`
- `hugo_stats.json` no `.gitignore` (gerado a cada build)
- `templates.Defer` no partial `head.html` para garantir compilação após todos os idiomas
- **Sem PostCSS, sem Autoprefixer, sem Browserslist, sem caniuse-lite, sem postcss-cli, sem @tailwindcss/postcss, sem Vite, sem @tailwindcss/vite**
- Alpine.js continua via CDN pinado (`3.15.12` em vez de `3.x.x`)

**Alt 2 (Tailwind 4 + `@tailwindcss/postcss` + Hugo Pipes)** fica como **fallback obrigatório** se, na spike de validação, `templates.Defer` + `hugo_stats.json` provarem-se instáveis para nosso setup PT/EN.

### Parecer objetivo — 14 respostas

1. **Hugo 0.164 favorece Tailwind 4?** — **Sim.** Suporta `css.TailwindCSS` nativamente.
2. **Ambiente de produção usa versão compatível?** — Produção não roda Hugo (é GitHub Pages servindo estático). CI usa 0.164.0 (mesmo local). Sem divergência ativa.
3. **CSS atual é por Hugo Pipes?** — **Sim.** `resources.Get "css/main.css" | postCSS | minify | fingerprint | resources.PostProcess`.
4. **`css.TailwindCSS` pode substituir?** — **Sim, com adaptação.** Requer `@tailwindcss/cli`, `[build.buildStats]`, `@source "hugo_stats.json"`, `templates.Defer`.
5. **`hugo_stats.json` é adequado?** — **Sim, com cautela.** Requer `templates.Defer` para site multilíngue; opcionalmente `@source "layouts/**/*.html"` como safety net.
6. **`templates.Defer` é necessário por causa do multilíngue?** — **Sim.** Sem ele, arriscamos CSS incompleto se apenas um idioma for renderizado no momento em que head.html executar.
7. **`@tailwindcss/typography` deve ser mantido?** — **Sim.** 129 usos ativos com múltiplos modificadores; conteúdo Markdown do CEDIS é rico e acadêmico. Migrar para `@plugin "@tailwindcss/typography"` no CSS.
8. **JavaScript pode ser processado por `js.Build`?** — **Sim, se algum dia decidirmos bundlear Alpine local.** Não é necessário nesta migração — Alpine continua via CDN.
9. **Vite oferece benefício concreto neste repo?** — **Não.** Ver ADR-002.
10. **PostCSS + Autoprefixer podem ser removidos?** — **Sim** (junto com browserslist, caniuse-lite, postcss-cli).
11. **`withdeploy` cria risco real?** — **Não hoje** (sem `[deployment.targets]`). Sim se targets forem adicionados sem revisão. Listado em Cat F dos comandos proibidos.
12. **Qual arquitetura é recomendada?** — **Alt 4** (Hugo nativo com `css.TailwindCSS`). Alt 2 como fallback.
13. **Requisitos a sincronizar entre dev e produção?**
    - Hugo ≥0.161 em CI (**temos 0.164.0** — OK)
    - Node ≥20 em CI (**temos 24** — OK)
    - Adicionar `hugo 0.164.0` ao `.tool-versions` para forçar versão local (**recomendado**)
    - Atualizar `module.hugoVersion.min` em `hugo.yaml` de `"0.104.0"` para `"0.161.0"`
14. **Alterações antes de iniciar migração:**
    - **Autorização explícita** (stakeholder).
    - Verificar via Google Analytics que <2% dos usuários usam Safari <16.4 ou Chrome <111.
    - Tag de backup (`git tag -a pre-tailwind-v4-YYYYMMDD`).
    - Baseline pa11y + lighthouse capturada.
    - Spike de 4h para validar `templates.Defer` + `hugo_stats.json` — se falhar, adotar Alt 2.
    - Instalar hook `.git/hooks/pre-push` bloqueando branch dev.

### Classificação final

**Favorável com condicionantes.**

Condicionantes:

- Autorização explícita antes de cada fase modificadora (ver `04-plano-de-migracao.md`).
- Spike técnico obrigatório (4h) para validar Alt 4 vs Alt 2.
- Baseline capturada antes de qualquer mudança.
- Branch local `dev/tailwind-v4-vite-local` sem upstream.
- Zero push acidental — hook `pre-push` instalado.
- Confirmação estatística de público em navegadores modernos.

## Confirmação de não-alteração

- Nenhuma dependência foi atualizada.
- Nenhum código funcional foi modificado.
- Nenhum arquivo em `docs/`, `assets/`, `content/`, `layouts/`, `data/`, `hugo.yaml`, `package.json`, `package-lock.json`, `tailwind.config.js` foi tocado.
- Apenas foram criados 10 documentos em `technical-docs/modernizacao-front-end/` (fora do `publishDir`).
- Nenhum commit foi feito.
- Nenhum push foi feito.
- Git `HEAD` continua em `13bd3e105` (commit `Rebuild do site publicado após refactor de design`).
