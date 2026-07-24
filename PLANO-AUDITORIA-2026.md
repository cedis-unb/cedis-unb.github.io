# Plano de execução — Auditoria integrada 2026 (v2)

**Referência:** auditoria integrada do site e do repositório Hugo do CEDIS (12 issues numeradas de I01 a I12) + arquitetura de navegação revisada de julho/2026 (novas issues I13 a I16).
**Data-base:** 20 de julho de 2026.
**Escopo:** este documento traduz a auditoria em um plano executável. Complementa (não substitui) o `ROADMAP.md` de comunicação e o `CONVENTIONS.md` de padrões editoriais.

## Changelog v1 → v2

- **+I13** menu principal com 6 itens (Sobre · Pesquisa · Projetos e produtos · Pessoas · Publicações · Participe).
- **+I14** notícias como camada transversal (home, projetos, produtos, perfis; sem primeiro nível de menu).
- **+I15** rodapé enriquecido (Notícias · Contato · Divulgação científica · Zenodo · GitHub · LinkedIn · YouTube · Intranet · Privacidade · Acessibilidade).
- **+I16** páginas institucionais estruturantes (Reconhecimentos, Infraestrutura, Indicadores, Contato, Divulgação científica).
- **Ajuste I07** — Publicações passa a se subdividir por tipo (Publicações científicas · TCCs · Dissertações e teses · Registros de software · Materiais no Zenodo · Cursos e materiais didáticos) para alimentar o menu de "Publicações".
- **Ajuste I09** — Oportunidades vira parte de "Participe" no menu, ao lado das trilhas por público (IC, TCC, Mestrado, Doutorado, Extensão, Parcerias, Proponha um projeto).
- **Reordenação de fases:** IA/nav (I13/I15/I16) sobe para Fase 2; modelo de dados (I02/I03) vai para Fase 3; reestruturação de conteúdo (I07/I09/I14/I08) vira Fase 4; qualidade+política (I10/I12) segue como Fase 5.

## Atualização de modelo de dados — 2026-07-24

O ciclo de refactor de 2026-07-24 consolidou a meta operacional do portal:
informação entra em uma fonte canônica e se propaga pelos templates.

Estado vigente:

- `data/advisors.yaml` foi removido. Contato, Lattes, ORCID, áreas e nível de perfil de docentes agora vivem no frontmatter de `content/people/<slug>.{pt,en}.md`.
- `layouts/partials/people-index.html` e `people-lookup.html` são a camada central para leitura de pessoas. Templates novos não devem consultar `hugo.Data.people` ou `content/people` diretamente quando precisam resolver uma pessoa por slug.
- `data/productions.yaml` separa pessoas e tópicos: `people[]` guarda slugs canônicos; `tags[]` guarda áreas, temas, projetos e estados.
- `data/productions.yaml` é a fonte única de publicações. `content/publications/**` é gerado por `scripts/build_publications.py`, marcado com `generated_by`/`canonical_source`, chamado automaticamente por `npm run build` e verificado por `scripts/build_publications.py --check` no CI.
- `layouts/partials/translated-label.html` resolve rótulos em cascata: i18n manual → `project-lookup` → `area-lookup` → `people-lookup` → `humanize`.
- `data/people.yaml` exige `slug:` explícito em toda entrada; `scripts/validate_content.py` valida essa regra.
- Frontmatter de perfis usa `profile_level` como tipo principal (`researcher`, `card_with_page`, `advisor_only`, `derived`). `categories` fica restrito a marcações taxonômicas legadas/necessárias, sem repetir o slug do próprio arquivo.

Backlog técnico pós-refactor, ordenado por retorno para a meta de
automação/manutenção:

