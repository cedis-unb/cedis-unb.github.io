# 06 — Checklist de testes

Checklist para validar a migração Tailwind 4 em branch local antes de qualquer autorização de merge.

## Preparação

- [ ] Baseline capturada (Fase 1 do plano): `tmp/baseline/` com pa11y JSON, lhci, screenshots, sizes.txt
- [ ] Branch `dev/tailwind-v4-vite-local` criada sem upstream
- [ ] Tag `pre-tailwind-v4-YYYYMMDD` criada
- [ ] Backup local do `docs/` (opcional, útil para diff visual)

## Testes de páginas (funcionamento visual e interativo)

### PT/EN — cada rota testada nos dois idiomas

- [ ] `/` (Home)
- [ ] `/pt/`
- [ ] `/en/`
- [ ] Sobre (`/about/` e `/pt/history/`)
- [ ] Áreas — lista (`/pt/areas/`, `/en/areas/`)
- [ ] Área detalhe (`/pt/areas/hpc/`, `/en/areas/hpc/`)
- [ ] Projetos — lista (`/pt/projects/`, `/en/projects/`)
- [ ] Projeto detalhe (ex.: `/pt/projects/framework_preditivo_engajamento/`)
- [ ] Produtos — lista (`/pt/products/`, `/en/products/`)
- [ ] Produto detalhe (ex.: `/pt/products/edutrack/`)
- [ ] Pessoas — lista (`/pt/people/`, `/en/people/`)
- [ ] Perfil pesquisador (ex.: `/pt/people/sergio_freitas/`)
- [ ] Perfil derivado (ex.: `/pt/people/all/`)
- [ ] Publicações (`/pt/publications/scientific/`)
- [ ] Publicação individual
- [ ] Notícias (`/pt/categories/news/`)
- [ ] Oportunidades (`/pt/oportunidades/`)
- [ ] Junte-se (`/pt/participe/` ou equivalente)
- [ ] Mapa (`/pt/mapa/`)
- [ ] 404 (`/xyz/`)

### Comparação CSS PT vs EN (NOVO — motivo: hugo_stats.json cobertura)

- [ ] Rodar build; comparar `docs/pt/**/*.html` × `docs/en/**/*.html` para confirmar mesmo CSS servido.
- [ ] Confirmar que nenhum template usa classes condicionadas por idioma via `{{ if eq $lang "pt" }}class="..."{{ else }}class="..."{{ end }}` que possa gerar classe só em um idioma.
- [ ] Grep: `grep -rn 'if eq .*Lang\|if eq .*Site.Language' layouts/ | grep -i class` — se >0 ocorrências, revisar caso a caso.

### Navegação e interação

- [ ] Menu desktop — expande e recolhe sub-menus (`x-data` em `nav.html`)
- [ ] Menu móvel (hamburger) — abre/fecha
- [ ] Seletor de idioma — troca PT ↔ EN preservando rota atual
- [ ] Toggle modo claro/escuro — persiste em localStorage
- [ ] Busca (Pagefind) — abre modal, aceita entrada, exibe resultados, links funcionam
- [ ] Accordion de perfil (5 seções: current-supervisions, previous-collaborators, npublications, researcher-projects, researcher-products) — abre/fecha com clique no h2
- [ ] Filtros de mapa (`_default/map.html`) — botões all/area/researcher/project/umbrella alternam
- [ ] Quiz (`_default/quiz.html`) — clique em resposta destaca; navegação de perguntas
- [ ] History expand/collapse all (`_default/history.html`)
- [ ] Volta ao topo (`backToTopBtn` shortcode)
- [ ] Copy email button no perfil — clipboard funciona

### Componentes visuais

- [ ] Cards de projeto (`.profile-project-card` — extensivo em `/people/`)
- [ ] Cards de destaque (`.researcher-highlights`)
- [ ] Cards de publicação (`.featured-publications`)
- [ ] Cards de contadores (VISÃO RÁPIDA na sidebar)
- [ ] Cards de área na home
- [ ] Chips/tags (área, tema, projeto)
- [ ] Badges com contagem (números em pílulas)
- [ ] Botões (rounded-full em vários lugares)
- [ ] Formulários (busca, contato se houver)
- [ ] Tabelas (raras, mas em `history.html`, publications)
- [ ] Blocos de código Markdown (com prism ou syntax highlight)
- [ ] Imagens (WebP servido via Hugo Pipes; verificar lazy loading)
- [ ] SVG decorativos (hero da home — `text-opacity-40` afetado)
- [ ] Shortcodes: `postsByCategoriesTags`, `filterPeople`, `publications`, `impact`, `imgc`

### Links

- [ ] Links internos (`/pt/...` e `/en/...`) — nenhum 404
- [ ] Links externos — abrem em nova aba com `target="_blank" rel="noopener"`
- [ ] Links de download (PDFs em `static/files/`)
- [ ] Rodapé — todos links funcionam

### Acessibilidade

