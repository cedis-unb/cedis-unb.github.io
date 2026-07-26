# 03 — Comparação de arquiteturas

Análise de três alternativas para o pipeline de CSS do site CEDIS.

## Contexto

O pipeline atual é:

```
main.css (entrada)
  ├── @tailwind base
  ├── @tailwind components
  └── @tailwind utilities
       │
       ▼ (npm run watch:tw compila para style.css)
     style.css (compilada, 150KB fonte)
       │
       ▼ (Hugo Pipes: resources.Get "css/style.css" | postCSS)
     postcss.config.js aplica { tailwindcss, autoprefixer }
       │
       ▼ (produção: | minify | fingerprint | resources.PostProcess)
     docs/css/style.min.<hash>.css
```

Alpine.js vem via CDN, Hugo processa imagens via `.Resize/.Fit`, sem bundler JS explícito.

## Alternativa 1 — Manter Tailwind 3 e PostCSS (statu quo)

### Vantagens

- **Zero risco visual imediato.** Nenhuma classe renomeada, nenhum default alterado.
- Ambiente já validado em CI e produção há meses.
- Nenhum retrabalho em `printf` de `people/single.html`.
- Documentação Tailwind 3 abundante, comunidade estável.
- `autoprefixer` continua garantindo compatibilidade retroativa (Safari <16.4, Chrome antigos, IE legacy).

### Desvantagens

- **Tailwind 3.4 é a linha final da série 3.** Fim de vida próximo. Fixes de segurança tendem a diminuir.
- Contínua duplicidade de execução Tailwind (CLI local + PostCSS no Hugo).
- `postcss.config.js` + `autoprefixer` + `browserslist` + `caniuse-lite` = 4 deps que Tailwind 4 dispensa.
- Cadeia de dependências mais longa = mais superfície de vulnerabilidade a longo prazo.
- Padrão do ecossistema move-se para v4 — cada issue novo de Alpine, plugin ou tema pode assumir v4.

### Complexidade de manutenção

Muito baixa. Nada muda. Custo: monitorar CVEs em `autoprefixer`/`postcss-cli`/`browserslist`.

### Risco

Baixo no curto prazo, médio no longo prazo (obsolescência).

### Esforço

Zero.

## Alternativa 2 — Tailwind 4 com PostCSS (sem Vite)

### Vantagens

- **Preserva Hugo Pipes.** Continuamos usando `resources.Get "css/main.css" | postCSS`. Zero mudança na pipeline de fingerprint/integridade/minify já validada.
- **Remove `autoprefixer`, `browserslist`, `caniuse-lite`.** Tailwind 4 gerencia prefixos e polyfills internamente via `@property` e `color-mix()`.
- **Remove `postcss-cli`** (nunca foi invocado — dep órfã).
- Substitui `tailwindcss` (plugin) por `@tailwindcss/postcss` (plugin oficial v4).
- Novo CSS mais rápido no build (v4 tem engine reescrito em Rust — Oxide).
- `@tailwindcss/typography` continua compatível (v0.5.20 já suporta v4).
- **Migração automática via `npx @tailwindcss/upgrade`** cuida de:
  - `@tailwind` → `@import "tailwindcss"`
  - Renames de shadow/rounded/blur
  - `text-opacity-*` → `<color>/<opacity>`
  - `flex-shrink-*` → `shrink-*`
- Custo cognitivo baixo — desenvolvedores familiares com Tailwind continuam produtivos.

### Desvantagens

- Requer navegadores modernos: **Safari 16.4+, Chrome 111+, Firefox 128+**. Pode haver impacto se público institucional tiver navegador desatualizado.
- Border color default = `currentColor` (era `gray-200`) — requer auditoria manual visual pós-migração em ~20 elementos que usam `border` sem cor.
- `ring` sem número default mudou de 3px para 1px — 2 elementos identificados no repo.
- Nova sintaxe de arbitrary values (`bg-(--var)` em vez de `bg-[--var]`) — verificar grep antes.
- Config em JS ainda funciona via `@config`, mas o padrão v4 é CSS-first (`@theme`). Adotar CSS-first requer reescrever `tailwind.config.js` como `assets/css/theme.css` — custo médio, ganho baixo.

