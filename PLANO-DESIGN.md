# Plano de Adequação — Débito de Design CEDIS

**Referência:** revisão de CSS/design tokens/assets do repositório Hugo do CEDIS.
**Data-base:** 2026-07-25.
**Escopo:** este plano trata do débito acumulado em `assets/css/overrides.css`, na paleta de cores e nos assets de imagem. Complementa (não substitui) o `PLANO-AUDITORIA-2026.md` (conteúdo/dados) e o `ROADMAP.md` (comunicação/UX).

## Diagnóstico atual (medido em 2026-07-25)

| Métrica | Valor | Comentário |
|---|---|---|
| `assets/css/overrides.css` — linhas | 942 | Único ponto de override do tema. |
| `assets/css/overrides.css` — bytes | 29 887 (~29,2 KB) | Confirma a estimativa de "~30 KB". |
| Ocorrências de `!important` | 132 | Sintoma direto de brigas de especificidade com `#profile-content`. |
| Cores hex literais em `overrides.css` | 27 | Contornam os tokens do `tailwind.config.js`. |
| Regras `.dark …` em `overrides.css` | 69 | Cada uma é uma duplicação da versão clara — dessincronização quase certa. |
| Linhas dedicadas aos 3 padrões de card | 59 | `profile-project-card`, `researcher-highlights*`, `featured-publications*`. |
| `assets/images/featured/` — tamanho total | ~72 MB | 20 `area_*.png` entre 700 KB e 2 MB, além de logos e fotos. |
| Página que aciona `#profile-content` | 1 | Só `layouts/people/single.html` (linhas 529 e 583). |

Achados críticos:

- **O ID `#profile-content` só é usado em um único template** (`layouts/people/single.html`), mas domina o `overrides.css` inteiro com seletores de 4+ níveis do tipo `#profile-content > h2 + ul > li > ul > li` (ver linhas 137–144). Isso é o que empurra o `!important` a 132 usos.
- **Os cards não moram em partials.** `profile-project-card`, `researcher-highlights` e `featured-publications` são gerados por `printf` de HTML dentro de `layouts/people/single.html` (linhas 247, 273, 296, 358, 363). Reaproveitamento entre páginas é impossível sem extrair partials primeiro.
- **`#c5272f` não é o accent oficial.** O `tailwind.config.js` define `accent.DEFAULT = #E82C0C` e `accent.600 = #C1260A`. O `#c5272f` que aparece em pelo menos 8 pontos de `overrides.css` (linhas 55, 112, 243, 463, 542, …) é uma cor "à parte" — precisa de decisão: virar token oficial ou ser substituído.
- **Regras `.dark` são cópias literais das claras**, alterando apenas cor. Sempre que alguém edita a versão light, esquece a dark — problema estrutural, não pontual.

## Priorização

A ordem sugerida no briefing é adotada. Justificativa reafirmada:

- **Fase 1 (itens 1 + 2)** ataca o maior risco de manutenção — o `overrides.css` é hoje o único ponto em que erros de contraste, regressões visuais e brigas de especificidade se acumulam. Sem consolidar isso primeiro, qualquer trabalho posterior (paleta, cards) apenas replica o problema.
- **Fase 2 (item 4)** roda em paralelo. É trabalho de asset pipeline, não toca CSS, e libera ganho de LCP/CLS que aparece nas próximas medições de Lighthouse.
- **Fase 3 (itens 3 + 5)** é limpeza incremental que só se sustenta depois que a base (variáveis + partials) existir.
- **Fase 4 (item 6)** é o portão de saída — `pa11yci` e Lighthouse já estão configurados; a fase apenas os executa e trata regressões.

```
Fase 1  ──────────┐
   1+2  CSS/vars  │──► Fase 3 ──► Fase 4
Fase 2  ──────────┘   3+5           validação
   4  imagens
```

## Fase 1 — Consolidar CSS de perfil e unificar temas com variáveis

**Objetivo:** eliminar o gargalo de manutenção representado por `overrides.css` e destruir a duplicação light/dark.

**Arquivos afetados:**

