# Plano de aproveitamento — Tailwind CSS 4 no site CEDIS

**Data-base:** 2026-07-27
**Estado:** proposto (execução pendente de autorização por fase)
**Contexto:** migração para Tailwind 4 concluída (commit `91e849f30`, produção ativa). Este plano trata do próximo passo — **usar recursos que a v4 trouxe que não existiam na v3.4**.

## Sumário executivo

A migração pura (Fases 1-15 anteriores) trocou o pipeline mantendo o mesmo conjunto de utilities. O ganho arquitetural veio de dependências reduzidas e um único `<link>`. O ganho **visual/UX** só aparece quando adotarmos recursos novos.

Após varredura concreta do repositório, dos 15 recursos citados como candidatos, **7 têm aplicação real imediata**, **3 têm aplicação média** e **5 têm aplicação nula ou muito marginal**.

**Recomendação:** executar Fase 1 (impacto alto, esforço ≤ 4h). Considerar Fase 2 (média-alta, ~8h). Fases 3-4 dependem de decisão sobre modernização visual maior.

## Recursos avaliados — matriz de aplicabilidade concreta

| # | Recurso | Aplicabilidade CEDIS | Evidência concreta no repo |
|---|---|---|---|
| 1 | Consultas de contêiner (`@container` + `@md:`) | **Alta** | 3 shortcodes reutilizados em `content/areas/*.md` (15+ páginas) dentro de contexts de largura diferente: `publications.html`, `postsByCategoriesTags.html`, `posts-template.html`. Grids `md:grid-cols-*`/`lg:grid-cols-*` em 6 templates. |
| 2 | Variantes `pointer-coarse`/`pointer-fine` | **Alta** | 153 botões `rounded-full` com padding fixo em vários templates. Padding uniforme entre mouse (`px-3 py-1`) e touch — em mobile ficam pequenos para touch targets WCAG (44×44 mínimo). |
| 3 | `wrap-anywhere` + `wrap-break-word` | **Alta parcial** | Já usado em `publications/single.html:60` (DOI/ISBN). NÃO aplicado a 5+ outros pontos: ORCID (`people/single.html:692`), email do perfil (`:672`), Lattes (`:686`), nomes derivados (`derivedPeople.html:34`). Todos usam `truncate` que corta silenciosamente. |
| 4 | Variáveis CSS de tema (`@theme` + tokens OKLCH) | **Alta** (manutenção) | 31 hex únicos em `tailwind.config.js`, 14 escalas de cor. Config JS legado carregado via `@config`. Migrar para `@theme` em CSS elimina uma indireção e permite consumir tokens em CSS custom (ex.: em profile.css já usamos `var(--brand-*)` mas os valores não são atualmente vinculados aos tokens Tailwind). |
| 5 | `color-scheme` (`scheme-light dark:scheme-dark`) | **Média-alta** | Site tem light/dark toggle. Barra de rolagem, campos nativos e controles de sistema NÃO acompanham — permanecem estilo OS default (branco em Firefox/Chrome mesmo com fundo escuro). 1 elemento `<html class="dark">` em `head.html:65`. |
| 6 | Utilities de scrollbar (`scrollbar-gutter-stable`) | **Média** | `scrollbar-gutter: stable` já usado 1× em `profile.css:664` como CSS puro (várias seções do perfil). Trocar por utility Tailwind no HTML elimina a regra CSS mas mesmo efeito. 3 elementos com `overflow-y-auto` em templates. |
| 7 | `field-sizing-content` | **Nula** | Zero `<textarea>` no site. Nenhum formulário local ativo. |
| 8 | `starting:` + `<div popover>` nativo | **Baixa-média** | 8 toggles Alpine funcionam bem hoje (`x-data="{ open: false }"`). Migração possível mas não urgente — Alpine popover paths estáveis, popover nativo ainda precisa fallback em Safari <17. |
| 9 | `@source` e detecção de fontes | **Já configurado** | Nossa `main.css` já tem `@source "hugo_stats.json"` + `@source "../../layouts"` (safety net). Não há trabalho adicional. |
| 10 | Valores dinâmicos ampliados (`grid-cols-15`, `w-17`) | **Baixa** | Não há uso atual de custom grid-cols numéricos incomuns. Nada a fazer. |
| 11 | Data-attribute variants (`data-current:font-bold`) | **Baixa-média** | Menu ativo é hoje detectado por Hugo template (`{{ if eq .Permalink ... }}`). Alpine também cuida. Migração possível mas invasiva sem ganho claro. |
| 12 | Paleta OKLCH e P3 | **Média** (se Fase 4 for adotada) | Depende da decisão do #4. OKLCH torna gradientes mais consistentes e libera P3, mas exige tests de contraste em cada token. |
| 13 | Gradientes radiais/cônicos | **Baixa** | Já usamos gradientes lineares e radiais via arbitrary values (`bg-[radial-gradient(...)]`). Ganho seria simplificação sintática, não capacidade nova. |
| 14 | Máscaras de imagem (`mask-*`) | **Baixa** | Fotografias de pesquisadores são retratos limpos que não precisam de fade. Cards de projeto usam WebP direto. |
| 15 | Sombras de texto | **Nula** | Site institucional não usa texto sobre imagens de fundo. Aplicaria só em hero da home, e o hero já tem tratamento sólido. |