| Ordem | Gap | Estado atual | Risco/impacto | Próxima ação | Critério de conclusão |
|---|---|---|---|---|---|
| 1 | Vínculos de produtos | Produtos vivem em `content/products/*.md` e usam `project`, `secondary_projects`, `responsible`, `publications`, `tags` e `categories` com validação parcial. | Produto pode ficar descoordenado de projeto/área/pesquisador sem falha clara no CI. | Reforçar `scripts/validate_content.py` para resolver todos os IDs citados em produtos e avisar duplicidade entre `project` e `secondary_projects`. | `npm test` falha quando produto aponta para projeto/pessoa/publicação inexistente ou vínculo redundante. |
| 2 | Notícias relacionadas | Posts ainda dependem principalmente de `tags`/`categories` para relação com pessoas, projetos, produtos e áreas. | Relações editoriais ficam frágeis e difíceis de usar em blocos automáticos de "notícias relacionadas". | Padronizar frontmatter opcional `people`, `projects`, `products`, `areas` em posts e adaptar `related-news.html` para preferir esses campos. | Uma notícia marcada uma vez aparece automaticamente nos perfis/projetos/produtos/áreas relacionados. |
| 3 | Produtos como fonte canônica | Produtos são páginas `.md`, não um YAML canônico. Isso é aceitável enquanto cada produto exige descrição rica. | Manutenção ainda exige editar par PT/EN e frontmatter manual. | Avaliar custo-benefício de `data/products.yaml` + geração de páginas, semelhante a publicações. | Decisão registrada: manter `.md` com validação forte ou migrar para YAML gerado. |
| 4 | Autores de publicações | `data/productions.yaml` usa `authors[]` textual e `people[]` separado para slugs canônicos. | Renomear/deduplicar autores externos ainda exige curadoria manual; erro de digitação em `authors[]` pode criar variação textual. | Migrar gradualmente para objetos `{slug, cited_as}` apenas quando houver tempo para curadoria. | Templates usam `slug` para link e `cited_as` para citação/BibTeX; autores externos ficam com `slug: null`. |
| 5 | Curadoria externa | ORCID, DOI, ISBN, Lattes, nomes externos e traduções dependem de entrada humana. | Não há automação completa sem integração externa ou revisão humana. | Melhorar validadores e relatórios, não tentar automatizar semanticamente tudo. | Validador aponta ausência/formato inválido; decisões semânticas continuam humanas. |

Observação sobre projetos e áreas: `layouts/partials/project-index.html`,
`project-list.html`, `project-lookup.html`, `area-index.html`,
`area-list.html` e `area-lookup.html` já centralizam o acesso a
`data/projects.yaml` e `data/areas.yaml`. Templates novos não devem iterar
`hugo.Data.projects`/`hugo.Data.areas` diretamente fora desses partials.

## Impacto em Fases 0 e 1 (concluídas)

Todas as entregas de Fase 0 (I11, I05) e Fase 1 (I04, I06, I01) **permanecem válidas sem correções** sob a nova IA:

- **I06 (canonical/og:type/robots)** — `og:type` mapeia por `.Section` (URL do conteúdo), não por menu. O mapeamento `products` → product, `people` → profile, `posts` → article, etc. permanece correto mesmo com "Projetos e produtos" agrupados no menu.
- **I01 (CI)** — valida build/links independentemente da IA. Nenhum ajuste.
- **I04 (correções factuais)** e **I05 (limpeza de `data/`)** — pré-requisitos permanentes, não tocam navegação.
- **I11 (README + metadados)** — descreve estrutura do repo, não menu. Sem impacto.
- **Layout de arquivo de notícias em `/categories/news/`** (entregue fora do plano em fase anterior) — sob a nova IA, essa URL passa a ser o **arquivo de notícias linkado do rodapé** (I15). O template editorial continua servindo perfeitamente a esse papel. Nenhuma edição de layout.
- **Bloco "Esta semana no CEDIS" na home** — sob a nova IA, continua sendo o destaque transversal de notícias na home. Sem alteração.

## Como ler este plano

Cada issue tem uma ficha de execução com **precondições**, **entregáveis concretos**, **verificação** e **arquivos alvo**. As fases apenas ordenam a execução — dentro de uma fase, várias issues podem ser tocadas em paralelo por pessoas diferentes.

Rótulos usados: `crítica` `alta` `média` para prioridade; `S` `M` `L` `XL` para esforço (dia/semana/2-4 semanas/mês+).

---

## Nova arquitetura de navegação (referência para I13 e I15)

**Menu principal (6 itens conceituais):**