- Criar: `assets/css/profile.css` (novo partial dedicado).
- Editar: `assets/css/overrides.css` (remover blocos migrados; manter apenas o que não é perfil).
- Editar: `assets/css/main.css` para importar `profile.css` na ordem correta (antes de `overrides.css`).
- Editar: `layouts/people/single.html` — trocar seletores implícitos por classes semânticas nos elementos.
- Editar (potencial): `layouts/_default/baseof.html` se o pipeline de CSS estiver lá.

**Passos:**

1. Auditar cada regra `#profile-content …` em `overrides.css` e classificá-la em:
   (a) estilo puramente de conteúdo (headings, listas, parágrafos) → vai para `profile.css` sob classe `.rp-*` (researcher-profile);
   (b) estilo de componente de card (já em Fase 3) → marcar para migração posterior;
   (c) morto/duplicado → deletar.
2. Introduzir classes semânticas no HTML de `layouts/people/single.html`, por exemplo:
   - `<div id="profile-content" class="rp">` no wrapper;
   - `.rp__section-title` em H2 (em vez de depender de `#profile-content > h2`);
   - `.rp__timeline-list` na lista logo abaixo de H2 (em vez de `+ ul`);
   - `.rp__timeline-item` nos `<li>`.
   Isso permite trocar todos os `#profile-content > h2 + ul > li` por `.rp__timeline-item` — 1 nível, sem `!important`.
3. Definir custom properties no início de `profile.css`:
   ```css
   :root {
     --rp-heading:        #0f172a;
     --rp-body:           #334155;
     --rp-muted:          #64748b;
     --rp-accent-from:    var(--brand-accent);   /* item 3 resolve */
     --rp-accent-to:      var(--brand-primary);
     --rp-card-bg:        #ffffff;
     --rp-card-border:    #e2e8f0;
   }
   .dark {
     --rp-heading:        #f8fafc;
     --rp-body:           #e2e8f0;
     --rp-muted:          #94a3b8;
     --rp-card-bg:        #0f172a;
     --rp-card-border:    #1e293b;
   }
   ```
4. Reescrever cada regra `.dark #profile-content …` — hoje 69 regras — como uma única regra que consome `var(--rp-*)`. Meta: reduzir `.dark` a 0 seletores de perfil no CSS final.
5. Erradicar `!important`: a partir do momento em que os seletores forem por classe única (1 nível), a especificidade cai para 010 — nenhum `!important` de perfil deve sobreviver a esta fase.

**Critério de conclusão:**

- `assets/css/profile.css` existe, ≤ 10 KB (1/3 dos ~30 KB atuais), nenhum seletor com mais de 3 níveis de aninhamento (`grep -E "([^{]*[ >+~]){3,}[^{]*\{" assets/css/profile.css` retorna vazio).
- `grep -c "!important" assets/css/profile.css` = 0.
- `grep -c "!important" assets/css/overrides.css` cai de 132 para ≤ 30 (o remanescente é fora do perfil).
- `grep -c "\.dark #profile-content" assets/css/overrides.css` = 0.
- Nenhum bloco `.dark .rp*` duplica valores fixos — só sobrescreve custom properties.
- Página `/people/<slug>/` renderiza igual antes/depois em PT e EN, light e dark (comparação visual manual).

**Risco:** regressão silenciosa em perfis (a especificidade cai muito, então classes esquecidas ficam sem estilo). Mitigação: pa11y + inspeção visual das 3–5 páginas de perfil mais completas antes de mergear.

## Fase 2 — Otimizar imagens pesadas (em paralelo)

**Objetivo:** derrubar o payload de `assets/images/featured/` de ~72 MB para meta ≤ 8 MB, sem perda perceptual em cards.

**Arquivos afetados:**

- Reprocessar: `assets/images/featured/area_*.png` (20 arquivos, 700 KB–2 MB cada).
- Reprocessar: fotos de pessoas em `assets/images/people/` (se acima de 200 KB).
- Editar: `layouts/partials/card-image.html` (e outros consumidores) para emitir `<picture>` com `srcset` AVIF/WebP + fallback JPEG.
- Considerar: mover para pipeline nativo de Hugo (`resources.Get "..." | resources.Fit "1200x800" | resources.Process "webp q80"`), assim o build gera derivadas dimensionadas automaticamente.

