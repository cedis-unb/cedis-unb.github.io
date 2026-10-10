# Ecossistema CEDIS no portal — plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publicar no portal Hugo o projeto *Ecossistema CEDIS* com seus seis produtos, seis notícias de apresentação ao público externo, o encerramento do PIBIC 2025–2026 e o novo PIBIC em dupla de Davi e Daniel — conforme `docs-src/specs/2026-10-10-ecossistema-cedis-design.md`.

**Architecture:** Tudo é conteúdo e dados do site estático: YAML em `data/`, Markdown com frontmatter em `content/`, imagens em `assets/`, chaves em `i18n/`. Nenhum layout muda. As relações (projeto ↔ produtos ↔ pessoas ↔ notícias) são declaradas por ids em frontmatter e resolvidas pelos layouts existentes; o guarda-chuva *Inovação digital e gamificação* herda os seis produtos por ser `project_type: umbrella` com o Ecossistema como filho.

**Tech Stack:** Hugo (publishDir `docs/`), Python 3 (edições cirúrgicas em YAML preservando formatação), `npm test` (validadores), `lychee` (links), `gh` (push com a conta da organização).

## Global Constraints

- Data única do ecossistema: **`2026-08-09`**. Projeto e cinco produtos novos: `date: 2026-08-09T09:00:00-03:00`. Deck Manager mantém `2026-07-16T09:00:00-03:00`.
- Notícias: `news-post.035` a `news-post.040`, todas em 2026-08-09, horários exatos da tabela da Task 4; hub (035) às 10:00, por último.
- Ids de produto: `slides`, `concept_studio`, `atlas`, `passport`, `learning_analytics`. Id de projeto: `project_ecossistema_cedis`. Guarda-chuva: `project_inovacao_digital_gamificacao`.
- `status` dos produtos: `active`, exceto `learning_analytics: beta`.
- Responsável e pesquisador de tudo: `sergio_freitas`. Estudantes do projeto: `daniel_rodrigues_da_rocha`, `davi_rodrigues_da_rocha`.
- PIBIC antigo: `status: closed`, `end_date: 2026-10-10`. PIBIC novo: `year: 2027`, título PT `Learning Analytics do Ecossistema CEDIS`, EN `Learning Analytics for the CEDIS Ecosystem`.
- Todo arquivo de `content/` nasce em **PT e EN**. Nomes de produto são nomes próprios e não se traduzem; "Atlas do Conhecimento" ganha a glosa *(Knowledge Atlas)* na primeira ocorrência em EN.
- Nenhum número, funcionalidade ou data que não esteja nas fontes: `docs/ECOSSISTEMA-CEDIS.md`, `docs/marketing-brief.md`, `docs/atlas/{PRODUCT-VISION,STATUS}.md`, `docs/questionnaires/README.md`, `docs/learning-analytics/{00-executive-summary,22-roadmap}.md`, `CEDIS-identity-suite/brand-system.md`, `README.md` — todos em `~/workspace/github/projects/CEDIS-Deck-Manager`. Chame esse caminho de **`$DECK`** nos comandos.
- Nunca editar `docs/` à mão: é gerado por `npm run build`, em commit separado `chore(build): regenerate docs/ for publication`.
- Edições em `data/*.yaml` por script Python linha a linha (nunca `yaml.dump` do arquivo inteiro — destrói formatação e comentários).
- Push só com a conta `cedis-unb` (`gh auth switch`), restaurando `sergioaafreitas` logo depois.
- Commits com `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` e `-c user.name="Sergio Freitas"`.

---

## Mapa de arquivos

| Ação | Arquivo | Responsabilidade |
|---|---|---|
| criar | `assets/images/featured/{slides,concept_studio,atlas,passport,learning_analytics}-logo.png` | capas dos produtos (identity suite, horizontal 1240×360) |
| criar | `assets/images/featured/project_ecossistema_cedis.png` | capa do projeto (infográfico geral) |
| criar | `assets/images/posts/ecossistema-cedis-infografico-{geral,docentes,estudantes}.png` | infográficos embutidos no hub e no projeto |
| criar | `content/products/{slides,concept_studio,atlas,passport,learning_analytics}.{pt,en}.md` | cinco páginas de produto |
| modificar | `i18n/pt.yaml`, `i18n/en.yaml` | seis rótulos de id de produto |
| modificar | `data/projects.yaml` | `project_ecossistema_cedis`; PIBIC antigo fechado e com slugs |
| criar | `content/projects/ecossistema_cedis.{pt,en}.md` | página do projeto |
| modificar | `content/projects/inovacao_digital_gamificacao.{pt,en}.md` | deixa de listar `deckmanager`; linka o Ecossistema |
| modificar | `content/products/deckmanager.{pt,en}.md` | migra para o Ecossistema; frase da skill |
| criar | `content/posts/news-post.{035..040}.{pt,en}.md` | hub + cinco notícias de produto |
| modificar | `data/people.yaml` | Davi e Daniel em `supervisions[]` (2025 inactive + 2027 active); Mylena 2025 inactive |
| modificar | `content/projects/framework_preditivo_engajamento.{pt,en}.md` | concluído, estudantes por slug |
| modificar | `content/people/mylena_faria.{pt,en}.md` | resumo e participação no passado, `inactive` |

Ordem: assets → produtos + i18n → projeto + guarda-chuva + Deck Manager → notícias → PIBIC → verificação e publicação. `validate_project_pages` exige que os ids de `products:` existam, por isso produtos antes do projeto.

---

### Task 1: Assets — logos e infográficos

**Files:**
- Create: `assets/images/featured/slides-logo.png`, `concept_studio-logo.png`, `atlas-logo.png`, `passport-logo.png`, `learning_analytics-logo.png`, `project_ecossistema_cedis.png`
- Create: `assets/images/posts/ecossistema-cedis-infografico-geral.png`, `-docentes.png`, `-estudantes.png`

**Interfaces:**
- Produces: os caminhos acima, referenciados por `featured_image` (Tasks 2–4) e por `{{< imgc src="posts/…" >}}` (Tasks 3–4).

- [ ] **Step 1: Copiar os cinco logos horizontais da identity suite**

