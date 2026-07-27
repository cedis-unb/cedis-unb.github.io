# Plano — Modelo de Defesas como entidade primeira

**Autor:** Sergio Freitas + assistente
**Início:** 2026-07-27
**Escopo:** reescrever a representação de defesas (TCC1, TCC2, qualificação de mestrado, defesa de mestrado, qualificação de doutorado, defesa de doutorado) para tratá-las como **entidade primeira** no site — com anúncio prévio, transição automática por data e notícia auto-gerada opcionalmente enriquecida.

**Decisão de arquitetura confirmada com Sergio em 2026-07-27:**

1. Aluno como perfil → `students[].slug: null` por padrão; perfil sob demanda. Suporta dupla (TCC).
2. Slug da defesa → gerado por script.
3. Aliases dos posts atuais → mantidos por enquanto; deprecação planejada.
4. Post `.md` de defesa → mantido por enquanto; deprecação planejada. Enquanto existir, `.md` fornece `narrative`; sem `.md`, template gera parágrafo padrão.
5. Localização → campos opcionais e livres (nem toda defesa tem local definido).
6. Roles da banca → `advisor|co_advisor|examiner|external_examiner|substitute` (todas, sempre que possível).

---

## 1. Objetivo

Uma defesa é um **evento único** (data + banca + tema + aluno + orientador) do qual podem decorrer notícia e publicação. Hoje o site trata "defesa" como campo secundário de `productions.yaml`; qualificações e TCC1 ficam órfãos de estrutura. Esta reforma resolve:

- **Anúncio prévio** de bancas marcadas para chamar público.
- **Transição automática** anúncio → notícia após a data, sem edição manual.
- **Notícia bem automatizada** — parágrafo padrão gerado do YAML; escrita autoral opcional.
- **Rastreabilidade unificada**: "quantas defesas fulano orientou em 2024?" resolvido lendo uma única fonte.
- **Egresso**: TCC1, TCC2, qualificação e defesa final compartilham a mesma modelagem.

---

## 2. Schema `data/defesas.yaml`

```yaml
- id: emanuel-oliveira-2025-12-11              # slug canônico, gerado por script (§3), imutável
  type: dissertation                            # tcc1|tcc|qualification|dissertation|phd_qualification|phd
  program: curso_ppca                           # slug já usado em productions.yaml (§2.3)
  scheduled_date: 2025-12-11T14:00:00-03:00     # data marcada — obrigatório
  held_date: 2025-12-11                         # data real, opcional; se ausente e scheduled_date < hoje ⇒ derivado (held)
  title:
    pt: 'Título em português'
    en: 'English title'
  summary:                                       # abstract/resumo do trabalho; ~150–400 palavras.
    pt: ''                                       # Renderizado como parágrafo em qualquer estado
    en: ''                                       # (upcoming, held, deposited) quando presente.
  students:                                      # 1 ou 2 (dupla em TCC)
    - name: Emanuel Oliveira
      slug: null                                 # ou 'emanuel_oliveira' se houver perfil (raro)
  advisor: george_marsicano                      # 1 orientador principal, slug canônico
  co_advisors:                                   # opcional
    - edna_canedo
  committee:                                     # banca
    - slug: george_marsicano                     # opcional; quando o membro tem perfil CEDIS
      name: George Marsicano Corrêa              # sempre presente (fallback quando template não resolve slug)
      affiliation: CIC/UnB                       # opcional
      role: advisor                              # advisor|co_advisor|examiner|external_examiner|substitute
    - name: Laerte Peotta de Melo                # membro externo — só nome+affiliation
      affiliation: CIC/PPCA/UnB
      role: examiner
    - name: Milton Vinicius Morais de Lima
      affiliation: CISSA/CESAR
      role: external_examiner
  location:                                      # opcional; qualquer combinação
    room: null                                   # ex.: 'Auditório PPCA' | null
    city: null                                   # ex.: 'Brasília' | null
    remote_url: null                             # ex.: link Meet/Zoom | null
  tags:                                          # tags temáticas + área do CEDIS (mesmo padrão de productions.yaml)
    - security
    - ai
  project: framework_preditivo_engajamento       # id em data/projects.yaml; null se defesa não pertence a projeto
  related_products:                              # slugs de content/products/ gerados a partir do trabalho
    - edutrack
  related_publications:                          # ids de publicações em productions.yaml derivadas do trabalho
    - 2026-emanuel-oliveira-a-motivation-aware...
  production_id: null                            # slug em productions.yaml quando trabalho for depositado; null antes
  news_slug: defesa-emanuel-oliveira-2025        # slug do post .md legado, se existir (transição §7); null nos novos
  narrative:                                     # opcional — parágrafo autoral, substitui o auto-gerado
    pt: null
    en: null
  status_override: null                          # opcional: 'withdrawn' força cancelamento; qualquer outro valor ignorado
```

