---
author: CEDIS
title: "DevDog"
date: 2026-04-19T12:00:00-03:00
language: en
product_language: pt
id: devdog
status: active
project: project_inovacao_digital_gamificacao
areas:
- gamification
- software_quality
- software_architecture
- active_learning
responsible:
- sergio_freitas
publications: []
weight: 3
featured_home: true
featured_home_order: 2
featured_home_url: "https://devdog.cedis.tec.br/"
featured_image: "../assets/images/featured/devdog-logo.png"
summary: Web application developed as a bachelor's thesis with academic support from CEDIS for gamified learning about code smells, combining conceptual guides, interactive exercises, hints, treats, statistics, and progression.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_inovacao_digital_gamificacao
tags:
- app
- gamification
- software_quality
- software_architecture
- active_learning
- project_inovacao_digital_gamificacao
---
## Project Description

**DevDog** is a web application designed to support learning about **code smells** through a gamified experience. The product was developed by **Luciano Ricardo da Silva Junior** as a bachelor's thesis under the supervision of Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}}, with academic support from the **Center for Studies, Development, and Innovation in Software (CEDIS)**, connecting Software Engineering education, hands-on code inspection, and reward-based progression.

The platform is available at [https://devdog.cedis.tec.br/](https://devdog.cedis.tec.br/) and structures the experience around two complementary modes: **Sniffer Mode**, focused on interactive code analysis exercises, and **Guide Mode**, dedicated to explanatory materials about different software smell categories.

## Project Objectives

The main objectives of the project are:

- to support teaching and learning activities focused on identifying code smells in academic and practical training contexts;
- to combine explanatory content and exercise solving in a single digital experience;
- to encourage engagement and continuity through gamification, progression, and rewards; and
- to provide an experimental basis for teaching, research, and outreach initiatives supported by CEDIS in gamification, software quality, and software architecture.

## Resources and Features

Among the features offered by **DevDog** are anonymous or authenticated access, exercise browsing by difficulty, recommendation of next challenges according to user progression, and attempt submission with suspicious-line marking and smell classification. The application computes performance scores, grants **treats** as rewards, stores attempt history, and presents personal and community statistics, including exercise-level ranking.

The system also provides **hints** that consume treats, such as the number of smelly lines, the number of distinct smell types, and the reveal of one problematic line. In **Guide Mode**, users can browse topic-based content about smells such as long method, large class, duplicated code, comments, feature envy, and other recurring design and maintenance problems. In this way, DevDog combines conceptual study and guided practice in a single environment.

## Academic Link and Support

- Luciano Ricardo da Silva Junior (product development as part of the bachelor's thesis)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (academic supervision)
- Prof. André Luiz Peron Martins Lanna (academic co-supervision)
- CEDIS (institutional and academic support)

## Related Scientific Output

The work behind DevDog had a paper accepted at the **Tools Track of the 40th Brazilian Symposium on Software Engineering (SBES 2026)**, titled _DevDog: A Gamified Web Platform for Teaching Code Smell Identification_, authored by Luciano Ricardo da Silva Junior, Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}}, and Prof. André Luiz Peron Martins Lanna.

## Access

The system is available at [DevDog](https://devdog.cedis.tec.br/). The source code is available on [GitHub](https://github.com/CedisUnB/CodeSmellGamification) under the MIT License, and a demo video can be found on [Zenodo](https://zenodo.org/records/20298757).