```bash
cd ~/workspace/github/homepages/cedis-unb.github.io
DECK=~/workspace/github/projects/CEDIS-Deck-Manager
S="$DECK/CEDIS-identity-suite"
cp "$S/cedis-slides-api/app/static/assets/identity/logo-horizontal-1240.png"               assets/images/featured/slides-logo.png
cp "$S/concepts/concepts_app/static/assets/identity/logo-horizontal-1240.png"             assets/images/featured/concept_studio-logo.png
cp "$S/atlas-api/app/static/assets/identity/logo-horizontal-1240.png"                     assets/images/featured/atlas-logo.png
cp "$S/cedis-slides-api/app/passport/static/assets/identity/logo-horizontal-1240.png"     assets/images/featured/passport-logo.png
cp "$S/learning-analytics/app/static/assets/identity/logo-horizontal-1240.png"            assets/images/featured/learning_analytics-logo.png
```

- [ ] **Step 2: Copiar os três infográficos (o geral também como capa do projeto)**

```bash
I="$DECK/Infográficos Ecossistema"
cp "$I/Cedis Deck Manager.infográfico.ALL.png"        assets/images/posts/ecossistema-cedis-infografico-geral.png
cp "$I/Cedis Deck Manager.infográfico.professor.png"  assets/images/posts/ecossistema-cedis-infografico-docentes.png
cp "$I/Cedis Deck Manager.infográfico.estudante.png"  assets/images/posts/ecossistema-cedis-infografico-estudantes.png
cp "$I/Cedis Deck Manager.infográfico.ALL.png"        assets/images/featured/project_ecossistema_cedis.png
```

- [ ] **Step 3: Verificar dimensões e que são os arquivos certos**

```bash
python3 - <<'PY'
from PIL import Image
for f in ["slides","concept_studio","atlas","passport","learning_analytics"]:
    im=Image.open(f"assets/images/featured/{f}-logo.png"); assert im.size==(1240,360), (f, im.size)
for f in ["geral","docentes","estudantes"]:
    im=Image.open(f"assets/images/posts/ecossistema-cedis-infografico-{f}.png"); assert im.width>=1400, (f, im.size)
print("assets ok")
PY
```
Expected: `assets ok`.

- [ ] **Step 4: Commit**

```bash
git add assets/images/featured assets/images/posts
git -c user.name="Sergio Freitas" commit -m "assets: logos dos produtos e infográficos do Ecossistema CEDIS

Logos: variante horizontal 1240x360 da CEDIS-identity-suite (mesma família
do deckmanager-logo.png). Infográficos: os três de 2026-08-09 do repositório
CEDIS-Deck-Manager (geral, docentes, estudantes).

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 2: Cinco páginas de produto + rótulos i18n

**Files:**
- Create: `content/products/{slides,concept_studio,atlas,passport,learning_analytics}.{pt,en}.md`
- Modify: `i18n/pt.yaml`, `i18n/en.yaml` (inserir chaves em ordem alfabética entre as existentes)

**Interfaces:**
- Consumes: logos da Task 1.
- Produces: ids `slides`, `concept_studio`, `atlas`, `passport`, `learning_analytics` — usados em `products:` do projeto (Task 3), em `tags`/`related_ids` das notícias (Task 4) e nas chaves i18n.

- [ ] **Step 1: Frontmatter PT — modelo e os cinco valores**

Esqueleto (idêntico ao de `content/products/deckmanager.pt.md`, exceto os campos da tabela):

```yaml
---
author: CEDIS
title: "<TÍTULO>"
date: 2026-08-09T09:00:00-03:00
language: pt
product_language: pt
id: <ID>
status: <STATUS>
project: project_ecossistema_cedis
areas:
<ÁREAS, uma por linha com "- ">
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/<ID>-logo.png"
summary: <RESUMO PT>
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_ecossistema_cedis
tags:
- app
<ÁREAS, uma por linha com "- ">
- project_ecossistema_cedis
---
```

| ID | TÍTULO | STATUS | ÁREAS | RESUMO PT |
|---|---|---|---|---|
| `slides` | CEDIS Slides | active | active_learning, digital_transformation | Runtime público das apresentações do CEDIS: serve os decks HTML aos estudantes, embute atividades e questionários, coleta respostas em tempo real e entrega ao docente o resumo ao vivo e a exportação em CSV. |
| `concept_studio` | CEDIS Concept Studio | active | active_learning, ai, learning_analytics | Ateliê semântico do docente: banco de conceitos, mapas conceituais versionados, extração assistida por IA com confirmação humana e o módulo de Questionários, que gera prática formativa embutida nos decks. |
| `atlas` | Atlas do Conhecimento | active | gamification, learning_analytics | Espaço pessoal e pseudônimo do estudante para ver o próprio percurso: progresso em quatro dimensões, rotas curadas, carimbos, diário, constelação de conceitos e bússola motivacional — sem ranking e com k-anonimato. |
| `passport` | CEDIS Learning Passport | active | digital_transformation, security | Identidade pseudônima do estudante no ecossistema: criada a partir de uma frase-semente, sem e-mail nem dado pessoal, com consentimento versionado, autorização por serviço e exclusão em cascata conforme a LGPD. |
| `learning_analytics` | CEDIS Learning Analytics | beta | learning_analytics, ai, machine_learning | Camada transversal que reúne os sinais de todo o ecossistema em um warehouse pseudonimizado com k-anonimato, para gerar indicadores e insights pedagógicos; ingestão e API em produção, dashboards docentes em construção. |

Em EN: `language: en`, `product_language: pt` (mantém), `summary` traduzido; os demais campos iguais.

- [ ] **Step 2: Corpo — seções obrigatórias e ficha de fatos por produto**

Seções, nesta ordem (PT / EN): `## Descrição do Projeto` / `## Project Description`; `## Objetivos do Projeto` / `## Project Objectives`; `## Recursos e Funcionalidades` / `## Resources and Features`; `## Vinculação Acadêmica e Apoio` / `## Academic Link and Support`; `## Acesso` / `## Access`. 350–500 palavras. "Vinculação" tem sempre três itens: `CEDIS (desenvolvimento e manutenção institucional)`, `Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordenação)`, `{{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}} (projeto de origem)`. "Acesso" cita o host como link e o repositório `https://github.com/cedis-unb/CEDIS-Deck-Manager` (licença MIT).

Fatos a usar — só estes (fonte: `$DECK/docs/ECOSSISTEMA-CEDIS.md`, salvo indicação):

