---
author: CEDIS
title: "Cibersegurança"
date: 2025-09-02T01:37:18-03:00
language: pt-br
weight: 5
featured_image: "../assets/images/featured/area_Cibersecurity.png"
summary: 'Cibersegurança consiste em um conjunto de práticas, tecnologias e metodologias voltadas para proteger sistemas, redes e dados contra acessos não autorizados, ciberataques, ameaças persistentes e falhas de segurança. Seu objetivo central é garantir a confidencialidade, a integridade e a disponibilidade da informação, especialmente em ambientes digitais cada vez mais complexos e interconectados.'
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

Cibersegurança consiste em um conjunto de práticas, tecnologias e metodologias voltadas para proteger sistemas, redes e dados contra acessos não autorizados, ciberataques, ameaças persistentes e falhas de segurança. Seu objetivo central é garantir a confidencialidade, a integridade e a disponibilidade da informação, especialmente em ambientes digitais cada vez mais complexos e interconectados.

## {{< i18n "area_coordinator" >}}
**Prof. Sergio Antônio Andrade de Freitas**  
<div style="margin-left: 20px;">  
Professor titular da Universidade de Brasília (UnB) e pesquisador em Engenharia de Software, com ampla experiência em cibersegurança e garantia da informação. Sua trajetória acadêmica inclui a orientação de trabalhos de graduação e pós-graduação em detecção de intrusões, protocolos criptográficos, análise de riscos e gestão de segurança da informação aplicada a organizações públicas e privadas. Coordenou e orientou projetos envolvendo arquiteturas seguras, governança de TI no setor público e continuidade de serviços críticos. Sua pesquisa integra cibersegurança com {{< link-interno "/areas/learning_analytics" "Learning Analytics" >}}. Suas contribuições se estendem à pesquisa aplicada, à formação de profissionais e à inovação em estratégias de ensino e aprendizagem no domínio da Engenharia de Software e da segurança da informação. <br>  
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
E-mail para informações e contato com a equipe: [sergiofreitas@unb.br](mailto:sergiofreitas@unb.br).

{{< tags >}}
