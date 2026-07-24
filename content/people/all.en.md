---
author: CEDIS
title: "Collaborators"
date: 2024-02-14T00:48:51-03:00
weight: 20
language: en
layout: collaborators
description: "Active network and institutional memory of CEDIS — advisees, collaborators, alumni and external authors in the group's outputs."
featured_image: "../assets/images/featured/people_Collaborators.png"
authorimage: ../assets/images/global/author.webp
---
<div class="space-y-10">

<section class="overflow-hidden rounded-[2rem] border border-black/5 bg-white/80 shadow-[0_20px_70px_rgba(15,23,42,0.08)] backdrop-blur dark:border-white/10 dark:bg-white/[0.04]">
<div class="grid gap-6 px-6 py-6 md:px-8 md:py-8 lg:grid-cols-[minmax(0,1.2fr)_minmax(18rem,0.8fr)] lg:items-start">
<div>
<span class="inline-flex rounded-full border border-primary-200 bg-primary-50 px-3 py-1 text-[0.68rem] font-semibold uppercase tracking-[0.24em] text-primary-700 dark:border-primary-400/30 dark:bg-primary-500/10 dark:text-primary-200">CEDIS Network</span>
<h2 id="current-collaborators" class="mt-4 text-3xl font-black tracking-tight text-gray-950 dark:text-white md:text-4xl">Collaborators</h2>
<p class="mt-4 max-w-3xl text-base leading-7 text-gray-600 dark:text-white/72">Advisees in progress, collaborators, alumni and external authors form the human network that produces CEDIS knowledge — organized by academic trajectory for easier reading.</p>
<div class="mt-6 flex flex-wrap gap-2">
<span class="inline-flex items-center gap-2 rounded-full border border-primary-200 bg-primary-50 px-3 py-1 text-sm font-semibold text-primary-700 dark:border-primary-400/25 dark:bg-primary-500/10 dark:text-primary-100"><a href="/categories/researcher/" class="hover:text-primary-600 dark:hover:text-primary-200"><strong>{{< peopleCount level="researcher" >}}</strong> researchers</a></span>
<span class="inline-flex items-center gap-2 rounded-full border border-black/10 bg-white px-3 py-1 text-sm font-semibold text-gray-700 dark:border-white/10 dark:bg-white/[0.03] dark:text-white/78"><strong>{{< peopleCount status="active" >}}</strong> active network</span>
<span class="inline-flex items-center gap-2 rounded-full border border-black/10 bg-white px-3 py-1 text-sm font-semibold text-gray-700 dark:border-white/10 dark:bg-white/[0.03] dark:text-white/78"><strong>{{< peopleCount status="inactive" >}}</strong> alumni</span>
<span class="inline-flex items-center gap-2 rounded-full border border-black/10 bg-white px-3 py-1 text-sm font-semibold text-gray-700 dark:border-white/10 dark:bg-white/[0.03] dark:text-white/78"><a href="#cited-authors" class="hover:text-primary-600 dark:hover:text-primary-200"><strong>{{< peopleCount level="derived" >}}</strong> external authors</a></span>
</div>
<div class="mt-4 flex flex-wrap gap-3">
<a href="#active-network" class="inline-flex items-center rounded-full border border-black/10 bg-white px-4 py-2 text-sm font-semibold text-gray-700 transition-colors hover:border-primary-500 hover:text-primary-600 dark:border-white/10 dark:bg-white/[0.03] dark:text-white/80 dark:hover:border-primary-300 dark:hover:text-primary-200">Active network</a>
<a href="#previous-collaborators" class="inline-flex items-center rounded-full border border-black/10 bg-white px-4 py-2 text-sm font-semibold text-gray-700 transition-colors hover:border-primary-500 hover:text-primary-600 dark:border-white/10 dark:bg-white/[0.03] dark:text-white/80 dark:hover:border-primary-300 dark:hover:text-primary-200">Alumni</a>
</div>
</div>
<div class="grid gap-3">
<div class="rounded-[1.5rem] border border-black/5 bg-stone-50 px-4 py-4 dark:border-white/10 dark:bg-white/[0.03]">
<div class="text-[0.68rem] font-semibold uppercase tracking-[0.24em] text-gray-400 dark:text-white/72">Coverage</div>
<p class="mt-3 text-sm leading-6 text-gray-600 dark:text-white/70">Doctorate, master's, specialization, undergraduate research, undergraduate thesis, and volunteers in a single trail.</p>
</div>
<div class="rounded-[1.5rem] border border-black/5 bg-stone-50 px-4 py-4 dark:border-white/10 dark:bg-white/[0.03]">
<div class="text-[0.68rem] font-semibold uppercase tracking-[0.24em] text-gray-400 dark:text-white/72">Quick reading</div>
<p class="mt-3 text-sm leading-6 text-gray-600 dark:text-white/70">Each card links to the individual profile when available, showing trajectory, publications, and linked projects.</p>
</div>
</div>
</div>
</section>

