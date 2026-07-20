# Plano de execução — Auditoria integrada 2026

**Referência:** auditoria integrada do site e do repositório Hugo do CEDIS (12 issues numeradas de I01 a I12).
**Data-base:** 20 de julho de 2026.
**Escopo:** este documento traduz a auditoria em um plano executável. Complementa (não substitui) o `ROADMAP.md` de comunicação e o `CONVENTIONS.md` de padrões editoriais.

## Como ler este plano

Cada issue tem uma ficha de execução com **precondições**, **entregáveis concretos**, **verificação** e **arquivos alvo**. As fases apenas ordenam a execução — dentro de uma fase, várias issues podem ser tocadas em paralelo por pessoas diferentes.

Rótulos usados: `crítica` `alta` `média` para prioridade; `S` `M` `L` `XL` para esforço (dia/semana/2-4 semanas/mês+).

---

## Ordem de execução

```
Fase 0 — Preparação                (~1 sem)   I11, I05
Fase 1 — Correções + fundação CI   (~2 sem)   I04, I06, I01
Fase 2 — Modelo de dados           (3-5 sem)  I02 → I03
Fase 3 — Reestruturações           (4-8 sem)  I07, I09, I08
Fase 4 — Qualidade e política      (contínuo) I10, I12
```

**Regra de sequenciamento:** I02 é pré-requisito de I03, I07 e I09. I01 é pré-requisito de I10. Todo o restante pode paralelizar.

---

## Fase 0 — Preparação

### I11 — Documentação e metadados do repositório
- **Prioridade:** média · **Esforço:** S · **Depende de:** —
- **Precondições:** decidir versão fixa do Hugo (recomendo pinar em `hugo.yaml` a mesma versão do CI).
- **Entregáveis:**
  1. `README.md` na raiz cobrindo: pré-requisitos (Node, Hugo Extended versão X), `npm ci`, `npm run dev`, `npm run build`, como rodar Pagefind, como publicar.
  2. `package.json` com `name`, `description`, `repository.url`, `bugs.url`, `homepage`, `author` do CEDIS (hoje herdados do TailBliss).
  3. `.tool-versions` com `hugo <versão>` e `nodejs <versão>` (asdf) — ou `.nvmrc` + nota da versão do Hugo no README.
- **Verificação:** clone limpo + seguir README chega a `hugo server` funcional.
- **Arquivos:** `README.md`, `package.json`, `.tool-versions`.

### I05 — Remoção de arquivos de dados antigos
- **Prioridade:** alta · **Esforço:** S · **Depende de:** verificação de uso
- **Precondições:** grep global por `people-old`, `people-oldold`, `people-errado`, `productions copy` em `layouts/`, `content/`, `scripts/`, `hugo.yaml`.
- **Entregáveis:**
  1. Remover `data/people-old.yaml`, `data/people-oldold.yaml`, `data/people-errado.yaml`, `data/productions copy.yaml`.
  2. Uma linha em `CONVENTIONS.md` deixando explícito quais arquivos são fontes canônicas em `data/`.
- **Verificação:** `hugo --gc --minify` continua limpo; `git grep` não encontra referências residuais.
- **Arquivos:** `data/*.yaml` (removidos), `CONVENTIONS.md`.

---

## Fase 1 — Correções factuais e fundação de CI

### I04 — Correções factuais e referenciais
- **Prioridade:** crítica · **Esforço:** S · **Depende de:** —
- **Entregáveis:**
  1. Corrigir `Prof. {{< link-interno "/people/sergio_freitas" "andre_lanna" >}}` no DFCris para apontar à URL de André Lanna.
  2. Padronizar `daniel_sundfeld` vs `/people/daniel_lima` (decidir o slug canônico e adicionar alias no *front matter* do outro).
  3. Grep global por `FGA` no site publicado e substituir por `FCTE` onde o contexto pós-transição se aplica.
  4. Substituir `Cibersecurity` por `Cybersecurity` (verificar `content/`, `data/`, `i18n/`, `layouts/`).
- **Verificação:** teste de link interno (parte de I01) roda sem quebras; `grep -RiEn 'FGA|cibersecurity' content data i18n layouts` retorna zero (respeitados nomes históricos legítimos).
- **Arquivos:** `content/projects/DFCris.*.md`, `content/people/*sundfeld*`, e o que o grep encontrar.