### Complexidade de manutenção

Baixa. Pipeline igual, uma dep a menos, sintaxe muito próxima do v3.

### Compatibilidade

- Node.js: ≥20 ✓ (temos 24)
- Hugo: `postCSS` continua funcionando ✓
- Browsers: Safari 16.4+ = março/2023; Chrome 111 = março/2023; Firefox 128 = julho/2024. Cobertura hoje >97% globalmente, mas depende do público real do CEDIS.

### Desempenho esperado

- Build local mais rápido (Oxide engine)
- CSS gerado ligeiramente menor (novo tree-shaking)
- Não muda runtime do browser (mesmo output CSS estático)

### Risco

**Médio.** Renames automáticos cobrem ~80% do trabalho, mas 27 substituições diretas + 20+ revisões manuais visuais são reais.

### Esforço

Estimado 8-16h de dev experiente, distribuído em ~3 dias com validação.

### Recomendação

**Preferida** para este repositório.

## Alternativa 4 — Tailwind 4 integrado nativamente ao Hugo (`css.TailwindCSS`)

Hugo 0.164 suporta a função `css.TailwindCSS` (introduzida em v0.161). Ela substitui `postCSS` no Hugo Pipes, chama diretamente o `@tailwindcss/cli` e elimina a necessidade de PostCSS e Autoprefixer no repositório.

### Como funciona

**Pré-requisitos:**

- `tailwindcss@4`, `@tailwindcss/cli@4`, `@tailwindcss/typography@0.5.20`
- `[build.buildStats] enable = true` em `hugo.yaml` — Hugo gera `hugo_stats.json` no root do projeto durante build, listando todas as classes/IDs/tags renderizados
- `@source "hugo_stats.json"` em `main.css` — Tailwind lê o stats para saber quais classes existem
- `hugo_stats.json` no `.gitignore` — arquivo temporário
- `templates.Defer` no partial que gera `<link rel="stylesheet">` — para site multilíngue, garante que Tailwind compile SÓ depois de renderizar todos os idiomas
- Cachebusters para invalidar cache Hugo quando `tailwind.config.js` mudar (já configurado hoje em `hugo.yaml`)

**Uso em `head.html`:**

```go-html-template
{{ with (templates.Defer (dict "key" "global")) }}
  {{ with resources.Get "css/main.css" }}
    {{ $opts := dict "minify" (not hugo.IsDevelopment) }}
    {{ with . | css.TailwindCSS $opts }}
      {{ if hugo.IsDevelopment }}
        <link rel="stylesheet" href="{{ .RelPermalink }}">
      {{ else }}
        {{ with . | fingerprint }}
          <link rel="stylesheet" href="{{ .RelPermalink }}"
                integrity="{{ .Data.Integrity }}" crossorigin="anonymous">
        {{ end }}
      {{ end }}
    {{ end }}
  {{ end }}
{{ end }}
```

**Novo `main.css`:**

```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";
@source "hugo_stats.json";
```

O `@config "../../tailwind.config.js"` pode ser adicionado se quisermos manter o JS config como fonte de verdade para tokens/colors/etc.

### Vantagens

- **Elimina PostCSS pipeline** — mais simples que Alt 2. Remove também `@tailwindcss/postcss`.
- **Cache Hugo integrado** — Hugo Pipes trata cache e invalidação de forma coerente com resto do build.
- **`.Data.Integrity` continua funcionando** — mesma pipeline `resources.Fingerprint` do Hugo.
- **`hugo_stats.json` é a fonte de classes** — sem precisar declarar `content:` ou `@source layouts/**/*.html`. Hugo sabe exatamente quais classes chegaram a ser renderizadas.
- Alinhado com direção oficial do Hugo (recomendado desde v0.161).
- Sem dev-server duplo, sem manifest paralelo.