**Campos obrigatórios:** `id`, `type`, `scheduled_date`, `title`, `students`, `advisor`.
**Todos os demais são opcionais** e derivados/nulos quando ausentes.

### 2.1 Vínculos com projetos, produtos e publicações

Uma defesa pode estar ligada a mais de um artefato do ecossistema CEDIS:

- **`project`** (0 ou 1): id de projeto em `data/projects.yaml`. Inferido automaticamente quando alguma tag do trabalho é id de projeto conhecido; pode ser preenchido/corrigido manualmente.
- **`related_products`** (0..N): slugs de `content/products/*.md` gerados a partir do trabalho defendido. Inferência inicial: produtos cuja `publications[]` cita a publicação do trabalho.
- **`related_publications`** (0..N): ids de publicações em `productions.yaml` (artigos, capítulos) derivadas do trabalho. Preenchimento manual por enquanto — inferência automática exige mais heurística.

**Template de notícia** (§6.5) usa esses vínculos para renderizar seções "Projeto associado", "Produtos gerados", "Publicações vinculadas" com link direto. Se todos ausentes, o bloco não aparece.

### 2.2 Committee — membros com ou sem perfil CEDIS

Cada membro em `committee[]` tem duas variantes:

1. **Membro do CEDIS** (com perfil): usa `slug` (obrigatório) + `name` (rótulo estável) + `affiliation` (opcional). Template renderiza como link para `/people/<slug>`.
2. **Membro externo**: usa `name` + `affiliation` (sem `slug`). Template renderiza como texto.

`migrate_defesas.py` detecta automaticamente o slug cruzando o nome com `content/people/*.md` (match tolerante a acentos, primeiro+último nome). Quando bate, adiciona `slug`.

## 3. Slug canônico (`id`)

Regra do gerador:

- 1 aluno: `<primeiro-nome>-<último-sobrenome>-<AAAA>-<MM>-<DD>`
- Dupla (TCC): `<nome1>-<nome2>-<AAAA>-<MM>-<DD>` (usar primeiro nome de cada)
- Normalização: minúsculo, sem acentos, hífens, remoção de "de", "da", "do" no meio.
- Data: `AAAA-MM-DD` de `scheduled_date` (nunca muda depois).

Exemplos:
- `emanuel-oliveira-2025-12-11`
- `henrique-marina-2026-07-04`
- `sergio-freitas-2013-08-15`

Script `scripts/gen_defesa_slug.py` produz o slug e detecta colisões (raro — mesmo primeiro nome + sobrenome + dia).

## 4. Estados derivados

Estado nunca é campo direto — é derivado em cada build:

```
if status_override == 'withdrawn': state = withdrawn
elif scheduled_date > now:          state = upcoming
elif production_id is null:         state = held
else:                                state = deposited
```

Vantagens:
- Zero atualização manual para transitar `upcoming → held`.
- Rebuild diário do GitHub Pages Actions já basta.
- `held → deposited` acontece quando o autor adicionar `production_id`.

## 5. Relação com `productions.yaml`

**Variante A** (confirmada): `productions.yaml` referencia `defesa` via `defesa_id: <slug>`. Campo `defense_date` **deixa de existir** em `productions.yaml` — vem de `data/defesas.yaml`.

`build_publications.py` passa a validar que todo item com `type in [tcc, dissertation, phd, specialization]` tem `defesa_id` apontando para entrada existente em `defesas.yaml`.

## 6. Templates e componentes

### 6.1 Nova página `/pt/defesas/<id>/` e `/defenses/<id>/`

Layout único que renderiza conforme estado:

| Estado | Cabeçalho | Corpo principal | Rodapé |
|---|---|---|---|
| `upcoming` | Selo "Defesa marcada" + data/hora + contagem regressiva | Tema + **resumo (`summary.<lang>`) quando presente** + banca + orientador + local/link remoto + botão .ics | CTA "assista" |
| `held` | Selo "Defesa realizada" + data | Parágrafo (gerado ou `narrative`) + **resumo quando presente** + banca + tema | Se `narrative` vazio, sugestão em Markdown pra editor |
| `deposited` | Selo "Trabalho depositado" | Igual `held` + card com link BDM/repositório + botão "Ler" | Cross-link para `/publications/<id>/` |
| `withdrawn` | Selo "Cancelada" | Nota curta | Sem CTA |

**Sobre o resumo/abstract:** quando `summary.<lang>` estiver preenchido no YAML, aparece como bloco `<blockquote>` estilizado logo abaixo do parágrafo-notícia (autogerado ou `narrative`). Em `upcoming`, serve para o público entender o tema com profundidade antes da defesa; em `held`/`deposited`, complementa a notícia como resumo executivo do trabalho. Se ausente, o layout não mostra placeholder.