### I06 — Canonical e robots
- **Prioridade:** alta · **Esforço:** S · **Depende de:** —
- **Entregáveis:**
  1. Adicionar `<link rel="canonical" href="{{ .Permalink }}">` no partial principal de `<head>`.
  2. Reescrever `static/robots.txt`: `Sitemap: https://cedis.unb.br/sitemap.xml`, regras explícitas de crawl, `Disallow` de `/pt/search/` e `/search/` se apropriado.
  3. Auditar `og:type` no partial de meta para emitir `article`, `profile`, `product` conforme `.Section`.
- **Verificação:** `grep -r 'rel="canonical"' /tmp/build/` retorna todas as páginas HTML; `curl` de `robots.txt` mostra Sitemap.
- **Arquivos:** `layouts/partials/meta.html` (ou o partial equivalente de `<head>`), `static/robots.txt`.

### I01 — CI de construção e validação
- **Prioridade:** crítica · **Esforço:** M · **Depende de:** I11 (versão Hugo fixada)
- **Entregáveis:**
  1. `.github/workflows/site-ci.yml` que, em todo push e pull request para `main`:
     - checkout com `fetch-depth: 0` (para `enableGitInfo`),
     - setup Node com cache de `node_modules`,
     - setup Hugo Extended fixado (via `peaceiris/actions-hugo@v3`),
     - `npm ci`,
     - `hugo --gc --minify --destination public`,
     - build do Pagefind,
     - **linkchecker** (lychee) em `public/`,
     - **HTMLproofer** (opcional) para validar HTML gerado,
     - upload de `public/` como artefato.
  2. Regra de branch protection em `main` exigindo o CI verde.
  3. Substituir `"test": "echo ... exit 1"` em `package.json` por um `npm run validate` que roda o mesmo pipeline localmente.
- **Verificação:** PR de teste com erro proposital (link quebrado) falha o job.
- **Arquivos:** `.github/workflows/site-ci.yml`, `package.json`, `lychee.toml` (opcional).

---

## Fase 2 — Modelo de dados canônico

### I02 — Esquema e validação dos dados
- **Prioridade:** crítica · **Esforço:** M · **Depende de:** decisão do modelo de informação (§20 da auditoria)
- **Precondições:** documento curto (`docs/data-model.md`, ~1 página) formalizando os campos obrigatórios de cada entidade, IDs estáveis e enumerações de estado.
- **Entregáveis:**
  1. `schemas/` com um JSON Schema por entidade: `person.schema.json`, `project.schema.json`, `product.schema.json`, `publication.schema.json`, `area.schema.json`, `partner.schema.json`, `opportunity.schema.json`.
  2. `scripts/validate_content.py` que percorre `data/` e `content/`, valida contra os schemas, cruza referências (todo `researcher_id` existe em `people`, todo `area` existe em `areas`, etc.) e sinaliza `translationKey` órfãos.
  3. Etapa `validate` no `site-ci.yml` (I01) chamando o script.
- **Verificação:** dados atuais devem passar; PR de teste inserindo referência inexistente deve falhar.
- **Arquivos:** `schemas/`, `scripts/validate_content.py`, `.github/workflows/site-ci.yml`, `docs/data-model.md`.

### I03 — Unificação de projetos e relações
- **Prioridade:** crítica · **Esforço:** L · **Depende de:** I02
- **Entregáveis:**
  1. Cada `content/projects/*.md` recebe `id`, `researchers: [...]`, `areas: [...]`, `partners: [...]`, `funding_agencies: [...]`, `products: [...]` no *front matter*.
  2. `data/projects.yaml` passa a ser **gerado** (ou eliminado) — se mantido, a origem é a página, e um script preenche o YAML para consumo por componentes que ainda dependem dele.
  3. Templates de perfil (`layouts/people/single.html`) derivam projetos via `where site.RegularPages "Params.researchers" "intersect" (slice $id)` — remove-se qualquer lista manual redundante no perfil.
  4. Regra explicitada em `CONVENTIONS.md`: **relações inversas nunca são registradas à mão**.
- **Verificação:** validador (I02) reporta zero referências manuais duplicadas; visual diff das páginas de projeto e de pessoa deve ser mínimo antes/depois.
- **Arquivos:** `content/projects/*`, `layouts/people/single.html`, `layouts/projects/single.html`, `data/projects.yaml`, `CONVENTIONS.md`.

