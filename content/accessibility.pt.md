---
title: "Acessibilidade"
date: 2026-07-20T09:00:00-03:00
draft: false
language: pt
description: "Situação da acessibilidade digital do site do CEDIS: o nível que buscamos, o que cada build verifica automaticamente, o que foi verificado manualmente e as lacunas que já conhecemos."
featured_image: "../assets/images/pages/media-CEDIS.webp"
eyebrow: "Compromisso com WCAG"
translationKey: accessibility
layout: institutional-page
---

O CEDIS trabalha para que o conteúdo deste site seja utilizável por pessoas com diferentes
tipos de deficiência. Nosso alvo são as diretrizes da
[Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/) em nível AA,
mais os acréscimos da WCAG 2.2 aplicáveis a um site de conteúdo. **Não declaramos conformidade
plena com nenhuma versão da WCAG**: parte do site foi verificada, parte não foi, e as lacunas
que já conhecemos estão listadas abaixo.

## Recursos já implementados

- Link "pular para o conteúdo" (skip link) no topo de cada página, apontando para um destino que existe.
- Navegação por teclado com foco visível no cabeçalho, nos filtros e no mapa de competências.
- Menu principal e submenus operáveis por teclado: abrem com Enter, informam o estado por `aria-expanded`, e Esc fecha devolvendo o foco ao botão que abriu.
- Mapa de competências com alternativa acessível por teclado: cada nó recebe foco e é ativável com Enter ou Espaço, e as mesmas relações são publicadas como uma lista de links comuns, que funciona com o JavaScript desligado.
- Rótulos ARIA em componentes interativos (menus, filtros, mapa, botão de tema).
- Alternativa textual (`alt`) em imagens de conteúdo.
- Estrutura semântica com hierarquia adequada de títulos.
- Suporte a redução de movimento (`prefers-reduced-motion`), respeitado pela animação do mapa.

## Verificado automaticamente em cada build

Cada push executa estas verificações no CI, e a falha bloqueia o build:

- **Pa11y** (HTML_CodeSniffer, padrão `WCAG2AA`) sobre **21 URLs fixas**, nos dois idiomas. É uma amostra, não o site inteiro — o site gera mais de três mil páginas.
- **Lighthouse CI em desktop** sobre **8 URLs**, exigindo da categoria de acessibilidade nota **mínima de 0,90** (não 100). A execução mobile usa o mesmo limite, mas é um comando local, não faz parte do CI.
- **Contraste em modo escuro** com axe-core sobre **8 arquétipos** (uma página por família de layout). Existe porque o Pa11y roda só no tema claro, e sem esta amostra uma regressão de contraste no escuro passaria pelo build.
- **Validação estrutural** do HTML gerado: trilha de navegação coerente com o respectivo JSON-LD, sem migalhas consecutivas duplicadas, sem `aria-controls` apontando para id inexistente (esta verificação roda em *todas* as páginas geradas), sem tempo de leitura em listagem de pesquisadores e com os cards contextuais de áreas nos perfis.

Ferramentas automatizadas desse tipo detectam apenas uma minoria dos critérios de sucesso da
WCAG — algo em torno de um terço, e só a parte decidível por máquina. Build verde significa
"nenhuma falha automatizada conhecida nas páginas amostradas", não "acessível".

## Última medição (2026-09-28)

Medido sobre um build local do site atual, nos dois idiomas:

- Pa11y (`WCAG2AA`): **0 erros em 21/21 URLs**.
- Varredura com axe-core 4.12.1 sobre **20 páginas x 2 temas** (claro e escuro), com as regras `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` e `wcag22aa`: **nenhuma violação**. A mesma varredura sobre a versão publicada em 2026-09-27 acusava 145.
- Teclado: 24 ciclos de abrir/fechar dos submenus do cabeçalho (6 menus x 2 idiomas x 2 temas) se comportaram corretamente, e uma varredura completa com Tab em quatro páginas por idioma não encontrou **nenhuma armadilha de teclado**.
- Mapa de competências: 53 nós, todos alcançáveis com Tab, todos ativáveis com Enter e Espaço, com anel de foco visível nos dois temas; os botões de zoom e de filtro têm todos 34 px de altura.
- Filtros de Oportunidades, Publicações e Defesas: todos os controles alcançáveis por teclado, todos nomeados por um `<label>` real, todos com 37 px de altura.
- Refluxo (SC 1.4.10): em **seis larguras entre 320 px e 1280 px** — que cobrem 400% e 200% de zoom —, nenhuma das 26 rotas testadas rola na horizontal.
- Contraste sobre **fundos em gradiente**, que as ferramentas automáticas não conseguem decidir: **635 elementos de texto medidos** em cabeçalho, rodapé, heroes e pills, contra cada parada de cor opaca do gradiente. **Nenhum abaixo do exigido**; piores razões 6,74:1 no rodapé, 5,18:1 nas pills e 7,22:1 nos heroes.
- Tamanho de área clicável (SC 2.5.8, mínimo de 24x24 px): **nenhuma falha** em oito páginas auditadas, aplicando a exceção inline prevista no critério — links de orientador vêm dentro de frase ("Orientador(a): Nome"), acompanhados de texto que não é alvo. Fora da exceção, todo alvo mede ao menos 24 px: o link de busca do cabeçalho agora renderiza 40x40 px e o título dos cards de defesa, 24 px de altura. Os 21 nós de 20x20 px do mapa seguem conformes pela exceção de espaçamento.

## Lacunas conhecidas

São reais, medidas, e estão na fila de correção. Preferimos publicá-las a dar a entender que não existem:

- **O mapa de competências depende de um CDN para a versão visual.** O D3 vem de `cdn.jsdelivr.net`; se o CDN falhar, o grafo não é desenhado. Não é uma falha WCAG — a lista de links equivalente é renderizada no servidor e continua disponível —, mas a experiência visual degrada.
- **Fundos em gradiente ainda dependem de conferência própria.** Quando o fundo é um gradiente, o axe classifica o contraste como "indeterminado" em vez de violação — foi assim que os rótulos do rodapé ficaram em 1,6:1 sem que o CI reclamasse. Passamos a medir esses trechos com um procedimento próprio, registrado acima, mas ele não roda a cada push: é executado após mudança de paleta ou de superfície.
- **Nenhum teste com leitor de tela está registrado.** Nada nesta página se apoia em uma sessão de NVDA, JAWS ou VoiceOver, e não afirmamos o contrário. O roteiro da sessão já está escrito e aguarda execução. Nenhuma auditoria externa foi contratada.

## Reportar uma barreira

Encontrou dificuldade em usar o site? Escreva para [cedis@unb.br](mailto:cedis@unb.br)
descrevendo a página, o que tentou fazer e o que aconteceu. Barreiras identificadas por
usuários têm prioridade na fila de correções.

## Padrões que usamos como referência

- WCAG 2.1 nível AA como alvo, mais os acréscimos aplicáveis da WCAG 2.2 (tamanho de área clicável, aparência do foco, ajuda consistente).
- eMAG (Modelo de Acessibilidade em Governo Eletrônico brasileiro), como referência — não verificado critério por critério.
- Lei Brasileira de Inclusão (Lei 13.146/2015).