**slides** — `slides.cedis.tec.br`. Quem usa: estudante (Passport opcional). Serve cada deck como um único HTML autocontido (CSS+JS embutidos). Navegação por teclado (setas, `n` notas, `f` tela cheia), swipe e botão de notas em touch. Atividades embutidas respondidas via `POST /api/responses`; código de sessão projetado pelo docente; resumo ao vivo em `/s/<deck>/<atividade>` (histograma, nuvem de tags, respostas frequentes); exportação CSV. Runtime dos questionários do Concept Studio (botão "Praticar"). Widget do Passport no canto inferior direito. Políticas de atividade vindas do Deck Manager (`always_open`, `class_window`, `presenter_only`, `scheduled`); fail-open na leitura, fail-closed no envio (README). Landing pública compartilhada com o Deck Manager. Analytics sem cookie de rastreio, DNT honrado, k=3 (README).

**concept_studio** — `concepts.cedis.tec.br`. Quem usa: docente (SSO). Banco de conceitos: criar, editar, mesclar, depreciar, promover (pessoal → pasta → CEDIS). Mapas conceituais por deck, versões imutáveis. Relações semânticas: pré-requisito, hierarquia, parte-de, contraste, confusão comum, relacionado. Extração assistida por IA (provider configurável: OpenAI, Anthropic ou stub local) — o docente confirma ou rejeita cada candidato; proveniência registrada (provider, modelo, versão do prompt, hash da entrada — `00-executive-summary.md`). Workspace com três regiões (material do deck, conceitos, sugestões), drag-and-drop. **Questionários**: banco de questões ligadas a conceitos, practice sets publicados para o Slides, feedback imediato ao aluno, página `/questionnaires/analytics` (taxa de acerto, tempo médio, questões mais erradas); tipos `single_choice`, `likert_5`, `semantic_differential_5`, `confidence_5`, `multiple_select`, `true_false`, `numeric`, `open_short`; ativação gradual por feature flag; fora de escopo por design: nota somativa, ranking, certificação (`docs/questionnaires/README.md`). Fornece as relações que viram linhas na constelação do Atlas.

**atlas** — `atlas.cedis.tec.br`. Quem usa: estudante, vindo do Passport por handoff com código de uso único. Não é LMS, não avalia, não emite certificado, não tem ranking nem comparação social (`PRODUCT-VISION.md`). Progresso 4D: exploração, prática, consolidação, reflexão — sem score único. `/mapa` (rotas como territórios, destinos com anéis por eixo), `/rotas` curadas pelo docente, `/carimbos` (monotônicos, nunca expiram; 12 por padrão), `/diario` (automático + manual), `/constelacao` (grafo dos conceitos tocados, com relações do Concept Studio), `/bussola` (perfil motivacional Octalysis, opt-in explícito, desligável), `/proximos-passos` (cinco heurísticas transparentes, sem ML), `/configuracoes` (exportar tudo em ZIP, desvincular com exclusão em cascata). Admin do docente dentro do Deck Manager em `/admin/atlas/*` com dashboard k-anônimo (K=5; buckets menores aparecem como "<5"). Latência típica evento → Atlas ~30 s (outbox + ingest). Estado: em produção desde agosto de 2026 (`STATUS.md` 2026-08-07).

**passport** — `passport.cedis.tec.br`. Quem usa: estudante. Criação sem dado pessoal: frase-semente de 12 palavras (tipo BIP39); sem e-mail, matrícula, CPF ou nome. Recuperação pela própria frase (não existe "esqueci minha senha"). Painel com o próprio percurso agrupado por deck; botão "apagar meu passaporte" com exclusão em cascata em Slides, Atlas e Concept Studio. Provedor OIDC leve para os outros serviços. Identificador que cruza fronteiras: `subject_hash` (HMAC, escopado por serviço). Consent bundle imutável: três documentos (manifestação, aviso de privacidade, termos) com hash SHA-256, trilha de aceite append-only, autorização granular por serviço, política de re-consentimento classificada; base legal LGPD art. 7º I + art. 46 §2 (`CLAUDE.md`). Por que existe: feedback pedagógico personalizado numa universidade pública sem armazenar e-mail institucional em sistemas de analytics.

**learning_analytics** — `analytics.cedis.tec.br`. Transversal, nos bastidores. Warehouse pseudonimizado alimentado pelos eventos de Slides, Atlas e Concept Studio (`cedis-la-ingest`), API (`cedis-la-api`) com K-anonimato ≥ 5, identidade analítica dedicada ligada a consentimento específico que o estudante pode revogar — revogação cascateia até o warehouse em um ciclo (DISCOVERY, status 2026-08-10). Objetivo: indicadores de engajamento e progresso, detecção de dificuldades, recomendações, correlações entre atividades, conceitos e desempenho (infográfico). **Estado, em texto claro:** ingestão, API e cascata LGPD em produção; a interface docente (dashboards) ainda em construção — por isso `beta`. Fundamentação: auditoria de descoberta de 2026-08-09 com 25 capítulos e roadmap por fases (`docs/learning-analytics/`). Em "Vinculação", acrescentar: `Iniciação científica PIBIC 2026–2027 de Daniel Rodrigues da Rocha e Davi Rodrigues da Rocha, orientados pelo Prof. Sergio Freitas`.

- [ ] **Step 3: Escrever os dez arquivos**

Escreva `content/products/<id>.pt.md` e `<id>.en.md` para os cinco ids com o frontmatter do Step 1 e o corpo do Step 2. EN é redação própria, não tradução literal; mantém os mesmos fatos e links.

- [ ] **Step 4: Chaves i18n**

```bash
python3 - <<'PY'
import pathlib
keys = {
 'pt': {'atlas':'Atlas do Conhecimento','concept_studio':'CEDIS Concept Studio','deckmanager':'CEDIS Deck Manager',
        'learning_analytics':'CEDIS Learning Analytics','passport':'CEDIS Learning Passport','slides':'CEDIS Slides'},
 'en': {'atlas':'Atlas do Conhecimento (Knowledge Atlas)','concept_studio':'CEDIS Concept Studio','deckmanager':'CEDIS Deck Manager',
        'learning_analytics':'CEDIS Learning Analytics','passport':'CEDIS Learning Passport','slides':'CEDIS Slides'},
}
for lang, kv in keys.items():
    p = pathlib.Path(f'i18n/{lang}.yaml'); lines = p.read_text(encoding='utf-8').splitlines(keepends=True)
    for k, v in kv.items():
        assert not any(l.startswith(f'{k}:') for l in lines), f'{k} já existe em {lang}'
        # insere antes da primeira chave de topo alfabeticamente maior (chaves de topo começam na coluna 0)
        idx = next((i for i, l in enumerate(lines) if l[:1].isalpha() and l.split(':')[0] > k), len(lines))
        lines.insert(idx, f'{k}: "{v}"\n')
    p.write_text(''.join(lines), encoding='utf-8'); print(lang, 'ok')
PY
grep -nE "^(atlas|concept_studio|deckmanager|learning_analytics|passport|slides):" i18n/pt.yaml i18n/en.yaml
```
Expected: 12 linhas (6 por idioma).