---

## Fase 3 — Reestruturações de conteúdo

### I07 — Publicações como páginas canônicas
- **Prioridade:** alta · **Esforço:** L · **Depende de:** I02
- **Entregáveis:**
  1. `content/publications/{ano}/{id}.{lang}.md` gerado a partir de `data/productions.yaml` (script `scripts/build_publications.py`).
  2. `layouts/publications/single.html` com título, autores (linkados por ID), resumo, DOI, tipo, projeto, produto, BibTeX copiável, JSON-LD **individual** de `ScholarlyArticle`/`Thesis`.
  3. `layouts/publications/list.html` com filtros preservados (ano, tipo, tema) e paginação — sem inflar o JSON-LD do índice.
  4. Redirects (aliases) das URLs antigas.
- **Verificação:** cada publicação tem URL própria (`curl -I` retorna 200), sitemap cresce proporcionalmente, Pagefind indexa individualmente.
- **Arquivos:** `scripts/build_publications.py`, `layouts/publications/`, `content/publications/` (gerado).

### I09 — Oportunidades estruturadas
- **Prioridade:** alta · **Esforço:** M · **Depende de:** I02
- **Entregáveis:**
  1. Nova seção `content/opportunities/` com *front matter* `status: (open|closed|expired)`, `deadline`, `audience: [tcc|iniciacao|mestrado|doutorado|voluntario|parceria]`, `project`, `responsible`.
  2. `layouts/opportunities/list.html` com filtros por situação e público, ocultação automática de expiradas (mantidas para SEO com `noindex`).
  3. Migrar chamadas de 2025 anteriores para arquivadas.
- **Verificação:** ao mudar `deadline` para uma data passada, a oportunidade some da listagem principal sem editar o `status` manualmente.
- **Arquivos:** `content/opportunities/`, `layouts/opportunities/`, `layouts/_default/list.html` (para roteamento).

### I08 — Paridade PT/EN
- **Prioridade:** alta · **Esforço:** M · **Depende de:** *front matter* padronizado (I02)
- **Entregáveis:**
  1. Toda página institucional obrigatória (lista em `CONVENTIONS.md`) declara `translationKey`.
  2. `scripts/validate_i18n.py` (evoluir o existente): reporta pares faltantes, campos divergentes (`title`, `description`, `featured_image`, `status`), links internos que apontam para o idioma errado.
  3. Job `i18n` no CI que falha com PR-comment listando as lacunas.
- **Verificação:** relatório de lacunas gerado como artefato do CI a cada PR.
- **Arquivos:** `scripts/validate_i18n.py`, `.github/workflows/site-ci.yml`, `CONVENTIONS.md`.

---

## Fase 4 — Qualidade e política

### I10 — Acessibilidade e desempenho contínuos
- **Prioridade:** alta · **Esforço:** M · **Depende de:** I01
- **Entregáveis:**
  1. `pa11y-ci` configurado com uma lista de URLs críticas (`/`, `/pt/`, `/pt/history/`, `/pt/categories/news/`, uma página de pesquisador, uma de projeto, uma de produto, uma de publicação individual).
  2. `lighthouserc.json` com orçamentos de performance (LCP < 2.5s, CLS < 0.1, INP monitorado) e categorias mínimas (perf ≥ 80, a11y ≥ 90, SEO ≥ 90, best practices ≥ 90).
  3. Job no CI executando ambos após o build; violações graves bloqueiam PR; relatórios anexados como artefato.
- **Verificação:** PR de teste com regressão de contraste falha; painel de resultados histórico visível.
- **Arquivos:** `lighthouserc.json`, `.pa11yci.json`, `.github/workflows/site-ci.yml`.

### I12 — Privacidade e uso do Analytics
- **Prioridade:** alta · **Esforço:** M · **Depende de:** orientação institucional UnB/LGPD
- **Entregáveis:**
  1. Página de política de privacidade (PT/EN) em `content/privacy/` cobrindo finalidade, retenção, controlador, contato do encarregado.
  2. Ativar `privacy.googleAnalytics.respectDoNotTrack: true` em `hugo.yaml`.
  3. Decisão registrada em `docs/privacy-decisions.md`: se GA é carregado antes ou depois de consentimento, se GPC é honrado, se há banner.
  4. Inventário de formulários e integrações externas com dado pessoal (nome, e-mail).
