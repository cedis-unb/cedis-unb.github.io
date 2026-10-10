---
title: "CEDIS Learning Analytics: os dados de todo o ecossistema viram evidência pedagógica — com privacidade por design"
date: 2026-08-09T09:40:00-03:00
draft: false
weight: 500
language: pt
featured_image: "../assets/images/featured/cedis_learning_analytics-logo.png"
summary: "A camada transversal do Ecossistema CEDIS reúne os sinais de Slides, Atlas e Concept Studio em um warehouse pseudonimizado com k-anonimato. Ingestão e API estão em produção; os dashboards docentes, em construção."
description: "CEDIS Learning Analytics, o sexto produto do Ecossistema CEDIS: indicadores, correlações e insights pedagógicos a partir de dados pseudonimizados."
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- learning_analytics
- ai
- machine_learning
- project_ecossistema_cedis
- cedis_learning_analytics
related_ids:
- cedis_learning_analytics
- project_ecossistema_cedis
- sergio_freitas
---

Brasília, 9 de agosto de 2026

Cinco produtos do Ecossistema CEDIS registram o que acontece em cada aula: leituras, respostas, questionários, conceitos tocados, rotas percorridas. O sexto é o que permite enxergar o conjunto. O **CEDIS Learning Analytics**, apresentado hoje como parte do {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}}, trabalha nos bastidores: reúne os sinais de todo o ecossistema em um único repositório analítico, pseudonimizado desde a origem, para que deles saiam indicadores, correlações e recomendações.

É a camada transversal da família — não é a ferramenta principal de nenhum docente nem de nenhum estudante. Nasce de uma auditoria de descoberta de 25 capítulos sobre tudo o que o ecossistema já registrava, concluída hoje, que fixou a arquitetura e um roadmap por fases. O objetivo é o do infográfico: indicadores de engajamento e progresso, detecção de dificuldades e avanços, recomendações personalizadas e correlações entre atividades, conceitos e desempenho — dados que viram decisões melhores.

A privacidade vem antes da análise. O estudante aceita, no {{< link-interno "/products/passport" "Learning Passport" >}}, um consentimento específico para analytics, e uma identidade analítica própria é derivada em camadas — ela nunca coincide com a identidade que o {{< link-interno "/products/slides" "Slides" >}} ou o {{< link-interno "/products/atlas" "Atlas" >}} conhecem. Revogar o consentimento propaga a exclusão até o warehouse em um único ciclo de ingestão. A API só devolve visões agregadas sob **K-anonimato igual ou superior a cinco**; perfis individuais ficam restritos a serviços autorizados.

Em texto claro, para não vender o que não existe: a ingestão, a API e a cascata de exclusão estão em produção em `analytics.cedis.tec.br`. A interface docente — os dashboards que o infográfico promete — está em construção. É por isso que o produto entra no catálogo do CEDIS como **beta**: a fundação de dados existe e funciona; a camada de visualização ainda não.

O Learning Analytics é coordenado pelo Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} e tem código aberto sob licença MIT. A {{< link-interno "/products/cedis_learning_analytics" "página do Learning Analytics" >}} descreve o que está no ar e o que não está; a visão de conjunto está em {{< link-interno "/posts/news-post.035" "a apresentação do Ecossistema CEDIS" >}}.
