---
title: "Contar pontos de função sem gente contando: dissertação lê requisições HTTP para automatizar SFP"
date: 2025-10-23T00:00:00-03:00
draft: false
weight: 500
language: pt
featured_image: "../assets/images/featured/area_Engenharia de requisitos.png"
summary: 'Diego Emanuel Ferreira da Rocha defendeu no PPCA/UnB a etapa de qualificação da dissertação que automatiza a identificação de processos elementares a partir da análise de requisições HTTP — reduzindo a fricção do Simple Function Points.'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- defesa
- software_requirements
- machine_learning
---
Brasília, 23 de outubro de 2025

Simple Function Points (SFP) é hoje uma das medidas de tamanho funcional mais aceitas no mercado — e uma das mais penosas de aplicar. A contagem é manual, exige documentação abrangente do sistema e depende de especialistas com o método na ponta da língua. **É contra essa fricção que a pesquisa de mestrado profissional de Diego Emanuel Ferreira da Rocha se organiza**, apresentada em outubro de 2025 no PPCA/UnB sob orientação do Prof. Dr. {{< link-interno "/people/andre_lanna" "André Luiz Peron Martins Lanna" >}}.

O trabalho propõe automatizar a identificação de processos elementares — a unidade básica do SFP — a partir da análise de requisições HTTP das aplicações web em execução. A ideia é elegante: as requisições revelam jornadas de usuário; agrupar requisições que ocorrem em conjunto revela funcionalidades; classificar esses agrupamentos segundo as regras do SFP produz medição funcional. O método é agnóstico de tecnologia — não depende de quais frameworks ou linguagens sustentam o software — e recorre a Longest Common Subsequence para lidar com variações reais das jornadas observadas.

Os resultados relatados alcançam variação média de 17% em relação à contagem manual, próxima ao patamar de 15% considerado aceitável na medição feita por humanos. É uma contribuição concreta para {{< link-interno "/areas/software_requirements/" "engenharia de requisitos" >}} e {{< link-interno "/areas/ai_pln/" "aprendizado de máquina aplicado" >}}: um caminho para tirar do fluxo aquilo que costuma paralisar a adoção do SFP.

A qualificação aconteceu em 23 de outubro de 2025 em Brasília. A banca foi presidida pelo orientador, Prof. Dr. André Luiz Peron Martins Lanna (FGA/UnB), e composta pela Prof.ª Dr.ª Monalessa Perini Barcellos (PPGI/UFES) e pelo Prof. Dr. Sérgio Antônio Andrade de Freitas (FGA/UnB). A Prof.ª Dr.ª Edna Dias Canedo, coordenadora do PPCA, também acompanhou a sessão.

O trabalho está disponível no [Repositório Institucional da UnB](https://repositorio.unb.br/handle/10482/54552).

---

Sobre o CEDIS:
O Centro de Estudos, Desenvolvimento e Inovação de Software (CEDIS), vinculado à Universidade de Brasília, pesquisa e desenvolve soluções inovadoras em software.
