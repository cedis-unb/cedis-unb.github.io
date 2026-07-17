# Roadmap UX & Engajamento — CEDIS/UnB

**Documento vivo para acompanhamento das ações estratégicas de conteúdo, UX e comunicação.**

- **Criado em:** 2026-07-17
- **Origem:** Relatório analítico pós-ciclo intensivo de a11y, SEO técnico, i18n e refactor visual
- **Como usar:** marque `[x]` nos itens concluídos, adicione bloco `> Nota (data): …` embaixo do item para registro. Cada Sprint deve ter revisão ao final.

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

- [ ] **A1** — Página "História em números" com métricas agregadas automáticas (12 anos, N publicações, N orientações, N produtos). Renderizar a partir dos `data/*.yaml`.
  <!-- > Nota: -->

- [ ] **A2** — Série "Histórias do CEDIS" — 5–8 posts contando origem de cada produto/projeto marcante (Contextus, Alvorecer, DFCris) com fotos, tensões, decisões, resultado. Formato: 800–1200 palavras + 3–5 imagens.
  <!-- > Nota: -->

- [ ] **A3** — "Um dia no lab" — post-vídeo mensal mostrando rotina de um pesquisador ou orientando. Baixa produção, alta autenticidade.
  <!-- > Nota: -->

- [ ] **A4** — "Onde estão nossos ex-alunos" — página com 15–20 cards de alumni: onde trabalham hoje, o que fazem, breve depoimento.
  <!-- > Nota: -->

- [ ] **A5** — Reescrever `about.md` (ou seção equivalente) com voz humana. Substituir "Somos um centro que promove excelência…" por "Desde 2013 estudamos como o software é feito, como as pessoas o fazem, e como ensinar isso melhor. Somos 7 professores, ~40 orientandos e 12 anos de história".
  <!-- > Nota: -->


### Eixo B — Prova social e sinais de confiança
> Ativa personas: 3, 4, 5

- [ ] **B1** — Página de parceiros com **histórias**, não só logos. "Com o MCTI construímos o sistema X que hoje atende Y".
  <!-- > Nota: -->

- [ ] **B2** — Depoimentos em vídeo (30–60s) de 3–5 parceiros externos, alumni ou orientandos.
  <!-- > Nota: -->

- [ ] **B3** — "Reconhecimentos" — página agregando prêmios recebidos, menções honrosas, editais aprovados (hoje dispersos nos perfis).
  <!-- > Nota: -->

- [ ] **B4** — Números de impacto visíveis na home: "311 publicações • 8 produtos registrados • 12 anos de história". Contadores animados, atualizados via `data/`.
  <!-- > Nota: -->

- [ ] **B5** — Página de "clipping" com menções na imprensa, entrevistas, participações em eventos.
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

- [ ] **D1** — Mapa visual das áreas de atuação — grafo ou mapa em D3.js ligando áreas, pesquisadores e projetos. Alto engagement.
  <!-- > Nota: -->

- [ ] **D2** — Timeline interativa da história — anos como pontos clicáveis, cada um expandindo em conquistas do ano. Substituir Markdown atual.
  <!-- > Nota: -->

- [ ] **D3** — Quiz "Qual área do CEDIS combina comigo?" — 5–6 perguntas para aspirantes descobrirem qual grupo/orientador se alinha.
  <!-- > Nota: -->

- [ ] **D4** — Gráfico de "temas em alta" — nuvem de tags dimensionada por frequência nas publicações recentes.
  <!-- > Nota: -->

- [ ] **D5** — Filtro nas publicações por área/ano/tipo com sliders (Alpine.js). Hoje é lista rolante.
  <!-- > Nota: -->


### Eixo E — Conversão
> Ativa personas: 1, 2, 4

- [ ] **E1** — CTA final em cada perfil de pesquisador — bloco padronizado no fim: "Interesse em orientação? [Ver processo] [Enviar email]".
  <!-- > Nota: -->

- [ ] **E2** — Formulário de contato multi-caminho — escolher tipo (orientação, parceria, imprensa, extensão), formulário adapta campos e destinatário.
  <!-- > Nota: -->

- [ ] **E3** — Página `/junte-se/` (Join us) — landing para todas as portas de entrada (IC, TCC, Mestrado, Doutorado, Extensão, Voluntário). Cada rota com passos claros e datas.
  <!-- > Nota: -->

- [ ] **E4** — Botões "Copiar email" e "Ver Lattes" nos perfis, além do link visual.
  <!-- > Nota: -->

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
- [ ] A5 — reescrever about com voz humana
- [ ] B4 — números de impacto na home
- [ ] E1 — CTA final nos perfis
- [ ] E4 — botões copiar email + Lattes
- [ ] A1 — página "história em números"

### Sprint 2 (mês 2) — Conversão e prova social
Meta: transformar visitas em contatos e reforçar credibilidade.
- [ ] E3 — página /junte-se/
- [ ] B1 — parceiros com histórias
- [ ] B3 — página de reconhecimentos
- [ ] A4 — alumni (coleta inicial, 5–10 nomes)

### Sprint 3 (mês 3) — Descoberta e retenção
Meta: criar rotina editorial e amplificar alcance.
- [ ] F1 — newsletter setup + primeira edição
- [ ] C2 — blog cadência (primeiro post)
- [ ] D5 — filtro nas publicações
- [ ] C3 — meta descriptions únicas

### Backlog — trimestre 2
- D1 — mapa visual das áreas (projeto de IC)
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

<!-- Modelo de nova entrada:
| YYYY-MM-DD | Nome | Descrição breve da mudança |
-->
