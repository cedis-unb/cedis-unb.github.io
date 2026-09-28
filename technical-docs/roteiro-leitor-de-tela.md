# Roteiro de sessão com leitor de tela

Estado: **não executado**. Esta é a principal evidência que ainda falta na
linha de base de acessibilidade — ver `acessibilidade-linha-de-base.md` §5.

Ferramentas automatizadas cobrem cerca de um terço dos critérios da WCAG, e só
a parte decidível por máquina. Ordem de leitura, nome anunciado, estado de
componentes e retorno de foco só se verificam ouvindo. Nada nas páginas
públicas do site afirma que este teste foi feito, e não deve afirmar até que
esta tabela esteja preenchida.

## Como executar

Uma sessão de 45 a 60 minutos basta para a primeira rodada.

- **macOS/VoiceOver**: `Cmd+F5` liga. `Ctrl+Option+seta` navega; `Ctrl+Option+U`
  abre o rotor (cabeçalhos, links, marcos); `Ctrl+Option+Espaço` ativa.
- **Windows/NVDA**: `Insert+seta` navega; `H` pula cabeçalhos; `D` pula marcos;
  `Insert+F7` lista elementos.
- Faça em **um idioma por vez** e repita o essencial no outro: o site é
  bilíngue e o atributo `lang` muda a pronúncia.
- Teste com o **tema claro e o escuro** apenas onde o estado for anunciado
  (o leitor não vê cor, mas componentes podem mudar de rótulo).

## O que percorrer

| # | Página | Fluxo | O que precisa ser verdade |
| --- | --- | --- | --- |
| 1 | `/pt/` e `/` | Entrar na página | O `lang` correto é anunciado; o skip link é o primeiro foco e leva ao conteúdo |
| 2 | qualquer | Menu principal | Cada gatilho anuncia nome + "recolhido/expandido"; Enter abre; Esc fecha e devolve o foco ao gatilho |
| 3 | < 1024px | Menu hambúrguer | O botão anuncia a ação (não só "Main"); o painel é alcançável; Esc devolve o foco |
| 4 | `/pt/mapa/` | Mapa de competências | O grupo é anunciado com o rótulo; cada nó anuncia tipo + nome + nº de conexões; Enter e Espaço ativam; a lista de links equivalente é alcançável e faz sentido sozinha |
| 5 | `/pt/people/sergio_freitas/` | Perfil | Ordem de leitura coerente; "Orientações anteriores" é anunciado como botão com estado; ao expandir, o conteúdo entra na ordem |
| 6 | `/pt/publications/` | Filtros | Cada `select` anuncia o próprio rótulo; mudar o filtro comunica que a lista mudou |
| 7 | `/pt/defesas/` | Alternador calendário/lista | Anuncia-se como aba, com o estado selecionado; o painel correspondente é encontrado |
| 8 | `/pt/oportunidades/` | Estado vazio e arquivo | Os dois cabeçalhos de seção são encontrados pelo rotor; o estado vazio é lido |
| 9 | `/pt/contact/` | Contato | Endereço, e-mail e links institucionais são lidos na ordem; os links dizem para onde vão |
| 10 | `/pt/junte-se/mestrado/` | Trilha | "Para quem é" e "Duração" são lidos como par rótulo/valor; os dois CTAs anunciam destino |
| 11 | qualquer | Trilha de navegação | Anunciada como navegação; o item atual é identificado como atual |
| 12 | `/pt/` | Cards e listagens | Cada card tem um nome acionável; nada é anunciado como "link" sem texto |

## Registro

Preencher e datar. Sem isto, a página pública continua dizendo, corretamente,
que nenhuma sessão foi registrada.

| # | Resultado | Observação |
| --- | --- | --- |
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |
| 10 | | |
| 11 | | |
| 12 | | |

Leitor e versão usados: ______   Sistema: ______   Data: ______   Quem executou: ______

## Depois

1. Abrir uma correção por defeito encontrado, com o item do roteiro no título.
2. Atualizar `acessibilidade-linha-de-base.md` §5 com o resumo e a data.
3. Atualizar `content/accessibility.{pt,en}.md`: a frase "nenhuma sessão de
   leitor de tela está registrada" só sai quando esta tabela estiver preenchida,
   e deve ser trocada pelo que foi de fato coberto — não por uma declaração
   genérica de conformidade.
