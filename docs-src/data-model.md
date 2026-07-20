# Modelo de dados do site CEDIS

Documento de referência para a issue **I02** do [`PLANO-AUDITORIA-2026.md`](../PLANO-AUDITORIA-2026.md).
Formaliza as entidades, seus campos obrigatórios, IDs estáveis e enumerações. Serve de base para os JSON Schemas em `schemas/` e para o validador em `scripts/validate_content.py`.

## Princípios

1. **Cada entidade tem um `id` estável.** O `id` é o *slug* usado em URLs, tags e relações. Deve ser `snake_case`, ASCII, sem acentos.
2. **Relações usam `id`, nunca nomes por extenso.** Um projeto que envolve o Prof. Sergio Freitas registra `researchers: [sergio_freitas]`, não `researchers: ["Sergio Antônio Andrade de Freitas"]`.
3. **Relações inversas não são registradas à mão.** Se o projeto declara seus pesquisadores, o perfil de cada pesquisador deriva a lista de projetos automaticamente. Templates fazem `where site.RegularPages "Params.researchers" "intersect" (slice $id)`.
4. **Pares PT/EN existem por `translationKey` ou por convenção de nome de arquivo.** No caso do CEDIS a maioria usa o segundo padrão (`foo.pt.md` + `foo.en.md`); páginas institucionais críticas ganham `translationKey` explícito para o validador confirmar a paridade.
5. **Enumerações são fechadas.** Status de projeto ∈ {`ongoing`, `closed`}. Tipo de publicação ∈ {`article`, `book`, `book chapter`, `book_section`, `conference`, `dissertation`, `phd`, `registro`, `specialization`, `tcc`, `workshop`}. Idioma ∈ {`pt`, `en`}.

## Fontes canônicas (recapitulação)

| Arquivo | Papel |
|---|---|
| `data/advisors.yaml` | Pesquisadores docentes do CEDIS, indexados por `id`. Fonte de nome, contato, ORCID, áreas primárias. |
| `data/areas.yaml` | Lista fechada de áreas de atuação. Cada área tem `id`, `name.{pt,en}` e lista de `researchers` por ID. |
| `data/people.yaml` | Orientandos ativos, alumni e não-docentes. Vinculados a orientadores via `advisors: [id]`. |
| `data/projects.yaml` | Metadados agregados de projetos (fonte a longo prazo passa a ser `content/projects/*.md` conforme I03). |
| `data/productions.yaml` | Produção científica. Referências a autores/orientadores por ID em `tags` e `advisors`. |

## Entidades

### Pesquisador (docente) — `advisors.yaml` + `content/people/{id}.md`

Campos obrigatórios em `data/advisors.yaml`:
- `name` — nome por extenso.
- `link` — path do perfil, ex.: `/people/sergio_freitas`.
- `areas` — lista de IDs de área (existentes em `areas.yaml`).

Campos opcionais recomendados:
- `lattes`, `orcid`, `email`.

Página em `content/people/{id}.{pt,en}.md` obrigatoriamente:
- `title` — nome por extenso.
- `categories` deve incluir `researcher` para aparecer nos agregadores.
- `date`, `language` — padrão Hugo.

### Pessoa (não-docente) — `data/people.yaml`

Cada item do array:
- `name` — obrigatório.
- `categories` — obrigatório; deve incluir `people` + um marcador de vínculo (`phd_candidate`, `master_student`, `tcc`, `specialization`, `scientific_initiation`, `volunteer`, `monitor`).
- `advisors` — lista de IDs (referência a `advisors.yaml`).
- `year` — ano de referência (início ou defesa).
- `program` — código de programa acadêmico (`curso_esw`, `curso_ppca_mestrado`, etc.).
- `title.{pt,en}` — título do trabalho, ambos idiomas.
- `tags` — inclui marcadores de estado (`active` ou `inactive`), IDs de área e IDs de projeto.

### Área — `data/areas.yaml` + `content/areas/{id}.{pt,en}.md`

`data/areas.yaml` cada item:
- `id` — obrigatório (usado em tags e categorias).
- `name.{pt,en}` — obrigatório.
- `researchers` — lista de IDs (de `advisors.yaml`).