- **Verificação:** requests do GA não saem quando `DNT: 1` ou `Sec-GPC: 1` estão presentes; página de privacidade indexada e linkada no rodapé.
- **Arquivos:** `hugo.yaml`, `content/privacy/`, `layouts/partials/footer.html`, `docs/privacy-decisions.md`.

---

## Riscos e mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Migração de `data/projects.yaml` (I03) quebra páginas dependentes | Média | Alto | Manter YAML gerado até que todos os consumers migrem; validar com snapshot HTML antes/depois. |
| Geração de páginas individuais de publicação (I07) explode o build | Média | Médio | Medir tempo de build antes/depois; se ultrapassar 30s, adotar `--noBuildLock` + cache de Hugo modules. |
| CI passa a bloquear editores não-técnicos (I01, I02, I10) | Alta | Médio | Documentar regras em `README.md`; job de validação com mensagens amigáveis; escalonar rigor (warnings → erros) em 2 sprints. |
| Decisão de privacidade (I12) depende de orientação institucional lenta | Média | Baixo | Enviar minuta para o encarregado LGPD da UnB no início da Fase 4; enquanto isso, ativar `respectDoNotTrack`. |
| Regressão de SEO ao mover publicações (I07) | Média | Alto | Aliases de URLs antigas + submeter novo sitemap ao Search Console; monitorar 30 dias. |

---

## Governança do plano

- **Cadência de revisão:** semanal na Fase 1 (foco em desbloqueio de CI), quinzenal nas demais.
- **Kanban:** cada issue vira uma issue do GitHub com o label `audit-2026` e o label da fase (`phase-0` … `phase-4`). O texto de cada issue vem pronto no relatório da auditoria — copiar como está.
- **Definition of done:** issue só fecha com PR mergeado, CI verde e verificação registrada na descrição da issue.
- **Métricas de acompanhamento** (revisar mensalmente):
  - % de issues concluídas por fase,
  - tempo médio de build no CI (regressão > 20% ⇒ investigar),
  - número de referências quebradas detectadas pelo validador,
  - lacunas PT/EN em páginas obrigatórias (meta: 0 após I08),
  - score médio Lighthouse a11y/perf (meta: ≥ 90 / ≥ 80).

## Critérios de sucesso do plano

O plano é considerado bem-sucedido quando:

1. **Zero fonte-de-verdade duplicada:** relações entre pessoas, projetos, produtos, publicações são declaradas em um único lugar (I03, I07).
2. **CI protege o `main`:** nenhum PR entra sem build verde, links válidos, dados validados, i18n conferido e a11y sem regressão grave (I01, I02, I08, I10).
3. **Cada publicação tem URL própria** e JSON-LD individual (I07).
4. **Oportunidades expiram sozinhas** (I09).
5. **`README.md` permite onboarding de um novo colaborador em menos de 30 minutos** (I11).
6. **Política de privacidade publicada e GA respeita DNT/GPC** (I12).
7. **Nenhuma referência a FGA, `Cibersecurity`, ou arquivos `*-old*` no repositório** (I04, I05).

---

## Anexo A — Mapa rápido issue ↔ arquivos

| Issue | Arquivos-chave |
|---|---|
| I01 | `.github/workflows/site-ci.yml`, `package.json` |
| I02 | `schemas/`, `scripts/validate_content.py`, `docs/data-model.md` |
| I03 | `content/projects/`, `layouts/people/single.html`, `data/projects.yaml`, `CONVENTIONS.md` |
| I04 | `content/projects/DFCris.*.md`, `content/people/*sundfeld*`, ocorrências de `FGA`/`Cibersecurity` |
| I05 | `data/people-old*.yaml`, `data/people-errado.yaml`, `data/productions copy.yaml` |
| I06 | `layouts/partials/meta.html`, `static/robots.txt` |
| I07 | `scripts/build_publications.py`, `layouts/publications/`, `content/publications/` |
| I08 | `scripts/validate_i18n.py`, `.github/workflows/site-ci.yml` |
| I09 | `content/opportunities/`, `layouts/opportunities/` |
| I10 | `lighthouserc.json`, `.pa11yci.json`, `.github/workflows/site-ci.yml` |
| I11 | `README.md`, `package.json`, `.tool-versions` |
| I12 | `hugo.yaml`, `content/privacy/`, `layouts/partials/footer.html`, `docs/privacy-decisions.md` |