1. **Sobre** — O CEDIS · História · Parceiros · Reconhecimentos · Infraestrutura · Indicadores · Contato
2. **Pesquisa** — Áreas de pesquisa · Mapa de competências · Linhas e temas · Pesquisa por pesquisador · Métodos e infraestrutura científica
3. **Projetos e produtos** — Projetos em andamento · Projetos concluídos · Produtos digitais · Sistemas e demonstrações · Bases de dados e recursos · Projetos por parceiro
4. **Pessoas** — Pesquisadores · Colaboradores · Estudantes e orientandos · Alumni
5. **Publicações** — Publicações científicas · TCCs · Dissertações e teses · Registros de software · Materiais no Zenodo · Cursos e materiais didáticos
6. **Participe** — Oportunidades abertas · IC · TCC · Mestrado · Doutorado · Extensão e voluntariado · Parcerias institucionais · Proponha um projeto

**Fora da navegação conceitual (cabeçalho):** busca, seletor de idioma, alternância claro/escuro.

**Rodapé:** Notícias · Contato · Divulgação científica · Zenodo · GitHub · LinkedIn · YouTube · Intranet · Privacidade · Acessibilidade.

**Notícias** ficam explicitamente fora do menu principal — servidas por (a) destaque na home, (b) blocos "notícias relacionadas" em páginas de projeto/produto/pesquisador, (c) arquivo completo em `/categories/news/` acessível pelo rodapé.

---

## Ordem de execução (v2)

```
Fase 0 — Preparação                        ✅ CONCLUÍDA   (I11, I05)
Fase 1 — Correções + fundação CI           ✅ CONCLUÍDA   (I04, I06, I01)
Fase 2 — Arquitetura de navegação          ✅ CONCLUÍDA   I13, I15, I16
Fase 3 — Modelo de dados canônico          ✅ CONCLUÍDA   I02 → I03
Fase 4 — Reestruturação de conteúdo        ✅ CONCLUÍDA   I07, I09, I14, I08
Fase 5 — Qualidade e política              ✅ CONCLUÍDA   I10, I12
```

**Regras de sequenciamento:**

- I02 é pré-requisito de I03, I07, I09 e I14 (relações estruturadas dependem de schema).
- I13 depende de I16 (estrutura de páginas institucionais precisa existir antes do menu apontar para elas).
- I01 é pré-requisito de I10.
- Fase 2 podia começar com conteúdo mínimo enquanto Fase 3 amadurecia — o menu não precisava esperar o modelo de dados.

---

## Fase 0 — Preparação ✅ CONCLUÍDA

Concluída em `58d1f8860` e commits anteriores. Detalhes originais preservados por referência.

### I11 — Documentação e metadados do repositório ✅
- README.md, `.tool-versions` (hugo 0.164.0, nodejs 24.14.1), `package.json` com metadados CEDIS.

### I05 — Remoção de arquivos de dados antigos ✅
- Removidos `data/people-old*.yaml`, `data/people-errado.yaml`, `data/productions copy.yaml`. `CONVENTIONS.md` documenta fontes canônicas.

---

## Fase 1 — Correções factuais e fundação de CI ✅ CONCLUÍDA

Concluída em `9756046cf` e commits anteriores.

### I04 — Correções factuais e referenciais ✅
- DFCris link corrigido para `/people/andre_lanna`; typo `Cibersecurity` → `Cybersecurity` (asset + 6 refs + título); `logoFGA.png` → `logoFCTE.png`; padrão `daniel_sundfeld` documentado.

### I06 — Canonical, og:type e robots ✅
- `<link rel="canonical">` em todas as páginas; `og:type` refinado por seção; `layouts/robots.txt` com Sitemap absoluto.

### I01 — CI de construção e validação ✅
- `.github/workflows/site-ci.yml` com Hugo 0.164.0 pinado, Pagefind, lychee. `lychee.toml` com exclusões calibradas.

---

## Fase 2 — Arquitetura de navegação

### I13 — Menu principal de 6 itens
- **Prioridade:** crítica · **Esforço:** M · **Depende de:** I16 (páginas-alvo devem existir; podem ser stubs)
- **Precondições:**
  1. Confirmar rota para cada sub-item (algumas já existem: `/history/`, `/parceiros/`, `/categories/knowledge_areas/`, `/people/`, `/projects/`, `/products/`, `/publications/`, `/oportunidades/`, `/junte-se/`, `/infra/`).
  2. Páginas-base criadas em I16 para todos os destinos do menu.
