# Formulário MS Forms — Defesas CEDIS

Guia de referência para construir um formulário MS Forms que permita aos pesquisadores CEDIS **inserir, alterar ou excluir defesas** no `data/defesas.yaml`.

- **Público:** 7 docentes CEDIS (`sergio_freitas`, `cristiane_ramos`, `andre_lanna`, `george_marsicano`, `ricardo_ajax`, `daniel_sundfeld`, `fabiana_mendes`).
- **Fluxo esperado:** professor preenche form → resposta cai numa planilha Excel/OneDrive → script Python lê a planilha → gera diff em `data/defesas.yaml` → PR ou commit direto.
- **Escopo:** apenas defesas 2008+, feitas por pesquisadores CEDIS, dentro da UnB (FGA/FCTE, PPCA, CIC ou outros programas UnB).

---

## 1. Considerações sobre MS Forms

**O que MS Forms suporta bem:**
- Perguntas de escolha (radio, checkbox, dropdown), texto (curto/longo), data, número, upload.
- Seções (sections) com quebras de página.
- **Branching** (ramificação): próxima pergunta depende da anterior.
- Autenticação institucional (captura automática do e-mail do respondente logado).
- Export para Excel/OneDrive automático.

**Limitações que forçam decisões:**
- **Não tem "repeating groups"** (arrays dinâmicos). Banca com N membros vira N perguntas fixas (repetir até um limite, ex.: 5 membros).
- **Não tem dropdown dinâmico** (com dados vindos de outra fonte). Lista de orientadores/programas fica hardcoded no form.
- **Não tem validação server-side** (só regex simples e ranges). Slug único, referências cruzadas, etc. ficam no script Python que processa a planilha.
- **Não tem "editar resposta anterior"** — para alterar/excluir uma defesa, o professor reenvia com uma coluna "Ação".

---

## 2. Estrutura geral do formulário

Divido em **7 seções**, algumas condicionais.

| # | Seção | Sempre exibida? |
|---|---|---|
| 1 | Introdução + Ação | Sim |
| 2 | Identificação da defesa | Sim (obrigatório informar o ID nas ações de alterar/excluir) |
| 3 | Dados do trabalho | Ação = inserir ou alterar |
| 4 | Aluno(s) | Ação = inserir ou alterar |
| 5 | Orientação | Ação = inserir ou alterar |
| 6 | Banca (membros 1 a 5) | Ação = inserir ou alterar |
| 7 | Local, agenda e vínculos | Ação = inserir ou alterar |
| 8 | Confirmação | Sim |

---

## 3. Seção 1 — Introdução e ação

### 1.1 Introdução (texto de instrução, não pergunta)

```
Este formulário atualiza o banco de defesas do CEDIS (data/defesas.yaml).
Você (pesquisador CEDIS logado) pode:
  • INSERIR uma defesa nova (marcada, realizada ou depositada)
  • ALTERAR uma defesa existente (correções, adição de banca, novo campo)
  • EXCLUIR uma defesa (cancelamento, duplicidade, erro de cadastro)

As mudanças passam por revisão antes de aparecer no site.
Responder este formulário não modifica o site imediatamente.
```

### 1.2 Ação a executar

- **Tipo:** Choice (radio, obrigatória).
- **Opções:**
  - `Inserir nova defesa`
  - `Alterar defesa existente`
  - `Excluir defesa`
- **Branching:** determina se seções 3-7 são exibidas.
- **Mapping YAML:** interna; controla o processamento pelo script (não vira campo do YAML).

### 1.3 Seu papel na defesa

- **Tipo:** Choice (radio, obrigatória).
- **Opções:**
  - `Sou o orientador principal`
  - `Sou co-orientador`
  - `Sou membro externo da banca` (informativo — geralmente não é o caso porque só CEDIS acessa o form)
  - `Estou registrando defesa de outro pesquisador CEDIS (com autorização)`
- **Mapping YAML:** interna, para auditoria.

---

## 4. Seção 2 — Identificação da defesa

### 2.1 ID da defesa (apenas em Alterar/Excluir)

