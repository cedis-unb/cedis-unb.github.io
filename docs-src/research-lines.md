# Linhas de pesquisa — modelo, ciclo de vida e operação

Documento técnico da camada **Linhas de pesquisa** do portal CEDIS.
Não é publicado no site (`docs-src/` fica fora de `content/`).
Registro de decisão e histórico: [`historical/2026-09-12-linhas-de-pesquisa.md`](historical/2026-09-12-linhas-de-pesquisa.md).

Última revisão: 2026-09-12. Estado: as cinco linhas estão `active` desde 2026-09-12 (ver registro histórico §3b).

---

## 1. Por que existe uma camada separada

O site já tinha **Áreas de atuação** (`data/areas.yaml` + `content/areas/`), que
funcionam como portas de entrada temáticas: "mostre tudo o que o CEDIS faz
sobre X". Elas são a **ontologia de comunicação** e continuam sendo a
navegação primária (home, menu, cards, mapa).

**Linhas de pesquisa** são outra coisa: programas científicos no sentido do
CNPq/DGP — temas aglutinadores com tradição investigativa, dos quais derivam
projetos e produção. São a **ontologia institucional/científica**, de
interesse para pesquisadores, avaliadores, agências e editais.

Decisão de arquitetura (2026-09-12): **as duas camadas coexistem**. Nenhuma
área foi convertida em linha; `areas.yaml` não mudou de semântica. A
hierarquia conceitual é

```
Linhas de pesquisa → Áreas de atuação → Temas → Projetos → produção/formação
```

sem ser árvore: todas as relações são muitos-para-muitos (uma área pode
pertencer a mais de uma linha; um projeto pode servir a duas linhas).

Princípio de exposição: *progressive disclosure*. O visitante vê áreas; quem
aprofunda encontra linhas em Pesquisa › Linhas de pesquisa, no bloco
"Linhas de pesquisa relacionadas" das páginas de área/perfil/projeto, no
mapa de conhecimento e num bloco discreto da home.

---

## 2. Fonte canônica: `data/research_lines.yaml`

```yaml
section:                      # título/descrição da página /research-lines/
  title: { pt: ..., en: ... }
  description: { pt: ..., en: ... }

research_lines:
  - id: line_software_engineering   # ^line_[a-z0-9_]+$ — estável, prefixado
    slug: software-engineering       # URL: /research-lines/<slug>/ (pt: /pt/research-lines/<slug>/)
    status: draft                    # draft | active | archived
    name:        { pt: ..., en: ... }
    summary:     { pt: ..., en: ... }   # 1–2 frases (hero, cards, blocos relacionados)
    description: { pt: |, en: | }       # markdown; seção "Escopo"
    questions:   { pt: [...], en: [...] }
    methods:     { pt: [...], en: [...] }
    history:     { pt: |, en: | }       # opcional
    period:      { start: 2016, end: null }   # opcional
    areas:       [software_architecture, ...] # ids de data/areas.yaml
    researchers: [sergio_freitas, ...]        # slugs de content/people (explícito!)
    projects:    [project_lfs, ...]           # ids de data/projects.yaml
    themes:
      - id: technical_debt                    # slug; vira chave i18n e liga à tag homônima
        name: { pt: "Dívida técnica", en: "Technical debt" }
```

Schema: `schemas/research_line.schema.json` (`additionalProperties: false`).

### Regras de modelagem

| Relação | Como é declarada | O que NÃO acontece |
|---|---|---|
| linha ↔ área | `areas[]` na linha | não se deduz de tags nem de `areas.yaml.researchers` |
| linha ↔ pesquisador | `researchers[]` na linha | **nunca** derivado de `areas.yaml`; deve ser validado por pessoa |
| linha ↔ projeto | `projects[]` na linha | não se deduz das tags dos projetos |
| linha ↔ tema | `themes[]` na linha | tema não precisa existir como tag; se existir, a página da linha liga a `/tags/<id>/` |