- [ ] Navegação por Tab: ordem lógica, todos elementos focáveis alcançáveis
- [ ] Foco visível em todos os interativos (ring, outline)
- [ ] Contraste WCAG AA em texto e ícones (usar Chrome DevTools ou pa11y)
- [ ] Leitores de tela (VoiceOver macOS ou NVDA) leem títulos, listas, botões corretamente
- [ ] Alt em imagens (já confirmado 0 img sem alt)
- [ ] Formulários com labels associados
- [ ] Skip-links (`href="#main-content"`) funcionam

### Responsividade

- [ ] Desktop (1440x900)
- [ ] Tablet (768x1024)
- [ ] Mobile (375x812 — iPhone 13)
- [ ] Ultra-wide (2560x1440)
- [ ] Verificar breakpoint `sm md lg xl 2xl` em rotas ricas

### Compatibilidade de navegadores

- [ ] Chrome/Chromium (última versão)
- [ ] Firefox (última versão)
- [ ] Safari (macOS/iOS 17+)
- [ ] Edge (última versão)
- [ ] Safari 16.4 (limite de suporte Tailwind 4 — testar via browserstack se possível)
- [ ] Chrome 111 (limite de suporte Tailwind 4)
- [ ] Firefox 128 (limite de suporte Tailwind 4)

### Desempenho

- [ ] Lighthouse Desktop — performance ≥ 90 em 8 rotas do `lighthouserc.json`
- [ ] Lighthouse Mobile — mesmo alvo
- [ ] LCP ≤ 2500ms em cada rota
- [ ] CLS ≤ 0.1 em cada rota
- [ ] Total CSS transferido ≤ baseline (comparar antes/depois)
- [ ] Tempo de build local `hugo --minify` ≤ 15s

### SEO

- [ ] Meta tags OK em cada rota (`og:*`, `twitter:*`, canonical)
- [ ] Sitemap gerado (`docs/sitemap.xml`)
- [ ] robots.txt correto
- [ ] hreflang em cada página (PT/EN pareamento)

### Erros no console

- [ ] Nenhum erro JS
- [ ] Nenhum 404 em CSS/JS/imagens
- [ ] Nenhum warning de deprecação
- [ ] CSP (se ativo) não bloqueia scripts inline necessários

### Testes automatizados existentes

- [ ] `npm test` — 0 erros (check:publications + validate_content + validate_i18n)
- [ ] `npx pa11y-ci --config .pa11yci.json` — 0 novos erros (comparar com baseline)
- [ ] `npx lhci autorun` — thresholds atingidos
- [ ] `npx lychee --config lychee.toml` — nenhum link quebrado (rodado em CI)

### Testes específicos da 4ª alternativa (Hugo native Tailwind)

Estes só se aplicam se decidirmos adotar a 4ª alternativa. Se ficarmos com Alt 2 (v4 + PostCSS), pular.

- [ ] `hugo_stats.json` é gerado durante build (`[build.buildStats] enable = true` habilitado)
- [ ] `assets/css/main.css` contém `@source "hugo_stats.json"` explícito
- [ ] `hugo_stats.json` está no `.gitignore` (mas Hugo o processa em runtime)
- [ ] Verificar `hugo_stats.json` gerado inclui classes usadas em ambos os idiomas (grep de uma classe única a cada idioma)
- [ ] `templates.Defer` aplicado no partial que gera o `<link rel="stylesheet">` para garantir que compilação ocorra depois de todos os templates renderizados
- [ ] Ausência de arquivo `style.css` intermediário — Tailwind compila direto de `main.css`
- [ ] `resources.Fingerprint` continua funcionando após `css.TailwindCSS`
- [ ] Integrity hash presente em produção
- [ ] Hot reload de CSS em `hugo server` funciona a cada mudança em template

## Testes finais antes de decidir merge

- [ ] Rodar `git diff main...dev/tailwind-v4-vite-local` — revisar todos os arquivos alterados
- [ ] Contar linhas alteradas — deve ser proporcional às fases documentadas
- [ ] Verificar que `docs/` foi regenerado (não deve ter diff de conteúdo além de fingerprints)
- [ ] Verificar `package.json`, `package-lock.json` — só as trocas planejadas
- [ ] Verificar que `hugo.yaml` NÃO foi alterado (a menos que necessário para buildStats)

## Testes pós-merge (se autorização concedida)

- [ ] Aguardar deploy do GitHub Pages (~2min)
- [ ] Testar site produção `https://cedis.unb.br/` — 10 rotas mais visitadas
- [ ] Testar em navegador limpo (sem cache)
- [ ] Confirmar CSS carrega com integrity hash correto
- [ ] Monitorar Google Analytics por 48h para taxa de erro JS

## Critério global de aprovação

Só aprovar merge se **TODOS** os itens forem sim:

- [ ] Zero novos erros pa11y (comparar JSON)
- [ ] Lighthouse Performance ≥ baseline em todas 8 rotas
- [ ] Lighthouse Accessibility ≥ baseline
- [ ] Screenshots visuais aprovados humanamente em ≥ 10 rotas PT/EN light/dark
- [ ] `npm test` passa
- [ ] Todos testes de navegadores (Chrome, Firefox, Safari, Edge) OK
- [ ] Sem regressões em interatividade (Alpine.js funcional)
- [ ] Bundle CSS ≤ baseline (opcionalmente aceitar até +10%)
- [ ] Nenhum warning de deprecação no console