- **Tipo:** Text (curto), obrigatória se ação ≠ inserir.
- **Placeholder:** `ex.: emanuel-oliveira-2025-12-03`
- **Instrução:**
  ```
  ID exibido no rodapé da página /defesas/<id>/ ou no arquivo YAML.
  Se não souber, deixe em branco e informe abaixo os dados que permitam encontrar.
  ```
- **Mapping YAML:** `.id` (chave primária).

### 2.2 Se não souber o ID (fallback)

- **Tipo:** Text (longo), opcional.
- **Instrução:**
  ```
  Cole aqui informações que ajudem a encontrar a defesa:
  nome completo do aluno, data aproximada, título parcial.
  ```
- **Mapping:** processado manualmente pelo script/revisor.

---

## 5. Seção 3 — Dados do trabalho

### 3.1 Tipo de trabalho

- **Tipo:** Choice (radio, obrigatória).
- **Opções (rótulos claros):**
  - `TCC1 (proposta de TCC)`
  - `TCC (final, TCC2)`
  - `Qualificação de mestrado`
  - `Dissertação de mestrado (defesa final)`
  - `Qualificação de doutorado`
  - `Tese de doutorado (defesa final)`
  - `Trabalho de especialização`
- **Mapping YAML:** `.type` → converter para códigos: `tcc1|tcc|qualification|dissertation|phd_qualification|phd|specialization`.

### 3.2 Programa acadêmico

- **Tipo:** Choice (dropdown, obrigatória).
- **Opções:**
  - `Engenharia de Software (FCTE/UnB) — curso_esw`
  - `Engenharia de Software 2 (FCTE/UnB) — curso_esw2`
  - `PPCA — Mestrado Profissional em Computação Aplicada — curso_ppca`
  - `PPEE — Engenharia Elétrica — curso_ppgee`
  - `PPGI — Informática — curso_ppgi`
  - `Bacharelado em Ciência da Computação (UnB) — curso_cc_unb`
  - `Especialização (UnB) — curso_espunb / espunb2 / espunb3`
  - `Outro (descrever no campo abaixo)`
- **Mapping YAML:** `.program` → extrair slug após o traço.

### 3.3 Título em português

- **Tipo:** Text (longo), obrigatório se `tipo ≠ TCC1|Qualificação e Ação = Inserir`.
- **Validação:** mín. 15 caracteres.
- **Mapping YAML:** `.title.pt`.

### 3.4 Título em inglês

- **Tipo:** Text (longo), opcional.
- **Instrução:** `Se não tiver, deixe em branco. O CEDIS pode traduzir depois.`
- **Mapping YAML:** `.title.en`.

### 3.5 Resumo em português (abstract)

- **Tipo:** Text (longo), opcional.
- **Instrução:** `Cole o resumo do trabalho — 150 a 400 palavras. Aparece na página pública da defesa quando preenchido.`
- **Mapping YAML:** `.summary.pt`.

### 3.6 Resumo em inglês

- **Tipo:** Text (longo), opcional.
- **Mapping YAML:** `.summary.en`.

---

## 6. Seção 4 — Aluno(s)

### 4.1 Quantos alunos defendem juntos?

- **Tipo:** Choice (radio, obrigatória).
- **Opções:**
  - `1 aluno` (padrão)
  - `2 alunos (dupla de TCC)` — só em TCC/TCC1
- **Branching:** exibe 4.2 sempre, 4.3-4.4 se selecionar "2 alunos".

### 4.2 Nome completo do aluno 1

- **Tipo:** Text (curto), obrigatória.
- **Instrução:** `Como no diploma/BDM (com acentos).`
- **Mapping YAML:** `.students[0].name`.

### 4.3 Nome completo do aluno 2 *(apenas para duplas)*

- **Tipo:** Text (curto), obrigatória em duplas.
- **Mapping YAML:** `.students[1].name`.

### 4.4 Slug de perfil dos alunos *(opcional, avançado)*

- **Tipo:** Text (longo), opcional.
- **Instrução:**
  ```
  Se o aluno tiver perfil em /people/<slug>/ (raro, geralmente só ex-orientandos ativos), informe o slug canônico.
  Formato: aluno1: slug_do_aluno1, aluno2: slug_do_aluno2
  Deixe em branco na maioria dos casos.
  ```
- **Mapping YAML:** `.students[i].slug`.

