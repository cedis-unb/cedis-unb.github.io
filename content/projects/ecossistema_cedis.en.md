---
author: CEDIS
title: "CEDIS Ecosystem"
date: 2026-08-09T09:00:00-03:00
language: en
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
summary: "Six integrated products — Deck Manager, Slides, Concept Studio, Atlas do Conhecimento, Learning Passport and Learning Analytics — that turn content into learning experiences, with data and intelligence at the service of teachers and students, and privacy by design."
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
## Overview

**Ongoing project.** Period: 2026-present.

*Learn. Teach. Connect.* The **CEDIS Ecosystem** is a family of six web applications that work together to turn content into meaningful learning experiences, with data and intelligence at the service of teachers and students. Each product is an independent application with its own subdomain and database; they talk to one another through signed APIs (HMAC, OAuth2/OIDC) with no code coupling — if one service goes down, the others carry on.

The ecosystem began in July 2026 with the {{< link-interno "/products/deckmanager" "CEDIS Deck Manager" >}} and, on 9 August 2026, consolidated into a family of six products with its own visual identity and the infographics reproduced at the end of this page. The code is open, under the MIT licence, in the monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).

## The journey: from content to insight

1. The teacher creates and organises content in the **Deck Manager**.
2. Delivers the class in **Slides**, with embedded interactions.
3. Explores concepts and applies questionnaires in **Concept Studio** — the questionnaires reach students from inside Slides.
4. Students move forward through the **Atlas do Conhecimento** (Knowledge Atlas).
5. Learning is recorded securely in the **Learning Passport**.
6. **Learning Analytics** aggregates signals from the whole ecosystem and produces correlations and insights.
7. The teacher makes better decisions, personalises teaching and supports each student.

The result: more learning, more engagement and pedagogical decisions grounded in data.

## The six products

{{< link-interno "/products/deckmanager" "CEDIS Deck Manager" >}} — `deck.cedis.tec.br`. The teacher's cockpit: browse and manage folders and decks, publish and version, access and engagement statistics, profile and avatar, a panel with views and dashboards, full audit trail.

{{< link-interno "/products/slides" "CEDIS Slides" >}} — `slides.cedis.tec.br`. Where the class happens: decks presented in HTML, embedded activities and questionnaires, real-time answers, a live summary for the teacher, CSV export, and the Passport and touch-screen Notes widgets.

{{< link-interno "/products/concept_studio" "CEDIS Concept Studio" >}} — `concepts.cedis.tec.br`. Create, connect and assess: interactive concept maps, a bank of concepts and relations, questionnaire authoring, analyses and reports, a smart question bank and deck import. Questionnaires are part of Concept Studio.

{{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} — `atlas.cedis.tec.br`. The student's journey: gamified progress along four dimensions, curated learning routes, stamps and expeditions, challenges and concept constellations, visual progress and achievements unlocked by study and practice.

{{< link-interno "/products/passport" "CEDIS Learning Passport" >}} — `passport.cedis.tec.br`. Your identity, your data: pseudonymous login without e-mail, a persistent identity, learning history, data control under the LGPD and integration with every product.

{{< link-interno "/products/cedis_learning_analytics" "CEDIS Learning Analytics" >}} — `analytics.cedis.tec.br`. Data that becomes better decisions: statistics and dashboards, learning indicators, correlations and actionable insights for teachers, with a cross-cutting view of the ecosystem and privacy by design.

## Privacy first

Six golden rules hold across the whole family:

- **End-to-end pseudonymity.** The only identifier that crosses service boundaries is a hash derived in the Passport, different for each service. No system outside the Passport ever sees an e-mail, enrolment number or name.
- **No public ranking.** There is never a named comparison between students; where comparison exists, it is against k-anonymous aggregates — K = 5 in the Atlas, K = 3 in Slides.
- **No manipulation.** The motivational drivers the literature calls "dark" appear only as information for the student to see their own motivation, never as coercion.
- **Native LGPD.** Unlinking the Passport erases the journey in Atlas, Slides and Concept Studio; the student can export all their data as a readable ZIP at any time.
- **Features ship switched off.** Everything new arrives behind a feature flag; the teacher turns it on when ready, and nothing appears to students without deliberation.
- **Silent failure between services.** If Concept Studio is down, the Atlas constellation shows only stars, without lines; if the Atlas is down, the deck keeps working; if the Passport is down, the student uses the deck anonymously.

## Current state

Five products are in production with their full feature sets: Deck Manager, Slides, Concept Studio, Atlas do Conhecimento and Learning Passport. Learning Analytics has ingest, API and deletion cascade live, with the teacher dashboards under construction — which is why it appears in the catalogue as *beta*.

## Team

- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Antônio Andrade de Freitas" >}} — coordination and development.
- Final-year project (2026–2027): **Daniel Rodrigues da Rocha** and **Davi Rodrigues da Rocha** — *Learning Analytics for the CEDIS Ecosystem*, advised by Prof. Sergio.

## Outreach material

{{< imgc src="posts/ecossistema-cedis-infografico-geral.png" alt="Infographic: overview of the CEDIS Ecosystem — six products, the journey from content to insight, and the privacy guarantees" >}}

{{< imgc src="posts/ecossistema-cedis-infografico-docentes.png" alt="Infographic: the CEDIS Ecosystem for teachers — how to plan, publish, follow and improve learning" >}}

{{< imgc src="posts/ecossistema-cedis-infografico-estudantes.png" alt="Infographic: the CEDIS Ecosystem for students — how to learn, practise and follow your journey" >}}
