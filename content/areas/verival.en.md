---
author: CEDIS
title: "Verification, Validation and Testing"
date: 2024-02-14T00:43:11-03:00
weight: 5
language: en
featured_image: "../assets/images/featured/area_Verificação e Validação.png"
summary: The area of Verification, Validation, and Testing is a critical discipline in software engineering, focused on ensuring that software products meet their specified requirements and function as expected.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- cristiane_ramos
- ricardo_ajax
tags: 
- verification_validation_testing
nav_next: true
---
<div id="top"></div>

The area of Verification, Validation, and Testing is a critical discipline in software engineering, focused on ensuring that software products meet their specified requirements and function as expected. This area covers a broad range of activities, including verifying that the software meets all design and development specifications, validating that the software meets the end-user's needs and expectations, and conducting systematic tests to identify and rectify defects.

## {{< i18n "area_coordinator" >}}
**Prof. Cristiane Ramos**
<div style="margin-left: 20px;">
At CEDIS, Verification, Validation, and Testing are considered fundamental pillars for developing high-quality software. Under the coordination of Prof. Cristiane Ramos, the research line is dedicated to studying and improving methods, tools, and processes that can enhance the effectiveness and efficiency of these activities. The team of specialized researchers works on various topics, such as test automation, regression testing, usability testing, performance and security testing, and integrating verification and validation practices into agile software development methodologies. The goal is to develop innovative approaches that can reduce the time and cost of the testing process while increasing the reliability and security of software products.
<br>
{{< link-interno "/people/cristiane_ramos" "area_more_about_a" >}}
</div>


## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="verification_validation_testing" notags="inactive" nocats="cristiane_ramos">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="verification_validation_testing" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="verification_validation_testing" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="verification_validation_testing" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="verification_validation_testing" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="verification_validation_testing" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="verification_validation_testing" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="verification_validation_testing" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="verification_validation_testing" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="verification_validation_testing" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="verification_validation_testing" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="verification_validation_testing" >}}


## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="verification_validation_testing" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="verification_validation_testing" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
- Email for information and team contact: [cristianesramos@unb.br](cristianesramos@unb.br).

{{< tags >}}