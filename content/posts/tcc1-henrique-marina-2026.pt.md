---
title: "Random Forest e Suricata: separar sinal de ruído em alertas de intrusão"
date: 2026-07-04T00:00:00-03:00
draft: false
weight: 500
language: pt
featured_image: "../assets/images/featured/area_Cybersecurity.webp"
summary: 'Henrique Azevedo Batalha e Marina Márcia Costa de Souza apresentaram na FCTE/UnB o TCC1 que integra o IDS Suricata a um classificador Random Forest — treinado sobre o dataset CSE-CIC-IDS2018 — para tornar a análise de alertas de intrusão mais organizada e menos susceptível a falsos positivos.'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- tcc1
- security
- machine_learning
- ai
---
Brasília, julho de 2026

Detectar intrusão em rede é como procurar agulha num palheiro que cresce por segundo. Sistemas de Detecção de Intrusões (IDS) tradicionais fazem seu trabalho — geram alertas — mas geram tantos que o analista, exausto, começa a ignorar sinais que talvez fossem legítimos. **É esse gargalo de análise, e não a detecção em si, que Henrique Azevedo Batalha e Marina Márcia Costa de Souza escolheram atacar em seu TCC1**, apresentado na Faculdade de Ciências e Tecnologias em Engenharia (FCTE), sob orientação do Prof. {{< link-interno "/people/sergio_freitas" "Sergio Antônio Andrade de Freitas" >}}.

A proposta integra três peças: o IDS open source Suricata, responsável por observar o tráfego de rede e emitir alertas; um classificador Random Forest, escolhido por sua robustez, capacidade de lidar com múltiplos atributos e possibilidade de explicar a importância relativa das *features*; e uma interface gráfica de apoio à análise, com histórico, filtros e dashboard.

Para os experimentos iniciais, o modelo foi treinado sobre uma versão em CSV do dataset CSE-CIC-IDS2018 — referência da área de {{< link-interno "/areas/security/" "cibersegurança" >}} com fluxos de rede rotulados. A dupla executou limpeza, conversão de atributos, definição da variável-alvo e a divisão canônica entre treinamento e teste. O TCC1 fecha a fase de requisitos, arquitetura lógica, treinamento inicial do modelo e prototipagem no Figma; deixa como próximo passo, para o TCC2, a integração dos componentes em uma aplicação funcional avaliada em ambiente controlado.

O que o trabalho coloca em evidência é uma tese incômoda: no perímetro corporativo típico, o valor agregado de um IDS não está mais no bit que detecta, e sim no bit que **prioriza**. Random Forest entra aqui como filtro de segundo nível, atribuindo veredito e nível de confiança para cada alerta — devolvendo tempo ao analista humano e reduzindo o custo cognitivo do falso positivo. É o tipo de aplicação em que {{< link-interno "/areas/ai_pln/" "aprendizado de máquina" >}} se acopla à {{< link-interno "/areas/security/" "segurança de redes" >}} não para substituir o especialista, mas para tornar seu trabalho sustentável.

---

Sobre o CEDIS:
O Centro de Estudos, Desenvolvimento e Inovação de Software (CEDIS), vinculado à Universidade de Brasília, pesquisa e desenvolve soluções inovadoras em software, com forte atuação em {{< link-interno "/areas/security/" "cibersegurança" >}} e {{< link-interno "/areas/ai_pln/" "inteligência artificial" >}}.
