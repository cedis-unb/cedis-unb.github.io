---
author: CEDIS
title: "High-Performance Computing and Cloud Computing"
date: 2025-04-01T01:37:18-03:00
language: en
weight: 5
featured_image: "../assets/images/featured/area_HPC.png"
summary: High-Performance Computing and Cloud Computing is a dynamic and essential field in computer science, focused on the development and application of advanced computing systems capable of processing large amounts of data at extremely high speeds.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- daniel_sundfeld
tags: 
- hpc
nav_next: true
---
<div id="top"></div>

The area of High-Performance Computing (HPC) and Cloud Computing is a dynamic and essential field in computer science, focused on the development and application of advanced computing systems capable of processing large amounts of data at extremely high speeds. High-Performance Computing involves the use of supercomputers and parallel processing systems to solve complex and processing-intensive problems. Meanwhile, Cloud Computing refers to the use of computing resources (such as servers, storage, databases, networks, software) over the internet, offering scalability, flexibility, and cost efficiency.

## {{< i18n "area_coordinator" >}}
**Prof. Daniel Sundfeld Lima**
<div style="margin-left: 20px;">
At CEDIS, the integration of High-Performance Computing and Cloud Computing is a research and development area of great interest. Coordinated by Prof. Daniel Sundfeld, this research line explores how these two technologies can be combined to offer more powerful and efficient solutions. The research team, comprised of experts in system architecture, computer networks, and software engineering, investigates topics such as algorithm optimization for HPC, the development of scalable cloud infrastructures, security in cloud computing environments, and the integration of cloud services with high-performance capabilities. The goal is to develop new approaches and technologies that fully leverage the large-scale processing capabilities of high-performance computing, along with the flexibility and accessibility of cloud computing, paving the way for innovations across various fields, from big data analysis to the modeling of complex systems.
<br>
{{< link-interno "/people/daniel_sundfeld" "area_more_about" >}}
</div>

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="hpc" notags="inactive" nocats="daniel_sundfeld">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="hpc" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="hpc" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="hpc" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="hpc" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="hpc" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="hpc" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="hpc" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="hpc" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="hpc" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="hpc" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="hpc" >}}

## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="hpc" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="hpc" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
- Email for information and contact with the team: [daniel.sundfeld@unb.br](mailto:daniel.sundfeld@unb.br)

{{< tags >}}