- **Entregáveis:**
  1. Reescrever `hugo.yaml` bloco `menu.main` para **6 itens** (PT e EN):
     `Sobre · Pesquisa · Projetos e produtos · Pessoas · Publicações · Participe`.
  2. Definir os sub-menus (`menu.sobre`, `menu.pesquisa`, `menu.projetos-produtos`, `menu.pessoas`, `menu.publicacoes`, `menu.participe`) preservando o padrão `pre: complexdropdown` já usado.
  3. Ajustar `layouts/partials/header.html` (ou equivalente) se necessário para renderizar os dropdowns nos novos identifiers.
  4. Adicionar redirecionamentos (aliases) das URLs antigas de menu que sumirem — ex.: `/oportunidades/` continua existindo (é o "Oportunidades abertas" dentro de "Participe"), mas caso a estrutura de rotas mude, aliases evitam 404 de bookmarks.
  5. Traduzir os 6 rótulos em `i18n/pt.yaml` e `i18n/en.yaml` (chaves novas `ui_menu_sobre`, `ui_menu_pesquisa`, etc.).
- **Verificação:** navegação por teclado percorre 6 dropdowns em PT e EN; nenhum item retorna 404; contagem de links do header antes/depois documentada; screenshot manual em mobile e desktop.
- **Arquivos:** `hugo.yaml`, `layouts/partials/header.html`, `i18n/pt.yaml`, `i18n/en.yaml`.

### I15 — Rodapé institucional
- **Prioridade:** alta · **Esforço:** S · **Depende de:** I16 (páginas de Contato/Divulgação científica/Privacidade/Acessibilidade devem existir)
- **Precondições:** decidir se Intranet é link externo (autenticado) ou página institucional.
- **Entregáveis:**
  1. Reorganizar `layouts/partials/footer.html` em duas colunas semânticas: **Explorar** (Notícias, Zenodo, Intranet) e **Institucional** (Contato, Divulgação científica, Privacidade, Acessibilidade).
  2. Ícones sociais (GitHub, LinkedIn, YouTube) permanecem em bloco dedicado; adicionar YouTube se ainda não existir.
  3. Link "Notícias" do rodapé aponta para `/categories/news/` (arquivo já reformulado em fase anterior).
  4. Testes de contraste em modo claro e escuro (validação leve; validação plena vem em I10).
- **Verificação:** rodapé renderiza em PT e EN sem broken links; todos os itens do bloco "rodapé" da nova IA estão presentes.
- **Arquivos:** `layouts/partials/footer.html`, `i18n/pt.yaml`, `i18n/en.yaml`, eventualmente `static/icons/`.

### I16 — Páginas institucionais estruturantes
- **Prioridade:** alta · **Esforço:** M · **Depende de:** —
- **Precondições:** decidir conteúdo mínimo publicável de cada página.
- **Entregáveis:**
  1. **Reconhecimentos** — `content/reconhecimentos/index.{pt,en}.md`: página que agrega prêmios e menções honrosas do CEDIS (dados já dispersos em `content/posts/news-post.002,013,017,019.*.md` e outros). Renderizada com título, ano, contexto, link para a notícia original.
  2. **Infraestrutura** — expandir `content/infra/index.{pt,en}.md` (existe hoje) com blocos de servidores, laboratórios físicos, licenças de software, serviços em nuvem.
  3. **Indicadores** — `content/indicadores/index.{pt,en}.md`: página pública com números-síntese (anos, pesquisadores, publicações, defesas, produtos, registros). Reutilizar métricas já geradas em `layouts/_default/history.html`.
  4. **Contato** — normalizar `content/contact/index.{pt,en}.md` (existe hoje) com endereço postal, coordenação, e-mail institucional, mapa.
  5. **Divulgação científica** — `content/divulgacao-cientifica.{pt,en}.md`: materiais institucionais, contato para consulta pública, notícias e áreas de expertise.
  6. **Política de privacidade** e **Acessibilidade** — páginas-base em `content/privacy/index.{pt,en}.md` e `content/accessibility/index.{pt,en}.md`, posteriormente detalhadas nas fases de política e qualidade.
- **Verificação:** cada URL responde 200 em PT e EN; título e descrição adequados para SEO; links no menu (I13) e rodapé (I15) resolvem.
- **Arquivos:** `content/reconhecimentos/`, `content/infra/`, `content/indicadores/`, `content/contact/`, `content/divulgacao-cientifica.*.md`, `content/privacy/`, `content/accessibility/`.

---

## Fase 3 — Modelo de dados canônico

