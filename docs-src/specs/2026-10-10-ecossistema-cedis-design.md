# Ecossistema CEDIS no portal — design

- **Data**: 2026-10-10
- **Decisões**: Sergio Freitas · **Redação**: Claude Code
- **Fonte**: varredura completa de `~/workspace/github/projects/CEDIS-Deck-Manager`
  (808 commits, 2026-07-06 → 2026-08-29), seus infográficos, `docs/ECOSSISTEMA-CEDIS.md`,
  `docs/marketing-brief.md`, documentação por produto e `CEDIS-identity-suite`.
- **Local do spec**: `docs-src/specs/` — `docs/` é o `publishDir` do Hugo.

## 1. Problema

O portal registra um único produto do ecossistema — o **CEDIS Deck Manager**
(`content/products/deckmanager`, 2026-07-16) — sob o guarda-chuva *Inovação
digital e gamificação*. O repositório, porém, é um monorepo de **seis produtos
em produção**, apresentados ao público como *Ecossistema CEDIS* desde 9 de
agosto de 2026 (infográficos, identity suite v1.2.0 "de cinco para seis
produtos", nascimento do Learning Analytics):

| Produto | Host | Nasce no git | Estado (docs + host no ar em 2026-10-10) |
|---|---|---|---|
| CEDIS Deck Manager | deck.cedis.tec.br | 2026-07-06 | produção; já no portal |
| CEDIS Slides | slides.cedis.tec.br | 2026-07-06 | produção |
| CEDIS Concept Studio + Questionários | concepts.cedis.tec.br | 2026-07-31 | produção; questionários fases 0–9, ativação gradual por feature flag |
| Atlas do Conhecimento | atlas.cedis.tec.br | 2026-08-06 | produção (`docs/atlas/STATUS.md` 2026-08-07) |
| CEDIS Learning Passport | passport.cedis.tec.br | 2026-08-04 | produção; consent bundle imutável, OIDC |
| CEDIS Learning Analytics | analytics.cedis.tec.br | 2026-08-09 | ingest + API + K-anonimato em produção; dashboards docentes em construção |

Paralelamente, o projeto PIBIC *Framework preditivo de engajamento*
(`project_framework_preditivo_engajamento`) teve as bolsas de Davi Rodrigues
da Rocha, Daniel Rodrigues da Rocha e Mylena Angélica Silva Farias encerradas
em outubro de 2026, e Davi e Daniel iniciam um novo PIBIC, em dupla, sobre o
Learning Analytics do ecossistema.

## 2. Fatos que mudaram o pedido

Dois pontos do pedido original não batiam com a evidência e foram decididos
com Sergio em 2026-10-10:

1. **Data.** O pedido era "na mesma data do Deck Manager" (2026-07-16). Em
   16/07 só existiam Deck Manager e Slides; Concept Studio, Passport, Atlas e
   Learning Analytics nascem entre 31/07 e 09/08. **Decisão:** projeto, cinco
   produtos novos e suas notícias levam **2026-08-09**, a data em que a família
   virou seis produtos. O Deck Manager mantém 2026-07-16.
2. **Vínculo com o PIBIC.** O pedido dizia que os produtos "estão vinculados
   ao projeto do Davi e do Daniel". No portal nenhum produto do ecossistema
   aponta para o PIBIC (que lista só EduTrack/EduTrack AI); no repositório os
   três estudantes têm zero ocorrências — 794 commits são de Sergio, 76 da
   conta da organização. **Decisão:** o Ecossistema entra como subprojeto de
   *Inovação digital e gamificação*, onde o Deck Manager já vive; nenhuma
   relação com o PIBIC antigo é inventada. O vínculo com Davi e Daniel passa a
   existir pelo **novo** PIBIC (§6), não pelo antigo.

## 3. Decisões

| # | Decisão | Alternativa recusada |
|---|---|---|
| D1 | Data 2026-08-09 para projeto, produtos novos e notícias | 2026-07-16 (retrodataria quatro produtos); datas reais por produto espalhadas por quatro semanas |
| D2 | `project_ecossistema_cedis` subprojeto de `project_inovacao_digital_gamificacao` | subprojeto do PIBIC antigo; projeto sem guarda-chuva |
| D3 | Deck Manager migra para o Ecossistema; guarda-chuva deixa de listá-lo diretamente | manter o Deck Manager no guarda-chuva e o Ecossistema sem ele |
| D4 | `status: beta` só para `learning_analytics`; `active` para os demais | tudo `active` (escondia que os dashboards não existem) |
| D5 | Seis notícias em 2026-08-09: uma de hub + cinco de produto; Deck Manager fica com a news-027 | só cinco; só o hub |
| D6 | Seis chaves i18n para ids de produto (inclui `deckmanager`, hoje sem rótulo) | deixar o fallback humanizado nas pills |
| D7 | PIBIC *Framework preditivo* fecha: `closed`, `end_date: 2026-10-10`; três estudantes `inactive` | manter o projeto `ongoing` até 2026-12-31 |
| D8 | Novo PIBIC em dupla para Davi e Daniel, ativo, título *Learning Analytics do Ecossistema CEDIS*, orientador `sergio_freitas`, conclusão prevista 2027, vinculado ao Ecossistema | — |
| D9 | Logos dos produtos: variante horizontal 1240×360 da identity suite, copiada como `assets/images/featured/<id>-logo.png` | marca quadrada; recortar como o `deckmanager-logo.png` atual (920×380) |
| D10 | Sem notícia de encerramento do PIBIC antigo | CONVENTIONS §3 só exige notícia para defesas; fica como opcional |

## 4. Parte A — projeto *Ecossistema CEDIS*

### 4.1 `data/projects.yaml`

```yaml
  - id: project_ecossistema_cedis
    name:
      en: "CEDIS Ecosystem"
      pt: "Ecossistema CEDIS"
    project_type: project
    umbrella_projects:
      - project_inovacao_digital_gamificacao
    status: ongoing
    start_date: 2026-08-09
    researchers:
      - sergio_freitas
    students:
      - daniel_rodrigues_da_rocha
      - davi_rodrigues_da_rocha
```

### 4.2 `content/projects/ecossistema_cedis.{pt,en}.md`

Frontmatter conforme `schemas/project.schema.json`: `id`, `status: ongoing`,
`start_date: 2026-08-09`, `date: 2026-08-09T09:00:00-03:00`,
`umbrella_projects`, `researchers: [sergio_freitas]`,
`students` (os dois slugs), `areas: [learning_analytics, active_learning,
digital_transformation, gamification]`, `partners: []`, `funding_agencies: []`,
`products: [deckmanager, slides, concept_studio, atlas, passport,
learning_analytics]`, `publications: []`,
`featured_image: ../assets/images/featured/project_ecossistema_cedis.png`
(o infográfico geral), `categories: [project, sergio_freitas,
project_ecossistema_cedis, project_inovacao_digital_gamificacao]`, `tags`
com as áreas e os dois ids de projeto.

Corpo, para público externo, com base em `docs/ECOSSISTEMA-CEDIS.md` e nos
infográficos — nenhum número ou funcionalidade fora dessas fontes:

1. **Visão geral** — o que é: seis aplicações web independentes, cada uma com
   subdomínio e banco próprios, conversando por APIs assinadas (HMAC/OIDC);
   nascido em julho de 2026 com o Deck Manager e consolidado como família em
   agosto. Código aberto (MIT) em `github.com/cedis-unb/CEDIS-Deck-Manager`.
2. **A jornada: do conteúdo ao insight** — os sete passos do infográfico
   (docente cria no Deck Manager → aula no Slides → conceitos e questionários
   no Concept Studio → aluno avança no Atlas → aprendizagem registrada no
   Passport → Learning Analytics agrega → docente decide).
3. **Os seis produtos** — um parágrafo cada, com host e `link-interno` para a
   página do produto.
4. **Privacidade em primeiro lugar** — as regras de ouro: identidade
   pseudônima sem e-mail nem PII, sem ranking público, k-anonimato (K=5 no
   Atlas, K=3 no Slides), unlink em cascata, feature flags nascem desligadas,
   falha silenciosa entre serviços.
5. **Estado atual** — cinco produtos em produção; Learning Analytics com
   ingestão, API e K-anonimato no ar e dashboards docentes em construção.
6. **Equipe** — Sergio (coordenação e desenvolvimento) e a dupla do novo PIBIC
   (§6), via `link-interno`.
7. **Material de divulgação** — os três infográficos embutidos (geral,
   docentes, estudantes), copiados para `assets/images/posts/ecossistema-cedis-infografico-{geral,docentes,estudantes}.png`.

### 4.3 Deck Manager migra

`content/products/deckmanager.{pt,en}.md`: `project: project_ecossistema_cedis`;
em `categories[]` e `tags[]`, `project_inovacao_digital_gamificacao` →
`project_ecossistema_cedis`; seção "Vinculação Acadêmica" passa a apontar para
o Ecossistema (e, por ele, ao guarda-chuva). `date` fica 2026-07-16.

`content/projects/inovacao_digital_gamificacao.{pt,en}.md`: remove
`deckmanager` de `products:`; o bullet do corpo que linka o Deck Manager passa
a linkar o projeto Ecossistema CEDIS. O guarda-chuva continua enxergando os
seis produtos por herança (o Ecossistema é seu subprojeto).

## 5. Parte B — cinco produtos e seis notícias

### 5.1 Produtos

`content/products/<id>.{pt,en}.md`, ids `slides`, `concept_studio`, `atlas`,
`passport`, `learning_analytics`. Frontmatter conforme
`schemas/product.schema.json`: `date: 2026-08-09T09:00:00-03:00`,
`product_language: pt`, `project: project_ecossistema_cedis`,
`responsible: [sergio_freitas]`, `publications: []`, `status` (D4),
`featured_image: ../assets/images/featured/<id>-logo.png`,
`categories: [products, sergio_freitas, project_ecossistema_cedis]`,
`tags: [app, <áreas>, project_ecossistema_cedis]`.

| id | título | áreas | status | fonte principal |
|---|---|---|---|---|
| `slides` | CEDIS Slides | active_learning, digital_transformation | active | ECOSSISTEMA §2, README (políticas, `/r/`, `/s/`) |
| `concept_studio` | CEDIS Concept Studio | active_learning, ai, learning_analytics | active | ECOSSISTEMA §4 e §6, `docs/questionnaires/README.md` |
| `atlas` | Atlas do Conhecimento | gamification, learning_analytics | active | ECOSSISTEMA §5, `docs/atlas/PRODUCT-VISION.md`, `STATUS.md` |
| `passport` | CEDIS Learning Passport | digital_transformation, security | active | ECOSSISTEMA §3, `CLAUDE.md` (consent bundle) |
| `learning_analytics` | CEDIS Learning Analytics | learning_analytics, ai, machine_learning | **beta** | `00-executive-summary.md`, `22-roadmap.md`, DISCOVERY |

Corpo no esqueleto da página do Deck Manager: Descrição, Objetivos, Recursos
e Funcionalidades, Vinculação Acadêmica e Apoio (CEDIS, Sergio, projeto
Ecossistema; no `learning_analytics`, também o PIBIC da dupla), Acesso (host).
O `learning_analytics` declara, em texto, o que está no ar e o que não está.

Em EN os nomes de produto são nomes próprios e ficam em português quando
assim foram batizados ("Atlas do Conhecimento", com a glosa *Knowledge
Atlas* na primeira ocorrência).

### 5.2 i18n (D6)

`i18n/{pt,en}.yaml`: `deckmanager`, `slides`, `concept_studio`, `atlas`,
`passport`, `learning_analytics` → nome do produto. Sem isso a pill de tag
mostra o id humanizado ("Learning analytics", "Deckmanager").

### 5.3 Notícias (D5)

Todas em 2026-08-09, `featured_image` = logo do produto (hub: infográfico
geral), `categories: [News]`, `tags: [News, <áreas>, project_ecossistema_cedis,
<id do produto>]`, `related_ids: [<id do produto>, project_ecossistema_cedis,
sergio_freitas]`. Horários escalonados para ordem determinística, hub por
último (listagens ordenam do mais recente):

| nº | assunto | hora |
|---|---|---|
| 035 | hub — "CEDIS apresenta o Ecossistema CEDIS: seis produtos, uma jornada" | 10:00 |
| 036 | CEDIS Slides | 09:00 |
| 037 | CEDIS Concept Studio | 09:10 |
| 038 | Atlas do Conhecimento | 09:20 |
| 039 | CEDIS Learning Passport | 09:30 |
| 040 | CEDIS Learning Analytics | 09:40 |

Corpo ~350 palavras, jornalístico, sem template: cada uma abre com
"Brasília, 9 de agosto de 2026", explica o problema que o produto resolve,
o que ele faz, como se encaixa na jornada, e fecha com o host e um
`link-interno` para o hub. O hub traz os três infográficos.

A notícia fixada (chamamento do Software para o Bem, até 2026-12-31) não é
afetada: estas são dois meses mais antigas.

## 6. Parte C — PIBIC: encerramento e nova dupla

### 6.1 Encerramento (D7)

- `data/people.yaml`: nas entradas 2025 de `scientific_initiation` de
  `davi_rodrigues_da_rocha`, `daniel_rodrigues_da_rocha` e `mylena_faria`,
  `active` → `inactive`.
- `data/projects.yaml::project_framework_preditivo_engajamento` e
  `content/projects/framework_preditivo_engajamento.{pt,en}.md`:
  `status: closed`, `end_date: 2026-10-10`; `students` deixa de usar nomes
  completos e passa a slugs (hoje `layouts/projects/single.html` não
  resolve nomes — os três aparecem sem link); tabela "Equipe" no passado, com
  nota de que as bolsas PIBIC 2025–2026 se encerraram em outubro de 2026.
- `content/people/mylena_faria.{pt,en}.md`: `summary` deixa de dizer
  "orientanda PIBIC no Projeto Canal Ciência" (projeto fechado), tag
  `active` → `inactive`, parágrafo de participação no passado.

### 6.2 Novo PIBIC (D8)

`data/people.yaml`: Davi e Daniel passam ao formato `supervisions[]` (o mesmo
de Mylena), preservando a entrada 2025 (`inactive`) e acrescentando:

```yaml
  - categories: [people, scientific_initiation]
    title:
      pt: "Learning Analytics do Ecossistema CEDIS"
      en: "Learning Analytics for the CEDIS Ecosystem"
    program: curso_esw2
    advisors: [sergio_freitas]
    tags: [active, learning_analytics, ai, machine_learning, project_ecossistema_cedis]
    year: 2027
```

`year` é o ano previsto de conclusão (CONVENTIONS §4.A.1); ciclo PIBIC
2026–2027. A dupla aparece em `/people/all/` como rede ativa, no perfil de
Sergio como orientação atual, e no projeto Ecossistema como estudantes.

## 7. Verificação

- `npm test` (conteúdo + i18n) e `npm run validate:rendered` sem erro nem
  aviso novo; `validate_project_pages` exige que os seis `products:` existam.
- Build local e inspeção: `/pt/projects/ecossistema_cedis/` com seis
  produtos e os três infográficos; `/pt/categories/products/` agrupando os
  seis sob o Ecossistema; `/pt/projects/inovacao_digital_gamificacao/`
  listando o Ecossistema como subprojeto e sem o Deck Manager direto;
  `/pt/categories/news/` com as seis notícias em 09/08 e o chamamento ainda
  fixado; `/pt/projects/framework_preditivo_engajamento/` como concluído e
  com os três estudantes linkados; `/pt/people/sergio_freitas/` com a dupla
  em "Orientações atuais".
- Lychee interno offline sobre `docs/` com 0 erros; os seis hosts
  `*.cedis.tec.br` respondendo.
- Paridade PT/EN de cada arquivo novo.

## 8. Pendências registradas

1. `project_super_r` tem o mesmo defeito de `students` por nome em vez de
   slug — fora de escopo.
2. Notícia de encerramento do PIBIC 2025–2026 (D10) — opcional.
3. Dashboards docentes do Learning Analytics: quando entrarem no ar, trocar
   `status: beta` por `active` e atualizar o parágrafo "Estado atual" do
   projeto e da notícia 040.
4. Página do produto `deckmanager` cita "skill compatível com ChatGPT/Codex";
   o repositório hoje distribui duas variantes (`cedis-deck` e
   `cedis-deck-code`, para Claude Code). Ajuste de uma frase, incluído na
   migração do Deck Manager.
