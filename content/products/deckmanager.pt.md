---
author: CEDIS
title: "CEDIS Deck Manager"
date: 2026-07-16T09:00:00-03:00
language: pt
product_language: pt
id: deckmanager
status: active
areas:
- learning_analytics
- active_learning
- digital_transformation
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/deckmanager-logo.png"
summary: Plataforma do CEDIS para publicar apresentações interativas em HTML, controlar quando e para quem elas aceitam respostas e acompanhar o engajamento em tempo real, com anonimização por padrão e conformidade com a LGPD.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
tags:
- app
- learning_analytics
- active_learning
- digital_transformation
---
## Descrição do Projeto

O **CEDIS Deck Manager** é uma plataforma aberta para publicar apresentações interativas em HTML, controlar quando e para quem elas aceitam respostas e acompanhar em tempo real o engajamento da turma — sem cookies de rastreio, com anonimização por design e conformidade com a **LGPD**. Desenvolvido e mantido pelo **CEDIS/UnB**, o sistema é licenciado sob **MIT** e roda em qualquer VPS Linux com Docker.

A plataforma é composta por dois serviços: o **painel administrativo**, onde docentes publicam decks, definem políticas de atividade e acompanham dashboards de analytics, e a **API pública de apresentações**, que serve os formulários de resposta e os resumos ao vivo consultados pelos alunos durante a aula.

## Objetivos do Projeto

O projeto tem como principais objetivos:

- oferecer uma alternativa auditável e self-hostable a plataformas comerciais de apresentação interativa (como Kahoot, Mentimeter, Slido e Poll Everywhere) para uso educacional;
- permitir que instituições de ensino publiquem apresentações e coletem respostas de alunos sob controle próprio dos dados, sem depender de provedores externos;
- oferecer controle flexível sobre quando uma atividade aceita respostas, de "sempre aberta" a programada por semestre, com sessão ao vivo ou código do apresentador; e
- aplicar privacidade por design em analytics educacionais, dispensando cookies de rastreio e banners de consentimento.

## Recursos e Funcionalidades

Entre os recursos do **CEDIS Deck Manager** estão a publicação de apresentações HTML com validação de segurança (proteção contra path traversal, zip bomb e extensões perigosas), quatro políticas de controle de atividade (`always_open`, `class_window`, `presenter_only` e `scheduled`, esta última com programação recorrente semelhante a agendas do tipo Teams ou Google Calendar) e pastas hierárquicas com permissões escalonadas para organizar decks por disciplina ou equipe.

O sistema também oferece **dashboards de learning analytics com privacidade por design**: hash anônimo com rotação diária de salt, truncamento de IP antes de qualquer processamento, classificação de User-Agent sem armazenar a string original, respeito ao Do Not Track (DNT) e supressão por **k-anonimato** nos relatórios agregados. A landing pública organiza decks por popularidade, avaliação e recência, com avaliação anônima por estrelas.

Como diferencial adicional, o Deck Manager conta com uma **skill de geração de apresentações** compatível com assistentes de IA (Claude, ChatGPT/Codex), que permite criar decks HTML com identidade visual do CEDIS, atividades interativas, QR Codes e resumo ao vivo, prontos para publicação direta no painel.

## Vinculação Acadêmica e Apoio

- CEDIS (desenvolvimento e manutenção institucional)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordenação)

## Acesso

A vitrine pública de apresentações está disponível em [slides.cedis.tec.br](https://slides.cedis.tec.br/) e o painel administrativo para docentes em [deck.cedis.tec.br/admin](https://deck.cedis.tec.br/admin/).