### I02 — Esquema e validação dos dados
- **Prioridade:** crítica · **Esforço:** M · **Depende de:** decisão do modelo de informação (§20 da auditoria)
- **Precondições:** documento curto (`docs-src/data-model.md`, ~1 página) formalizando os campos obrigatórios de cada entidade, IDs estáveis e enumerações de estado.
- **Entregáveis:**
  1. `schemas/` com um JSON Schema por entidade: `person.schema.json`, `project.schema.json`, `product.schema.json`, `publication.schema.json`, `area.schema.json`, `partner.schema.json`, `opportunity.schema.json`, `recognition.schema.json`.
  2. `scripts/validate_content.py` que percorre `data/` e `content/`, valida contra os schemas, cruza referências (todo `researcher_id` existe em `people`, todo `area` existe em `areas`, etc.) e sinaliza `translationKey` órfãos.
  3. Etapa `validate` no `site-ci.yml` (I01) chamando o script.
- **Verificação:** dados atuais devem passar; PR de teste inserindo referência inexistente deve falhar.
- **Arquivos:** `schemas/`, `scripts/validate_content.py`, `.github/workflows/site-ci.yml`, `docs-src/data-model.md`.

> Nota (2026-07-24): I02 foi atualizado para o modelo sem `data/advisors.yaml`.
> O validador agora cruza pessoas por `content/people/*.md` + `data/people.yaml`,
> exige `slug:` em `data/people.yaml`, valida `people[]` em publicações e aceita
> entradas consolidadas com `supervisions[]`.

### I03 — Unificação de projetos, produtos e relações
- **Prioridade:** crítica · **Esforço:** L · **Depende de:** I02
- **Entregáveis:**
  1. Cada `content/projects/*.md` recebe `id`, `researchers`, `areas`, `partners`, `funding_agencies`, `products`, `publications` no *front matter*.
  2. Cada `content/products/*.md` recebe `id`, `status`, `areas`, `responsible`, `project`, `publications`.
  3. `data/projects.yaml` passa a ser **gerado** (ou eliminado) — a origem é a página.
  4. Templates de perfil (`layouts/people/single.html`) derivam projetos/produtos via `where site.RegularPages "Params.researchers" "intersect" (slice $id)` — remove-se qualquer lista manual redundante.
  5. **Sob a nova IA (agrupamento Projetos e produtos):** a página "Projetos" mostra bloco "Produtos derivados"; a página de cada produto mostra "Projetos de origem". Cross-linking automático.
  6. Regra explicitada em `CONVENTIONS.md`: **relações inversas nunca são registradas à mão**.
- **Verificação:** validador (I02) reporta zero referências manuais duplicadas; visual diff das páginas de projeto/produto/perfil deve ser mínimo antes/depois; cada projeto lista seus produtos e vice-versa sem edição manual.
- **Arquivos:** `content/projects/*`, `content/products/*`, `layouts/people/single.html`, `layouts/projects/single.html`, `layouts/products/single.html`, `data/projects.yaml`, `CONVENTIONS.md`.

> Nota (2026-07-24): parte da unificação foi concluída pelo `people-index`,
> pela remoção de `data/advisors.yaml`, pela separação `people[]`/`tags[]` em
> publicações e pela cascata i18n. `data/projects.yaml` permanece como fonte
> canônica de metadados agregados de projetos; eliminar ou gerar esse arquivo
> a partir de `content/projects/*` fica como decisão futura.

---

## Fase 4 — Reestruturação de conteúdo ✅ CONCLUÍDA

Concluída em julho/2026 com geração canônica de publicações, oportunidades estruturadas sem chamadas abertas no momento, trilhas "Participe", notícias relacionadas em páginas de projeto/produto/pesquisador e validação PT/EN no CI.

### I07 — Publicações como páginas canônicas (ajuste v2) ✅
- **Prioridade:** alta · **Esforço:** L · **Depende de:** I02
- **Ajuste v2:** o menu "Publicações" (I13) espera sub-itens por tipo — a geração precisa oferecer listagens filtráveis e URLs limpas por tipo:
  - `/publications/scientific/` (article, book, book chapter)
  - `/publications/tcc/` (tcc)
  - `/publications/thesis/` (dissertation, phd)
  - `/publications/specialization/` (specialization)
  - `/publications/registrations/` (registro)
  - `/publications/zenodo/` (materiais depositados no Zenodo — novo campo `zenodo_record` já existe)
  - `/publications/didactic/` (cursos e materiais didáticos — novo tipo `didactic` a ser incluído em I02)
