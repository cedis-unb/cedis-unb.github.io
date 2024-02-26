<div>
  <input type="text" id="searchInput" placeholder="Digitex para pesquisar..." onkeyup="search()">
  <ul id="searchResults"></ul>
</div>

<script>
let index = new FlexSearch.Index();
let pagesData = []; // Armazena os dados das páginas

// Carrega os dados e cria o índice de busca
fetch('/index.json')
  .then(response => response.json())
  .then(data => {
    pagesData = data.pages; // Salva os dados das páginas
    data.pages.forEach((page, id) => {
      index.add(id, page.title + " " + page.content); // Indexa título e conteúdo
    });
  });

function search() {
  const input = document.getElementById('searchInput');
  const filter = input.value;
  const results = index.search(filter, { limit: 10 }); // Limita os resultados a 10
  const ul = document.getElementById("searchResults");
  ul.innerHTML = ''; // Limpa os resultados anteriores

  results.forEach(id => {
    const page = pagesData[id]; // Acessa os dados da página diretamente
    if (page) { // Verifica se a página existe
      const li = document.createElement("li");
      li.innerHTML = `<a href="${page.url}">${page.title}</a>`;
      ul.appendChild(li);
    }
  });
}
</script>
