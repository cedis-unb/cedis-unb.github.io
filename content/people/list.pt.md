---
author: CEDIS
title: "Colaboradores"
date: 2024-02-14T00:48:51-03:00
weight: 20
language: pt
---
<div class="space-y-4">
  <!-- Seção de Colaboradores Atuais -->
  <div>
    <h2 class="text-xl font-bold mb-2 text-primary-900">Colaboradores Atuais</h2>
    <p class="mb-4 text-neutral-700">Conheça a equipe que está contribuindo ativamente para nossos projetos e pesquisas.</p>
    <div>
      {{< teste caput="## Doutorado" categories="phd_candidate" tags="" notags="inactive" >}}
      {{< teste caput="## Mestrado" categories="master_student" tags="" notags="inactive" >}}
      {{< teste caput="## Especialização Pós-Graduada" categories="specialization" tags="" notags="inactive" >}}
      {{< teste caput="## Pesquisa de Graduação" categories="scientific_initiation" tags="" notags="inactive" >}}
      {{< teste caput="## Trabalho de Conclusão de Curso" categories="tcc" tags="" notags="inactive" >}}
    </div>
  </div>
  <div id="formers-section"></div>
  <!-- Seção de Colaboradores Anteriores -->
  <div id="previous-collaborators" x-data="{ showPrevious: false }">
    <h2 id="former-collaborators-title" @click="showPrevious = !showPrevious" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      Colaboradores Anteriores
      <svg :class="{'rotate-0': !showPrevious, 'rotate-180': showPrevious}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <p x-show="showPrevious" x-cloak class="mb-4 text-neutral-700">Estes são os colaboradores que contribuíram para o nosso sucesso no passado. Somos gratos por seu esforço e dedicação.</p>
    <div x-show="showPrevious" x-cloak>
      {{< teste caput="## Doutorado" categories="phd_candidate" tags="inactive" notags="" >}}
      {{< teste caput="## Mestrado" categories="master_student" tags="inactive" notags="" >}}
      {{< teste caput="## Especialização Pós-Graduada" categories="specialization" tags="inactive" notags="" >}}
      {{< teste caput="## Pesquisa de Graduação" categories="scientific_initiation" tags="inactive" notags="" >}}
      {{< teste caput="## Trabalho de Conclusão de Curso" categories="tcc" tags="inactive" notags="" >}}
    </div>
  </div>
</div>

{{< backToTopBtn target="formers-section" >}}