- **Entregáveis:**
  1. `content/publications/{tipo}/{ano}/{id}.{lang}.md` gerado a partir de `data/productions.yaml` (script `scripts/build_publications.py`).
  2. `layouts/publications/single.html` com título, autores (linkados por ID), resumo, DOI, tipo, projeto, produto, BibTeX copiável, JSON-LD **individual** de `ScholarlyArticle`/`Thesis`/`SoftwareSourceCode`.
  3. `layouts/publications/list.html` para o índice geral e para cada sub-tipo — filtros preservados (ano, tema).
  4. Redirects (aliases) das URLs antigas.
- **Verificação:** `scripts/build_publications.py --check` garante sincronização com `data/productions.yaml`; cada publicação tem URL própria (`curl -I` retorna 200); sitemap cresce proporcionalmente; Pagefind indexa individualmente; menu "Publicações" leva a cada sub-listagem.
- **Arquivos:** `scripts/build_publications.py`, `layouts/publications/`, `content/publications/` (gerado).

### I09 — Oportunidades estruturadas + trilhas "Participe" (ajuste v2) ✅
- **Prioridade:** alta · **Esforço:** M · **Depende de:** I02
- **Ajuste v2:** o antigo "Oportunidades" passa a ser **um dos itens do menu "Participe"** (I13). Trilhas por público (IC/TCC/Mestrado/Doutorado/Extensão/Parcerias/Proponha) já existem parcialmente em `content/junte-se/` — devem ser formalizadas e alinhadas.
- **Entregáveis:**
  1. Nova seção `content/opportunities/` com *front matter* `status: (open|closed|expired)`, `deadline`, `audience: [tcc|iniciacao|mestrado|doutorado|voluntario|parceria]`, `project`, `responsible`.
  2. `layouts/opportunities/list.html` com filtros por situação e público, ocultação automática de expiradas (mantidas para SEO com `noindex`).
  3. Reorganizar `content/junte-se/` em trilhas explícitas: `iniciacao-cientifica`, `tcc`, `mestrado`, `doutorado`, `extensao`, `parcerias`, `proponha-projeto` — cada uma com sua página.
  4. Migrar chamadas de 2025 anteriores para arquivadas.
- **Verificação:** ao mudar `deadline` para uma data passada, a oportunidade some da listagem principal sem editar `status` manualmente; menu "Participe" (I13) leva a cada trilha.
- **Arquivos:** `content/opportunities/`, `content/junte-se/*/`, `layouts/opportunities/`, `layouts/_default/list.html`.

### I14 — Notícias como camada transversal ✅
- **Prioridade:** alta · **Esforço:** M · **Depende de:** I03
- **Contexto:** como Notícias saiu do menu principal, sua descobribilidade agora depende de: (a) destaque na home ✅ (já entregue), (b) blocos "notícias relacionadas" em páginas de projeto/produto/pesquisador, (c) arquivo completo em `/categories/news/` linkado do rodapé ✅ (já entregue via I15).
- **Entregáveis:**
  1. Partial `layouts/partials/related-news.html` que recebe um `id` (de pesquisador, projeto ou produto) e renderiza até 5 notícias que citam esse `id` via `tags`, `categories` ou campo estruturado em `posts` frontmatter (a ser padronizado em I02).
  2. Chamar o partial em `layouts/projects/single.html`, `layouts/products/single.html` e `layouts/people/single.html` — em bloco "Últimas notícias sobre X" ao final da página.
  3. Adicionar campo `related_ids: [proj_x, prod_y, person_z]` no *front matter* das notícias (I02 já validará).
  4. Fallback silencioso: se não há notícias relacionadas, o bloco é omitido.
- **Verificação:** amostragem — em `content/products/contextus.pt.md`, o bloco de notícias deve mostrar Contextus lançamento, registro INPI, produtos derivados; em `content/people/sergio_freitas.pt.md`, ver as notícias que o citam.
- **Arquivos:** `layouts/partials/related-news.html`, `layouts/projects/single.html`, `layouts/products/single.html`, `layouts/people/single.html`, `content/posts/*.md` (adição de `related_ids`).