- [ ] **Step 5: Validar**

```bash
python3 scripts/validate_content.py && python3 scripts/validate_i18n.py
```
Expected: `Total: 0 erros, 0 warnings.` e `Total: 0 erros.` (o projeto ainda não existe, mas produtos não são validados contra projeto).

- [ ] **Step 6: Commit**

```bash
git add content/products i18n
git -c user.name="Sergio Freitas" commit -m "feat(products): cinco produtos do Ecossistema CEDIS

CEDIS Slides, CEDIS Concept Studio, Atlas do Conhecimento, CEDIS Learning
Passport e CEDIS Learning Analytics, datados de 2026-08-09 — o dia em que a
família virou seis produtos — e vinculados ao projeto Ecossistema CEDIS.
Learning Analytics entra como beta: ingestão, API e K-anonimato estão em
produção, os dashboards docentes não. Seis chaves i18n para os ids de produto
(inclui deckmanager, que não tinha rótulo).

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 3: Projeto Ecossistema CEDIS, guarda-chuva e migração do Deck Manager

**Files:**
- Modify: `data/projects.yaml` (inserir antes de `  - id: project_framework_preditivo_engajamento`)
- Create: `content/projects/ecossistema_cedis.{pt,en}.md`
- Modify: `content/projects/inovacao_digital_gamificacao.{pt,en}.md` (linhas 22–28 `products:`; linha 104 bullet)
- Modify: `content/products/deckmanager.{pt,en}.md` (`project:`, categories, tags, "Vinculação", linha 53)

**Interfaces:**
- Consumes: ids dos produtos (Task 2), assets (Task 1).
- Produces: `project_ecossistema_cedis` — usado em tags/related_ids das notícias (Task 4) e nas tags do novo PIBIC (Task 5).

- [ ] **Step 1: `data/projects.yaml`**

```bash
python3 - <<'PY'
import pathlib
p=pathlib.Path('data/projects.yaml'); t=p.read_text(encoding='utf-8')
anchor="  - id: project_framework_preditivo_engajamento\n"
assert anchor in t and 'project_ecossistema_cedis' not in t
block = """  - id: project_ecossistema_cedis
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

"""
p.write_text(t.replace(anchor, block+anchor,1), encoding='utf-8'); print('projects.yaml ok')
PY
```

- [ ] **Step 2: `content/projects/ecossistema_cedis.pt.md` — frontmatter**

```yaml
---
author: CEDIS
title: "Ecossistema CEDIS"
date: 2026-08-09T09:00:00-03:00
language: pt
status: ongoing
start_date: 2026-08-09
id: project_ecossistema_cedis
project_type: project
umbrella_projects:
- project_inovacao_digital_gamificacao
researchers:
- sergio_freitas
students:
- daniel_rodrigues_da_rocha
- davi_rodrigues_da_rocha
areas:
- learning_analytics
- active_learning
- digital_transformation
- gamification
partners: []
funding_agencies: []
products:
- deckmanager
- slides
- concept_studio
- atlas
- passport
- learning_analytics
publications: []
summary: "Seis produtos integrados — Deck Manager, Slides, Concept Studio, Atlas do Conhecimento, Learning Passport e Learning Analytics — que transformam conteúdo em experiências de aprendizagem com dados e inteligência a serviço de docentes e estudantes, com privacidade por design."
featured_image: "../assets/images/featured/project_ecossistema_cedis.png"
authorimage: ../assets/images/global/author.webp
categories:
- project
- sergio_freitas
- project_ecossistema_cedis
- project_inovacao_digital_gamificacao
tags:
- learning_analytics
- active_learning
- digital_transformation
- gamification
- project_ecossistema_cedis
- project_inovacao_digital_gamificacao
---
```
EN: `language: en`, `title: "CEDIS Ecosystem"`, `summary` traduzido; resto igual.

- [ ] **Step 3: Corpo do projeto (PT e EN), seções e fatos**

1. `## Visão geral` — "**Projeto em andamento.** Período: 2026-Atual." Seis aplicações web independentes, cada uma com subdomínio e banco Postgres próprios, conversando por APIs assinadas (HMAC, OAuth2/OIDC). Começou em julho de 2026 com o Deck Manager e consolidou-se como família de seis em 9 de agosto de 2026. Código aberto, MIT, monorepo `https://github.com/cedis-unb/CEDIS-Deck-Manager`. Lema do infográfico: "Aprender. Ensinar. Conectar."
2. `## A jornada: do conteúdo ao insight` — lista numerada 1–7 do infográfico: (1) docente cria e organiza no Deck Manager; (2) apresenta as aulas no Slides, com interações; (3) explora conceitos e aplica questionários no Concept Studio; (4) estudantes avançam no Atlas do Conhecimento; (5) aprendizagem registrada com segurança no Learning Passport; (6) Learning Analytics agrega sinais de todo o ecossistema; (7) docente decide melhor, personaliza o ensino e apoia cada estudante.
3. `## Os seis produtos` — seis parágrafos, cada um abrindo com `{{< link-interno "/products/<id>" "<Título>" >}}` e o host, com uma frase do infográfico e uma do ECOSSISTEMA: Deck Manager "seu cockpit completo" (deck.cedis.tec.br); Slides "onde a aula acontece"; Concept Studio "crie, conecte e avalie" (questionários fazem parte dele e chegam aos estudantes via Slides); Atlas "sua jornada épica"; Passport "sua identidade, seus dados"; Learning Analytics "dados que viram decisões melhores".
4. `## Privacidade em primeiro lugar` — as seis regras de ouro de `ECOSSISTEMA-CEDIS.md`: pseudonímia ponta a ponta (`subject_hash`), sem ranking público, sem manipulação (drivers Octalysis "escuros" só como informação ao próprio aluno), LGPD nativa (unlink cascateia; exportação em ZIP), feature flags nascem desligadas, falha silenciosa entre serviços (nenhum serviço bloqueia outro). K-anonimato: K=5 no Atlas, K=3 no Slides.
5. `## Estado atual` — cinco produtos em produção; Learning Analytics com ingestão, API e cascata LGPD no ar e dashboards docentes em construção.
6. `## Equipe` — Prof. Sergio (coordenação e desenvolvimento) via `link-interno`; "Iniciação científica PIBIC 2026–2027: Daniel Rodrigues da Rocha e Davi Rodrigues da Rocha — *Learning Analytics do Ecossistema CEDIS*" (sem link: não têm página).
7. `## Material de divulgação` — três chamadas `{{< imgc src="posts/ecossistema-cedis-infografico-geral.png" alt="Infográfico: panorama do Ecossistema CEDIS" >}}`, `…-docentes.png` ("Ecossistema CEDIS para professores"), `…-estudantes.png` ("Ecossistema CEDIS para estudantes").

