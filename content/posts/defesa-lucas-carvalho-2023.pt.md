---
title: "Quanto vai custar essa Lambda? TCC prevê tempo de execução em serverless"
date: 2023-07-27T00:00:00-03:00
draft: false
weight: 500
language: pt
featured_image: "../assets/images/featured/area_HPC.png"
summary: 'Lucas Ganda Carvalho e Wíctor Bastos Girardi defenderam na UnB Gama um TCC que investiga a predição do tempo de execução de código em funções AWS Lambda — informação chave para estimar custo em ambientes serverless.'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- defesa
- hpc
---
Brasília, 27 de julho de 2023

Em serverless, o custo é função direta do tempo. Uma função que roda em 200ms paga uma tarifa; a mesma função que roda em 800ms paga quatro vezes mais. E, no entanto, prever esse tempo antes de rodar é uma disciplina pouco desenvolvida — o mercado costuma decidir por benchmarks isolados e otimismo. **É esse espaço vazio que o TCC defendido em julho de 2023 por Lucas Ganda Carvalho e Wíctor Bastos Girardi ocupa**, sob orientação do Prof. {{< link-interno "/people/daniel_lima" "Daniel Sundfeld Lima" >}}.

O trabalho encara o problema com instrumento: em vez de estimar tempo por analogia, propõe uma abordagem preditiva para funções Lambda que combine características do código com dados observados em execuções controladas. Prever com precisão importa por duas razões práticas: quando o custo é bem estimado, a arquitetura ganha grau de liberdade para escolher entre opções serverless e opções tradicionais; quando é mal estimado, o time descobre o preço só depois de encerrado o ciclo de faturamento.

Ao situar {{< link-interno "/areas/HPC/" "computação de alto desempenho" >}} sob a lente do serverless, o TCC contribui para uma agenda de pesquisa que continua ativa no CEDIS — culminando, em 2025, na dissertação de mestrado sobre Nimbus, ambiente serverless para correção automática de códigos.

O TCC pode ser lido na [Biblioteca Digital da Produção Intelectual Discente da UnB](https://www.bdm.unb.br/handle/10483/39151).

---

Sobre o CEDIS:
O Centro de Estudos, Desenvolvimento e Inovação de Software (CEDIS), vinculado à Universidade de Brasília, pesquisa e desenvolve soluções inovadoras em software, com atuação em {{< link-interno "/areas/HPC/" "computação de alto desempenho" >}}.
