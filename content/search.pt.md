---
title: "Buscar no site"
description: "Busca em todo o conteúdo do CEDIS — pesquisadores, projetos, publicações e notícias."
author: CEDIS
language: pt
layout: institutional
authorimage: ../assets/images/global/author.webp
eyebrow: "Ferramenta de descoberta"
---

<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<script src="/pagefind/pagefind-ui.js" type="text/javascript"></script>

<div class="rounded-[1.5rem] border border-black/5 bg-white/85 p-4 shadow-[0_18px_50px_rgba(15,23,42,0.06)] backdrop-blur dark:border-white/10 dark:bg-white/[0.04] md:p-6">
    <div id="search" class="cedis-search"></div>
    <p class="mt-6 text-sm leading-6 text-gray-500 dark:text-white/60">
        Dica: use aspas para uma expressão exata (ex.: <code class="rounded bg-stone-100 px-1.5 py-0.5 text-xs dark:bg-white/[0.06]">"engenharia de software"</code>) ou combine termos para restringir o resultado.
    </p>
</div>

<script>
window.addEventListener("DOMContentLoaded", () => {
    new PagefindUI({
        element: "#search",
        showImages: false,
        showEmptyFilters: false,
        excerptLength: 30,
        resetStyles: false,
        translations: {
            placeholder: "Buscar em publicações, projetos, pessoas…",
            clear_search: "Limpar",
            load_more: "Ver mais resultados",
            search_label: "Buscar no CEDIS",
            filters_label: "Filtros",
            zero_results: "Nenhum resultado encontrado para [SEARCH_TERM].",
            many_results: "[COUNT] resultados encontrados para [SEARCH_TERM].",
            one_result: "1 resultado encontrado para [SEARCH_TERM].",
            searching: "Buscando por [SEARCH_TERM]..."
        }
    });
});
</script>