- [ ] **Step 4: Guarda-chuva deixa de listar o Deck Manager (PT e EN)**

```bash
python3 - <<'PY'
import pathlib
for lang in ('pt','en'):
    p=pathlib.Path(f'content/projects/inovacao_digital_gamificacao.{lang}.md'); t=p.read_text(encoding='utf-8')
    assert t.count('- deckmanager\n')==1
    t=t.replace('- deckmanager\n','',1)
    old='- {{< link-interno "/products/deckmanager" "CEDIS Deck Manager" >}}\n'
    new=('- {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}}'
         + (' (Deck Manager, Slides, Concept Studio, Atlas do Conhecimento, Learning Passport e Learning Analytics)\n' if lang=='pt'
            else ' (Deck Manager, Slides, Concept Studio, Atlas do Conhecimento, Learning Passport and Learning Analytics)\n'))
    assert old in t; t=t.replace(old,new,1)
    p.write_text(t,encoding='utf-8'); print(lang,'ok')
PY
```

- [ ] **Step 5: Deck Manager migra (PT e EN)**

```bash
python3 - <<'PY'
import pathlib
for lang in ('pt','en'):
    p=pathlib.Path(f'content/products/deckmanager.{lang}.md'); t=p.read_text(encoding='utf-8')
    assert t.count('project_inovacao_digital_gamificacao')==3  # project:, categories, tags
    t=t.replace('project: project_inovacao_digital_gamificacao','project: project_ecossistema_cedis')
    t=t.replace('- project_inovacao_digital_gamificacao\n','- project_ecossistema_cedis\n')
    # frase da skill: hoje só cita ChatGPT/Codex; o repo distribui também a variante para Claude Code
    t=t.replace('(ChatGPT/Codex)','(ChatGPT/Codex e Claude Code)' if lang=='pt' else '(ChatGPT/Codex and Claude Code)')
    if lang=='pt':
        old='- {{< link-interno "/projects/inovacao_digital_gamificacao" "Inovação digital e gamificação para o ensino, divulgação e engenharia de software" >}} (projeto de origem)\n'
        new='- {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}} (projeto de origem, dentro de {{< link-interno "/projects/inovacao_digital_gamificacao" "Inovação digital e gamificação" >}})\n'
        assert old in t; t=t.replace(old,new,1)
    else:
        old='- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordination)\n'
        new=old+'- {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}} (origin project, within {{< link-interno "/projects/inovacao_digital_gamificacao" "Digital innovation and gamification" >}})\n'
        assert old in t; t=t.replace(old,new,1)
    p.write_text(t,encoding='utf-8'); print(lang,'ok')
PY
```

- [ ] **Step 6: Validar e conferir relações no build**

```bash
npm test 2>&1 | grep -E "^Total"
hugo --quiet --destination /tmp/eco-t3 && python3 - <<'PY'
import re,pathlib
t=pathlib.Path('/tmp/eco-t3/pt/projects/ecossistema_cedis/index.html').read_text()
ids=['deckmanager','slides','concept_studio','atlas','passport','learning_analytics']
print('produtos no projeto:', [i for i in ids if f'/pt/products/{i}' in t])
u=pathlib.Path('/tmp/eco-t3/pt/projects/inovacao_digital_gamificacao/index.html').read_text()
print('guarda-chuva lista Ecossistema:', '/pt/projects/ecossistema_cedis' in u, '| herda deckmanager:', '/pt/products/deckmanager' in u)
c=pathlib.Path('/tmp/eco-t3/pt/categories/products/index.html').read_text()
print('catálogo cita o Ecossistema:', c.count('/pt/projects/ecossistema_cedis'))
PY
```
Expected: os seis ids listados; `True | True`; contagem ≥ 6.

- [ ] **Step 7: Commit**

