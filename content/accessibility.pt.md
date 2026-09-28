---
title: "Acessibilidade"
date: 2026-07-20T09:00:00-03:00
draft: false
language: pt
description: "Situação da acessibilidade digital do site do CEDIS: o nível que buscamos, o que cada build verifica automaticamente, o que foi verificado manualmente e as lacunas que já conhecemos."
featured_image: "../assets/images/pages/media-CEDIS.webp"
eyebrow: "Compromisso com WCAG"
translationKey: accessibility
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
- **Validação estrutural** do HTML gerado: trilha de navegação coerente com o respectivo JSON-LD, sem migalhas consecutivas duplicadas, sem `aria-controls` apontando para id inexistente (esta verificação roda em *todas* as páginas geradas), sem tempo de leitura em listagem de pesquisadores e com os cards contextuais de áreas nos perfis.

Ferramentas automatizadas desse tipo detectam apenas uma minoria dos critérios de sucesso da
WCAG — algo em torno de um terço, e só a parte decidível por máquina. Build verde significa
"nenhuma falha automatizada conhecida nas páginas amostradas", não "acessível".

## Última medição (2026-09-27)

Medido sobre um build local do site atual, nos dois idiomas:

- Pa11y (`WCAG2AA`): **0 erros em 21/21 URLs**.
- Varredura com axe-core 4.12.1 sobre **16 páginas x 2 temas** (claro e escuro), com as regras `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` e `wcag22aa`: **nenhuma violação**. A mesma varredura sobre a versão publicada anteriormente acusava 145.
- Teclado: 24 ciclos de abrir/fechar dos submenus do cabeçalho (6 menus x 2 idiomas x 2 temas) se comportaram corretamente, e uma varredura completa com Tab em quatro páginas por idioma não encontrou **nenhuma armadilha de teclado**.
- Mapa de competências: 53 nós, todos alcançáveis com Tab, todos ativáveis com Enter e Espaço, com anel de foco visível nos dois temas; os botões de zoom e de filtro têm todos 34 px de altura.
- Filtros de Oportunidades, Publicações e Defesas: todos os controles alcançáveis por teclado, todos nomeados por um `<label>` real, todos com 37 px de altura.
- Refluxo (SC 1.4.10): com **zoom de 200%** (viewport de 640 px), nenhuma das 13 rotas testadas rola na horizontal.
- Tamanho de área clicável (WCAG 2.2, mínimo de 24x24 px): todo `<button>` e todo `<select>` tem ao menos 34 px de altura. Dois controles ficam abaixo de 24 px e conformam apenas pela exceção de espaçamento prevista no critério: o link de busca do cabeçalho (**20x40 px**) e 21 dos 53 nós do mapa (**20x20 px**).

## Lacunas conhecidas

São reais, medidas, e estão na fila de correção. Preferimos publicá-las a dar a entender que não existem:

- **Refluxo a 400% de zoom.** Em um viewport de 320 px, a página inicial, Publicações e os perfis de pesquisador ainda rolam na horizontal por 13 a 34 px. A 200% o site está limpo.
- **Listagens densas e área clicável.** Na listagem de Defesas, os links de texto de cards consecutivos ficam mais próximos entre si do que os 24 px pedidos pela WCAG 2.2.
- **A verificação automatizada de contraste no CI roda só em modo claro.** A varredura em modo escuro descrita acima é um procedimento manual; nada impede que uma regressão de contraste no tema escuro passe pelo build.
- **Fundos em gradiente escapam da verificação automática.** Quando o fundo é um gradiente, o axe classifica o contraste como "indeterminado" em vez de violação — foi assim que os rótulos do rodapé ficaram em 1,6:1 sem que o CI reclamasse. Trechos com gradiente precisam de conferência manual.
- **Nenhum teste com leitor de tela está registrado.** Nada nesta página se apoia em uma sessão de NVDA, JAWS ou VoiceOver, e não afirmamos o contrário. Nenhuma auditoria externa foi contratada.

## Reportar uma barreira

Encontrou dificuldade em usar o site? Escreva para [cedis@unb.br](mailto:cedis@unb.br)
descrevendo a página, o que tentou fazer e o que aconteceu. Barreiras identificadas por
usuários têm prioridade na fila de correções.

## Padrões que usamos como referência

- WCAG 2.1 nível AA como alvo, mais os acréscimos aplicáveis da WCAG 2.2 (tamanho de área clicável, aparência do foco, ajuda consistente).
- eMAG (Modelo de Acessibilidade em Governo Eletrônico brasileiro), como referência — não verificado critério por critério.
- Lei Brasileira de Inclusão (Lei 13.146/2015).
