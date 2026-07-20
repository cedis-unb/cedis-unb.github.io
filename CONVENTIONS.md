# Convenções de conteúdo do site CEDIS

Este documento consolida as regras editoriais e técnicas aplicadas ao
conteúdo do site cedis-unb.github.io. Use-o como referência ao inserir
novos itens (notícias, publicações, pessoas, produtos, projetos) para
manter conformidade com o padrão atual.

Última revisão: julho/2026.

---

## Fontes canônicas em `data/`

Todo arquivo `.yaml` no diretório `data/` é carregado automaticamente pelo
Hugo. Para evitar edição da fonte incorreta, o repositório mantém apenas
as fontes canônicas listadas abaixo. Cópias históricas, versões
"antigas" e ensaios devem ficar **fora do repositório** (backup local,
gist privado, branch efêmera) — nunca em `data/`.

| Arquivo | Papel canônico |
|---|---|
| `data/advisors.yaml` | Orientadores e áreas primárias por pesquisador. |
| `data/areas.yaml` | Áreas de atuação do CEDIS. |
| `data/people.yaml` | Pessoas do CEDIS (pesquisadores, orientandos ativos, alumni). |
| `data/productions.yaml` | Produção científica (artigos, defesas, registros). |
| `data/projects.yaml` | Projetos (metadados agregados; a fonte de longo prazo será a página em `content/projects/`, ver issue I03 do `PLANO-AUDITORIA-2026.md`). |

Não crie arquivos como `people-old.yaml`, `productions copy.yaml`, ou
sufixos `-v2`, `-backup`, `-errado`. Se precisar experimentar uma
alteração de estrutura, use uma branch e um PR.

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

Os pesquisadores CEDIS têm slugs fixos usados em `advisors:` no YAML e
em URLs de perfil (`/people/<slug>`).

| Slug | Nome completo | URL de perfil |
|------|---------------|----------------|
| `sergio_freitas` | Sergio Antônio Andrade de Freitas | `/people/sergio_freitas` |
| `cristiane_ramos` | Cristiane Soares Ramos | `/people/cristiane_ramos` |
| `andre_lanna` | André Luiz Peron Martins Lanna | `/people/andre_lanna` |
| `george_marsicano` | George Marsicano Corrêa | `/people/george_marsicano` |
| `ricardo_ajax` | Ricardo Ajax Dias Kosloski | `/people/ricardo_ajax` |
| `daniel_sundfeld` | Daniel Sundfeld Lima | `/people/daniel_lima` ⚠️ |
| `fabiana_mendes` | Fabiana Freitas Mendes | `/people/fabiana_mendes` |

⚠️ Atenção: Daniel usa `daniel_sundfeld` como advisor em `productions.yaml`
mas a página de perfil está em `/people/daniel_lima`.

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

### 2.7 Tags de pesquisador em publicações

Toda produção científica, defesa, registro ou produto acadêmico que
deva aparecer no perfil de um pesquisador precisa ter o slug do
pesquisador em `tags:` e, quando for orientação, também em
`advisors:`.

Exemplo:

```yaml
tags:
- gamification
- software_quality
- sergio_freitas
advisors:
- sergio_freitas
```

Regras:

- `advisors:` define vínculo de orientação.
- `tags:` define indexação temática e associação com páginas de
  pesquisador, categorias e listas de publicações.
- Se o autor CEDIS participa de um artigo mas não é orientador, ainda
  assim inclua o slug em `tags:`.
- Ao revisar publicações de um pesquisador, conferir se todas as
  entradas esperadas têm o slug correto; ausência do slug é a causa
  mais comum de publicação não aparecer no perfil.

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
