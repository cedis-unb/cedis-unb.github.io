---
author: CEDIS
title: "Teamwork and Soft Skills"
date: 2024-02-14T01:37:18-03:00
language: en
weight: 5
featured_image: "../assets/images/featured/area_Team work and soft skills.png"
summary: The area of Teamwork and Soft Skills is an interdisciplinary field in project management and software development, emphasizing the importance of interpersonal and behavioral skills for the success of IT teams.
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

The area of Teamwork and Soft Skills is an interdisciplinary field in project management and software development, emphasizing the importance of interpersonal and behavioral skills for the success of IT teams. This discipline recognizes that, in addition to technical competencies, skills such as effective communication, collaboration, conflict resolution, leadership, and empathy are fundamental for the efficient operation of software teams. Focusing on soft skills is essential for improving team dynamics, job satisfaction, and consequently, the productivity and quality of the developed software.


## {{< i18n "area_coordinator" >}}
**Prof. George Marsicano**
<div style="margin-left: 20px;">
Under the coordination of Prof. George Marsicano, the research and development line is dedicated to exploring best practices, methodologies, and tools to strengthen collaboration and interpersonal skills in software development environments. The research team, composed of experts in organizational psychology, human resource management, and software engineering, works on themes such as leadership development, effective communication, conflict management, and teamwork techniques. The goal is to create innovative and practical approaches to empower software teams to achieve higher levels of performance and satisfaction, emphasizing the importance of human development in the context of information technology.
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
- Email for information and team contact: [georgemarsicano@unb.br](georgemarsicano@unb.br).

{{< tags >}}