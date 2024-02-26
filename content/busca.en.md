---
title: "Página de Busca"
layout: "search"  # Este layout precisa ser criado em 'layouts/search.html' ou ajuste conforme necessário
description: "Use a busca para encontrar conteúdo no site."
---

<section class="search-page" x-data="searchComponent()">
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold text-center mb-4">Buscar no Site</h1>
    <input x-model="searchQuery" type="search" placeholder="Digite sua busca..." class="search-input px-4 py-2 w-full border rounded" @input.debounce.400="search()">
    <div class="search-results mt-4" x-show="results.length > 0">
      <template x-for="result in results" :key="result.id">
        <div class="result-item mb-2 p-2 border-b">
          <a :href="result.url" x-text="result.title" class="text-lg font-medium"></a>
          <p x-text="result.summary" class="text-sm"></p>
        </div>
      </template>
    </div>
    <div class="no-results" x-show="searchQuery && results.length === 0">
      <p>Nenhum resultado encontrado.</p>
    </div>
  </div>
</section>

<script>
function searchComponent() {
  return {
    searchQuery: '',
    results: [],
    init() {
      fetch('/index.json')
        .then((response) => response.json())
        .then((data) => {
          this.index = new FlexSearch.Index({
            tokenize: "forward",
            document: {
              id: "id",
              index: ["title", "content"],
            },
          });
          this.index.add(data);
        });
    },
    search() {
      if (!this.searchQuery) {
        this.results = [];
        return;
      }
      this.results = this.index.search(this.searchQuery, {
        limit: 10,
        enrich: true,
      }).map((result) => result.doc);
    },
  }
}
</script>
