# 05 — Matriz de riscos

Cada risco tem: identificação, probabilidade, impacto, gravidade (P×I), evidência no repo, mitigação, teste, plano de reversão.

## Escalas

- **Probabilidade:** Baixa (raro se seguir plano) / Média (pode ocorrer) / Alta (provável se descuidar)
- **Impacto:** Baixo (cosmético) / Médio (funcional) / Alto (produção comprometida)
- **Gravidade:** combinação — Crítica / Alta / Média / Baixa

## R1 — Push acidental durante migração publica site em produção

- **Probabilidade:** Média
- **Impacto:** Alto (deploy é automático via GitHub Pages a partir de `docs/` em `main`)
- **Gravidade:** **CRÍTICA**
- **Evidência:** `hugo.yaml:558` = `publishDir: "docs"`. `docs/` é versionado. GitHub Pages configurado para servir da branch `main`. `.github/workflows/site-ci.yml` faz `paths-ignore: docs/**` (não bloqueia deploy, só evita CI redundante). Nenhum branch protection registrado.
- **Mitigação:**
  - Trabalhar exclusivamente em branch local `dev/tailwind-v4-vite-local` **sem upstream**.
  - Configurar hook local `.git/hooks/pre-push` que rejeita push da branch dev.
  - Verificar `git branch -vv` antes e depois de qualquer sessão de trabalho — a branch dev nunca deve mostrar `[origin/...]`.
  - Antes de qualquer merge para main, obter autorização explícita por escrito.
- **Teste:** simular push com `git push --dry-run` e confirmar que branch dev não pode ser pushada (via hook).
- **Reversão:** se push acidental ocorrer para outra branch que não main, `git push origin :branch-name` (delete remoto). Se push atingir main via merge, `git revert` do commit + push, aguardando ~1min para propagar em GitHub Pages.

## R2 — Renames de shadow/rounded/blur não aplicados manualmente

- **Probabilidade:** Baixa (com ferramenta `npx @tailwindcss/upgrade`)
- **Impacto:** Médio (elementos ganham sombra/blur/radius maior — visual pronunciadamente diferente)
- **Gravidade:** Média
- **Evidência:** 81 `shadow-sm`, número não medido de `rounded-sm`/`rounded`/`blur-sm`/`blur` no repo.
- **Mitigação:**
  - Executar `npx @tailwindcss/upgrade` que faz o rename em massa.
  - Grep pós-migração: verificar que não sobrou nenhum `shadow-sm` sem intenção.
- **Teste:** comparar screenshots pré/pós de rotas com muitos cards (home, publicações, projetos).
- **Reversão:** `git checkout .` no working tree da branch dev.

## R3 — Borders sem cor explícita ficam invisíveis em v4

- **Probabilidade:** Alta se não auditado
- **Impacto:** Médio (bordas somem visualmente)
- **Gravidade:** Média
- **Evidência:** ~20+ usos de `class="... border ..."` sem `border-<color>` em templates (grep `\bborder\b` sem cor). Em v4, default é `currentColor` (era `gray-200` em v3). Se `currentColor` = cor do texto = quase igual ao bg, a borda desaparece.
- **Mitigação:**
  - Grep sistemático pós-migração; adicionar `border-gray-200 dark:border-white/10` explicitamente onde necessário.
  - Alternativa: adicionar CSS legacy shim no `main.css`:
    ```css
    @layer base {
      *, ::after, ::before {
        border-color: var(--color-gray-200, currentColor);
      }
    }
    ```
- **Teste:** inspeção visual de tabelas, cards, chips, inputs em modo claro e escuro.
- **Reversão:** ajuste incremental por classe; se muito difundido, aplicar o shim CSS.

## R4 — `text-opacity-40` em SVG do hero da home quebra

- **Probabilidade:** Baixa (upgrade tool cobre)
- **Impacto:** Baixo (elemento decorativo, não funcional)
- **Gravidade:** Baixa
- **Evidência:** `layouts/index.html:737,738` — 2 `<path>` decorativos com `class="text-primary-600 text-opacity-40"`.
- **Mitigação:** `npx @tailwindcss/upgrade` renomeia para `text-primary-600/40`.
- **Teste:** visual da home em desktop.
- **Reversão:** substituição manual.

## R5 — Suporte a navegadores antigos perdido em Tailwind 4

