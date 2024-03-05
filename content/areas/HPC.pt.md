---
author: CEDIS
title: "Computação de alto desempenho e computação em nuvem"
date: 2024-02-14T01:37:18-03:00
language: pt
weight: 5
featured_image: "../assets/images/featured/area_HPC.png"
summary: Computação de Alto Desempenho e Computação em Nuvem é um campo dinâmico e essencial na ciência da computação, focado no desenvolvimento e na aplicação de sistemas computacionais avançados capazes de processar grandes quantidades de dados a velocidades extremamente altas.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- daniel_sundfeld
tags: 
- hpc
nav_next: true
---
<div id="top"></div>

A área de Computação de Alto Desempenho e Computação em Nuvem é um campo dinâmico e essencial na ciência da computação, focado no desenvolvimento e na aplicação de sistemas computacionais avançados capazes de processar grandes quantidades de dados a velocidades extremamente altas. A Computação de Alto Desempenho (High-Performance Computing, HPC) envolve o uso de supercomputadores e sistemas de processamento paralelo para resolver problemas complexos e intensivos em termos de processamento. Já a Computação em Nuvem refere-se ao uso de recursos de computação (como servidores, armazenamento, bancos de dados, redes, software) sobre a internet, oferecendo escalabilidade, flexibilidade e eficiência de custos.

## {{< i18n "area_coordinator" >}}
**Prof. Daniel Sundfeld Lima**
<div style="margin-left: 20px;">
No CEDIS, a integração de Computação de Alto Desempenho e Computação em Nuvem é uma área de pesquisa e desenvolvimento de grande interesse. Coordenada pelo Prof. Daniel Sundfeld, a linha de pesquisa explora como essas duas tecnologias podem ser combinadas para oferecer soluções mais potentes e eficientes. A equipe de pesquisa, formada por especialistas em arquitetura de sistemas, redes de computadores e engenharia de software, investiga temas como a otimização de algoritmos para HPC, o desenvolvimento de infraestruturas de nuvem escaláveis, a segurança em ambientes de computação em nuvem e a integração de serviços de nuvem com capacidades de alto desempenho. O objetivo é desenvolver novas abordagens e tecnologias que permitam aproveitar ao máximo as capacidades de processamento em larga escala da computação de alto desempenho, juntamente com a flexibilidade e a acessibilidade da computação em nuvem, abrindo caminho para inovações em diversos campos, desde a análise de big data até a modelagem de sistemas complexos.
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
- E-mail para informações e contato com a equipe: [daniel.sundfeld@unb.br](mailto:daniel.sundfeld@unb.br)

{{< tags >}}