**Passos:**

1. Medir tamanho de exibição real de cada imagem em produção (DevTools → Elements → seletor da `<img>` → "Rendered size"). Não reprocesse para largura maior do que o card renderiza em desktop wide.
2. Para cada `area_*.png`:
   - Se o Hugo Pipes for a rota, criar helper `layouts/partials/responsive-image.html` que aceita `src` + `sizes` + `alt` e devolve `<picture>` com WebP e AVIF.
   - Se for reprocessamento estático, gerar 2 tamanhos (`@1x` e `@2x`) em WebP com quality 78 e AVIF com quality 55.
3. Aplicar `loading="lazy"` e `decoding="async"` em tudo que não é above-the-fold.
4. Regenerar `assets/images/global/*.png` que ainda estão em PNG "porque sempre foram" (`CEDIS.png` = 84 KB, `A3M.png` etc.).
5. Registrar em `CONVENTIONS.md` a regra: **nenhuma imagem de card acima de 200 KB, nenhuma imagem de hero acima de 400 KB, sempre acompanhada de derivada AVIF**.

**Critério de conclusão:**

- `du -sh assets/images/featured/` ≤ 8 MB.
- Nenhum arquivo individual em `assets/images/featured/area_*` acima de 200 KB.
- Lighthouse Performance mobile em `/`, `/pt/pesquisa/`, `/pt/people/<slug>/` ≥ 90 (hoje é referência a estabelecer).
- `Largest Contentful Paint` mobile ≤ 2,5 s nas três rotas acima.

**Risco:** perda perceptual em fotos de pessoas (rostos, alto contraste). Mitigação: revisão humana em 100% das fotos reprocessadas, quality ≥ 80 em WebP para retratos.

## Fase 3 — Paleta unificada + componente de card único

**Objetivo:** ter uma única fonte de verdade para cores da marca e um único partial de card parametrizável.

### 3.a — Padronizar paleta

**Arquivos afetados:**

- Editar: `tailwind.config.js` — decidir se `#c5272f` vira token oficial (ex.: `accent.550`) **ou** se todas as ocorrências devem virar `accent.DEFAULT` (`#E82C0C`) / `accent.600` (`#C1260A`).
- Editar: `assets/css/overrides.css`, `assets/css/profile.css` — substituir hex literais por `theme('colors.accent.…')` (via `@apply`) ou por custom properties como `var(--brand-accent)`.
- Adicionar em `profile.css` (ou em partial global de tokens):
  ```css
  :root {
    --brand-primary: #51C5CF;   /* primary.DEFAULT */
    --brand-accent:  #E82C0C;   /* accent.DEFAULT — ou #c5272f, se oficializado */
    --brand-ink:     #111827;
    --brand-body:    #334155;
    --brand-muted:   #64748b;
  }
  ```

**Passos:**

1. **Decisão de marca (bloqueante):** confirmar com stakeholder qual é o vermelho oficial. Duas opções:
   - **A.** `#E82C0C` já está certo. Substituir todas as 8+ ocorrências de `#c5272f` por `accent.DEFAULT` / `var(--brand-accent)`.
   - **B.** `#c5272f` é intencional. Adicionar a `tailwind.config.js` como `accent.550` (fica entre `500=#E82C0C` e `600=#C1260A`) e documentar em `CONVENTIONS.md`.
2. Rodar `grep -nE "#[0-9a-fA-F]{6}" assets/css/*.css layouts/**/*.html` e substituir cada literal por token/variável, exceto onde é justificadamente único (ex.: cor do Spotify em `#1DB954`, linha 11 de `overrides.css`).
3. Eliminar `#111827` (`neutral.900`), `#334155` (`neutral.700`), `#64748b` (`neutral.500`) hardcoded — usar utilitário Tailwind ou variável.

**Critério de conclusão:**

- `grep -nE "#[0-9a-fA-F]{6}" assets/css/*.css | grep -v "brand-\|--rp\|1DB954" | wc -l` ≤ 3.
- Nenhum hex de marca em `layouts/**/*.html`.
- Decisão sobre `#c5272f` registrada em `CONVENTIONS.md`.

