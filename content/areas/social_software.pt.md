---
author: CEDIS
title: "Software social"
date: 2025-05-01T01:37:18-03:00
language: pt
weight: 5
featured_image: "../assets/images/featured/area_Social_Software.png"
summary: Área de pesquisa que envolve o desenvolvimento e a análise de tecnologias digitais (especialmente software) com o objetivo explícito de gerar impacto social positivo, sem fins lucrativos ou de exploração comercial direta. Essa abordagem é colaborativa, interdisciplinar e centrada nas pessoas.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- george_marsicano
- ricardo_ajax
tags: 
- social_software
nav_next: true
---
<div id="top"></div>

Software social é uma área emergente da computação que se concentra no design, desenvolvimento e avaliação de tecnologias digitais — especialmente sistemas de software — destinadas a atender demandas sociais e promover transformações sociais positivas. Essa área enfatiza abordagens centradas nas pessoas, interdisciplinares e participativas, priorizando a responsabilidade ética, a inclusão e o engajamento comunitário em detrimento do lucro comercial. O software social contribui para a criação de soluções digitais equitativas, promovendo acessibilidade, empoderamento e inovação social em contextos diversos.

## {{< i18n "area_coordinator" >}}
**Prof. George Marcicano**
<div style="margin-left: 20px;">
Professor e pesquisador na área de Software Social. Atualmente, é professor associado na Universidade de Brasília, com contribuições significativas para o curso de Engenharia de Software do campus Gama e para o Programa de Pós-Graduação em Computação Aplicada.
<br>
{{< link-interno "/people/george_marsicano" "area_more_about" >}}
</div>

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="social_software" notags="inactive" nocats="george_marsicano">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="social_software" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="social_software" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="social_software" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="social_software" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="social_software" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="social_software" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="social_software" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="social_software" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="social_software" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="social_software" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="social_software" >}}

## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="social_software" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="social_software" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
- E-mail para informações e contato com a equipe: [georgemasicano@unb.br](mailto:georgemasicano@unb.br).

{{< tags >}}
