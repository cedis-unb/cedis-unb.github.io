---
author: CEDIS
title: "Verificação, Validação e Testes"
date: 2024-02-14T00:43:11-03:00
weight: 5
language: pt
featured_image: "../assets/images/featured/area_Verificação e Validação.png"
summary: A área de Verificação, Validação e Testes é uma disciplina crítica na engenharia de software, focada em garantir que os produtos de software atendam aos seus requisitos especificados e funcionem conforme esperado.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- cristiane_ramos
- ricardo_ajax
tags: 
- verification_validation_testing
nav_next: true
---
<div id="top"></div>

A área de Verificação, Validação e Testes é uma disciplina crítica na engenharia de software, focada em garantir que os produtos de software atendam aos seus requisitos especificados e funcionem conforme esperado. Esta área abrange uma ampla gama de atividades, incluindo a verificação de que o software atende a todas as especificações de design e desenvolvimento, a validação de que o software atende às necessidades e expectativas do usuário final, e a realização de testes sistemáticos para identificar e corrigir defeitos.

## {{< i18n "area_coordinator" >}}
**Prof. Cristiane Ramos**
<div style="margin-left: 20px;">
No CEDIS, a área de Verificação, Validação e Testes são considerados pilares fundamentais para o desenvolvimento de software de alta qualidade. Sob a coordenação da Profa. Cristiane Ramos, a linha de pesquisa se dedica ao estudo e aprimoramento de métodos, ferramentas e processos que possam aumentar a eficácia e a eficiência dessas atividades. A equipe de pesquisadores especializados trabalha em diversos tópicos, como automação de testes, testes de regressão, testes de usabilidade, testes de desempenho e segurança, além da integração de práticas de verificação e validação em metodologias ágeis de desenvolvimento de software. O objetivo é desenvolver abordagens inovadoras que possam reduzir o tempo e o custo do processo de teste, ao mesmo tempo que aumentam a confiabilidade e a segurança dos produtos de software.
<br>
{{< link-interno "/people/cristiane_ramos" "area_more_about_a" >}}
</div>

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="verification_validation_testing" notags="inactive" nocats="cristiane_ramos">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="verification_validation_testing" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="verification_validation_testing" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="verification_validation_testing" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="verification_validation_testing" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="verification_validation_testing" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="volunteer" categories="volunteer" advisors="" tags="verification_validation_testing" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="verification_validation_testing" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="verification_validation_testing" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="verification_validation_testing" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="verification_validation_testing" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="verification_validation_testing" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="verification_validation_testing" >}}


## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="verification_validation_testing" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="verification_validation_testing" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
- E-mail para informações e contato com a equipe: [cristianesramos@unb.br](mailto:cristianesramos@unb.br).

{{< tags >}}