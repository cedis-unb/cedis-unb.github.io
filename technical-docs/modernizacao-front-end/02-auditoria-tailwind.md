# 02 — Auditoria Tailwind

Análise profunda do uso atual de Tailwind CSS 3.4.19 no repositório e do que precisará mudar para Tailwind CSS 4.

## Configuração atual

**Arquivo:** `tailwind.config.js` (121 linhas)

```js
module.exports = {
  content: ['./layouts/**/*.html', './content/**/*.md'],
  darkMode: 'class',
  theme: {
    extend: {
      animation: {
        'pulse-slow': 'pulse 3s infinite',
        'bounce-slow': 'bounce 2s infinite',
        'marquee':     'marquee 45s linear infinite',
      },
      keyframes: { /* pulse, bounce, marquee */ },
      colors: {
        primary:   { DEFAULT: '#51C5CF', 50..900 },
        secondary: { DEFAULT: '#F7941E', 50..900 },
        accent:    { DEFAULT: '#E82C0C', 50..900, 550: '#C5272F' },
        neutral:   defaultTheme.colors.gray,   // referência simbólica
      },
      lineHeight: { 'extra-loose': '2.5', '12': '3rem' },
      typography: (theme) => ({ /* customização completa de --tw-prose-* */ }),
    },
  },
  variants: {
    extend: { typography: ['dark'] },
  },
  plugins: [require('@tailwindcss/typography')],
};
```

- `content:` inclui apenas layouts e content Markdown — **não inclui `data/*.yaml` nem `hugo.yaml`** (confirmado seguro: 0 classes Tailwind nesses arquivos).
- `safelist:` **não existe** (nenhuma classe é forçada a existir independente do scan).
- `darkMode: 'class'` — controle via classe `.dark` no `<html>` (via `layouts/partials/head.html:60-68`).
- `plugins:` apenas `@tailwindcss/typography`.
- `neutral: defaultTheme.colors.gray` — referência simbólica. Efeito colateral: `shadow-neutral-*` e `bg-neutral-*` **não geram utilities** (2 usos observados em `layouts/_default/single.html:24`, silenciosamente ignorados hoje).

## Uso de classes Tailwind — inventário

Dados extraídos via `tmp/audit_v2.py` (extrai de `class="..."` e `:class="..."` Alpine).

- **Total de tokens de classe únicos em templates:** 1212
- **Formato Tailwind-válidos (após correções de 2026-07-25):** ~1133
- **Silenciosamente inválidos remanescentes:** 3 (`not-prose` false positive; `shadow-neutral-100/20`, `dark:shadow-neutral-800/40` — não compilam mas efeito é benigno)

### Uso do plugin typography

Grep em `layouts/`:

| Modificador | Ocorrências |
|---|---|
| `prose-a` | 28 |
| `prose-h*` | 24 |
| `prose` (base) | 19 |
| `prose-headings` | 16 |
| `prose-invert` | 9 |
| `prose-zinc` | 8 |
| `prose-strong` | 6 |
| `prose-p` | 6 |
| `prose-li` | 4 |
| `not-prose` | 9 |

**Total: 129 usos.** Plugin `@tailwindcss/typography` é **essencial** para páginas Markdown longas (publicações, notícias, projetos, perfis). **Manter.** Compatível com Tailwind 4 conforme documentação oficial.

### `@apply`, `@layer`, `@screen`, `@variants`

Grep em `assets/css/*.css`: **0 ocorrências** de qualquer um.

**Consequência:** migração v4 dispensa a etapa de reescrita de `@layer` → `@utility`.

### `theme()` function em CSS

Grep em `assets/css/*.css`: **0 ocorrências** de `theme(`.

`theme()` é usado apenas em contexto JavaScript dentro de `tailwind.config.js:79-108` (typography plugin config). Isso é suportado nativamente em v4.

### `@source` / `@config`

**Ainda não usados** (arquitetura v3 tradicional). Serão necessários em v4 se optar por CSS-first config.

### Breakpoints customizados

`tailwind.config.js` **não define `theme.screens`**. Usa apenas defaults: `sm`, `md`, `lg`, `xl`, `2xl`.