---

## 7. Seção 5 — Orientação

### 5.1 Orientador principal

- **Tipo:** Choice (dropdown, obrigatória — presente sempre para todos os tipos).
- **Opções (fixadas — 7 docentes CEDIS):**
  - `Sergio Antônio Andrade de Freitas`
  - `Cristiane Soares Ramos`
  - `André Luiz Peron Martins Lanna`
  - `George Marsicano Corrêa`
  - `Ricardo Ajax Dias Kosloski`
  - `Daniel Sundfeld Lima`
  - `Fabiana Freitas Mendes`
- **Mapping YAML:** `.advisor` (slug canônico).

### 5.2 Há co-orientador(es)?

- **Tipo:** Choice (radio, obrigatória).
- **Opções:** `Não` / `Sim, um` / `Sim, dois`.
- **Branching:** exibe 5.3 e 5.4 conforme selecionado.

### 5.3 Co-orientador 1 *(condicional)*

- **Tipo:** Choice (dropdown, obrigatória se marcado).
- **Opções:** mesmos 7 docentes CEDIS **+**
  - `Edna Dias Canedo (externa, PPCA)`
  - `Andrea Felippe Cabello (externa)`
  - `Marilia Miranda Forte Gomes (externa)`
  - `Berilhes Borges Garcia (externo)`
  - `Célia Higawa (externa)`
  - `Outro (descrever no campo texto abaixo)`
- **Mapping YAML:** `.co_advisors[0]` (slug quando existir stub em `content/people/`; nome cru quando "Outro").

### 5.4 Co-orientador 2 *(condicional)*

- Igual 5.3, mapeia para `.co_advisors[1]`.

---

## 8. Seção 6 — Banca (5 membros fixos)

**Design:** cada membro em bloco de 4 campos. **Mostrar 5 blocos**; deixar vazios os que não usar. Script Python descarta blocos com nome vazio.

### 6.1 Instrução da seção

```
Preencha o(s) membro(s) da banca EXAMINADORA (além do orientador,
que já foi informado na seção 5). O orientador vai como membro
role=advisor automaticamente.

Ordem sugerida:
  1º e 2º blocos → examinadores obrigatórios
  3º bloco → 3º examinador (dissertações/teses) OU vazio
  4º bloco → suplente (opcional)
  5º bloco → co-orientador que participa da banca (raro)

Deixe em branco os blocos que não usar.
```

### 6.2 Membro N (repetir 5×)

Para cada N em {1, 2, 3, 4, 5}:

- **6.N.a Nome completo do membro N** — Text (curto), opcional.
- **6.N.b Papel do membro N** — Choice (dropdown):
  - `Examinador(a)` → `examiner`
  - `Examinador(a) externo(a) à UnB` → `external_examiner`
  - `Suplente` → `substitute`
  - `Co-orientador(a) participando` → `co_advisor`
- **6.N.c Afiliação (sigla/instituição)** — Text (curto), opcional. Ex.: `PPCA/UnB`, `IMD/UFRN`, `CISSA/CESAR`.
- **6.N.d Este membro tem perfil no site CEDIS?** — Choice (dropdown), opcional:
  - `Não é do CEDIS` (padrão)
  - `sergio_freitas`
  - `cristiane_ramos`
  - `andre_lanna`
  - `george_marsicano`
  - `ricardo_ajax`
  - `daniel_sundfeld`
  - `fabiana_mendes`
  - `edna_canedo`
  - `andrea_cabello`
  - `marilia_miranda`
  - `berilhes_garcia`
  - `celia_higawa`

**Mapping YAML:** `.committee[i]` → `{ role, name, affiliation, slug }`.

---

## 9. Seção 7 — Local, agenda e vínculos

### 7.1 Data da defesa

- **Tipo:** Date, obrigatória.
- **Instrução:**
  ```
  Data em que a defesa ocorreu (marcada, se ainda não realizada).
  Se souber apenas o ano, informe 15/junho do ano.
  ```
- **Mapping YAML:** `.scheduled_date` (concatenar com hora abaixo).

### 7.2 Horário da defesa

