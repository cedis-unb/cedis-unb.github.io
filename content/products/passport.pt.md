---
author: CEDIS
title: "CEDIS Learning Passport"
date: 2026-08-09T09:00:00-03:00
language: pt
product_language: pt
id: passport
status: active
project: project_ecossistema_cedis
areas:
- digital_transformation
- security
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/passport-logo.png"
summary: Identidade pseudônima do estudante no ecossistema. Criada a partir de uma frase-semente, sem e-mail nem dado pessoal, com consentimento versionado, autorização por serviço e exclusão em cascata conforme a LGPD.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_ecossistema_cedis
tags:
- app
- digital_transformation
- security
- project_ecossistema_cedis
---
## Descrição do Projeto

O **CEDIS Learning Passport** é a identidade do estudante no ecossistema — um passaporte de viagem que registra passagens pelo território do conhecimento sem revelar quem é o viajante. É ele que permite ao {{< link-interno "/products/slides" "Slides" >}} lembrar o que um aluno já respondeu, ao {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} desenhar o percurso desse aluno e ao {{< link-interno "/products/cedis_learning_analytics" "Learning Analytics" >}} reunir sinais ao longo do tempo — tudo sem que nenhum desses serviços saiba o nome, o e-mail ou a matrícula de ninguém.

O motivo de existir é concreto: uma universidade pública brasileira precisa oferecer feedback pedagógico personalizado sem violar a LGPD, e não pode sequer armazenar o e-mail institucional do estudante em sistemas de analytics de aprendizagem. O Passaporte resolve o problema na raiz: fora dele, nenhum serviço vê mais do que um identificador pseudônimo derivado por HMAC e escopado por serviço.

## Objetivos do Projeto

- criar uma identidade de aprendiz **sem dado pessoal**: nem e-mail, nem matrícula, nem CPF, nem nome;
- deixar o estudante no controle — ele decide se usa o Passaporte, o que compartilha com cada serviço e quando apagar tudo;
- tornar o consentimento probatório e versionado, à altura do ônus da prova que a LGPD impõe;
- servir de provedor de identidade pseudônima para os demais produtos, sem que cada um reinvente autenticação.

## Recursos e Funcionalidades

**Criação por frase-semente.** O estudante gera seu passaporte a partir de uma frase de doze palavras, no padrão de carteiras digitais. A frase é a chave: não existe "esqueci minha senha", existe digitar a frase e recuperar o passaporte.

**Painel do estudante.** Mostra o próprio percurso agrupado por deck — leituras, respostas enviadas — e traz o botão "apagar meu passaporte", que dispara a exclusão em cascata em Slides, Atlas e Concept Studio.

**Consentimento como pacote imutável.** Cada versão reúne três documentos — manifestação, aviso de privacidade e termos — com hash SHA-256 registrado, e a trilha de aceite é *append-only*: preserva exatamente o que foi apresentado ao estudante. A autorização é granular, por serviço (Slides, Concept Studio, Atlas, Learning Analytics), e revogar o Learning Analytics apaga os dados dele na origem. Mudanças materiais exigem novo aceite; ajustes de redação, não. Base legal: LGPD, art. 7º, I, e art. 46, § 2º.

**Provedor OIDC.** O Passaporte é um servidor OpenID Connect leve: os outros serviços do CEDIS o usam como identidade pseudônima, com um identificador diferente por relação — rotacionar qualquer chave quebra o vínculo, por desenho.

## Vinculação Acadêmica e Apoio

- CEDIS (desenvolvimento e manutenção institucional)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordenação)
- {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}} (projeto de origem)

## Acesso

Passaporte do estudante em [passport.cedis.tec.br](https://passport.cedis.tec.br/), acionado pelo widget "Usar Passaporte" em qualquer deck do Slides. Código aberto, licença MIT, no monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
