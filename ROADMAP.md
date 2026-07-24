# Roadmap UX & Engajamento — CEDIS/UnB

**Documento vivo para acompanhamento das ações estratégicas de conteúdo, UX e comunicação.**

- **Criado em:** 2026-07-17
- **Origem:** Relatório analítico pós-ciclo intensivo de a11y, SEO técnico, i18n e refactor visual
- **Como usar:** marque `[x]` nos itens concluídos, adicione bloco `> Nota (data): …` embaixo do item para registro. Cada Sprint deve ter revisão ao final.

> Nota (2026-07-24): o backlog técnico de automação do modelo de dados
> fica centralizado em `PLANO-AUDITORIA-2026.md`, seção "Atualização de
> modelo de dados". Este roadmap mantém os eixos de UX, conteúdo e
> engajamento para evitar duas listas técnicas divergentes.

---

## Sumário executivo

Após o ciclo de correções técnicas de 2026-07, o site do CEDIS está com base **acima da média** para centros de pesquisa universitária brasileiros:

- WCAG AA parcial atingido (contraste, skip-link, aria-expanded, alt text, iframe titles)
- SEO técnico completo (JSON-LD Person + ScholarlyArticle, hreflang, sitemap tunado, meta bilíngue)
- Pagefind com traduções PT e dicas de sintaxe
- 261 PT / 250 EN páginas, switcher explícito, URLs paralelas
- 311 publicações estruturadas + BibTeX export

**Lacuna estrutural remanescente:** o site é hoje um **catálogo bem organizado**, não uma **narrativa de descoberta**. Público não-especialista chega, vê nomes de professores e listas de artigos, e sai. Este roadmap fecha essa lacuna.

---

## Mapa de audiências

| # | Persona | Volume estimado | Pergunta central |
|---|---------|-----------------|------------------|
| 1 | Aspirante a mestrado/doutorado | 40–50% | "Devo me candidatar? A quem?" |
| 2 | Undergrad procurando IC/TCC | 15–20% | "Como entro num projeto?" |
| 3 | Pesquisador de outra instituição | 10–15% | "Quem trabalha com X? Vale colaborar?" |
| 4 | Parceiro industrial/agência | 5–10% | "Vocês entregam? Qual o histórico?" |
| 5 | Financiador (CAPES/CNPq/MCTI) | 5% | "Onde foi o dinheiro?" |
| 6 | Jornalista/comunicador | 3–5% | "Qual é a novidade?" |
| 7 | Ex-aluno | 5–10% | "O que rolou desde que saí?" |
| 8 | Internacional (EN) | 5% | "É um lab sério pra intercâmbio?" |

---

## Os 4 gatilhos de retenção

1. **Sinais de vitalidade** — datas recentes, próximo evento, banner de atualização
2. **Rosto humano** — pitch pessoal, fotos casuais do lab, orientandos como cards
3. **Concreto > abstrato** — produto em destaque, métricas agregadas, exemplos tangíveis
4. **Próximo passo óbvio** — CTA em cada perfil, caminho de candidatura passo-a-passo

---

## Roadmap tático — por eixo

### Eixo A — Storytelling e conteúdo editorial
> Ativa personas: 1, 2, 6, 8

- [x] **A1** — Página "História em números" com métricas agregadas automáticas (12 anos, N publicações, N orientações, N produtos). Renderizar a partir dos `data/*.yaml`.
  > Nota (2026-07-17): bloco "CEDIS em números" adicionado no topo de `layouts/_default/history.html`, puxando anos (desde 2013), pesquisadores ativos, publicações (`hugo.Data.productions.items`), produtos e orientações (`hugo.Data.people.people`). Reusa i18n `ui_impact_*` e o mesmo cálculo da home.

- [ ] **A2** — Série "Histórias do CEDIS" — 5–8 posts contando origem de cada produto/projeto marcante (Contextus, Alvorecer, DFCris) com fotos, tensões, decisões, resultado. Formato: 800–1200 palavras + 3–5 imagens.
  <!-- > Nota: -->

- [ ] **A3** — "Um dia no lab" — post-vídeo mensal mostrando rotina de um pesquisador ou orientando. Baixa produção, alta autenticidade.
  <!-- > Nota: -->

