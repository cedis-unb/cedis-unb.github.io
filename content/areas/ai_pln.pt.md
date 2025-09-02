---
author: CEDIS
title: "Inteligência Artificial e Processamento de Linguagem Natural"
date: 2025-08-02T01:37:18-03:00
language: pt
weight: 5
featured_image: "../assets/images/featured/area_IA.png"
summary: A Inteligência Artificial (IA) é um ramo da ciência da computação que busca desenvolver sistemas capazes de imitar e aprimorar habilidades humanas, como o raciocínio, aprendizado e percepção. Uma de suas subáreas mais fascinantes é o Processamento de Linguagem Natural (PLN).
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- sergio_freitas
tags: 
- ai
- nlp
- machine_learning
nav_next: true
---
<div id="top"></div>

A Inteligência Artificial (IA) é um ramo da ciência da computação que busca desenvolver sistemas capazes de imitar e aprimorar habilidades humanas, como o raciocínio, aprendizado e percepção. Uma de suas subáreas mais fascinantes é o Processamento de Linguagem Natural (PLN), que se dedica a compreender e interpretar a linguagem humana, permitindo que máquinas e programas interajam com as pessoas de maneira mais eficiente e intuitiva. O PLN engloba desde a análise sintática e semântica das palavras até a geração de texto coerente e significativo, possibilitando a criação de assistentes virtuais, sistemas de tradução automática e outras aplicações que facilitam a comunicação e o acesso à informação em nosso cotidiano.

## {{< i18n "area_coordinator" >}}

**Prof. Sergio Antônio Andrade de Freitas**
<div style="margin-left: 20px;">
Professor e pesquisador na área de Inteligência Artificial (IA) e Processamento de Linguagem Natural (PLN), é professor Titular na Universidade de Brasília - UnB. Algumas de suas contribuições para o campo do PLN são a interpretação automatizada de anáforas, um estudo pioneiro que aprofundou a compreensão de como máquinas podem processar e interpretar texto humano, contribuindo para a resolução de anáforas e avanços na compreensão textual computacional. Além disso, suas pesquisas em IA exploram a integração de métodos computacionais avançados para desenvolver sistemas mais inteligentes e intuitivos, reforçando a interação humana-computador e promovendo inovações tecnológicas no campo. Atualmente, ele é docente do curso de Engenharia de Software e membro ativo do corpo docente do Programa de Pós-graduação em Computação Aplicada (PPCA).
<br>
{{< link-interno "/people/sergio_freitas" "area_more_about" >}}
</div>

## {{< i18n "area_research_team" >}}
{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="ai,nlp,machine_learning" notags="inactive" nocats="sergio_freitas">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="ai,nlp,machine_learning" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="ai,nlp,machine_learning" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="ai,nlp,machine_learning" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="ai,nlp,machine_learning" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="ai,nlp,machine_learning" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="ai,nlp,machine_learning" notags="active,sergio_freitas" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="ai,nlp,machine_learning" notags="active,sergio_freitas" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="ai,nlp,machine_learning" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="ai,nlp,machine_learning" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="ai,nlp,machine_learning" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="ai,nlp,machine_learning" >}}

## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="ai,nlp,machine_learning" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="ai,nlp,machine_learning" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

### {{< i18n "area_apps" >}}
- FREITAS, S. A. A.; SILVA, A. C.; SILVA; M. Fl; BATISTA, R. C.; Contextus - AI, NLP, and ML platform for Scientific Analysis. 2024.
- FREITAS, S. A. A.; PEREIRA, J. G. L. ; QUARESMA, P. ; RODRIGUES, I. P. Engine for document retrieval of PGR opinions on the web, integrating morpho-syntactic knowledge of Portuguese. 1998.

## {{< i18n "area_contact" >}}
E-mail para informações e contato com a equipe: [sergiofreitas@unb.br](mailto:sergiofreitas@unb.br).

{{< tags >}}