Relações inversas (área → linhas, pesquisador → linhas, projeto → linhas)
são calculadas **só** a partir deste arquivo, pelo partial
`research-lines-for`, e **só** para linhas `active`.

### Derivações (as únicas)

| Na página da linha | Regra |
|---|---|
| Produção recente | itens de `productions.yaml` cujas `tags` interceptam `areas ∪ projects ∪ themes.id` da linha; ordenados por ano desc; 8 exibidos, contagem total |
| Orientações vinculadas | entradas de `defesas.yaml` cujo `project` ∈ `projects` **ou** cujas `tags` interceptam o mesmo conjunto; 6 exibidas, contagem total |
| Produtos derivados | páginas de `content/products/` cujo `project` ou `secondary_projects` ∈ `projects`, ou cujas `tags` interceptam o mesmo conjunto |

Como quase toda produção é etiquetada com ids de área, uma área presente em
duas linhas faz a mesma produção contar nas duas. É intencional (centro
interdisciplinar); não é bug.

---

## 3. Ciclo de status

| status | página | menu / home / mapa | relações inversas | seção `/research-lines/` |
|---|---|---|---|---|
| `draft` | **não gerada** (`draft: true` no stub → fora do build, sitemap, RSS, busca, coleções) | não | não | conta como inexistente |
| `active` | gerada | sim | sim | listada em cards |
| `archived` | gerada com selo "Arquivada" | não | não | listada em "Linhas anteriores" (recolhido) |

Enquanto **nenhuma** linha for `active`:

- os stubs `_index.{pt,en}.md` recebem `build: {render: never, list: never}`
  — a URL `/research-lines/` não existe;
- o item de menu `pesquisa-linhas` (com `params.requires: research_lines`)
  é omitido por `layouts/partials/nav.html`;
- o bloco da home (`partials/research-lines-home.html`) e o nó "Linhas" do
  mapa não renderizam;
- `research-line-index` fica vazio, então nenhum bloco "relacionadas"
  aparece.

Tudo isso é decidido em tempo de build lendo o YAML; promover uma linha
não exige alteração de template.

---

## 4. Como promover uma linha (`draft` → `active`)

1. Confrontar nome, escopo e vínculos com o registro do grupo no DGP/CNPq.
2. Preencher `researchers[]` explicitamente (validar com cada pesquisador).
3. Revisar `areas[]`, `projects[]`, `themes[]`; opcionalmente `period`,
   `history`.
4. Trocar `status: active`.
5. Rodar:

   ```sh
   python3 scripts/build_research_lines.py   # regenera content/research-lines/
   python3 scripts/update_i18n.py            # sincroniza nomes/temas em i18n
   npm test                                  # schema, referências, paridade pt/en
   npm run build                             # exige Node 24 (ver README)
   ```

6. Conferir `/pt/research-lines/<slug>/`, o item em Pesquisa, o bloco nas
   áreas relacionadas e o nó no mapa.

Para arquivar: `status: archived` e os mesmos passos. Para reverter uma
publicação: `status: draft` — a página some do build seguinte (URLs
externas passam a 404; considerar `archived` se a linha já foi divulgada).

---

## 4a. Pré-visualizar rascunhos localmente

Em produção rascunhos não existem. Para revisá-los antes de promover:

```sh
npm run start:lines-preview     # = HUGO_CEDIS_PREVIEW_LINES=1 build:research-lines + hugo server
```

Abre `/pt/research-lines/` com todos os rascunhos marcados "Rascunho" e uma
faixa de aviso. Ao encerrar (Ctrl+C) o script regenera os stubs em modo
normal; se isso não acontecer, `npm test` acusa "divergente" e basta rodar
`npm run build:research-lines`. Nunca commitar stubs gerados em preview.

