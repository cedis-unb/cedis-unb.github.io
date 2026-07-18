---
author: CEDIS
title: "Nativo"
date: 2025-12-16T09:00:00-03:00
language: pt
product_language: pt
weight: 4
featured_image: "../assets/images/featured/nativo-logo.png"
summary: Aplicativo móvel desenvolvido em TCC na UnB para apoiar a preservação e o ensino de línguas indígenas brasileiras, com foco inicial na língua Munduruku, por meio de consultas, histórico e curadoria colaborativa de traduções.
authorimage: ../assets/images/global/author.webp
categories:
- products
- sergio_freitas
tags:
- app
- active_learning
- social_software
- software_products
---
## Descrição do Projeto

O **Nativo** é um aplicativo móvel voltado ao apoio da preservação, da consulta e do ensino de línguas indígenas brasileiras, com foco inicial na língua **Munduruku**. O produto surgiu em um trabalho de conclusão de curso da Universidade de Brasília, desenvolvido por **Alexia Cardoso** sob orientação do Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} e coorientação da Profa. Dra. Célia Higawa.

A proposta nasceu a partir do contato com a Aldeia Munduruku de Bragança e busca oferecer uma ferramenta útil para o dia a dia da comunidade e para contextos de aprendizagem, permitindo consultar palavras e expressões em português e acessar suas traduções escritas no idioma atendido. A implementação combina um aplicativo em **React Native** com uma API em **Python/Flask**, persistência em **Firestore** e controle de acesso por perfis de usuário.

## Objetivos do Projeto

O projeto tem como principais objetivos:

- contribuir para a valorização, a preservação e o ensino da língua Munduruku em formato digital;
- oferecer uma experiência móvel para busca de traduções escritas entre o português e a língua indígena contemplada;
- permitir evolução colaborativa do conteúdo por meio de cadastro, revisão e moderação de traduções; e
- estruturar uma base técnica que possa receber novos idiomas, mídias e recursos de apoio em versões futuras.

## Recursos e Funcionalidades

Entre os recursos do **Nativo** estão a consulta de traduções a partir de palavras e expressões informadas pelo usuário, a exibição da categoria do discurso associada ao resultado e o armazenamento de histórico para reutilização de buscas anteriores. O aplicativo também reúne materiais informativos e manuais de apoio voltados ao uso da solução e ao contexto cultural que motivou o projeto.

Além da experiência principal de consulta, a arquitetura do sistema contempla perfis com responsabilidades distintas, como usuário, moderador, professor e administrador, viabilizando cadastro, edição, revisão e organização de traduções, idiomas, categorias e usuários. A base do projeto ainda prevê expansão com recursos como áudio, imagens e ampliação do conjunto de idiomas atendidos.

## Vinculação Acadêmica

- Alexia Cardoso (desenvolvimento do produto no TCC)
- Prof. {{< link-interno "/people/sergio_freitas" "Sergio Freitas" >}} (orientação acadêmica)
- Profa. Dra. Célia Higawa (coorientação)
- Comunidade Munduruku de Bragança (contexto de origem e alinhamento do problema)

## Acesso

O código-fonte do projeto está disponível em [GitHub](https://github.com/CedisUnB/Nativo).
