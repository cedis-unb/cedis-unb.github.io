---
title: "Who wrote that commit? An undergraduate thesis computes authorship rates inside Git projects"
date: 2018-12-11T00:00:00-03:00
draft: false
weight: 500
language: en
featured_image: "../assets/images/featured/area_Arquitetura de Software.png"
summary: 'Laércio Silva de Sousa Júnior defended at FCTE/UnB an undergraduate thesis investigating ways to compute developer authorship rates inside Git-versioned projects.'
author: CEDIS
authorimage: ../assets/images/global/author.webp
categories:
- News
tags:
- News
- defesa
- software_architecture
- digital_transformation
---
Brasília, December 11, 2018

Counting lines of code added by each developer sounds trivial. But any medium-sized project turns the sum into a trap: refactors shift apparent authorship, merges rewrite responsibilities, and a strong developer may remove more code than they produce. **This is the puzzle Laércio Silva de Sousa Júnior dedicates his thesis to**, defended in December 2018 at FCTE/UnB under the advising of Prof. {{< link-interno "/people/andre_lanna" "André Luiz Peron Martins Lanna" >}}.

The work starts from a naive metric — the *diff* as a proxy for effort — and shows why it produces distorted portraits of real teams. The proposal replaces the raw sum with a context-sensitive authorship rate computed from Git history: code that survives, meaningful refactors, participation in critical blocks. The outcome is a more honest reading of contribution, useful both for team retrospectives and for {{< link-interno "/areas/software_architecture/" "architectural analysis" >}} and {{< link-interno "/areas/transformation/" "code governance" >}} instruments.

The full text — written in Portuguese — is available at the [UnB Undergraduate Theses Digital Library](https://www.bdm.unb.br/handle/10483/23055).

---

About CEDIS:
The Center for Studies, Development, and Innovation in Software (CEDIS), linked to the University of Brasília, researches and develops innovative software solutions.
