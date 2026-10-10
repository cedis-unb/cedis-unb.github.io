---
author: CEDIS
title: "CEDIS Learning Analytics"
date: 2026-08-09T09:00:00-03:00
language: pt
product_language: pt
id: cedis_learning_analytics
status: beta
project: project_ecossistema_cedis
areas:
- learning_analytics
- ai
- machine_learning
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/cedis_learning_analytics-logo.png"
summary: Camada transversal que reúne os sinais de todo o ecossistema em um warehouse pseudonimizado com k-anonimato, para gerar indicadores e insights pedagógicos. Ingestão e API em produção; dashboards docentes em construção.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_ecossistema_cedis
tags:
- app
- learning_analytics
- ai
- machine_learning
- project_ecossistema_cedis
---
## Descrição do Projeto

O **CEDIS Learning Analytics** trabalha nos bastidores do ecossistema. Enquanto o {{< link-interno "/products/slides" "Slides" >}}, o {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} e o {{< link-interno "/products/concept_studio" "Concept Studio" >}} registram o que acontece em cada aula, o Learning Analytics reúne esses sinais em um único repositório analítico, pseudonimizado desde a origem, para que deles saiam indicadores, correlações e recomendações — dados que viram decisões pedagógicas melhores.

É a camada transversal da família: não é a ferramenta principal de nenhum docente nem de nenhum estudante, mas é a que permite enxergar o conjunto. Nasceu em 9 de agosto de 2026 a partir de uma auditoria de descoberta de 25 capítulos sobre tudo o que o ecossistema já registrava, que fixou a arquitetura e o roadmap por fases.

## Objetivos do Projeto

- construir indicadores de engajamento e de progresso a partir de evidência, não de intuição;
- detectar cedo dificuldades e avanços e devolver recomendações personalizadas ao estudante, no Atlas e nos próprios percursos;
- correlacionar atividades, conceitos e desempenho para apoiar o docente e a gestão acadêmica;
- fazer tudo isso com privacidade por design: identidade analítica própria, consentimento específico e revogável, k-anonimato em toda agregação.

## Recursos e Funcionalidades

**Ingestão.** Um serviço dedicado consome os eventos operacionais — leituras e respostas no Slides, toques em conceitos e progresso no Atlas, respostas de questionários — e os materializa em um *warehouse* analítico separado, sem impacto nos serviços de origem.

**API analítica.** Expõe visões agregadas (resumos semanais e mensais, coortes) sempre sob **K-anonimato igual ou superior a 5**, e perfis individuais apenas a serviços autorizados, por token pré-compartilhado.

**Identidade analítica e consentimento.** O estudante aceita um consentimento específico para analytics no {{< link-interno "/products/passport" "Learning Passport" >}}; revogá-lo propaga a exclusão até o warehouse em um ciclo de ingestão. A identidade analítica é derivada por camadas e nunca coincide com a identidade de nenhum outro serviço.

**Estado atual, em texto claro.** Ingestão, API e a cascata de exclusão estão em produção em `analytics.cedis.tec.br`. A interface docente — os dashboards que o infográfico promete — está em construção. Por isso o produto aparece aqui como **beta**: a fundação de dados existe e funciona; a camada de visualização ainda não.

## Vinculação Acadêmica e Apoio

- CEDIS (desenvolvimento e manutenção institucional)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordenação)
- {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}} (projeto de origem)
- Iniciação científica PIBIC 2026–2027 de Daniel Rodrigues da Rocha e Davi Rodrigues da Rocha, orientados pelo Prof. Sergio Freitas

## Acesso

Serviço em [analytics.cedis.tec.br](https://analytics.cedis.tec.br/), com acesso autenticado. Código aberto, licença MIT, no monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
