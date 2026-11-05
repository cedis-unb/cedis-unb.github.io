---
title: "A IA escreve. Quem garante? O novo eixo da Engenharia de Software"
date: 2026-11-05T09:00:00-03:00
draft: false
language: pt
translationKey: perspectiva_ia_novo_eixo_engenharia_software
original_language: pt
authors:
- sergio_freitas
areas:
- ai
- education
- software_quality
related_ids: []
tags: []
summary: "Um estudo de Harvard com 655 empresas mostra que a IA multiplica o código, mas não a entrega: o gargalo migrou para a revisão. O que isso muda para quem está se formando em Engenharia de Software na UnB — com apresentação e infográfico usados em sala."
featured_image: "../assets/images/perspectivas/ia-novo-eixo-engenharia-software-capa.png"
---

Brasília, 5 de novembro de 2026

Como muita gente que atua no curso de Engenharia de Software, passei os últimos dois anos com uma inquietação que não é a pergunta da moda — "a IA vai substituir o programador?" — mas uma mais concreta: **o que muda para quem está se formando agora e vai chegar ao mercado em 2027 ou 2028?** Que competências vão valer mais, quais vão valer menos e o nosso currículo está olhando para o lado certo?

Duas coisas me ajudaram a transformar a inquietação em estudo. Um artigo de pesquisa de Harvard com uma base de dados enorme e um vídeo de um engenheiro de software que vive esse problema todo dia. Cruzei os dois com o Projeto Pedagógico do Curso (PPC) de Engenharia de Software da UnB, montei uma apresentação e um infográfico e levei pra conversar com meus alunos de Compiladores. Este texto é o que eu disse a eles, com as ressalvas que a sala de aula às vezes não comporta. Os dois materiais estão públicos no fim da página.

## O estudo: muito mais código, pouco mais software

O artigo é *Artificial Intelligence in the Firm: Bottlenecks in Software Production*, de Fiona Chen e James Stratton (Harvard University). A versão que analisei é a de 28 de outubro de 2026 — um *job market paper*, portanto um manuscrito de trabalho, ainda sem revisão por pares. Isso importa, e volto a isso adiante.

A base é o que chama a atenção primeiro: cerca de **445 milhões de eventos de trabalho**, de **720.542 profissionais** em **655 empresas**, entre janeiro de 2021 e agosto de 2026, cobrindo duas gerações de ferramentas — assistentes de programação (como o GitHub Copilot) e agentes de programação (como o Claude Code). O mérito científico não está em medir quanto código a IA produz. Está em perguntar **quanto desse esforço vira resultado organizacional**.

A resposta, em números, depois de 16 meses de adoção de assistentes e 12 meses de adoção de agentes:

| Indicador | Assistentes de IA | Agentes de IA |
|---|---|---|
| Linhas de código adicionadas | +38,6% | +44,0% |
| Commits realizados | +25,5% | +36,0% |
| Pull requests abertos | +25,2% | +35,7% |
| Issues do Jira resolvidas | +2,0% | +13,7% |
| Epics do Jira concluídos | +1,7% | +18,0% |
| Emprego em Engenharia de Software | +3,1% | −2,6% |

*Fonte: Chen & Stratton (2026), seções 4.3, 4.6 e 4.7. Os efeitos dos agentes são adicionais à adoção prévia de assistentes, não uma comparação experimental direta entre ferramentas.*

Há uma distinção estatística que muda a leitura da tabela inteira: **os aumentos em commits e pull requests são significativos; os aumentos em issues e epics concluídos não alcançam significância convencional**. As estimativas de linhas de código também carregam incerteza considerável. Ou seja: o estudo demonstra com segurança que a *atividade* de programação cresceu. Que a *entrega* de software cresceu na mesma medida, não.

## O gargalo não sumiu. Mudou de lugar.

Este é, para mim, o achado central. Depois da adoção de agentes, os autores mediram:

- **+56,1%** no tempo total até a aprovação do código;
- **+59,9%** no tempo de espera por um revisor;
- **+58,5%** no tempo gasto em revisão ativa;
- **+38,6%** no número de comentários por pull request.

