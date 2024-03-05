---
author: CEDIS
title: "Green Software Development"
date: 2024-02-14T00:43:11-03:00
weight: 5
language: pt
featured_image: "../assets/images/featured/area_Green Software.png"
summary: A área de Green Software Development, ou Desenvolvimento de Software Sustentável, é um campo emergente na engenharia de software que se concentra na criação de software com um impacto ambiental mínimo.  
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- fabiana_mendes
tags: 
- green_software
nav_next: true
---
<div id="top"></div>

A área de Green Software Development, ou Desenvolvimento de Software Sustentável, é um campo emergente na engenharia de software que se concentra na criação de software com um impacto ambiental mínimo. Esta disciplina envolve práticas e estratégias para desenvolver software de maneira ecologicamente responsável, reduzindo o consumo de energia e recursos, e minimizando a pegada de carbono associada ao ciclo de vida do software, desde o design até a manutenção e a disposição.

## {{< i18n "area_coordinator" >}}
**Prof. Fabiana Mendes**
<div style="margin-left: 20px;">
Coordenado pela Profa. Fabiana Mendes, o objetivo da linha de pesquisa é promover o desenvolvimento de software de forma sustentável e consciente ambientalmente. A equipe de pesquisadores, composta por especialistas em sustentabilidade, ciências da computação e engenharia de software, trabalha em diversos aspectos como otimização de código para eficiência energética, infraestruturas de TI verdes, padrões de design sustentáveis e avaliação do impacto ambiental do software. O grupo busca não apenas avançar no conhecimento teórico sobre práticas sustentáveis no desenvolvimento de software, mas também aplicar esses conceitos na prática, incentivando a indústria de software a adotar uma abordagem mais verde e responsável. A pesquisa em Green Software Development visa contribuir para o desenvolvimento de tecnologias que sejam não apenas inovadoras e eficazes, mas também harmoniosas com o meio ambiente.
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
- E-mail para informações e contato com a equipe: [fabianamendes@unb.br](mailto:fabianamendes@unb.br).

{{< tags >}}