---
title: "AgroMart migrates from IaaS to serverless: student duo shows small farmers can stay inside the free tier"
date: 2025-02-25T00:00:00-03:00
draft: false
weight: 500
language: en
featured_image: "../assets/images/featured/area_Arquitetura de Software.png"
summary: 'Kalebe Cunha and Murilo Santana defended in February 2025 at UnB’s Engineering Faculty an undergraduate thesis that migrates AgroMart from IaaS to AWS Lambda and tests the feasibility of running the app within the free tier — dropping cost for farmers.'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- defesa
- software_architecture
- digital_transformation
---
Brasília, February 25, 2025

The core question of this undergraduate thesis is not technical, it’s economic: how much does a small farmer pay today, in dollars, to keep alive the Community-Supported Agriculture (CSA) group through which she sells directly to consumers? **The work defended by Kalebe Lopes da Cunha and Murilo Schiler Lopes Santana in February 2025 at UnB’s Faculty of Sciences and Technologies in Engineering (FCTE) proposes an architectural answer — and tests it** — advised by Prof. {{< link-interno "/people/andre_lanna" "André Luiz Peron Martins Lanna" >}}.

AgroMart, an application that connects producers and consumers under a CSA model, runs on EC2 instances following a traditional Infrastructure-as-a-Service pattern. This is a reasonable and defensible choice — and, for the project’s target users, an unavoidable cost issue: every real charged from the farmer is one less argument to adopt the platform. The authors take this bottleneck as their entry point: if accessibility is the goal, architecture has to follow suit.

The proposal migrates both the dictionary API and the STRAPI backend to a serverless paradigm, specifically Function as a Service (FaaS) running on AWS Lambda. The work is at once about {{< link-interno "/areas/software_architecture/" "software architecture" >}} and about {{< link-interno "/areas/transformation/" "digital transformation" >}}, because the architectural shift is the vehicle for the social outcome — allowing the infrastructure to operate within AWS free-tier limits, eliminating operational cost in typical usage scenarios.

Beyond the migration exercise, the thesis analyzes under which conditions the APIs may exceed the free tier and what the cost implications would be — essential guidance for future maintainers to know how far the model stretches before it demands investment. This is a concrete case study of how platform decisions translate into direct social impact for a user group that rarely fits within the budgets of standard architectures.

The full text — written in Portuguese — is available at the [UnB Undergraduate Theses Digital Library](https://bdm.unb.br/handle/10483/43566).

---

About CEDIS:
The Center for Studies, Development, and Innovation in Software (CEDIS), linked to the University of Brasília, researches and develops innovative software solutions with strong presence in {{< link-interno "/areas/software_architecture/" "software architecture" >}} and {{< link-interno "/areas/transformation/" "digital transformation" >}}.