Os dados apontam dois mecanismos. O primeiro é **saturação**: chega mais código para revisar do que os revisores conseguem absorver, e forma-se fila. O segundo é **mais esforço por revisão**: cada alteração exige mais comentários e mais tempo, o que os autores interpretam como indício de queda na qualidade do que é submetido.

Aqui vale a cautela que repeti várias vezes em sala: **indício não é prova**. O estudo não examina o código — usa indicadores indiretos de qualidade. E não encontra aumento estatisticamente significativo de defeitos reportados no Jira depois da entrega. Uma leitura razoável é que a revisão humana está absorvendo os problemas antes que cheguem à produção. O que, convenhamos, é exatamente o papel dela — e exatamente o que a torna o novo gargalo.

## Por que "contrate mais revisores" não resolve

A primeira reação de qualquer gestor é redistribuir gente para a revisão. O artigo mostra por que isso não é trivial:

- **82,8%** das revisões são feitas por quem já conhecia a base de código;
- **75,7%** das revisões de código de engenheiros seniores são feitas por outros seniores;
- **79,1%** das empresas já usavam IA para revisar código em julho de 2026 — mas apenas **23,3%** dos comentários de revisão vinham da IA.

Revisar exige conhecer a arquitetura, as regras de negócio e o histórico do sistema. Essa capacidade não se amplia por decreto, e a IA, por ora, não a substitui. O efeito é mais forte onde a base é mais complexa: nas empresas com mais repositórios, o tempo até a integração subiu **69,7%**, contra **25,4%** nas com menos.

## E o emprego?

No período observado, **não há redução estatisticamente significativa** do número de engenheiros. Os +3,1% (assistentes) e −2,6% (agentes) da tabela são ruído. O que o artigo faz é calibrar um modelo econômico que sugere uma redistribuição do esforço: de aproximadamente **66% programação / 34% revisão** antes dos agentes para **51% / 49%** depois. São valores inferidos, não medições de tempo.

O modelo também projeta cenários para 2031 que vão de −10% a −76% no emprego, dependendo de hipóteses sobre reorganização das empresas e evolução da tecnologia. Deixei claro para os alunos: **isso não é previsão, é simulação condicional**. O cenário extremo supõe que a produtividade de programação fique 41 vezes maior que antes da IA e que a revisão acompanhe. Os próprios autores o tratam como limite superior.

## O vídeo: menos tokens, mais engenharia

O segundo material é o vídeo *O pesadelo do Code Review: IA vs. Produtividade*, de Vinícius Pasquantonio (Staff Engineer, canal pasquadev). Ele parte do mesmo estudo e da própria experiência: desenvolvedores abrindo muito mais PRs, fila de revisão travada, um chefe que fez um protótipo em dez minutos e cobra o mesmo ritmo do time. E cunha um termo que os alunos reconheceram na hora — a *ansiedade de tokens*: a pressão por volume leva o engenheiro a gerenciar vários agentes em paralelo e o custo cognitivo da troca de contexto cobra a conta.

A tese dele é que a saída não está em mais ferramentas e sim em resgatar engenharia:

1. **Planejar antes de delegar** — requisitos e arquitetura definidos antes de qualquer linha ou qualquer agente;
2. **Programação incremental** — mudanças pequenas e coesas, PRs de no máximo ~300 linhas;
3. **Contexto e testes no PR** — explicar o quê e o porquê, e cobrir os cenários antes da revisão humana;
4. **Métodos e paradigmas** — DDD e programação funcional como instrumentos de legibilidade.

Ele próprio parou de medir e divulgar linhas, commits e PRs semanais. Passou a medir se desbloqueia o time.

Uma ressalva minha: "300 linhas" é uma heurística útil, não um limite validado cientificamente.

## O que isso tem a ver com o nosso currículo

Foi aqui que o estudo virou aula. Se o eixo da profissão está se deslocando de **"escrever mais código"** para **"decidir → verificar → integrar → entregar"**, então o PPC de Engenharia de Software da UnB pode ser lido como um **mapa de responsabilidades** — e algumas disciplinas ganham uma centralidade que nem sempre o estudante enxerga no semestre em que as cursa.