- **Probabilidade:** Média (depende do público real)
- **Impacto:** Médio (usuários com Safari <16.4 ou Chrome <111 podem ver layouts quebrados)
- **Gravidade:** Média
- **Evidência:** Documentação oficial Tailwind 4 exige Safari 16.4+ / Chrome 111+ / Firefox 128+. Público institucional de UnB pode ter computadores desatualizados.
- **Mitigação:**
  - Antes de aprovar, consultar Google Analytics para composição de navegadores dos últimos 90 dias.
  - Se >2% dos usuários em navegadores incompatíveis, considerar adiar migração.
  - Fornecer aviso banner temporário em navegadores obsoletos (v3 tem `<script>` para detectar).
- **Teste:** browserstack ou similar — testar em Safari 16.3 (versão limite) e Chrome 110.
- **Reversão:** rollback completo (git switch main + npm ci).

## R6 — Ferramenta `npx @tailwindcss/upgrade` inclui mudança indesejada

- **Probabilidade:** Baixa
- **Impacto:** Médio (pode reescrever config em CSS-first quando pedimos JS-config)
- **Gravidade:** Baixa
- **Evidência:** Nossa `tailwind.config.js` tem 121 linhas com typography theme customizado. A ferramenta pode oferecer converter para `@theme` — que se aceito exige revalidação.
- **Mitigação:**
  - Rodar `npx @tailwindcss/upgrade` interativo e recusar conversão CSS-first nesta fase.
  - Se a ferramenta insistir, aceitar apenas as mudanças óbvias (@tailwind → @import, renames) e reverter as demais via `git diff` seletivo.
- **Teste:** verificar `git diff tailwind.config.js` após rodar upgrade — não deve estar deletado.
- **Reversão:** `git checkout tailwind.config.js`.

## R7 — Alpine.js CDN 3.x.x atualiza para versão quebrada durante migração

- **Probabilidade:** Baixa (Alpine 3.x é estável há anos)
- **Impacto:** Alto (interatividade some — menu, filtros, accordions)
- **Gravidade:** Média
- **Evidência:** `layouts/partials/footer.html:2` usa `alpinejs@3.x.x` — auto-atualiza patches.
- **Mitigação:**
  - Considerar pinar versão exata (ex.: `alpinejs@3.15.12`) durante migração.
  - Registrar como decisão em ADR.
- **Teste:** verificar console em rotas com Alpine (nav, filterPeople).
- **Reversão:** trocar URL para versão exata anterior.

## R8 — Classes construídas por `printf` invisíveis ao scanner v4

- **Probabilidade:** Baixa (scanner v4 usa mesmo mecanismo textual)
- **Impacto:** Alto (18 blocos em `people/single.html` deixam de estilizar)
- **Gravidade:** Média
- **Evidência:** `layouts/people/single.html:145, 152, 156, 163, 276, 296, 299, 316, 323, 358, 363, 390, 394` — printf gera HTML com literals de classes.
- **Mitigação:**
  - Confirmar `content` (v3) ou `@source` (v4) inclui `layouts/**/*.html` — inclui hoje.
  - Se optar por CSS-first, migrar `content` → `@source "layouts/**/*.html"` explicitamente.
  - Grep pós-migração: `grep "profile-project-card\|researcher-highlights\|featured-publications" docs/**/*.html` — devem seguir existindo.
- **Teste:** carregar 3 perfis de pesquisador em ambos modos e verificar layout dos cards inseridos por printf.
- **Reversão:** adicionar `@source inline("class1 class2 ...")` no CSS-first ou `safelist` (deprecated em v4).

## R9 — Sintaxe de arbitrary value muda (`bg-[--var]` → `bg-(--var)`)

- **Probabilidade:** Baixa se grep antes
- **Impacto:** Baixo (classe fica inválida — sem efeito visual, ou muda cor)
- **Gravidade:** Baixa
- **Evidência:** Não medido. Grep antes de migrar: `grep -rn "bg-\[--\|text-\[--\|border-\[--" layouts/`.
- **Mitigação:** substituir manualmente ou via upgrade tool.
- **Teste:** grep pós-migração deve retornar 0.
- **Reversão:** substituição manual.

## R10 — Grid arbitrary value com vírgula quebra (`grid-cols-[max-content,auto]`)

- **Probabilidade:** Baixa
- **Impacto:** Médio (layout de grid quebra)
- **Gravidade:** Baixa
- **Evidência:** Não medido. Grep: `grep -rn "grid-cols-\[.*,.*\]" layouts/`.
- **Mitigação:** substituir vírgula por underscore.
- **Teste:** visual de grids conhecidos.
- **Reversão:** manual.

## R11 — Hugo Pipes conflita com `@tailwindcss/postcss`