- [x] **A4** — "Onde estão nossos ex-alunos" — página com 15–20 cards de alumni: onde trabalham hoje, o que fazem, breve depoimento.
  > Nota (2026-07-17): página `/alumni/` (PT) e `/alumni/` (EN) criada com layout `alumni.html` e schema completo de frontmatter (name, program, year_end, advisor, current_role, current_org, location, linkedin, story, tags). Estado inicial vazio com CTA "Quero aparecer" chamando o formulário de contato. Basta o Sergio popular a lista `alumni:` no frontmatter conforme coleta os depoimentos.

- [x] **A5** — Reescrever `about.md` (ou seção equivalente) com voz humana. Substituir "Somos um centro que promove excelência…" por "Desde 2013 estudamos como o software é feito, como as pessoas o fazem, e como ensinar isso melhor. Somos 7 professores, ~40 orientandos e 12 anos de história".
  > Nota (2026-07-17): `hugo.yaml` params `p1.content` (PT e EN) já reescritos com a voz humana ("Desde 2013 estudamos como o software é feito — e como as pessoas o fazem. Somos 7 pesquisadores, dezenas de orientandos..."). Renderiza em `layouts/index.html` na seção mission. Não existe `about.md` isolado — conteúdo vive nos params do site.


### Eixo B — Prova social e sinais de confiança
> Ativa personas: 3, 4, 5

- [x] **B1** — Página de parceiros com **histórias**, não só logos. "Com o MCTI construímos o sistema X que hoje atende Y".
  > Nota (2026-07-17): `content/parceiros.pt.md` e `.en.md` reescritos com schema `partners:` estruturado (name, full_name, logo, since, story, outcomes, url). Layout `partners.html` renderiza cards com logo + 2-3 frases de história + bullets de resultados concretos. 6 parceiros: IBICT, A3M, FAP-DF, Finatec, Canal Ciência, VISTA Lab. Também corrigido erro no texto antigo que dizia "Centro de Estudos em Direito e Sociedade". EN publicada em `/partners/`.

- [ ] **B2** — Depoimentos em vídeo (30–60s) de 3–5 parceiros externos, alumni ou orientandos.
  <!-- > Nota: -->

- [x] **B3** — "Reconhecimentos" — página agregando prêmios recebidos, menções honrosas, editais aprovados (hoje dispersos nos perfis).
  > Nota (2026-07-17): página `/reconhecimentos/` (PT) e `/recognitions/` (EN) com layout `awards.html`. Schema por item (year, title, kind, recipients, detail, linked_project). 5 tipos suportados via i18n: conference_award, grant, milestone, media_mention, thesis_award. Ordena por ano decrescente e agrupa. Sidebar com nav "Ir para o ano". 4 marcos iniciais registrados (ICCSA 2024, SpB 2020, renomeação 2019); expansível.

- [x] **B4** — Números de impacto visíveis na home: "311 publicações • 8 produtos registrados • 12 anos de história". Contadores animados, atualizados via `data/`.
  > Nota (2026-07-17): seção "CEDIS em números" ativa em `layouts/index.html:126-183` com 5 cards (anos, pesquisadores, publicações, produtos, orientações) atualizados via `hugo.Data.productions.items`, `hugo.Data.people.people` e contagem de páginas. Contadores estáticos (não animados) — animação pode ser upgrade futuro.

- [ ] **B5** — Página de menções públicas, entrevistas acadêmicas, participação em eventos e circulação institucional.
  <!-- > Nota: -->


### Eixo C — Descoberta e SEO editorial
> Ativa personas: 3, 6, 8

- [ ] **C1** — Longform pillar pages por área de atuação — 2000–3000 palavras cada, cobrindo estado da arte + o que o CEDIS faz. Rankeia em Google Scholar e queries orgânicas.
  <!-- > Nota: -->

- [ ] **C2** — Blog técnico regular — 1 post curto/quinzena por algum membro. Cria trilha de conteúdo, sinaliza atividade.
  <!-- > Nota: -->

- [ ] **C3** — Meta description única por página (140–160 chars). Hoje muitas herdam a global.
  <!-- > Nota: -->

- [ ] **C4** — Open Graph images customizadas por perfil/projeto — gerar dinamicamente com título + foto.
  <!-- > Nota: -->

- [x] **C5** — hreflang `pt-BR` implementado. Verificar Google Search Console para indexação correta pós-mudança.
  > Nota (2026-07-17): tag implementada no ciclo técnico. GSC ainda não conferido.


### Eixo D — Interatividade e curiosidade
> Ativa personas: 1, 2