- **Tipo:** Text (curto, formato HH:MM), opcional.
- **Placeholder:** `14:00`
- **Validação:** regex `^\d{2}:\d{2}$`.
- **Instrução:** `Só preencha se souber. Formato 24h. Deixe em branco para "horário não definido".`
- **Mapping YAML:** compõe `.scheduled_date` (`YYYY-MM-DDTHH:MM:00-03:00`).

### 7.3 Data aproximada?

- **Tipo:** Choice (radio, obrigatória):
  - `Não, é a data exata` (padrão)
  - `Sim, é aproximada (usada apenas o ano)`
- **Mapping YAML:** `.date_approximate` (bool).

### 7.4 Local presencial (sala)

- **Tipo:** Text (curto), opcional.
- **Placeholder:** `Auditório PPCA` / `Sala D1-31/FCTE`
- **Mapping YAML:** `.location.room`.

### 7.5 Cidade

- **Tipo:** Text (curto), opcional (padrão implícito: Brasília).
- **Mapping YAML:** `.location.city`.

### 7.6 Link para sala virtual (se aplicável)

- **Tipo:** Text (curto, URL), opcional.
- **Validação:** regex URL válida.
- **Placeholder:** `https://meet.google.com/xxx-xxxx-xxx`
- **Mapping YAML:** `.location.remote_url`.

### 7.7 Áreas do CEDIS relacionadas (tags temáticas)

- **Tipo:** Choice (checkbox, múltipla escolha), obrigatória (mín. 1).
- **Opções (áreas oficiais + tags técnicas comuns):**
  - `active_learning — Aprendizagem Ativa`
  - `ai — Inteligência Artificial`
  - `gamification — Gamificação`
  - `green_software — Software Verde`
  - `hpc — Alto Desempenho`
  - `learning_analytics — Learning Analytics`
  - `machine_learning — Aprendizado de Máquina`
  - `nlp — Processamento de Linguagem Natural`
  - `security — Cibersegurança`
  - `social_software — Software Social`
  - `software_architecture — Arquitetura de Software`
  - `software_product_line — Linha de Produtos`
  - `software_quality — Qualidade de Software`
  - `software_requirements — Engenharia de Requisitos`
  - `soft_skills — Habilidades Socioemocionais`
  - `digital_transformation — Transformação Digital`
  - `verification_validation_testing — V&V e Testes`
- **Mapping YAML:** `.tags[]` — extrair slug antes do traço.

### 7.8 Este trabalho está vinculado a algum projeto do CEDIS?

- **Tipo:** Choice (dropdown), opcional.
- **Opções (populadas a partir de `data/projects.yaml`; script atualiza periodicamente):**
  - `— nenhum —` (padrão)
  - `framework_preditivo_engajamento`
  - `ia_dados_transformacao_digital`
  - `inovacao_digital_gamificacao`
  - `evidentia`
  - `octaanalysis`
  - `dfcris`
  - `contextus`
  - `alvorecer`
  - `jornada`
  - *(demais projetos)*
- **Mapping YAML:** `.project`.

### 7.9 Produtos gerados pelo trabalho

- **Tipo:** Text (longo), opcional.
- **Instrução:**
  ```
  Slugs dos produtos em /products/ separados por vírgula.
  Exemplo: edutrack, atloria, git-ranking
  Deixe em branco se não gera produto.
  ```
- **Mapping YAML:** `.related_products[]` — split por vírgula.

### 7.10 Artigos científicos derivados

- **Tipo:** Text (longo), opcional.
- **Instrução:**
  ```
  IDs de publicações em productions.yaml derivadas deste trabalho.
  Exemplo: 2026-emanuel-oliveira-a-motivation-aware..., 2025-...
  Deixe em branco se não houver.
  ```
- **Mapping YAML:** `.related_publications[]` — split por vírgula.

### 7.11 URL do trabalho depositado (BDM/Repositório UnB)

- **Tipo:** Text (curto, URL), opcional.
- **Instrução:**
  ```
  Preencha APENAS quando o trabalho já foi depositado.
  BDM: https://bdm.unb.br/handle/10483/<n>
  Repositório: https://repositorio.unb.br/handle/10482/<n>
  ```
- **Mapping YAML:** compõe `.production_id` via cross-lookup em `productions.yaml`.

### 7.12 Narrativa jornalística (opcional, autoral)

