---
title: "CEDIS Concept Studio: concept maps, AI with human review, and questionnaires inside the class"
date: 2026-08-09T09:10:00-03:00
draft: false
weight: 500
language: en
featured_image: "../assets/images/featured/concept_studio-logo.png"
summary: "The teacher's semantic studio organises a course's concepts into versioned maps, accepts AI suggestions only with human confirmation, and turns the map into practice questionnaires that reach students through Slides."
description: "CEDIS Concept Studio, the CEDIS Ecosystem product for creating, connecting and assessing concepts — with integrated formative questionnaires."
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- active_learning
- ai
- learning_analytics
- project_ecossistema_cedis
- concept_studio
related_ids:
- concept_studio
- project_ecossistema_cedis
- sergio_freitas
---

Brasilia, August 9, 2026

Which concept is confusing the class? The question sounds simple, yet almost no teacher has an objective way of answering it before the exam. **CEDIS Concept Studio**, presented today as part of the {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}}, was built to answer exactly that.

Concept Studio is the teacher's semantic studio. Starting from a deck published in the {{< link-interno "/products/deckmanager" "Deck Manager" >}}, the teacher builds the map of concepts the lesson covers and connects them with relations that carry meaning — prerequisite, hierarchy, part-of, contrast, common confusion. The concept bank is alive: concepts are created, edited and merged, and one can be promoted from personal use to the folder and to CEDIS as a whole. Every map has immutable versions.

Artificial intelligence enters as an assistant, never as an authority. The teacher asks the AI to analyse the deck and propose concepts and relations; every candidate is confirmed or rejected by a person, and every suggestion keeps its provenance — which provider, which model, which prompt version, which passage of text. The provider is configurable, including a local stub with no external call.

That is where the **questionnaires** come from. From the concept bank, the teacher writes questions — single or multiple choice, true/false, numeric, short answer, Likert, semantic-differential and confidence scales — and publishes them as practice sets. {{< link-interno "/products/slides" "Slides" >}} serves them to students at the end of the deck, with immediate feedback; the analytics page gives the teacher the hit rate per question, the average time and the most-missed questions. By design there is no summative grade, ranking or certification: it is formative practice.

Concept Studio also feeds the {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} (Knowledge Atlas): the relations between concepts become the lines of the constellation each student sees of their own journey. And everything ships switched off — the questionnaire system is enabled by feature flags, environment by environment.

The application is live at [concepts.cedis.tec.br](https://concepts.cedis.tec.br/), behind institutional login and open source under the MIT licence, coordinated by Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}}. The {{< link-interno "/products/concept_studio" "Concept Studio page" >}} details the features; the big picture is in {{< link-interno "/posts/news-post.035" "the CEDIS Ecosystem presentation" >}}.