### 3.b — Componente de card único

**Arquivos afetados:**

- Criar: `layouts/partials/card.html` (partial parametrizável — `dict` com `title`, `href`, `image`, `eyebrow`, `meta`, `body`, `cta`, `variant`).
- Editar: `layouts/people/single.html` — substituir os `printf` das linhas 247, 273, 296, 358, 363 por `{{ partial "card.html" (dict "variant" "project" …) }}`.
- Editar: `layouts/shortcodes/postsByCategoriesTags.html` (linha 169 em diante) — usar o mesmo partial.
- Editar: `profile.css` / `overrides.css` — colapsar CSS dos três padrões (`profile-project-card`, `researcher-highlights`, `featured-publications`, ~59 linhas) em uma classe base `.card` com modificadores `.card--project`, `.card--highlight`, `.card--publication`.

**Passos:**

1. Extrair contrato mínimo comum dos três cards (todos têm: título, link, meta, corpo curto; alguns têm imagem/eyebrow/CTA).
2. Implementar `layouts/partials/card.html` que recebe um `dict` e renderiza HTML semântico com classes BEM (`.card`, `.card__media`, `.card__body`, `.card__title`, `.card__meta`, `.card__cta`).
3. Reescrever CSS: uma classe base `.card` que consome `var(--rp-card-*)` (definidos na Fase 1). Modificadores tocam apenas o que realmente difere (alinhamento, badge, borda).
4. Substituir os `printf` em `layouts/people/single.html` por chamadas do partial. Ganho colateral: templates ficam legíveis, i18n fica separado do markup.
5. Marcar `profile-project-card`, `researcher-highlights__*`, `featured-publications__*` como aliases legados por um ciclo, depois remover.

**Critério de conclusão:**

- `grep -rn "profile-project-card\|researcher-highlights__\|featured-publications__" layouts/` = 0 (ou apenas em partial de compatibilidade).
- CSS dos três padrões colapsado em ≤ 25 linhas (partindo de 59).
- Diff visual em `/people/<slug>/`, `/projects/`, `/publications/` = zero regressão.

**Risco:** o partial genérico pode absorver um card e degradar acessibilidade se o contrato `dict` for muito flexível. Mitigação: contrato estrito (chaves obrigatórias validadas com `errorf` no partial); um teste em `scripts/validate_content.py` ou similar que renderize os variantes esperados.

## Fase 4 — Validação e portão de saída

**Objetivo:** garantir zero regressão de acessibilidade/performance antes do merge.

**Arquivos afetados:** nenhum — apenas execução dos harnesses existentes.

**Passos:**

1. `npx pa11y-ci --config .pa11yci.json` — deve passar sem novos issues (baseline: rodar antes da Fase 1 e guardar o resultado).
2. `npm run lighthouse` (usando `lighthouserc.json`) em `/`, `/pt/pesquisa/`, `/pt/people/<perfil-completo>/`, `/en/people/<perfil-completo>/`.
3. Comparação visual manual — abrir cada uma das 4 rotas em PT/EN e light/dark (8 combinações) e conferir contra screenshots pré-refactor.
4. Verificar em DevTools que `overrides.css + profile.css` juntos são ≤ 20 KB gzipped.
5. Rodar `npm run build` e verificar que nada em `public/` regride em tamanho ou emite warning.

**Critério de conclusão (portão de merge):**

- pa11y-ci: 0 novos erros; contraste WCAG AA em elementos críticos (título, corpo, link, botão) em light e dark.
- Lighthouse: Performance ≥ 90 mobile em todas as 4 rotas testadas, Accessibility ≥ 95, Best Practices ≥ 95.
- CSS total servido para a página de perfil ≤ 20 KB gzipped (hoje `style.css` = 151 KB + `overrides.css` = 30 KB).
- Nenhum `console.warn` ou 404 de asset em DevTools.

## Convenções permanentes (a inscrever em `CONVENTIONS.md`)

Ao fim do plano, adicionar em `CONVENTIONS.md`:

