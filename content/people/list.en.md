---
author: CEDIS
title: "Collaborators"
date: 2024-02-14T00:48:51-03:00
weight: 20
language: en
---
<div class="space-y-4">
  <!-- Current Collaborators Section -->
  <div>
    <h2 class="text-xl font-bold mb-2">Current Collaborators</h2>
    <p class="mb-4 text-gray-600">Meet the team that is actively contributing to our projects and research.</p>
    <div>
  {{< teste caput="## PhD" categories="phd_candidate" tags="" notags="inactive" >}}
  {{< teste caput="## Master's degree" categories="master_student" tags="" notags="inactive" >}}
  {{< teste caput="## Postgraduate Specialization" categories="specialization" tags="" notags="inactive" >}}
  {{< teste caput="## Undergraduate Research" categories="scientific_initiation" tags="" notags="inactive" >}}
  {{< teste caput="## Bachelor's Thesis" categories="tcc" tags="" notags="inactive" >}}
    </div>
  </div>

  <!-- Former Collaborators Section -->
  <div x-data="{ showPrevious: false }">
    <h2 @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center">
      Former Collaborators
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <p x-show="showPrevious" x-cloak class="mb-4 text-gray-600">These are the collaborators who contributed to our success in the past. We are grateful for their effort and dedication.</p>
    <div x-show="showPrevious" x-cloak>
    <!-- Conteúdo da Seção "Previous" -->
    {{< teste caput="## PhD" categories="phd_candidate" tags="inactive" notags="" >}}
    {{< teste caput="## Master's degree" categories="master_student" tags="inactive" notags="" >}}
    {{< teste caput="## Postgraduate Specialization" categories="specialization" tags="inactive" notags="" >}}
    {{< teste caput="## Undergraduate Research" categories="scientific_initiation" tags="inactive" notags="" >}}
    {{< teste caput="## Bachelor's Thesis" categories="tcc" tags="inactive" notags="" >}}
    </div>
  </div>
</div>

