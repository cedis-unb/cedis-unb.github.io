---
title: Interpretação automatizada de textos - processamento de anáforas
date: '2005-01-01T00:00:00-03:00'
draft: false
language: pt
translationKey: publication_2005_sergio_antonio_andrade_de_freitas_interpretacao_automatizada_de_textos_processamento
generated_by: scripts/build_publications.py
canonical_source: data/productions.yaml
id: publication_2005_sergio_antonio_andrade_de_freitas_interpretacao_automatizada_de_textos_processamento
publication_index: 219
publication_group: thesis
publication_type: phd
schema_type: Thesis
year: 2005
authors:
- Sergio Antônio Andrade de Freitas
authors_structured:
- name: Sergio Antônio Andrade de Freitas
  id: sergio_freitas
  url: /people/sergio_freitas
tags:
- nlp
- ai
advisors: []
doi_isbn: ''
source_title: ''
publisher: Biblioteca Central da Universidade Federal do Espirito Santo
location: ''
pages: ''
volume: ''
external_url: https://repositorio.ufes.br/items/0a851464-4e72-46fa-9dde-5b1995f16a91
spotify_podcast: ''
github_repo: ''
zenodo_record: ''
summary: Esta tese apresenta uma solução para a interpretação de anáforas nominais
  definidas.Considere o seguinte texto- (1) a. Mariana comprou um carro novo. b. O
  motor veio danificado. A frase (1a) apresenta duas entidades- Mariana e um carro
  novo. Já a frase (1.2b) tem apenas uma entidade o motor. No processo de interpretação,
  humano ou computacional, a utilização do artigo de nido o é um indicativo de que
  a entidade já havia sido introduzida no discurso, i.e. apresenta um caráter anafórico.
  Resolver uma anáfora é, a priori, identicar a quem ou a que se refere esta anáfora.
  Mas no caso acima é mais do que isto sem dúvida o motor existe no texto por causa
  da existência de um carro, porém a interpretação do motor deve ir além disto e identi
  car como este motor está ligado com aquele carro. Isto é uma anáfora nominal de
  nida. A interpretação das anáforas nominais de nidas ou de qualquer fenômeno anafórico
  pode ser generalizada como um processo que atribui valores aos itens da seguinte
  equação- R(A, T ) (2) onde- A denota a entidade introduzida pela interpretação fora
  de contexto de um pronome, de uma elipse ou de um sintagma nominal de nido, T denota
  o seu antecedente e R é a relação existente entre A e T . O processo de resolução
  da equação, que é propriamente o processo de resolução de anáforas, consiste em
  descobrir T e R dado A. Nesta tese é proposta uma metodologia computacional que
  interpreta as anáforas nominais de nidas cuja relação R é uma dentre - parte de,
  membro de, subcategorizado por e coreferência. A obtenção das relações é feita por
  um conjunto de regras pragmáticas [Freitas, Lopes e Menezes 2004, Filho e Freitas
  2003] (cap. 3). Caso seja constatado que A não seja anafórica então ela é acomodada
  no contexto. A metodologia computacional é construída sobre um ambiente de programação
  em lógica [Damásio, Nejdl e Pereira 1994] que permite raciocinar abdutivamente [Kakas,
  Kowalski e Toni 1992] sobre a representação semântica do texto [Kamp e Reyle 1993].
  A partir da interpretação das entidades é construída a estrutura nominal do discurso
  [Lopes e Freitas 1994] (cap. 4), a qual permite - (1) fazer o acompanhamento das
  entidades mais salientes em cada frase [Freitas e Lopes 1994], (2) limitar o universo
  de escolha de possíveis antecedentes[Freitas e Lopes 1996] e (3) prover um resumo
  das entidades do discurso. O resultado é uma metodologia que permite, de forma integrada,
  resolver anáforas e elipses, sendo que a estrutura nominal do discurso pode ser
  usada na busca de informações.
bibtex: "@phdthesis{2005-sergio-antonio-andrade-de-freitas-interpretacao-automatizada-de-textos-processamento,\n\
  \  author = {Sergio Antônio Andrade de Freitas},\n  title = {Interpretação automatizada\
  \ de textos - processamento de anáforas},\n  year = {2005},\n  publisher = {Biblioteca\
  \ Central da Universidade Federal do Espirito Santo}\n}"
aliases:
- /publications/2005-sergio-antonio-andrade-de-freitas-interpretacao-automatizada-de-textos-processamento/
---
## Resumo

Esta tese apresenta uma solução para a interpretação de anáforas nominais definidas.Considere o seguinte texto- (1) a. Mariana comprou um carro novo. b. O motor veio danificado. A frase (1a) apresenta duas entidades- Mariana e um carro novo. Já a frase (1.2b) tem apenas uma entidade o motor. No processo de interpretação, humano ou computacional, a utilização do artigo de nido o é um indicativo de que a entidade já havia sido introduzida no discurso, i.e. apresenta um caráter anafórico. Resolver uma anáfora é, a priori, identicar a quem ou a que se refere esta anáfora. Mas no caso acima é mais do que isto sem dúvida o motor existe no texto por causa da existência de um carro, porém a interpretação do motor deve ir além disto e identi car como este motor está ligado com aquele carro. Isto é uma anáfora nominal de nida. A interpretação das anáforas nominais de nidas ou de qualquer fenômeno anafórico pode ser generalizada como um processo que atribui valores aos itens da seguinte equação- R(A, T ) (2) onde- A denota a entidade introduzida pela interpretação fora de contexto de um pronome, de uma elipse ou de um sintagma nominal de nido, T denota o seu antecedente e R é a relação existente entre A e T . O processo de resolução da equação, que é propriamente o processo de resolução de anáforas, consiste em descobrir T e R dado A. Nesta tese é proposta uma metodologia computacional que interpreta as anáforas nominais de nidas cuja relação R é uma dentre - parte de, membro de, subcategorizado por e coreferência. A obtenção das relações é feita por um conjunto de regras pragmáticas [Freitas, Lopes e Menezes 2004, Filho e Freitas 2003] (cap. 3). Caso seja constatado que A não seja anafórica então ela é acomodada no contexto. A metodologia computacional é construída sobre um ambiente de programação em lógica [Damásio, Nejdl e Pereira 1994] que permite raciocinar abdutivamente [Kakas, Kowalski e Toni 1992] sobre a representação semântica do texto [Kamp e Reyle 1993]. A partir da interpretação das entidades é construída a estrutura nominal do discurso [Lopes e Freitas 1994] (cap. 4), a qual permite - (1) fazer o acompanhamento das entidades mais salientes em cada frase [Freitas e Lopes 1994], (2) limitar o universo de escolha de possíveis antecedentes[Freitas e Lopes 1996] e (3) prover um resumo das entidades do discurso. O resultado é uma metodologia que permite, de forma integrada, resolver anáforas e elipses, sendo que a estrutura nominal do discurso pode ser usada na busca de informações.