Classes com breakpoint encontradas: `sm:`, `md:`, `lg:`, `xl:`, `2xl:` (todos padrão). Zero customizações.

## Classes incompatíveis com Tailwind 4 — inventário

### Categoria A — removidas em v4 (precisam substituição direta)

| Utility removida em v4 | Substituição | Ocorrências | Arquivos |
|---|---|---|---|
| `text-opacity-40` | `text-primary-600/40` | 2 | `layouts/index.html:737,738` (SVG decorativo do hero da home) |
| `flex-shrink-0` | `shrink-0` | 25 | `index.html` (10), `publications/list.html`, `_default/list.html`, `_default/history.html`, `people/single.html`, `_default/quiz.html`, `partials/opportunity-card.html`, `_default/partners.html` |
| `overflow-ellipsis` | `text-ellipsis` | **0** | — |
| `decoration-slice`, `decoration-clone` | `box-decoration-*` | **0** | — |
| `flex-grow-*` | `grow-*` | **0** | — |
| `bg-opacity-*`, `border-opacity-*`, `divide-opacity-*`, `ring-opacity-*`, `placeholder-opacity-*` | `<color>/<opacity>` | **0** | — |

**Total: 27 ocorrências reais a migrar** (2 opacity + 25 shrink).

### Categoria B — renames automáticos (mesma sintaxe, tamanho diferente)

Tailwind v4 renomeou o "shift" das escalas de shadow/blur/rounded. `npx @tailwindcss/upgrade` faz automaticamente. Se não corrigirmos, elementos ficam maiores (mais sombra/blur/radius).

| Utility v3 | Utility v4 (equivalente ao v3) | Ocorrências | Impacto se não migrar |
|---|---|---|---|
| `shadow-sm` (v3 = 2px) | `shadow-xs` (v4 = 2px) | **81** | Elementos ganham sombra maior (v4 `shadow-sm` = 4px) |
| `shadow` (v3 = 4px) | `shadow-sm` (v4 = 4px) | requer grep — provavelmente <20 | Elementos ganham sombra maior |
| `rounded-sm` (v3 = 2px) | `rounded-xs` (v4 = 2px) | não medido — grep antes de migrar | Cantos mais arredondados que o pretendido |
| `rounded` (v3 = 4px) | `rounded-sm` (v4 = 4px) | não medido | Idem |
| `blur-sm` (v3 = 4px) | `blur-xs` (v4 = 4px) | não medido | Blur mais forte |
| `blur` (v3 = 8px) | `blur-sm` (v4 = 8px) | não medido | Blur mais forte |
| `drop-shadow-sm` | `drop-shadow-xs` | não medido | Sombra maior |
| `ring` (v3 = 3px) | `ring-3` (v4 = 3px) | 2 (grep `\bring\b` sem número) | Ring com espessura reduzida (v4 `ring` = 1px) |

**81 ocorrências de `shadow-sm` são a maior superfície de rename.** `npx @tailwindcss/upgrade` lida com isso automaticamente — verificação manual necessária para confirmar aplicação.

### Categoria C — comportamento inalterado mas atenção

| Mudança de comportamento | Impacto no CEDIS |
|---|---|
| Border color default = `currentColor` (v3 era `gray-200`) | 20+ usos de `border` sem cor explícita em templates — verificar visualmente após migrar |
| Placeholder color = 50% da cor do texto (v3 era `gray-400`) | Poucos inputs no site (busca do pagefind é o principal) — baixo impacto |
| `hover:` só ativa em dispositivos com hover (`@media (hover: hover)`) | Toque em mobile já não deveria acionar hover; comportamento mais correto — baixo risco |
| `transition`/`transition-colors` inclui `outline-color` | Neutro |
| `outline-none` removido em favor de `outline-hidden` | Verificar `focus:outline-none` (nav.html usa em botões) |
| Espaçamento `space-y-*` mudou seletor internamente | 0 ocorrências detectadas — pode existir; grep antes de migrar |
| Variant stacking mudou: `first:*:pt-0` → `*:first:pt-0` | Não observado no repo, mas grep antes |

## Classes dinâmicas — inventário detalhado

