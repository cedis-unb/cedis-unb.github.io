---
author: CEDIS
title: "Cibersecurity"
date: 2025-09-02T01:37:18-03:00
language: en
weight: 5
featured_image: "../assets/images/featured/area_Cibersecurity.png"
summary: 'Cybersecurity consists of a set of practices, technologies, and methodologies aimed at protecting systems, networks, and data against unauthorized access, cyberattacks, persistent threats, and security failures. Its central goal is to ensure the confidentiality, integrity, and availability of information, especially in increasingly complex and interconnected digital environments.'
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- sergio_freitas
- george_marsicano
tags: 
- security
nav_next: true
---
<div id="top"></div>

Cybersecurity consists of a set of practices, technologies, and methodologies aimed at protecting systems, networks, and data against unauthorized access, cyberattacks, persistent threats, and security failures. Its central goal is to ensure the confidentiality, integrity, and availability of information, especially in increasingly complex and interconnected digital environments.

## {{< i18n "area_coordinator" >}}
**Prof. Sergio Antônio Andrade de Freitas**  
<div style="margin-left: 20px;">  
Full Professor at the University of Brasília (UnB) and researcher in Software Engineering, with extensive experience in cybersecurity and information assurance. His academic trajectory includes supervision of undergraduate and graduate works on intrusion detection, cryptographic protocols, risk analysis, and information security management applied to both public and private organizations. He has coordinated and guided projects involving secure architectures, governance of IT in the public sector, and continuity of critical services. His research integrates cybersecurity with {{< link-interno "/areas/learning_analytics" "Learning Analytics" >}}. His contributions extend to applied research, training of professionals, and innovation in teaching and learning strategies within the domain of Software Engineering and information security. <br>  
{{< link-interno "/people/sergio_freitas" "area_more_about" >}}  
</div>  

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="security" notags="inactive" nocats="sergio_freitas">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="security" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="security" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="security" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="security" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="security" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="security" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="security" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="security" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="security" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="security" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>


## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="security" >}}

## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="security" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="security" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
 Email for information and contact with the team: [sergiofreitas@unb.br](mailto:sergiofreitas@unb.br).

{{< tags >}}