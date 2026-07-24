---
author: CEDIS
title: "Daniel Sundfeld Lima"
profile_level: researcher
date: 2023-05-01T00:00:00-03:00
weight: 70
language: pt
featured_image: "../assets/images/featured/people_Daniel Sundfeld.png"
summary: Professor Adjunto da Universidade de Brasília (UnB), atua no curso de Engenharia de Software com foco em computação paralela, alto desempenho, GPU, nuvem e bioinformática.
contact:
  email: daniel.sundfeld@unb.br
  lattes: https://lattes.cnpq.br/2619423058109475
  orcid: https://orcid.org/0000-0002-5147-3698
areas:
- hpc
authorimage: ../assets/images/global/author.webp
categories:
- people
- researcher
tags:
- project_laguna
nav_next: true
---
<div id="top"></div>

## {{< i18n "people_profile" >}}
- Posição Atual: Professor Adjunto da [Universidade de Brasília](https://www.unb.br/) (UnB), atuando no curso de graduação em [Engenharia de Software](http://software.unb.br/) desde 2022.
- Áreas de Atuação: {{< link-interno "/areas/hpc/" "Computação paralela" >}}, {{< link-interno "/areas/hpc/" "computação de alto desempenho" >}}, unidades de processamento gráfico (GPU), computação em nuvem, sistemas distribuídos e bioinformática.
- Atuação Institucional: Participa de projetos de pesquisa e desenvolvimento com o IBICT voltados à infraestrutura informacional aberta, lagos de dados e recuperação de informação científica.

## {{< i18n "people_background" >}}
- Doutorado em Informática - Universidade de Brasília, com doutorado-sanduíche na University of Copenhagen (2013-2017).
- Tese de doutorado: "Alinhamento primário e secundário de sequências biológicas em arquiteturas de alto desempenho" (2017).
- Mestrado em Informática - Universidade de Brasília (2010-2012).
- Graduação em Ciência da Computação - Universidade de Brasília (2003-2007).

## {{< i18n "people_professional_activities" >}}
- Professor do magistério superior na Universidade de Brasília desde 2022, atuando no curso de Engenharia de Software.
- Ministrou disciplinas como Fundamentos de Sistemas Operacionais e Algoritmos e Programação de Computadores.
- Foi professor do Instituto Federal de Brasília (2018-2022), incluindo atuação como coordenador do curso de Tecnologia em Sistemas para Internet.
- Possui experiência anterior na indústria como desenvolvedor sênior e gerente de projetos na Aker Security Solutions, com atuação em software de segurança, Linux, redes, OpenSSL e manutenção de produtos.
- Desenvolve pesquisas em computação de alto desempenho, computação em nuvem, sistemas distribuídos e bioinformática, aplicando essas áreas à solução de problemas complexos.

## {{< i18n "people_contributions" >}}
- Menção Honrosa no concurso de Teses e Dissertações em Arquiteturas de Computadores e Computação de Alto Desempenho (WSCAD-CTD), Sociedade Brasileira de Computação (2018).
- Best Achievement Awards - PUMPS 2015, Universitat Politècnica de Catalunya.
- Revisor de periódicos como *Concurrency and Computation: Practice & Experience*, *Journal of the ACM* e *Parallel Computing*.
- Desenvolvimento de ferramentas e softwares como CUDA-Sankoff, Foldalign 2.5 e PA-Star, voltados à bioinformática e ao processamento de alto desempenho.

## {{< i18n "people_research_areas" >}}
{{< postsByCategoriesTags caput="" categories="knowledge_areas,daniel_sundfeld" >}}


## {{< i18n "people_supervisory_experience" >}}
### {{< i18n "people_current_supervisions" >}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="daniel_sundfeld" tags="" notags="inactive" sort="alpha" grid="true">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="daniel_sundfeld" tags="" notags="inactive" sort="alpha" grid="true">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="daniel_sundfeld" tags="" notags="inactive" sort="alpha" grid="true">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="daniel_sundfeld" tags="" notags="inactive" sort="alpha" grid="true">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="daniel_sundfeld" tags="" notags="inactive" sort="alpha" grid="true">}}
<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "people_former_supervisions" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="daniel_sundfeld" notypes="" tags="" notags="active" sort="year_alpha" grid="true">}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="daniel_sundfeld" notypes="" tags="" notags="active" sort="year_alpha" grid="true">}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="daniel_sundfeld" notypes="" tags="" notags="active" sort="year_alpha" grid="true">}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="daniel_sundfeld" tags="" notags="active" sort="year_alpha" grid="true">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="daniel_sundfeld" notypes="" tags="" notags="active" sort="year_alpha" grid="true">}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" types="" notypes="" tags="daniel_sundfeld" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications caput="" year="" types="" notypes="" tags="daniel_sundfeld" notags="" >}}
      {{< backToTopBtn target="top" >}}
    </div>
</div>


{{< backToTopBtn target="top" >}}