## Fase 1 — Ganhos rápidos (impacto alto, esforço ≤ 4h)

Objetivo: eliminar quebras de layout comuns em mobile e melhorar controles nativos, sem tocar componentes complexos.

### 1.1 — `wrap-anywhere` para identificadores e URLs longos

**Arquivos afetados:**

- `layouts/people/single.html:672` — email do perfil
- `layouts/people/single.html:686` — link Lattes
- `layouts/people/single.html:692` — link ORCID
- `layouts/shortcodes/derivedPeople.html:34` — nomes derivados

**Mudança:** substituir `truncate` por `wrap-anywhere` em elementos onde cortar o texto perde informação (email, ORCID, DOI). Manter `truncate` onde a truncagem é intencional (títulos de card com resumo abaixo).

**Critério de conclusão:** DOI, ORCID, emails e Lattes URLs quebram corretamente em `width < 320px` sem overflow horizontal na página.

**Reversão:** trivial (`git checkout` dos arquivos).

### 1.2 — `scheme-light` / `dark:scheme-dark` em `<html>`

**Arquivo afetado:** `layouts/partials/head.html:64-68` (bloco `<script>` que aplica `.dark`)

**Mudança:** adicionar `scheme-light dark:scheme-dark` como classe inicial no `<html>` (via template Hugo, não via JS) OU incluir no bloco JS que aplica `.dark`.

Após aplicar:
- Scrollbar em light mode = clara; em dark mode = escura (nativo)
- Campos de busca Pagefind respeitam tema
- Menus dropdown nativos (se surgirem no futuro) acompanham

**Critério de conclusão:** rolagem visível em dark mode passa a ter cor escura em Chrome/Safari/Firefox.

**Reversão:** trivial.

### 1.3 — Substituir `scrollbar-gutter: stable` do CSS por utility Tailwind

**Arquivo afetado:** `assets/css/profile.css:663-664` — regra CSS custom pode ser eliminada em favor de utility no HTML.

Não é mudança visual, é limpeza. Remover 1 regra de `profile.css`, adicionar `scrollbar-gutter-stable` nas classes dos containers no HTML template.

**Critério de conclusão:** `profile.css` perde 1 regra; comportamento visual idêntico.

**Reversão:** trivial.

### 1.4 — Touch targets: `pointer-coarse:` em botões críticos

Aplicar seletivamente onde o botão é usado principalmente por dedo (menu mobile, filtros, botões de ação).

**Arquivos-alvo (prioridade):**

- `layouts/partials/nav.html` — toggle menu móvel (linha 148, botões `xs:hidden` removidos anteriormente)
- `layouts/_default/map.html:106-128` — botões de filtro do mapa (all/area/researcher/project/umbrella)
- `layouts/partials/language-switcher.html:7` — seletor PT/EN
- `layouts/shortcodes/filterPeople.html:296` — filtro de pessoas
- `layouts/shortcodes/backToTopBtn.html:2` — volta ao topo

