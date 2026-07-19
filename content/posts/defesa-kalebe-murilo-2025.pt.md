---
title: "AgroMart migra de IaaS para serverless: dupla mostra que produtor rural pode ficar dentro do free tier"
date: 2025-02-25T00:00:00-03:00
draft: false
weight: 500
language: pt
featured_image: "../assets/images/featured/area_Arquitetura de Software.png"
summary: 'Kalebe Cunha e Murilo Santana defenderam em fevereiro de 2025, na FCTE/UnB, um TCC que migra o AgroMart do modelo IaaS para AWS Lambda e testa a viabilidade de operar dentro do free tier — reduzindo o custo do agricultor.'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- defesa
- software_architecture
- digital_transformation
---
Brasília, 25 de fevereiro de 2025

A pergunta central deste TCC não é técnica, é econômica: quanto custa hoje, em dólares, para um pequeno produtor rural manter viva a Comunidade que Sustenta a Agricultura (CSA) na qual ele vende diretamente para consumidores? **O trabalho defendido por Kalebe Lopes da Cunha e Murilo Schiler Lopes Santana em fevereiro de 2025, na Faculdade de Ciências e Tecnologias em Engenharia (FCTE) da UnB, propõe uma resposta arquitetural — e a testa** — sob orientação do Prof. {{< link-interno "/people/andre_lanna" "André Luiz Peron Martins Lanna" >}}.

O AgroMart, aplicação que conecta produtores e consumidores em modelo CSA, roda em instâncias EC2 dentro de um modelo tradicional de Infraestrutura como Serviço. É uma escolha comum e defensável — e, para o público-alvo do projeto, incontornável em termos de custo: cada real cobrado do agricultor é um argumento a menos para adotar a solução. Os autores partem justamente desse gargalo para justificar a investigação: se o objetivo é acessibilidade, então a arquitetura precisa acompanhar.

A proposta é migrar tanto a API de dicionário quanto o backend STRAPI para o paradigma serverless, especificamente Função como Serviço (FaaS) rodando em AWS Lambda. O trabalho é ao mesmo tempo de {{< link-interno "/areas/software_architecture/" "arquitetura de software" >}} e de {{< link-interno "/areas/transformation/" "transformação digital" >}}, porque a mudança arquitetural é o veículo para o resultado social — permitir que a infraestrutura opere dentro dos limites gratuitos da AWS, eliminando custos operacionais em cenários típicos de uso.

Além do exercício de migração, o TCC analisa em que condições as APIs podem estourar os limites do free tier e quais implicações isso trará — informação essencial para que futuros mantenedores saibam o quanto o modelo aguenta antes de exigir investimento. É um estudo de caso concreto de como decisões de plataforma se traduzem em impacto social direto para um grupo de usuários que raramente cabe no orçamento das arquiteturas padrão.

O trabalho pode ser lido na íntegra na [Biblioteca Digital da Produção Intelectual Discente da UnB](https://bdm.unb.br/handle/10483/43566).

---

Sobre o CEDIS:
O Centro de Estudos, Desenvolvimento e Inovação de Software (CEDIS), vinculado à Universidade de Brasília, pesquisa e desenvolve soluções inovadoras em software, com forte atuação em {{< link-interno "/areas/software_architecture/" "arquitetura de software" >}} e {{< link-interno "/areas/transformation/" "transformação digital" >}}.