```bash
git add data/projects.yaml content/projects/ecossistema_cedis.pt.md content/projects/ecossistema_cedis.en.md content/projects/inovacao_digital_gamificacao.pt.md content/projects/inovacao_digital_gamificacao.en.md content/products/deckmanager.pt.md content/products/deckmanager.en.md
git -c user.name="Sergio Freitas" commit -m "feat(projects): criar o projeto Ecossistema CEDIS e migrar o Deck Manager

Subprojeto de Inovação digital e gamificação, com os seis produtos, a
jornada do conteúdo ao insight, as regras de privacidade do ecossistema e os
três infográficos de 2026-08-09. O Deck Manager passa a ter o Ecossistema
como projeto de origem; o guarda-chuva deixa de listá-lo diretamente e o
herda como umbrella. A frase da skill passa a citar as duas variantes
distribuídas (ChatGPT/Codex e Claude Code).

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 4: Seis notícias (news-post.035–040)

**Files:**
- Create: `content/posts/news-post.{035,036,037,038,039,040}.{pt,en}.md`

**Interfaces:**
- Consumes: ids de produto (Task 2), `project_ecossistema_cedis` (Task 3), assets (Task 1).

- [ ] **Step 1: Frontmatter modelo (PT) e tabela**

```yaml
---
title: "<TÍTULO>"
date: 2026-08-09T<HORA>:00-03:00
draft: false
weight: 500
language: pt
featured_image: "../assets/images/<CAPA>"
summary: "<RESUMO>"
description: "<DESCRIÇÃO CURTA>"
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
<ÁREAS do produto, "- ">
- project_ecossistema_cedis
- <ID DO PRODUTO>            # omitir no hub
related_ids:
- <ID DO PRODUTO>            # omitir no hub
- project_ecossistema_cedis
- sergio_freitas
---
```

| nº | HORA | ID | CAPA | TÍTULO PT |
|---|---|---|---|---|
| 035 | 10:00 | — | `featured/project_ecossistema_cedis.png` | CEDIS apresenta o Ecossistema CEDIS: seis produtos, uma jornada do conteúdo ao insight |
| 036 | 09:00 | slides | `featured/slides-logo.png` | CEDIS Slides: a aula acontece no navegador, com respostas e resumo ao vivo |
| 037 | 09:10 | concept_studio | `featured/concept_studio-logo.png` | CEDIS Concept Studio: mapas conceituais, IA com revisão humana e questionários dentro da aula |
| 038 | 09:20 | atlas | `featured/atlas-logo.png` | Atlas do Conhecimento: o estudante vê o próprio percurso, sem ranking e sem expor quem é |
| 039 | 09:30 | passport | `featured/passport-logo.png` | CEDIS Learning Passport: uma identidade de aprendiz sem e-mail, sem CPF e sob controle do estudante |
| 040 | 09:40 | learning_analytics | `featured/learning_analytics-logo.png` | CEDIS Learning Analytics: os dados de todo o ecossistema viram evidência pedagógica — com privacidade por design |

Títulos EN são redação própria com a mesma ideia. Tags do hub: `News`, as quatro áreas do projeto, `project_ecossistema_cedis`.

- [ ] **Step 2: Corpo — regras e conteúdo**

Abertura: `Brasília, 9 de agosto de 2026` (PT) / `Brasilia, August 9, 2026` (EN). 300–400 palavras, estilo jornalístico, sem template entre as seis: variar o gancho (problema do docente; dado do estudante; contraste com SaaS comercial — `marketing-brief.md` §2 e §7; metáfora do produto — `brand-system.md`). Cada notícia de produto: o problema, o que o produto faz (fatos da Task 2 Step 2), onde ele entra na jornada de sete passos, uma frase honesta de estado, e fecha com o host (link) e `{{< link-interno "/posts/news-post.035" "a apresentação do Ecossistema CEDIS" >}}`. Mencionar `{{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}}` como coordenador e a página do produto via `link-interno`.

Hub (035): abre com o lema "Aprender. Ensinar. Conectar." e a frase do infográfico "Seis produtos. Um ecossistema. Uma missão: transformar conhecimento em impacto."; um parágrafo por produto com `link-interno`; a jornada em sete passos; "Privacidade em primeiro lugar" (sem e-mail e sem PII por padrão, identidade pseudônima, LGPD por design, você decide o que compartilhar — infográfico); os três infográficos com `{{< imgc src="posts/ecossistema-cedis-infografico-<geral|docentes|estudantes>.png" alt="…" >}}`; fecha com o repositório e o `link-interno` para `/projects/ecossistema_cedis`.

- [ ] **Step 3: Escrever os doze arquivos e validar**

```bash
python3 scripts/validate_content.py && python3 scripts/validate_i18n.py
hugo --quiet --destination /tmp/eco-t4 && python3 - <<'PY'
import re,pathlib,os
for n in range(35,41):
    for lang,base in (('pt','/pt/'),('en','/')):
        p=f'/tmp/eco-t4{base}posts/news-post.0{n}/index.html'
        t=pathlib.Path(p).read_text()
        hrefs=[h for h in dict.fromkeys(re.findall(r'href="?(/[^" >]+)', t)) if re.match(r'/(pt/)?(products|projects|people|posts)/',h)]
        bad=[h for h in hrefs if not os.path.isfile('/tmp/eco-t4'+h.rstrip('/')+'/index.html')]
        print(f'0{n} {lang}: links={len(hrefs)} quebrados={bad} shortcode_cru={"{{<" in t}')
PY
```
Expected: `quebrados=[]` e `shortcode_cru=False` em todas as doze.

- [ ] **Step 4: Confirmar que a notícia fixada não muda**

```bash
python3 -c "
import re,pathlib
t=pathlib.Path('/tmp/eco-t4/pt/categories/news/index.html').read_text()
print([h for h in dict.fromkeys(re.findall(r'href=\"?(/pt/posts/[^\" >]+)', t))][:3])"
```
Expected: primeiro item `/pt/posts/news-post.034/` (chamamento fixado), e as seis novas aparecem depois das de setembro/julho conforme a data.

- [ ] **Step 5: Commit**

```bash
git add content/posts/news-post.03[5-9].*.md content/posts/news-post.040.*.md
git -c user.name="Sergio Freitas" commit -m "content(posts): seis notícias de apresentação do Ecossistema CEDIS

Um hub (035) com os três infográficos e uma notícia por produto (036–040),
todas em 2026-08-09 com horários escalonados para ordem determinística —
hub por último, para liderar as seis nas listagens. Redação para público
externo a partir do ECOSSISTEMA-CEDIS.md, do brief de divulgação e da
documentação de cada produto; nada afirmado fora dessas fontes. O chamamento
do Software para o Bem segue fixado — estas são dois meses mais antigas.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 5: PIBIC — encerramento do antigo e abertura do novo

**Files:**
- Modify: `data/people.yaml` (blocos `- name: Daniel Rodrigues da Rocha` ~L422 e `- name: Davi Rodrigues da Rocha` ~L441; Mylena, supervision 2025)
- Modify: `data/projects.yaml` (bloco `project_framework_preditivo_engajamento`)
- Modify: `content/projects/framework_preditivo_engajamento.{pt,en}.md`
- Modify: `content/people/mylena_faria.{pt,en}.md`

**Interfaces:**
- Consumes: `project_ecossistema_cedis` (Task 3).
- Produces: slugs de Davi e Daniel aparecendo como orientação atual de `sergio_freitas` e como estudantes do Ecossistema.

- [ ] **Step 1: Davi e Daniel → `supervisions[]` (2025 inactive + 2027 active)**

```bash
python3 - <<'PY'
import pathlib,re
p=pathlib.Path('data/people.yaml'); lines=p.read_text(encoding='utf-8').splitlines(keepends=True)
def block(slug):
    i=next(k for k,l in enumerate(lines) if l.strip()==f'slug: {slug}')
    s=next(k for k in range(i,-1,-1) if re.match(r'^-\s+name:',lines[k]))
    e=next((k for k in range(s+1,len(lines)) if re.match(r'^-\s+name:',lines[k])),len(lines))
    return s,e
for name,slug in (("Daniel Rodrigues da Rocha","daniel_rodrigues_da_rocha"),("Davi Rodrigues da Rocha","davi_rodrigues_da_rocha")):
    s,e=block(slug); old=''.join(lines[s:e])
    assert '- active\n' in old and 'supervisions' not in old, slug
    new=f"""- name: {name}
  slug: {slug}
  supervisions:
  - categories:
    - people
    - scientific_initiation
    title:
      pt: Learning Analytics do Ecossistema CEDIS
      en: Learning Analytics for the CEDIS Ecosystem
    program: curso_esw2
    advisors:
    - sergio_freitas
    tags:
    - active
    - learning_analytics
    - ai
    - machine_learning
    - project_ecossistema_cedis
    year: 2027
  - categories:
    - people
    - scientific_initiation
    title:
      pt: Framework preditivo de engajamento e desempenho discente em ambientes de aprendizagem gamificados com base em Octalysis, indicadores neurocientíficos e machine learning
      en: Predictive Framework for Student Engagement and Performance in Gamified Learning Environments Based on Octalysis, Neuroscientific Indicators, and Machine Learning
    program: curso_esw2
    advisors:
    - sergio_freitas
    tags:
    - inactive
    - gamification
    - machine_learning
    - ai
    - learning_analytics
    - project_framework_preditivo_engajamento
    year: 2025
"""
    lines[s:e]=[new]; print(slug,'ok')
p.write_text(''.join(lines),encoding='utf-8')
PY
```

