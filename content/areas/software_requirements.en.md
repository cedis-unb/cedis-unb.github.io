---
author: CEDIS
title: "Requirements Engineering"
date: 2024-02-14T00:43:11-03:00
weight: 5
language: en
featured_image: "../assets/images/featured/area_Engenharia de requisitos.png"
summary: Requirements engineering (RE) is an interdisciplinary area of Software Engineering aimed at bridging the gap between the acquirer's and the supplier's or developer's domains.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- george_marsicano
tags: 
- software_requirements
nav_next: true
---
## Introduction
Requirements engineering (RE) is an interdisciplinary area of Software Engineering aimed at bridging the gap between the acquirer's and the supplier's or developer's domains, to establish and maintain the requirements to be met by the system, software product, or service of interest. Its process involves elicitation and discovery, analysis and consensus, statement, representation, verification and validation, and organization and updating of requirements.

At CEDIS, Requirements Engineering is currently a research, development, and application area with a focus on plan-driven, agile, and hybrid software development approaches, in the processes and human relations to be built during the execution of RE, and in the use of artificial intelligence tools.

This research line is coordinated by Prof. George Marsicano and has a team of dedicated researchers. The goal is to develop, identify, and establish processes, methods, and tools that make the RE process more efficient and innovative, both from a technical and human standpoint.

## Publications and Productions
<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< npublications caput="Publications" year="" type="" notypes="" tags="software_requirements" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="software_requirements" notags="" >}} 
    </div>
</div>


{{< tags >}}