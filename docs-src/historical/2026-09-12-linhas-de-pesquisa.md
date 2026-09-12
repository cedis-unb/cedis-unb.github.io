# Registro de decisão — camada "Linhas de pesquisa" e ajustes pós-reunião (2026-09-11/12)

Histórico de construção deste ciclo do site. Documento interno
(`docs-src/` não é publicado). Documento técnico da camada:
[`../research-lines.md`](../research-lines.md).

Participantes: Sergio Freitas (decisão e requisitos), assistente de código
(análise e implementação). Insumos externos: reunião com George Marsicano
em 2026-09-11 e duas análises escritas sobre taxonomia institucional.

---

## 1. Ponto de partida: reunião de 2026-09-11 (Sergio + George)

Pauta: usabilidade e exibição de dados do Software para o Bem (SpB).
Problemas relatados por George e diagnóstico no repositório:

| Relato | Causa encontrada | Correção (2026-09-12) |
|---|---|---|
| SpB não aparece na linha Software Social | `content/projects/software_bem.*.md` tinha só `gamification` em `areas`/`tags`; a página de área lista por tag | adicionada `social_software` (pt/en) |
| Divergência cronológica: projeto de 2025 com INPI de 2026 | produtos com `date: 2025-12-31` (provisória); textos misturavam "registrado no Lattes (2025)" com "registro INPI (2026)" | textos distinguem cadastro Lattes 2025 de INPI 2026; datas reais ficaram pendentes com George |
| "Nem todos os projetos anteriores aparecem" | só Doarti vinculado ao SpB em `projects.yaml`; LEPIC e produtos 2020–2024 não cadastrados | pendente de dados do George |
| Falta uma seção de registros INPI | `/publications/registrations/` existia mas não estava no menu nem linkada | item no menu Publicações; blocos "Registros de software (INPI)" em projeto e produto |
| Áreas mostravam "só discentes" | além do bug de tag, "Projetos em andamento" incluía encerrados | shortcode ganhou `caputKey`; áreas separam "Projetos encerrados" |
| Contagens de orientação provisórias | indicador somava toda `people.yaml` (230) | passou a somar `defesas.yaml` + orientandos ativos (188) |
| Onde publicar a chamada de extensão | oportunidades não propagavam para a capa; textos fixos "todos encerrados" | chamadas abertas entram no pulse da home; textos neutros; `archetypes/opportunities.md` |
| — | nome "Marcicano" e e-mail sem "r" na página da área | corrigidos |

Pendências que ficaram com George (planilha de orientações, banca do
Bruno, chamada de extensão, histórico dos produtos SpB, frente de SPUX e
Melhoria do Serviço Público, área Segurança no perfil) foram consolidadas
numa página privada compartilhável.

Aprendizado de ambiente: o build exige Node 24 (`mise`), porque o shell
abre com Node 20 e o Tailwind invocado pelo Hugo falha com
`bad option: --permission`.

---

## 2. A pergunta: trocar "Áreas de atuação" por "Linhas de pesquisa"?

### Análise 1 — taxonomia (resumo)

- O site tinha 15 páginas de área (20 ids em `areas.yaml`) chamadas de
  formas diferentes: "Áreas de atuação" (home), "Áreas de pesquisa" (menu e
  perfis), "Areas of Expertise" (EN), "Linhas e temas do centro" (submenu).
- Pelo CNPq, linha de pesquisa é "tema aglutinador de estudos científicos
  sustentado por tradição investigativa, do qual se originam projetos".
  Estrutura: grupo → linhas → projetos → estudos.
- As 15 áreas misturam naturezas (domínio, campo científico, abordagem,
  subárea de ES, temática transversal). Funcionam como **mapa de
  competências**, não como 15 linhas formais.
- Evidência empírica: várias áreas têm 0 projetos ativos e dezenas de
  publicações — típico de competência acumulada, não de agenda em execução.
- 7 pesquisadores para 15 linhas transmitiria fragmentação; 5–6 programas
  fortes seriam mais defensáveis.
- Avaliação das opções: converter as 15 em linhas (4/10); renomear para
  "Áreas de pesquisa" (7/10); manter "Áreas de atuação" (9/10);
  **áreas + nova camada formal de linhas (10/10)**.
- Proposta inicial de cinco linhas: Engenharia de software, arquitetura e
  qualidade · IA, linguagem e análise de dados · Tecnologias para
  aprendizagem, gamificação e fatores humanos · Transformação digital e
  sistemas sociotécnicos · Sistemas seguros, escaláveis e de alto
  desempenho. A confrontar com o DGP/CNPq.

### Análise 2 — arquitetura dual (resumo)

