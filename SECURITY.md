## Política de Segurança

Este repositório publica um site estático (Hugo → `docs/`). Todo o JavaScript enviado a visitantes vem de `assets/` e do tema; nenhuma `devDependency` de npm chega ao bundle.

### Como reportar uma vulnerabilidade

Envie um e-mail para a equipe do CEDIS ou abra um issue privado neste repositório. Retornamos em até 5 dias úteis.

### Aceitação de risco: `extract-zip@2.0.1` (GHSA-jmr9-qjv8-65gv)

O Dependabot sinaliza `extract-zip` como transitivo de `pa11y-ci → puppeteer → @puppeteer/browsers`. Não há patch publicado no npm (o último release continua `2.0.1`).

- **Superfície**: `extract-zip` só é executado quando o `puppeteer` baixa o Chromium do CDN do Google durante `npm install`.
- **Vetor**: exige que um `.zip` malicioso seja fornecido ao extrator — no nosso pipeline, isso significaria comprometer o CDN oficial do Chromium.
- **Blast radius**: ambiente local do desenvolvedor ou runner de CI. Nenhum código de produção é afetado.
- **Ação**: risco aceito até `pa11y-ci` bumpar `puppeteer` (ou `extract-zip` receber patch upstream). Revalidar a cada `npm outdated`.

Os 8 demais alertas listados por `npm audit` (`@puppeteer/browsers`, `puppeteer`, `puppeteer-core`, `pa11y`, `pa11y-ci`, `lighthouse`, `@lhci/cli`, `@lhci/utils`) são efeitos transitivos do mesmo `extract-zip` e se resolvem no mesmo bump.
