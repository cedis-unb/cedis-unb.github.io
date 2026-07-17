---
title: "Search the site"
description: "Search across all CEDIS content — researchers, projects, publications, and news."
author: CEDIS
language: en
layout: institutional
authorimage: ../assets/images/global/author.webp
eyebrow: "Discovery tool"
---

<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<script src="/pagefind/pagefind-ui.js" type="text/javascript"></script>

<div class="rounded-[1.5rem] border border-black/5 bg-white/85 p-4 shadow-[0_18px_50px_rgba(15,23,42,0.06)] backdrop-blur dark:border-white/10 dark:bg-white/[0.04] md:p-6">
    <div id="search" class="cedis-search"></div>
    <p class="mt-6 text-sm leading-6 text-gray-500 dark:text-white/60">
        Tip: quote a phrase to search for an exact match (e.g. <code class="rounded bg-stone-100 px-1.5 py-0.5 text-xs dark:bg-white/[0.06]">"software engineering"</code>) or combine multiple terms to narrow the results.
    </p>
</div>

<script>
window.addEventListener("DOMContentLoaded", () => {
    new PagefindUI({
        element: "#search",
        showImages: false,
        showEmptyFilters: false,
        excerptLength: 30,
        resetStyles: false
    });
});
</script>
