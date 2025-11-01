---
author: CEDIS
title: "Trabalho em equipe e Soft Skills"
date: 2024-02-14T01:37:18-03:00
language: pt
weight: 5
featured_image: "../assets/images/featured/area_Team work and soft skills.png"
summary: A área de Trabalho em Equipe e Soft Skills é um campo interdisciplinar na gestão de projetos e desenvolvimento de software, enfatizando a importância das habilidades interpessoais e comportamentais para o sucesso de equipes de TI.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- george_marsicano
tags: 
- teamwork
- soft_skills
nav_next: true
---
<div id="top"></div>

A área de Trabalho em Equipe e Soft Skills é um campo interdisciplinar na gestão de projetos e desenvolvimento de software, enfatizando a importância das habilidades interpessoais e comportamentais para o sucesso de equipes de TI. Esta disciplina reconhece que, além das competências técnicas, habilidades como comunicação eficaz, colaboração, resolução de conflitos, liderança e empatia são cruciais para o funcionamento eficiente de equipes de software. O foco em soft skills é essencial para melhorar a dinâmica de equipe, a satisfação no trabalho e, consequentemente, a produtividade e a qualidade do software desenvolvido.

## {{< i18n "area_coordinator" >}}
**Prof. George Marsicano**
<div style="margin-left: 20px;">
Sob a coordenação do Prof. George Marsicano, a linha de pesquisa e desenvolvimento se dedica a explorar as melhores práticas, metodologias e ferramentas para fortalecer a colaboração e as habilidades interpessoais em ambientes de desenvolvimento de software. A equipe de pesquisa, composta por especialistas em psicologia organizacional, gestão de recursos humanos e engenharia de software, trabalha em temas como desenvolvimento de liderança, comunicação eficiente, gestão de conflitos e técnicas de trabalho em equipe. O objetivo é criar abordagens inovadoras e práticas para capacitar equipes de software a alcançar níveis mais altos de desempenho e satisfação, enfatizando a importância do desenvolvimento humano no contexto da tecnologia da informação.
<br>
{{< link-interno "/people/george_marsicano" "area_more_about" >}}
</div>

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="soft_skills" notags="inactive" nocats="george_marsicano">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="soft_skills" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="soft_skills" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="soft_skills" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="soft_skills" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="soft_skills" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="volunteer" categories="volunteer" advisors="" tags="soft_skills" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="soft_skills" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="soft_skills" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="soft_skills" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="soft_skills" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="soft_skills" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="soft_skills" >}}


## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="soft_skills" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="soft_skills" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
- E-mail para informações e contato com a equipe: [georgemarsicano@unb.br](mailto:georgemarsicano@unb.br).

{{< tags >}}