---
title: "How much will that Lambda cost? An undergraduate thesis predicts execution time in serverless"
date: 2023-07-27T00:00:00-03:00
draft: false
weight: 500
language: en
featured_image: "../assets/images/featured/area_HPC.png"
summary: 'Lucas Ganda Carvalho and Wíctor Bastos Girardi defended at UnB Gama an undergraduate thesis investigating execution-time prediction for AWS Lambda functions — a key input for cost estimation in serverless environments.'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- defesa
- hpc
---
Brasília, July 27, 2023

In serverless, cost is a direct function of time. A function that runs in 200ms pays one fare; the same function running in 800ms pays four times that. Yet predicting that time before actually running is an underdeveloped discipline — the market typically decides by isolated benchmarks and optimism. **This vacuum is where the undergraduate thesis defended in July 2023 by Lucas Ganda Carvalho and Wíctor Bastos Girardi steps in**, advised by Prof. {{< link-interno "/people/daniel_lima" "Daniel Sundfeld Lima" >}}.

The work approaches the problem with instrumentation: rather than estimating time by analogy, it proposes a predictive approach for Lambda functions that combines code features with data observed in controlled runs. Predicting accurately matters for two practical reasons: when cost is well estimated, architecture gains the freedom to choose between serverless and traditional options; when it is misestimated, the team learns the price only after the billing cycle closes.

By placing {{< link-interno "/areas/HPC/" "high-performance computing" >}} under the serverless lens, the thesis contributes to a research agenda that remains active at CEDIS — culminating, in 2025, in a master’s dissertation on Nimbus, a serverless environment for automatic code grading.

The full text — written in Portuguese — is available at the [UnB Undergraduate Theses Digital Library](https://www.bdm.unb.br/handle/10483/39151).

---

About CEDIS:
The Center for Studies, Development, and Innovation in Software (CEDIS), linked to the University of Brasília, researches and develops innovative software solutions, with presence in {{< link-interno "/areas/HPC/" "high-performance computing" >}}.
