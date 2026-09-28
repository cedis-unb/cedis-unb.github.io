# Linha de base de acessibilidade

Registro técnico do que o projeto **de fato** verifica em acessibilidade, do que foi
verificado manualmente e quando, e do que não está coberto. É a evidência por trás da
página pública `content/accessibility.{en,pt}.md` — se um número mudar aqui, muda lá.

- **Data desta medição:** 2026-09-27
- **Alvo declarado:** WCAG 2.1 nível AA, mais os acréscimos aplicáveis da WCAG 2.2.
  **Não há declaração de conformidade plena** — nem 2.1, nem 2.2.
- **Ambiente:** build local do site atual servido em `http://127.0.0.1:4173`
  (`npx serve public -l 4173`), Chrome do sistema
  (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`), viewport 1440x900
  salvo onde indicado.
- **Scripts da passagem manual:** `tmp/qa/a11y-*.mjs` (caminho ignorado pelo Git; os JSON
  de saída ficam ao lado). Não são suíte de teste: são instrumentação descartável.

## 1. O que o CI verifica em cada push

Definido em `.github/workflows/site-ci.yml`. Falha em qualquer etapa bloqueia o build.

| Etapa | Ferramenta | Configuração | Cobertura | O que garante |
| --- | --- | --- | --- | --- |
| `Accessibility audit (pa11y-ci)` | pa11y-ci 4.1.1 (runner padrão: HTML_CodeSniffer) | `.pa11yci.json`, `"standard": "WCAG2AA"` | **21 URLs fixas**, PT e EN | Zero erro HTMLCS nas 21 páginas amostradas |
| `Lighthouse CI` | `@lhci/cli` 0.15.1 | `lighthouserc.json`, preset desktop | **8 URLs** | `categories:accessibility` com `minScore: 0.9` como **error** |
| `Validate rendered HTML` | `scripts/validate_rendered.py` | — | ver abaixo | Invariantes estruturais |

Pontos que costumam ser descritos errado:

- **O CI não roda Lighthouse mobile.** `lighthouserc-mobile.json` só é executado pelo script
  local `npm run audit:lighthouse-mobile`. O passo de CI usa apenas `lighthouserc.json`.
- **O limite do Lighthouse é 0,90, não 100.** Uma página pode ter falha de acessibilidade
  real e o build continuar verde — é exatamente o caso da página inicial hoje (ver §4).
- **As 21 URLs do pa11y são amostra.** O build gera mais de três mil páginas; a amostra
  cobre home, institucionais, listagens, uma entidade de cada tipo, um perfil, uma
  publicação, o mapa e as duas páginas de ingresso, nos dois idiomas.
- **Tudo roda em modo claro.** `assets/js/darkmode.js` só ativa a classe `dark` a partir do
  `localStorage` (`color-theme`) ou de `prefers-color-scheme`. O Chrome do CI sobe com
  ambos vazios/claros, então **nenhuma verificação automatizada olha o modo escuro**.
- **Cobertura conceitual.** pa11y/HTMLCS e o axe do Lighthouse decidem cerca de um terço dos
  critérios de sucesso, e só a parte decidível por máquina. Verde significa "nenhuma falha
  automatizada conhecida na amostra".

**Contraste em modo escuro** — `npm run audit:dark`
(`scripts/audit_dark_contrast.mjs`): regra `color-contrast` do axe-core sobre 8
arquétipos, um por família de layout, com o tema escuro forçado via
`localStorage`. Entra no CI logo depois do Pa11y, que roda só no tema claro.
Falha o build. Amostra pequena de propósito: fecha a regressão silenciosa sem
duplicar o custo da suíte.

### Invariantes de `scripts/validate_rendered.py`

Roda sobre o diretório gerado (`docs` no `npm run build`, `public` no CI):

- `validate_breadcrumbs` — trilha visível coerente com o JSON-LD `BreadcrumbList` e sem
  migalhas consecutivas duplicadas.
- `validate_aria_controls` — nenhum `aria-controls` apontando para id inexistente. **É a
  única verificação com cobertura total**: itera `root.rglob("*.html")`.
- `validate_opportunities` — headings e estado vazio de Oportunidades nos dois idiomas.
- `validate_researcher_cards` — listagem de pesquisadores sem metadado de tempo de leitura.
- `validate_profile_area_cards` / `validate_knowledge_area_catalogue` — cards contextuais de
  áreas nos perfis e a variante correta no catálogo.
- `validate_structural_alternates` — `alternate` cruzado PT/EN em Oportunidades, Ingresso e Mapa.

## 2. Resultados automatizados medidos em 2026-09-27

> Esta seção é a medição **antes** das correções do mesmo dia, mantida como linha
> de base. Depois delas, a varredura axe-core — ampliada para **16 páginas x 2
> temas** — reporta **0 violações**, e o pa11y-ci segue em 21/21. O detalhamento
> do que foi corrigido está em §4.


- **pa11y-ci, `WCAG2AA`, 21 URLs: 21/21 passaram, 0 erros.** Reprodução local exigiu
  `PUPPETEER_EXECUTABLE_PATH` apontando para o Chrome do sistema — o Chrome for Testing em
  `~/.cache/puppeteer` está com o framework quebrado nesta máquina.
- **Lighthouse (relatórios de 2026-09-26 em `lhci-report/` e `lhci-report-mobile/`):**
  acessibilidade **1,00 em 7 das 8 URLs** e **0,90 na home**, idêntico em desktop e mobile.
  A home passa o gate com margem zero.
- **axe-core 4.12.1** (via Puppeteer, tags `wcag2a,wcag2aa,wcag21a,wcag21aa,wcag22aa`),
  7 páginas por idioma x 2 temas = 28 execuções:

| Página | Claro | Escuro |
| --- | --- | --- |
| home | 3 violações (`aria-allowed-attr` 2, `aria-required-children` 1) | as mesmas 3 + **`color-contrast` 38** |
| mapa | 1 (`nested-interactive`) | 1 (`nested-interactive`) |
| perfil de pesquisador | 0 | 1 (`color-contrast`) |
| oportunidades, publicações, defesas, ingresso | 0 | 0 |

  Idêntico em PT e EN. O axe ainda marca `color-contrast` como *incomplete* em 3.508 nós ao
  longo das execuções — lembrete de que contraste não é integralmente decidível por máquina.

**Consequência importante:** o pa11y reporta 0 erros na home enquanto o axe e o Lighthouse
apontam 3 violações críticas/sérias na mesma página, em modo claro. Um único verificador
automatizado não é evidência suficiente.

## 3. Passagem manual de 2026-09-27

Instrumentada com Puppeteer + Chrome do sistema, sempre com `--accept-lang=en-US` (sem isso
o autodetect de idioma em `layouts/partials/head.html` redireciona toda URL inglesa para a
gêmea `/pt/` e o teste inglês vira um segundo teste português). Cobertura: EN e PT, tema
claro e escuro.

| Área | O que foi feito | Resultado |
| --- | --- | --- |
| Menu principal | Tab pelo cabeçalho; Enter em cada gatilho; Tab para dentro do painel; Esc | **24/24 ciclos corretos** (6 submenus x 2 idiomas x 2 temas): `aria-expanded` `false`→`true`→`false`, Esc fecha e **devolve o foco ao gatilho** |
| Skip link | Medição antes e depois do foco | `a[href="#main-content"]`, destino existe; 1x1 px oculto → **170,7x36 px (EN) / 180x36 px (PT)** com foco |
| Armadilha de teclado | Ciclo completo de Tab em home, oportunidades, publicações e defesas, nos 2 idiomas | **Nenhuma armadilha**; ciclo maior = 670 paradas (publicações); todos voltam ao `body` |
| Mapa — semântica | Atributos do `<svg>` | `role="img"`, `aria-label` localizado, `aria-describedby` → id existente |
| Mapa — nós | Tab real pela página; Enter e Espaço | **53 nós**, todos com `tabindex="0"` + `role="button"` + `aria-label` localizado; caminhada de Tab: 169 paradas, **53 nelas são nós**; **Enter e Espaço** selecionam e revelam o link de detalhe (`/tags/...`, `/pt/tags/...`) |
| Mapa — foco | Estilo computado com e sem foco | Visível nos **dois temas**: `stroke` branco 2 px → `#0f172a` 5 px, mais o anel do UA (`outline: auto 5px`, `rgb(0,95,204)` claro / `rgb(153,200,255)` escuro) |
| Mapa — zoom | Medição e Tab | 8 botões na barra (5 filtros + afastar/aproximar/redefinir), **todos 34 px de altura**, todos com `tabIndex 0`, nos 2 idiomas; Tab a partir do último cai num nó |
| Mapa — movimento | `prefers-reduced-motion: reduce` emulado | Respeitado: flag Alpine `prefersReducedMotion` = `true`, transições em 0 ms, `document.getAnimations()` = 0; sem a preferência, `false` |
| Mapa — alternativa | JavaScript desligado | SVG com **0 filhos** e `main` ainda com **202 `<a href>` reais** renderizados no servidor — a alternativa não depende do D3. **Ressalva:** 125 desses links estão dentro de `<details>` fechados e só recebem foco depois que o usuário expande |
| Filtros | Oportunidades (1 `select`), Publicações (3), Defesas (3) | Todos focalizáveis por teclado, **todos com 37 px de altura**, **todos nomeados por `<label>` envolvente**; 0 controle sem nome acessível |
| Cards | Contagem de `article` e de link de título | Defesas 168/168 com link no título; Oportunidades 3/3; nenhum card sem link |
| Tamanho de área (2.5.8) | Bounding box real + exceção de espaçamento implementada (círculo de 24 px vs caixa dos outros alvos) | home 105 alvos / 16 abaixo de 24 px / **0 falhas**; mapa 291 / 58 / **1 falha** (EN); oportunidades 38 / 3 / 0; publicações 668 / 30 / 0; **defesas 369 / 334 / 121 falhas (EN) e 152 (PT)** |
| Menor controle | Medição | **Link de busca do cabeçalho: 20x40 px** — abaixo dos 24 px de largura, passa só pela exceção de espaçamento (alvo mais próximo a 37,3 px) |
| Nós do mapa | Medição | **21 de 53 com 20x20 px**, 20 com 24x24, 7 com 32x32, 5 com 36x36 — os de 20 px passam só pela exceção de espaçamento |
| Refluxo (1.4.10) | Viewports de 640 px (= 200%) e 320 px (= 400%) | **200%:** só `/defesas/` (EN) transborda (649 vs 640). **400%:** `/` 333, `/pt/` 334, `/publications/` e `/pt/publications/` 408, `/defesas/` 649, `/pt/defesas/` 632 — todos contra 320. `/map/`, `/pt/mapa/`, `/opportunities/`, `/pt/oportunidades/` **limpos** |
| Modo escuro | axe-core com a classe `dark` aplicada | **38 nós de contraste insuficiente na home** e 1 no perfil — ver §4 |
| Paridade PT/EN | Nome acessível dos controles do cabeçalho | **Duas falhas**: botão de tema anuncia `"Alternar modo claro/escuro"` também em inglês; botão do menu móvel anuncia `aria-label="Main"` nos dois idiomas |
| Divulgação por clique | Foco e Tab sobre `#former-collaborators-title` | **Inoperável por teclado**: `tabIndex` −1, sem `role`, sem `aria-expanded`, sem handler de teclado; 400 Tabs não alcançam |

## 4. Defeitos: corrigidos e abertos

A passagem manual de 2026-09-27 levantou 13 defeitos. Doze foram corrigidos no
mesmo dia; a varredura axe-core sobre 16 páginas x 2 temas saiu de **145
violações para 0**.

### Corrigidos em 2026-09-27

| Onde | Problema | Critério | O que foi feito |
| --- | --- | --- | --- |
| 44 arquivos em `content/people/` e `content/areas/` | `<h2>`/`<h3>` com `@click`: sem foco, sem papel, sem tecla. O bloco "Orientações anteriores" (71 itens no perfil do Sérgio) e "Pesquisadores anteriores" eram inalcançáveis por teclado | 2.1.1 (A) | `<button type="button">` dentro do heading, com `:aria-expanded` e `aria-controls`, no mesmo padrão que `content/people/all.*.md` já usava |
| mesmo markup | `text-primary-900` sem variante dark: 1,02:1 | 1.4.3 | `dark:text-primary-100` |
| `layouts/partials/upcoming-defenses-agenda.html` | `role="tablist"` com `<button>` sem `role="tab"` (axe crítico); prendia a capa em 0,90 no Lighthouse, que é exatamente o portão do CI | 4.1.2 | `role="tab"`, tabindex móvel, `aria-controls` e `role="tabpanel"` nos painéis |
| `layouts/index.html` e mais 5 templates | 64 usos de `dark:text-slate-500` em cards escuros: 2,7–3,1:1 | 1.4.3 | `dark:text-slate-400` (4,9–5,6:1) |
| `assets/css/main.css` | `--tw-prose-links` em `#51C5CF` sobre branco (2,05:1) e `--tw-prose-lead` em primary-600 (3,58:1) | 1.4.3 | primary-700 (5,79:1) |
| `assets/css/main.css` | o bloco `.prose` vinha depois de `dark:prose-invert` com a mesma especificidade e vencia — o tema escuro seguia com a paleta clara (títulos 1,07:1) | 1.4.3 | mapeamento invertido reafirmado com especificidade maior |
| `layouts/_default/map.html` | `<svg role="img">` com 53 nós focáveis dentro (`nested-interactive`) | 4.1.2 | `role="group"` com o mesmo rótulo |
| `layouts/partials/theme-toggle.html` | `aria-label`/`title` fixos em português em toda página inglesa | 3.1.2 | `i18n "ui_theme_toggle"` |
| `layouts/partials/nav.html` | botão do menu mobile com `aria-label="Main"`, fixo e sem descrever a ação | 2.4.6 | `i18n "ui_menu_toggle"` |
| `layouts/partials/footer.html` | rótulos de seção em `text-slate-700`/`text-slate-500` sobre a faixa escura: 1,6:1 e 3,8:1 | 1.4.3 | `text-slate-400` (~6:1) |
| `layouts/shortcodes/tags.html` | pílulas herdavam `prose-a:text-sky-700` sobre `bg-gray-300` (3,97:1) e ficavam claras no tema escuro | 1.4.3 | `not-prose` no contêiner e variante dark na pílula |
| `layouts/shortcodes/{prev,next}.html`, `layouts/partials/footer.html` | links prev/next em primary-500 sobre primary-50: 1,87:1 | 1.4.3 | primary-700 e superfície escura para o cartão |
| `layouts/defesas/list.html` | `<select>` sem limite de largura crescia até a maior opção e estourava já em 200% de zoom | 1.4.10 | `w-full max-w-full min-w-0 truncate` no select e `min-w-0` no label |

### Corrigidos em 2026-09-28 — refluxo e área clicável

| Onde | Problema | Critério | O que foi feito |
| --- | --- | --- | --- |
| `layouts/people/single.html` | o `<aside>` da barra lateral é item de grid sem `min-w-0`, então herda `min-width: auto` e o seu conteúdo mínimo alargava a trilha acima da viewport | 1.4.10 | `min-w-0` no aside e `[&>*]:min-w-0` no grid do hero |
| `layouts/index.html` | a grade de áreas em 2 colunas dá 138 px por célula; com o ícone de 36 px sobram ~64 px e "Transformation" precisa de ~105 px | 1.4.10 | uma coluna abaixo de 22rem (`grid-cols-1 min-[22rem]:grid-cols-2`) |
| `layouts/_default/publications.html`, `layouts/shortcodes/publications.html` | a linha de veículo traz tokens sem espaço, como `(ISPA/BDCloud/SocialCom/SustainCom)`, que não quebram em 320 px | 1.4.10 | `[overflow-wrap:anywhere]` no parágrafo |
| `layouts/partials/nav.html` | link de busca declarado `h-10 w-10` renderizava 20x40 px porque o flex o espremia | 2.5.8 | `shrink-0` |
| `layouts/partials/defesa-card.html` | o `<a>` do título é inline e mede a altura da fonte (18 px) | 2.5.8 | `block min-h-6` — ocupa a linha inteira, sem mover o layout |

Depois disso: **0 rolagens horizontais** em 24 rotas a 320, 375 e 640 px, e
**0 falhas de SC 2.5.8** em oito páginas com a exceção inline aplicada.

### Contraste sobre gradientes — sessão registrada (2026-09-28)

O axe classifica contraste sobre gradiente como *incomplete*, não como
violação, então essa superfície precisa de conferência própria.
`npm run audit:gradient` (`scripts/audit_gradient_contrast.mjs`) calcula a
razão contra **cada parada de cor opaca** do gradiente do ancestral mais
próximo e reporta o pior caso, cobrindo cabeçalho, rodapé, heroes e pills em
8 páginas x 2 temas.

| Superfície | Elementos medidos | Abaixo do exigido | Pior razão |
| --- | --- | --- | --- |
| Rodapé | 240 | 0 | 6,74:1 |
| Pills | 366 | 0 | 5,18:1 |
| Heroes | 29 | 0 | 7,22:1 |

Duas armadilhas de método, encontradas ao calibrar o script e que qualquer
reexecução precisa respeitar:

- a busca pelo gradiente tem de **parar no primeiro ancestral com cor de fundo
  opaca** — sem isso, texto sobre um hero `bg-slate-950` era comparado com o
  gradiente da página, bem mais acima, dando razões falsas de 1,00:1;
- só as **paradas opacas** descrevem o fundo efetivo. Véus radiais como
  `rgba(197,39,47,0.12)` e o `transparent` que o navegador expande para
  `rgba(0,0,0,0)` são tingimentos sobre a base; tratá-los como cor cheia
  produzia razões falsas de ~1:1 em heroes claros.

Não é portão de CI de propósito: a leitura das paradas é heurística e uma
forma de gradiente nova poderia derrubar o build sem haver defeito. É
verificação de rotina após mudança de paleta ou de superfície.

### Corrigidos em 2026-09-28 — cabeçalho, templates e cobertura de CI

| Onde | Problema | Critério | O que foi feito |
| --- | --- | --- | --- |
| `layouts/partials/nav.html` | cabeçalho `md:sticky` fixava 199 px entre 768 e 1023 px e 159 px entre 1024 e 1440 px durante todo o scroll | — | hambúrguer abaixo de `lg`, duas linhas de `lg` a `2xl` sem sticky, uma linha e sticky a partir de `2xl` |
| `layouts/_default/single.html` (fallback) | about, contact, privacy, accessibility, reconhecimentos e divulgação científica caíam num fallback com faixa `bg-primary-600` e h1 branco centralizado, fora do padrão do site | — | `_default/institutional-page.html`, no padrão da família institucional |
| `content/junte-se/*` | as 7 trilhas tinham `audience`, `duration` e dois CTAs no frontmatter e **nenhum** chegava ao HTML — a página de detalhe publicava menos que a listagem que levava até ela | — | `layouts/junte-se/single.html` publica todos os campos |
| CI | contraste em modo escuro não era verificado | 1.4.3 | `npm run audit:dark` no pipeline |
| — | contraste sobre gradiente sem medição registrada | 1.4.3 | `npm run audit:gradient` e a sessão registrada acima |

### Ainda abertos

| Onde | Problema | Critério | Observação |
| --- | --- | --- | --- |
| qualquer fundo em gradiente | o axe classifica contraste sobre gradiente como *incomplete*, não como violação | 1.4.3 | há procedimento próprio (`npm run audit:gradient`, sessão registrada acima), mas ele não roda a cada push — é executado após mudança de paleta ou de superfície |
| `layouts/_default/map.html` | D3 7.9.0 vem de `cdn.jsdelivr.net`; se o CDN cair o grafo não é desenhado | — | não é falha WCAG: a lista semântica de links é renderizada no servidor |
| processo | nenhuma sessão de leitor de tela registrada | — | nada aqui se apoia em NVDA, JAWS ou VoiceOver. Roteiro pronto para execução em `roteiro-leitor-de-tela.md` |

## 5. Não coberto — e assumido como não coberto

- **Leitor de tela.** Nenhuma sessão de NVDA, JAWS, Narrator ou VoiceOver está registrada.
  Afirmações sobre "ordem de leitura" ou "anúncio correto" não têm respaldo aqui.
- **Auditoria externa.** Nenhuma contratada. Não citar nenhuma.
- **Modo escuro no CI.** Coberto desde 2026-09-28 por `npm run audit:dark`, mas só em 8 arquétipos — as demais páginas em tema escuro seguem sem verificação automatizada (§1).
- **Mobile no CI.** Só local (§1).
- **eMAG critério por critério.** Usado como referência, não verificado.
- **Zoom de texto isolado**, orientação, entrada por voz, `forced-colors`/alto contraste do
  Windows, legendas/transcrições de mídia embutida: fora desta passagem.
- **As 3.000+ páginas fora da amostra.** Seguem a mesma família de templates das amostradas,
  o que é argumento de plausibilidade — não evidência.

## 6. Como reproduzir

```bash
# servidor de auditoria (gzip nativo; python http.server distorce Lighthouse)
npx serve public -l 4173 --no-clipboard

# pa11y-ci — 21 URLs, WCAG2AA
PUPPETEER_EXECUTABLE_PATH='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
  npx --no-install pa11y-ci --config .pa11yci.json

# Lighthouse desktop (gate do CI) e mobile (só local)
npm run audit:lighthouse
npm run audit:lighthouse-mobile

# contraste em modo escuro (8 arquétipos) — mesmo passo que roda no CI
npm run audit:dark

# contraste sobre gradientes (cabeçalho, rodapé, heroes, pills) — não é portão
npm run audit:gradient

# invariantes estruturais
python3 scripts/validate_rendered.py public
```

Para repetir a passagem manual, os scripts de 2026-09-27 ficam em `tmp/qa/`
(`a11y-manual-pass.mjs`, `a11y-followup.mjs`, `a11y-followup2.mjs`, `a11y-followup3.mjs`,
`a11y-axe.mjs`, `a11y-contrast-detail.mjs`). Sempre com
`args: ['--no-sandbox','--lang=en-US','--accept-lang=en-US']`.