- **Probabilidade:** Baixa (arquitetura é padrão)
- **Impacto:** Alto (CSS não gera)
- **Gravidade:** Alta
- **Evidência:** Hoje `postcss.config.js` tem `{ tailwindcss, autoprefixer }`. Em v4, será `{ '@tailwindcss/postcss': {} }`. `resources.Get "css/main.css" | postCSS` no `head.html` deve continuar funcionando — postCSS pipeline é a mesma abstração.
- **Mitigação:**
  - Fazer build limpo em branch dev antes de assumir pronto.
  - Ler `resources/_gen/assets/` para confirmar CSS gerado.
- **Teste:** `hugo --minify` termina sem erro; CSS servido pela dev-server contém utilities Tailwind.
- **Reversão:** `git checkout postcss.config.js && npm install tailwindcss@3` (força downgrade).

## R12 — Remoção de `postcss`, `autoprefixer` etc. quebra transitivamente

- **Probabilidade:** Baixa
- **Impacto:** Médio (build falha)
- **Gravidade:** Média
- **Evidência:** `@tailwindcss/postcss` depende de `postcss` transitivamente. `postcss` pode continuar necessário como transitive.
- **Mitigação:**
  - Após `npm uninstall autoprefixer browserslist caniuse-lite postcss-cli`, rodar `npm ls postcss` para confirmar que continua presente via transitive.
  - Se necessário, manter `postcss` como dependência direta.
- **Teste:** `npm run build` completa; `docs/css/*.css` tem tamanho normal.
- **Reversão:** `git checkout package.json package-lock.json && npm ci`.

## R13 — Perda de `.Fingerprint` + `.Integrity` do Hugo Pipes

- **Probabilidade:** Nula em Alt 2 (mantida). Alta em Alt 3 (Vite).
- **Impacto:** Alto (SRI hash quebra em produção; browsers rejeitam CSS)
- **Gravidade:** N/A para Alt 2. Alta se Alt 3.
- **Evidência:** `head.html:74,82` usa `$over.Data.Integrity`. Vite não gera integrity hash.
- **Mitigação:** ficar em Alt 2 nesta migração.
- **Teste:** verificar produção pós-deploy que CSS carrega.

## R14 — `docs/` regenerado inclui diffs enormes distraindo revisão

- **Probabilidade:** Alta
- **Impacto:** Baixo (dificulta code review)
- **Gravidade:** Baixa
- **Evidência:** commit 6 do refactor anterior teve 3974 arquivos em docs/. Cada `npm run build` regenera todos.
- **Mitigação:**
  - Durante migração local, NÃO regenerar `docs/` a cada commit — apenas no final.
  - No push final para main, um único commit `Rebuild do site publicado`.
- **Teste:** revisar `git diff --stat` — commits de source ficam limpos.

## R15 — Descarte de `browserslist` remove fallbacks para IE/Safari antigos

- **Probabilidade:** Alta (parte da migração)
- **Impacto:** Baixo (usuários em navegadores antigos já perdem suporte v4 mesmo com autoprefixer)
- **Gravidade:** Baixa
- **Evidência:** Sem `.browserslistrc`, mas `browserslist` decl. em `package.json` faz autoprefixer usar defaults.
- **Mitigação:** documentar em ADR que Tailwind 4 assume browsers modernos por padrão.
- **Teste:** browserslist agora é irrelevante; sem prefixos vendor não pega mais Safari 15.
- **Reversão:** N/A (parte da migração).

## R16 — `text-md`, `xs:hidden`, `dark-mode:` residuais quebram após migração

- **Probabilidade:** Baixa (já corrigidos em 2026-07-25)
- **Impacto:** Baixo (classe não faz nada, situação atual)
- **Gravidade:** Baixa
- **Evidência:** commits `fe5e704f5` de 2026-07-25 já corrigiu 255 classes silenciosamente ignoradas. Nenhuma remanescente conhecida.
- **Mitigação:** rodar `tmp/audit_v2.py` antes da migração — confirmar 3 outliers benignos (`not-prose` false positive, `shadow-neutral-*`).
- **Teste:** grep pós-migração idêntico ao pré.

## Riscos adicionais introduzidos pelo complemento de auditoria (Alt 4 Hugo native)

## R17 — Divergência de versão do Hugo entre local, CI e produção

