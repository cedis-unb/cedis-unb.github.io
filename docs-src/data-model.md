# Modelo de dados do site CEDIS

Documento de referência para o modelo de "banco de dados" do portal.
Última revisão: 2026-07-24 (após conclusão dos Gaps #1, #2 e correções Gap #10).

Formaliza as entidades, seus campos obrigatórios, IDs estáveis e enumerações.
Serve de base para os JSON Schemas em `schemas/` e para o validador em
`scripts/validate_content.py`.

## Princípios

1. **Cada entidade tem um `id` (ou `slug`) estável.** Usado em URLs, tags e
   relações. Deve ser `snake_case`, ASCII, sem acentos.
2. **Relações usam `id`/`slug`, nunca nomes por extenso.** Um projeto que
   envolve o Prof. Sergio Freitas registra `researchers: [sergio_freitas]`,
   não `researchers: ["Sergio Antônio Andrade de Freitas"]`.
3. **Relações inversas não são registradas à mão.** Se o projeto declara
   seus pesquisadores, o perfil de cada pesquisador deriva a lista de
   projetos automaticamente via `people-index` e `where site.RegularPages`.
4. **Pares PT/EN existem por `translationKey` ou por convenção de nome de
   arquivo.** No CEDIS a maioria usa `foo.pt.md` + `foo.en.md`; páginas
   institucionais críticas ganham `translationKey` explícito.
5. **Idiomas usam IDs internos estáveis.** O português do site é
   português do Brasil (`locale: pt-BR` em `hugo.yaml`), mas o ID interno
   do Hugo e dos arquivos é `pt` (`*.pt.md`, `language: pt`). Não usar
   `pt-br` como sufixo ou frontmatter.
6. **Enumerações são fechadas.** Status de projeto ∈ {`active`, `ongoing`,
   `closed`}. Tipo de publicação ∈ {`article`, `book`, `book_chapter`,
   `book_section`, `conference`, `dissertation`, `phd`, `registro`,
   `specialization`, `tcc`, `workshop`}. Idioma ∈ {`pt`, `en`}.
   `profile_level` ∈ {`researcher`, `card_with_page`, `card`, `advisor_only`,
   `derived`}.

## Fontes canônicas (estado atual após refactor de julho/2026)

| Arquivo | Papel | Notas |
|---|---|---|
| `data/areas.yaml` | Áreas de atuação com `id`, `name.{pt,en}`, `researchers`. | Consumido via `area-index`/`area-list`/`area-lookup`. |
| `data/projects.yaml` | Projetos com `id`, `name.{pt,en}`, `researchers`, `students`, `products`, `umbrella_projects`, `status`. | Consumido via `project-index`/`project-list`/`project-lookup`. |
| `data/people.yaml` | Orientandos/colaboradores sem página individual. Cada entrada tem `slug` (obrigatório) e opcionalmente `supervisions[]` para múltiplas orientações da mesma pessoa. | Passo 4a-b. |
| `data/productions.yaml` | Publicações com `authors[]` (strings livres), `people[]` (slugs canônicos — Gap #10), `tags[]` (tópicos/projetos), `advisors[]`. | Passo 10 separou pessoas de tags. |
| ~~`data/advisors.yaml`~~ | **REMOVIDO em 2026-07-24 (Gap #1).** Contato e áreas dos advisors agora ficam no frontmatter dos `.md`. | Templates leem via `partial "people-lookup"`. |

## Índice unificado (partial `people-index`)

Fonte lógica única para tudo relacionado a pessoas. Consumidores usam
`partial "people-lookup" $slug` para obter dict com:

```
{
  slug, found, name, profile_level, sources[],
  page, page_url, link,
  advisor (compat, sempre ""),
  data_entry, supervisions[], supervisions_count,
  publications[], publications_count,
  contact{email, lattes, orcid}, areas[]
}
```

O partial `people-index` (cached) é construído a partir de:
1. `content/people/*.md` (fonte autoritativa)
2. `data/people.yaml` (via `slug:` field)

Publicações são pré-indexadas via `.people[]` (canônico) e `.tags[]` (legado
retrocompatível) de productions.

## Entidades

### Pessoa (todas as categorias)

Fonte: `content/people/<slug>.{pt,en}.md`.

Frontmatter obrigatório:
- `title` — nome canônico por extenso.
- `profile_level` — declara o tipo. Valores:
  - `researcher` — docente permanente CEDIS.
  - `card_with_page` — colaborador CEDIS com bio.
  - `advisor_only` — orientador externo (só stub minimal, layout: derived).
  - `derived` — autor externo auto-gerado pelo `scripts/derive_people.py`.
  - (implícito `card` se pessoa está só em `data/people.yaml`)
- Slug da página — inferido do basename do arquivo (`<slug>.pt.md` +
  `<slug>.en.md`). Stubs derivados podem declarar `slug:` no frontmatter,
  mas perfis mantidos manualmente não precisam repetir esse campo.
- `date`, `language` — padrão Hugo.
  Exceção: `date` não é obrigatório para `profile_level: derived` ou
  `profile_level: advisor_only`, pois esses arquivos são stubs técnicos
  derivados de relações/produções, sem data editorial própria.

Frontmatter recomendado (researcher/card_with_page):
- `contact.email`, `contact.lattes`, `contact.orcid` (dict).
- `areas: [<area_id>]` — deriva chips e mapeamento em `/map/`, `/quiz/`.
- `summary` — resumo curto para SEO.
- `categories: [people, <role>]` — role ∈ `researcher | undergraduate | ...`
  para agregação em `/categories/`. **NÃO** incluir o próprio slug em
  `categories` (redundante — o slug já é o nome do arquivo).
- `tags: [<theme_ids>]` — temas de pesquisa (evitar duplicar com areas).

Frontmatter obrigatório para `advisor_only`:
- `layout: derived` — força o template minimal.

Frontmatter obrigatório para `derived`:
- `layout: derived` — força o template minimal.
- `matched_productions: [{title, year, type}]` — pré-computado
  pelo script.
- `aliases_authors: [<name variations>]`.

### Pessoa não-canônica — `data/people.yaml`

Cada item do array:
- `slug` — **obrigatório** (validado pelo `validate_content.py`). Se pessoa
  também tem `.md`, `slug` bate com o basename. Se não tem, é o slug longo
  derivado do nome.
- `name` — obrigatório.
- `categories` — obrigatório; deve incluir `people` + um marcador
  (`phd_candidate`, `master_student`, `tcc`, `specialization`,
  `scientific_initiation`, `volunteer`, `monitor`).
- `advisors` — lista de slugs (referência a pessoas com `profile_level` in
  [`researcher`, `advisor_only`]).
- `year` — ano de referência.
- `program` — código de programa acadêmico.
- `title.{pt,en}` — título do trabalho, ambos idiomas.
- `tags` — inclui `active`/`inactive` + IDs de área/projeto.

Se a pessoa tem múltiplas orientações (ex.: Mylena tem 3), usa-se
`supervisions:` como array dentro da mesma entrada (consolidação do
passo 4b). Nesse caso, campos `categories`, `title`, `program`, `advisors`,
`tags`, `year` ficam DENTRO de cada item de `supervisions[]`.

### Área — `data/areas.yaml` + `content/areas/{id}.{pt,en}.md`

`data/areas.yaml` cada item:
- `id` — obrigatório (usado em tags e categorias).
- `name.{pt,en}` — obrigatório. Consumido pela cascata i18n.
- `researchers` — lista de slugs.

Página em `content/areas/{slug}.{pt,en}.md`:
- `title`, `summary`, `featured_image` — obrigatórios.
- `tags` inclui o próprio `id` da área para SEO e filtragem interna.

### Projeto — `data/projects.yaml` + `content/projects/{id}.{pt,en}.md`

Entrada em `data/projects.yaml`:
- `id` — obrigatório.
- `name.{pt,en}` — obrigatório. Consumido pela cascata i18n.
- `project_type` — `project` | `umbrella` | `platform_project`.
- `umbrella_projects: [<parent_id>]` — se este é filho de outro.
- `status` — `active` | `ongoing` | `closed`.
- `start_date`, `end_date` — ISO 8601.
- `researchers`, `students` — slugs.
- `partners`, `funding_agencies` — strings ou slugs.
- `products` — IDs de produto.

Página opcional em `content/projects/{id}.{pt,en}.md`:
- Frontmatter mínimo (`title`, `date`).
- Body: descrição rica.

### Produto — `content/products/{id}.{pt,en}.md`

Frontmatter obrigatório:
- `title`, `date`, `language`, `summary`.
- `id` — slug do produto.
- `project` — ID do projeto primário.

Frontmatter opcional:
- `secondary_projects: [<project_id>]` — projetos associados.
- `status` — `active` | `prototype` | `archived` | `beta`.
- `areas`, `responsible` — slugs.
- `publications` — IDs de publicações associadas.

### Publicação — `data/productions.yaml`

Fonte canônica: `data/productions.yaml`.

Artefato derivado: `content/publications/**`. Esses arquivos são
reescritos por `scripts/build_publications.py`, versionados apenas para
servir Hugo/SEO/Pagefind e verificados por
`scripts/build_publications.py --check`. Não editar manualmente.

Cada item:
- `type` — enum fechada.
- `year` — inteiro ou string ISO.
- `title.{pt,en}` — obrigatório em ambos idiomas.
- `authors[]` — lista de strings livres (ABNT ou natural).
- `people[]` — **slugs canônicos** de coautores conhecidos (Gap #10).
  Substitui uso de person-slugs em `tags[]`.
- `tags[]` — inclui IDs de área, projeto e status (`active`/`inactive`).
  **NÃO** inclui mais person-slugs (todos migrados para `people[]`).
- `advisors[]` — slugs de orientadores.
- `summary`, `book_title`, `journal_event`, `location`, `pages`,
  `publisher`, `doi_isbn`, `url` — metadados publicação.

Frontmatter obrigatório nas páginas derivadas:
- `generated_by: scripts/build_publications.py`
- `canonical_source: data/productions.yaml`
- `publication_index` — índice do item em `data/productions.yaml`.
- `publication_group`, `publication_type`, `authors_structured`,
  `bibtex`, `external_url`.

## Regras de propagação

### Contagens automáticas — como funcionam

Contadores de publicações por pessoa (`publicationCount` em templates)
sempre fazem `or (in .people $slug) (in .tags $slug)` — retrocompatível.
Templates envolvidos:
- `layouts/people/single.html:131` — perfil individual.
- `layouts/partials/posts-template.html:84` — `/categories/researcher/`.
- `layouts/shortcodes/publications.html`, `npublications.html` — filtros
  por tag também consultam `.people[]`.
- `layouts/partials/people-index.html:68-88` — pré-indexação global.

### Cascata i18n para rótulos (Gap #2)

Todos os pills/badges de tag usam `partial "translated-label.html"` que
faz cascata:
1. `i18n <slug>` — traduções manuais explícitas.
2. `partial "project-lookup" <slug>` → `.name`.
3. `partial "area-lookup" <slug>` → `.name`.
4. `partial "people-lookup" <slug>` → `.name`.
5. `humanize(<slug>)` — última linha de defesa.

Consequência: **projeto novo em `data/projects.yaml` não requer edição de
`i18n/*.yaml` para labels de tag funcionarem**.

## Regras cruzadas (validador)

Verificações executadas por `scripts/validate_content.py`:

1. **IDs de área únicos e resolvem.** Todo ID citado em `areas:` ou como
   tag de área deve existir em `data/areas.yaml`.
2. **IDs de projeto únicos e resolvem.** Idem para `data/projects.yaml`.
3. **Slugs em `data/people.yaml` são obrigatórios.** Cada entrada precisa
   ter `slug:` explícito. Slug deve ser único (ou fazer parte de
   `supervisions[]` da mesma pessoa).
4. **Slugs em `people[]` de productions.yaml resolvem.** Devem existir em
   `content/people/*.md` ou em `data/people.yaml`.
5. **Enumerações válidas.** `type`, `status`, `profile_level`, `program`
   pertencem a conjuntos fechados.
6. **Pares PT/EN.** Toda página em `content/` com `translationKey` deve ter
   contrapartida.
7. **Etiquetas não vazias.** Tags `""` ou `null` são reportadas.
8. **Datas coerentes.** `start_date <= end_date` em projetos; `year` de
   produção é razoável (1990-2030).

## Modo de operação do validador

- `STRICT=false` — não falhar em warnings (default para transição).
- `CEDIS_VALIDATE_STRICT=1` — erros críticos causam exit != 0 (bloqueia PR).
- `CEDIS_VALIDATE_REPORT=<path>` — grava relatório em Markdown adicional.

## Fluxo de adição de novo conteúdo (referência rápida)

Ver `CONVENTIONS.md §7` para checklists práticos.

| Tipo | Arquivos | Validação | Propagação |
|---|---|---|---|
| Publicação | +1 bloco em `productions.yaml` | `people[]` resolvem | Perfis, taxonomias, projetos, contadores |
| Post | 1 `.md` × 2 idiomas | Frontmatter válido | `/news/`, home, tags |
| Orientando (card) | +1 bloco em `people.yaml` com `slug` | Validador | `/people/all/`, perfil orientador, áreas |
| Colaborador com bio | 1 `.md` × 2 idiomas | `profile_level` correto | Perfil + card em `/people/all/` |
| Pesquisador | 1 `.md` × 2 idiomas | `profile_level: researcher` | `/categories/researcher/`, áreas, `/map/`, `/quiz/` |
| Advisor externo | `scripts/create_external_advisor_stubs.py` | (não bate no validador) | Aparece em pills de orientação |
| Coautor citado | `scripts/derive_people.py --apply` | Automático | Bloco 4 do `/people/all/` |
| Projeto | +1 bloco em `projects.yaml` opcional `.md` | ID único | Todas as áreas, pills, cascata i18n |
| Área | +1 bloco em `areas.yaml` opcional `.md` | ID único | Cards, cascata i18n |
