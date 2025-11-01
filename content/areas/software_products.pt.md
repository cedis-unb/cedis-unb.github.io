---
author: CEDIS
title: "Engenharia de Linhas de Produto de Software"
date: 2024-02-14T00:43:11-03:00
weight: 5
language: pt
featured_image: "../assets/images/featured/area_Linha de produtos.png"
summary: A Engenharia de Linhas de Produto de Software é uma área especializada na engenharia de software, que se concentra no desenvolvimento eficiente de uma família de produtos de software relacionados. 
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- andre_lanna
tags: 
- software_product_line
nav_next: true
---
<div id="top"></div>

A Engenharia de Linhas de Produto de Software é uma área especializada na engenharia de software, que se concentra no desenvolvimento eficiente de uma família de produtos de software relacionados. Esta disciplina envolve a criação de uma arquitetura comum e um conjunto de componentes compartilhados, permitindo a customização e a geração de múltiplas variantes de produtos de software a partir de uma base comum. Este campo é essencial para melhorar a reutilização de software, reduzir custos e tempo de desenvolvimento, e aumentar a qualidade e a consistência entre os produtos de software.

## {{< i18n "area_coordinator" >}}
**Prof. André Lanna**
<div style="margin-left: 20px;">
No CEDIS, a Engenharia de Linhas de Produto de Software é uma área-chave de pesquisa, desenvolvimento e inovação. Coordenada pelo Prof. André Lanna, a linha de pesquisa foca em avançar as práticas, técnicas e ferramentas relacionadas a esta área. A equipe de pesquisadores se dedica a estudar e melhorar métodos para modelagem de características comuns e variáveis, estratégias de customização, gerenciamento de dependências e integração de novas tecnologias. O objetivo é explorar como linhas de produto de software podem ser eficientemente projetadas, implementadas e mantidas, contribuindo para a eficiência e a competitividade das empresas no mercado de software. A pesquisa nesta área visa não apenas aprimorar o entendimento teórico, mas também aplicar esses conhecimentos na prática, ajudando organizações a otimizar seu desenvolvimento de software em larga escala.
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
{{< filterPeople caput="#### " caputKey="volunteer" categories="volunteer" advisors="" tags="software_product_line" notags="inactive">}}

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
- E-mail para informações e contato com a equipe: [andrelanna@unb.br](mailto:andrelanna@unb.br).

{{< tags >}}