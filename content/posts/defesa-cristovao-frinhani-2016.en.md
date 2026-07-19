---
title: "Before the generative AI boom, an undergraduate thesis was already teaching machines to grade essays"
date: 2016-07-01T00:00:00-03:00
draft: false
weight: 500
language: en
featured_image: "../assets/images/featured/area_IA.png"
summary: 'Back in 2016, well before the LLM frenzy, Cristóvão Frinhani defended at FCTE/UnB an undergraduate thesis that uses semantic similarity and machine learning to support distance-learning tutors grading essay questions.'
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
Brasília, July 1, 2016

What today feels almost trivial in the face of any modern chatbot was, a decade ago, an open problem: teaching a computer to judge whether an essay-style answer is close to or far from a reference answer. **This was the challenge tackled by Cristóvão de Lima Frinhani in his undergraduate thesis in Software Engineering at FCTE/UnB**, defended in July 2016 under the advising of Prof. {{< link-interno "/people/sergio_freitas" "Sergio Antônio Andrade de Freitas" >}} and the co-advising of Prof. Mauricio Vidotti Fernandes.

The motivation is tightly bound to a real bottleneck in distance education: a modality that grew rapidly in Brazil while struggling with time and cost of grading essay questions. The system proposed by the author works on two fronts. First, semantic similarity between the student’s answer and the tutor-provided reference is used to produce a preliminary grade. Then, a machine learning component refines that grade based on tutor feedback — every human correction adjusts the model so that subsequent errors shrink.

The idea is elegant because it combines {{< link-interno "/areas/ai_pln/" "natural language processing" >}} with a supervised learning loop that dampens the imperfections of similarity algorithms. To test the system, the author ran experiments using content from a Computer Architecture Fundamentals course, comparing machine-generated grades against manually assigned ones.

The thesis was advised inside the research line on {{< link-interno "/areas/active_learning/" "active learning" >}} and educational technologies that has long marked Prof. Sergio Freitas’s work at CEDIS, and anticipates — in an academic setting — questions the community would revisit with force after 2022 as large language models became mainstream: how to calibrate automated assessments in contexts where errors are pedagogically costly.

The research also led to two papers with Cristóvão among the authors: [_An automatic essay correction for an active learning environment_](https://doi.org/10.1109/AICCSA.2016.7945769), published in 2016, and [_Evaluation of an Automatic Essay Correction System Used as an Assessment Tool_](https://doi.org/10.1007/978-3-319-58700-4_18), published in the proceedings of the 19th International Conference on Human-Computer Interaction in 2017. The papers bring the automatic-grading proposal into scientific article form.

The work, defended at the FCTE/UnB and written in Portuguese, is available at the [UnB Undergraduate Theses Digital Library](https://bdm.unb.br/handle/10483/14871).

---

About CEDIS:
The Center for Studies, Development, and Innovation in Software (CEDIS), linked to the University of Brasília, researches and develops innovative software solutions with strong presence in {{< link-interno "/areas/ai_pln/" "AI and Natural Language Processing" >}}.
