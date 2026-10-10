---
title: "CEDIS Learning Analytics: the whole ecosystem's data becomes pedagogical evidence — with privacy by design"
date: 2026-08-09T09:40:00-03:00
draft: false
weight: 500
language: en
featured_image: "../assets/images/featured/cedis_learning_analytics-logo.png"
summary: "The cross-cutting layer of the CEDIS Ecosystem gathers the signals from Slides, Atlas and Concept Studio into a pseudonymised, k-anonymous warehouse. Ingest and API are in production; the teacher dashboards are under construction."
description: "CEDIS Learning Analytics, the sixth product of the CEDIS Ecosystem: indicators, correlations and pedagogical insights from pseudonymised data."
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

Brasilia, August 9, 2026

Five products of the CEDIS Ecosystem record what happens in each class: readings, answers, questionnaires, concepts touched, routes travelled. The sixth is what makes the whole visible. **CEDIS Learning Analytics**, presented today as part of the {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}}, works backstage: it gathers the signals of the whole ecosystem into a single analytical store, pseudonymised at the source, so that indicators, correlations and recommendations can come out of them.

It is the family's cross-cutting layer — not the main tool of any teacher or student. It is born out of a 25-chapter discovery audit of everything the ecosystem already recorded, completed today, which fixed the architecture and a phased roadmap. The goal is the one on the infographic: engagement and progress indicators, detection of difficulties and advances, personalised recommendations and correlations between activities, concepts and performance — data that becomes better decisions.

Privacy comes before analysis. The student accepts, in the {{< link-interno "/products/passport" "Learning Passport" >}}, a specific consent for analytics, and a dedicated analytical identity is derived in layers — it never coincides with the identity that {{< link-interno "/products/slides" "Slides" >}} or the {{< link-interno "/products/atlas" "Atlas" >}} know. Revoking the consent propagates deletion all the way to the warehouse within a single ingest cycle. The API only returns aggregate views under **K-anonymity of five or more**; individual profiles are restricted to authorised services.

Plainly, so as not to sell what does not exist: ingest, the API and the deletion cascade are in production at `analytics.cedis.tec.br`. The teacher interface — the dashboards the infographic promises — is under construction. That is why the product enters the CEDIS catalogue as **beta**: the data foundation exists and works; the visualisation layer does not yet.

Learning Analytics is coordinated by Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} and is open source under the MIT licence. The {{< link-interno "/products/cedis_learning_analytics" "Learning Analytics page" >}} describes what is live and what is not; the big picture is in {{< link-interno "/posts/news-post.035" "the CEDIS Ecosystem presentation" >}}.
