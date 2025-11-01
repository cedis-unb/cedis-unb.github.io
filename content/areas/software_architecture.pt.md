---
author: CEDIS
title: "Arquitetura de Software"
date: 2024-02-14T01:37:18-03:00
language: pt
weight: 5
featured_image: "../assets/images/featured/area_Arquitetura de Software.png"
summary:  Arquitetura de Software é um campo fundamental na engenharia de sistemas que envolve a organização estrutural de componentes de software, suas interações e os princípios orientadores que definem o design e a evolução dos sistemas. Essa área garante a eficiência, a escalabilidade e a manutenção dos sistemas de software, impactando diretamente na qualidade e no desempenho das aplicações.
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

A Arquitetura de Software é um campo fundamental na engenharia de sistemas que envolve a organização estrutural de componentes de software, suas interações e os princípios orientadores que definem o design e a evolução dos sistemas. Essa área é vital para garantir a eficiência, a escalabilidade e a manutenção dos sistemas de software, impactando diretamente na qualidade e no desempenho das aplicações.

## {{< i18n "area_coordinator" >}}
**Prof. André Lanna**
<div style="margin-left: 20px;">
Professor e pesquisador na área de Arquitetura de Software. Atualmente, desempenha o papel de professor adjunto na Universidade de Brasília, contribuindo significativamente para o curso de graduação em Engenharia de Software no campus Gama e para o Programa de Pós-Graduação em Computação Aplicada. 
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
{{< filterPeople caput="#### " caputKey="volunteer" categories="volunteer" advisors="" tags="software_architecture" notags="inactive">}}

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
- E-mail para informações e contato com a equipe: [andrelanna@unb.br](mailto:andrelanna@unb.br).

{{< tags >}}