- A home é organizada por intenção do visitante ("quero pesquisar aqui",
  "conhecer o trabalho", "parcerias"), não por taxonomia científica: é uma
  **arquitetura de comunicação e descoberta**, e isso é uma qualidade.
- "Areas of Expertise" no EN confirma: as áreas dizem "no que o CEDIS tem
  competência", não "como organiza sua agenda científica".
- O site cobre três frentes (pesquisa, produtos, formação); organizar a
  interface por linhas seria restritivo.
- Conclusão revista: **back-end semântico sofisticado, front-end simples**.
  Linhas existem como estrutura de conhecimento; áreas continuam sendo a
  navegação. Linhas aparecem em Pesquisa (sem o protagonismo das áreas),
  como "inserção científica" nas páginas de área e no mapa. Princípio:
  *progressive disclosure*.
- Padronizar "Áreas de atuação" nos perfis e reservar "Linhas de pesquisa"
  para a nova entidade, no schema, no conteúdo e na interface.

### Decisão (Sergio, 2026-09-12)

Implementar **"Áreas de atuação + nova camada formal de linhas de
pesquisa"**, combinando "as 5 propostas como rascunho" com "só a estrutura":

1. estrutura própria (`research_lines.yaml`), seguindo o padrão do projeto;
2. id/slug estável; nome pt/en; descrição; status `draft|active|archived`;
   áreas, pesquisadores, projetos, temas; período opcional;
3. relações muitos-para-muitos;
4. **não** deduzir pesquisadores de `areas.yaml`; vínculo explícito e
   validado depois;
5. não converter áreas em linhas nem alterar a semântica de `areas.yaml`;
6. `draft` invisível em navegação, sitemap, páginas institucionais e
   descoberta; seção só aparece com ≥ 1 linha `active`;
7. páginas, partials, schema, validação, i18n e relações prontos para que
   promover uma linha não exija mudança estrutural;
8. relações inversas em área, pesquisador e projeto;
9. hierarquia Linhas → Áreas → Temas → Projetos/produção, não estritamente
   arbórea;
10. as cinco linhas apenas como rascunho inicial.

---

## 3. O que foi construído (2026-09-12)

Ver tabela de arquivos em `../research-lines.md`. Pontos de desenho que
merecem registro:

- **Stubs gerados** (`scripts/build_research_lines.py`), como
  `build_defesas.py`: o YAML é a única fonte; `draft: true` nos stubs de
  linhas não ativas usa o mecanismo nativo do Hugo para excluir do build.
  `_index` recebe `build.render/list: never` sem linha ativa.
- **Índice exclui `draft` na origem** (`research-line-index`), para que
  nenhum template consiga vazar um rascunho.
- **Menu condicional** via `params.requires` na entrada de menu e
  `{{ continue }}` em `nav.html`; a configuração fica em `hugo.yaml`, a
  decisão em tempo de build.
- **Temas com rótulo próprio** (`themes[].{id,name}`): viram chaves i18n
  (só quando ausentes, para não sobrescrever tags existentes) e ligam à
  taxonomia de tags quando a tag existe.
- **Casamento área ↔ página de área** pelo id da página **e** por tags que
  sejam ids de `areas.yaml`, porque há 20 ids e 15 páginas.
- **Mapa**: nó âmbar "line" só com linha ativa; botão, contagem e legenda
  condicionais.
- **Terminologia**: "Áreas de atuação" em menu e perfis (pt), "Areas of
  expertise" (en); submenu passa a "Competências e frentes do centro".
- Rascunho das cinco linhas: `projects[]` preenchido pelas tags dos projetos
  apenas para exercitar a renderização, com aviso no arquivo. `researchers[]`
  nasceu vazio (regra: nada deduzido de `areas.yaml`). Em 2026-09-12 Sergio
  declarou os vínculos linha a linha, com base numa tabela de evidência
  (presença nas áreas da linha, participação em projeto vinculado e
  orientações concluídas com as tags da linha) e com a regra adicional
  "quem está em projeto vinculado entra na linha". Cada vínculo ficou
  comentado no YAML com a evidência. Continua pendente o confronto com o
  DGP/CNPq antes de promover qualquer linha.

Verificação: `npm test` (schema + referências + paridade pt/en +
sincronização dos stubs), build de produção sem linhas ativas (nada muda
no site publicado) e build de teste com uma linha temporariamente ativa
para conferir página, lista, menu, blocos relacionados, home e mapa.

---

## 3a. Ajustes do mesmo dia após revisão de Sergio na pré-visualização

