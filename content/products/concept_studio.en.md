---
author: CEDIS
title: "CEDIS Concept Studio"
date: 2026-08-09T09:00:00-03:00
language: en
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
summary: The teacher's semantic studio. A concept bank, versioned concept maps, AI-assisted extraction with human confirmation, and the Questionnaires module, which generates formative practice embedded in the decks.
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
## Project Description

**CEDIS Concept Studio** is the studio where a teacher shapes the concepts of a course and connects them into navigable maps. Starting from a deck published in the {{< link-interno "/products/deckmanager" "Deck Manager" >}}, the teacher builds the map of concepts that lecture covers, relates them to one another and, when ready, turns that map into practice questionnaires that reach students inside {{< link-interno "/products/slides" "Slides" >}} itself.

It is a teacher-facing application, behind institutional login, that feeds two other products in the ecosystem: it gives the {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} (Knowledge Atlas) the relations that become the lines in a student's concept constellation, and it publishes to Slides the practice sets a student finds at the end of each deck.

## Project Objectives

- give the teacher a living concept bank — create, edit, merge, deprecate and promote concepts from personal use to the folder and to CEDIS as a whole;
- record relations with meaning, not just links: prerequisite, hierarchy, part-of, contrast, common confusion, related;
- use artificial intelligence as an assistant and never as an authority: the AI proposes concepts and relations from the deck, the teacher confirms or rejects every candidate, and every suggestion keeps its provenance (provider, model, prompt version, input hash);
- bring formative practice into the lesson, with immediate feedback for the student and analytics for the teacher — and, by design, no summative grades, rankings or certification.

## Resources and Features

**Workspace** with three regions — the deck material, the map's concepts and the AI suggestions — with drag-and-drop and keyboard shortcuts. Every map has immutable versions. The AI provider is configurable (OpenAI, Anthropic or a local stub).

**Questionnaires.** The teacher builds a question bank tied to concepts, assembles practice sets and publishes them; the snapshot goes to Slides, which serves it to students. Question types available: single choice, multiple select, true/false, numeric, short answer, 5-point Likert, semantic differential and confidence scale. The analytics page shows the hit rate per question, average time and the most-missed questions — that is how a teacher finds out which concept is confusing the class.

**Gradual activation.** The questionnaire system ships switched off and is enabled by feature flags, environment by environment, separately for authoring and for the dashboard.

## Academic Link and Support

- CEDIS (institutional development and maintenance)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordination)
- {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}} (origin project)

## Access

Teacher application at [concepts.cedis.tec.br](https://concepts.cedis.tec.br/), behind institutional login. Open source, MIT licence, in the monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