- [x] **D1** — Mapa visual das áreas de atuação — grafo ou mapa em D3.js ligando áreas, pesquisadores e projetos. Alto engagement.
  > Nota (2026-07-17; atualizado em 2026-07-24): página nova `/mapa/` (PT) e `/map/` (EN) com grafo force-directed em D3.js v7 (CDN). Nodes coloridos por tipo (áreas azul, pesquisadores vermelho, projetos verde), com drag + zoom + click-para-abrir. Filtro Alpine.js por tipo. Sidebar mostra contagem e detalhes do nó selecionado. Dados JSON gerados a partir de `area-list`, `content/people/*.md`/`people-index` e `project-list`. Adicionado no menu About/CEDIS entre "História" e "Oportunidades".

- [x] **D2** — Timeline interativa da história — anos como pontos clicáveis, cada um expandindo em conquistas do ano. Substituir Markdown atual.
  > Nota (2026-07-17): `layouts/_default/history.html` reescrito com Alpine.js. Botões de ano pinçam/focam o card correspondente e aplicam scroll suave. Cada card colapsa/expande independente (por padrão só o mais recente aberto). Botões "Expandir tudo" / "Recolher tudo". Marcador do dot muda de intensidade quando o card está aberto. i18n `ui_timeline_*` novos.

- [ ] **D3** — Quiz "Qual área do CEDIS combina comigo?" — 5–6 perguntas para aspirantes descobrirem qual grupo/orientador se alinha.
  <!-- > Nota: -->

- [x] **D4** — Gráfico de "temas em alta" — nuvem de tags dimensionada por frequência nas publicações recentes.
  > Nota (2026-07-17): seção "Temas em alta" na home (`layouts/index.html`), logo após "CEDIS em números". Agrega tags de `data/productions.yaml` dos últimos 4 anos (2023-2026), exclui pesquisadores e marcas active/inactive. Top 20 renderizadas como cloud com font-size proporcional (0.85rem–2.45rem) e opacidade proporcional à frequência. Cada tag linka para `/tags/{tag}/`. i18n `ui_trending_*` novos.

- [x] **D5** — Filtro nas publicações por área/ano/tipo com sliders (Alpine.js). Hoje é lista rolante.
  > Nota (2026-07-17): filtro no topo da página `/publications/` em `layouts/_default/publications.html` com 3 selects (Ano, Tipo, Tema). Alpine.js aplica `x-show` em cada `<li>` do shortcode (data-attrs `data-pub-year/type/topics`) e esconde `<h2>` de ano sem itens visíveis. Contador "total → filtrado" e botão Limpar. Sem sliders (selects mais eficientes com o volume de dados). i18n `ui_filter_*` e `pub_type_*` novos.


### Eixo E — Conversão
> Ativa personas: 1, 2, 4

- [x] **E1** — CTA final em cada perfil de pesquisador — bloco padronizado no fim: "Interesse em orientação? [Ver processo] [Enviar email]".
  > Nota (2026-07-17): bloco CTA "Interessado(a) em orientação ou colaboração?" adicionado ao fim de `layouts/people/single.html` (só quando `$isResearcher`). Três botões: Ver oportunidades (`/oportunidades/`), Enviar email (mailto com subject preenchido), Falar com o CEDIS (`/contact/`). i18n `people_cta_*` novos em pt/en.

- [ ] **E2** — Formulário de contato multi-caminho — escolher tipo (orientação, parceria, divulgação científica, extensão), formulário adapta campos e destinatário.
  <!-- > Nota: -->

- [x] **E3** — Página `/junte-se/` (Join us) — landing para todas as portas de entrada (IC, TCC, Mestrado, Doutorado, Extensão, Voluntário). Cada rota com passos claros e datas.
  > Nota (2026-07-17): página `/junte-se/` (PT) e `/join/` (EN) com layout `join.html`. 6 trilhas (IC, TCC-ES, Mestrado PPCA, Doutorado PPCA, Extensão, Voluntário CEDIS), cada uma com audience, duration, 3-4 steps numerados e CTAs primário/secundário. Card "Não sabe por onde começar" no rodapé chama /contact/. i18n `ui_join_*` completo. Adicionada ao menu People/Equipe entre Colaboradores e Alumni.

- [x] **E4** — Botões "Copiar email" e "Ver Lattes" nos perfis, além do link visual.
  > Nota (2026-07-17): card "Contato" no sidebar do perfil (`layouts/people/single.html`) exibe email + botão Copiar (Alpine.js `navigator.clipboard`), link Lattes e link ORCID. Desde 2026-07-24 os dados vêm de `partial "people-lookup"` lendo o frontmatter em `content/people/*.md`; `data/advisors.yaml` foi removido.