**Mudança:** adicionar `pointer-coarse:px-5 pointer-coarse:py-3` (ou similar) em botões com padding atual `px-3 py-1` / `px-4 py-2`. Target: mínimo 44×44 CSS pixels em touch.

**Critério de conclusão:** botões dessa lista atingem 44×44 mínimo em viewport mobile (medir com DevTools).

**Escopo total Fase 1:** ~4h de dev + 30 min de validação (screenshots mobile + Lighthouse a11y).

## Fase 2 — Container queries em componentes reutilizados (impacto alto, esforço ~8h)

Objetivo: um mesmo shortcode/template renderiza corretamente em contextos de largura variável — sem precisar duplicar variantes ou recorrer a arbitrary media queries.

### 2.1 — Shortcode `publications.html`

**Arquivo afetado:** `layouts/shortcodes/publications.html`

Hoje esse shortcode é chamado em `content/areas/*.md` (15+ páginas). Cada página de área tem um `<article>` com largura contextual (às vezes com sidebar, às vezes sem). O grid interno é `md:grid-cols-2 lg:grid-cols-3` — decisão baseada no viewport, não no espaço disponível.

**Mudança:**

```html
<div class="@container">
  <div class="grid grid-cols-1 @md:grid-cols-2 @xl:grid-cols-3 gap-4">
    <!-- items -->
  </div>
</div>
```

**Critério de conclusão:** renderizar shortcode em largura 400px, 800px e 1200px produz layouts adequados sem overflow ou classes redundantes.

### 2.2 — `postsByCategoriesTags.html`

**Arquivo afetado:** `layouts/shortcodes/postsByCategoriesTags.html`

Mesmo padrão — invocado em 6+ páginas de área para listar projetos.

### 2.3 — `posts-template.html` e `products-catalog.html`

Grids `md:grid-cols-2 xl:grid-cols-3` que poderiam ser `@md:grid-cols-2 @xl:grid-cols-3`.

**Critério de conclusão Fase 2:** substituir 3 shortcodes/partials para container queries. Confirmar em screenshots que layout permanece correto quando renderizados em diferentes larguras (main, sidebar hipotética, embed em modal).

**Trade-off:** perde-se apoio de Safari <16.4 para container queries. Já é o requisito v4 (mesma versão).

## Fase 3 — Migração para CSS-first (`@theme` + tokens OKLCH)

**Requisito bloqueante:** stakeholder aprovar mudança de cores (OKLCH pode reproduzir hex diferente, especialmente em telas P3).

### 3.1 — Migrar `tailwind.config.js` para `@theme` em `main.css`

**Arquivos afetados:**

- `assets/css/main.css` — adicionar bloco `@theme { --color-primary-50: oklch(...); ... }`
- `tailwind.config.js` — deletar (ou manter só como referência para `@tailwindcss/typography` config, se necessário)
- Remover `@config "./tailwind.config.js"` do `main.css`

Tokens que precisam ser preservados:
- `primary.DEFAULT` = `#51C5CF` + escala 50-900
- `secondary.DEFAULT` = `#F7941E` + escala 50-900
- `accent.DEFAULT` = `#E82C0C` + escala 50-900 + `accent.550` = `#C5272F`
- `neutral` = `defaultTheme.colors.gray` (poderia herdar do default v4)
- Custom typography theme (todos os `--tw-prose-*`)
- Custom animations (`marquee`, `bounce`, `pulse`)

**Ganho:**
- Uma indireção a menos (Hugo → main.css, sem passar por config JS)
- Tokens acessíveis via `var(--color-primary-500)` de qualquer CSS custom (hoje profile.css tem `var(--brand-primary)` DESVINCULADO do Tailwind — poderiam ser o mesmo valor)
- CSS gerado ligeiramente menor (não gera utilities para tokens não usados)

**Risco:** OKLCH vs sRGB. Cor visualmente idêntica em telas sRGB comuns, mas ligeiramente diferente em telas P3 (MacBook, iPhone recente). Precisa validação visual em ≥ 1 dispositivo P3 e 1 sRGB.

