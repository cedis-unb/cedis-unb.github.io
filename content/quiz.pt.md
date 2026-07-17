---
title: "Qual área do CEDIS combina com você?"
date: 2026-07-17T00:00:00-03:00
draft: false
language: pt
layout: quiz
description: "5 perguntas rápidas para descobrir com que área do CEDIS e quais pesquisadores seu perfil mais se alinha."
featured_image: "../assets/images/pages/media-CEDIS.png"
eyebrow: "Descoberta guiada"
questions:
  - id: q1
    text: "Qual problema mais te atrai?"
    options:
      - text: "Ensinar melhor, medir aprendizagem, criar experiências educacionais"
        weights: { active_learning: 3, gamification: 3, learning_analytics: 3, education: 3 }
      - text: "Fazer software mais robusto, testável e seguro"
        weights: { software_quality: 3, verification_validation_testing: 3, security: 2, software_architecture: 2 }
      - text: "Usar IA, PLN e dados para resolver algo do mundo real"
        weights: { ai: 3, machine_learning: 3, nlp: 2, learning_analytics: 2 }
      - text: "Impacto social — governo digital, ONGs, políticas públicas"
        weights: { social_software: 3, digital_transformation: 3, education: 2, software_requirements: 1 }
      - text: "Infraestrutura crítica, performance, escala"
        weights: { hpc: 3, software_architecture: 2, security: 2 }

  - id: q2
    text: "Como você se descreve?"
    options:
      - text: "Empolgado(a) por trabalhar com pessoas e equipes"
        weights: { soft_skills: 3, teamwork: 3, active_learning: 2, education: 2, software_requirements: 1 }
      - text: "Detalhista, gosto de análise e prova rigorosa"
        weights: { verification_validation_testing: 3, software_quality: 2, software_architecture: 2 }
      - text: "Curioso(a) por padrões escondidos nos dados"
        weights: { machine_learning: 3, ai: 2, learning_analytics: 3, nlp: 2 }
      - text: "Construtor(a) — quero fazer coisas funcionarem"
        weights: { software_architecture: 3, software_product_line: 2, software_quality: 2, digital_transformation: 2 }
      - text: "Estratégico(a) — entendo o contexto antes de decidir"
        weights: { software_requirements: 3, digital_transformation: 2, social_software: 2 }

  - id: q3
    text: "Qual desses temas te acende mais?"
    options:
      - text: "Chatbots, transformers, PLN aplicado"
        weights: { nlp: 3, ai: 3, machine_learning: 2 }
      - text: "Jogos educacionais, motivação, engajamento"
        weights: { gamification: 3, active_learning: 2, learning_analytics: 2, education: 2 }
      - text: "Sistemas em produção com muitos usuários"
        weights: { software_architecture: 3, software_quality: 2, software_product_line: 2, digital_transformation: 1 }
      - text: "Segurança da informação, criptografia, defesa"
        weights: { security: 3, software_architecture: 1, verification_validation_testing: 1 }
      - text: "Impacto ambiental de software (Green SD)"
        weights: { green_software: 3, software_quality: 2 }
      - text: "Alto desempenho, GPU, paralelismo"
        weights: { hpc: 3 }

  - id: q4
    text: "Que tipo de resultado te dá mais satisfação?"
    options:
      - text: "Ver uma pessoa aprendendo melhor por causa do que fiz"
        weights: { active_learning: 3, education: 3, gamification: 2, learning_analytics: 2 }
      - text: "Um artigo científico rigoroso em bom venue"
        weights: { verification_validation_testing: 3, software_architecture: 2, software_requirements: 2, machine_learning: 1 }
      - text: "Um sistema que outros usam e recomendam"
        weights: { software_architecture: 3, digital_transformation: 3, software_product_line: 2, software_quality: 2 }
      - text: "Um modelo/algoritmo que resolve um problema específico"
        weights: { machine_learning: 3, ai: 3, nlp: 2, hpc: 2 }
      - text: "Uma metodologia que muda como equipes trabalham"
        weights: { soft_skills: 3, teamwork: 3, software_requirements: 2, active_learning: 2 }

  - id: q5
    text: "Onde você quer estar daqui 3-4 anos?"
    options:
      - text: "Pesquisando ou lecionando em universidade"
        weights: { active_learning: 2, education: 3, learning_analytics: 2, software_requirements: 1, verification_validation_testing: 1, ai: 1 }
      - text: "Em empresa de produto — dev sênior / tech lead"
        weights: { software_architecture: 3, software_quality: 3, software_product_line: 2, software_requirements: 2 }
      - text: "Em startup ou consultoria de IA/dados"
        weights: { machine_learning: 3, ai: 3, nlp: 2, digital_transformation: 2 }
      - text: "Servindo ao setor público / transformação digital"
        weights: { digital_transformation: 3, social_software: 2, security: 2, software_requirements: 2 }
      - text: "Empreendendo com produto educacional ou social"
        weights: { gamification: 3, active_learning: 2, social_software: 2, education: 2, green_software: 1 }
---
