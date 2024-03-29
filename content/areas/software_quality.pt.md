---
author: CEDIS
title: "Qualidade de Software"
date: 2024-02-14T01:37:18-03:00
language: pt
weight: 5
featured_image: "../assets/images/featured/area_Software Quality.png"
summary: Um dos pilares fundamentais na engenharia de software, reflete diretamente na satisfação do usuário, na eficiência operacional e na sustentabilidade de sistemas computacionais. 
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- cristiane_ramos
- ricardo_ajax
tags: 
- software_quality
nav_next: true
---
<div id="top"></div>

A Qualidade de Software constitui um dos pilares fundamentais na engenharia de software, refletindo diretamente na satisfação do usuário, na eficiência operacional e na sustentabilidade de sistemas computacionais. Este conceito abrange uma gama de atributos e critérios que determinam o quão bem um software atende às necessidades e expectativas dos seus usuários e stakeholders, além de aderir a padrões de desenvolvimento pré-estabelecidos.

Para compreender a Qualidade de Software, é essencial considerar dois aspectos: a qualidade interna e a qualidade externa. A qualidade interna diz respeito às características inerentes ao código e à arquitetura do software, incluindo sua legibilidade, reusabilidade, modularidade, e a facilidade com que pode ser mantido e evoluído. Estes atributos são críticos para os desenvolvedores e mantenedores do sistema. Por outro lado, a qualidade externa relaciona-se com a experiência do usuário ao interagir com o software, abrangendo aspectos como usabilidade, desempenho, confiabilidade, e segurança. A qualidade externa é frequentemente avaliada por meio de testes de software e feedback direto dos usuários.

Normas e modelos têm sido desenvolvidos para auxiliar na avaliação e garantia da qualidade de software, entre os quais se destacam o ISO/IEC 25010:2011, também conhecido como SQuaRE (System and Software Quality Requirements and Evaluation), e o CMMI (Capability Maturity Model Integration). O modelo ISO/IEC 25010, por exemplo, define um conjunto de características de qualidade, subdivididas em subcaracterísticas, que proporcionam um framework para a avaliação do software. Tais características incluem a funcionalidade, eficiência de desempenho, compatibilidade, usabilidade, confiabilidade, segurança, manutenibilidade e portabilidade.

A implementação de práticas de garantia de qualidade de software é um processo contínuo, que começa nas fases iniciais de concepção do software e se estende por todo o seu ciclo de vida. Envolve a aplicação de metodologias de desenvolvimento ágil, integração contínua, testes automatizados, revisões de código, e outras práticas de engenharia de software destinadas a identificar e corrigir defeitos precocemente, melhorar a eficiência do desenvolvimento, e assegurar que o produto final atenda ou supere as expectativas dos usuários.

Em suma, a qualidade de software não é um atributo que pode ser adicionado após o desenvolvimento; ela deve ser uma consideração intrínseca em cada etapa do processo de desenvolvimento de software. Uma abordagem sistemática para a gestão da qualidade é fundamental para a entrega de produtos de software que não apenas funcionem conforme o esperado, mas que também ofereçam uma experiência de usuário satisfatória, mantenham-se relevantes e evolutivos frente às demandas do mercado e desafios tecnológicos.

## {{< i18n "area_coordinator" >}}
**Prof. Ricardo Ajax**
<div style="margin-left: 20px;">
<br>
{{< link-interno "/people/ricardo_ajax" "area_more_about" >}}
</div>

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="software_quality" notags="inactive" nocats="ricardo_ajax">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="software_quality" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="software_quality" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="software_quality" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="software_quality" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="software_quality" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="software_quality" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="software_quality" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="software_quality" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="software_quality" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="software_quality" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="software_quality" >}}


## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="software_quality" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="software_quality" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

## {{< i18n "area_contact" >}}
- E-mail para informações e contato com a equipe: [ricardoajax@unb.br](mailto:ricardoajax@unb.br).

{{< tags >}}