### I08 — Paridade PT/EN ✅
- **Prioridade:** alta · **Esforço:** M · **Depende de:** *front matter* padronizado (I02)
- **Entregáveis:**
  1. Toda página institucional obrigatória (lista em `CONVENTIONS.md`) declara `translationKey`.
  2. `scripts/validate_i18n.py` (evoluir o existente): reporta pares faltantes, campos divergentes (`title`, `description`, `featured_image`, `status`), links internos que apontam para o idioma errado.
  3. Job `i18n` no CI que falha com PR-comment listando as lacunas.
- **Verificação:** relatório de lacunas gerado como artefato do CI a cada PR.
- **Arquivos:** `scripts/validate_i18n.py`, `.github/workflows/site-ci.yml`, `CONVENTIONS.md`.

---

## Fase 5 — Qualidade e política

### I10 — Acessibilidade e desempenho contínuos
- **Prioridade:** alta · **Esforço:** M · **Depende de:** I01
- **Entregáveis:**
  1. `pa11y-ci` configurado com URLs críticas cobrindo **os 6 itens do novo menu** (home, `/about/`, `/pt/history/`, `/categories/knowledge_areas/`, `/projects/`, `/products/`, uma página de pesquisador, uma de projeto, uma de produto, uma de publicação individual, `/oportunidades/`, `/categories/news/`).
  2. `lighthouserc.json` com orçamentos de performance (LCP < 2.5s, CLS < 0.1, INP monitorado) e categorias mínimas (perf ≥ 80, a11y ≥ 90, SEO ≥ 90, best practices ≥ 90).
  3. Job no CI executando ambos após o build; violações graves bloqueiam PR; relatórios anexados como artefato.
- **Verificação:** PR de teste com regressão de contraste falha; painel histórico visível.
- **Arquivos:** `lighthouserc.json`, `.pa11yci.json`, `.github/workflows/site-ci.yml`.

### I12 — Privacidade e uso do Analytics
- **Prioridade:** alta · **Esforço:** M · **Depende de:** orientação institucional UnB/LGPD
- **Entregáveis:**
  1. Página de política de privacidade em `content/privacy/` cobrindo finalidade, retenção, controlador, contato do encarregado.
  2. Ativar `privacy.googleAnalytics.respectDoNotTrack: true` em `hugo.yaml`.
  3. Decisão registrada em `docs-src/privacy-decisions.md`: se GA é carregado antes ou depois de consentimento, se GPC é honrado, se há banner.
  4. Inventário de formulários e integrações externas com dado pessoal.
- **Verificação:** requests do GA não saem quando `DNT: 1` ou `Sec-GPC: 1` estão presentes; página de privacidade indexada e linkada no rodapé (I15).
- **Arquivos:** `hugo.yaml`, `content/privacy/`, `layouts/partials/footer.html`, `docs-src/privacy-decisions.md`.

---

## Riscos e mitigações (revisado v2)

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Reestruturação do menu (I13) quebra bookmarks/analytics | Alta | Médio | Aliases Hugo para todas as URLs antigas; anúncio no rodapé/newsletter; monitoramento de 404s por 30 dias. |
| Placeholders de I16 ficam "vazios" por meses | Média | Médio | Definir conteúdo mínimo aceitável para publicar cada página (checklist em `CONVENTIONS.md`); calendário de preenchimento. |
| Migração de `data/projects.yaml` (I03) quebra páginas dependentes | Média | Alto | Manter YAML gerado até que todos os consumers migrem; snapshot HTML antes/depois. |
| Publicações individuais (I07) explodem o build | Média | Médio | Medir tempo antes/depois; se > 30s, ativar cache Hugo modules. |
| CI passa a bloquear editores não-técnicos | Alta | Médio | Documentar regras no README; mensagens amigáveis; escalonar rigor (warnings → erros) em 2 sprints. |
| Decisão de privacidade (I12) depende de orientação institucional lenta | Média | Baixo | Enviar minuta ao encarregado LGPD da UnB no início da Fase 5; enquanto isso, ativar `respectDoNotTrack`. |
| Regressão de SEO ao mover publicações (I07) | Média | Alto | Aliases + submeter novo sitemap ao Search Console; monitorar 30 dias. |
| Sub-menu "Publicações → Zenodo/Didático" sem conteúdo suficiente | Média | Baixo | Aceitar página "em construção" com CTA de contato; priorizar preenchimento em Fase 4. |

