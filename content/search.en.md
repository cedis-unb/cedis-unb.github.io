---
author: CEDIS
language: en
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
            // Initializes the Pagefind UI as soon as the component is mounted
            new PagefindUI({
                element: "#search",
                showImages: false
            });
        }
    }
}
</script>
