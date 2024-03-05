---
author: CEDIS
title: "Green Software Development"
date: 2024-02-14T00:43:11-03:00
weight: 5
language: en
featured_image: "../assets/images/featured/area_Green Software.png"
summary: The area of Green Software Development, or Sustainable Software Development, is an emerging field in software engineering focused on creating software with minimal environmental impact. 
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- fabiana_mendes
tags: 
- green_software
nav_next: true
---
<div id="top"></div>

Green Software Development, or Sustainable Software Development, is an emerging field in software engineering focused on creating software with minimal environmental impact. This discipline involves practices and strategies for developing software in an environmentally responsible manner, reducing energy and resource consumption, and minimizing the carbon footprint associated with the software lifecycle, from design to maintenance and disposal.

## {{< i18n "area_coordinator" >}}
**Prof. Fabiana Mendes**
<div style="margin-left: 20px;">
Coordinated by Prof. Fabiana Mendes, the research line's goal is to promote software development that is both sustainable and environmentally conscious. The team of researchers, composed of experts in sustainability, computer science, and software engineering, works on various aspects such as code optimization for energy efficiency, green IT infrastructures, sustainable design patterns, and the environmental impact assessment of software. The group aims not only to advance theoretical knowledge on sustainable practices in software development but also to apply these concepts in practice, encouraging the software industry to adopt a greener and more responsible approach. Research in Green Software Development aims to contribute to the development of technologies that are not only innovative and effective but also in harmony with the environment.
<br>
{{< link-interno "/people/fabiana_mendes" "area_more_about_a" >}}
</div>

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="green_software" notags="inactive" nocats="fabiana_mendes">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="green_software" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="green_software" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="green_software" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="green_software" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="green_software" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="green_software" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="green_software" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="green_software" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="green_software" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="green_software" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="green_software" >}}


## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="green_software" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="green_software" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
- Email for information and team contact: [fabianamendes@unb.br](mailto:fabianamendes@unb.br).

{{< tags >}}