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
- cedis_learning_analytics
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
## Visão geral

**Projeto em andamento.** Período: 2026-Atual.

*Aprender. Ensinar. Conectar.* O **Ecossistema CEDIS** é uma família de seis aplicações web que trabalham juntas para transformar conteúdo em experiências de aprendizagem significativas, com dados e inteligência a serviço de docentes e estudantes. Cada produto é uma aplicação independente, com subdomínio e banco de dados próprios; elas conversam por APIs assinadas (HMAC, OAuth2/OIDC), sem acoplamento de código — se um serviço sai do ar, os outros continuam.

O ecossistema começou em julho de 2026 com o {{< link-interno "/products/deckmanager" "CEDIS Deck Manager" >}} e, em 9 de agosto de 2026, consolidou-se como família de seis produtos, com identidade visual própria e os infográficos reproduzidos ao fim desta página. O código é aberto, sob licença MIT, no monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).

## A jornada: do conteúdo ao insight

1. O docente cria e organiza seus conteúdos no **Deck Manager**.
2. Apresenta as aulas no **Slides**, com interações embutidas.
3. Explora conceitos e aplica questionários no **Concept Studio** — os questionários chegam aos estudantes por dentro do Slides.
4. Os estudantes avançam pelo **Atlas do Conhecimento**.
5. A aprendizagem fica registrada com segurança no **Learning Passport**.
6. O **Learning Analytics** agrega sinais de todo o ecossistema e gera correlações e insights.
7. O docente toma decisões melhores, personaliza o ensino e apoia cada estudante.

Resultado: mais aprendizado, mais engajamento e decisões pedagógicas baseadas em dados.

## Os seis produtos

{{< link-interno "/products/deckmanager" "CEDIS Deck Manager" >}} — `deck.cedis.tec.br`. O cockpit do docente: explorar e gerenciar pastas e decks, publicar e versionar, estatísticas de acesso e engajamento, perfil e avatar, painel com vistas e dashboards, auditoria completa.

{{< link-interno "/products/slides" "CEDIS Slides" >}} — `slides.cedis.tec.br`. Onde a aula acontece: apresentação dos decks em HTML, atividades e questionários embutidos, respostas em tempo real, resumo ao vivo para o docente, exportação em CSV e os widgets de Passaporte e de Notas em telas de toque.

{{< link-interno "/products/concept_studio" "CEDIS Concept Studio" >}} — `concepts.cedis.tec.br`. Crie, conecte e avalie: mapas conceituais interativos, banco de conceitos e relações, criação de questionários, análises e relatórios, banco de questões inteligente e importação de decks. Os questionários são parte do Concept Studio.

{{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} — `atlas.cedis.tec.br`. A jornada do estudante: progresso gamificado em quatro dimensões, rotas de aprendizado curadas, carimbos e expedições, desafios e constelações de conceitos, progresso visual e conquistas desbloqueadas por estudo e prática.

{{< link-interno "/products/passport" "CEDIS Learning Passport" >}} — `passport.cedis.tec.br`. Sua identidade, seus dados: login pseudônimo sem e-mail, identidade persistente, histórico de aprendizagem, controle de dados conforme a LGPD e integração com todos os produtos.

{{< link-interno "/products/cedis_learning_analytics" "CEDIS Learning Analytics" >}} — `analytics.cedis.tec.br`. Dados que viram decisões melhores: estatísticas e dashboards, indicadores de aprendizagem, correlações e insights acionáveis para docentes, com visão transversal do ecossistema e privacidade por design.

## Privacidade em primeiro lugar

Seis regras de ouro valem para toda a família:

- **Pseudonímia de ponta a ponta.** O único identificador que cruza fronteiras entre serviços é um hash derivado no Passaporte, diferente para cada serviço. Nenhum sistema fora do Passaporte vê e-mail, matrícula ou nome.
- **Sem ranking público.** Nunca há comparação nominal entre estudantes; quando existe comparação, é contra agregados k-anônimos — K = 5 no Atlas, K = 3 no Slides.
- **Sem manipulação.** Os impulsos motivacionais que a literatura chama de "escuros" só aparecem como informação para o próprio estudante enxergar sua motivação, nunca como coerção.
- **LGPD nativa.** Desvincular o Passaporte apaga o percurso em Atlas, Slides e Concept Studio; o estudante pode exportar todos os seus dados em ZIP legível a qualquer momento.
- **Funcionalidades nascem desligadas.** Toda novidade chega por feature flag; o docente ativa quando quiser e nada aparece para o estudante sem deliberação.
- **Falha silenciosa entre serviços.** Se o Concept Studio está fora do ar, a constelação do Atlas mostra só as estrelas, sem as linhas; se o Atlas está fora, o deck continua funcionando; se o Passaporte está fora, o estudante usa o deck anonimamente.

## Estado atual

Cinco produtos estão em produção com seus conjuntos de funcionalidades completos: Deck Manager, Slides, Concept Studio, Atlas do Conhecimento e Learning Passport. O Learning Analytics tem ingestão, API e cascata de exclusão no ar, e os dashboards docentes em construção — por isso aparece no catálogo como *beta*.

## Equipe

- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Antônio Andrade de Freitas" >}} — coordenação e desenvolvimento.
- Iniciação científica PIBIC 2026–2027: **Daniel Rodrigues da Rocha** e **Davi Rodrigues da Rocha** — *Learning Analytics do Ecossistema CEDIS*, sob orientação do Prof. Sergio.

## Material de divulgação

{{< imgc src="posts/ecossistema-cedis-infografico-geral.png" alt="Infográfico: panorama do Ecossistema CEDIS — seis produtos, a jornada do conteúdo ao insight e as garantias de privacidade" >}}

{{< imgc src="posts/ecossistema-cedis-infografico-docentes.png" alt="Infográfico: o Ecossistema CEDIS para professores — como planejar, publicar, acompanhar e aprimorar a aprendizagem" >}}

{{< imgc src="posts/ecossistema-cedis-infografico-estudantes.png" alt="Infográfico: o Ecossistema CEDIS para estudantes — como aprender, praticar e acompanhar sua jornada" >}}