- [ ] **E5** — Cronograma anual visível — próximas datas: PPCA, eventos, palestras. Formato compacto na home.
  <!-- > Nota: -->


### Eixo F — Retenção e comunidade
> Ativa personas: 1, 3, 7

- [ ] **F1** — Newsletter mensal com resumo (novos produtos, publicações, editais). Substack ou Buttondown, signup na home.
  <!-- > Nota: -->

- [x] **F2** — Feed RSS por seção. Divulgar publicamente (badge "assine o feed").
  > Nota (2026-07-17): RSS agora visível como ícone no rodapé, apontando pra `/categories/news/index.xml`. Divulgação editorial ainda pendente.

- [ ] **F3** — Página de alumni ativa — permite ex-alunos atualizarem cadastro. Cria rede.
  <!-- > Nota: -->

- [ ] **F4** — Espaço de fórum/discussão — Discourse ou GitHub Discussions vinculado. Aumenta permanência mas requer moderação.
  <!-- > Nota: -->

- [ ] **F5** — Podcast institucional — já existe Spotify no rodapé. Amplificar produção com cadência mensal e cross-link em perfis.
  <!-- > Nota: -->

---

## Instrumentação — o que medir

Recomendação de tracking mínimo:

- [ ] Substituir/complementar GA4 por **Plausible** ou **Umami** (leve, privacy-friendly, sem cookie banner)
- [ ] Eventos custom:
  - [ ] `contact_form_start` / `contact_form_submit`
  - [ ] `bibtex_copy` (botão já implementado, falta instrumentar)
  - [ ] `search_query` (informa gaps de conteúdo)
  - [ ] `pdf_download` / `outbound_link_click`
  - [ ] `scroll_depth_50/75/100` em perfis e projetos

### KPIs sugeridos — baseline 2026-07, revisão trimestral

| Métrica | Baseline | Meta 6 meses | Fonte |
|---------|----------|--------------|-------|
| Visitas mensais (únicos) | _a preencher_ | +40% | Analytics |
| Taxa conversão contato | ~0.8% (estim.) | 2% | Eventos custom |
| Dwell time em perfis | _a medir_ | +30s → +90s | Plausible |
| Assinantes newsletter | 0 | 250 | Provedor direto |
| Downloads BibTeX | 0 | Baseline em 90d | Evento custom |
| Bounce rate na home | _a medir_ | −10% | Analytics |

---

## Cadência editorial recomendada

| Frequência | Ativo | Responsável sugerido |
|------------|-------|---------------------|
| Semanal | 1 post curto no LinkedIn/X linkando conteúdo do site | Comunicação/estagiário |
| Quinzenal | 1 news no site (produto, prêmio, publicação, aula aberta) | Rotativo entre pesquisadores |
| Mensal | Newsletter compilando as 2–4 news do mês + destaque de alumni | Comunicação |
| Mensal | 1 vídeo curto (30–90s) "no lab" | Orientandos em rotação |
| Semestral | 1 pillar page ou reescrita de área | Coordenador da área |
| Anual | "Retrospectiva CEDIS" (post + dados agregados) | Coordenação geral |

---

## Sequenciamento — 90 dias

### Sprint 1 (mês 1) — Quick wins de storytelling
Meta: reforçar percepção de vitalidade + rosto humano com esforço baixo.
- [x] A5 — reescrever about com voz humana
- [x] B4 — números de impacto na home
- [x] E1 — CTA final nos perfis
- [x] E4 — botões copiar email + Lattes
- [x] A1 — página "história em números"

### Sprint 2 (mês 2) — Conversão e prova social
Meta: transformar visitas em contatos e reforçar credibilidade.
- [x] E3 — página /junte-se/
- [x] B1 — parceiros com histórias
- [x] B3 — página de reconhecimentos
- [x] A4 — alumni (estrutura pronta, coleta inicial pendente)

### Sprint 3 (mês 3) — Descoberta e retenção
Meta: criar rotina editorial e amplificar alcance.
- [ ] F1 — newsletter setup + primeira edição
- [ ] C2 — blog cadência (primeiro post)
- [ ] D5 — filtro nas publicações
- [ ] C3 — meta descriptions únicas