### Desvantagens

- **`hugo_stats.json` é gerado por idioma:** se apenas um idioma for renderizado (ex.: erro em i18n do outro), CSS ficará incompleto. **`templates.Defer` mitiga**, mas exige verificação em ambos os idiomas.
- **Feature relativamente nova** — menos rodagem em produção que PostCSS clássico.
- Se algum shortcode gerar classe condicionalmente (ex.: `{{ if eq $type "phd" }}bg-red-500{{ end }}`) apenas para conteúdo raro, `hugo_stats.json` pode não capturar em build de teste — necessário rodar build completa antes de deploy.
- `templates.Defer` requer chave global (`dict "key" "global"`) — se usado incorretamente, causa condições de corrida.
- Sem fallback simples se `@tailwindcss/cli` estiver ausente — comando `hugo` falha.

### Compatibilidade

- Hugo: ≥0.161 ✓ (temos 0.164.0)
- Hugo Extended: **não é estritamente necessário** para `css.TailwindCSS`, mas Extended é o padrão do projeto e do CI (imagens WebP dependem dele).
- Node.js: idem Alt 2 (≥20).
- Alpine.js: qualquer (independente).
- `@tailwindcss/typography`: `@plugin` no CSS-first, funciona idêntico ao Alt 2.

### Desempenho

- Build local: potencialmente mais rápido (menos passos de pipeline; direto Hugo → Tailwind CLI Rust).
- Runtime browser: idêntico (mesmo CSS estático).

### Multilíngue — cuidado extra

O CEDIS renderiza cada rota em PT e EN. `hugo_stats.json` precisa capturar classes de **todos** os templates renderizados. Sem `templates.Defer`, o partial `head.html` executa por página no início da renderização — antes de todo `hugo_stats.json` estar completo.

**Com `templates.Defer`:** o bloco defer executa após tudo mais, na renderização final. Aí sim `hugo_stats.json` cobre PT e EN.

**Sem templates.Defer:** risco de CSS incompleto em uma das linguagens. Não usar.

### Complexidade de manutenção

Baixa a média. Substitui um plugin (postcss) por outro (`css.TailwindCSS`). Exige aprender `[build.buildStats]` e `templates.Defer`.

### Risco

**Médio.** Feature nova, mas oficial e bem documentada. Rollback trivial (`git checkout head.html main.css`).

### Esforço

Estimado 6-10h — comparável a Alt 2. Um pouco mais na configuração inicial (`buildStats`, `templates.Defer`), um pouco menos na desinstalação de deps (não precisa `@tailwindcss/postcss`).

### Reversibilidade

Fácil — mesma branch local dev, `git checkout` restaura estado anterior.

## Alternativa 3 — Tailwind 4 com Vite

### Vantagens

- Ecossistema moderno: **`@tailwindcss/vite`** é o plugin oficial recomendado pela equipe Tailwind.
- HMR (Hot Module Replacement) local mais rápido — feedback quase instantâneo em desenvolvimento.
- Vite abstrai bundling de JS futuro (se um dia migrarmos Alpine para bundle local ou adicionarmos código JS mais complexo).
- Pipeline padrão do TailBliss atual (referência de compatibilidade).

### Desvantagens

- **Reescrita da integração Hugo.** Hugo Pipes tem `resources.Get + postCSS` como abstração central. Vite gera CSS/JS independentemente e produz um manifest (`manifest.json`) que precisa ser lido para resolver hashes.
- Precisa reconfigurar `head.html` para ler manifest do Vite (via `getJSON` ou `resources.Get` de arquivo de manifest) OU abandonar fingerprint do Hugo e adotar hashing do Vite.
- Perde integração nativa com `.Fingerprint` + `.Integrity` do Hugo Pipes (usada em `head.html:74,82`).
- Introduz dependência de porta de dev-server extra (Vite dev-server na porta 5173 além do Hugo server na 1313).
- Configuração dupla: `vite.config.ts` + hugo continua rodando; comandos npm ficam mais complexos.
- Sem benefício claro para site 100% estático sem SPA — Vite é essencialmente um bundler de aplicações JS.
- `concurrently` continua necessário (ou substituído por Vite plugin que roda Hugo).