**Escopo estimado:** 6-10h + validação.

### 3.2 — Unificar tokens de `profile.css` (`--rp-*` e `--brand-*`) com tokens Tailwind

`profile.css` hoje declara suas próprias custom properties (`--brand-accent: #c5272f;` etc.) que **não estão vinculadas** aos tokens `accent-550` do Tailwind config. Duas fontes de verdade.

Após 3.1, essas variáveis podem ser expressas como `var(--color-accent-550)` — fonte única.

## Fase 4 — Alpine popover → HTML `popover` nativo + `starting:` (adiar)

**Recomendação: não fazer agora.**

Alpine funciona bem, Popover API tem 90%+ suporte mas Safari 17 é o mínimo (temos requisito Safari 16.4+ do v4, então há gap). Migração seria evolução incremental por componente:

- Menu de idioma (`language-switcher.html`)
- Dropdown de menu (`nav.html`)
- Sub-menus complexos

Cada um precisa fallback para Alpine em Safari 16.4. Custo/benefício ruim hoje.

Registrar como possível refactor de 2027+.

## Recursos rejeitados neste plano

| Recurso | Motivo |
|---|---|
| `field-sizing-content` | Zero textareas no site |
| Gradientes radiais/cônicos utilities | Já usamos via arbitrary values, ganho seria só sintático |
| Máscaras de imagem | Fotos de pesquisadores são retratos; não há uso institucional para fades |
| `text-shadow-*` | Site institucional não tem texto sobre imagens de fundo |
| `data-*:` variants | Menu ativo já resolvido por Hugo + Alpine |
| Transformações 3D | Sem uso institucional |
| Valores numéricos dinâmicos (grid-cols-15, w-17) | Nenhum uso atual precisa |
| Detecção `@source` melhorada | Já configurada corretamente na migração |

## Métricas antes → alvo por fase

| Fase | Métrica | Antes | Alvo |
|---|---|---|---|
| 1.1 | DOI/ORCID que quebram em 320px sem overflow | ~50% | 100% |
| 1.2 | Elementos nativos com tema respeitado (dark) | scroll: não | scroll + campos: sim |
| 1.3 | Regras `scrollbar-gutter` em `profile.css` | 1 | 0 (utility) |
| 1.4 | Touch targets ≥ 44px em botões críticos | ~30% (medido em mobile) | 100% em 5 componentes-alvo |
| 2 | Shortcodes com container queries | 0 | 3 |
| 3.1 | `tailwind.config.js` | 121 linhas | 0 (`@theme` em CSS) |
| 3.2 | Duplicidade de tokens `--brand-*` vs Tailwind | 2 fontes | 1 fonte |

## Riscos globais

| # | Risco | Mitigação |
|---|---|---|
| A | Container query cria layout diferente em Chrome/Firefox pré-105 (raro hoje) | Requisito v4 já exclui esses navegadores; sem novo risco |
| B | `wrap-anywhere` quebra visualmente onde antes truncava | Aplicar seletivamente em elementos de identificador (não em títulos) |
| C | OKLCH renderiza cor ligeiramente diferente em P3 vs sRGB | Fase 3 exige validação em ambos os tipos de tela |
| D | `pointer-coarse:` aplicado errado aumenta botão em desktop touch (raro) | Testar em laptop com tela touchscreen |
| E | Alpine popover → HTML popover perde interatividade em Safari 16.4 | Fase 4 fica adiada; sem risco imediato |

## Ordem sugerida de autorização

1. **Fase 1 completa** (1.1 + 1.2 + 1.3 + 1.4) — 4h — impacto imediato em mobile
2. Aguardar 2-3 dias de estabilidade em produção
3. **Fase 2** (container queries em 3 shortcodes) — 8h — melhora reutilização de componentes em áreas
4. Aguardar mais 1 semana
5. **Fase 3** só se stakeholder aprovar migração de paleta para OKLCH — 8h — arquitetural, não visual
6. **Fase 4** deferida indefinidamente

Nenhuma dessas fases é bloqueante para a estabilidade da migração v4 já concluída. Todas são melhorias incrementais.