### Padrão A — `printf` em templates Hugo

**72+ ocorrências.** Concentradas em `layouts/people/single.html` (18 instâncias entre linhas 145-394).

Exemplos (linhas exatas):

- `layouts/people/single.html:145` — badge com `ml-2 inline-flex items-center rounded-full border border-primary-200 bg-primary-50 px-2.5 py-1 text-sm font-black text-primary-700 dark:border-primary-400/25 dark:bg-primary-500/10 dark:text-primary-100`
- `layouts/people/single.html:276` — bloco de projetos anteriores completo (h2 + span badge + svg + wrapper)
- `layouts/people/single.html:299` — bloco de projetos atuais similar
- `layouts/people/single.html:316` — li de produto com 15+ classes
- `layouts/people/single.html:390` — li de publicação com 12+ classes
- `layouts/areas/single.html:273` — card breakdown de estudante
- 5 outras em `_default/history.html`, `_default/quiz.html`, `_default/map.html`, `layouts/index.html`

**Como Tailwind detecta:** o scan lê o arquivo HTML/JS/CSS como texto e captura todo token que pareça classe Tailwind. Strings dentro de `printf` são apenas texto no HTML fonte — o scanner as vê. **Tanto v3 quanto v4 detectam corretamente**, desde que o arquivo esteja em `content` (v3) ou `@source` (v4).

**Risco em v4:** nenhum se `@source` incluir `layouts/**/*.html`. Se migrarmos para CSS-first config, precisamos incluir explicitamente.

### Padrão B — hash MD5 em nome de classe

- `layouts/shortcodes/imgc.html:89` — `<div class="relative imgB-{{ $imgBd5 }} bg-center">`

`imgB-<md5>` **não é uma classe Tailwind**. É um nome custom usado como âncora CSS para regras injetadas pelo próprio shortcode (verificação: linhas anteriores do shortcode geram um `<style>` com `.imgB-<hash> { background-image: url(...) }`). Não afeta migração Tailwind — é CSS puro custom.

### Padrão C — Alpine `:class="..."` dinâmico

**23 ocorrências.** Todas usam strings literais de classes (não construção com concat), então o scanner Tailwind detecta.

Exemplos:
- `layouts/index.html:657` — `:class="current === {{ $index }} ? 'w-8 bg-primary-500 dark:bg-primary-400' : 'w-2 bg-slate-300 hover:bg-slate-400 dark:bg-white/20 dark:hover:bg-white/30'"`
- `layouts/_default/history.html:120` — condicional entre 2 conjuntos de classes literais
- `layouts/_default/map.html:107-125` — 5 condicionais similares (filter buttons)
- `layouts/_default/quiz.html:63` — condicional quiz answer

Todas seguras porque as strings dentro das aspas literais estão diretamente no arquivo `.html`.

### Padrão D — classes em `data/*.yaml`, `hugo.yaml`, `i18n/*.yaml`

**0 ocorrências.** Confirmado por Explore agent scan em todos os 4 data files + hugo.yaml + i18n. Content de YAML é textual (descrições, nomes), não CSS.

## Modo escuro

- Estratégia: `darkMode: 'class'` (v3) — classe `.dark` no `<html>` controlada por JS inline em `head.html:60-68`.
- **Em v4 a config `darkMode: 'class'` deu lugar a variantes:** `@custom-variant dark (&:where(.dark, .dark *))` em CSS-first, ou continua funcionando via `@config` fallback.
- 105 regras `!important` em `profile.css` (defensivas contra `.prose`) e 20 `!important` em `overrides.css` (média print) — inalterados por Tailwind.
- Custom properties `--rp-*` e `--brand-*` em `profile.css` **funcionam idênticas em v4** (feature de CSS nativo).

## `@apply` e `@layer` — impacto potencial

- **0 usos hoje.** Se decidirmos criar utilities/componentes em CSS futuramente, v4 usa `@utility <name> { … }` em vez de `@layer utilities { .<name> { … } }`.
- Documentar em `CONVENTIONS.md` como padrão para novos utilities.

## Uso de `shadow-*`, `rounded-*`, `ring-*`, `border-*`, `outline-*` e opacidades

