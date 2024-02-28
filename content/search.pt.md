---
author: CEDIS
language: pt
---

<link href="/pagefind/pagefind-ui.css" rel="stylesheet">
<script src="/pagefind/pagefind-ui.js" type="text/javascript"></script>
<div x-data="searchComponent()" x-init="initPagefindUI" class="mt-8">
    <div id="search"></div>
</div>

<script>
function searchComponent() {
    return {
        initPagefindUI() {
            // Inicializa a UI do Pagefind assim que o componente é montado
            new PagefindUI({
                element: "#search",
                showImages: false
            });
        }
    }
}
</script>