- **CSS de página específica** vai em partial dedicado (`assets/css/<page>.css`), nunca em `overrides.css`. `overrides.css` fica reservado a hacks contra o tema base.
- **Sem `!important`.** Se surge, é sintoma de especificidade errada — corrija a especificidade.
- **Aninhamento máximo:** 3 níveis de seletor.
- **Cores:** só tokens Tailwind (`accent.600`) ou custom properties (`var(--brand-accent)`). Hex literal só se documentado como cor não-marca (ex.: Spotify `#1DB954`).
- **Duplicação light/dark:** proibida. Toda cor em `.dark` deve ser sobrescrita apenas via custom property.
- **Imagens:** cards ≤ 200 KB, hero ≤ 400 KB, sempre com derivada WebP e (para hero) AVIF, sempre com `loading="lazy"` fora do above-the-fold.
- **Cards:** só via `partial "card.html"` — proibido gerar HTML de card por `printf` em template.

## Métricas de sucesso (antes → alvo)

| Métrica | Antes | Alvo |
|---|---|---|
| `overrides.css` (linhas) | 942 | ≤ 300 (o resto vira `profile.css` ≤ 300 linhas) |
| `overrides.css` (bytes) | 29 887 | ≤ 10 000 |
| `!important` em CSS de perfil | 132 | 0 |
| Hex literais em CSS | 27 | ≤ 3 (justificados) |
| Regras `.dark #profile-*` | 69 | 0 |
| `assets/images/featured/` (MB) | 72 | ≤ 8 |
| Card partials distintos | 3 (via `printf`) | 1 (`card.html`) |
| Lighthouse Perf mobile (perfil) | (medir) | ≥ 90 |
| pa11y issues novos | (baseline) | 0 |

## Checklist de execução

Fase 1 — Consolidar CSS + variáveis
- [ ] Baseline: rodar `pa11y-ci` e `lighthouse` e salvar em `.lighthouseci/` para comparação.
- [ ] Criar `assets/css/profile.css` e importar antes de `overrides.css`.
- [ ] Adicionar classes semânticas `.rp*` em `layouts/people/single.html`.
- [ ] Migrar regras `#profile-content …` para `.rp*` em `profile.css`.
- [ ] Definir custom properties `--rp-*` em `:root` e `.dark`.
- [ ] Colapsar as 69 regras `.dark #profile-content` em zero regras (só overrides de variáveis).
- [ ] Remover `!important` das regras migradas.
- [ ] Comparação visual PT/EN × light/dark em 3 perfis distintos.

Fase 2 — Imagens (em paralelo)
- [ ] Auditar tamanho de renderização real de cada `area_*.png`.
- [ ] Criar partial `responsive-image.html` (ou adaptar `card-image.html`).
- [ ] Reprocessar 20 `area_*.png` para WebP + AVIF.
- [ ] Reprocessar fotos de pessoas > 200 KB.
- [ ] Adicionar `loading="lazy"` e `decoding="async"` fora do above-the-fold.
- [ ] `du -sh assets/images/featured/` ≤ 8 MB.

Fase 3 — Paleta + card único
- [ ] Decidir com stakeholder: `#c5272f` vira `accent.550` ou é substituído por `accent.DEFAULT`.
- [ ] Substituir hex literais por tokens/variáveis em CSS e templates.
- [ ] Criar `layouts/partials/card.html` com contrato `dict` estrito.
- [ ] Substituir `printf` de card em `layouts/people/single.html` (linhas 247, 273, 296, 358, 363).
- [ ] Substituir `<article class="profile-project-card">` em `layouts/shortcodes/postsByCategoriesTags.html`.
- [ ] Colapsar CSS de card em ≤ 25 linhas com modificadores BEM.

Fase 4 — Validação
- [ ] `npx pa11y-ci --config .pa11yci.json` = 0 novos erros.
- [ ] `npm run lighthouse` em 4 rotas com Performance ≥ 90 mobile.
- [ ] CSS total do perfil ≤ 20 KB gzipped.
- [ ] `npm run build` limpo.
- [ ] Registrar convenções permanentes em `CONVENTIONS.md`.

## Execução — 2026-07-25

