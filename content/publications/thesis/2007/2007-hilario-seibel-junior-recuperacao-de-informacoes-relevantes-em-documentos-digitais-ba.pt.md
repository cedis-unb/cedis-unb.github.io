---
title: Recuperação de informações relevantes em documentos digitais baseada na resolução
  de anáforas
date: '2007-01-01T00:00:00-03:00'
draft: false
language: pt
translationKey: publication_2007_hilario_seibel_junior_recuperacao_de_informacoes_relevantes_em_documentos_digitais_ba
generated_by: scripts/build_publications.py
canonical_source: data/productions.yaml
id: publication_2007_hilario_seibel_junior_recuperacao_de_informacoes_relevantes_em_documentos_digitais_ba
publication_index: 217
publication_group: thesis
publication_type: dissertation
schema_type: Thesis
year: 2007
authors:
- Hilário Seibel Júnior
authors_structured:
- name: Hilário Seibel Júnior
  id: seibel_hilario
  url: /people/seibel_hilario
tags:
- nlp
- ai
advisors:
- sergio_freitas
doi_isbn: ''
source_title: ''
publisher: Biblioteca Central da Universidade Federal do Espirito Santo
location: ''
pages: ''
volume: ''
external_url: http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=104831
spotify_podcast: ''
github_repo: ''
zenodo_record: ''
summary: Os métodos de recuperação de informação (RI) tradicionais se baseiam essencialmente
  na contagem da freqüência em que as palavras aparecem em um documento; sem apresentar
  soluções para que o conteúdo semântico do discurso seja interpretado [Van Rijsbergen
  1979; Baeza-Yates e Ribeiro-Neto 1999]. Por não interpretarem o documento analisado;
  tais métodos podem deixar de considerar informações importantes a seu respeito.
  Uma solução para contornar esse problema; citada em [Salton e McGill 1986]; é utilizar
  o Processamento de Linguagem Natural (PLN) na recuperação de informação. Uma aplicação
  do PLN é o processamento de anáforas. Anáfora [Carter 1987; Beaver 2004] é um fenômeno
  lingüístico no qual uma entidade introduzida a priori é referenciada posteriormente
  em outra frase através de alguma expressão lingüística; tal como em "Valentina nasceu
  em São Paulo. A menina é do signo de Peixes.". A resolução das anáforas identifica
  que o termo menina presente na segunda frase do texto referencia a entidade introduzida
  no discurso pelo termo Valentina da primeira frase. Isso permite afirmar que Valentina
  é mais relevante em relação ao texto do que se tal referência não ocorresse. Freitas
  propõe em [Freitas 2005] um método para resolver as anáforas de um documento através
  da criação de uma estrutura que permite acompanhar as entidades que se mantêm em
  evidência ao longo do discurso. Essa estrutura armazena informações que podem ser
  aproveitadas por um método de recuperação de informação. Esta dissertação propõe
  uma metodologia computacional para recuperar informações relevantes a partir da
  resolução das anáforas de um documento; visando aumentar a qualidade dos resultados
  de uma query. A resolução de anáforas permite identificar exatamente a quantidade
  de vezes que cada entidade é referenciada em um discurso; expondo entidades e ligações
  que podiam estar obscuras no discurso original. Essa informação torna possível decidir
  se certa entidade é mais relevante que outra no documento; dando mais enfoque ao
  que o autor escreveu. Dessa forma; os documentos relevantes recuperados são classificados
  pela quantidade de informação que apresentam a respeito dos termos buscados; e não
  apenas pela localização e/ou quantidade de ocorrências de tais termos. Este trabalho
  também permite identificar; através da estrutura gerada pelo processamento de anáforas;
  os termos sinônimos (aqueles que referenciam uma mesma entidade). Se o documento
  indica que dois termos são sinônimos; a busca por um deles retorna o mesmo resultado
  que a busca pelo outro; aumentando ainda mais a qualidade dos resultados de uma
  query. Este trabalho apresenta os detalhes da metodologia proposta - as medidas
  utilizadas para calcular a relevância de um termo em relação ao documento interpretado
  pelo processamento de anáforas; os procedimentos necessários para a realização de
  uma query; o protótipo implementado e a análise de sua complexidade de tempo. Além
  disso; são avaliadas as características desta abordagem que a diferenciam dos métodos
  tradicionais em relação à qualidade dos resultados obtidos.
