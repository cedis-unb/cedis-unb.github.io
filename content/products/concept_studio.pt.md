---
author: CEDIS
title: "CEDIS Concept Studio"
date: 2026-08-09T09:00:00-03:00
language: pt
product_language: pt
id: concept_studio
status: active
project: project_ecossistema_cedis
areas:
- active_learning
- ai
- learning_analytics
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/concept_studio-logo.png"
summary: Ateliê semântico do docente. Banco de conceitos, mapas conceituais versionados, extração assistida por IA com confirmação humana e o módulo de Questionários, que gera prática formativa embutida nos decks.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_ecossistema_cedis
tags:
- app
- active_learning
- ai
- learning_analytics
- project_ecossistema_cedis
---
## Descrição do Projeto

O **CEDIS Concept Studio** é o ateliê onde o docente esculpe os conceitos de uma disciplina e os conecta em mapas navegáveis. A partir de um deck publicado no {{< link-interno "/products/deckmanager" "Deck Manager" >}}, o docente monta o mapa dos conceitos que aquela aula aborda, relaciona uns aos outros e, quando quiser, transforma esse mapa em questionários de prática que chegam aos estudantes dentro do próprio {{< link-interno "/products/slides" "Slides" >}}.

É uma aplicação de uso docente, com login institucional, que alimenta dois outros produtos do ecossistema: fornece ao {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} as relações que viram linhas na constelação de conceitos do estudante, e publica no Slides os conjuntos de prática que o aluno encontra ao fim de cada deck.

## Objetivos do Projeto

- dar ao docente um banco de conceitos vivo — criar, editar, mesclar, depreciar e promover conceitos do uso pessoal para a pasta e para o CEDIS inteiro;
- registrar relações com significado, não apenas links: pré-requisito, hierarquia, parte-de, contraste, confusão comum, relacionado;
- usar inteligência artificial como assistente e nunca como autoridade: a IA propõe conceitos e relações a partir do deck, o docente confirma ou rejeita cada candidato, e toda sugestão guarda sua proveniência (provedor, modelo, versão do prompt, hash da entrada);
- levar a prática formativa para dentro da aula, com feedback imediato ao aluno e analytics para o docente — e, por desenho, sem nota somativa, ranking ou certificação.

## Recursos e Funcionalidades

**Workspace** com três regiões — o material do deck, os conceitos do mapa e as sugestões da IA — com arrastar-e-soltar e atalhos de teclado. Cada mapa tem versões imutáveis. O provedor de IA é configurável (OpenAI, Anthropic ou um *stub* local).

**Questionários.** O docente cria um banco de questões ligadas a conceitos, monta *practice sets* e os publica; o snapshot vai para o Slides, que o serve aos estudantes. Tipos de questão disponíveis: escolha única, múltipla seleção, verdadeiro ou falso, numérica, resposta curta, Likert de 5 pontos, diferencial semântico e escala de confiança. A página de analytics mostra taxa de acerto por questão, tempo médio e as questões mais erradas — é assim que o docente descobre qual conceito está gerando confusão na turma.

**Ativação gradual.** O sistema de questionários nasce desligado e é ativado por feature flags, ambiente a ambiente, para autoria e para o dashboard separadamente.

## Vinculação Acadêmica e Apoio

- CEDIS (desenvolvimento e manutenção institucional)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordenação)
- {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}} (projeto de origem)

## Acesso

Aplicação do docente em [concepts.cedis.tec.br](https://concepts.cedis.tec.br/), com login institucional. Código aberto, licença MIT, no monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
