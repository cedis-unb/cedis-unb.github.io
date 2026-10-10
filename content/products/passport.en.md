---
author: CEDIS
title: "CEDIS Learning Passport"
date: 2026-08-09T09:00:00-03:00
language: en
product_language: pt
id: passport
status: active
project: project_ecossistema_cedis
areas:
- digital_transformation
- security
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/passport-logo.png"
summary: The student's pseudonymous identity in the ecosystem. Created from a seed phrase, with no e-mail or personal data, with versioned consent, per-service authorisation and cascading deletion under the LGPD.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_ecossistema_cedis
tags:
- app
- digital_transformation
- security
- project_ecossistema_cedis
---
## Project Description

The **CEDIS Learning Passport** is the student's identity in the ecosystem — a travel passport that records passages through the territory of knowledge without revealing who the traveller is. It is what lets {{< link-interno "/products/slides" "Slides" >}} remember what a student has already answered, the {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} (Knowledge Atlas) draw that student's journey, and {{< link-interno "/products/cedis_learning_analytics" "Learning Analytics" >}} gather signals over time — all without any of those services knowing anyone's name, e-mail or enrolment number.

The reason it exists is concrete: a Brazilian public university must offer personalised pedagogical feedback without breaching the LGPD, and may not even store a student's institutional e-mail in learning-analytics systems. The Passport solves the problem at the root: outside it, no service sees more than a pseudonymous identifier derived by HMAC and scoped per service.

## Project Objectives

- create a learner identity **with no personal data**: no e-mail, no enrolment number, no national ID, no name;
- leave the student in control — they decide whether to use the Passport, what to share with each service, and when to erase everything;
- make consent evidentiary and versioned, equal to the burden of proof the LGPD imposes;
- act as the pseudonymous identity provider for the other products, so none of them reinvents authentication.

## Resources and Features

**Creation by seed phrase.** The student generates their passport from a twelve-word phrase, in the style of digital wallets. The phrase is the key: there is no "forgot my password", only typing the phrase and recovering the passport.

**Student panel.** Shows the student's own journey grouped by deck — readings, answers submitted — and carries the "delete my passport" button, which triggers cascading deletion across Slides, Atlas and Concept Studio.

**Consent as an immutable bundle.** Each version gathers three documents — declaration, privacy notice and terms — with a recorded SHA-256 hash, and the acceptance trail is append-only: it preserves exactly what the student was shown. Authorisation is granular, per service (Slides, Concept Studio, Atlas, Learning Analytics), and revoking Learning Analytics deletes its data at the source. Material changes require fresh acceptance; wording fixes do not. Legal basis: LGPD, art. 7, I, and art. 46, § 2.

**OIDC provider.** The Passport is a lightweight OpenID Connect server: the other CEDIS services use it as their pseudonymous identity, with a different identifier per relationship — rotating any key breaks the link, by design.

## Academic Link and Support

- CEDIS (institutional development and maintenance)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordination)
- {{< link-interno "/projects/ecossistema_cedis" "CEDIS Ecosystem" >}} (origin project)

## Access

Student passport at [passport.cedis.tec.br](https://passport.cedis.tec.br/), triggered by the "Use Passport" widget in any Slides deck. Open source, MIT licence, in the monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