- **Tipo:** Text (longo), opcional.
- **Instrução:**
  ```
  Se quiser escrever um parágrafo autoral em vez da notícia auto-gerada,
  cole aqui em português. O CEDIS pode traduzir para inglês.
  ~300 palavras. Use gancho jornalístico: qual era o problema, o que
  o trabalho descobriu, por que importa.
  ```
- **Mapping YAML:** `.narrative.pt` (e `.en` se preencher em ambos idiomas via 7.13).

### 7.13 Narrativa em inglês

- **Tipo:** Text (longo), opcional.
- **Mapping YAML:** `.narrative.en`.

### 7.14 Esta defesa foi cancelada?

- **Tipo:** Choice (radio, obrigatória).
- **Opções:**
  - `Não` (padrão)
  - `Sim, marcar como cancelada (mantém histórico)`
- **Mapping YAML:** `.status_override` = `withdrawn` se sim.

---

## 10. Seção 8 — Confirmação e envio

### 8.1 Observações para o revisor

- **Tipo:** Text (longo), opcional.
- **Instrução:** `Contexto adicional, correções específicas de campo que já existia, motivo da exclusão, etc.`

### 8.2 Confirmação (obrigatória)

- **Tipo:** Choice (checkbox, obrigatória — 1 item marcado).
- **Opção:**
  - `☐ Confirmo que os dados informados são verdadeiros e autorizo a publicação no site do CEDIS.`

### 8.3 Aviso final

Texto de fechamento após envio:

```
Obrigado! Sua submissão foi registrada. A atualização no site
acontece após revisão (tipicamente em até 3 dias úteis).
Para dúvidas: cedis@unb.br.
```

---

## 11. Do MS Forms para o `data/defesas.yaml`

### 11.1 Fluxo técnico

```
[Prof. preenche form]
         ↓
[MS Forms grava em planilha do OneDrive/SharePoint (auto)]
         ↓
[Script Python semanal: scripts/import_defesas_form.py]
         ↓
[Diff em data/defesas.yaml (nova entrada, alterações, remoções lógicas)]
         ↓
[PR automático via GitHub Action OU commit manual do mantenedor]
         ↓
[Site atualiza no próximo build]
```

### 11.2 Script `scripts/import_defesas_form.py` (a construir)

Contrato:

```python
python3 scripts/import_defesas_form.py \
    --xlsx path/para/respostas.xlsx \
    --since "2026-07-01" \
    --out data/defesas.yaml \
    --report tmp/import-report.md
```

Responsabilidades:

1. **Ler cada linha** da planilha (uma resposta = uma ação).
2. **Validar** e-mail do respondente contra whitelist CEDIS.
3. **Traduzir rótulos** (ex.: "Sergio Antônio Andrade de Freitas" → `sergio_freitas`).
4. **Compor `scheduled_date`** juntando data + hora + fuso `-03:00`.
5. **Gerar slug** para inserção via `scripts/gen_defesa_slug.py` (já existe).
6. **Aplicar ação:**
   - `inserir` → adiciona nova entry; falha se `id` já existe.
   - `alterar` → localiza por `id`; falha se não encontrar; aplica campos preenchidos, preserva os não informados.
   - `excluir` → remove entry (ou marca com `status_override: withdrawn` se preservar histórico).
7. **Rodar validators** (`scripts/validate_content.py`) antes de escrever.
8. **Emitir relatório Markdown** com: linhas processadas, avisos, erros, diff pré/pós.

### 11.3 Governança

- **Frequência:** rodar 1× por semana (ou on-demand quando alguém avisar).
- **Revisor:** mantenedor do repositório (você).
- **Conflitos:** se dois professores editarem a mesma defesa entre rodadas, script marca no relatório e pede resolução manual.
- **Auditoria:** planilha original arquivada por 1 ano (compliance LGPD art. 37 — registro de operações de tratamento).

### 11.4 Campos não editáveis via form

Alguns campos precisam de intervenção manual (fora do formulário):

- **Migração de posts legados** (`news_slug`) — preenchido só uma vez pelo mantenedor.
- **`held_date`** derivada — script infere a partir da `scheduled_date` no passado.
- **`production_id`** — inferido cruzando `url` (7.11) com `productions.yaml`.

