---
author: CEDIS
title: "Engenharia de Requisitos"
date: 2024-02-14T00:43:11-03:00
weight: 5
language: pt
featured_image: "../assets/images/featured/area_Engenharia de requisitos.png"
summary: Engenharia de requisitos (ER) é uma área interdisciplinar da Engenharia de Software que visa realizar a mediação (ponte) entre os domínios do adquirente e do fornecedor ou desenvolvedor.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- george_marsicano
tags: 
- software_requirements
nav_next: true
---
## Introdução
Engenharia de requisitos (ER) é uma área interdisciplinar da Engenharia de Software que visa realizar a mediação (ponte) entre os domínios do adquirente e do fornecedor ou desenvolvedor, para estabelecer e manter os requisitos a serem atendidos pelo sistema, produto de software ou serviço de interesse. Seu processo envolve a elicitação e descoberta, análise e consenso, declaração, representação, verificação e validação, e organização e atualização de requisitos.

No CEDIS, atualmente, a Engenharia de Requisitos é uma área de pesquisa, desenvolvimento e aplicação com enfoque em abordagens de desenvolvimento de software dirigidas a plano, ágeis e híbridas, nos processos e relações humanas a serem construídas durante a execução da ER e, no uso de ferramentas de inteligência artificial. 

Esta linha de pesquisa é coordenada pelo Prof. George Marsicano e conta com uma equipe de pesquisadores dedicados. O objetivo é desenvolver, identificar e estabelecer processos, métodos e ferramentas que tornem o processo de ER mais eficiente e inovador, tanto do ponto de vista técnico quanto humano.

## Publicações e produções

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< npublications caput="Publicações" year="" type="" notypes="" tags="software_requirements" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="software_requirements" notags="" >}} 
    </div>
</div>

{{< tags >}}