<section id="active-network" class="space-y-6">
<div class="flex items-baseline justify-between gap-4">
<h2 class="m-0 text-2xl font-black tracking-tight text-gray-950 dark:text-white md:text-3xl">Active network</h2>
<span class="text-[0.68rem] font-semibold uppercase tracking-[0.24em] text-gray-400 dark:text-white/72">Work in progress</span>
</div>
<p class="max-w-3xl text-base leading-7 text-gray-600 dark:text-white/72">Advisees with training in progress, organized by academic stage.</p>
{{< filterPeople caput="### Doctorate" categories="phd_candidate" tags="" notags="inactive" sort="alpha" grid="true">}}
{{< filterPeople caput="### Master's" categories="master_student" tags="" notags="inactive" sort="alpha" grid="true">}}
{{< filterPeople caput="### Specialization" categories="specialization" tags="" notags="inactive" sort="alpha" grid="true">}}
{{< filterPeople caput="### Undergraduate research" categories="scientific_initiation" tags="" notags="inactive" sort="alpha" grid="true">}}
{{< filterPeople caput="### Undergraduate thesis" categories="tcc" tags="" notags="inactive" sort="alpha" grid="true">}}
{{< filterPeople caput="### Volunteers" categories="volunteer" tags="" notags="inactive" sort="alpha" grid="true">}}
</section>

<div id="formers-section"></div>

<section id="previous-collaborators" x-data="{ showPrevious: false }" class="overflow-hidden rounded-[2rem] border border-black/5 bg-white/80 shadow-[0_20px_70px_rgba(15,23,42,0.08)] backdrop-blur dark:border-white/10 dark:bg-white/[0.04]">
<button type="button" @click="showPrevious = !showPrevious" class="flex w-full items-center justify-between gap-6 px-6 py-6 text-left transition-colors hover:bg-black/[0.02] dark:hover:bg-white/[0.02] md:px-8 md:py-7">
<div>
<span class="text-[0.68rem] font-semibold uppercase tracking-[0.24em] text-gray-400 dark:text-white/72">Group memory</span>
<h2 id="former-collaborators-title" class="mt-3 text-3xl font-black tracking-tight text-gray-950 dark:text-white md:text-4xl">Alumni</h2>
</div>
<svg :class="{'rotate-180': showPrevious, 'rotate-0': !showPrevious}" class="h-6 w-6 shrink-0 transform text-primary-600 transition-transform duration-200 dark:text-primary-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
</button>
<div x-show="showPrevious" x-cloak class="space-y-6 border-t border-black/5 px-6 py-6 dark:border-white/10 md:px-8 md:py-8">
<p class="m-0 max-w-3xl text-base leading-7 text-gray-600 dark:text-white/72">Completed advisings, former members, and contributions that helped build the CEDIS trajectory. The history remains available as academic and institutional memory.</p>
{{< publications caput="#### Doctorate" year="" types="phd" advisors="" notypes="" tags="" notags="sergio_freitas" sort="year_alpha" grid="true" >}}
{{< publications caput="#### Master's" year="" types="dissertation" advisors="" notypes="" tags="" notags="sergio_freitas" sort="year_alpha" grid="true" >}}
{{< publications caput="#### Specialization" year="" types="specialization" advisors="" notypes="" tags="" notags="" sort="year_alpha" grid="true" >}}
{{< filterPeople caput="#### Undergraduate research" categories="scientific_initiation" advisors="" tags="inactive" notags="" sort="year_alpha" grid="true" >}}
{{< publications caput="#### Undergraduate thesis" year="" types="tcc" advisors="" notypes="" tags="" notags="" sort="year_alpha" grid="true" >}}
{{< publications caput="#### Volunteers" year="" types="volunteer" advisors="" notypes="" tags="" notags="" sort="year_alpha" grid="true" >}}
{{< backToTopBtn target="top" >}}
</div>
</section>

<section id="cited-authors" x-data="{ showCited: false }" class="overflow-hidden rounded-[2rem] border border-dashed border-primary-200 bg-primary-50/30 p-6 dark:border-primary-400/25 dark:bg-primary-500/5 md:p-8">
<button type="button" @click="showCited = !showCited" class="flex w-full items-start gap-3 text-left transition-colors hover:bg-primary-50/30 dark:hover:bg-primary-500/5">
<span class="mt-1 inline-flex h-8 w-8 items-center justify-center rounded-full bg-primary-100 text-primary-700 dark:bg-primary-500/20 dark:text-primary-200">✨</span>
<div class="flex-1">
<h2 class="m-0 text-xl font-black tracking-tight text-gray-950 dark:text-white md:text-2xl">External authors in CEDIS outputs</h2>
<p class="mt-3 max-w-3xl text-sm leading-6 text-gray-600 dark:text-white/72">External researchers and professionals who appear as authors in CEDIS papers, chapters and technical works. Each name links to the list of outputs where the person appears.</p>
</div>
<svg :class="{'rotate-180': showCited, 'rotate-0': !showCited}" class="mt-2 h-5 w-5 shrink-0 transform text-primary-600 transition-transform duration-200 dark:text-primary-300" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
</button>
<div x-show="showCited" x-cloak class="mt-6 border-t border-primary-200/50 pt-6 dark:border-primary-400/25">
{{< derivedPeople >}}
<p class="mt-4 text-xs italic text-gray-500 dark:text-white/60">Want to update your information or complement this list? <a href="/join/" class="text-primary-600 hover:underline dark:text-primary-200">Contact CEDIS</a>.</p>
</div>
</section>

</div>
{{< backToTopBtn target="formers-section" >}}
