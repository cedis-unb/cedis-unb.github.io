<div x-data="searchComponent()" class="max-w-xl mx-auto my-10">
  <div class="mb-4">
    <input x-model="searchQuery" type="search" placeholder="Search..."
           class="w-full px-4 py-2 border rounded-md shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50">
  </div>
  <div class="space-y-4">
    <template x-for="item in filteredList" :key="item.id">
      <div class="p-4 border rounded-md shadow-sm">
        <h2 class="text-lg font-semibold" x-text="item.title"></h2>
        <p x-text="item.content.substring(0, 150) + '...'"></p>
        <a :href="item.url" class="text-blue-500 hover:text-blue-700">Read more &rarr;</a>
      </div>
    </template>
    <div x-show="filteredList.length === 0" class="text-gray-500">
      <p x-show="searchQuery" class="text-center">No results found.</p>
      <p x-show="!searchQuery" class="text-center">Please enter a search term to begin.</p>
    </div>
  </div>
</div>

<script>
  function searchComponent() {
    return {
      searchQuery: '',
      index: null,
      rawData: [],
      init() {
        fetch('/index.json')
          .then((response) => response.json())
          .then((data) => {
            this.rawData = data.data;
            this.index = new FlexSearch.Index();
            this.rawData.forEach((doc, id) => {
              this.index.add(id, doc.content);
            });
          });
      },
      get filteredList() {
        if (!this.searchQuery) return [];
        const searchResults = this.index.search(this.searchQuery);
        return this.rawData.filter(doc => searchResults.includes(doc.id));
      }
    }
  }
</script>