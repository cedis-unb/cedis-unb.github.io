---
author: CEDIS
title: "Arquitetura de Software"
date: 2024-02-14T01:37:18-03:00
language: pt
weight: 5
featured_image: "../assets/images/featured/area_Arquitetura de Software.png"
summary:  Arquitetura de Software é um campo fundamental na engenharia de sistemas que envolve a organização estrutural de componentes de software, suas interações e os princípios orientadores que definem o design e a evolução dos sistemas. Essa área garante a eficiência, a escalabilidade e a manutenção dos sistemas de software, impactando diretamente na qualidade e no desempenho das aplicações.
authorimage: ../assets/images/global/author.webp
categories:
- knowledge_areas
- andre_lanna
- george_marsicano
tags: 
- software_architecture
nav_next: true
---
# Arquitetura de Software

## Introdução
A Arquitetura de Software é um campo fundamental na engenharia de sistemas que envolve a organização estrutural de componentes de software, suas interações e os princípios orientadores que definem o design e a evolução dos sistemas. Essa área é vital para garantir a eficiência, a escalabilidade e a manutenção dos sistemas de software, impactando diretamente na qualidade e no desempenho das aplicações.

## Sobre o coordenador da área
**Prof. André Lanna**

Professor e pesquisador na área de Arquitetura de Software. Atualmente, desempenha o papel de professor adjunto na Universidade de Brasília, contribuindo significativamente para o curso de graduação em Engenharia de Software no campus Gama e para o Programa de Pós-Graduação em Computação Aplicada. Conheça mais sobre o coordenador {{< link-interno "/people/andre_lanna" "aqui" >}}.

## Projetos em andamento
Uma visão geral dos projetos atuais, destacando as inovações e os objetivos desses projetos.

## Equipe de pesquisadores
Apresentação dos membros da equipe, com uma breve descrição de suas especialidades e contribuições para a área.

<div id="npublications-section" x-data="{ showPublications: false }">
    <h2 id="npublications-title" @click="showPublications = !showPublications" class="text-xl font-bold mb-2 cursor-pointer flex items-center text-primary-900">
      {{< npublications caput="Publicações" year="" type="" notypes="" tags="software_architecture" notags="" >}}
      <svg :class="{'rotate-0': !showPublications, 'rotate-180': showPublications}" class="ml-2 h-5 w-5 transform transition-transform duration-200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="#51C5CF"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" /></svg>
    </h2>
    <div x-show="showPublications" x-cloak>
      {{< publications year="" type="" notypes="" tags="software_architecture" notags="" >}} 
    </div>
</div>

## Contato e colaboração
Informações sobre como entrar em contato com a equipe, e oportunidades para colaborações externas.

{{< tags >}}