### Complexidade de manutenção

Alta. Dois sistemas de build ativos, dev-server duplo, manifest.json entre eles. Rollback difícil.

### Compatibilidade

- Node.js: `^20.19.0 || >=22.12.0` (Vite 8.x) ✓ (temos 24)
- Requer aprender configuração Vite se o time é novo nisso.

### Desempenho esperado

- HMR local ~10x mais rápido em CSS
- Build de produção: sem diferença significativa (mesmo output)

### Risco

**Alto.** Reescreve fundamento da pipeline de assets. Rollback difícil.

### Esforço

Estimado 40-60h de dev experiente. Muito maior que Alt 2.

### Recomendação

**Não recomendada** neste momento. Considerar apenas se surgir necessidade concreta (SPA, chunk splitting JS, etc.).

## Tabela consolidada (4 alternativas)

| Critério | Alt 1 — Statu quo | Alt 2 — v4 + PostCSS | Alt 3 — v4 + Vite | Alt 4 — v4 nativo Hugo |
|---|---|---|---|---|
| **Benefícios** | Zero risco imediato | Deps menores, engine Oxide | HMR agressivo | Menor cadeia possível, pipeline Hugo integrada |
| **Desvantagens** | Fim de vida | Verificações visuais manuais | Reescrita pipeline, dev-server duplo | Feature nova, precisa `templates.Defer` para PT/EN |
| **Complexidade** | Baixa | Média | Alta | Média |
| **Compatibilidade Hugo** | qualquer | qualquer | qualquer | ≥0.161 ✓ (temos 0.164) |
| **Compatibilidade Hugo Extended** | opcional | opcional | opcional | opcional (mas Extended usado hoje) |
| **Compatibilidade Node** | Qualquer | ≥20 (temos 24) ✓ | ≥20.19 (temos 24) ✓ | ≥20 (temos 24) ✓ |
| **Compatibilidade Browser** | Ampla | Safari 16.4+ / Chrome 111+ / Firefox 128+ | Idem Alt 2 | Idem Alt 2 |
| **Desempenho build** | Baseline | Melhor (Oxide) | Melhor | Melhor (Oxide direto, sem PostCSS) |
| **Deps removidas** | 0 | postcss-cli, autoprefixer, browserslist, caniuse-lite | Idem Alt 2 | Idem Alt 2 + PostCSS (fica só transitive se necessário) |
| **Deps adicionadas** | 0 | @tailwindcss/postcss | vite, @tailwindcss/vite | @tailwindcss/cli |
| **Alpine.js integração** | CDN igual | CDN igual | Vite bundle possível | CDN igual (ou `js.Build` se quiser bundle) |
| **Site multilíngue (PT/EN)** | OK | OK | OK | Requer `templates.Defer` explícito |
| **`@tailwindcss/typography`** | plugins:[] JS | idem OU `@plugin` CSS | idem | `@plugin "@tailwindcss/typography"` em CSS |
| **Facilidade de deploy** | idem | idem | idem | idem — só muda pipeline CSS |
| **Impacto sobre GitHub Pages** | zero | zero | zero | zero — mesmo `docs/` |
| **Preservação `.Data.Integrity`** | ✓ (postCSS) | ✓ (postCSS) | ✗ (Vite não gera) | ✓ (Hugo Pipes) |
| **Proximidade do TailBliss atual** | distante | próximo | idêntico | próximo (mais Hugo-idiomático) |
| **Manutenção futura** | Aumenta | Menor | Aumenta (dois builds) | Menor |
| **Risco de regressão** | Nulo | Médio | Alto | Médio |
| **Esforço** | 0h | 8-16h | 40-60h | 6-10h |
| **Reversibilidade** | N/A | Fácil | Difícil | Fácil |
| **Recomendação** | Só se bloqueador | Aceitável | Adiar | **Preferida** |

