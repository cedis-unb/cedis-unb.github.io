---
author: CEDIS
title: "Atlas do Conhecimento"
date: 2026-08-09T09:00:00-03:00
language: en
product_language: pt
id: atlas
status: active
project: project_ecossistema_cedis
areas:
- gamification
- learning_analytics
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/atlas-logo.png"
summary: The student's personal, pseudonymous space to see their own journey. Progress along four dimensions, curated routes, stamps, a diary, a concept constellation and a motivational compass — no rankings, and k-anonymity throughout.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_ecossistema_cedis
tags:
- app
- gamification
- learning_analytics
- project_ecossistema_cedis
---
## Project Description

The **Atlas do Conhecimento** (Knowledge Atlas) is the student's personal space to see, revisit and celebrate their own learning journey across the CEDIS ecosystem. The metaphor is cartographic: the student is an explorer, knowledge is a continent with thematic regions, every deck read is a destination and every concept a star. The passport holds stamps, the diary holds memories, the compass suggests paths — but never dictates.

The Atlas is not a learning management system: it hosts no content, grades nothing, issues no certificates. It also has no ranking, no leaderboard, no public comparison between students. A student arrives from the {{< link-interno "/products/passport" "Learning Passport" >}} through a secure handoff with a one-time code, and what they see there is theirs alone.

## Project Objectives

- show pedagogical progress along **four dimensions** — exploration, practice, consolidation and reflection — without collapsing everything into a single score;
- reward milestones with stamps that never reset or expire, and offer optional expeditions with no penalty for giving up;
- give the student a transparent reading of their own motivation, with full control over collection;
- comply with the LGPD natively: unlinking erases the journey, and export is always available.

## Resources and Features

**Map** (`/mapa`): routes become territories, decks become destinations, and rings around each destination show the 4D progress in that deck. **Routes** (`/rotas`): thematic paths curated by the teacher, with completion requirements. **Stamps** (`/carimbos`): twelve by default, with monotonic progress. **Diary** (`/diario`): a timeline of automatic entries and reflections the student writes. **Constellation** (`/constelacao`): an interactive graph of the concepts already touched, with relations coming from {{< link-interno "/products/concept_studio" "Concept Studio" >}}; each star's colour tells whether the concept was mentioned, practised or consolidated. **Compass** (`/bussola`): an Octalysis motivational profile, explicit opt-in, switchable off at any time. **Next steps** (`/proximos-passos`): plain-language recommendations from five transparent heuristics — no machine learning, no black box. **Settings**: export all data as a readable ZIP and unlink from the Passport, with cascading deletion.

**Teacher admin.** Inside the {{< link-interno "/products/deckmanager" "Deck Manager" >}}, under `/admin/atlas/*`, the teacher edits routes, stamps and expeditions and consults the class dashboard. Every aggregate is **k-anonymous** (K = 5): no bucket with fewer than five students is ever shown as an absolute number.

**How events arrive.** Reading a slide, answering an activity or writing a reflection produces an event in Slides; an ingest service consumes it and the Atlas updates counters, stamps and signals. Typical latency: about thirty seconds.

## Academic Link and Support

- CEDIS (institutional development and maintenance)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordination)
- {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}} (origin project)

## Access

Student space at [atlas.cedis.tec.br](https://atlas.cedis.tec.br/), reached from the Passport widget in any deck. Open source, MIT licence, in the monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
