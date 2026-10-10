---
author: CEDIS
title: "CEDIS Learning Analytics"
date: 2026-08-09T09:00:00-03:00
language: en
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
summary: The cross-cutting layer that gathers the signals of the whole ecosystem into a pseudonymised, k-anonymous warehouse to produce pedagogical indicators and insights. Ingest and API in production; teacher dashboards under construction.
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
## Project Description

**CEDIS Learning Analytics** works behind the scenes of the ecosystem. While {{< link-interno "/products/slides" "Slides" >}}, the {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} (Knowledge Atlas) and {{< link-interno "/products/concept_studio" "Concept Studio" >}} record what happens in each class, Learning Analytics gathers those signals into a single analytical store, pseudonymised at the source, so that indicators, correlations and recommendations can come out of them — data that turns into better pedagogical decisions.

It is the family's cross-cutting layer: not the main tool of any teacher or student, but the one that makes the whole visible. It was born on 9 August 2026 out of a 25-chapter discovery audit of everything the ecosystem already recorded, which fixed the architecture and a phased roadmap.

## Project Objectives

- build engagement and progress indicators from evidence rather than intuition;
- detect difficulties and advances early and return personalised recommendations to the student, in the Atlas and along their own paths;
- correlate activities, concepts and performance to support teachers and academic management;
- do all of it with privacy by design: a dedicated analytical identity, specific and revocable consent, k-anonymity in every aggregate.

## Resources and Features

**Ingest.** A dedicated service consumes operational events — readings and answers in Slides, concept touches and progress in the Atlas, questionnaire responses — and materialises them in a separate analytical warehouse, with no impact on the source services.

**Analytical API.** Exposes aggregate views (weekly and monthly summaries, cohorts) always under **K-anonymity of 5 or more**, and individual profiles only to authorised services, through a pre-shared token.

**Analytical identity and consent.** The student accepts a specific consent for analytics in the {{< link-interno "/products/passport" "Learning Passport" >}}; revoking it propagates deletion all the way to the warehouse within one ingest cycle. The analytical identity is derived in layers and never coincides with the identity of any other service.

**Current state, plainly.** Ingest, the API and the deletion cascade are in production at `analytics.cedis.tec.br`. The teacher interface — the dashboards the infographic promises — is under construction. That is why the product appears here as **beta**: the data foundation exists and works; the visualisation layer does not yet.

## Academic Link and Support

- CEDIS (institutional development and maintenance)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordination)
- {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}} (origin project)
- PIBIC undergraduate research 2026–2027 by Daniel Rodrigues da Rocha and Davi Rodrigues da Rocha, advised by Prof. Sergio Freitas

## Access

Service at [analytics.cedis.tec.br](https://analytics.cedis.tec.br/), authenticated access. Open source, MIT licence, in the monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