## Justificativa da recomendação — atualizada com Alt 4

**Recomendação atualizada: Alternativa 4 (Tailwind 4 nativo Hugo via `css.TailwindCSS`)**, com Alt 2 como fallback se `templates.Defer` + `hugo_stats.json` provarem-se instáveis em teste.

### Por que Alt 4 > Alt 2

- Elimina PostCSS pipeline totalmente (Alt 2 troca plugin PostCSS por outro; Alt 4 remove PostCSS do repo).
- Hugo passa a ser o **único** orquestrador de assets — pipeline mais coerente.
- Cache e invalidação sob controle Hugo (não duplicada).
- Alinhado com direção oficial recomendada pelo Hugo desde v0.161.
- Cadeia de dependências mínima: `tailwindcss@4 + @tailwindcss/cli + @tailwindcss/typography`.

### Por que não Alt 3 (Vite)

- Reescreve o `head.html`, perde `.Data.Integrity` do Hugo Pipes, adiciona dev-server duplo.
- Não há benefício claro para site 100% estático sem JS complexo.
- Rollback caro.
- TailBliss usa Vite não por necessidade técnica desse tema, mas por padrão da comunidade JS moderna. Para nossa arquitetura Hugo-centric, Vite é fricção.

### Condição para migrar Alt 4

Spike de 4h antes da migração real para validar:

1. `hugo_stats.json` gerado inclui classes de PT e EN.
2. `templates.Defer` funciona com nossa estrutura de `head.html`.
3. `resources.Fingerprint` continua produzindo integrity hash.
4. `hugo server --disableFastRender` recarrega CSS ao alterar template.

Se qualquer critério falhar, **cair para Alt 2** (custo idêntico de migração).

## Justificativa histórica — antes do complemento

**Adotar Alternativa 2 (Tailwind 4 + PostCSS + Hugo Pipes).**

Razões:

1. **Ganho arquitetural real:** 4 dependências removidas (postcss-cli, autoprefixer, browserslist, caniuse-lite) simplificam a superfície de manutenção e reduzem CVEs futuros.
2. **Pipeline Hugo intacto:** todo o investimento em Hugo Pipes (fingerprint, integrity, WebP resize, minify) é preservado.
3. **Migração automatizada:** `npx @tailwindcss/upgrade` cobre ~80% do trabalho mecânico.
4. **Baixa fricção com o CI:** o `site-ci.yml` atual continua funcionando com uma linha alterada (o `postcss.config.js`).
5. **Reversibilidade:** branch local + tag pré-migração garante rollback trivial.
6. **Sem benefício claro do Vite para site 100% estático:** o CEDIS não tem SPA, o JS é 90% Alpine via CDN, o CSS não precisa de HMR sofisticado. Vite adiciona complexidade sem retorno.

Riscos aceitos:

- Auditoria visual manual de ~20 elementos (borders sem cor).
- Perda potencial de suporte a Safari <16.4 e Chrome <111 (verificar público real via GA antes de aprovar).
- Vetor de regressão no primeiro build v4 até validar pa11y + lighthouse.

## Se Alternativa 3 for exigida no futuro

Condições necessárias:

- Necessidade concreta identificada (ex.: adicionar SPA para dashboard interno, mover Alpine para bundle local por CSP, adicionar TypeScript com type-checking em build).
- Ciclo separado de migração após Tailwind 4 estar estável em produção.
- Reescrita da integração Hugo Pipes → Vite manifest documentada em ADR.
- Redesign do `head.html` para ler manifest do Vite.

Não fazer as duas migrações no mesmo ciclo.