- **Probabilidade:** Baixa (mesmo alinhado agora)
- **Impacto:** Alto — `css.TailwindCSS` exige Hugo ≥0.161
- **Gravidade:** Média
- **Evidência:**
  - Local: `hugo v0.164.0+extended+withdeploy` (via Homebrew)
  - CI (`site-ci.yml:31`): `HUGO_VERSION: '0.164.0'` + `peaceiris/actions-hugo@v3` com `extended: true`
  - `hugo.yaml:615-617`: `module.hugoVersion.min: "0.104.0"` — TOO permissivo se adotarmos Alt 4 (exigimos ≥0.161)
- **Mitigação:**
  - Antes de merge da migração Alt 4, atualizar `hugo.yaml` para `module.hugoVersion.min: "0.161.0"` — força erro claro se alguém rodar Hugo mais antigo
  - Confirmar CI segue em `HUGO_VERSION: '0.164.0'` ou superior
  - Documentar em README que Hugo 0.161+ é necessário
- **Teste:** `hugo version` local, `hugo version` no log do CI, ambos ≥0.161
- **Reversão:** Alt 2 (que não exige Hugo específico) se algum ambiente não puder atualizar

## R18 — CSS incompleto em um dos idiomas (Alt 4 com hugo_stats.json)

- **Probabilidade:** Média se `templates.Defer` não for aplicado
- **Impacto:** Alto — classes usadas só em PT ou só em EN podem ser podadas
- **Gravidade:** Alta
- **Evidência:** `hugo_stats.json` é preenchido conforme templates são renderizados. Sem `templates.Defer`, `head.html` roda antes de todos os idiomas serem processados. Nosso site é bilíngue via `hugo.yaml:9 languages:`.
- **Mitigação:**
  - Usar `templates.Defer` obrigatoriamente no bloco `css.TailwindCSS` (ver `04-plano-de-migracao.md`)
  - Verificar em CI que build gera CSS que cobre ambos os idiomas (`grep` de classe única em PT e outra em EN nos HTMLs finais)
- **Teste:** rodar build; grep classes usadas apenas em cada idioma; confirmar todas presentes no CSS gerado
- **Reversão:** cair para Alt 2 (PostCSS não depende de stats)

## R19 — Ambiente de produção sem suporte para `css.TailwindCSS`

- **Probabilidade:** Nula — produção é GitHub Pages, servindo `docs/` estático já gerado localmente ou por CI
- **Impacto:** Nulo (o build é local/CI, não em produção)
- **Gravidade:** Baixa
- **Evidência:** GitHub Pages serve `docs/` versionado; não roda Hugo em produção. CI usa Hugo 0.164.0 (compatível).
- **Mitigação:** N/A — arquitetura estática protege.
- **Teste:** `curl -sI https://cedis.unb.br/` — verifica que HTML é servido, não gerado.
- **Reversão:** N/A.

## R20 — Execução acidental de `hugo deploy`

- **Probabilidade:** Baixa
- **Impacto:** Baixo hoje (sem `targets:` em `[deployment]`), potencialmente Alto se targets forem adicionados
- **Gravidade:** Baixa (agora), Média (se targets configurados no futuro)
- **Evidência:**
  - Binário Hugo local tem capability `withdeploy`
  - `hugo config` mostra `[deployment]` com `invalidatecdn=true`, `maxdeletes=256`, `workers=10` mas **sem `targets:`** — `hugo deploy` seria no-op
  - Nenhum script npm ou Makefile invoca `hugo deploy`
- **Mitigação:**
  - Documentar em CONVENTIONS.md que `hugo deploy` está proibido sem autorização
  - Adicionar `hugo deploy` a `09-comandos-propostos.md` como Categoria F (proibido)
  - Se algum dia targets forem adicionados, exigir revisão de segurança separada
- **Teste:** `hugo deploy --dryRun` — dry run é seguro, permite auditar se targets aparecerem por engano
- **Reversão:** N/A hoje

## R21 — Alteração acidental do `publishDir`

- **Probabilidade:** Baixa
- **Impacto:** Alto — se mudar para `public/` (default Hugo), site publicado quebra
- **Gravidade:** Média
- **Evidência:** `hugo.yaml:558` = `publishDir: "docs"`. GitHub Pages configurado para `docs/`.
- **Mitigação:**
  - Nunca alterar `publishDir` sem autorização escrita
  - CI verificar que build escreve em `docs/` (implícito em `hugo --minify --cleanDestinationDir` do `npm run build`)
  - Documentar em README
- **Teste:** `hugo config | grep publishdir` sempre = `docs`
- **Reversão:** `git checkout hugo.yaml`

## R22 — Adoção desnecessária de Vite

