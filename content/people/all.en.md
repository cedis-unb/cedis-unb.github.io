---
author: CEDIS
title: "Collaborators"
date: 2024-02-14T00:48:51-03:00
weight: 20
language: en
featured_image: "../assets/images/featured/people_Collaborators.png"
authorimage: ../assets/images/global/author.webp
---
<div class="space-y-4">
  <!-- Current Collaborators Section -->
  <div>
    <h2 class="text-xxl font-bold mb-2 text-primary-900">Current Collaborators</h2>
    <p class="mb-4 text-neutral-700">Meet the team that is actively contributing to our projects and research.</p>
    <div>
      {{< filterPeople caput="### PhD" categories="phd_candidate" tags="" notags="inactive" >}}
      {{< filterPeople caput="### Master's degree" categories="master_student" tags="" notags="inactive" >}}
      {{< filterPeople caput="### Postgraduate Specialization" categories="specialization" tags="" notags="inactive" >}}
      {{< filterPeople caput="### Undergraduate Research" categories="scientific_initiation" tags="" notags="inactive" >}}
      {{< filterPeople caput="### Bachelor's Thesis" categories="tcc" tags="" notags="inactive" >}}
      {{< filterPeople caput="### CEDIS volunteer" categories="volunteer" tags="" notags="inactive" >}}
    </div>
  </div>
  <div id="formers-section"></div>
  <!-- Former Collaborators Section -->
  <div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      Former Collaborators
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <p x-show="showPrevious" x-cloak class="mb-4 text-neutral-700">These are the collaborators who contributed to our success in the past. We are grateful for their effort and dedication.</p>
    <div x-show="showPrevious" x-cloak>
      {{< publications caput="#### PhD" year="" types="phd" advisors="" notypes="" tags="" notags="sergio_freitas" >}}
      {{< publications caput="#### Master's degree" year="" types="dissertation" advisors="" notypes="" tags="" notags="sergio_freitas" >}}
      {{< publications caput="#### Postgraduate Specialization" year="" types="specialization" advisors="" notypes="" tags="" notags="" >}}
      {{< filterPeople caput="#### Undergraduate Research" categories="scientific_initiation" advisors="" tags="inactive" notags="">}}
      {{< publications caput="#### Bachelor's Thesis" year="" types="tcc" advisors="" notypes="" tags="" notags="" >}}
      {{< publications caput="#### CEDIS volunteer" year="" types="volunteer" advisors="" notypes="" tags="" notags="" >}}
    </div>
  </div>
</div>

{{< backToTopBtn target="formers-section" >}}

