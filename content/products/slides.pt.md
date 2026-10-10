---
author: CEDIS
title: "CEDIS Slides"
date: 2026-08-09T09:00:00-03:00
language: pt
product_language: pt
id: slides
status: active
project: project_ecossistema_cedis
areas:
- active_learning
- digital_transformation
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/slides-logo.png"
summary: Runtime público das apresentações do CEDIS. Serve os decks HTML aos estudantes, embute atividades e questionários, coleta respostas em tempo real e entrega ao docente o resumo ao vivo e a exportação em CSV.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_ecossistema_cedis
tags:
- app
- active_learning
- digital_transformation
- project_ecossistema_cedis
---
## Descrição do Projeto

O **CEDIS Slides** é o lugar onde a aula acontece. Enquanto o {{< link-interno "/products/deckmanager" "Deck Manager" >}} é o painel em que o docente cataloga e publica suas apresentações, o Slides é o runtime público que entrega cada deck ao estudante no navegador — em qualquer dispositivo, sem instalar nada.

Cada deck publicado é um único arquivo HTML autocontido, com CSS e JavaScript embutidos. O estudante abre `slides.cedis.tec.br/<pasta>/<deck>`, navega com as setas do teclado ou por gesto na tela, e responde às atividades que o docente embutiu nos slides. A landing pública de `slides.cedis.tec.br` é a porta de entrada mais comum do aluno: um grid dos decks abertos, organizado por popularidade, avaliação e recência.

## Objetivos do Projeto

- entregar apresentações autorais em HTML leve e acessível, sem formato proprietário nem dependência de provedor externo;
- transformar o slide em instrumento de participação: a resposta do aluno sai do próprio deck e chega ao docente em segundos;
- respeitar as políticas de atividade definidas no Deck Manager — a aula "só na sala", a programação recorrente por semestre, o código projetado pelo apresentador;
- preservar a privacidade do estudante: sem cookies de rastreio, *Do Not Track* honrado, relatórios agregados com k-anonimato.

## Recursos e Funcionalidades

**Navegação** por teclado (setas, `n` para as notas do apresentador, `f` para tela cheia), *swipe* no toque e um botão flutuante de notas em iPad e iPhone, onde não há teclado.

**Atividades embutidas.** Um slide marcado como atividade exibe o formulário; o aluno responde e clica "Enviar". Quando a política do deck exige, o estudante digita o **código de sessão** que o docente projeta na tela para sincronizar a turma. O docente acompanha o **resumo ao vivo** em `/s/<deck>/<atividade>` — histograma, nuvem de tags, respostas mais frequentes — e baixa tudo em **CSV**.

**Questionários.** Ao fim do deck, o botão "Praticar" abre as sessões de prática publicadas pelo {{< link-interno "/products/concept_studio" "Concept Studio" >}}, com feedback imediato a cada resposta.

**Passaporte.** No canto inferior direito, o widget "Usar Passaporte" permite ao estudante, se quiser, vincular a leitura e as respostas à sua identidade pseudônima do {{< link-interno "/products/passport" "Learning Passport" >}} — e, a partir daí, ver o percurso no {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}}.

**Modo de falha consciente.** Se o painel do Deck Manager estiver fora do ar, a leitura do deck continua (*fail-open*); o envio de respostas em políticas controladas por sessão, código ou agendamento é bloqueado (*fail-closed*). A aula nunca para por causa de um serviço vizinho.

## Vinculação Acadêmica e Apoio

- CEDIS (desenvolvimento e manutenção institucional)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordenação)
- {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}} (projeto de origem)

## Acesso

Vitrine pública e runtime dos decks em [slides.cedis.tec.br](https://slides.cedis.tec.br/). Código aberto, licença MIT, no monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