### 6.2 Nova página `/pt/defesas/` (index)

3 seções:
- **Próximas defesas** — `state == upcoming`, ordenadas por `scheduled_date` ascendente.
- **Últimas realizadas** — `state in [held, deposited]`, últimas 10 por `held_date/scheduled_date` desc.
- **Arquivo** — link para `/pt/defesas/arquivo/<ano>/`.

Filtros Alpine.js: orientador, programa, tipo (mesmo padrão de `/publications/`).

### 6.3 Bloco "Próxima defesa" nos perfis

`layouts/people/single.html` ganha bloco antes de "Publicações em destaque":
- Aparece **se houver** ≥ 1 defesa `upcoming` orientada pela pessoa (`advisor == slug` ou `co_advisors contém slug`).
- Card compacto: aluno + data + tema + link para `/defesas/<id>/`.

### 6.4 Feed vivo da home

Aggregação em `layouts/index.html` (bloco `$pulseItems` linha 37-99) passa a incluir 2 tipos novos:
- `type: defense_upcoming` — badge azul "Defesa marcada em X dias"
- `type: defense_result` — badge verde "Defesa realizada" (já cobre parcialmente hoje)

### 6.5 Partial `defesa-body.html`

Gera parágrafo padrão da notícia a partir do YAML. Escolhe entre 3-4 templates com base em `type` e `program` (ex.: TCC vs dissertação vs qualificação). Localizável PT/EN.

Estrutura de renderização:

1. **Parágrafo-notícia**: se `narrative.<lang>` preenchido, usa direto; caso contrário, gera a partir de `type`, `students`, `advisor`, `title`, `program` e `held_date`.
2. **Bloco de resumo**: se `summary.<lang>` preenchido, renderiza como `<blockquote>` semântico com rótulo "Resumo" (PT) / "Abstract" (EN). Sem placeholder quando ausente.
3. **Banca estruturada**: lista com nomes + afiliação + role, ordenada por role (advisor, co_advisor, examiner, external_examiner, substitute).

Se `narrative.pt` (ou `.en`) preenchido: substitui apenas o parágrafo-notícia — resumo e banca continuam renderizados a partir do YAML.

## 7. Migração

Etapas do script `scripts/migrate_defesas.py`:

1. **Bootstrap `data/defesas.yaml`** — lê `data/productions.yaml`, filtra `type in [tcc, dissertation, phd, specialization]`, gera 1 entrada por publicação com `production_id` preenchido, `state = deposited`, `scheduled_date = held_date = defense_date` (ou 15-06-<year> se só ano).
2. **Extrair banca dos posts atuais** — parse do parágrafo padronizado em `content/posts/defesa-*.md` (formato §3.7 CONVENTIONS). Popula `committee[]`. **Perda esperada:** posts que fugiram do formato — flagados no relatório do script para edição manual.
3. **Adicionar entradas para tcc1/qualificacao/qualificação_lucas_linard existentes** — 4 arquivos, sem `production_id`.
4. **Preencher `news_slug` para todos** — slug do post `.md` correspondente.
5. **Adicionar `defesa_id` em `productions.yaml`** — via script; remover `defense_date`.
6. **Regenerar `content/publications/`** via `build_publications.py`.
7. **Validador em `scripts/validate_content.py`**:
   - `productions.yaml` items com `type in [tcc, dissertation, phd, specialization]` devem ter `defesa_id`.
   - Toda `defesa_id` referenciada deve existir em `defesas.yaml`.
   - `defesas.yaml` `advisor` e `co_advisors` devem ser slugs válidos em `people-index`.
   - `committee[].role` em enum válido.
   - `slug` (id) único.

## 8. URLs e aliases

**Novas URLs:**
- `/pt/defesas/`, `/defenses/`
- `/pt/defesas/<id>/`, `/defenses/<id>/`

**Aliases** (via frontmatter `aliases:` em cada `.md` legado, ou tabela em `layouts/_default/`):
- `/pt/posts/defesa-emanuel-oliveira-2025/` → `/pt/defesas/emanuel-oliveira-2025-12-11/` (301 via Hugo alias)
- Idem para todos os 27 posts (22 defesas + 4 tcc1 + 1 qualificação).

Deprecação planejada mas fora deste ciclo: apagar os `.md` legados quando não houver mais `narrative` autoral (ou quando `narrative` for migrado para YAML).

## 9. Sprints

### Sprint 1 — Schema, migração e validação (target: 3-5 dias)

