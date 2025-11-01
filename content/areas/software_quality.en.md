---
author: CEDIS
title: "Software Quality"
date: 2024-02-14T01:37:18-03:00
language: en
weight: 5
featured_image: "../assets/images/featured/area_Software Quality.png"
summary: Constitutes a fundamental pillar in software engineering, directly reflecting on user satisfaction, operational efficiency, and the sustainability of computer systems. 
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

Software Quality constitutes a fundamental pillar in software engineering, directly reflecting on user satisfaction, operational efficiency, and the sustainability of computer systems. This concept encompasses a range of attributes and criteria that determine how well software meets the needs and expectations of its users and stakeholders, in addition to adhering to pre-established development standards.

To understand Software Quality, it is essential to consider two aspects: internal quality and external quality. Internal quality refers to the inherent characteristics of the software's code and architecture, including its readability, reusability, modularity, and the ease with which it can be maintained and evolved. These attributes are critical for the developers and maintainers of the system. On the other hand, external quality relates to the user's experience when interacting with the software, covering aspects such as usability, performance, reliability, and security. External quality is often assessed through software testing and direct feedback from users.

Standards and models have been developed to assist in the evaluation and assurance of software quality, among which ISO/IEC 25010:2011, also known as SQuaRE (System and Software Quality Requirements and Evaluation), and CMMI (Capability Maturity Model Integration) stand out. The ISO/IEC 25010 model, for instance, defines a set of quality characteristics, subdivided into sub-characteristics, that provide a framework for software evaluation. Such characteristics include functionality, performance efficiency, compatibility, usability, reliability, security, maintainability, and portability.

The implementation of software quality assurance practices is a continuous process, starting in the early stages of software conception and extending throughout its life cycle. It involves the application of agile development methodologies, continuous integration, automated testing, code reviews, and other software engineering practices aimed at identifying and correcting defects early, improving development efficiency, and ensuring that the final product meets or exceeds user expectations.

In summary, software quality is not an attribute that can be added after development; it must be an intrinsic consideration at every stage of the software development process. A systematic approach to quality management is important for delivering software products that not only function as expected but also provide a satisfactory user experience, remain relevant and evolvable in the face of market demands and technological challenges.


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
{{< filterPeople caput="#### " caputKey="volunteer" categories="volunteer" advisors="" tags="software_quality" notags="inactive">}}

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
- Email for information and team contact: [ricardoajax@unb.br](mailto:ricardoajax@unb.br).

{{< tags >}}