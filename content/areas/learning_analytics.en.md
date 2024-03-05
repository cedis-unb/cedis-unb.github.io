---
author: CEDIS
title: "Learning Analytics and Educational Management"
date: 2024-02-14T02:18:30-03:00
weight: 5
language: en
featured_image: "../assets/images/featured/area_Learning Analytics.png"
summary: An interdisciplinary area that combines data analysis, computer science, and educational psychology to enhance learning and educational environments. By collecting, analyzing, and interpreting data about learners and their contexts, it provides insights to personalize education, identify students who need more support, and improve educational outcomes.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- sergio_freitas
- cristiane_ramos
tags: 
- learning_analytics
nav_next: true
---
<div id="top"></div>

Learning Analytics is an interdisciplinary field that integrates data analysis, computer science, and educational psychology to improve learning and educational environments. By collecting, analyzing, and interpreting data about learners and their contexts, it offers insights for personalizing education, identifying students in need of additional support, and enhancing educational outcomes. In educational management, it is important for providing significant data for decisions about resources and teaching strategies, helping to identify trends and future needs. Its integration represents a significant shift in education, making it more data-driven, responsive, and student-centered.

## {{< i18n "area_coordinators" >}}
**Prof. Sergio Antônio Andrade de Freitas**
<div style="margin-left: 20px;">
A researcher in the field of Learning Analytics and Educational Management, he is a Full Professor at the University of Brasília - UnB. In addition to being a faculty member in the Software Engineering course, he has played a significant role in various administrative functions within and outside UnB, including president of the National Forum of Undergraduate Deans (ForGRAD), Dean of Undergraduate Studies, and director of the Distance Education Center (CEAD). Currently, he is an active member of the faculty in the Postgraduate Program in Applied Computing (PPCA), dedicating himself intensely to research in Active Methodologies in the fields of Engineering, Computing, and Learning Analytics.
<br>
{{< link-interno "/people/sergio_freitas" "area_more_about" >}}
</div>

**Profa. Cristiane Soares Ramos**
<div style="margin-left: 20px;">
An academic in the area of Learning Analytics and Educational Management. She serves as a professor in the Software Engineering course at the University of Brasília, where she is distinguished by her innovative approach and commitment to teaching and research quality. Her specialization in Knowledge Management and Information Technology, with a focus on software quality, positions her at the forefront of integrating educational technologies and data analysis into the learning process. 
<br>
{{< link-interno "/people/cristiane_soares" "area_more_about_a" >}}
</div>

## {{< i18n "area_research_team" >}}

{{< filterPeople caput="#### " caputKey="researcher" categories="researcher" advisors="" tags="learning_analytics" notags="inactive" nocats="sergio_freitas,cristiane_ramos">}}
{{< filterPeople caput="#### " caputKey="phd_candidate" categories="phd_candidate" advisors="" tags="learning_analytics" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="master_student" categories="master_student" advisors="" tags="learning_analytics" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="specialization" categories="specialization" advisors="" tags="learning_analytics" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="learning_analytics" notags="inactive">}}
{{< filterPeople caput="#### " caputKey="tcc" categories="tcc" advisors="" tags="learning_analytics" notags="inactive">}}

<div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< i18n "area_previous_researchers" >}}
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### " caputKey="phd_candidate"  year="" types="phd" advisors="" notypes="" tags="learning_analytics" notags="active" >}}
    {{< publications caput="#### " caputKey="master_student" year="" types="dissertation" advisors="" notypes="" tags="learning_analytics" notags="active" >}}
    {{< publications caput="#### " caputKey="specialization" year="" types="specialization" advisors="" notypes="" tags="learning_analytics" notags="active" >}}
    {{< filterPeople caput="#### " caputKey="scientific_initiation" categories="scientific_initiation" advisors="" tags="learning_analytics" notags="active">}}
    {{< publications caput="#### " caputKey="tcc" year="" types="tcc" advisors="" notypes="" tags="learning_analytics" notags="active" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>

## {{< i18n "area_ongoing_projets" >}}

{{< postsByCategoriesTags categories="project" tags="learning_analytics" >}}
- A new approach applied to the University Course Timetable Problem  
    Éber Júnio Borges Moreira, Start: 2023, status: ongoing.  
    Work focused on optimizing university course scheduling, applying techniques to improve efficiency and effectiveness in academic timetable management. This work aims to solve common challenges in timetable management, providing a more adaptable and convenient solution for higher education institutions. UnB is used as a case study.


## {{< i18n "area_publications_productions" >}}

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< publications countOnly=true caputKey="publications" year="" type="" notypes="" tags="learning_analytics" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="learning_analytics" notags="" >}} 
      {{< backToTopBtn target="top" >}}
    </div>
</div>

### {{< i18n "area_apps" >}}
1. FREITAS, S. A. A. Analyzer of quality indicators of Brazilian higher education. UnB, 2020.
2. FREITAS, S. A. A. Collaborative editor for pedagogical course projects - UnB version. 2019.
3. FREITAS, S. A. A. MCE - Curriculum Matrix Editor. UFES, 2005.
4. FREITAS, S. A. A. Course Pedagogical Project Generator. UFES, 2005.
5. FREITAS, S. A. A. Academic Management System for Postgraduate Courses at the Federal University of Espírito Santo (UFES). UFES, 2002.

## {{< i18n "area_contact" >}}
- Email for information and contact with the team: [sergiofreitas@unb.br](mailto:sergiofreitas@unb.br) or [cristanesramos@unb.br](mailto:cristanesramos@unb.br).

{{< tags >}}