---

## 12. Riscos e mitigações

| Risco | Mitigação |
|---|---|
| Professor digita nome do orientador diferente do slug | Dropdown fixo (5.1) elimina — só slugs válidos |
| Membro externo com nome ambíguo entra duas vezes com grafia diferente | Script normaliza acentos/caixa e deduplica na revisão |
| Slug único quebra em duplas raras (mesmo par de nomes + data) | `gen_defesa_slug.py` já detecta colisão e sufixa `-2`, `-3` |
| Prof. envia por engano com ação = Excluir | Script mostra diff no PR; mantenedor rejeita se necessário. Alternativa: exigir dupla confirmação por email antes de aplicar exclusão |
| Fuso horário confuso (submissão do exterior) | `scheduled_date` sempre concatena `-03:00` (Brasília) |
| Aluno com nome longo estoura limite de linha na planilha | MS Forms permite até 4000 caracteres por campo — mais que suficiente |
| Prof. preenche seção "Alterar" mas esquece o ID | Script rejeita com mensagem clara no relatório |

---

## 13. Estimativa de esforço

- **Construir o form no MS Forms:** 2-3h (copiar/colar deste doc + testes).
- **Escrever `import_defesas_form.py`:** 6-8h (parser Excel + validação + diff YAML).
- **Testar com 3-5 respostas reais:** 2h.
- **Documentar no CONVENTIONS.md §3.9:** 1h.
- **Total inicial:** ~12h. Manutenção subsequente: ~30 min/semana.

---

## 14. Rascunho de mapeamento planilha → YAML (para referência)

Colunas típicas da planilha exportada do MS Forms:

| Coluna Excel | Campo form | Campo YAML |
|---|---|---|
| `Start time` | (auto) | (metadata) |
| `Email` | (auto, login institucional) | (metadata — validação) |
| `Ação` | 1.2 | (controle) |
| `Papel` | 1.3 | (auditoria) |
| `ID da defesa` | 2.1 | `.id` (ou gerado) |
| `Info para encontrar` | 2.2 | (revisor manual) |
| `Tipo` | 3.1 | `.type` |
| `Programa` | 3.2 | `.program` |
| `Título PT` | 3.3 | `.title.pt` |
| `Título EN` | 3.4 | `.title.en` |
| `Resumo PT` | 3.5 | `.summary.pt` |
| `Resumo EN` | 3.6 | `.summary.en` |
| `# alunos` | 4.1 | (controla len de students) |
| `Aluno 1` | 4.2 | `.students[0].name` |
| `Aluno 2` | 4.3 | `.students[1].name` |
| `Slugs alunos` | 4.4 | `.students[i].slug` |
| `Orientador` | 5.1 | `.advisor` |
| `# co-orientadores` | 5.2 | (controla len) |
| `Co-orientador 1` | 5.3 | `.co_advisors[0]` |
| `Co-orientador 2` | 5.4 | `.co_advisors[1]` |
| `Banca 1 nome/papel/aff/slug` | 6.1.a-d | `.committee[0]` |
| … | … | … |
| `Banca 5 nome/papel/aff/slug` | 6.5.a-d | `.committee[4]` |
| `Data` | 7.1 | `.scheduled_date` (parte data) |
| `Hora` | 7.2 | `.scheduled_date` (parte hora) |
| `Data aproximada` | 7.3 | `.date_approximate` |
| `Sala` | 7.4 | `.location.room` |
| `Cidade` | 7.5 | `.location.city` |
| `Link virtual` | 7.6 | `.location.remote_url` |
| `Áreas` | 7.7 | `.tags[]` |
| `Projeto` | 7.8 | `.project` |
| `Produtos` | 7.9 | `.related_products[]` |
| `Publicações` | 7.10 | `.related_publications[]` |
| `URL trabalho` | 7.11 | `.production_id` (via lookup) |
| `Narrativa PT` | 7.12 | `.narrative.pt` |
| `Narrativa EN` | 7.13 | `.narrative.en` |
| `Cancelada` | 7.14 | `.status_override` |
| `Observações` | 8.1 | (comentário revisor) |
| `Confirmação` | 8.2 | (rejeitar se não marcado) |