- [ ] `data/defesas.yaml` inicial gerado do script (~200 entradas).
- [ ] `scripts/migrate_defesas.py` e `scripts/gen_defesa_slug.py`.
- [ ] `scripts/validate_content.py` cobre novo modelo.
- [ ] `productions.yaml` migrado (com `defesa_id`, sem `defense_date`).
- [ ] `build_publications.py` atualizado.
- [ ] `npm test` passa 100%.
- **Definition of done:** commit revertible; validador do CI passa; dados canônicos íntegros.

### Sprint 2 — Template `/defesas/<id>/` com 4 estados

- [ ] `layouts/defesas/single.html` renderiza 4 estados.
- [ ] `layouts/partials/defesa-body.html` gera parágrafo padrão.
- [ ] Aliases de todos os 27 posts legados apontando pro novo URL.
- [ ] Amostra visual: 4 defesas (uma por estado) com screenshot no PR.
- **Definition of done:** URL antiga redireciona; URL nova responde; parágrafo automático sensato em 80% dos casos amostrados.

### Sprint 3 — Página `/defesas/` (index) + feed vivo

- [ ] `layouts/defesas/list.html` com 3 seções (próximas, últimas, arquivo).
- [ ] Filtros Alpine.js.
- [ ] `layouts/index.html` inclui `defense_upcoming` no feed vivo.
- [ ] `layouts/people/single.html` mostra "Próxima defesa" quando houver.
- [ ] Menu de navegação: item "Defesas" sob People/Equipe (ou sub-item de Publicações).
- **Definition of done:** navegação fluida; próximas defesas visíveis em ≥ 3 lugares (home, /defesas/, perfil do orientador).

### Sprint 4 — CONVENTIONS + limpeza

- [ ] Reescrever CONVENTIONS §3 completa (agora sobre `defesas.yaml` como fonte primária).
- [ ] Adicionar `PLANO-DEFESAS-2026.md` ao `README.md` como referência.
- [ ] Atualizar `content/accessibility.pt/en.md` se aplicável.
- [ ] Escrever guia curto "Como adicionar defesa" (target: 60 segundos de leitura).
- [ ] Marcar como concluído no ROADMAP e no PLANO-AUDITORIA.
- **Definition of done:** convenção documentada; um usuário novo consegue adicionar defesa lendo apenas a nova §3.

### Sprint 5 (opcional, futuro) — Deprecar `.md` legados

- [ ] Migrar `narrative` autoral dos 22 posts para o campo `narrative` do YAML.
- [ ] Deletar `content/posts/defesa-*.md`, `qualificacao-*.md`, `tcc1-*.md`.
- [ ] Manter aliases indefinidamente (SEO).

Não é escopo dos sprints 1-4.

## 10. Impacto em CONVENTIONS

§3 vai ser reescrita quase toda. Nova estrutura:

- **§3.0** — Fonte canônica `data/defesas.yaml` (era: "matriz TCC1/TCC2/...")
- **§3.1** — Slug canônico (novo)
- **§3.2** — Campos e schema (era: frontmatter de post .md)
- **§3.3** — Estados derivados (novo)
- **§3.4** — Banca estruturada (era: parágrafo padronizado)
- **§3.5** — Relação com `productions.yaml`
- **§3.6** — Narrativa opcional (era: "Corpo")
- **§3.7** — Aliases e deprecação de posts (novo)
- **§3.8** — Como adicionar defesa (guia rápido)

Rascunho da reescrita entregue no Sprint 4.

## 11. Riscos e mitigações

| Risco | Impacto | Mitigação |
|---|---|---|
| Parse de banca dos posts atuais quebra em 5-10% | Perda de dado histórico | Script emite relatório de falhas; editor humano popula manualmente. Fallback: `committee: []` e nota "Banca não migrada". |
| Colisão de slug em datas iguais com nomes parecidos | 2 defesas confundem | Verificação no script; sufixo `-2` quando colidir. |
| SEO: URLs mudam | Perda de tráfego | Aliases 301 desde o dia 1; sitemap regenerado. |
| Rebuild diário pode não acontecer no dia certo | Anúncio some tardio | GitHub Actions cron opcional; aceitável ter até 24h de atraso na transição. |
| Templates novos regridem a11y | Perda de score | Rodar pa11y-ci e Lighthouse a cada sprint; regressão bloqueia PR. |
| Notícia auto-gerada fica robótica | Comunicação empobrecida | `narrative` sempre pode ser adicionado depois; 22 posts atuais continuam ativos até narrativa migrar. |

## 12. Autorização para prosseguir

Ao aprovar este plano, Sergio autoriza execução de Sprint 1. Cada sprint tem gate de validação — assistente pausa e apresenta resultado antes de seguir.

**Referências cruzadas:**
- CONVENTIONS §2 (productions.yaml) e §3 (defesas)
- PLANO-AUDITORIA-2026.md (validators)
- ROADMAP.md (visibilidade e comunicação)
