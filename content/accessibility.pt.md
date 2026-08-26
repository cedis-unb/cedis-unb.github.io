---
title: "Acessibilidade"
date: 2026-07-20T09:00:00-03:00
draft: false
language: pt
description: "Compromissos de acessibilidade digital do site do CEDIS: padrões seguidos, recursos disponíveis e canal para reportar barreiras."
featured_image: "../assets/images/pages/media-CEDIS.webp"
eyebrow: "Compromisso com WCAG"
translationKey: accessibility
---

O CEDIS trabalha para que o conteúdo deste site seja utilizável por pessoas com diferentes tipos de deficiência, seguindo as diretrizes da [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/) em nível AA.

## Recursos já implementados

- Link "pular para o conteúdo" (skip link) no topo de cada página.
- Contraste de cor testado em modo claro e escuro.
- Navegação por teclado com foco visível.
- Rótulos ARIA em componentes interativos (menus, botões de tema, formulários).
- Alternativa textual (`alt`) em imagens de conteúdo.
- Estrutura semântica com hierarquia adequada de títulos.
- Suporte a redução de movimento (`prefers-reduced-motion`).

## Validação contínua

- Validação automatizada com Pa11y integrada ao CI para páginas críticas (WCAG 2.0 AA).
- Auditoria com Lighthouse CI em desktop e mobile.
- Relatórios de acessibilidade e Lighthouse anexados aos artefatos do workflow.
- Revisões manuais complementares em fluxos críticos com leitor de tela, navegação por teclado, modo escuro e zoom de 200% e 400%.

## Última medição empírica (2026-07-27)

- Pa11y (WCAG 2.0 AA): **0 erros em 15 URLs representativas**.
- Lighthouse acessibilidade desktop: **100 em 8/8 páginas** (média 100).
- Lighthouse acessibilidade mobile: **100 em 8/8 páginas** (média 100).
- Lighthouse SEO: 100 em todas as páginas medidas.
- Lighthouse boas práticas: 96 em todas as páginas medidas.

Esses números são revalidados a cada alteração de layout ou paleta.

## Reportar uma barreira

Encontrou dificuldade em usar o site? Escreva para [cedis@unb.br](mailto:cedis@unb.br) descrevendo a página, o que tentou fazer e o que aconteceu. Barreiras identificadas por usuários têm prioridade na fila de correções.

## Padrões seguidos

- WCAG 2.1 nível AA (referência internacional).
- eMAG (Modelo de Acessibilidade em Governo Eletrônico brasileiro), quando aplicável.
- Lei Brasileira de Inclusão (Lei 13.146/2015).
