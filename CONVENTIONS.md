# Convenções de conteúdo do site CEDIS

Este documento consolida as regras editoriais e técnicas aplicadas ao
conteúdo do site cedis-unb.github.io. Use-o como referência ao inserir
novos itens (notícias, publicações, pessoas, produtos, projetos) para
manter conformidade com o padrão atual.

Última revisão: julho/2026 (pós-Gaps #1, #2 e correções Gap #10).

---

## Idiomas do Hugo

O portal publica dois idiomas: português do Brasil e inglês. Por
compatibilidade com Hugo, URLs existentes e sufixos de arquivo, a chave
interna do português é `pt`, mas o `locale` configurado em `hugo.yaml` é
`pt-BR`.

Regras:
- Arquivos em português usam sufixo `.pt.md` e frontmatter
  `language: pt`.
- Arquivos em inglês usam sufixo `.en.md` e frontmatter `language: en`.
- Não crie arquivos `.pt-br.md` nem frontmatter `language: pt-br`; o
  validador deve reportar isso.
- Metadados públicos (`hreflang`, Open Graph e sitemap) expõem o
  português como `pt-BR`.

---

## Fontes canônicas em `data/` (4 arquivos)

Todo arquivo `.yaml` no diretório `data/` é carregado automaticamente pelo
Hugo. Para evitar edição da fonte incorreta, o repositório mantém apenas
as fontes canônicas listadas abaixo. Cópias históricas, versões
"antigas" e ensaios devem ficar **fora do repositório** (backup local,
gist privado, branch efêmera) — nunca em `data/`.

| Arquivo | Papel canônico |
|---|---|
| `data/areas.yaml` | Áreas de atuação do CEDIS. Consumido pela cascata i18n. |
| `data/people.yaml` | Pessoas sem página individual (orientandos ativos, alumni). Cada entrada tem `slug` **obrigatório** (validado). |
| `data/productions.yaml` | Produção científica. `authors[]` (strings), `people[]` (slugs), `tags[]` (tópicos/projetos). |
| `data/projects.yaml` | Projetos (metadados agregados). Consumido pela cascata i18n. |

**Removido em 2026-07-24:** `data/advisors.yaml`. Contato/áreas/link de
docentes agora ficam no frontmatter dos `.md` em `content/people/`.
Templates consultam via `partial "people-lookup"`.

Não crie arquivos como `people-old.yaml`, `productions copy.yaml`, ou
sufixos `-v2`, `-backup`, `-errado`. Se precisar experimentar uma
alteração de estrutura, use uma branch e um PR.

### Identificadores de pessoa: slug canônico

O identificador de pessoa é o `slug` (snake_case, ASCII, sem acentos).
Referências estruturadas (`advisors`, `people`, `researchers`, `students`,
`responsible`, `creators`) usam o slug. Nunca use nome por extenso.

Regras:
- Se pessoa tem `.md` em `content/people/<slug>.md`, o slug é o basename
  do arquivo. O frontmatter pode declarar `slug:` em stubs derivados, mas
  perfis mantidos manualmente não precisam repetir esse campo.
- Se pessoa está em `data/people.yaml`, o campo `slug:` é obrigatório e
  deve casar com o `.md` (se existir).
- `categories` não deve repetir o slug da própria pessoa. Use
  `profile_level` para tipo de perfil e categorias apenas para taxonomia
  (`people`, `researcher`, `master_student`, etc.).
- `tags` em perfis não deve duplicar valores de `areas`; o template de
  perfil já exibe `areas` junto aos temas.

**Daniel Sundfeld**: consolidado em 2026-07-24 como `daniel_sundfeld` em
toda a base. O `.md` é `content/people/daniel_sundfeld.pt.md`.
Zero exceções em templates.

Novos pesquisadores devem usar o mesmo string tanto como slug do
arquivo quanto como identificador em tags/advisors — sem exceções.

### Relações estruturadas entre projetos, produtos e pessoas

A partir da Fase 3 do plano de auditoria, a fonte canônica de relações
entre projetos, produtos e perfis fica no *front matter* das páginas:

- `content/projects/*.md`: `id`, `status`, `researchers`, `areas`,
  `partners`, `funding_agencies`, `products`, `publications`.
- `content/products/*.md`: `id`, `status`, `areas`, `responsible`,
  `project` quando houver projeto de origem claro, `publications`.

Relações inversas nunca devem ser editadas manualmente. Se um projeto
declara `products: [contextus]`, a página do produto e os templates
podem derivar o vínculo; se um produto declara `project: dfcris`, a
página do projeto também pode encontrá-lo. Perfis de pesquisadores
derivam projetos por `Params.researchers` e produtos por
`Params.responsible`, mantendo categorias e tags apenas como camada de
compatibilidade visual e de taxonomia.

`data/projects.yaml` permanece no repositório como compatibilidade para
consumidores legados e deve ser tratado como espelho transitório. Novas
relações devem ser adicionadas primeiro nas páginas em `content/`.

### Macroprojetos, subprojetos e vínculos de produção

O portal distingue três níveis de vínculo entre produções, produtos e
projetos:

| Nível | Quando usar | Como registrar hoje |
|---|---|---|
| Projeto individual | Existe um projeto específico que explica diretamente a produção, produto, TCC, dissertação ou artigo. | Adicionar o ID do projeto individual em `tags:` de `data/productions.yaml` ou em `project:`/`secondary_projects:` de `content/products/*.md`. |
| Macroprojeto direto | A produção/produto pertence à frente estratégica, mas não há projeto individual mais específico cadastrado. | Adicionar o ID do macroprojeto em `tags:` da produção ou `project:` do produto. |
| Sem vínculo claro | O tema é próximo, mas não há evidência suficiente de relação com projeto ou macroprojeto. | Não adicionar tag de projeto. Registrar como sugestão pendente, se necessário. |

A regra de decisão é sempre do mais específico para o mais amplo:

1. Procurar primeiro um projeto individual já existente.
2. Se não houver projeto individual, verificar se a produção é produto
   direto de um macroprojeto.
3. Se houver apenas semelhança temática, manter sem vínculo.
4. Não duplicar em macroprojeto uma produção que já está vinculada a
   projeto individual apenas porque esse projeto pertence ao macro. O
   template deve conseguir agregar por relação guarda-chuva.

Macroprojetos atuais:

| ID | Nome |
|---|---|
| `project_ia_dados_transformacao_digital` | Artificial intelligence and data analysis for digital transformation |
| `project_inovacao_digital_gamificacao` | Digital innovation and gamification for teaching, outreach, and software engineering |
| `project_software_bem` | Software para o Bem |

Projetos individuais podem declarar `umbrella_projects:` em
`data/projects.yaml` e/ou no front matter futuro das páginas de projeto.
Exemplos já usados:

| Projeto individual | Macroprojeto |
|---|---|
| `dfcris` | `project_ia_dados_transformacao_digital` |
| `project_cc` | `project_inovacao_digital_gamificacao` |
| `project_alvorecer` | `project_inovacao_digital_gamificacao` |
| `project_jornada` | `project_inovacao_digital_gamificacao` |
| `project_framework_preditivo_engajamento` | `project_inovacao_digital_gamificacao`, `project_ia_dados_transformacao_digital` |
| `project_super_r` | `project_inovacao_digital_gamificacao` |
| `evidentia` | `project_ia_dados_transformacao_digital` |
| `octaanalysis` | `project_inovacao_digital_gamificacao` |
| `project_doarti` | `project_software_bem` |

Produtos também podem ser produtos diretos de macroprojeto quando não
há projeto individual intermediário. Exemplos: `atloria`,
`deckmanager`, `devdog`, `gitranking`, `moodlegam` e `nativo` pertencem
ao macroprojeto de inovação/gamificação; `apoio_estudantil_fcte`,
`magra`, `predicao_euploidia` e `saga` pertencem ao macroprojeto de IA
e dados; `bem_estar_universitario`, `prevencao_abuso_infantil` e
`prevencao_violencia_infancia` pertencem ao macroprojeto Software para
o Bem.

#### Produções e orientações vinculadas

As produções vinculadas a projetos são registradas hoje por meio de IDs
de projeto em `tags:` dentro de `data/productions.yaml`. Isso vale para
artigos, livros, capítulos, TCCs, dissertações, teses, registros,
materiais e produções técnicas.

Para decidir se uma produção entra como "Produção C&T vinculada" ou
"Orientação vinculada":

- `type: article`, `conference`, `book`, `book chapter`,
  `book_section`, `workshop`, `registro`, `didactic` e softwares
  registrados contam como produção C&T.
- `type: tcc`, `dissertation`, `phd`, `specialization` contam como
  orientação quando há orientador CEDIS em `advisors:`.
- Uma dissertação ou TCC pode também gerar produto ou artigo. Nesse
  caso, todos os itens podem ter o mesmo ID de projeto, mas não devem
  ser duplicados como se fossem a mesma produção.
- Se o mesmo resultado aparece como TCC e artigo, vincular os dois
  quando ambos existem em `data/productions.yaml`, pois eles representam
  produtos acadêmicos distintos.

Os títulos nas tabelas "Produção C&T vinculada" e "Orientações
vinculadas" devem ser linkados apenas quando houver página específica
em `content/publications/` ou `content/products/`. Não criar link para
página genérica de tag/projeto apenas para "ter link". Em tabelas
densas, o link deve ser discreto: linkar somente o título, sem adicionar
coluna "link", botão, CTA ou texto auxiliar.

#### Equipe principal e rede ampliada

Macroprojetos exibem dois conceitos distintos:

- **Equipe principal/Core team**: pesquisadores centrais declarados no
  próprio macroprojeto.
- **Rede ampliada/Extended network**: pessoas que participaram por meio
  de subprojetos, produtos, artigos, TCCs, mestrados, registros e outras
  produções ligadas ao macroprojeto.

A contagem da rede ampliada deve ser deduplicada por pessoa, mas a
interface não deve usar termos técnicos como "deduplicate count" ou
"other linked people". Use linguagem humana: "Rede ampliada" em PT e
"Extended network" em EN.

#### Automação desejada em Hugo

O estado ideal é não manter manualmente as tabelas "Produção C&T
vinculada" e "Orientações vinculadas" em `content/projects/*.md`.
Templates ou shortcodes Hugo devem derivar essas listas assim:

1. Ler o ID do projeto atual (`.Params.id`).
2. Se for macroprojeto, montar o escopo com:
   - o próprio ID do macroprojeto;
   - todos os projetos individuais cujo `umbrella_projects` contenha o
     macroprojeto;
   - produtos cujo `project`, `secondary_projects`, `tags` ou
     `categories` contenham algum ID do escopo;
   - publicações declaradas em produtos ou projetos do escopo.
3. Percorrer `hugo.Data.productions.items`.
4. Incluir uma produção quando:
   - `tags` contém o ID do projeto atual; ou
   - `tags` contém algum projeto individual do escopo do macroprojeto; ou
   - a produção corresponde a publicação declarada em produto/projeto do
     escopo.
5. Separar a renderização por tipo:
   - produção C&T: artigos, capítulos, livros, registros, software,
     materiais e eventos;
   - orientação: TCC, dissertação, tese, especialização e IC/voluntariado
     quando modelados.
6. Ordenar por ano decrescente e, dentro do ano, por título.
7. Linkar automaticamente para a página gerada em `content/publications`
   quando existir. Para produtos, linkar para `content/products`.
8. Exibir só o título como link dentro da tabela; sem botão ou coluna
   extra.

Até essa automação existir, uma IA deve seguir o mesmo algoritmo de
forma manual: localizar o item em `data/productions.yaml`, acrescentar
o ID de projeto correto em `tags:`, rodar `scripts/build_publications.py`
com um ambiente Python que tenha PyYAML, revisar diffs colaterais do
gerador e executar `npm run build`.

#### Plano para automação completa dos vínculos de projetos

O objetivo da automação é fazer Hugo renderizar, sem tabelas manuais,
os vínculos entre macroprojetos, projetos individuais, produtos,
produção C&T, orientações e pessoas. A automação deve ser determinística:
Hugo só deve aplicar relações explicitamente registradas nos metadados.
Quando o vínculo depender de interpretação histórica, semântica ou
contextual, a etapa de curadoria por pessoa ou IA ainda será necessária
antes do build.

Para chegar ao estado automatizado, seguir este plano:

1. **Padronizar projetos.**
   Todo projeto deve ter `id`, `project_type`, `researchers`,
   `students` quando aplicável e `umbrella_projects` quando fizer parte
   de macroprojeto. Macroprojetos devem usar `project_type: umbrella`.
   Projetos individuais devem usar `project_type: project` ou omitir o
   campo quando o padrão for projeto individual.

2. **Padronizar produtos.**
   Todo produto em `content/products/*.md` deve declarar `id` e, sempre
   que conhecido, `project`, `secondary_projects` e `publications`.
   Produtos diretos de macroprojeto devem usar o ID do macroprojeto em
   `project`. Produtos com vínculo secundário devem usar
   `secondary_projects`, sem duplicar o vínculo principal.

3. **Padronizar produções.**
   Todo item em `data/productions.yaml` deve declarar `type`, `year`,
   `title` e `tags` com IDs de projeto quando houver vínculo conhecido.
   Orientações devem ter `advisors` e, quando possível, orientando em ID
   consistente. A automação de Hugo não deve inferir vínculo apenas por
   palavras do título.

4. **Criar um escopo de projeto reutilizável.**
   Implementar um partial ou bloco comum em Hugo que, dado o ID do
   projeto atual, retorne:
   - o próprio projeto;
   - subprojetos, quando o projeto atual for macroprojeto;
   - macroprojetos, quando o projeto atual for individual;
   - produtos diretos e secundários do escopo;
   - publicações declaradas em projetos e produtos do escopo.

5. **Automatizar as tabelas de produção.**
   Substituir as tabelas manuais "Produção C&T vinculada" e "Orientações
   vinculadas" por shortcodes ou seções automáticas do template de
   projeto. A tabela deve usar o escopo calculado, percorrer
   `hugo.Data.productions.items`, filtrar por `tags` e por publicações
   declaradas em produtos/projetos, ordenar por ano decrescente e título,
   e separar produção C&T de orientações conforme a regra de tipos
   definida acima.

6. **Automatizar links internos.**
   A renderização deve procurar a página correspondente em
   `content/publications/` e linkar somente o título quando a página
   existir. Para produtos, deve linkar `content/products/`. Itens sem
   página própria devem aparecer como texto simples.

7. **Automatizar rede ampliada.**
   Para macroprojetos, Hugo deve calcular "Rede ampliada" a partir de
   subprojetos, produtos, produções, orientações e pessoas declaradas nos
   metadados. A contagem deve remover duplicações por ID ou, quando não
   houver ID, por nome normalizado. A interface deve continuar usando
   linguagem humana, não termos técnicos.

8. **Remover duplicação manual.**
   Depois que o template estiver validado, remover dos arquivos
   `content/projects/*.md` as tabelas manuais equivalentes. O Markdown do
   projeto deve manter texto curatorial, objetivos, contexto, dados gerais
   e narrativa; os blocos relacionais devem ser derivados por Hugo.

9. **Adicionar validações.**
   Criar checagens de consistência para IDs inexistentes, produtos sem
   projeto, publicações com tag de projeto inexistente, páginas geradas
   sem fonte em `data/productions.yaml` e orientações sem `advisors`.
   Essas validações podem ser scripts auxiliares executados antes de
   `npm run build`.

10. **Definir o papel residual da IA.**
    Depois da automação, IA não deve ser necessária para renderizar o
    portal. Ela pode continuar útil para sugerir vínculos novos, revisar
    casos ambíguos, enriquecer metadados e transformar evidências
    textuais em IDs estruturados. A decisão final deve virar dado
    explícito antes do build.

Critério de conclusão: uma alteração em `data/productions.yaml`,
`data/projects.yaml` ou no front matter de `content/products/*.md` deve
ser suficiente para que `npm run build` atualize automaticamente as
páginas de projeto, as contagens, os links, as produções vinculadas, as
orientações vinculadas e a rede ampliada, sem edição manual das tabelas
em Markdown.

### Publicações geradas

As páginas em `content/publications/` são geradas a partir de
`data/productions.yaml` por `scripts/build_publications.py`. Não edite
essas páginas manualmente; corrija a fonte em `data/productions.yaml` e
rode o gerador.

O gerador cria uma página PT e EN para cada item, URLs por tipo e ano,
índices por agrupamento (`scientific`, `tcc`, `thesis`,
`specialization`, `registrations`, `zenodo`, `didactic`), BibTeX e
JSON-LD. Links externos de publicação devem continuar no campo `url:` da
fonte YAML; nas páginas geradas eles aparecem como `external_url` para
não conflitar com o campo reservado `url` do Hugo.

### Oportunidades e trilhas Participe

Oportunidades ficam em `content/opportunities/`, com pares PT/EN e
campos `status`, `deadline`, `audience`, `project` e `responsible`
quando aplicável. As chamadas encerradas devem ter `status: expired` ou
`closed` e `noindex: true`.

Em julho/2026, todos os editais cadastrados estão encerrados; não há
oportunidades abertas. Não marque uma oportunidade como `open` sem uma
chamada vigente, prazo futuro e texto revisado.

As trilhas permanentes de participação ficam em `content/junte-se/`:
`iniciacao-cientifica`, `tcc`, `mestrado`, `doutorado`, `extensao`,
`parcerias` e `proponha-projeto`.

### Notícias relacionadas

Posts podem declarar `related_ids:` com IDs de projeto, produto ou
pessoa. O partial `layouts/partials/related-news.html` usa esse campo,
além de `tags` e `categories`, para renderizar notícias relacionadas em
páginas de projetos, produtos e perfis.

Use IDs estáveis já declarados no front matter das entidades, como
`contextus`, `dfcris`, `project_inovacao_digital_gamificacao` ou
`sergio_freitas`.

### Paridade PT/EN

Páginas institucionais, oportunidades, trilhas e índices estruturantes
devem ter par PT/EN com o mesmo `translationKey`. Rode
`python3 scripts/validate_i18n.py` antes de publicar alterações de
conteúdo bilíngue.

---

## 1. Atribuição institucional

### 1.1 CEDIS vs. programas de ensino

**CEDIS agrega pesquisadores (professores) e suas produções — não
estudantes.** Um TCC ou dissertação NÃO é feito "por estudantes do
CEDIS". Os estudantes pertencem aos programas de ensino aos quais
estão vinculados; a ligação com o CEDIS acontece pelo orientador.

| Contexto | ❌ Errado | ✅ Certo |
|----------|-----------|----------|
| TCC de graduação | estudantes do CEDIS | estudantes de Engenharia de Software |
| Dissertação | aluno do CEDIS | mestrando do PPCA (ou PPEE, PPGEE conforme o caso) |
| Contato | ao CEDIS | ao Prof. `<link>` no CEDIS |
| Autoria de post | (aceitável) | `author: CEDIS` no frontmatter |
| Produtos digitais | (aceitável) | produtos do CEDIS |

Regra prática: pergunte "essa pessoa é professor(a) vinculado(a) ao
CEDIS?". Se sim, pode dizer "pesquisador(a) do CEDIS". Se não, use o
programa (graduação/PPCA/PPEE) e mencione o vínculo indireto via
orientador.

### 1.2 Faculdade — sempre FCTE

A antiga **Faculdade UnB Gama (FGA)** foi renomeada para **Faculdade
de Ciências e Tecnologias em Engenharia (FCTE)**. Use sempre a
denominação atual, mesmo em textos históricos.

| ❌ Não use | ✅ Use |
|-----------|--------|
| Faculdade UnB Gama | Faculdade de Ciências e Tecnologias em Engenharia (FCTE) |
| Faculdade do Gama | Faculdade de Ciências e Tecnologias em Engenharia (FCTE) |
| FGA / FGA/UnB | FCTE / FCTE/UnB |
| Gama Faculty | FCTE/UnB |
| at UnB Gama (em EN, referindo-se à faculdade) | at FCTE/UnB |
| defendeu na UnB Gama | defendeu na FCTE/UnB |

**Preservar como está**: "Campus Gama" (localização física) e
endereço postal "Setor Leste, Gama, DF" — o campus continua sendo em
Gama, só a faculdade foi renomeada.

### 1.3 Slugs de pesquisadores CEDIS

Os pesquisadores CEDIS têm slugs fixos usados em `advisors:`/`people:` no
YAML e em URLs de perfil (`/people/<slug>`).

| Slug | Nome completo | URL de perfil |
|------|---------------|----------------|
| `sergio_freitas` | Sergio Antônio Andrade de Freitas | `/people/sergio_freitas` |
| `cristiane_ramos` | Cristiane Soares Ramos | `/people/cristiane_ramos` |
| `andre_lanna` | André Luiz Peron Martins Lanna | `/people/andre_lanna` |
| `george_marsicano` | George Marsicano Corrêa | `/people/george_marsicano` |
| `ricardo_ajax` | Ricardo Ajax Dias Kosloski | `/people/ricardo_ajax` |
| `daniel_sundfeld` | Daniel Sundfeld Lima | `/people/daniel_sundfeld` |
| `fabiana_mendes` | Fabiana Freitas Mendes | `/people/fabiana_mendes` |

Advisors externos (co-orientam mas não são docentes CEDIS): `andrea_cabello`,
`berilhes_garcia`, `edna_canedo`, `marilia_miranda`, `claudia_ochoa`,
`celia_higawa` — cada um tem stub minimal em `content/people/<slug>.md`
com `profile_level: advisor_only`.

### 1.4 Índice unificado (`people-index` / `people-lookup`)

Templates NÃO devem consultar `hugo.Data.people`, `hugo.Data.advisors` (não
existe mais) ou `content/people/` diretamente. Use os partials centrais:

```go-html-template
{{/* consultar UMA pessoa */}}
{{ $p := partial "people-lookup" $slug }}
{{ if $p.found }}
  <a href="{{ $p.link }}">{{ $p.name }}</a>
  {{ $p.publications_count }} publicações
  {{ $p.contact.email }}
{{ end }}

{{/* iterar TODAS as pessoas */}}
{{ $idx := partialCached "people-index" "global" }}
{{ range $slug, $entry := $idx }}
  {{ if eq $entry.profile_level "researcher" }}...{{ end }}
{{ end }}
```

Campos do dict retornado documentados em `docs-src/data-model.md`.

### 1.5 Cascata i18n para rótulos (Gap #2, 2026-07)

Tag pills, labels de área/projeto e H1 de `/tags/<slug>/` devem usar o
partial `translated-label.html` (nunca `{{ . | i18n }}` direto).

```go-html-template
<a href="/tags/{{ $slug }}/" class="pill">
  {{ partial "translated-label.html" (dict "value" $slug) }}
</a>
```

O partial resolve em cascata:
1. `i18n <slug>` (traduções manuais)
2. `partial "project-lookup" <slug>` → `.name`
3. `partial "area-lookup" <slug>` → `.name`
4. `partial "people-lookup" <slug>` → `.name`
5. `humanize(<slug>)`

**Consequência**: novo projeto em `data/projects.yaml` ou nova área em
`data/areas.yaml` propaga label pra todas as pills automaticamente — não
precisa mais editar `i18n/*.yaml`.

---

## 2. `data/productions.yaml`

### 2.1 Campos por item

```yaml
- authors:                     # lista de nomes completos como no BDM
  - Fulano de Tal
  - Beltrano Silva              # co-autores no mesmo item (não criar duplicata)
  title:
    pt: 'Título original em português'
    en: 'Título traduzido em inglês'
  summary:                      # abstract (pode ficar vazio)
    pt: ''
    en: ''
  book_title: ''
  volume: ''
  doi_isbn: ''
  journal_event: ''
  location: ''
  pages: ''
  publisher: 'Biblioteca Central da Universidade de Brasília'   # para TCCs UnB
  tags:
  - tag1                        # tags temáticas do item (áreas CEDIS)
  - tag2
  type: tcc                     # ver §2.2
  program: curso_esw            # ver §2.3
  advisors:
  - sergio_freitas              # slugs de pesquisadores CEDIS
  url: https://bdm.unb.br/handle/10483/12345   # ver §2.4
  defense_date: 2025-07-15      # ver §2.5
  year: 2025
```

### 2.2 Tipos válidos (`type:`)

| Tipo | Descrição |
|------|-----------|
| `article` | Artigo em periódico |
| `book` | Livro |
| `book_section` | Capítulo de livro |
| `book chapter` | Capítulo de livro (variante legada; preferir `book_section` em novos itens) |
| `conference` | Trabalho completo em anais |
| `workshop` | Resumo expandido / trabalho em workshop |
| `didactic` | Curso, oficina ou material didático |
| `tcc` | Trabalho de Conclusão de Curso (graduação) |
| `dissertation` | Dissertação de mestrado |
| `phd` | Tese de doutorado |
| `specialization` | Trabalho de especialização |
| `registro` | Registro de programa de computador ou patente |

### 2.3 Programas (`program:`)

| Slug | Programa |
|------|----------|
| `curso_esw` / `curso_esw2` | Graduação em Engenharia de Software (FCTE/UnB) |
| `curso_ppca` | Mestrado Profissional em Computação Aplicada (PPCA/UnB) |
| `curso_ppgee` | Pós-Graduação Profissional em Engenharia Elétrica (PPEE/UnB) |
| `curso_ppgi` | Pós-Graduação em Informática (PPGI/UnB) |
| `curso_cc` | Ciência da Computação |
| `curso_cc_unb` | Bacharelado em CC/UnB |
| `curso_espucb_esw`, `curso_espufes`, `curso_espunb*`, `curso_espunicesp_psi` | Cursos de especialização |
| `curso_tsi_ifb` | Tecnologia em Sistemas para Internet (IFB) |
| `curso_ppgi_ufrgs` | Externo (UFRGS) |

### 2.4 URLs

- **BDM (TCCs UnB)**: `https://bdm.unb.br/handle/10483/<n>`
- **Repositório (mestrado/doutorado UnB)**: `https://repositorio.unb.br/handle/10482/<n>`
- **UFES (DSpace 9)**: `https://repositorio.ufes.br/handle/10/<n>` (canônico — evite links UUID ou de bitstream direto)

Regras:
- Sempre HTTPS. Nunca HTTP.
- Sempre a URL canônica `/handle/...`. Nunca `/items/<UUID>` nem `/server/api/core/bitstreams/...`.
- Prefira `bdm.unb.br` sem `www.` (o site aceita ambos, mas o metadado
  DC.date completo só sai da versão sem `www`).

### 2.5 `defense_date`

Campo em formato ISO `YYYY-MM-DD` (ou parcial `YYYY-MM` / `YYYY`
quando o BDM só registrou parte).

Origem, em ordem de preferência:
1. `<meta name="DC.date" content="YYYY-MM-DD">` na página do BDM/Repositório.
2. Rótulo `Data de apresentação:` na tabela de metadados HTML,
   convertendo abreviações portuguesas (Jan/Fev/Mar/Abr/Mai/Jun/
   Jul/Ago/Set/Out/Nov/Dez).

Posição: imediatamente antes de `year:` no bloco do item.

### 2.6 Consolidação de duplicatas

TCCs em dupla devem ter **uma entrada única** com os dois autores em
`authors:`, e não duas entradas separadas apontando para o mesmo
handle. Ao inserir novo TCC de dupla:

1. Verifique se algum dos autores já está no `productions.yaml`.
2. Se sim, adicione o coautor à entrada existente.
3. Nunca crie linha nova apontando para handle já registrado.

### 2.7 Slugs de pessoas em publicações (Gap #10, 2026-07)

**Novo padrão**: person-slugs vão no campo `people[]`, NÃO em `tags[]`.
Templates consultam ambos com fallback retrocompatível.

Toda produção científica, defesa, registro ou produto acadêmico que
deva aparecer no perfil de um pesquisador precisa ter o slug do
pesquisador em `people:` e, quando for orientação, também em `advisors:`.

Exemplo (padrão atual):

```yaml
tags:
- gamification
- software_quality
- project_dfcris          # projetos e temas continuam em tags[]
people:
- sergio_freitas          # ← pessoas em people[]
- andre_silva
advisors:
- sergio_freitas          # ← orientação em advisors[]
```

Regras:

- `advisors:` define vínculo de orientação.
- `people:` define coautoria/associação a uma pessoa (canônico).
- `tags:` define indexação temática e associação com projetos/áreas.
  **Não coloque mais person-slug em `tags:`** — o script
  `scripts/separate_people_from_tags.py` já migrou os existentes.
- Se o autor CEDIS participa de um artigo mas não é orientador, ainda
  assim inclua o slug em `people:`.
- Ao revisar publicações de um pesquisador, conferir se todas as
  entradas esperadas têm o slug correto em `people:`; ausência é a
  causa mais comum de publicação não aparecer no perfil.

### 2.7.1 Como pessoa vira autor conhecido

Fluxo automático:

1. Adicionar entrada em `productions.yaml` com o slug em `people[]`.
2. Se pessoa não tem `.md` nem entrada em `people.yaml`:
   - Rodar `python3 scripts/derive_people.py --apply`
   - Gera stub `content/people/<slug>.md` com `profile_level: derived`
3. Pessoa passa a ter URL própria `/people/<slug>/` mostrando as
   publicações onde é autora.

Templates envolvidos na propagação:
- `layouts/people/single.html:131` — perfil individual (count e list).
- `layouts/partials/posts-template.html:84` — `/categories/researcher/`.
- `layouts/shortcodes/publications.html`, `npublications.html` — filtros
  usam `.people[]` além de `.tags[]`.
- `layouts/partials/people-index.html:68-88` — pré-indexação global.

### 2.8 Publicações científicas vs. orientações

Use "publicações científicas" apenas para produção acadêmica publicada:

- `article`
- `conference`
- `workshop`
- `book`
- `book_section`
- `book chapter` (legado)

Não trate como "artigo científico":

- `tcc`
- `dissertation`
- `phd`
- `specialization`
- `registro`

Esses itens contam como produção/orientação/registro conforme o
contexto, mas não devem entrar em vitrines de "publicações em destaque"
quando a intenção for exibir artigos científicos recentes.

Recortes específicos já adotados:

- Publicações de Ricardo Ajax Dias Kosloski no CEDIS devem considerar
  **2014 em diante**.

### 2.9 Ordenação de listas

Listas de publicações, produções e orientações geradas a partir de
`data/productions.yaml` devem aparecer sempre por ano, do mais recente
para o mais antigo. Dentro do mesmo ano, use semestre mais recente
primeiro quando houver ano no formato `YYYY/S`.

Regra prática: não dependa da posição do item no YAML para definir a
ordem de exibição. O shortcode de publicações deve ordenar os itens
filtrados antes de renderizar.

---

## 3. Notícias de defesa (`content/posts/defesa-*.md`)

Toda defesa (TCC, mestrado, doutorado) com `defense_date >= 2015`
tem uma notícia jornalística associada, em PT e EN.

### 3.1 Nomeclatura

Filename: `defesa-<slug>-<ano>.<lang>.md`

- `slug`: `<primeiro-nome>-<sobrenome>` do primeiro autor, sem acentos,
  minúsculo, hífens. Ex.: `defesa-emanuel-oliveira-2025.pt.md`.
- Para dupla: usar apenas o primeiro autor no slug OU nomes
  concatenados quando o trabalho é conhecido pela dupla (ex.:
  `defesa-kalebe-murilo-2025.pt.md`).

### 3.2 Frontmatter

```yaml
---
title: "Título jornalístico — não use template"
date: 2025-07-22T00:00:00-03:00     # = defense_date da entrada em productions.yaml
draft: false
weight: 500
language: pt                         # ou en
featured_image: "../assets/images/featured/area_XXX.png"   # ver §3.4
summary: 'Frase única resumindo a defesa (mencionar autores, orientador implícito, tema).'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- defesa
- <tag1 do YAML>                     # replicar tags temáticas da entrada
- <tag2 do YAML>
---
```

`date` deve ser exatamente o `defense_date` (com hora zerada
`T00:00:00-03:00`). Se o `defense_date` for parcial (só ano), use
data intermediária como `<ano>-06-15T00:00:00-03:00`.

### 3.3 Corpo

- Aproximadamente **400 palavras** (~250-450), estilo jornalismo
  científico/acadêmico.
- **Não use template**. Varie o gancho jornalístico: pergunta central,
  metáfora, número marcante, contexto histórico, comparação
  temporal, foco em produto, foco em impacto social, revisão
  bibliométrica, etc.
- Comece com data por extenso: `Brasília, 22 de julho de 2025` (PT) /
  `Brasília, July 22, 2025` (EN).
- Sempre mencione o(s) orientador(es) via shortcode `link-interno`:
  ```
  {{< link-interno "/people/sergio_freitas" "Sergio Antônio Andrade de Freitas" >}}
  ```
- Sempre mencione **1 a 2 áreas** via `link-interno`:
  ```
  {{< link-interno "/areas/gamification/" "gamificação" >}}
  ```
- Termine o corpo com o link ao BDM/Repositório (ver §3.5).
- Feche com bloco `Sobre o CEDIS:` / `About CEDIS:`.

### 3.4 Mapeamento tag → imagem/área

| Tag YAML | featured_image | Link `/areas/` |
|----------|----------------|-----------------|
| `hpc` | `area_HPC.png` | `/areas/HPC/` |
| `active_learning`, `education`, `ihc` | `area_Aprendizagem Ativa.png` | `/areas/active_learning/` |
| `ai`, `nlp`, `machine_learning` | `area_IA.png` | `/areas/ai_pln/` |
| `gamification` | `area_Gamificação.png` | `/areas/gamification/` |
| `green_software` | `area_Green Software.png` | `/areas/green_software/` |
| `learning_analytics` | `area_Learning Analytics.png` | `/areas/learning_analytics/` |
| `security` | `area_Cibersecurity.png` | `/areas/security/` |
| `social_software` | `area_Social_Software.png` | `/areas/social_software/` |
| `soft_skills`, `teamwork` | `area_Team work and soft skills.png` | `/areas/soft_skills/` |
| `software_architecture`, `software_development_tools` | `area_Arquitetura de Software.png` | `/areas/software_architecture/` |
| `software_product_line` | `area_Linha de produtos.png` | `/areas/software_products/` |
| `software_quality` | `area_Software Quality.png` | `/areas/software_quality/` |
| `software_requirements` | `area_Engenharia de requisitos.png` | `/areas/software_requirements/` |
| `digital_transformation` | `area_Transformação Digital.png` | `/areas/transformation/` |
| `verification_validation_testing` | `area_Verificação e Validação.png` | `/areas/verival/` |

Escolha a primeira tag mapeável no `productions.yaml` como área
principal. Se houver empate, priorize a mais específica ao conteúdo.

### 3.5 Link para o trabalho

Toda notícia deve conter o link canônico ao trabalho publicado:

**TCCs (BDM):**
- PT: `O TCC pode ser lido na [Biblioteca Digital da Produção Intelectual Discente da UnB](https://bdm.unb.br/handle/10483/<n>).`
- EN: `The full text ... is available at the [UnB Undergraduate Theses Digital Library](https://bdm.unb.br/handle/10483/<n>).`

**Mestrados/doutorados (Repositório):**
- PT: `A dissertação está disponível na íntegra no [Repositório Institucional da UnB](https://repositorio.unb.br/handle/10482/<n>).`
- EN: `The full text ... is available at the [UnB Institutional Repository](https://repositorio.unb.br/handle/10482/<n>).`

### 3.6 Sinalização de idioma

Quando o **idioma da notícia difere do idioma do trabalho**, sinalize
explicitamente no link do texto integral:

- Notícia EN, trabalho em português: `The full text — written in Portuguese — is available at ...`
- Notícia PT, trabalho em inglês: `O trabalho — escrito em inglês — está disponível em ...`

Como saber o idioma do trabalho: campo `<meta name="DC.language">`
no HTML da página do BDM/Repositório. Valores como `por` /
`Português` indicam PT; `eng` / `English` indicam EN.

### 3.7 Banca (obrigatório para dissertações e teses)

Para `type: dissertation` ou `type: phd`, incluir um parágrafo com a
banca examinadora, obtido pela leitura das primeiras páginas do PDF
da dissertação (folha de aprovação).

Formato PT:
```
A defesa aconteceu em 27 de dezembro de 2023 em Brasília. A banca
examinadora foi presidida pelo orientador, Prof. Dr. <Nome>
(<Sigla/UnB>), e composta pelo Prof. Dr. <Nome> (<Instituição>) e
pelo Prof. Dr. <Nome> (<Instituição>). A Prof.ª Dr.ª <Nome do
coordenador>, coordenador(a) do PPCA, também acompanhou a sessão.
```

Formato EN:
```
The defense took place on December 27, 2023 in Brasília. The
examining committee was chaired by the advisor, Prof. Dr. <Name>
(<Affiliation>), and composed of Prof. Dr. <Name> (<Affiliation>)
and Prof. Dr. <Name> (<Affiliation>). Prof. Dr. <Coordinator's
Name>, PPCA program coordinator, also attended the session.
```

Extraia banca via `pdfplumber` (as 5 primeiras páginas geralmente
bastam). Preserve titulação (Prof. Dr., Prof.ª Dr.ª) e vínculo
(CIC/UnB, FCTE/UnB, PPCA, PPEE, IMD/UFRN, PPGI/PUC-PR, etc.).

### 3.8 Vínculo entre defesa e artigo publicado

Algumas defesas de TCC, mestrado ou doutorado geram artigo científico
com o aluno como autor. Quando isso acontecer, a notícia da defesa deve
mencionar a ligação com o(s) artigo(s) publicado(s).

Regras:

- Procurar o nome do aluno em `data/productions.yaml` antes de concluir
  a notícia.
- Vincular na notícia todos os artigos científicos claramente
  relacionados ao trabalho defendido.
- Usar link direto quando houver `url` ou DOI no item de produção.
- Não vincular automaticamente artigos antigos ou de outro ciclo de
  formação apenas porque o aluno tem o mesmo nome.
- Cuidado especial: **Arthur Temporim** tem artigo anterior ligado à
  graduação e outro ligado ao mestrado; em notícias do mestrado, não
  confundir os dois.

---

## 4. Perfis de pesquisadores (`content/people/*.md`)

- Campo `Lattes iD` sempre com HTTPS: `https://lattes.cnpq.br/<id>`.
- Não registrar telefone institucional da FCTE como telefone pessoal de
  pesquisador. Se não houver telefone pessoal real e autorizado, omitir.
- Não repetir `Site institucional` / `Institutional website` no Markdown
  individual do pesquisador quando o destino for sempre a FCTE. O
  template deve exibir esse vínculo de forma padronizada como
  **Vínculo institucional: FCTE/UnB**.

### 4.1 Estrutura editorial dos perfis

As páginas de pesquisadores devem priorizar leitura rápida e valor
acadêmico antes do currículo formal.

Ordem recomendada:

1. Bloco automático **Atuação em destaque**.
2. Perfil acadêmico/profissional.
3. Áreas de pesquisa.
4. Produtos vinculados, quando houver.
5. Projetos atuais.
6. Orientações atuais e anteriores.
7. Publicações em destaque e lista completa de publicações.
8. Formação acadêmica.
9. Contato.

Regras de layout:

- Os perfis não devem voltar ao formato de currículo em lista crua.
  Listas diretas de "Perfil", "Formação", "Atividades",
  "Contribuições" e "Contato" devem ser tratadas visualmente como
  blocos editoriais/timeline pelo template e CSS.
- Não inserir frases explicativas óbvias abaixo dos títulos de seção
  dos perfis. O layout deve organizar a leitura sem repetir o que o
  próprio título já comunica.
- "Áreas de pesquisa" devem ser compactas; esconder descrições longas
  e imagens quando o contexto for a página do pesquisador.
- "Projetos atuais" deve seguir o mesmo padrão de produtos,
  orientações e publicações: bloco colapsável, fechado por padrão,
  contador à direita e lista rolável quando houver muitos itens.
- Projetos escritos manualmente como bullets dentro do perfil do
  pesquisador devem ser convertidos em páginas em `content/projects/`.
  Não manter listas ad hoc de projetos no Markdown do perfil.
- Projetos encerrados usam `status: closed`, `start_date`, `end_date`
  quando conhecida e a tag `closed`; devem aparecer automaticamente no
  perfil do pesquisador em **Projetos anteriores**, com layout
  colapsável equivalente ao de Projetos atuais.
- Projetos em andamento usam `status: active` e `start_date`, sem tag
  `closed`; devem aparecer automaticamente em **Projetos atuais**.
- Quando só houver anos publicados para abertura/encerramento, registrar
  datas ISO com precisão anual (`YYYY-01-01` e `YYYY-12-31`) e tratar a
  exibição pública como ano/intervalo de anos.
- "Produtos" deve seguir o mesmo padrão de orientações/publicações:
  bloco colapsável, contador à direita, lista rolável quando houver
  muitos itens.
- "Orientações atuais", "Orientações anteriores", "Produtos" e
  "Publicações" começam fechados por padrão.
- Contadores desses blocos ficam alinhados à direita do título.
- O bloco lateral de contato deve ser um único cartão com linhas
  internas para email, Lattes e ORCID; não usar cartões separados para
  cada canal.
- Se a contagem de qualquer indicador for **0**, não exibir o item nem
  o zero. Isso vale para cards laterais, resumo executivo, badges e
  blocos automáticos.
- A tipografia dos perfis deve ser normalizada via
  `assets/css/overrides.css`; evitar tamanhos avulsos em Markdown.

### 4.2 Publicações nos perfis de pesquisadores

O perfil do pesquisador depende do vínculo correto em
`data/productions.yaml`:

- Para aparecer na lista completa do pesquisador, o item deve conter o
  slug do pesquisador em `tags:`.
- Para contar como orientação anterior, o item de defesa deve conter o
  slug em `advisors:`.
- O bloco "Publicações em destaque" deve selecionar apenas tipos
  científicos (§2.8), preferindo itens recentes.
- Se um pesquisador tem número esperado de publicações diferente do
  exibido, verifique primeiro os slugs em `tags:` antes de alterar
  templates.

---

## 4.A Ciclo de vida do orientando (`data/people.yaml`)

Este é o fluxo padrão de registro dos orientandos:

### 4.A.1 Enquanto a orientação está em andamento

- Cria-se uma entrada em `data/people.yaml` com o orientando.
- Tag **`active`** entre as tags.
- `categories`: `people` + o tipo do trabalho (`tcc`,
  `master_student`, `phd_candidate`, `scientific_initiation`,
  `volunteer`).
- `advisors`: slugs dos orientadores CEDIS (§1.3). Se houver co-orientador,
  adicionar todos.
- `title.pt` / `title.en`: tema do trabalho.
- `program`: programa (§2.3).
- `year`: ano previsto de conclusão.

```yaml
- name: Fulano de Tal
  categories:
  - people
  - tcc
  title:
    pt: 'Título do trabalho'
    en: 'Work title'
  program: curso_esw2
  advisors:
  - sergio_freitas
  tags:
  - active
  - gamification
  - education
  year: 2026
```

### 4.A.2 Após a defesa

Ao defender, o orientando ganha **três presenças** no repositório:

1. **Entrada em `data/productions.yaml`** — como TCC (`type: tcc`),
   dissertação (`type: dissertation`), tese (`type: phd`) ou
   especialização (`type: specialization`). Ver §2.
2. **Notícia de defesa** em `content/posts/defesa-<slug>-<ano>.<lang>.md`
   (§3), em PT e EN.
3. **Entrada em `data/people.yaml` continua** — a entrada NÃO é apagada:
   apenas a tag `active` é substituída por **`inactive`**, preservando
   o histórico da orientação tanto para o orientador quanto para o
   orientando.

Mudança mínima no `people.yaml`:

```diff
   tags:
-  - active
+  - inactive
   - gamification
   - education
```

### 4.A.3 Verificações que devem passar após uma defesa

Para o mesmo orientando:

- [ ] Existe entrada em `productions.yaml` com o mesmo `year` (ou
      `defense_date`) do trabalho.
- [ ] Existe notícia `defesa-*.md` em PT e EN.
- [ ] A entrada em `people.yaml` tem tag `inactive` (não `active`).
- [ ] Os nomes batem entre `people.yaml`, `productions.yaml` e
      as notícias (evitar variantes com/sem acento, abreviações,
      erros de digitação — usar sempre o nome como aparece no BDM).

### 4.A.4 Regras para casos especiais

- **TCC de dupla**: cada aluno tem sua própria entrada em `people.yaml`
  (uma por pessoa), mas apenas UMA entrada em `productions.yaml`
  (com os dois autores em `authors:`).
- **Coorientação**: mesmo orientando pode ter mais de um slug em
  `advisors:` — a entrada em `people.yaml` aparece nas listas de
  orientação de todos eles.
- **Alunos que mudam de tema/programa** sem defender: manter uma
  única entrada e ajustar os campos (não criar entrada nova).
- **Alunos que abandonam sem defender**: manter a entrada com
  `active` removido e adicionar tag descritiva (`abandoned` ou
  similar) se quiser marcar; não confundir com `inactive`, que
  significa "orientação concluída com defesa".

---

## 4.B Como o site conta defesas e orientações

Entender como o Hugo agrega os números ajuda a decidir onde
registrar cada informação.

### Página inicial (`/` — "Nossa cadência em 2026")

Definições no topo de `layouts/index.html`:

```
$defenseTypes := slice "phd" "dissertation" "tcc" "specialization"
```

Card | Cálculo | Fonte
---|---|---
**Publicações** (do ano) | items em `productions.yaml` com `year == currentYear` e `type NOT IN $defenseTypes` e `type != "registro"` | `data/productions.yaml`
**Defesas** (do ano) | items em `productions.yaml` com `year == currentYear` e `type IN $defenseTypes` | `data/productions.yaml`
**Registros** (do ano) | items com `year == currentYear` e `type == "registro"` | `data/productions.yaml`
**Produtos digitais** | páginas em `content/products/` (não filtra por ano) | `content/products/`

### Página de história (`/history/`)

Card | Cálculo | Fonte
---|---|---
**Anos** | `now.Year - 2013` | data corrente
**Publicações** (total) | items em `productions.yaml` com `type != "registro"` (**inclui defesas**) | `data/productions.yaml`
**Registros** (total) | items com `type == "registro"` | `data/productions.yaml`
**Produtos** | páginas em `content/products/` | `content/products/`
**Pesquisadores** | páginas em `content/people/` com categoria `researcher` | `content/people/*.md`
**Orientações** | **`len(hugo.Data.people.people)`** — total de entradas em `people.yaml` (ativas + inativas) | `data/people.yaml`

### Página de pesquisador (`/people/<slug>/`)

Card | Cálculo | Fonte
---|---|---
**Orientações atuais** | entradas em `data/people.yaml` com `advisors` contendo o slug e sem tag `inactive` | `data/people.yaml`
**Orientações anteriores** | itens `phd`, `dissertation`, `specialization`, `tcc` em `productions.yaml` com `advisors` contendo o slug e sem tag `active`, mais pessoas inativas de `scientific_initiation`, `volunteer` e `monitor` | `data/productions.yaml` + `data/people.yaml`
**Publicações** | itens em `productions.yaml` com o slug em `tags:` | `data/productions.yaml`
**Projetos atuais** | páginas em `content/projects/` com o slug em `categories:` ou `tags:`, `status: active` e sem tag `closed`/`inactive` | `content/projects/*.md`
**Projetos anteriores** | páginas em `content/projects/` com o slug em `categories:` ou `tags:` e `status: closed`, tag `closed` ou tag `inactive` | `content/projects/*.md`
**Produtos** | páginas em `content/products/` com o slug em `categories:`, `tags:`, `advisors:` ou `creators:` | `content/products/*.md`

Regras de cadastro de projetos:

- Criar página bilíngue em `content/projects/<slug>.pt.md` e
  `content/projects/<slug>.en.md`.
- Registrar o projeto também em `data/projects.yaml`, com `id`, nome PT/EN,
  `status`, `start_date`, `end_date` quando houver encerramento,
  `researchers` e `students` quando os estudantes forem conhecidos.
- O `id` do projeto deve aparecer em `categories:` e `tags:` da página.
- Projetos encerrados devem ter `status: closed` e tag `closed`.
- Projetos em andamento devem ter `status: active` e não devem ter tag
  `closed`.
- Perfis de pesquisadores não devem listar projetos em bullets manuais:
  o vínculo deve vir da página do projeto e dos metadados.

Observações:

- **Especializações contam como orientações anteriores** quando
  registradas em `productions.yaml` com `type: specialization`.
- Itens com contagem **0** não devem aparecer como card, badge ou linha
  do resumo executivo.

### Consequências operacionais

- **Uma defesa gera 2 incrementos**: +1 em publicações (via
  `productions.yaml`) e +0 em orientações (a entrada em
  `people.yaml` já existia — apenas mudou de `active` para
  `inactive`).
- **Uma orientação em andamento** (aluno ainda não defendeu) gera
  +1 em orientações e +0 em publicações — até o dia da defesa.
- **Não deletar entradas em `people.yaml`** após a defesa: o número
  de orientações reflete o histórico total, e apagar a entrada
  distorceria essa contagem.
- **Não duplicar entradas em `productions.yaml`** para o mesmo
  trabalho: alunos de dupla vão em `authors:` do mesmo item.

### Detalhes de i18n dos cards

Textos ficam em `i18n/pt.yaml` e `i18n/en.yaml`, chaves:

- Home (cadência do ano): `ui_metric_pubs_this_year`,
  `ui_metric_defenses_this_year`, `ui_metric_registrations_this_year`.
- History (totais): `ui_history_metrics_*`,
  `ui_metric_years`, `ui_metric_publications`,
  `ui_metric_registrations_total`, `ui_metric_products`,
  `ui_metric_researchers`, `ui_metric_supervisions`.

---

## 5. Notícias gerais (`content/posts/news-post.NNN.*.md`)

- `date` no frontmatter reflete a data do evento reportado.
- `categories: [News]`, `tags: [News, ...tags temáticas]`.
- Não atribua estudantes ao CEDIS (§1.1) — refira ao programa.

---

## 6. Adicionando um novo orientando

Fluxo recomendado ao registrar uma nova defesa:

1. **Encontrar o item no BDM/Repositório**
   - Por autor: `bdm.unb.br/browse?type=advisor&value=<Sobrenome,+Nome>` (usar variantes de acento).
   - Verificar handle canônico (`/handle/10483/...` para TCC,
     `/handle/10482/...` para dissertação/tese).

2. **Extrair metadados via HTML**
   - `DC.title`, `DC.creator`, `DC.contributor`, `DC.subject`,
     `DC.date`, `DC.language`.
   - Abstract via `DCTERMS.abstract` (PT) e `DC.description` (EN,
     quando presente).

3. **Se for dissertação/tese**: baixar PDF (`href="/bitstream/.../*.pdf"`)
   e extrair banca com `pdfplumber` (primeiras 5 páginas).

4. **Inserir no `productions.yaml`** seguindo §2.
   - Escolher `type`, `program`, `advisors`, `tags`.
   - Adicionar `defense_date` e `year`.
   - Verificar duplicatas (§2.6).

5. **Criar notícia de defesa** (§3), em PT e EN.

6. **Atualizar `data/people.yaml`** (§4.A) — trocar tag `active`
   por `inactive` na entrada do orientando. Se o orientando ainda
   não estava em `people.yaml`, adicionar com `inactive` (não
   `active`).

7. **Rodar `hugo`** e verificar build limpo.

8. **Commit e push**.

---

## 7. Comandos de verificação úteis

Antes de commitar, rodar:

```bash
# Nenhuma menção incorreta a estudantes CEDIS
grep -rn "estudantes do CEDIS\|aluno do CEDIS\|CEDIS student" content/

# Nenhuma referência residual a FGA/UnB Gama como faculdade
grep -rn "FGA\|Faculdade UnB Gama\|Faculdade do Gama\|UnB Gama\b" content/ data/

# Nenhum HTTP em Lattes
grep -rn "http://lattes.cnpq.br" content/

# Build limpo
hugo | tail -3
```

**Coerência people ↔ productions** (§4.A) — nenhum orientando com
notícia de defesa deve estar como `active` em `people.yaml`:

```bash
python3 -c "
import yaml, os, re, unicodedata
def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode()
    return re.sub(r'\W+',' ',s).lower().strip()
p = {norm(x['name']): x for x in yaml.safe_load(open('data/people.yaml'))['people']}
bad = []
for f in sorted(os.listdir('content/posts/')):
    if not f.startswith('defesa-') or not f.endswith('.pt.md'): continue
    txt = open(f'content/posts/{f}').read()
    m = re.search(r'summary: [\"\\'](.+?) defende', txt)
    if not m: continue
    for name in re.split(r' e | and ', m.group(1)):
        k = norm(name)
        if k in p and 'active' in (p[k].get('tags') or []):
            bad.append((f, name))
for f,n in bad: print(f'ATIVO com defesa: {f} → {n}')
print(f'\\ntotal inconsistente: {len(bad)}')
"
```

Se houver ocorrências, corrigir antes do commit.

---

## 8. Convenções de commit

- Mensagens em inglês, curtas no assunto, expandidas no corpo.
- Um commit por unidade de mudança (não misturar tipografia com
  novos itens).
- Inclui rodapé `Co-Authored-By:` quando aplicável.
- Regerar `docs/` (`hugo`) antes de commitar; o `docs/` é o output
  publicado pelo GitHub Pages e deve ser mantido em sincronia com
  o source.

---

## 9. Áreas do CEDIS (referência rápida)

Diretório: `content/areas/`. Cada área tem `.pt.md` e `.en.md`.

| Slug arquivo | Nome PT | Nome EN | Tags cobertas |
|---|---|---|---|
| `HPC` | Computação de Alto Desempenho | HPC | hpc |
| `active_learning` | Aprendizagem Ativa | Active Learning | active_learning, education, ihc |
| `ai_pln` | IA e PLN | AI and NLP | ai, nlp, machine_learning |
| `gamification` | Gamificação | Gamification | gamification |
| `green_software` | Green Software | Green Software | green_software |
| `learning_analytics` | Learning Analytics | Learning Analytics | learning_analytics |
| `security` | Cibersegurança | Cybersecurity | security |
| `social_software` | Software Social | Social Software | social_software |
| `soft_skills` | Soft Skills | Soft Skills | soft_skills, teamwork |
| `software_architecture` | Arquitetura de Software | Software Architecture | software_architecture, software_development_tools |
| `software_products` | Linha de Produtos | Product Line | software_product_line |
| `software_quality` | Qualidade de Software | Software Quality | software_quality |
| `software_requirements` | Engenharia de Requisitos | Requirements Engineering | software_requirements |
| `transformation` | Transformação Digital | Digital Transformation | digital_transformation |
| `verival` | Verificação e Validação | Verification and Validation | verification_validation_testing |

---

## 10. Checklist final para um novo item

- [ ] Entrada em `data/productions.yaml` com todos os campos (§2)
- [ ] `defense_date` no formato ISO
- [ ] `url` canônica HTTPS
- [ ] Advisors com slugs válidos (§1.3)
- [ ] Tags temáticas escolhidas (mapeáveis para áreas — §3.4)
- [ ] Slugs dos pesquisadores CEDIS incluídos em `tags:` quando a
      produção deve aparecer no perfil (§2.7)
- [ ] Notícia de defesa em PT (§3)
- [ ] Notícia de defesa em EN (§3), com sinalização de idioma se
      trabalho estiver em português (§3.6)
- [ ] Se a defesa gerou artigo científico com o aluno como autor, a
      notícia menciona e linka esse artigo (§3.8)
- [ ] Para mestrado/doutorado: banca extraída do PDF (§3.7)
- [ ] Link ao BDM/Repositório em ambas notícias (§3.5)
- [ ] Referências a "Faculdade" usando FCTE (§1.2)
- [ ] Nenhuma atribuição de estudante ao CEDIS (§1.1)
- [ ] Entrada correspondente em `data/people.yaml` marcada como
      **`inactive`** (§4.A) — se ainda não existia, criar como
      `inactive`
- [ ] Nomes coerentes entre `productions.yaml`, `people.yaml` e
      notícias (§4.A.3)
- [ ] Perfis de pesquisadores não exibem cards, badges ou linhas com
      contagem zero (§4.1, §4.B)
- [ ] `hugo` roda sem erros
- [ ] Commit + push