Antes do código, as que decidem o que precisa existir: **Requisitos de Software** (entrevistar, esclarecer ambiguidades, definir critérios de aceitação) e **Arquitetura e Desenho de Software** (escolher estruturas, contratos, limites, e justificar decisões). Depois do código, as que demonstram que funciona: **Testes de Software**, **Qualidade de Software 1** (medir resultado, risco e retrabalho — não linhas) e **Gerência de Configuração e Evolução** (revisar PRs e integrar com segurança). Em volta delas, as catalisadoras: Fundamentos de Programação, Paradigmas, Métodos de Desenvolvimento, Interação Humano-Computador e Engenharia de Produto.

Não são matérias isoladas. São um único sistema — especificar, projetar, implementar, validar, integrar — que os Projetos Integradores, o estágio e o TCC obrigam a montar inteiro.

{{< imgc src="perspectivas/ia-novo-eixo-engenharia-software-infografico.png" alt="Infográfico: IA na Engenharia de Software — o paradoxo, o gargalo da revisão, o que muda para o profissional, disciplinas que ganham centralidade na UnB, soft skills e o futuro desejável" >}}

E há um conjunto de competências que o artigo não mede, mas que a fila de revisão expõe: pensamento crítico para questionar o que a IA propôs, comunicação técnica para explicar decisões e escrever bons PRs, colaboração para revisar e desbloquear colegas, autonomia intelectual para compreender o que foi gerado, e responsabilidade pelo que se integra. A pergunta que fechei a aula foi direta: **você aprovaria este PR gerado por IA?** Atende ao requisito real? Preserva a arquitetura? Tem evidência independente dos erros possíveis? Qual o risco se estiver errado? Quem responde pela integração é o profissional — mesmo quando o agente escreve.

## Minha leitura crítica do estudo

Três contribuições me parecem sólidas. A **distinção entre produtividade local e organizacional**: acelerar uma tarefa não acelera o processo. A **identificação de mecanismos**: o artigo não para em "a IA gera mais código"; explica por que isso não vira entrega — capacidade de revisão, especialização dos revisores, possível retrabalho. E a **hipótese de reorganização do trabalho antes do emprego**: a mudança aparece primeiro na composição do que se faz, não no número de pessoas.

As limitações também são reais. O desenho de diferenças em diferenças depende de tendências paralelas entre empresas que adotaram em momentos distintos — verificada empiricamente, mas não garantida. Os indicadores de produção final são proxies do Jira, não valor de negócio nem satisfação de usuário. A qualidade do código é inferida por comentários; o código em si não está na base. E a amostra é de empresas médias e grandes: generalizar para equipes pequenas, projetos acadêmicos ou startups pede cuidado.

## Em síntese

O estudo não diz que a IA é pouco produtiva. Diz que **os ganhos da IA são limitados pela capacidade da organização de absorvê-los** — e que, hoje, essa capacidade se chama revisão, validação e integração. Para quem está se formando, a consequência é menos assustadora do que a manchete sugere, e mais exigente: o diferencial não será a quantidade de código que você consegue gerar, será a qualidade das decisões que você consegue sustentar.

A IA escreve. O engenheiro garante.

## Materiais

- **Apresentação usada em sala** (20 slides, PDF): [A IA escreve. Quem garante? — O novo eixo da Engenharia de Software](/files/perspectivas/ia-novo-eixo-engenharia-software-apresentacao.pdf)
- **Infográfico** (PNG, alta resolução): [IA na Engenharia de Software — o novo eixo da produtividade](/files/perspectivas/ia-novo-eixo-engenharia-software-infografico.png)

## Referências

- Chen, F.; Stratton, J. *Artificial Intelligence in the Firm: Bottlenecks in Software Production*. Harvard University, manuscrito de trabalho (job market paper), versão de 28 de outubro de 2026.
- Pasquantonio, V. *O pesadelo do Code Review: IA vs. Produtividade (Harvard mediu 718 empresas)*. Canal pasquadev, 2026. [youtube.com/watch?v=BYc8W145mI4](https://www.youtube.com/watch?v=BYc8W145mI4)
- Projeto Pedagógico do Curso de Engenharia de Software — Universidade de Brasília, FCTE.
