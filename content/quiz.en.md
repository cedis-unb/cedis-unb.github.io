---
title: "Which CEDIS area fits you?"
date: 2026-07-17T00:00:00-03:00
draft: false
language: en
url: /quiz/
layout: quiz
description: "5 quick questions to discover which CEDIS area and researchers align best with your profile."
featured_image: "../assets/images/pages/media-CEDIS.png"
eyebrow: "Guided discovery"
questions:
  - id: q1
    text: "Which problem excites you most?"
    options:
      - text: "Teach better, measure learning, design educational experiences"
        weights: { active_learning: 3, gamification: 3, learning_analytics: 3, education: 3 }
      - text: "Build more robust, testable, and secure software"
        weights: { software_quality: 3, verification_validation_testing: 3, security: 2, software_architecture: 2 }
      - text: "Apply AI, NLP, and data to real-world problems"
        weights: { ai: 3, machine_learning: 3, nlp: 2, learning_analytics: 2 }
      - text: "Social impact — digital government, NGOs, public policy"
        weights: { social_software: 3, digital_transformation: 3, education: 2, software_requirements: 1 }
      - text: "Critical infrastructure, performance, scale"
        weights: { hpc: 3, software_architecture: 2, security: 2 }

  - id: q2
    text: "How would you describe yourself?"
    options:
      - text: "Excited by working with people and teams"
        weights: { soft_skills: 3, teamwork: 3, active_learning: 2, education: 2, software_requirements: 1 }
      - text: "Detail-oriented, love analysis and rigorous proof"
        weights: { verification_validation_testing: 3, software_quality: 2, software_architecture: 2 }
      - text: "Curious about hidden patterns in data"
        weights: { machine_learning: 3, ai: 2, learning_analytics: 3, nlp: 2 }
      - text: "Builder — I want things to work"
        weights: { software_architecture: 3, software_product_line: 2, software_quality: 2, digital_transformation: 2 }
      - text: "Strategic — understand context before deciding"
        weights: { software_requirements: 3, digital_transformation: 2, social_software: 2 }

  - id: q3
    text: "Which of these topics lights you up?"
    options:
      - text: "Chatbots, transformers, applied NLP"
        weights: { nlp: 3, ai: 3, machine_learning: 2 }
      - text: "Educational games, motivation, engagement"
        weights: { gamification: 3, active_learning: 2, learning_analytics: 2, education: 2 }
      - text: "Production systems with many users"
        weights: { software_architecture: 3, software_quality: 2, software_product_line: 2, digital_transformation: 1 }
      - text: "Information security, cryptography, defense"
        weights: { security: 3, software_architecture: 1, verification_validation_testing: 1 }
      - text: "Environmental impact of software (Green SD)"
        weights: { green_software: 3, software_quality: 2 }
      - text: "High performance, GPU, parallelism"
        weights: { hpc: 3 }

  - id: q4
    text: "What kind of outcome feels most rewarding?"
    options:
      - text: "Watching someone learn better because of what I built"
        weights: { active_learning: 3, education: 3, gamification: 2, learning_analytics: 2 }
      - text: "A rigorous scientific paper in a good venue"
        weights: { verification_validation_testing: 3, software_architecture: 2, software_requirements: 2, machine_learning: 1 }
      - text: "A system others use and recommend"
        weights: { software_architecture: 3, digital_transformation: 3, software_product_line: 2, software_quality: 2 }
      - text: "A model/algorithm that solves a specific problem"
        weights: { machine_learning: 3, ai: 3, nlp: 2, hpc: 2 }
      - text: "A methodology that changes how teams work"
        weights: { soft_skills: 3, teamwork: 3, software_requirements: 2, active_learning: 2 }

  - id: q5
    text: "Where do you see yourself in 3-4 years?"
    options:
      - text: "Researching or teaching at a university"
        weights: { active_learning: 2, education: 3, learning_analytics: 2, software_requirements: 1, verification_validation_testing: 1, ai: 1 }
      - text: "At a product company — senior dev / tech lead"
        weights: { software_architecture: 3, software_quality: 3, software_product_line: 2, software_requirements: 2 }
      - text: "At an AI/data startup or consultancy"
        weights: { machine_learning: 3, ai: 3, nlp: 2, digital_transformation: 2 }
      - text: "Serving the public sector / digital transformation"
        weights: { digital_transformation: 3, social_software: 2, security: 2, software_requirements: 2 }
      - text: "Entrepreneuring with an educational or social product"
        weights: { gamification: 3, active_learning: 2, social_software: 2, education: 2, green_software: 1 }
---
