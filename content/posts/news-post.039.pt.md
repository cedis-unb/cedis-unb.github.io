---
title: "CEDIS Learning Passport: uma identidade de aprendiz sem e-mail, sem CPF e sob controle do estudante"
date: 2026-08-09T09:30:00-03:00
draft: false
weight: 500
language: pt
featured_image: "../assets/images/featured/passport-logo.png"
summary: "Criado a partir de uma frase de doze palavras, o Passaporte registra o percurso do estudante por todo o Ecossistema CEDIS sem armazenar nenhum dado pessoal — e deixa com ele a decisão de compartilhar ou apagar."
description: "CEDIS Learning Passport, a identidade pseudônima que permite feedback pedagógico personalizado em conformidade com a LGPD."
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- digital_transformation
- security
- project_ecossistema_cedis
- passport
related_ids:
- passport
- project_ecossistema_cedis
- sergio_freitas
---

Brasília, 9 de agosto de 2026

Uma universidade pública que quer dar feedback pedagógico personalizado a cada estudante esbarra num limite concreto: pela LGPD, não pode sequer armazenar o e-mail institucional do aluno em sistemas de análise da aprendizagem. Como lembrar o que alguém já respondeu sem saber quem é esse alguém? O **CEDIS Learning Passport**, apresentado hoje como parte do {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}}, resolve o problema na raiz.

O Passaporte é a identidade do estudante no ecossistema — um passaporte de viagem que registra passagens pelo território do conhecimento sem revelar quem é o viajante. Ele é criado a partir de uma **frase-semente de doze palavras**, no padrão das carteiras digitais. Nem e-mail, nem matrícula, nem CPF, nem nome. A frase é a chave: não existe "esqueci minha senha", existe digitar a frase e recuperar o passaporte.

Fora do Passaporte, nenhum serviço vê mais do que um identificador pseudônimo, derivado por HMAC e diferente para cada produto. É assim que o {{< link-interno "/products/slides" "Slides" >}} lembra o que um aluno respondeu, o {{< link-interno "/products/atlas" "Atlas do Conhecimento" >}} desenha seu percurso e o {{< link-interno "/products/cedis_learning_analytics" "Learning Analytics" >}} reúne sinais ao longo do tempo — sem que nenhum deles conheça a pessoa por trás do hash. O Passaporte funciona como um provedor OpenID Connect leve para toda a família, e rotacionar qualquer chave quebra o vínculo, por desenho.

O consentimento é tratado como prova, não como formalidade. Cada versão reúne três documentos — manifestação, aviso de privacidade e termos — com hash registrado e trilha de aceite que preserva exatamente o que foi apresentado. A autorização é granular, serviço a serviço; revogar o Learning Analytics apaga os dados dele na origem. Mudanças materiais exigem novo aceite; ajustes de redação, não. No painel, o estudante vê o próprio percurso agrupado por deck e tem à mão o botão "apagar meu passaporte", que dispara a exclusão em cascata em Slides, Atlas e Concept Studio.

O Passaporte está em produção em [passport.cedis.tec.br](https://passport.cedis.tec.br/), com código aberto sob licença MIT, coordenado pelo Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}}. A {{< link-interno "/products/passport" "página do Learning Passport" >}} detalha os recursos; a visão de conjunto está em {{< link-interno "/posts/news-post.035" "a apresentação do Ecossistema CEDIS" >}}.