Página em `content/areas/{slug}.{pt,en}.md`:
- `title`, `summary`, `featured_image` — obrigatórios.
- `categories` inclui `knowledge_areas` + IDs dos pesquisadores responsáveis.
- `tags` inclui o próprio `id` da área.

### Projeto — `content/projects/{id}.{pt,en}.md`

Frontmatter obrigatório:
- `title`, `date`, `language`, `summary`.
- `id` — slug do projeto (ex.: `dfcris`).
- `status` — `ongoing` | `closed`.
- `researchers` — lista de IDs de pesquisadores/participantes com página no site.
- `areas` — lista de IDs de área.
- `partners` — lista textual ou IDs.
- `funding_agencies` — lista textual.
- `products` — lista de IDs de produto derivado.
- `publications` — lista de IDs/DOI.
- `categories` inclui `project` + IDs dos pesquisadores.
- `tags` inclui IDs de área + marcador de estado (`active` | `inactive` | `closed`).

### Produto — `content/products/{id}.{pt,en}.md`

Frontmatter obrigatório:
- `title`, `date`, `language`, `summary`.
- `id` — slug do produto.
- `status` — `active` | `prototype` | `archived` | `beta`.
- `areas` — IDs de área.
- `responsible` — IDs de pesquisadores responsáveis.
- `publications` — IDs de publicações associadas.
- `categories` inclui `products`.

Frontmatter opcional:
- `project` — ID do projeto de origem quando o vínculo é claro.

### Publicação — `data/productions.yaml`

Cada item (esquema já documentado em `CONVENTIONS.md §2`):
- `type` — enum fechada.
- `year` — inteiro ou string ISO (o script tolera as duas formas).
- `title.{pt,en}` — obrigatório em ambos idiomas.
- `authors` — lista de nomes.
- `tags` — inclui IDs de pesquisador e de área.

### Parceiro — hoje textual em `content/parceiros.{pt,en}.md`

Modelo aspiracional (não implementado):
- `id`, `title`, `url`, `type` (institution|company|lab|funding_agency).

### Oportunidade — `content/oportunidades.{pt,en}.md` (I09 a estruturar)

Modelo aspiracional (não implementado):
- `id`, `title`, `status` (`open`|`closed`|`expired`), `deadline`, `audience`.

### Reconhecimento — `content/reconhecimentos.{pt,en}.md` (I16 já cria a página)

Modelo aspiracional (o conteúdo hoje é textual, mas cada item pode migrar para YAML):
- `id`, `title`, `year`, `context`, `link_to_post`.

## Regras cruzadas

Verificações que o `scripts/validate_content.py` executa:

1. **IDs de pesquisador únicos.** Nenhuma chave em `advisors.yaml` se repete.
2. **Referências de pesquisador resolvem.** Todo ID citado em `advisors:`, `researchers:`, `categories:`, ou nas áreas de `areas.yaml` deve existir em `advisors.yaml`. Exceção transitória documentada em `CONVENTIONS.md`: `daniel_sundfeld` (slug de URL é `daniel_lima`).
3. **Referências de área resolvem.** Todo ID citado em `areas:` ou como tag de área deve existir em `areas.yaml`.
4. **Enumerações válidas.** `type` de produção pertence ao conjunto fechado; `status` de projeto pertence ao conjunto fechado.
5. **Pares PT/EN.** Toda página em `content/` cuja frontmatter declare `translationKey` deve ter contrapartida no outro idioma com mesmo `translationKey`.
6. **Etiquetas não vazias.** Tags que consistam apenas em `""` ou `null` são reportadas.
7. **Datas coerentes.** `start_date <= end_date` em projetos; `year` de produção é razoável (1990-2030).

## Modo de operação

Nesta fase inicial (I02), o validador roda em **modo warn**: relata problemas em `stderr` e no relatório mas termina com exit 0. Após um ciclo de correções, o CI passa a modo strict (exit != 0 bloqueia PR).

Chaves de configuração do validador (defaults):

- `STRICT=false` — não falhar em warnings.
- `MAX_WARNINGS` — sem limite.
- `IGNORE_TRANSITIONAL` — respeita exceções listadas em `scripts/validate_content.py::TRANSITIONAL_EXCEPTIONS`.
