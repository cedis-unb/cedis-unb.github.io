# Pesquisadores colaboradores, co-orientações do AgroMart e página do projeto — design

- **Data**: 2026-10-09
- **Decisões**: Sergio Freitas · **Redação**: Claude Code
- **Local do spec**: `docs-src/specs/` — `docs/` é o `publishDir` do Hugo e é
  apagado por `hugo --cleanDestinationDir`.

## 1. Problema

O portal distingue hoje sete pesquisadores CEDIS (`profile_level: researcher`,
listados em `/categories/researcher/`) de todo o resto da rede humana
(orientandos, alumni, autores externos, em `/people/all/`). Falta uma figura
intermediária: o **pesquisador colaborador** — docente de outra unidade que
co-orienta trabalhos e participa de projetos do centro sem compor o corpo
efetivo.

Dois docentes da Faculdade de Ciências e Tecnologias em Engenharia (FCTE/UnB)
precisam dessa figura:

| Nome completo | Slug | Lattes | Situação atual |
|---|---|---|---|
| Rudi Henri van Els | `rudi_van_els` | `5225196180314173` | inexistente |
| Marília Miranda Forte Gomes | `marilia_miranda` | `9169095482512290` | `profile_level: advisor_only`, `layout: derived` |

A apuração do vínculo do Rudi na Biblioteca Digital da Produção Intelectual
Discente da UnB (BDM) revelou três lacunas adjacentes, que entram no mesmo
trabalho porque compartilham os mesmos arquivos de dados:

1. As quatro co-orientações do Rudi em TCCs do AgroMart não estão registradas.
2. O registro do TCC da Luana Souza Silva Torres tem data errada, coorientador
   ausente e metadados vazios.
3. O oitavo TCC do AgroMart não existe no repositório.
4. O **AgroMart** não tem página de projeto, apesar de oito TCCs registrados.

## 2. Fonte de evidência

Todas as orientações foram extraídas do registro completo de cada item no BDM
(`?show=full`, campos "Orientador(es)" e "Coorientador(es)" do DSpace):