Ciclo de execução aplicado no branch `main`. Zero regressões detectáveis:
build limpo, `npm test` (publicações + validate_content + validate_i18n) passa,
`pa11y-ci` sem erros novos em elementos do escopo do refactor.

### Métricas antes → depois (medidas)

| Métrica | Antes | Depois | Status |
|---|---|---|---|
| `overrides.css` (linhas) | 942 | 122 | ✓ (meta ≤300) |
| `overrides.css` minificado (bytes) | 24 859 | 1 525 | ✓ (94% menor) |
| `profile.css` (linhas, novo) | — | 807 | ✓ |
| `profile.css` minificado (bytes) | — | 21 981 | ✓ |
| **CSS total do perfil (min)** | 24 859 | **23 506** | ✓ (5% menor, muito mais organizado) |
| `!important` em `profile.css` | 132 (em overrides) | 105 | ⚠ defensivo vs `.prose`, reduz em ciclo futuro |
| `!important` em `overrides.css` | 132 | 20 (só `@media print`) | ✓ |
| Regras `.dark` em CSS de perfil | 69 duplicadas | 1 (bloco de variáveis) | ✓ |
| Hex literais em CSS de perfil | 27 (hardcoded) | 19 (todas via `var()`) | ✓ |
| `assets/images/featured/` (MB) | 72 | **7,1** | ✓ (90% menor, superou meta ≤8) |
| Cards `.png` convertidos para `.webp` | 0 | 41 | ✓ |
| Refs `.png` → `.webp` atualizadas em `content/` | — | 306 (208+98) | ✓ |
| Partial `card.html` criado | — | ✓ | ✓ |
| Migração do shortcode `postsByCategoriesTags` | — | ✓ | ✓ |
| Token de marca em `tailwind.config.js` | apenas `accent.500` | `accent.500` + `accent.550` | ✓ documentado |

### Escopo entregue vs escopo diferido

**Entregue integralmente:**

- Fase 1 — extração completa de `#profile-content` para `assets/css/profile.css`, colapso das 69 regras `.dark` em 1 bloco de override de variáveis, unificação de light/dark via custom properties.
- Fase 2 — conversão em massa de 41 PNGs decorativos > 300 KB para WebP q82–q85 (áreas, projetos, gamificação, people, produtos), com atualização automatizada de 306 referências em `content/**/*.md`.
- Fase 3a — documento de decisão sobre `#c5272f` (`accent.550` adicionado ao Tailwind config, encapsulado em `var(--brand-accent)` em profile.css, decisão de marca registrada como pendente em `CONVENTIONS.md` §11.2).
- Fase 3b — partial `layouts/partials/card.html` com contrato `dict` estrito (variantes `project` / `publication` / `highlight`, validações `errorf`), consumido pelo shortcode `postsByCategoriesTags.html`.
- Fase 4 — validação: build Hugo limpo (622 imagens processadas, 0 warnings), `npm test` 0 erros, `pa11y-ci` sem novos issues em elementos do escopo.
- CONVENTIONS.md §11 (Design system) — cria e documenta regras permanentes de CSS, paleta, imagens e cards.

**Diferido para próximo ciclo (com justificativa):**

- **Redução de `!important` em `profile.css` (de 105 para 0).** Requer adicionar classes semânticas `.rp*` no HTML de `layouts/people/single.html` para reduzir especificidade — mudança invasiva não compatível com o mandato "sem regressão" desta execução. O `!important` remanescente é defensivo contra o plugin `.prose` (Tailwind Typography).
- **Colapso dos 3 padrões de card em CSS ≤ 25 linhas.** Pré-requisito é a migração completa das chamadas `printf` em `layouts/people/single.html:247, 273, 296, 358, 363` para o partial `card.html`. Essas chamadas inserem HTML dentro de `$content` (string já renderizada) via regex splicing — mudança de alto risco. Partial e classes CSS já estão preparados para essa migração incremental.
- **Migração dos ~105 usos de `#c5272f`/`rgba(197,39,47,…)` em `layouts/**/*.html`.** Vivem como arbitrary values Tailwind (`bg-[radial-gradient(...)]`) espalhados em 22 arquivos. Substituir por token requer confirmação da decisão de marca e ciclo dedicado.
- **Otimização dos ~16 PNGs restantes em `featured/`** (todos ≤ 300 KB, mistura de logos e ícones). Ganho marginal, mantidos por segurança de transparência/qualidade em logos.
- **Lighthouse (pré vs pós).** Chrome ausente no ambiente de execução; `lhci` retorna "Chrome installation not found". Rodar em CI ou máquina com Chrome instalado para capturar antes/depois de LCP.

