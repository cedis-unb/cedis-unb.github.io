---
title: "CEDIS Concept Studio: mapas conceituais, IA com revisão humana e questionários dentro da aula"
date: 2026-08-09T09:10:00-03:00
draft: false
weight: 500
language: pt
featured_image: "../assets/images/featured/concept_studio-logo.png"
summary: "O ateliê semântico do docente organiza os conceitos de uma disciplina em mapas versionados, aceita sugestões de IA só com confirmação humana e transforma o mapa em questionários de prática que chegam aos estudantes pelo Slides."
description: "CEDIS Concept Studio, o produto do Ecossistema CEDIS para criar, conectar e avaliar conceitos — com questionários formativos integrados."
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- active_learning
- ai
- learning_analytics
- project_ecossistema_cedis
- concept_studio
related_ids:
- concept_studio
- project_ecossistema_cedis
- sergio_freitas
---

Brasília, 9 de agosto de 2026

Qual conceito está confundindo a turma? A pergunta parece simples, mas quase nenhum docente tem um jeito objetivo de respondê-la antes da prova. O **CEDIS Concept Studio**, apresentado hoje como parte do {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}}, foi feito para responder exatamente isso.

O Concept Studio é o ateliê semântico do docente. A partir de um deck publicado no {{< link-interno "/products/deckmanager" "Deck Manager" >}}, o professor monta o mapa dos conceitos que a aula aborda e os conecta com relações que têm significado — pré-requisito, hierarquia, parte-de, contraste, confusão comum. O banco de conceitos é vivo: cria-se, edita-se, mescla-se, e um conceito pode ser promovido do uso pessoal para a pasta e para o CEDIS inteiro. Cada mapa tem versões imutáveis.

A inteligência artificial entra como assistente, nunca como autoridade. O docente pede à IA que analise o deck e proponha conceitos e relações; cada candidato é confirmado ou rejeitado por uma pessoa, e toda sugestão guarda sua proveniência — qual provedor, qual modelo, qual versão do prompt, qual trecho do texto. O provedor é configurável, inclusive um *stub* local sem chamada externa.

É daí que saem os **questionários**. Do banco de conceitos, o docente cria questões — escolha única ou múltipla, verdadeiro ou falso, numérica, resposta curta, escalas Likert, de diferencial semântico e de confiança — e as publica como conjuntos de prática. O {{< link-interno "/products/slides" "Slides" >}} os serve aos estudantes ao fim do deck, com feedback imediato; a página de analytics devolve ao docente a taxa de acerto por questão, o tempo médio e as questões mais erradas. Por desenho, não há nota somativa, ranking nem certificação: é prática formativa.

O Concept Studio também alimenta o {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}}: as relações entre conceitos viram as linhas da constelação que cada estudante vê do seu próprio percurso. E tudo nasce desligado — o sistema de questionários é ativado por feature flags, ambiente a ambiente.

A aplicação está no ar em [concepts.cedis.tec.br](https://concepts.cedis.tec.br/), com login institucional e código aberto sob licença MIT, coordenada pelo Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}}. A {{< link-interno "/products/concept_studio" "página do Concept Studio" >}} detalha os recursos; a visão de conjunto está em {{< link-interno "/posts/news-post.035" "a apresentação do Ecossistema CEDIS" >}}.
