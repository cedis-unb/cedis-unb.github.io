---
author: CEDIS
title: "Colaboradores"
date: 2024-02-14T00:48:51-03:00
weight: 20
language: pt
featured_image: "../assets/images/featured/people_Collaborators.png"
authorimage: ../assets/images/global/author.webp
---
<div class="space-y-4">
  <!-- Current Collaborators Section -->
  <div>
    <h2 class="text-xxl font-bold mb-2 text-primary-900">Colaboradores atuais</h2>
    <p class="mb-4 text-neutral-700">Conheça a equipe que está contribuindo ativamente para nossos projetos e pesquisas.</p>
    <div>
      {{< filterPeople caput="### PhD" categories="phd_candidate" tags="" notags="inactive" >}}
      {{< filterPeople caput="### Mestrado" categories="master_student" tags="" notags="inactive" >}}
      {{< filterPeople caput="### Especialização" categories="specialization" tags="" notags="inactive" >}}
      {{< filterPeople caput="### Iniciação científica" categories="scientific_initiation" tags="" notags="inactive" >}}
      {{< filterPeople caput="### TCC" categories="tcc" tags="" notags="inactive" >}}
      {{< filterPeople caput="### Voluntário CEDIS" categories="volunteer" tags="" notags="inactive" >}}
    </div>
  </div>
  <div id="formers-section"></div>
  <!-- Former Collaborators Section -->
  <div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      Colaboradores anteriores
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <p x-show="showPrevious" x-cloak class="mb-4 text-neutral-700">Estes são os colaboradores que contribuíram para o nosso sucesso no passado. Somos gratos pelo esforço e dedicação deles.</p>
    <div x-show="showPrevious" x-cloak>
    {{< publications caput="#### Doutorado" year="" types="phd" advisors="" notypes="" tags="" notags="sergio_freitas" >}}
    {{< publications caput="#### Mestrado" year="" types="dissertation" advisors="" notypes="" tags="" notags="sergio_freitas" >}}
    {{< publications caput="#### Especialização" year="" types="specialization" advisors="" notypes="" tags="" notags="" >}}
    {{< filterPeople caput="#### Iniciação Científica" categories="scientific_initiation" advisors="" tags="inactive" notags="">}}
    {{< publications caput="#### Trabalho de Conclusão de Curso (TCC)" year="" types="tcc" advisors="" notypes="" tags="" notags="" >}}
    {{< publications caput="#### Voluntário CEDIS" year="" types="volunteer" advisors="" notypes="" tags="" notags="" >}}
    {{< backToTopBtn target="top" >}}
    </div>
  </div>
</div>

{{< backToTopBtn target="formers-section" >}}