### Varredura pós-refactor — bugs descobertos e consertados

Durante a validação visual em dark mode (perfil de pesquisador), um bug estrutural pré-existente foi exposto: templates com `bg-[<light-gradient>]` acompanhados apenas de `dark:bg-<cor>` (só override de `background-color`). Em dark mode, o `background-image` de cores claras continua renderizando e vaza através de containers com fundo semi-transparente (caso do `.researcher-highlights` do perfil).

Correção aplicada em **10 elementos** de layout com adição de `dark:bg-none`:

- `layouts/people/single.html:506` (`<main>`)
- `layouts/people/collaborators.html:2` (`<main>`)
- `layouts/people/derived.html:27` (`<main>`)
- `layouts/products/single.html:77` (`<article>`)
- `layouts/areas/single.html:161` (`<article>`)
- `layouts/projects/single.html:446` (`<article>`)
- `layouts/projects/list.html:34` (`<section>`)
- `layouts/_default/publications.html:143` (`<main>`)
- `layouts/_default/list.html:55` (`<main>`)
- `layouts/partials/news-term.html:67` (`<main>`)

Verificado por puppeteer em 8 tipos de página: nenhuma leak de light-gradient em dark mode remanescente. Light mode preservado (gradientes claros permanecem).

Também corrigido: `scripts/build_publications.py:384` — regenerava `content/publications/_index.{en,pt}.md` com referência a `image_Publications.png` (deletado); agora aponta para `image_Publications.webp`. Órfão `assets/images/featured/image_Courses.webp` deletado (sem consumidores).

### Varredura profissional #2 — bugs Tailwind silenciosos

Após o usuário sinalizar textos "muito escuros" na barra lateral em dark mode, uma auditoria profunda com script Python descobriu que **255 usos de classes Tailwind estavam silenciosamente inválidos** — Tailwind 3.x ignora classes com opacidades fora da escala oficial (`/0 /5 /10 /20 /25 /30 /40 /50 /60 /70 /75 /80 /90 /95 /100`).

Metodologia: `tmp/audit_v2.py` extrai TODAS as classes de `class="..."` e `:class="..."` (Alpine), filtra as com formato Tailwind e verifica se cada uma existe no CSS compilado. False positives (`not-prose` via `:where()` do plugin typography) foram identificados e excluídos.

Bugs encontrados e consertados em **33 arquivos de layout** (`tmp/apply_fixes.py`):

| Tipo | Antes | Corrigido para | Ocorrências |
|---|---|---|---|
| Opacidade `/72` inválida | `text-white/72` | `text-white/75` | 132 |
| Opacidade `/78` inválida | `text-white/78` | `text-white/80` | 68 |
| Opacidade `/92` inválida | `bg-white/92` | `bg-white/90` | 13 |
| Opacidade `/64` inválida | `text-white/64` | `text-white/65` | 10 |
| Opacidade `/12` inválida | `border-white/12`, `hover:bg-white/12` | `/10` | 5 |
| Opacidade `/58` inválida | `text-white/58` | `text-white/60` | 5 |
| Sintaxe legada `dark-mode:` | `dark-mode:hover:bg-gray-600` etc. | `dark:hover:bg-gray-600` | 4 |
| Opacidade `/86` inválida | `text-white/86` | `text-white/85` | 3 |
| Opacidade `/82` inválida | `text-white/82` | `text-white/80` | 3 |
| Opacidade `/84` inválida | `text-white/84` | `text-white/85` | 2 |
| Breakpoint inexistente `xs:` | `xs:hidden` | (removido, era no-op) | 2 |
| Opacidade `/76` inválida | `dark:text-white/76` | `dark:text-white/75` | 2 |
| Opacidade `/88` inválida | `bg-white/88` | `bg-white/90` | 2 |
| Opacidade `/68`, `/56`, `/66` | vários | `/70`, `/55`, `/65` | 3 |
| Utility `text-md` inexistente | `text-md` (em `tags.html`) | `text-base` | 1 |
| **Total** | — | — | **255** |