bibtex: "@mastersthesis{2007-hilario-seibel-junior-recuperacao-de-informacoes-relevantes-em-documentos-digitais-ba,\n\
  \  author = {Hilário Seibel Júnior},\n  title = {Recuperação de informações relevantes\
  \ em documentos digitais baseada na resolução de anáforas},\n  year = {2007},\n\
  \  publisher = {Biblioteca Central da Universidade Federal do Espirito Santo}\n}"
aliases:
- /publications/2007-hilario-seibel-junior-recuperacao-de-informacoes-relevantes-em-documentos-digitais-ba/
---
## Resumo

Os métodos de recuperação de informação (RI) tradicionais se baseiam essencialmente na contagem da freqüência em que as palavras aparecem em um documento; sem apresentar soluções para que o conteúdo semântico do discurso seja interpretado [Van Rijsbergen 1979; Baeza-Yates e Ribeiro-Neto 1999]. Por não interpretarem o documento analisado; tais métodos podem deixar de considerar informações importantes a seu respeito. Uma solução para contornar esse problema; citada em [Salton e McGill 1986]; é utilizar o Processamento de Linguagem Natural (PLN) na recuperação de informação. Uma aplicação do PLN é o processamento de anáforas. Anáfora [Carter 1987; Beaver 2004] é um fenômeno lingüístico no qual uma entidade introduzida a priori é referenciada posteriormente em outra frase através de alguma expressão lingüística; tal como em "Valentina nasceu em São Paulo. A menina é do signo de Peixes.". A resolução das anáforas identifica que o termo menina presente na segunda frase do texto referencia a entidade introduzida no discurso pelo termo Valentina da primeira frase. Isso permite afirmar que Valentina é mais relevante em relação ao texto do que se tal referência não ocorresse. Freitas propõe em [Freitas 2005] um método para resolver as anáforas de um documento através da criação de uma estrutura que permite acompanhar as entidades que se mantêm em evidência ao longo do discurso. Essa estrutura armazena informações que podem ser aproveitadas por um método de recuperação de informação. Esta dissertação propõe uma metodologia computacional para recuperar informações relevantes a partir da resolução das anáforas de um documento; visando aumentar a qualidade dos resultados de uma query. A resolução de anáforas permite identificar exatamente a quantidade de vezes que cada entidade é referenciada em um discurso; expondo entidades e ligações que podiam estar obscuras no discurso original. Essa informação torna possível decidir se certa entidade é mais relevante que outra no documento; dando mais enfoque ao que o autor escreveu. Dessa forma; os documentos relevantes recuperados são classificados pela quantidade de informação que apresentam a respeito dos termos buscados; e não apenas pela localização e/ou quantidade de ocorrências de tais termos. Este trabalho também permite identificar; através da estrutura gerada pelo processamento de anáforas; os termos sinônimos (aqueles que referenciam uma mesma entidade). Se o documento indica que dois termos são sinônimos; a busca por um deles retorna o mesmo resultado que a busca pelo outro; aumentando ainda mais a qualidade dos resultados de uma query. Este trabalho apresenta os detalhes da metodologia proposta - as medidas utilizadas para calcular a relevância de um termo em relação ao documento interpretado pelo processamento de anáforas; os procedimentos necessários para a realização de uma query; o protótipo implementado e a análise de sua complexidade de tempo. Além disso; são avaliadas as características desta abordagem que a diferenciam dos métodos tradicionais em relação à qualidade dos resultados obtidos.
