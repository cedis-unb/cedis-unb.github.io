---
title: "Random Forest and Suricata: separating signal from noise in intrusion alerts"
date: 2026-07-04T00:00:00-03:00
draft: false
weight: 500
language: en
featured_image: "../assets/images/featured/area_Cybersecurity.webp"
summary: 'Henrique Azevedo Batalha and Marina Márcia Costa de Souza presented at FCTE/UnB the TCC1 that integrates the Suricata IDS with a Random Forest classifier — trained on the CSE-CIC-IDS2018 dataset — to make intrusion alert analysis more organized and less prone to false positives.'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- tcc1
- security
- machine_learning
- ai
---
Brasília, July 2026

Detecting intrusions in a network is like looking for a needle in a haystack that grows by the second. Traditional Intrusion Detection Systems (IDS) do their job — they emit alerts — but so many that the exhausted analyst starts ignoring signs that might well be legitimate. **It is this analysis bottleneck, not detection itself, that Henrique Azevedo Batalha and Marina Márcia Costa de Souza chose to attack in their TCC1**, presented at the Faculty of Sciences and Technologies in Engineering (FCTE), advised by Prof. {{< link-interno "/people/sergio_freitas" "Sergio Antônio Andrade de Freitas" >}}.

The proposal integrates three pieces: the open source IDS Suricata, in charge of observing network traffic and emitting alerts; a Random Forest classifier, chosen for its robustness, its ability to deal with multiple attributes, and its capacity to explain the relative importance of *features*; and a graphical interface that supports the analyst with history, filters, and a dashboard.

For the initial experiments, the model was trained on a CSV version of the CSE-CIC-IDS2018 dataset — a {{< link-interno "/areas/security/" "cybersecurity" >}} reference of labeled network flows. The pair went through data cleaning, attribute conversion, target variable definition, and the canonical train/test split. TCC1 closes the requirements, logical architecture, initial model training, and Figma prototyping phase; it leaves as the next step, for TCC2, the integration of the components into a functional application evaluated in a controlled environment.

What the work brings into focus is an uncomfortable thesis: in a typical corporate perimeter, the added value of an IDS is no longer in the bit that detects, but in the bit that **prioritizes**. Random Forest enters here as a second-level filter, assigning a verdict and a confidence level to each alert — giving time back to the human analyst and reducing the cognitive cost of the false positive. It is the kind of application in which {{< link-interno "/areas/ai_pln/" "machine learning" >}} couples with {{< link-interno "/areas/security/" "network security" >}} not to replace the specialist, but to make their work sustainable.

---

About CEDIS:
The Center for Studies, Development, and Innovation in Software (CEDIS), linked to the University of Brasília, researches and develops innovative software solutions with strong presence in {{< link-interno "/areas/security/" "cybersecurity" >}} and {{< link-interno "/areas/ai_pln/" "artificial intelligence" >}}.
