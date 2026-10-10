---
title: "CEDIS Learning Passport: a learner identity with no e-mail, no national ID, and under the student's control"
date: 2026-08-09T09:30:00-03:00
draft: false
weight: 500
language: en
featured_image: "../assets/images/featured/passport-logo.png"
summary: "Created from a twelve-word phrase, the Passport records a student's journey across the whole CEDIS Ecosystem without storing any personal data — and leaves the decision to share or erase with them."
description: "CEDIS Learning Passport, the pseudonymous identity that makes personalised pedagogical feedback possible in compliance with the LGPD."
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- digital_transformation
- security
- project_ecossistema_cedis
- passport
related_ids:
- passport
- project_ecossistema_cedis
- sergio_freitas
---

Brasilia, August 9, 2026

A public university that wants to give each student personalised pedagogical feedback runs into a concrete limit: under the LGPD, it may not even store a student's institutional e-mail in learning-analytics systems. How do you remember what someone has already answered without knowing who that someone is? The **CEDIS Learning Passport**, presented today as part of the {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}}, solves the problem at the root.

The Passport is the student's identity in the ecosystem — a travel passport that records passages through the territory of knowledge without revealing who the traveller is. It is created from a **twelve-word seed phrase**, in the style of digital wallets. No e-mail, no enrolment number, no national ID, no name. The phrase is the key: there is no "forgot my password", only typing the phrase and recovering the passport.

Outside the Passport, no service sees more than a pseudonymous identifier, derived by HMAC and different for each product. That is how {{< link-interno "/products/slides" "Slides" >}} remembers what a student answered, the {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} (Knowledge Atlas) draws their journey, and {{< link-interno "/products/cedis_learning_analytics" "Learning Analytics" >}} gathers signals over time — without any of them knowing the person behind the hash. The Passport works as a lightweight OpenID Connect provider for the whole family, and rotating any key breaks the link, by design.

Consent is treated as evidence, not as a formality. Each version gathers three documents — declaration, privacy notice and terms — with a recorded hash and an acceptance trail that preserves exactly what was shown. Authorisation is granular, service by service; revoking Learning Analytics deletes its data at the source. Material changes require fresh acceptance; wording fixes do not. In the panel, the student sees their own journey grouped by deck and has the "delete my passport" button at hand, which triggers cascading deletion across Slides, Atlas and Concept Studio.

The Passport is in production at [passport.cedis.tec.br](https://passport.cedis.tec.br/), open source under the MIT licence, coordinated by Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}}. The {{< link-interno "/products/passport" "Learning Passport page" >}} details the features; the big picture is in {{< link-interno "/posts/news-post.035" "the CEDIS Ecosystem presentation" >}}.