---

## Governança do plano

- **Cadência de revisão:** quinzenal a partir da Fase 2.
- **Kanban:** cada issue vira uma issue do GitHub com label `audit-2026` e label da fase (`phase-2` … `phase-5`).
- **Definition of done:** issue só fecha com PR mergeado, CI verde e verificação registrada na descrição.
- **Métricas mensais:**
  - % de issues concluídas por fase,
  - tempo médio de build no CI (regressão > 20% ⇒ investigar),
  - número de referências quebradas detectadas pelo validador,
  - lacunas PT/EN em páginas obrigatórias (meta: 0 após I08),
  - score médio Lighthouse a11y/perf (meta: ≥ 90 / ≥ 80),
  - **404s em URLs antigas do menu** (meta: 0 após 60 dias de aliases).

## Critérios de sucesso do plano (v2)

O plano é bem-sucedido quando:

1. **Menu de 6 itens vivo em PT e EN**, com todos os sub-itens resolvendo 200 (I13).
2. **Rodapé enriquecido** com Notícias/Contato/Divulgação científica/Zenodo/GitHub/LinkedIn/YouTube/Intranet/Privacidade/Acessibilidade presentes e funcionais (I15).
3. **Páginas institucionais estruturantes** existentes com conteúdo mínimo (I16).
4. **Zero fonte-de-verdade duplicada:** relações entre pessoas, projetos, produtos e publicações declaradas em um único lugar (I03, I07).
5. **CI protege o `main`:** nenhum PR entra sem build verde, links válidos, dados validados, i18n conferido e a11y sem regressão grave (I01✅, I02, I08, I10).
6. **Cada publicação tem URL própria** e JSON-LD individual, com sub-listagens por tipo (I07).
7. **Oportunidades expiram sozinhas**; trilhas "Participe" formalizadas por público (I09).
8. **Blocos de notícias relacionadas** em páginas de projeto/produto/pesquisador (I14).
9. **README** permite onboarding em < 30 min (I11 ✅).
10. **Política de privacidade publicada** e GA respeita DNT/GPC (I12).
11. **Nenhuma referência a FGA, `Cibersecurity`, ou arquivos `*-old*`** no repositório (I04 ✅, I05 ✅).

---

## Anexo A — Mapa rápido issue ↔ arquivos

| Issue | Status | Arquivos-chave |
|---|---|---|
| I01 | ✅ | `.github/workflows/site-ci.yml`, `package.json`, `lychee.toml` |
| I02 | ✅ | `schemas/`, `scripts/validate_content.py`, `docs-src/data-model.md`, `.github/workflows/site-ci.yml` |
| I03 | ✅ | `content/projects/`, `content/products/`, `layouts/people/single.html`, `layouts/projects/single.html`, `layouts/products/single.html`, `CONVENTIONS.md` |
| I04 | ✅ | `content/projects/DFCris.*.md`, `content/areas/security.*.md`, assets renomeados |
| I05 | ✅ | `data/*.yaml` (removidos) |
| I06 | ✅ | `layouts/partials/meta.html`, `layouts/robots.txt` |
| I07 | ✅ | `scripts/build_publications.py`, `layouts/publications/`, `content/publications/` |
| I08 | ✅ | `scripts/validate_i18n.py`, `.github/workflows/site-ci.yml` |
| I09 | ✅ | `content/opportunities/`, `content/junte-se/*/`, `layouts/opportunities/` |
| I10 | ✅ | `lighthouserc.json`, `.pa11yci.json`, `.github/workflows/site-ci.yml` |
| I11 | ✅ | `README.md`, `package.json`, `.tool-versions` |
| I12 | ✅ | `hugo.yaml`, `content/privacy/`, `layouts/partials/head.html`, `docs-src/privacy-decisions.md` |
| **I13** | ✅ | `hugo.yaml`, `layouts/partials/nav.html`, `i18n/*.yaml` |
| **I14** | ✅ | `layouts/partials/related-news.html`, `layouts/{projects,products,people}/single.html` |
| **I15** | ✅ | `layouts/partials/footer.html`, `i18n/*.yaml` |
| **I16** | ✅ | `content/reconhecimentos/`, `content/infra/`, `content/indicadores/`, `content/contact/`, `content/divulgacao-cientifica.*.md`, `content/privacy/`, `content/accessibility/` |