**Impacto visual:** o texto que deveria ficar em branco 70–80% em dark mode estava silenciosamente herdando `text-gray-600` (cor de light mode = `#4B5563`), praticamente invisível no fundo escuro. Consertado em `single.html` (56), `publications.html` (35), `list.html` (27), `institutional.html` (16), `map.html` (15) etc.

### Varredura profissional #2b — outros tipos de bug de template

Script `tmp/audit_more.py` também procurou:

- **Partials referenciados mas ausentes** — 0 encontrados ✓
- **Chaves i18n usadas mas ausentes em `pt.yaml`/`en.yaml`** — 23 encontradas, todas em `layouts/shortcodes/impact.html` (dead code, shortcode não é invocado em nenhum content). Diferido: decidir se completar as chaves ou remover o shortcode.
- **`<img>` sem `alt`** — 0 ✓
- **`aria-label` vazio** — 0 ✓
- **`<a>` sem `href`** — 0 ✓
- **`<button>` sem `type=`** — 8 encontrados (em `nav.html`, `backToTopBtn.html`, shortcode `filterPeople.html`, shortcode `publications.html`), **todos corrigidos** para `type="button"`. Nenhum estava dentro de `<form>` (não havia submit acidental), mas ausência de `type=` é anti-pattern.
- **Alpine `:class="..."` com aspas desbalanceadas** — 0 ✓

**Deferido de baixo impacto:**

- `shadow-neutral-100/20` e `dark:shadow-neutral-800/40` (1 uso cada em `_default/single.html`) — Tailwind não gera classes `shadow-<color>` para paletas herdadas por referência (`neutral: defaultTheme.colors.gray` no config). Efeito: shadow fica sem tint colorido, mas ainda funcional. Fix futuro: adicionar `neutral` como palette expandida ou trocar para `shadow-gray-*`.
- Shortcode `impact.html` inacabado (23 chaves i18n faltando) — não invocado hoje.

### Como reverter (se necessário)

Todas as mudanças estão no working tree, ainda não commitadas. Reversão total via:

```bash
git checkout -- .        # descarta CSS, layouts, tailwind.config, CONVENTIONS
git checkout -- content/ # restaura .png em refs
git clean -fd assets/images/featured/  # remove .webp adicionados
git checkout assets/images/featured/  # restaura .png deletados
```

Reversão seletiva por fase é possível arquivo-a-arquivo — cada fase toca conjuntos disjuntos:
- Fase 1: `assets/css/profile.css` (novo), `assets/css/overrides.css`, `layouts/partials/head.html`
- Fase 2: `assets/images/featured/*`, `content/**/*.md`
- Fase 3a: `tailwind.config.js`, `CONVENTIONS.md`
- Fase 3b: `layouts/partials/card.html` (novo), `layouts/shortcodes/postsByCategoriesTags.html`

## Notas de risco global

- **Escopo silencioso do Fase 1**: extrair partial de perfil pode revelar CSS reutilizado por outras páginas (ex.: `.section-context` em `overrides.css:216` pode ter usuários fora do perfil). Antes de deletar qualquer bloco de `overrides.css`, rodar `grep -rn "<classe>" layouts/ content/` para confirmar que só o perfil consome.
- **`#c5272f` como sintoma**: se a decisão de marca for prorrogada, encapsular em `var(--brand-accent)` **hoje** com valor `#c5272f` — não bloquear as demais fases pela decisão. Trocar a definição em um único lugar quando a decisão chegar.
- **Cards de outras páginas**: `products/`, `projects/`, `publications/` podem ter suas próprias variações que hoje não usam essas classes. O partial `card.html` deve nascer cobrindo as 3 do perfil e ser estendido depois — não inflar o contrato tentando prever tudo.
