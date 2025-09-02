---
author: CEDIS
title: "Artificial Intelligence and Natural Language Processing"
date: 2025-08-02T01:37:18-03:00
language: en
weight: 5
featured_image: "../assets/images/featured/area_IA.png"
summary: Artificial Intelligence (AI) is a branch of computer science that seeks to develop systems capable of mimicking and enhancing human abilities such as reasoning, learning, and perception. One of its most fascinating subareas is Natural Language Processing (NLP).
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

Artificial Intelligence (AI) is a branch of computer science that seeks to develop systems capable of mimicking and enhancing human abilities such as reasoning, learning, and perception. One of its most fascinating subareas is Natural Language Processing (NLP), dedicated to understanding and interpreting human language, allowing machines and programs to interact with people more efficiently and intuitively. NLP encompasses everything from syntactic and semantic analysis of words to the generation of coherent and meaningful text, enabling the creation of virtual assistants, automatic translation systems, and other applications that facilitate communication and information access in our daily lives.

## {{< i18n "area_coordinator" >}}

**Prof. Sergio Antônio Andrade de Freitas**
<div style="margin-left: 20px;">
Professor and researcher in the field of Artificial Intelligence (AI) and Natural Language Processing (NLP), he holds a tenure position at the University of Brasília - UnB. Some of his contributions to the field of NLP include the automated interpretation of anaphoras, a pioneering study that deepened the understanding of how machines can process and interpret human text, contributing to the resolution of anaphoras and advancements in computational text comprehension. Moreover, his research in AI explores the integration of advanced computational methods to develop more intelligent and intuitive systems, enhancing human-computer interaction and promoting technological innovations in the field. Currently, he is a faculty member of the Software Engineering course and an active member of the Graduate Program in Applied Computing (PPCA).
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
For information and contact with the team: [sergiofreitas@unb.br](mailto:sergiofreitas@unb.br).

{{< tags >}}