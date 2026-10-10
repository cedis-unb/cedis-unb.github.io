---
title: "CEDIS Slides: the class happens in the browser, with live answers and a live summary"
date: 2026-08-09T09:00:00-03:00
draft: false
weight: 500
language: en
featured_image: "../assets/images/featured/slides-logo.png"
summary: "The public runtime for CEDIS presentations serves decks on any device, embeds activities and questionnaires, collects answers in real time and gives the teacher a live summary — with no tracking cookies."
description: "CEDIS Slides, the CEDIS Ecosystem product where students attend classes, answer activities and the teacher follows the class live."
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- active_learning
- digital_transformation
- project_ecossistema_cedis
- slides
related_ids:
- slides
- project_ecossistema_cedis
- sergio_freitas
---

Brasilia, August 9, 2026

Anyone who has tried to run a quiz in class knows the dilemma: either pay per seat for a commercial platform that takes students' data outside the university, or improvise with a generic form that neither talks to the slide nor shows anything live. **CEDIS Slides**, presented today as part of the {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}}, is CEDIS's answer to that dilemma.

Slides is where the class happens. Every deck a teacher publishes in the {{< link-interno "/products/deckmanager" "Deck Manager" >}} becomes a single, light, self-contained HTML file that the student opens at `slides.cedis.tec.br` — on a computer, a tablet or a phone, with nothing to install. They navigate with the arrow keys or by swiping; on touch screens, a floating button opens the presenter notes.

The difference lies in the activities. A slide marked as an activity shows the form; the student answers and clicks "Send". If the deck's policy requires it, they type the session code the teacher projects on screen to keep the class in sync. On the other side, the teacher follows the **live summary** — histogram, tag cloud, most frequent answers — and, at the end, downloads everything as CSV. When the teacher publishes questionnaires in {{< link-interno "/products/concept_studio" "Concept Studio" >}}, they appear at the end of the deck under a "Practise" button, with immediate feedback.

Slides is also the student's doorway to the rest of the family. In the corner of the screen, the "Use Passport" widget lets them link readings and answers to their pseudonymous identity in the {{< link-interno "/products/passport" "Learning Passport" >}} — and from there see their own journey in the {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} (Knowledge Atlas). All optional: without the Passport, the deck works anonymously.

There are deliberate engineering choices behind the simplicity. If the Deck Manager panel goes down, reading continues; submitting answers under policies controlled by session or schedule is blocked, to preserve the integrity of what the class answered. There are no tracking cookies, the *Do Not Track* signal is honoured, and aggregate reports apply k-anonymity.

The product is live at [slides.cedis.tec.br](https://slides.cedis.tec.br/), open source under the MIT licence, and coordinated by Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}}. The {{< link-interno "/products/slides" "CEDIS Slides page" >}} details features and access; the big picture is in {{< link-interno "/posts/news-post.035" "the CEDIS Ecosystem presentation" >}}.