- [ ] **Step 2: Mylena 2025 → inactive**

```bash
python3 - <<'PY'
import pathlib,re
p=pathlib.Path('data/people.yaml'); lines=p.read_text(encoding='utf-8').splitlines(keepends=True)
i=next(k for k,l in enumerate(lines) if l.strip()=='slug: mylena_faria')
j=next(k for k in range(i,len(lines)) if 'project_framework_preditivo_engajamento' in lines[k])
k=next(k for k in range(j,i,-1) if lines[k].strip()=='- active')   # a tag active imediatamente acima, na mesma supervision
lines[k]=lines[k].replace('- active','- inactive'); p.write_text(''.join(lines),encoding='utf-8'); print('mylena ok')
PY
python3 -c "
import yaml
d=yaml.safe_load(open('data/people.yaml'))
for p in d['people']:
    if p['slug'] in ('daniel_rodrigues_da_rocha','davi_rodrigues_da_rocha','mylena_faria'):
        for u in p.get('supervisions') or [p]:
            print(f\"  {p['slug']:28s} {u['year']} {'active' if 'active' in u['tags'] else 'inactive':8s} {u['title']['pt'][:48]}\")"
```
Expected: Daniel e Davi com `2027 active Learning Analytics…` e `2025 inactive Framework…`; Mylena com `2025 inactive Framework…`, `2024 inactive`, `2025 inactive Atloria`.

- [ ] **Step 3: `data/projects.yaml` — PIBIC antigo fechado, estudantes por slug**

```bash
python3 - <<'PY'
import pathlib,re
p=pathlib.Path('data/projects.yaml'); lines=p.read_text(encoding='utf-8').splitlines(keepends=True)
i=next(k for k,l in enumerate(lines) if l.strip()=='- id: project_framework_preditivo_engajamento')
e=next((k for k in range(i+1,len(lines)) if re.match(r'^\s*-\s+id:\s',lines[k])),len(lines))
blk=lines[i:e]
def setl(pat,val):
    for k,l in enumerate(blk):
        if re.match(pat,l): ind=re.match(r'^(\s*)',l).group(1); blk[k]=f'{ind}{val}\n'; return
    raise AssertionError(pat)
setl(r'^\s*status:','status: closed'); setl(r'^\s*end_date:','end_date: 2026-10-10')
m={'- Daniel Rodrigues da Rocha':'- daniel_rodrigues_da_rocha','- Davi Rodrigues da Rocha':'- davi_rodrigues_da_rocha','- Mylena Angélica Silva Farias':'- mylena_faria'}
for k,l in enumerate(blk):
    for a,b in m.items():
        if l.strip()==a: blk[k]=l.replace(a,b)
lines[i:e]=blk; p.write_text(''.join(lines),encoding='utf-8'); print('framework fechado')
PY
```

- [ ] **Step 4: Página do PIBIC antigo (PT e EN)**

Frontmatter: `status: closed`, `end_date: 2026-10-10`, `students:` com os três slugs. Corpo PT: em "Visão geral", `**Projeto em andamento.** Período informado: PIBIC 2025-2026.` → `**Projeto concluído.** Período: PIBIC 2025–2026, bolsas encerradas em outubro de 2026.`; em "Dados gerais", `| Situação | Em andamento |` → `| Situação | Concluído (bolsas PIBIC encerradas em outubro de 2026) |`; tabela "Equipe": as três linhas de estudantes passam a `{{< link-interno "/people/…" … >}}` quando houver página (só Mylena: `/people/mylena_faria`) e ao passado ("foi estudante de iniciação científica orientado(a) pelo Prof. Sergio, 2025–2026"). Acrescentar após a tabela: `Daniel e Davi seguem no CEDIS em novo PIBIC (2026–2027), *Learning Analytics do Ecossistema CEDIS*, vinculado ao {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}}.` EN equivalente (`**Completed project.**`, `| Status | Completed (PIBIC scholarships ended in October 2026) |`).

```bash
python3 - <<'PY'
import pathlib
for lang in ('pt','en'):
    p=pathlib.Path(f'content/projects/framework_preditivo_engajamento.{lang}.md'); t=p.read_text(encoding='utf-8')
    t=t.replace('status: ongoing\n','status: closed\n',1).replace('end_date: 2026-12-31\n','end_date: 2026-10-10\n',1)
    t=t.replace('- Daniel Rodrigues da Rocha\n','- daniel_rodrigues_da_rocha\n',1).replace('- Davi Rodrigues da Rocha\n','- davi_rodrigues_da_rocha\n',1).replace('- Mylena Angélica Silva Farias\n','- mylena_faria\n',1)
    assert 'status: closed' in t and '- mylena_faria\n' in t
    p.write_text(t,encoding='utf-8'); print(lang,'frontmatter ok')
PY
```
Depois, editar o corpo (Visão geral, Dados gerais, Equipe) conforme o parágrafo acima, nos dois idiomas.

- [ ] **Step 5: Mylena (PT e EN)**

PT: `summary:` → `Graduanda em Engenharia de Software na Universidade de Brasília; foi orientanda PIBIC do Prof. Sergio Freitas nos projetos Canal Ciência (2024) e Framework preditivo de engajamento (2025–2026).`; tag `- active` → `- inactive`; bullet "Participação CEDIS" → `foi orientanda PIBIC do Prof. … no … Projeto Canal Ciência (2024) e no projeto … Framework preditivo … (2025–2026, bolsa encerrada em outubro de 2026); autora do TCC que deu origem ao {{< link-interno "/products/atloria" "Atloria" >}} (2025).` EN equivalente (`was a PIBIC undergraduate research advisee … scholarship ended in October 2026`).

- [ ] **Step 6: Validar e conferir no build**

