---
author: CEDIS
title: "CEDIS Slides"
date: 2026-08-09T09:00:00-03:00
language: en
product_language: pt
id: slides
status: active
project: project_ecossistema_cedis
areas:
- active_learning
- digital_transformation
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/slides-logo.png"
summary: The public runtime for CEDIS presentations. It serves the HTML decks to students, embeds activities and questionnaires, collects responses in real time, and gives the teacher a live summary and a CSV export.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_ecossistema_cedis
tags:
- app
- active_learning
- digital_transformation
- project_ecossistema_cedis
---
## Project Description

**CEDIS Slides** is where the class happens. While the {{< link-interno "/products/deckmanager" "Deck Manager" >}} is the panel where a teacher catalogues and publishes presentations, Slides is the public runtime that delivers each deck to the student in the browser — on any device, with nothing to install.

Every published deck is a single self-contained HTML file, with CSS and JavaScript embedded. The student opens `slides.cedis.tec.br/<folder>/<deck>`, navigates with the arrow keys or by swiping, and answers the activities the teacher embedded in the slides. The public landing page at `slides.cedis.tec.br` is the student's usual way in: a grid of open decks, organised by popularity, rating and recency.

## Project Objectives

- deliver authored presentations as light, accessible HTML, with no proprietary format and no dependency on an external provider;
- turn the slide into an instrument of participation: the student's answer leaves the deck itself and reaches the teacher within seconds;
- honour the activity policies set in the Deck Manager — the "in-class only" lecture, the recurring semester schedule, the code the presenter projects;
- protect the student's privacy: no tracking cookies, *Do Not Track* honoured, aggregate reports under k-anonymity.

## Resources and Features

**Navigation** by keyboard (arrows, `n` for presenter notes, `f` for full screen), swipe on touch screens, and a floating notes button on iPad and iPhone, where there is no keyboard.

**Embedded activities.** A slide marked as an activity shows the form; the student answers and clicks "Send". When the deck's policy requires it, the student types the **session code** the teacher projects on screen to keep the class in sync. The teacher follows the **live summary** at `/s/<deck>/<activity>` — histogram, tag cloud, most frequent answers — and downloads everything as **CSV**.

**Questionnaires.** At the end of a deck, the "Practise" button opens the practice sets published from {{< link-interno "/products/concept_studio" "Concept Studio" >}}, with immediate feedback on every answer.

**Passport.** In the bottom-right corner, the "Use Passport" widget lets the student, if they wish, link their reading and answers to their pseudonymous identity in the {{< link-interno "/products/passport" "Learning Passport" >}} — and from there see their journey in the {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} (Knowledge Atlas).

**Deliberate failure modes.** If the Deck Manager panel is down, reading the deck still works (*fail-open*); submitting answers under policies controlled by session, code or schedule is blocked (*fail-closed*). A class never stops because a neighbouring service did.

## Academic Link and Support

- CEDIS (institutional development and maintenance)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordination)
- {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}} (origin project)

## Access

Public showcase and deck runtime at [slides.cedis.tec.br](https://slides.cedis.tec.br/). Open source, MIT licence, in the monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
