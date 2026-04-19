---
author: CEDIS
title: "Collaborators"
date: 2024-02-14T00:48:51-03:00
weight: 20
language: en
layout: collaborators
description: "Active team and historical collaborators of CEDIS, organized by training stage and academic trajectory."
featured_image: "../assets/images/featured/people_Collaborators.png"
authorimage: ../assets/images/global/author.webp
---
<div class="space-y-10">
<section class="overflow-hidden rounded-[2rem] border border-black/5 bg-white/80 shadow-[0_20px_70px_rgba(15,23,42,0.08)] backdrop-blur dark:border-white/10 dark:bg-white/[0.04]">
<div class="grid gap-6 px-6 py-6 md:px-8 md:py-8 lg:grid-cols-[minmax(0,1.2fr)_minmax(18rem,0.8fr)] lg:items-start">
<div>
<span class="inline-flex rounded-full border border-primary-200 bg-primary-50 px-3 py-1 text-[0.68rem] font-semibold uppercase tracking-[0.24em] text-primary-700 dark:border-primary-400/30 dark:bg-primary-500/10 dark:text-primary-200">Active network</span>
<h2 id="current-collaborators" class="mt-4 text-3xl font-black tracking-tight text-gray-950 dark:text-white md:text-4xl">Current Collaborators</h2>
<p class="mt-4 max-w-3xl text-base leading-7 text-gray-600 dark:text-white/72">Meet the team actively contributing to CEDIS projects, research, and supervision. The sections below organize the network by training stage so the page is easier to scan.</p>
<div class="mt-6 flex flex-wrap gap-3">
<a href="#previous-collaborators" class="inline-flex items-center rounded-full border border-black/10 bg-white px-4 py-2 text-sm font-semibold text-gray-700 transition-colors hover:border-primary-500 hover:text-primary-600 dark:border-white/10 dark:bg-white/[0.03] dark:text-white/80 dark:hover:border-primary-300 dark:hover:text-primary-200">Jump to legacy</a>
</div>
</div>
<div class="grid gap-3">
<div class="rounded-[1.5rem] border border-black/5 bg-stone-50 px-4 py-4 dark:border-white/10 dark:bg-white/[0.03]">
<div class="text-[0.68rem] font-semibold uppercase tracking-[0.24em] text-gray-400 dark:text-white/45">Coverage</div>
<p class="mt-3 text-sm leading-6 text-gray-600 dark:text-white/70">PhD, master's, specialization, undergraduate research, bachelor's thesis, and volunteer collaboration in one place.</p>
</div>
<div class="rounded-[1.5rem] border border-black/5 bg-stone-50 px-4 py-4 dark:border-white/10 dark:bg-white/[0.03]">
<div class="text-[0.68rem] font-semibold uppercase tracking-[0.24em] text-gray-400 dark:text-white/45">Quick reading</div>
<p class="mt-3 text-sm leading-6 text-gray-600 dark:text-white/70">Open the legacy section to review completed supervisions, alumni, and the academic memory of the collaboration network.</p>
</div>
</div>
</div>
</section>
<section class="space-y-6">
{{< filterPeople caput="### PhD" categories="phd_candidate" tags="" notags="inactive" >}}
{{< filterPeople caput="### Master's degree" categories="master_student" tags="" notags="inactive" >}}
{{< filterPeople caput="### Postgraduate Specialization" categories="specialization" tags="" notags="inactive" >}}
{{< filterPeople caput="### Undergraduate Research" categories="scientific_initiation" tags="" notags="inactive" >}}
{{< filterPeople caput="### Bachelor's Thesis" categories="tcc" tags="" notags="inactive" >}}
{{< filterPeople caput="### CEDIS volunteer" categories="volunteer" tags="" notags="inactive" >}}
</section>
<div id="formers-section"></div>
<section id="previous-collaborators" x-data="{ showPrevious: false }" class="overflow-hidden rounded-[2rem] border border-black/5 bg-white/80 shadow-[0_20px_70px_rgba(15,23,42,0.08)] backdrop-blur dark:border-white/10 dark:bg-white/[0.04]">
<button type="button" @click="showPrevious = !showPrevious" class="flex w-full items-center justify-between gap-6 px-6 py-6 text-left transition-colors hover:bg-black/[0.02] dark:hover:bg-white/[0.02] md:px-8 md:py-7">
<div>
<span class="text-[0.68rem] font-semibold uppercase tracking-[0.24em] text-gray-400 dark:text-white/45">Group legacy</span>
<h2 id="former-collaborators-title" class="mt-3 text-3xl font-black tracking-tight text-gray-950 dark:text-white md:text-4xl">Former Collaborators</h2>
</div>
<svg :class="{'rotate-180': showPrevious, 'rotate-0': !showPrevious}" class="h-6 w-6 shrink-0 transform text-primary-600 transition-transform duration-200 dark:text-primary-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
</button>
<div x-show="showPrevious" x-cloak class="space-y-6 border-t border-black/5 px-6 py-6 dark:border-white/10 md:px-8 md:py-8">
<p class="m-0 max-w-3xl text-base leading-7 text-gray-600 dark:text-white/72">This section preserves completed supervisions, alumni, and contributions that helped shape the CEDIS trajectory. It keeps the academic and institutional memory of the collaboration network accessible.</p>
{{< publications caput="#### PhD" year="" types="phd" advisors="" notypes="" tags="" notags="sergio_freitas" >}}
{{< publications caput="#### Master's degree" year="" types="dissertation" advisors="" notypes="" tags="" notags="sergio_freitas" >}}
{{< publications caput="#### Postgraduate Specialization" year="" types="specialization" advisors="" notypes="" tags="" notags="" >}}
{{< filterPeople caput="#### Undergraduate Research" categories="scientific_initiation" advisors="" tags="inactive" notags="">}}
{{< publications caput="#### Bachelor's Thesis" year="" types="tcc" advisors="" notypes="" tags="" notags="" >}}
{{< publications caput="#### CEDIS volunteer" year="" types="volunteer" advisors="" notypes="" tags="" notags="" >}}
{{< backToTopBtn target="top" >}}
</div>
</section>
</div>
{{< backToTopBtn target="formers-section" >}}