```bash
npm test 2>&1 | grep -E "^Total"
hugo --quiet --destination /tmp/eco-t5 && python3 - <<'PY'
import re,pathlib
s=pathlib.Path('/tmp/eco-t5/pt/people/sergio_freitas/index.html').read_text()
i=s.find('Orientações atuais'); seg=s[i:i+20000]
print('dupla em Orientações atuais do Sergio:', 'Daniel Rodrigues da Rocha' in seg and 'Davi Rodrigues da Rocha' in seg)
f=pathlib.Path('/tmp/eco-t5/pt/projects/framework_preditivo_engajamento/index.html').read_text()
print('PIBIC antigo linka Mylena:', '/pt/people/mylena_faria' in f, '| diz concluído:', 'Projeto concluído' in f)
e=pathlib.Path('/tmp/eco-t5/pt/projects/ecossistema_cedis/index.html').read_text()
print('Ecossistema cita a dupla:', 'Daniel Rodrigues da Rocha' in e and 'Davi Rodrigues da Rocha' in e)
a=pathlib.Path('/tmp/eco-t5/pt/people/all/index.html').read_text()
print('rede ativa cita Learning Analytics do Ecossistema:', 'Learning Analytics do Ecossistema CEDIS' in a)
PY
```
Expected: quatro `True`.

- [ ] **Step 7: Commit**

```bash
git add data/people.yaml data/projects.yaml content/projects/framework_preditivo_engajamento.pt.md content/projects/framework_preditivo_engajamento.en.md content/people/mylena_faria.pt.md content/people/mylena_faria.en.md
git -c user.name="Sergio Freitas" commit -m "fix(people): encerrar o PIBIC 2025–2026 e abrir o novo PIBIC em dupla

Framework preditivo de engajamento passa a closed, end_date 2026-10-10
(bolsas encerradas em outubro); Davi, Daniel e Mylena ficam inactive nessa
orientação. students[] deixa de usar nomes completos e passa a slugs — o
layout não resolvia nomes e os três apareciam sem link. Mylena deixa de ser
'orientanda PIBIC no Canal Ciência', projeto fechado.

Davi e Daniel abrem novo PIBIC em dupla, 2026–2027, 'Learning Analytics do
Ecossistema CEDIS', orientador Sergio Freitas, vinculado ao projeto
Ecossistema CEDIS — entrada em formato supervisions[], como a da Mylena,
preservando o histórico de 2025.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 6: Verificação completa, publicação e confirmação no ar

**Files:**
- Modify (gerado): `docs/**`

- [ ] **Step 1: Suíte completa**

```bash
npm test 2>&1 | grep -E "^Total"
npm run build 2>&1 | grep -iE "error|Total in|Finished" ; npm run validate:rendered 2>&1 | tail -1
lychee --offline --no-progress --root-dir "$PWD/docs" --exclude '^https?://' 'docs/**/*.html' 2>&1 | tail -1
```
Expected: `0 erros, 0 warnings` / `0 erros`; `Rendered HTML OK`; lychee `🚫 0 Errors`.

- [ ] **Step 2: Inspeção das páginas do §7 do spec**

```bash
for u in pt/projects/ecossistema_cedis pt/products/slides pt/products/concept_studio pt/products/atlas pt/products/passport pt/products/learning_analytics pt/posts/news-post.035 pt/posts/news-post.040 pt/projects/framework_preditivo_engajamento projects/ecossistema_cedis products/learning_analytics posts/news-post.035; do
  [ -f "docs/$u/index.html" ] && echo "  OK  /$u/" || echo "  FALTA /$u/"; done
grep -c 'imgc\|ecossistema-cedis-infografico' docs/pt/projects/ecossistema_cedis/index.html
head -5 docs/build.txt | tail -2
```
Expected: tudo `OK`; infográficos ≥ 3; `dirty=no`.

- [ ] **Step 3: Commit do build e push**

```bash
git add docs && git -c user.name="Sergio Freitas" commit -m "chore(build): regenerate docs/ for publication

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
gh auth switch --hostname github.com --user cedis-unb >/dev/null 2>&1
git push origin main 2>&1 | tail -2
gh auth switch --hostname github.com --user sergioaafreitas >/dev/null 2>&1
echo "conta ativa: $(gh auth status 2>&1 | grep -B1 'Active account: true' | head -1 | sed 's/.*account //;s/ .*//')"
```
Expected: `main -> main` e conta ativa `sergioaafreitas`.

- [ ] **Step 4: Confirmar no ar por conteúdo (não pelo carimbo)**

```bash
gh run watch $(gh run list --limit 6 --json databaseId,name --jq '[.[] | select(.name=="pages build and deployment")][0].databaseId') --exit-status --interval 15 >/dev/null 2>&1
for u in pt/projects/ecossistema_cedis pt/products/learning_analytics pt/posts/news-post.035 pt/projects/framework_preditivo_engajamento; do
  printf "  HTTP %s  /%s/\n" "$(curl -s -o /dev/null -w '%{http_code}' --max-time 25 -H 'Cache-Control: no-cache' "https://cedis.unb.br/$u/?cb=$RANDOM")" "$u"; done
echo "  dupla no perfil do Sergio: $(curl -s --max-time 25 "https://cedis.unb.br/pt/people/sergio_freitas/" | grep -c 'Learning Analytics do Ecossistema CEDIS')"
echo "  carimbo: $(curl -s --max-time 25 -H 'Cache-Control: no-cache' "https://cedis.unb.br/build.txt?cb=$RANDOM" | grep -E '^(short|dirty)=' | tr '\n' ' ')"
```
Expected: quatro `HTTP 200`, dupla ≥ 1, `dirty=no`.

---

## Self-review (feito ao escrever)

- **Cobertura do spec:** §4.1–4.3 → Task 3; §5.1–5.2 → Task 2; §5.3 → Task 4; §6.1–6.2 → Task 5; §7 → Task 6; D9 → Task 1; pendência 4 (frase da skill) → Task 3 Step 5. D10 (sem notícia de encerramento) respeitado.
- **Placeholders:** nenhum "TBD"; os corpos em prosa têm fichas de fatos fechadas e fontes nomeadas; todo passo de edição tem comando.
- **Consistência de nomes:** ids `slides`, `concept_studio`, `atlas`, `passport`, `learning_analytics`, `project_ecossistema_cedis`, slugs `daniel_rodrigues_da_rocha`, `davi_rodrigues_da_rocha`, `mylena_faria` — idênticos em todas as tasks. Caminhos de assets da Task 1 batem com os `featured_image` das Tasks 2–4 e com os `imgc src` das Tasks 3–4.
