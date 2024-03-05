---
author: CEDIS
title: "Software Architecture"
date: 2024-02-14T01:37:18-03:00
language: en
weight: 5
featured_image: "../assets/images/featured/area_Arquitetura de Software.png"
summary: Software Architecture is a fundamental field in systems engineering involving the structural organization of software components, their interactions, and the guiding principles that define the design and evolution of systems. This area ensures the efficiency, scalability, and maintainability of software systems, directly impacting the quality and performance of applications.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- andre_lanna
- george_marsicano
tags: 
- software_architecture
nav_next: true
---
<div id="top"></div>

Software Architecture is a key field in systems engineering that encompasses the structural organization of software components, their interactions, and the guiding principles that govern the design and evolution of systems. This area is pivotal in ensuring efficiency, scalability, and maintainability of software systems, directly affecting the quality and performance of applications.

## {{< i18n "area_coordinator" >}}
**Prof. André Lanna**
<div style="margin-left: 20px;">
A professor and researcher in the field of Software Architecture. Currently, he serves as an associate professor at the University of Brasília, significantly contributing to the undergraduate Software Engineering program at the Gama campus and the Graduate Program in Applied Computing. 
<br>
{{< link-interno "/people/andre_lanna" "area_more_about" >}}
</div>

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="software_architecture" notags="inactive" nocats="andre_lanna">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="software_architecture" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="software_architecture" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="software_architecture" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="software_architecture" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="software_architecture" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="software_architecture" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="software_architecture" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="software_architecture" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="software_architecture" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="software_architecture" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="software_architecture" >}}

## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="software_architecture" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="software_architecture" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
- Email for information and team contact: [andrelanna@unb.br](mailto:andrelanna@unb.br).

{{< tags >}}