- **Probabilidade:** Média (pressão de "seguir TailBliss" ou "usar tooling moderno")
- **Impacto:** Alto — reescrita da pipeline, perda de `.Data.Integrity`
- **Gravidade:** Média
- **Evidência:** ADR-002 documenta a decisão de NÃO adotar Vite. Deve ser revisada só com necessidade concreta.
- **Mitigação:** ADR-002 registrado; qualquer proposta futura de Vite deve responder aos critérios de "necessidade concreta" (SPA, TypeScript build, chunk splitting).
- **Teste:** N/A (decisão).
- **Reversão:** N/A.

## R23 — Conflito Hugo Pipes + Vite se ambos convivem

- **Probabilidade:** Baixa (só em ADR-002 rejeitado)
- **Impacto:** Alto — dois sistemas escrevendo assets, cache incoerente
- **Gravidade:** Alta (se materializar)
- **Evidência:** Cenário hipotético — não implementar.
- **Mitigação:** ADR-002 impede.

## R24 — Classes ausentes em `hugo_stats.json`

- **Probabilidade:** Média (Alt 4)
- **Impacto:** Alto (classe não gera CSS → elemento sem estilo)
- **Gravidade:** Média
- **Evidência:** Cenários específicos onde `hugo_stats.json` pode falhar:
  - Classes em shortcodes chamados condicionalmente por conteúdo raro (só existem em um poucos content .md)
  - Classes em `printf` renderizados em condicionais raras
  - Classes em templates de erro (404) — precisam ser renderizadas para entrar no stats
  - Classes inseridas por JS em runtime (Alpine `:class="cond ? 'X' : 'Y'"` — se X for único e cond raramente true, stats pode não capturar em dev build)
- **Mitigação:**
  - Rodar build **completo** antes de deploy (não parcial de rota específica)
  - Manter `@source "layouts/**/*.html"` como safety net adicional em `main.css` (paga custo de scan mas cobre casos raros)
  - Grep manual de classes suspeitas no CSS gerado após build
- **Teste:** grep classe rara conhecida em CSS gerado
- **Reversão:** adicionar mais `@source` explícitos ao main.css

## Sumário

| # | Risco | Gravidade |
|---|---|---|
| R1 | Push acidental publica em produção | **Crítica** |
| R2 | Renames automáticos não aplicados | Média |
| R3 | Borders sem cor ficam invisíveis | Média |
| R4 | text-opacity-40 quebra no hero | Baixa |
| R5 | Suporte a navegadores antigos perdido | Média |
| R6 | Upgrade tool inclui mudança indesejada | Baixa |
| R7 | Alpine CDN atualiza para versão quebrada | Média |
| R8 | Classes por printf invisíveis ao scanner | Média |
| R9 | Sintaxe arbitrary value CSS variable | Baixa |
| R10 | Grid arbitrary com vírgula | Baixa |
| R11 | Hugo Pipes vs @tailwindcss/postcss | Alta |
| R12 | Remoção de deps quebra transitiva | Média |
| R13 | Perda de Fingerprint+Integrity (só em Alt 3) | Alta se Alt 3 |
| R14 | Diff enorme em docs/ distrai review | Baixa |
| R15 | Descarte browserslist perde prefixes | Baixa |
| R16 | Classes silenciosamente inválidas residuais | Baixa |
| R17 | Divergência versão Hugo local/CI/prod | Média |
| R18 | CSS incompleto em um idioma (Alt 4) | **Alta** |
| R19 | Prod sem suporte `css.TailwindCSS` | Baixa (arquitetura protege) |
| R20 | Execução acidental `hugo deploy` | Baixa hoje, Média se targets adicionados |
| R21 | Alteração acidental `publishDir` | Média |
| R22 | Adoção desnecessária de Vite | Média |
| R23 | Conflito Hugo Pipes + Vite | Alta (se materializar) |
| R24 | Classes ausentes em `hugo_stats.json` | Média |

**Riscos críticos ativos: 1 (R1).**
**Riscos altos a monitorar: 3 (R11, R8, R18).**
**Riscos médios (mitigação obrigatória): 8 (R2, R3, R5, R7, R12, R17, R21, R24).**

## Mitigação global

- Estritamente respeitar as restrições da Fase 2 (branch sem upstream).
- Hook `.git/hooks/pre-push` rejeita push da branch `dev/tailwind-v4-vite-local`.
- Cada fase do plano tem critério de conclusão e reversão explícitos.
- Rollback completo garantido via tag `pre-tailwind-v4-YYYYMMDD` + `git switch main`.
