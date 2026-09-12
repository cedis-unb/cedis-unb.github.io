---
# Uso: hugo new opportunities/<slug>.pt.md  (e o par .en.md)
# Ajuste `language`, `deadline`, `audience`, `project` e `responsible`.
# Com status: open e deadline futuro, a chamada aparece em /oportunidades/,
# no pulse da capa e na trilha Extensão de Junte-se; após o prazo vira arquivo.
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: false
language: pt
translationKey: opportunity_{{ replace .Name "-" "_" }}
id: {{ replace .Name "-" "_" }}
status: open
deadline: {{ ((time .Date).AddDate 0 1 0) | time.Format "2006-01-02" }}
audience:
- tcc
- iniciacao
- voluntario
project: ""
responsible:
- sergio_freitas
source: ""
summary: ""
---
Descreva a chamada: objetivo, vagas, requisitos, como se inscrever e contato.

## Público

- 

## Inscrição

- 
