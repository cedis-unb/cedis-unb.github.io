---
title: "Antes do boom da IA generativa, um TCC já ensinava a máquina a corrigir dissertativas"
date: 2016-07-01T00:00:00-03:00
draft: false
weight: 500
language: pt
featured_image: "../assets/images/featured/area_IA.png"
summary: 'Em 2016, muito antes do frenesi dos LLMs, Cristóvão Frinhani defendeu na UnB Gama um TCC que usa similaridade semântica e aprendizado de máquina para auxiliar tutores de EAD na correção de questões dissertativas.'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- defesa
- ai
- nlp
- machine_learning
---
Brasília, 1º de julho de 2016

O que hoje soa quase trivial diante de qualquer chatbot moderno era, há uma década, um problema aberto: dar a um computador a capacidade de julgar se uma resposta dissertativa está próxima ou distante de um gabarito. **Foi esse o desafio enfrentado por Cristóvão de Lima Frinhani em seu Trabalho de Conclusão de Curso de Engenharia de Software na Faculdade UnB Gama**, defendido em julho de 2016 sob orientação do Prof. {{< link-interno "/people/sergio_freitas" "Sergio Antônio Andrade de Freitas" >}} e coorientação do Prof. Mauricio Vidotti Fernandes.

A motivação do trabalho é diretamente ligada ao gargalo do ensino a distância: modalidade que crescia rapidamente no país e esbarrava em custos e tempo para correção de avaliações discursivas. O sistema proposto pelo autor articula duas frentes. Primeiro, a similaridade semântica entre a resposta do aluno e o gabarito registrado pelo tutor é usada para produzir uma nota preliminar. Depois, um componente de aprendizado de máquina refina essa nota com base no *feedback* que o tutor devolve — cada correção humana ajusta o modelo para que os erros seguintes fiquem menores.

A ideia é elegante por combinar {{< link-interno "/areas/ai_pln/" "processamento de linguagem natural" >}} com um laço de aprendizado supervisionado que amortece as imperfeições dos algoritmos de similaridade. Para testar o sistema, o autor conduziu experimentos usando conteúdos da disciplina de Fundamentos de Arquitetura de Computadores, comparando notas geradas pela máquina com notas atribuídas manualmente.

O TCC foi orientado dentro da linha de pesquisa em {{< link-interno "/areas/active_learning/" "aprendizagem ativa" >}} e tecnologias educacionais que sempre marcou a atuação do Prof. Sergio Freitas no CEDIS, e antecipa, em contexto acadêmico, questões que a comunidade voltaria a discutir com força a partir de 2022 com a popularização dos grandes modelos de linguagem: como calibrar avaliações automáticas em contextos onde erros são pedagogicamente custosos.

O trabalho, defendido na Faculdade UnB Gama, está disponível na [Biblioteca Digital da Produção Intelectual Discente da UnB](https://bdm.unb.br/handle/10483/14871).

---

Sobre o CEDIS:
O Centro de Estudos, Desenvolvimento e Inovação de Software (CEDIS), vinculado à Universidade de Brasília, pesquisa e desenvolve soluções inovadoras em software com forte atuação em {{< link-interno "/areas/ai_pln/" "IA e Processamento de Linguagem Natural" >}}.