Mecanismo: com a variável definida, o gerador grava os rascunhos com
`draft: false` e põe `research_lines_preview: true` no `_index` (em vez de
`build.render: never`); `research-line-index` e a lista só incluem rascunhos
quando esse param existe. Não usa `-D` nem APIs obsoletas do Hugo. Todos
os pontos de exposição (menu, home, mapa, blocos "relacionadas", link em
Sobre › Para saber mais) usam o modo `visible` de `research-line-list`:
ativas em produção; ativas + rascunhos em pré-visualização, com o rótulo
"(rascunho)" no mapa e o selo nos cards. Assim a pré-visualização é fiel
ao que a promoção vai publicar.

Atenção com `hugo server` já aberto: ao trocar o status de uma linha para
`draft`, o servidor pode manter a página antiga em memória até ser
reiniciado.

## 5. Validação (`scripts/validate_content.py::validate_research_lines`)

Erros (falham `npm test`):

- schema inválido; `id` ou `slug` duplicado; `status` fora do enum;
- `areas[]` com id inexistente em `areas.yaml`;
- `researchers[]` com slug inexistente em `content/people`;
- `projects[]` com id inexistente em `projects.yaml`/`content/projects`;
- `themes[].id` duplicado; `period.end < period.start`;
- linha `active` sem área ou sem pesquisador.

Avisos:

- pesquisador que não é perfil `researcher`/`advisor_only`;
- tema cujo id coincide com id de área;
- linha `active` sem projeto.

`scripts/build_research_lines.py --check` (em `npm test`) falha se
`content/research-lines/` estiver dessincronizado do YAML.

---

## 6. Arquivos

| Arquivo | Papel |
|---|---|
| `data/research_lines.yaml` | fonte canônica |
| `schemas/research_line.schema.json` | schema JSON |
| `scripts/build_research_lines.py` | gera stubs em `content/research-lines/` (`--check` no `npm test`) |
| `scripts/update_i18n.py` | sincroniza `line_*` (sempre) e temas (só quando ausentes) em `i18n/` |
| `scripts/validate_content.py` | `validate_research_lines` |
| `layouts/partials/research-line-index.html` | dicionário id → entrada (exclui `draft`) |
| `layouts/partials/research-line-list.html` | lista ordenada por modo `active`/`archived`/`all` (modo na chave de cache) |
| `layouts/partials/research-lines-for.html` | relação inversa por `kind` (`area`, `researcher`, `project`, `theme`) |
| `layouts/partials/research-line-related.html` | bloco lateral "Linhas de pesquisa relacionadas" (renderiza nada se vazio) |
| `layouts/partials/research-lines-home.html` | bloco discreto da home |
| `layouts/shortcodes/research-lines-link.html` | item "Linhas de pesquisa" em Sobre › Para saber mais (vazio sem linha visível) |
| `layouts/research-lines/single.html`, `list.html` | páginas |
| `layouts/partials/nav.html` | omite itens com `params.requires` não satisfeito |
| `layouts/areas/single.html`, `people/single.html`, `projects/single.html` | chamam `research-line-related` |
| `layouts/_default/map.html` | nó `line` (âmbar) ligado a áreas, pesquisadores e projetos |
| `hugo.yaml` | item `pesquisa-linhas` em Pesquisa; "Áreas de atuação" unificado |
| `i18n/{pt,en}.yaml` | chaves `ui_research_line*`, `ui_line_*`, `ui_lines_home_*`, `ui_map_*_line(s)`, `breadcrumb_research-lines` |

Casamento área ↔ página de área: `research-line-related` na página de área
usa o id da página **e** as tags da página que sejam ids de `areas.yaml`
(ex.: página `ai_pln` tem tag `ai`; a linha declara `ai`). Isso cobre a
diferença entre ids de `areas.yaml` (20) e páginas de área (15).

---

## 7. Fora de escopo neste ciclo (registrado para decisão futura)

- **Contextos** e **métodos** como entidades relacionais (hoje `methods` é
  lista textual da linha).
- Produtos no mapa e relação linha ↔ produto direta (produto chega via
  projeto).
- Indicadores por linha na página de Indicadores.
- Exportação DGP/CNPq.
