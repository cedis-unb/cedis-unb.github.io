# Segunda onda: inventário estrutural

Este inventário descreve os contratos dos templates Hugo na branch
`wave2-structural-standardization`. A primeira onda está preservada no commit
`5ff6633095`; o checkpoint inicial desta onda é `a0af8d3153`.

## Famílias de páginas

| Família | Templates | Contrato compartilhado | Composição própria |
| --- | --- | --- | --- |
| A — institucionais | `_default/history.html`, `_default/infrastructure.html`, `_default/partners.html`, `opportunities/list.html` | Título de página, título de seção, métricas e estado vazio quando aplicáveis | Linha do tempo, infraestrutura, parceiros e cartões de oportunidades |
| B — catálogos | `publications/list.html`, `defesas/list.html`, `_default/join.html` | Cabeçalho, métricas e seções de catálogo | Filtros, agrupamento por ano, agenda e CTA de ingresso |
| C — entidades | `areas/single.html`, `products/single.html`, `projects/single.html`, `research-lines/single.html` | Breadcrumb e título com resumo | Metadados, indicadores, relacionamentos e barras laterais de cada entidade |
| Editoriais e especiais | `people/single.html`, `posts/single.html`, `defesas/single.html`, `publications/single.html`, `_default/map.html`, `_default/quiz.html` | Breadcrumb quando há hierarquia | Conteúdo editorial, perfil, mapa e interações específicas |
| Fallback e outras listagens | `_default/single.html`, `_default/list.html`, `_default/institutional.html`, `_default/indicators.html`, `projects/list.html`, `research-lines/list.html`, `products/list.html` | Cabeçalho e breadcrumb conforme o contexto | Conteúdo e navegação próprios |

## Contratos extraídos

Os partials em `layouts/partials/ui/` concentram somente estruturas repetidas:

| Partial | Entrada | Saída |
| --- | --- | --- |
| `page-heading.html` | `page`, `variant`, `align`, `showBreadcrumb`, `eyebrow`, `title`, `description` e classes opcionais | Um breadcrumb opcional, um `h1` e resumo opcional |
| `section-heading.html` | `eyebrow`, `title`, `description`, `actionHtml` e classes opcionais | Um `h2` com ação opcional |
| `stat-card.html` | `tag`, `class`, `value`, `label`, `subtext` e classes opcionais | Métrica em `div`, `li` ou `article`; `0` é valor válido |
| `empty-state.html` | `variant`, `title`, `description`, `ctaLabel`, `ctaUrl` e classes opcionais | Mensagem com CTA opcional |

Classes específicas ficam no template que as usa. Os partials não substituem o
grid, os cards de conteúdo nem a hierarquia editorial de cada página. O
breadcrumb visível continua vindo de `layouts/partials/breadcrumbs.html`, que
também fornece o JSON-LD correspondente.

## Verificação

Após mudanças estruturais, renderizar Hugo em diretório isolado, executar
`python3 scripts/validate_rendered.py <diretório>` e então rodar o build completo
para recompor `docs/` e o índice Pagefind. O validador cobre breadcrumbs
visíveis/JSON-LD e `aria-controls`, além dos invariantes de conteúdo publicados.

Para Lighthouse local, servir a saída com compressão gzip, conforme
`CONVENTIONS.md` §11.5. A coleta do perfil de Sérgio deve usar uma saída
completa; um build interrompido deixa `docs/` parcial e produz 404 espúrio.

Em 2026-09-26, após `npm run build`, o perfil
`/pt/people/sergio_freitas/` respondeu com `Content-Encoding: gzip` no servidor
local de auditoria. Uma coleta Lighthouse por modo deu Performance 99/100 e
LCP 2,11 s em mobile; Performance 100/100 e LCP 0,46 s em desktop. São medidas
locais pontuais, úteis para descartar a hipótese de uma regressão de LCP neste
build, não um orçamento de performance para todas as páginas.
