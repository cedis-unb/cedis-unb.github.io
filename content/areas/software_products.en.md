---
author: CEDIS
title: "Software Product Line Engineering"
date: 2024-02-14T00:43:11-03:00
weight: 5
language: en
featured_image: "../assets/images/featured/area_Linha de produtos.png"
summary: Software Product Line Engineering is a specialized area in software engineering focusing on the efficient development of a family of related software products. 
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- andre_lanna
tags: 
- software_product_line
nav_next: true
---
<div id="top"></div>

Software Product Line Engineering is a specialized area within software engineering, focusing on the efficient development of a family of related software products. This discipline involves creating a common architecture and a set of shared components, allowing for customization and the generation of multiple software product variants from a common base. This field is essential for enhancing software reuse, reducing development costs and time, and increasing the quality and consistency across software products.

## {{< i18n "area_coordinator" >}}
**Prof. André Lanna**
<div style="margin-left: 20px;">
At CEDIS, Software Product Line Engineering is a key area of research, development, and innovation. Coordinated by Prof. André Lanna, the research line focuses on advancing practices, techniques, and tools related to this area. The team of researchers is dedicated to studying and improving methods for modeling common and variable features, customization strategies, dependency management, and integrating new technologies. The goal is to explore how software product lines can be efficiently designed, implemented, and maintained, contributing to the efficiency and competitiveness of companies in the software market. The research in this area aims not only to enhance theoretical understanding but also to apply this knowledge in practice, assisting organizations in optimizing their large-scale software development.
<br>
{{< link-interno "/people/andre_lanna" "area_more_about" >}}
</div>

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="software_product_line" notags="inactive" nocats="andre_lanna">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="software_product_line" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="software_product_line" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="software_product_line" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="software_product_line" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="software_product_line" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="software_product_line" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="software_product_line" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="software_product_line" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="software_product_line" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="software_product_line" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="software_product_line" >}}


## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="software_product_line" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="software_product_line" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
- Email for information and team contact: [andrelanna@unb.br](mailto:andrelanna@unb.br).

{{< tags >}}