| Handle | Defesa em `data/defesas.yaml` | Data (BDM) | Orientador | Coorientador |
|---|---|---|---|---|
| [10483/30718](https://bdm.unb.br/handle/10483/30718) | `lucas-lucas-2021-05-27` | 2021-05-27 | Lanna | — |
| [10483/33850](https://bdm.unb.br/handle/10483/33850) | `byron-igor-2022-05-09` | 2022-05-09 | Lanna | **van Els** |
| [10483/35945](https://bdm.unb.br/handle/10483/35945) | `andre-pedro-2023-02-14` | 2023-02-14 | Lanna | **van Els** |
| [10483/39189](https://bdm.unb.br/handle/10483/39189) | `felipe-giovanna-2023-07-28` | 2023-07-28 | Lanna | **van Els** |
| [10483/39809](https://bdm.unb.br/handle/10483/39809) | `abner-rafael-2023-12-22` | 2023-12-22 | Lanna | **van Els** |
| [10483/40098](https://bdm.unb.br/handle/10483/40098) | `christian-thiago-2024-09-17` | 2024-09-17 | Lanna | — |
| [10483/43566](https://bdm.unb.br/handle/10483/43566) | `kalebe-murilo-2025-02-25` | 2025-02-25 | Lanna | — |
| [10483/45343](https://bdm.unb.br/handle/10483/45343) | `luana-torres-2025-06-15` | **2025-12-15** | Ramos | **Lanna** |
| [10483/45338](https://bdm.unb.br/handle/10483/45338) | **ausente** | 2025-12-18 | Lanna | — |

O índice dos TCCs vem do perfil público da organização
(`https://github.com/AgroMart`, arquivo `.github/profile/README.md`).

Nota de método: o BDM apresenta cadeia TLS incompleta e falha em clientes com
verificação estrita (Node/WebFetch). `curl` resolve normalmente — a extração foi
feita com `curl` e parsing do `itemDisplayTable` do DSpace 4.2.

## 3. Decisões tomadas

| # | Decisão | Alternativa recusada |
|---|---|---|
| D1 | Novo valor `collaborating_researcher` no eixo `profile_level` | `data/collaborating_researchers.yaml` — duplicaria a pessoa fora de `content/people/`, contra CONVENTIONS.md §1.4 |
| D2 | Cards compactos (sem capa, sem contadores) em seção própria depois do grid dos sete | Lista de linhas; cards com capa em escala reduzida |
| D3 | Cada colaborador mantém página individual, renderizada por `layouts/people/single.html` | Card sem página — quebraria `/people/marilia_miranda/`, já referenciada por publicações e defesas |
| D4 | Campo de frontmatter `affiliation` como eyebrow do card | Derivar do `summary` |
| D5 | AgroMart: `status: ongoing`, `start_date: 2021-05-27`, sem `end_date` | Encerrado em 2025; início em 2020 |
| D6 | Adicionar `andre_lanna` a `data/areas.yaml::social_software.researchers[]` | Deixar a área intacta |
| D7 | A página do projeto cita `https://github.com/AgroMart` | Sem link externo |
| D8 | Renomear a defesa da Luana para `luana-torres-2025-12-15` **com alias** da URL antiga | Manter o id mentindo sobre a data; renomear sem alias |
| D9 | Cadastrar o 8º TCC completo (pessoas, produção, defesa); a notícia jornalística de §3 da CONVENTIONS fica como pendência editorial | Escrever a notícia no mesmo lote; apenas registrar a pendência |
| D10 | Resumos PT/EN escritos a partir do BDM, não copiados: o texto extraído tem artefatos de OCR ("desenvol vida", "o!ering") | Colar o resumo do BDM literalmente |
| D11 | `production_id` dos dois registros novos segue o padrão placeholder dos vizinhos; o vínculo vivo é `defesa_id` em `productions.yaml` (§8.1) | Tratar `production_id` como chave de integridade |

## 4. Parte A — a figura do pesquisador colaborador

### 4.1 Modelo de dados

Fonte canônica continua `content/people/<slug>.{pt,en}.md`:

```yaml
author: CEDIS
title: Rudi Henri van Els
profile_level: collaborating_researcher
affiliation: "Professor Associado · FCTE/UnB"
slug: rudi_van_els
language: pt
summary: "…uma a duas linhas…"
authorimage: ../assets/images/global/author.webp
contact:
  email: rudi@unb.br
  lattes: http://lattes.cnpq.br/5225196180314173
```

Sem `categories:` e sem `layout:`. Consequências:

- Não entram no grid dos sete, que `posts-template.html` monta a partir das
  páginas do termo `categories/researcher`.
- Não aparecem em `/categories/people/`.
- O perfil cai em `layouts/people/single.html`, que já atende perfis
  não-docentes (`card_with_page`) e distingue `$isResearcher` nos rótulos.
- `content/people/` não é validado contra schema
  (`validate_content_section` só cobre `projects` e `products`), logo
  `affiliation` não exige mudança de schema.

`affiliation` é rótulo puro, por idioma (PT "Professor Associado · FCTE/UnB";
EN "Associate Professor · FCTE/UnB"). Não colide com a chave `affiliation` do
JSON-LD de `layouts/people/single.html:573`, que é literal fixa da UnB.

### 4.2 Os dois registros

**`rudi_van_els`** — criar `.pt.md` e `.en.md`. Professor Associado da FCTE/UnB
no curso de Engenharia de Energia; graduação em Engenharia Elétrica (UFMA,
1990), mestrado em Engenharia Elétrica (UnB), doutorado pelo Centro de
Desenvolvimento Sustentável da UnB (2008); pesquisa em energia renovável,
eletrificação rural e mobilidade elétrica. Vínculo com o CEDIS: mentor do
AgroMart junto com André Lanna e coorientador de quatro TCCs do projeto
(§2). Sem `areas`: as áreas próprias dele não existem em `data/areas.yaml` e
inventar pills geraria links `/tags/` vazios.

**`marilia_miranda`** — editar os dois arquivos existentes: `profile_level` de
`advisor_only` para `collaborating_researcher`, remover `layout: derived`,
remover `matched_productions: []`, acrescentar `affiliation`, substituir o corpo
derivado por corpo real. Professora Associada da FCTE/UnB; graduação em
Estatística (UnB, 2005), mestrado (2008) e doutorado (2011) em Demografia pelo
Cedeplar/UFMG; docente permanente do PPGEB e do PPGDSCI. Co-orienta trabalhos do
CEDIS sobre envelhecimento populacional, letramento digital e serviços públicos
digitais. `areas: [digital_transformation, software_quality]` — ambas com
evidência em `data/productions.yaml`.

A migração corrige um defeito visível: com `layout: derived` e
`matched_productions: []`, `/people/marilia_miranda/` exibe hoje o selo âmbar
"Perfil derivado automaticamente" e a frase "Coautor(a) citado(a) em **0
produções** do CEDIS", o que é falso — ela é coorientadora em
`data/defesas.yaml` e coautora em `data/productions.yaml`.

### 4.3 Renderização

Novo partial `layouts/partials/collaborating-researchers.html`:

- Lê `partialCached "people-index" "global"`; filtra
  `profile_level == "collaborating_researcher"`; ordena por nome.
- Devolve vazio se não houver ninguém (a seção inteira desaparece).
- Emite cabeçalho (título + intro) e grid de cards compactos. Cada card:
  `affiliation` como eyebrow, nome ligado ao perfil, `summary`, pills de área
  quando `areas` existir, rodapé com "Perfil individual →" e
  "Currículo Lattes ↗".
- Vocabulário visual da página: `rounded-4xl`, `border-black/5`, `bg-white`,
  `shadow-panel`, par `dark:` para cada cor. Sem `data-randomize-card` — ordem
  alfabética estável.

Em `layouts/_default/list.html`, depois de `{{ partial "posts-template.html" . }}`:

```go-html-template
{{ if and $isResearchersList (eq $currentPage $totalPages) }}
  {{ partial "collaborating-researchers.html" . }}
{{ end }}
```

As três variáveis já existem no template. A guarda de última página mantém a
posição "depois dos pesquisadores" caso o termo passe de
`pagination.pagerSize: 12` (hoje são sete).

Novas chaves em `i18n/pt.yaml` e `i18n/en.yaml`:

| Chave | PT | EN |
|---|---|---|
| `ui_collaborating_researchers` | Pesquisadores colaboradores | Collaborating researchers |
| `ui_collaborating_researchers_intro` | Pesquisadores de outros laboratórios que participam das atividades do CEDIS. | Researchers from other labs who take part in CEDIS activities. |

`people_lattes` e `ui_individual_profile` já existem e são reaproveitadas.

## 5. Parte B — co-orientações do Rudi nos dados

Quatro defesas, oito orientandos (§2):

| `data/defesas.yaml` `id` | Orientandos |
|---|---|
| `byron-igor-2022-05-09` | `byron_kamal_barreto_correa`, `igor_guimaraes_veludo` |
| `andre-pedro-2023-02-14` | `andre_aben_athar_de_freitas`, `pedro_vitor_de_salles_cella` |
| `felipe-giovanna-2023-07-28` | `felipe_boccardi_silva_agustini`, `giovanna_borges_bottino` |
| `abner-rafael-2023-12-22` | `abner_filipe_cunha_ribeiro`, `rafael_leao_teixeira_de_magalhaes` |

Edições:

1. `data/defesas.yaml` — `co_advisors: [rudi_van_els]` nas quatro defesas
   (hoje todas com o campo em `null`).
2. `data/productions.yaml` — `advisors: [andre_lanna, rudi_van_els]` nas quatro
   produções correspondentes.
3. `data/people.yaml` — `advisors: [andre_lanna, rudi_van_els]` nas oito
   entradas de orientandos. O arquivo não usa `co_advisors` (zero ocorrências) e
   já tem 31 entradas com dois nomes em `advisors[]`: é o padrão vigente.

Não é preciso regenerar `content/defesas/`:
`scripts/build_defesas.py::_frontmatter` emite frontmatter mínimo (sem
`advisor`, `co_advisors` ou `project`) e `layouts/partials/defesa-body.html` lê
`site.Data.defesas` em tempo de render. `content/publications/` **precisa** ser
regenerado, porque `build_publications.py` grava `advisors` no frontmatter.

## 6. Parte C — correções apuradas no BDM

### 6.1 TCC da Luana Souza Silva Torres

Registro atual (`luana-torres-2025-06-15`) com quatro defeitos. Correções:

| Campo | De | Para |
|---|---|---|
| `id` | `luana-torres-2025-06-15` | `luana-torres-2025-12-15` |
| `scheduled_date` / `held_date` | `2025-06-15` | `2025-12-15` |
| `date_approximate` | `true` | `false` |
| `co_advisors` | `null` | `[andre_lanna]` |
| `title.pt` | "…: a experiência do Agromart" | "…: a experiência Agromart" |
| `production_id` | — | inalterado (vestigial, §8.1) |

`advisor` permanece `cristiane_ramos` — o BDM confirma "Orientador(es): Ramos,
Cristiane Soares". Em `data/productions.yaml`, o mesmo item recebe
`url: https://bdm.unb.br/handle/10483/45343`, `pages: '76'`,
`co_advisors`/`advisors` com `andre_lanna` acrescentado, `title.pt` corrigido e
**`defesa_id: luana-torres-2025-12-15`** — este último é o vínculo que de fato
liga defesa e publicação (§8.1), e é obrigatório atualizá-lo junto com a
renomeação do `id`.

O corte de 90 caracteres de `ascii_slug` (`build_publications.py:301`, que gera
o nome do arquivo em `content/publications/`) faz o slug terminar em `-a-ex`
tanto com "do Agromart" quanto com "Agromart", então a correção do título **não**
renomeia
`content/publications/tcc/2025/2025-luana-souza-silva-torres-…-a-ex.{pt,en}.md`.

**Alias da URL antiga** (D8). `scripts/build_defesas.py::_aliases_for` devolve
hoje `[]` por decisão do Sprint 5 do PLANO-DEFESAS-2026. Implementação:

- Novo campo opcional `legacy_ids: [str]` em `data/defesas.yaml`, com
  `luana-torres-2025-06-15` na entrada renomeada. O schema tem
  `additionalProperties: true`; acrescentar a propriedade a
  `schemas/defesa.schema.json` para documentá-la.
- `_aliases_for` passa a emitir `/defesas/<legacy_id>/` para cada item de
  `legacy_ids`, mantendo o retorno vazio quando o campo não existir — a decisão
  do Sprint 5 sobre os posts legados fica intacta.
- Regenerar `content/defesas/` com `python3 scripts/build_defesas.py`.

### 6.2 Oitavo TCC — Redesign responsivo

"Redesign responsivo da interface web do Agromart: uma proposta de
acessibilidade digital para agricultores" — Guilherme Nishimura da Silva e
Matheus Costa Gomes; orientador André Lanna, sem coorientador; apresentado em
2025-12-18; 91 f.; handle [10483/45338](https://bdm.unb.br/handle/10483/45338).
Substitui a camada de apresentação do CMS Strapi por uma interface desacoplada
em Vue.js consumindo a API REST, com foco em responsividade e acessibilidade
para agricultores.

Cadastro em quatro lugares:

1. `data/people.yaml` — duas entradas novas, slugs
   `guilherme_nishimura_da_silva` e `matheus_costa_gomes` (padrão nome completo
   em snake_case sem acentos, como as 13 entradas de orientandos do AgroMart já
   existentes). `categories: [people, tcc]`,
   `advisors: [andre_lanna]`, `year: 2025`, `program: curso_esw`,
   `tags: [inactive, software_quality, social_software, project_agromart]`,
   `title` PT/EN.
2. `data/productions.yaml` — item novo, `type: tcc`, `year: 2025`,
   `program: curso_esw`, `advisors: [andre_lanna]`,
   `authors: [Guilherme Nishimura da Silva, Matheus Costa Gomes]`,
   `url: https://bdm.unb.br/handle/10483/45338`, `pages: '91'`,
   `publisher: Biblioteca Central da Universidade de Brasília`,
   `tags: [software_quality, social_software, project_agromart]`,
   `defesa_id: guilherme-matheus-2025-12-18`.
3. `data/defesas.yaml` — entrada nova. `id: guilherme-matheus-2025-12-18`
   (regra de `scripts/gen_defesa_slug.py` para dupla: primeiro nome de cada
   aluno + data), `type: tcc`, `program: curso_esw`,
   `scheduled_date`/`held_date` `2025-12-18`, `advisor: andre_lanna`,
   `co_advisors: null`, `committee: []`, `project: project_agromart`,
   `production_id: 2025-guilherme-nishimura-redesign-responsivo-da-interface-web-do`,
   `news_slug: null`, `date_approximate: false`.
4. `content/publications/` — regenerado por `build_publications.py`.

O `production_id` acima segue a regra de
`scripts/migrate_defesas.py::_extract_production_slug` (`<ano>-<dois primeiros
tokens do primeiro autor>-<seis primeiras palavras do título>`), que é a regra
usada pelos 154 valores já presentes no arquivo — verificada reproduzindo o
valor da entrada da Luana. O vínculo funcional é `defesa_id` no item de
`productions.yaml` (§8.1).

Área escolhida: `software_quality` (acessibilidade e usabilidade como qualidade
de produto) e `social_software`. Os assuntos do BDM ("Acessibilidade digital",
"Design responsivo", "Usabilidade (Computação)", "Agricultores") não têm
correspondente direto em `data/areas.yaml`.

## 7. Parte D — página de projeto do AgroMart

### 7.1 `data/projects.yaml`

```yaml
  - id: project_agromart
    name:
      en: "AgroMart"
      pt: "AgroMart"
    project_type: project
    status: ongoing
    start_date: 2021-05-27
    researchers:
      - andre_lanna
      - rudi_van_els
    students: [ … 17 slugs … ]
```

Os 17 orientandos, por defesa: `lucas_pereira_de_andrade_macedo`,
`lucas_siqueira_rodrigues` (2021); `byron_kamal_barreto_correa`,
`igor_guimaraes_veludo` (2022); `andre_aben_athar_de_freitas`,
`pedro_vitor_de_salles_cella`, `felipe_boccardi_silva_agustini`,
`giovanna_borges_bottino`, `abner_filipe_cunha_ribeiro`,
`rafael_leao_teixeira_de_magalhaes` (2023); `christian_fleury_alencar_siqueira`,
`thiago_siqueira_gomes` (2024); `kalebe_lopes_da_cunha`,
`murilo_schiler_lopes_santana`, `luana_souza_silva_torres`,
`guilherme_nishimura_da_silva`, `matheus_costa_gomes` (2025).

`validate_data_projects` confere `researchers[]` contra `person_ids`
(`content/people/` ∪ `data/people.yaml`): `rudi_van_els` só passa a ser válido
depois da Parte A — a ordem de implementação (§10) depende disso.
`students[]` não é xref-validado.

### 7.2 `content/projects/agromart.{pt,en}.md`

Frontmatter conforme `schemas/project.schema.json` (obrigatórios: `title`,
`date`, `language`, `summary`, `id`, `status`, `researchers`, `areas`,
`partners`, `funding_agencies`, `products`, `publications`):

```yaml
id: project_agromart
status: ongoing
start_date: 2021-05-27
researchers: [andre_lanna, rudi_van_els]
areas: [social_software, digital_transformation, software_architecture]
partners: []
funding_agencies: []
products: []
publications: []
categories: [project, andre_lanna, rudi_van_els, project_agromart]
tags: [social_software, digital_transformation, software_architecture, project_agromart]
```

`categories[]` com os slugs das pessoas segue o padrão de
`content/projects/doarti.pt.md` e alimenta o fallback de `$memberIDs` em
`layouts/projects/single.html`. Isso cria o termo `/categories/rudi_van_els/`,
como já ocorre para os sete pesquisadores — é a taxonomia do **projeto**, não do
perfil, e não contradiz §4.1.

Sem `featured_image`: três projetos já existem sem ela
(`laboratorio_fabrica_software`, `nimbus`, `melhoria_servico_publico_digital`).

Corpo no padrão de `content/projects/doarti.pt.md`: visão geral (plataforma para
Comunidades que Sustentam a Agricultura, nascida de um hackathon em 2020 e
evoluída em TCCs sucessivos da FCTE/UnB desde 2021), equipe (Lanna e Rudi como
mentores, via `link-interno`), repositório público `https://github.com/AgroMart`.
`publications[]` fica vazio: a lista sai da relação inversa de §7.3.

### 7.3 Relações inversas

- `data/productions.yaml`: acrescentar `project_agromart` a `tags[]` nas nove
  produções do AgroMart (as oito atuais mais a de §6.2).
  `layouts/projects/single.html:311` casa publicação com projeto quando
  `tags[]` ou `categories[]` contém o id do projeto — mecanismo que o Doarti já
  usa. Depois, regenerar `content/publications/`.
- `data/defesas.yaml`: `project: project_agromart` nas nove defesas. O campo já
  existe no arquivo (usado por 18 defesas de outros projetos) e aparece na
  página da defesa via `layouts/partials/defesa-body.html:167`.

### 7.4 Linha de pesquisa e área

- `data/research_lines.yaml::line_digital_transformation.projects[]` recebe
  `project_agromart`. A linha é "Sistemas sociotécnicos e transformação digital"
  (`slug: sociotechnical-systems`) e já declara `social_software` e
  `digital_transformation` entre suas áreas. Rodar depois
  `python3 scripts/build_research_lines.py`.
- `data/areas.yaml::social_software.researchers[]` recebe `andre_lanna` (D6).
- `rudi_van_els` **não** entra em `research_lines.yaml::researchers[]` nem em
  `areas.yaml::researchers[]`: ambos exigem `profile_level: researcher` e os
  vínculos ali são declarados explicitamente por Sergio. Ele aparece como
  pesquisador do projeto e como coorientador das defesas.

## 8. Ajustes de borda

- `scripts/validate_content.py::collect_advisor_page_ids` aceita hoje apenas
  `{"researcher", "advisor_only"}`. Acrescentar `"collaborating_researcher"`.
  Sem isso, `marilia_miranda` e `rudi_van_els` deixam de ser advisors válidos e
  surgem avisos de xref em `defesas.yaml`, `productions.yaml` e `people.yaml`.
- `schemas/defesa.schema.json`: documentar `legacy_ids` (§6.1).
- `CONVENTIONS.md` §1.3: a lista de advisors externos cita `marilia_miranda`
  como `advisor_only` — atualizar e documentar o nível novo com a tabela dos
  dois colaboradores. §1.4: acrescentar `collaborating_researcher` à enumeração
  de `profile_level`.
- `docs-src/data-model.md`: documentar o nível, `affiliation` e `legacy_ids`.
- Efeito colateral aceito: o chip "rede ativa" em `/people/all/` sobe, porque
  `peopleCount status="active"` conta quem tem página sem a tag `inactive` e o
  Rudi passa a ter página. Sem chip próprio de colaboradores nessa página — é
  escopo separado.

### 8.1 Como defesa e publicação se ligam (apuração)

`layouts/partials/defesa-body.html:251-269` resolve o link "trabalho
depositado" por dois caminhos:

1. `$matchesDefense` — `productions.yaml::items[].defesa_id == defesa.id`.
2. `$matchesProduction` — `productions.yaml::items[].slug == defesa.production_id`.

Estado real, medido: **154 de 154** defesas com `production_id` resolvem pelo
caminho 1. O caminho 2 nunca dispara, porque **nenhum** dos 350 itens de
`productions.yaml` tem campo `slug`. Não há link quebrado.

Consequências para este trabalho:

- O campo que importa ao criar ou renomear uma defesa é **`defesa_id` no item de
  `productions.yaml`**, não `production_id` em `defesas.yaml`.
- `production_id` é vestigial: `scripts/migrate_defesas.py::_extract_production_slug`
  documenta no próprio docstring que grava um placeholder e que "o script real do
  sprint seguinte substitui pelo slug estável de build_publications" — sprint que
  não aconteceu. Os valores não correspondem aos slugs de
  `build_publications.py:301` e não precisam corresponder.
- O fallback `/publications/#<production_id>` (linha 251) também é inócuo: a
  lista de publicações só emite âncoras de ano
  (`layouts/_default/publications.html:301`). É sempre sobrescrito pelo
  caminho 1.
- `layouts/partials/defesa-state.html` apenas testa se `production_id` é
  não-vazio, o que continua verdadeiro.

### 8.2 `advisor_level` (acrescentado na implementação)

A lista de níveis que contam como orientador estava replicada em seis
templates como `researcher or advisor_only`: `_default/map.html`,
`_default/quiz.html`, `_default/publications.html` (dois pontos),
`partials/home-topic-stats.html` e `shortcodes/publications.html`. Nenhum teste
cobre essa duplicação, então `collaborating_researcher` nasceria ausente dos
seis. `people-index` passou a expor `advisor_level` e os seis consumidores
testam o campo. `partials/posts-template.html:93` ficou de fora de propósito —
ali a pergunta é "quem é o sujeito deste card", não "quem pode orientar".

### 8.3 Código morto remanescente

Limpeza possível, **fora deste escopo** (sem efeito visível):
remover o ramo `$matchesProduction` do partial ou implementar `slug` em
`productions.yaml`; e decidir se `production_id` deve ser aposentado em favor de
`defesa_id`. Merece spec próprio.

## 9. Pendências registradas

1. **Notícia jornalística do 8º TCC** — CONVENTIONS.md §3 pede
   `content/posts/defesa-*.{pt,en}.md` para toda defesa com data ≥ 2015. O
   cadastro de §6.2 entra sem a notícia, por decisão D9.
1b. **`co_advisors` não é exibido na página da defesa.**
   `layouts/partials/defesa-body.html` mostra a banca a partir de
   `committee[]` (papéis `advisor`, `co_advisor`, …) e o orientador no
   parágrafo-notícia, mas nunca lê o campo `co_advisors`. Com `committee: []`,
   as co-orientações agora registradas não aparecem em `/defesas/<id>/` —
   aparecem em `/publications/`, no perfil do coorientador e nos contadores.
   Alcança as 158 defesas do arquivo, não só as cinco tocadas aqui, e merece
   decisão própria: exibir `co_advisors` no parágrafo-notícia ou preencher
   `committee[]`.
2. **Aposentar ou implementar `production_id` / `$matchesProduction`** — §8.1.
3. **Áreas próprias do Rudi** (energia renovável, eletrificação rural,
   mobilidade elétrica) não existem em `data/areas.yaml`. Exibi-las como pills
   exigiria criar área nova; decisão editorial pendente.
4. **Marília no mapa e no quiz** — ao declarar `areas`, ela passou a aparecer
   em `/map/` e `/quiz/`, como qualquer pessoa de nível `advisor_only` que
   declare áreas. É consequência de `advisor_level` (§8.2), não decisão
   editorial registrada; reverter é remover `areas` do perfil dela.
5. **Normalização de títulos do AgroMart** — `data/defesas.yaml` e
   `data/productions.yaml` usam " - " onde o BDM e `data/people.yaml` usam " : "
   ("Uma evolução do projeto Agromart - open source…"). Divergência
   pré-existente, fora de escopo.
6. **Registro do grupo no DGP/CNPq** — pendência pré-existente de
   `data/research_lines.yaml`, agora com um projeto a mais na linha de
   transformação digital.

## 10. Ordem de implementação

A Parte A precede a D, porque `validate_data_projects` exige que
`rudi_van_els` exista como pessoa antes de ser `researcher` de projeto.

1. **A** — perfis de Rudi e Marília, partial, `list.html`, i18n,
   `collect_advisor_page_ids`.
2. **B** — `co_advisors` nas quatro defesas; `advisors` nas quatro produções e
   nas oito entradas de orientandos.
3. **C** — correção da defesa da Luana (renomeação + `legacy_ids` + alias no
   gerador); cadastro do 8º TCC em `people.yaml`, `productions.yaml` e
   `defesas.yaml`.
4. **D** — `projects.yaml`, páginas do projeto, tags e `project:` nas nove
   produções/defesas, `research_lines.yaml`, `areas.yaml`.
5. Regenerar: `build_publications.py`, `build_defesas.py`,
   `build_research_lines.py`.
6. Documentação: `CONVENTIONS.md`, `docs-src/data-model.md`,
   `schemas/defesa.schema.json`.

## 11. Verificação

- `python3 scripts/build_publications.py`,
  `python3 scripts/build_defesas.py` e
  `python3 scripts/build_research_lines.py` antes dos testes — os modos
  `--check` falham se `content/` estiver dessincronizado dos dados.
- `npm test` — `check:publications`, `check:research-lines`, `check:css`,
  `check:alpine`, `validate_content.py`, `validate_i18n.py`. Sem avisos novos
  de xref.
- `npm run build` e inspeção de `/pt/categories/researcher/`: sete cards
  grandes, seguidos da seção nova com dois cards compactos.
- `/pt/people/marilia_miranda/` sem o selo "Perfil derivado automaticamente".
- `/pt/people/rudi_van_els/` com as quatro co-orientações.
- `/pt/defesas/byron-igor-2022-05-09/` mostrando Rudi como coorientador.
- `/pt/defesas/luana-torres-2025-12-15/` com data 15/12/2025 e Lanna como
  coorientador; `/pt/defesas/luana-torres-2025-06-15/` redirecionando para ela.
- `/pt/defesas/guilherme-matheus-2025-12-18/` existente e com link para a
  publicação.
- `/pt/projects/agromart/` com equipe, nove publicações e link do repositório;
  `/pt/research-lines/sociotechnical-systems/` listando o AgroMart.
- Paridade PT/EN em cada arquivo novo de `content/`.