- **Pré-visualização de rascunhos** (`npm run start:lines-preview`): o
  gerador, com `HUGO_CEDIS_PREVIEW_LINES=1`, grava os rascunhos sem `draft`
  e marca o `_index` com `research_lines_preview: true`; `research-line-list`
  ganhou o modo `visible` (ativas em produção; ativas + rascunhos em
  preview), usado por menu, home, mapa, blocos "relacionadas" e pelo novo
  shortcode `research-lines-link` (item em Sobre › Para saber mais). Nada
  disso usa `-D` nem `.Site.BuildDrafts` (obsoleto no Hugo 0.156).
- **Vínculos pesquisador–linha** declarados por Sergio a partir da tabela de
  evidência (ver §3); regra "quem está em projeto vinculado entra na linha".
- **Regressão do modo escuro corrigida.** O botão de tema não tinha efeito
  desde a migração para Tailwind 4 (commit `af8896cc6b`, 2026-07-27): o
  `tailwind.config.js` apagado carregava `darkMode: 'class'` e o `main.css`
  novo não declarava `@custom-variant dark (&:where(.dark, .dark *))`, então
  todos os `dark:` compilavam para `@media (prefers-color-scheme: dark)` e
  só o sistema operacional controlava o tema, enquanto `overrides.css` e
  `profile.css` seguiam a classe (estados mistos). Diagnóstico feito no
  navegador (classe `dark` no `<html>` sem mudar o fundo do `body`) e no CSS
  compilado. Correção: uma linha em `main.css`; guarda de regressão
  `npm run check:css` dentro de `npm test`.

## 3b. Revisão dos nomes frente ao CNPq/CAPES e ativação (2026-09-12)

Sergio confrontou as cinco propostas com o conceito de linha do DGP/CNPq
(tema aglutinador com tradição investigativa; nem todo integrante precisa
estar em todas as linhas) e com o Documento de Área de Computação
2025–2028 da CAPES (Engenharia de Software, IA, Ciência de Dados,
Cibersegurança, sistemas computacionais e aplicações interdisciplinares
com contribuição da/para a Computação). Conclusões aplicadas:

| Antes | Depois | Motivo |
|---|---|---|
| Engenharia de software, arquitetura e qualidade | **Engenharia, evolução e qualidade de software** | subárea explícita do CNPq; agrega VV&T, Arquitetura e Linhas de Produto já registradas pelo grupo (SIGAA, 2021–atual) |
| Inteligência artificial, linguagem e análise de dados | **Inteligência artificial, processamento de linguagem e ciência de dados** | "ciência de dados" tem identidade disciplinar reconhecida pela CAPES; CEDIS integra o CenIA/UnB |
| Tecnologias para aprendizagem, gamificação e fatores humanos | (mantido) | evolui "Ciência da Aprendizagem, Serious Games e Gamificação" (SIGAA); nome deixa clara a identidade computacional |
| Transformação digital e sistemas sociotécnicos | **Sistemas sociotécnicos e transformação digital** | "impacto social" é missão transversal do centro, não objeto aglutinador de linha |
| Sistemas seguros, escaláveis e de alto desempenho | **Sistemas computacionais: segurança, desempenho e sustentabilidade** | "desempenho" é campo investigativo reconhecível; absorve software verde e sustentabilidade computacional |

Ajustes decorrentes no YAML: `history` nas linhas 1 e 3 com a evidência
institucional do SIGAA; temas novos (evolução de software, ciência de
dados, jogos sérios, ciência da aprendizagem, governo digital, processos
organizacionais, DevOps) e tema "software de impacto social" removido;
`green_software` e o projeto GSD também na linha 5, com Fabiana Mendes
pela regra de projeto vinculado; slugs atualizados (linhas ainda não
tinham URL pública).

A página da linha passou a listar **produtos derivados** (produto cujo
projeto de origem ou secundário está na linha, ou cujas tags interceptam
as chaves da linha), fechando a cadeia de evidência pesquisadores →
projetos → publicações → orientações → produtos.

**Ativação.** Na sequência, Sergio decidiu não manter o estado de
rascunho: as cinco linhas passaram a `status: active` e foram publicadas.
Pendência que fica: alinhar o registro do grupo no DGP/CNPq às cinco
linhas.

## 4. Próximos passos registrados

1. Alinhar o registro do grupo no DGP/CNPq às cinco linhas publicadas
   (nomes revisados em 2026-09-12, ver §3b).
2. Validar `researchers[]` com cada pesquisador (vínculos já declarados
   por Sergio em 2026-09-12, comentados com a evidência no YAML).
3. Revisar `projects[]` e `themes[]`; decidir `period` e `history`.
4. (Feito em 2026-09-12: as cinco linhas foram ativadas de uma vez.)
5. Avaliar, depois da primeira promoção: indicadores por linha, produtos no
   mapa, contextos/métodos como entidades.