| Utility | Ocorrências | Análise v4 |
|---|---|---|
| `shadow-sm` | 81 | **rename automático → `shadow-xs`** (mesmo valor 2px) |
| `shadow` (bare) | verificar antes de migrar | rename `→ shadow-sm` |
| `shadow-md`, `shadow-lg`, etc. | ok | mantidos |
| `shadow-[0_...]` (arbitrary) | comum | mantidos, mas semântica de shadow-color pode mudar |
| `rounded-full` | comum | ok |
| `rounded-sm`, `rounded` (bare) | verificar | rename automático |
| `rounded-md`, `rounded-lg`, `rounded-xl`, `rounded-[...]` | comum | ok |
| `ring-1`, `ring-2`, `ring-4` | 31 | ok (com número explícito) |
| `ring` (bare) | 2 (em `focus:ring` provavelmente) | **default mudou 3px→1px**; ver arquivos |
| `border` (sem cor) | 20+ | **default color mudou** (era gray-200, agora currentColor); verificar |
| `outline-none` | verificar em `focus:outline-none` | v4 renomeado para `outline-hidden` |
| `bg-<color>/<num>` | comum | ok |
| `bg-opacity-*` | 0 | ok |

## Variantes empilhadas

Ordem de aplicação mudou em v4 (right-to-left → left-to-right). Padrões suspeitos como `first:*:pt-0` precisariam virar `*:first:pt-0`. **Grep antes de migrar** em `layouts/**/*.html`.

## Valores arbitrários

Comum no repo. Sintaxes que mudam em v4:

| Sintaxe v3 | Sintaxe v4 | Ocorrências |
|---|---|---|
| `bg-[--var]` | `bg-(--var)` | não medido — grep antes |
| `grid-cols-[max-content,auto]` (vírgula) | `grid-cols-[max-content_auto]` (underscore) | não medido |
| `bg-[radial-gradient(...)]` | igual | ubíquo |

## Pontos que exigem revisão manual pós-migração

1. **Home (`/`, `/pt/`)** — 81 `shadow-sm` visíveis, especialmente em cards de destaque
2. **Perfis de pesquisador** (`/people/<slug>/`) — 18 `printf` gerando HTML complexo
3. **Bordas sem cor explícita** — verificar contraste antes/depois em modo claro
4. **SVGs decorativos** — `text-opacity-40` no hero da home
5. **Focus visible** — verificar `focus:outline-none` em botões (nav, filters, buttons)
6. **Ring em focus** — inputs de busca podem mudar espessura

## Riscos visuais estimados

| Elemento | Antes (v3) | Depois de migrar sem correção (v4) | Depois de migrar com `upgrade` tool |
|---|---|---|---|
| Card com `shadow-sm` | 2px de sombra | 4px de sombra (mais pronunciada) | 2px (rename para `shadow-xs`) |
| Botão com `ring` (bare) | ring 3px azul | ring 1px currentColor | ring-3 currentColor |
| Div com `border` sem cor | border gray-200 | border currentColor (fica invisível se text = bg) | manual — precisa `border-gray-200` explícito |
| SVG com `text-opacity-40` | fill com 40% de opacidade | fill com opacidade padrão (100%) | `text-primary-600/40` |
| Card com `flex-shrink-0` | não encolhe | classe ignorada, encolhe se flex-container permitir | rename para `shrink-0` |
| Elemento com hover em mobile | hover ativa no toque | hover NÃO ativa em toque (mais correto) | comportamento novo aceito |

## Resumo

- **27 usos de classes que serão removidas em v4** (2 text-opacity + 25 flex-shrink)
- **~110 usos de classes que serão renomeadas** automaticamente (81 shadow-sm + resto por medir)
- **72+ classes construídas por `printf`** — safe se `@source layouts/**/*.html` for configurado
- **129 usos do plugin typography** — mantidos, plugin compatível
- **20+ `border` sem cor explícita** — precisam revisão manual pós-migração
- **A ferramenta oficial `npx @tailwindcss/upgrade`** cobre a maioria dos renames automáticos (categoria B); os itens críticos (categoria A e C) requerem revisão humana.