### Backlog — trimestre 2
- ~~D1 — mapa visual das áreas~~ ✓ adiantado em 2026-07-17 (D3.js force graph em `/mapa/`)
- D3 — quiz "qual área combina" (projeto de TCC)
- B2 — vídeos de depoimento (projeto de extensão)
- C1 — pillar pages por área

---

## Voz e identidade — princípios editoriais

O que diferencia sites de centros de pesquisa memoráveis dos genéricos é **voz**. Adotar:

- **Direto:** "Estudamos como o software é feito. Faz 12 anos."
- **Curioso:** "Como uma equipe de programadores decide entre duas arquiteturas? Nosso projeto Contextus tenta responder."
- **Humano:** "O que aprendi orientando 8 mestrados sobre engenharia verde." (post em 1ª pessoa)

Evitar:
- ❌ "Prezado visitante, temos o prazer de recebê-lo…"
- ❌ "Somos um centro que promove excelência…"
- ❌ "Nossa missão é fomentar…"

---

## Log de revisões

| Data | Revisor | Mudança |
|------|---------|---------|
| 2026-07-17 | Sergio Freitas + assistente | Criação inicial pós-ciclo técnico. Marcados C5 e F2 como concluídos (implementados no ciclo). |
| 2026-07-17 | Sergio Freitas + assistente | Sprint 1 concluído: A1 (métricas na página de história), A5 (voz humana no p1), B4 (números na home), E1 (CTA final nos perfis de pesquisador), E4 (card contato com Copiar email + Lattes + ORCID). Link "Cursos e treinamentos" atualizado para `https://slides.cedis.tec.br/programas-de-formacao`. Novos i18n `people_cta_*`, `people_lattes`, `ui_copy_email*` em pt/en. |
| 2026-07-17 | Sergio Freitas + assistente | Eixo D em massa: D5 (filtro Alpine.js em /publications/), D2 (timeline interativa com colapso por ano), D4 (nuvem "Temas em alta" na home, top 20 tags dos últimos 4 anos), D1 (grafo D3.js em nova página /mapa/ conectando áreas ↔ pesquisadores ↔ projetos, com drag/zoom/filter/sidebar). Menu de navegação ganha "Mapa de conhecimento" sob About/CEDIS. |
| 2026-07-17 | Sergio Freitas + assistente | Sprint 2 concluído: E3 (`/junte-se/` com 6 trilhas), B1 (parceiros com histórias — 6 parceiros com outcomes concretos e correção do texto genérico anterior), B3 (`/reconhecimentos/` com 4 marcos e schema expansível), A4 (`/alumni/` com layout pronto e estado vazio + CTA "Quero aparecer"). Menu ganha Junte-se e Alumni em People/Equipe e Parceiros/Reconhecimentos em About/CEDIS. |
| 2026-07-17 | Sergio Freitas + assistente | Reorganização do menu About (Opção A após análise): reduzido de 8 para 4 itens (Áreas, História, Parceiros e reconhecimentos, Infra). Oportunidades promovido a top-level (`Saiba mais > Pessoas > Projetos > Oportunidades > Produções`). Reconhecimentos consolidado como seção final da página de Parceiros (schema `awards:` unificado em `content/parceiros.pt.md`), com alias `/reconhecimentos/ → /parceiros/`. Intranet movido para o rodapé. Mapa saiu do menu e ganhou banner CTA em `/categories/knowledge_areas/`. Arquivos `content/reconhecimentos.*.md` e `layouts/_default/awards.html` deletados. |
| 2026-07-24 | Sergio Freitas + assistente | Refactor do modelo de dados: `data/advisors.yaml` removido; contato/áreas de docentes vivem no frontmatter de `content/people/*.md`; `people-index`/`people-lookup` viram fonte unificada para pessoas; `translated-label.html` resolve labels via i18n → projetos → áreas → pessoas → humanize; publicações passam a usar `people[]` para slugs de pessoas e `tags[]` para temas/projetos. |
| 2026-07-24 | Sergio Freitas + assistente | Backlog #1 do PLANO-AUDITORIA fechado: `scripts/validate_content.py::validate_product_pages` ganhou validação forte de produtos — resolve `secondary_projects[]` e `publications[]` contra IDs gerados por `build_publications.py`, flagra redundância entre `project` e `secondary_projects` (error), garante `id` único por idioma. CI já invoca; 0 erros/0 warnings no estado atual. |

<!-- Modelo de nova entrada:
| YYYY-MM-DD | Nome | Descrição breve da mudança |
-->
