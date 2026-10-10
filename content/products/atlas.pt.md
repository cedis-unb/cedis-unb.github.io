---
author: CEDIS
title: "Atlas do Conhecimento"
date: 2026-08-09T09:00:00-03:00
language: pt
product_language: pt
id: atlas
status: active
project: project_ecossistema_cedis
areas:
- gamification
- learning_analytics
responsible:
- sergio_freitas
publications: []
weight: 8
featured_image: "../assets/images/featured/atlas-logo.png"
summary: Espaço pessoal e pseudônimo do estudante para ver o próprio percurso. Progresso em quatro dimensões, rotas curadas, carimbos, diário, constelação de conceitos e bússola motivacional — sem ranking e com k-anonimato.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
- project_ecossistema_cedis
tags:
- app
- gamification
- learning_analytics
- project_ecossistema_cedis
---
## Descrição do Projeto

O **Atlas do Conhecimento** é o espaço pessoal do estudante para ver, revisar e celebrar o próprio percurso de aprendizagem no ecossistema CEDIS. A metáfora é cartográfica: o aluno é um explorador, o conhecimento é um continente com regiões temáticas, cada deck lido é um destino e cada conceito uma estrela. O passaporte guarda carimbos, o diário guarda memórias, a bússola sugere caminhos — mas nunca dita.

O Atlas não é um sistema de gestão de aprendizagem: não hospeda conteúdo, não avalia, não emite certificado. Também não tem ranking, *leaderboard* nem comparação pública entre estudantes. O aluno chega a ele a partir do {{< link-interno "/products/passport" "Learning Passport" >}}, por um handoff seguro com código de uso único, e o que vê ali é só dele.

## Objetivos do Projeto

- mostrar progresso pedagógico em **quatro dimensões** — exploração, prática, consolidação e reflexão — sem reduzir tudo a um único *score*;
- recompensar marcos com carimbos que nunca "resetam" nem expiram, e oferecer expedições opcionais sem penalidade por abandono;
- dar ao estudante uma leitura transparente da própria motivação, com controle total sobre a coleta;
- cumprir a LGPD nativamente: desvincular apaga o percurso e exportar está sempre disponível.

## Recursos e Funcionalidades

**Mapa** (`/mapa`): rotas viram territórios, decks viram destinos, e anéis ao redor de cada destino mostram o progresso 4D naquele deck. **Rotas** (`/rotas`): percursos temáticos curados pelo docente, com requisitos para conclusão. **Carimbos** (`/carimbos`): doze por padrão, de progresso monotônico. **Diário** (`/diario`): linha do tempo com entradas automáticas e reflexões escritas pelo próprio aluno. **Constelação** (`/constelacao`): grafo interativo dos conceitos já tocados, com as relações vindas do {{< link-interno "/products/concept_studio" "Concept Studio" >}}; a cor de cada estrela mostra se o conceito foi mencionado, praticado ou consolidado. **Bússola** (`/bussola`): perfil motivacional Octalysis, por adesão explícita e desligável a qualquer momento. **Próximos passos** (`/proximos-passos`): recomendações em linguagem simples, por cinco heurísticas transparentes — sem aprendizado de máquina nem caixa-preta. **Configurações**: exportar todos os dados em ZIP legível e desvincular do Passaporte, com exclusão em cascata.

**Admin do docente.** Dentro do {{< link-interno "/products/deckmanager" "Deck Manager" >}}, em `/admin/atlas/*`, o docente edita rotas, carimbos e expedições e consulta o dashboard da turma. Toda agregação é **k-anônima** (K = 5): nenhum bucket com menos de cinco estudantes aparece com número absoluto.

**Como os eventos chegam.** Ler um slide, responder uma atividade ou escrever uma reflexão gera um evento no Slides; um serviço de ingestão o consome e o Atlas atualiza contadores, carimbos e sinais. Latência típica: cerca de trinta segundos.

## Vinculação Acadêmica e Apoio

- CEDIS (desenvolvimento e manutenção institucional)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (coordenação)
- {{< link-interno "/projects/ecossistema_cedis" "Ecossistema CEDIS" >}} (projeto de origem)

## Acesso

Espaço do estudante em [atlas.cedis.tec.br](https://atlas.cedis.tec.br/), acessível a partir do widget do Passaporte em qualquer deck. Código aberto, licença MIT, no monorepo [github.com/cedis-unb/CEDIS-Deck-Manager](https://github.com/cedis-unb/CEDIS-Deck-Manager).
