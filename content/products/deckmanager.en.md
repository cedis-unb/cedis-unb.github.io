---
author: CEDIS
title: "CEDIS Deck Manager"
date: 2026-07-16T09:00:00-03:00
language: en
product_language: pt
id: deckmanager
status: active
areas:
- learning_analytics
- active_learning
- digital_transformation
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/deckmanager-logo.png"
summary: A CEDIS platform for publishing interactive HTML presentations, controlling when and for whom they accept responses, and tracking engagement in real time, with privacy-by-design anonymization and LGPD compliance.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
tags:
- app
- learning_analytics
- active_learning
- digital_transformation
---
## Project Description

**CEDIS Deck Manager** is an open platform for publishing interactive HTML presentations, controlling when and for whom they accept responses, and tracking classroom engagement in real time — with no tracking cookies, privacy-by-design anonymization, and compliance with Brazil's **LGPD** (General Data Protection Law). Developed and maintained by **CEDIS/UnB**, the system is **MIT**-licensed and runs on any Linux VPS with Docker.

The platform is made up of two services: the **admin panel**, where instructors publish decks, define activity policies, and monitor analytics dashboards, and the **public presentation API**, which serves the response forms and live summaries students consult during class.

## Project Objectives

The main objectives of the project are:

- to offer an auditable, self-hostable alternative to commercial interactive presentation platforms (such as Kahoot, Mentimeter, Slido, and Poll Everywhere) for educational use;
- to allow educational institutions to publish presentations and collect student responses under their own control of the data, without relying on external providers;
- to provide flexible control over when an activity accepts responses, from "always open" to scheduled per semester, live sessions, or presenter codes; and
- to apply privacy-by-design to educational analytics, dispensing with tracking cookies and consent banners.

## Resources and Features

Among the features offered by **CEDIS Deck Manager** are HTML presentation publishing with security validation (protection against path traversal, zip bombs, and dangerous file extensions), four activity control policies (`always_open`, `class_window`, `presenter_only`, and `scheduled`, the latter with recurring scheduling similar to Teams or Google Calendar), and hierarchical folders with tiered permissions to organize decks by course or team.

The system also provides **privacy-by-design learning analytics dashboards**: anonymous hashing with daily salt rotation, IP truncation before any processing, User-Agent classification without storing the original string, respect for Do Not Track (DNT), and **k-anonymity** suppression in aggregated reports. The public landing page organizes decks by popularity, rating, and recency, with anonymous star ratings.

As an additional distinguishing feature, Deck Manager ships with a **presentation-generation skill** compatible with AI assistants (Claude, ChatGPT/Codex), enabling the creation of HTML decks with CEDIS visual identity, interactive activities, QR codes, and live summaries, ready for direct publication on the panel.

## Academic Link and Support

- CEDIS (institutional development and maintenance)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordination)

## Access

The public presentation showcase is available at [slides.cedis.tec.br](https://slides.cedis.tec.br/) and the admin panel for instructors at [deck.cedis.tec.br/admin](https://deck.cedis.tec.br/admin/).
