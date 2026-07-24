---
title: Retrieval of relevant information in digital documents based on anaphora resolution
date: '2007-01-01T00:00:00-03:00'
draft: false
language: en
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
summary: Traditional Information Retrieval (IR) methods are primarily based on counting
  the frequency of word occurrences in a document, without offering solutions for
  interpreting the semantic content of the discourse [Van Rijsbergen 1979; Baeza-Yates
  and Ribeiro-Neto 1999]. By not interpreting the analyzed document, such methods
  may overlook important information about it. A solution to overcome this issue,
  mentioned in [Salton and McGill 1986], is to use Natural Language Processing (NLP)
  in information retrieval. One application of NLP is the processing of anaphoras.
  Anaphora [Carter 1987; Beaver 2004] is a linguistic phenomenon where an entity introduced
  a priori is referenced later in another sentence through some linguistic expression,
  as in "Valentina was born in São Paulo. The girl is a Pisces." Anaphora resolution
  identifies that the term "girl" in the second sentence references the entity introduced
  in the discourse by the term "Valentina" from the first sentence. This allows us
  to assert that Valentina is more relevant to the text than if such reference had
  not occurred. Freitas proposes in [Freitas 2005] a method to resolve anaphoras in
  a document by creating a structure that allows tracking entities that remain prominent
  throughout the discourse. This structure stores information that can be leveraged
  by an information retrieval method. This dissertation proposes a computational methodology
  to retrieve relevant information from the resolution of anaphoras in a document,
  aiming to improve the quality of query results. Anaphora resolution enables precise
  identification of the number of times each entity is referenced in a discourse,
  revealing entities and connections that may have been obscured in the original discourse.
  This information makes it possible to decide whether a certain entity is more relevant
  than another in the document, focusing more on what the author wrote. Thus, the
  relevant documents retrieved are ranked by the amount of information they present
  regarding the searched terms, and not merely by the location and/or number of occurrences
  of such terms. This work also allows identifying, through the structure generated
  by anaphora processing, synonymous terms (those that reference the same entity).
  If the document indicates that two terms are synonymous, searching for one will
  return the same result as searching for the other, further increasing the quality
  of query results. This work presents the details of the proposed methodology - the
  measures used to calculate the relevance of a term in relation to the document interpreted
  through anaphora processing, the procedures necessary for conducting a query, the
  implemented prototype, and the analysis of its time complexity. Furthermore, the
  characteristics of this approach that differentiate it from traditional methods
  regarding the quality of the obtained results are evaluated.
bibtex: "@mastersthesis{2007-hilario-seibel-junior-recuperacao-de-informacoes-relevantes-em-documentos-digitais-ba,\n\
  \  author = {Hilário Seibel Júnior},\n  title = {Retrieval of relevant information\
  \ in digital documents based on anaphora resolution},\n  year = {2007},\n  publisher\
  \ = {Biblioteca Central da Universidade Federal do Espirito Santo}\n}"
aliases:
- /publications/2007-hilario-seibel-junior-recuperacao-de-informacoes-relevantes-em-documentos-digitais-ba/
---
## Abstract

Traditional Information Retrieval (IR) methods are primarily based on counting the frequency of word occurrences in a document, without offering solutions for interpreting the semantic content of the discourse [Van Rijsbergen 1979; Baeza-Yates and Ribeiro-Neto 1999]. By not interpreting the analyzed document, such methods may overlook important information about it. A solution to overcome this issue, mentioned in [Salton and McGill 1986], is to use Natural Language Processing (NLP) in information retrieval. One application of NLP is the processing of anaphoras. Anaphora [Carter 1987; Beaver 2004] is a linguistic phenomenon where an entity introduced a priori is referenced later in another sentence through some linguistic expression, as in "Valentina was born in São Paulo. The girl is a Pisces." Anaphora resolution identifies that the term "girl" in the second sentence references the entity introduced in the discourse by the term "Valentina" from the first sentence. This allows us to assert that Valentina is more relevant to the text than if such reference had not occurred. Freitas proposes in [Freitas 2005] a method to resolve anaphoras in a document by creating a structure that allows tracking entities that remain prominent throughout the discourse. This structure stores information that can be leveraged by an information retrieval method. This dissertation proposes a computational methodology to retrieve relevant information from the resolution of anaphoras in a document, aiming to improve the quality of query results. Anaphora resolution enables precise identification of the number of times each entity is referenced in a discourse, revealing entities and connections that may have been obscured in the original discourse. This information makes it possible to decide whether a certain entity is more relevant than another in the document, focusing more on what the author wrote. Thus, the relevant documents retrieved are ranked by the amount of information they present regarding the searched terms, and not merely by the location and/or number of occurrences of such terms. This work also allows identifying, through the structure generated by anaphora processing, synonymous terms (those that reference the same entity). If the document indicates that two terms are synonymous, searching for one will return the same result as searching for the other, further increasing the quality of query results. This work presents the details of the proposed methodology - the measures used to calculate the relevance of a term in relation to the document interpreted through anaphora processing, the procedures necessary for conducting a query, the implemented prototype, and the analysis of its time complexity. Furthermore, the characteristics of this approach that differentiate it from traditional methods regarding the quality of the obtained results are evaluated.
