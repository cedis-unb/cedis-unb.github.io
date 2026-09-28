#!/usr/bin/env node
/**
 * Varredura de contraste em MODO ESCURO sobre uma amostra de arquétipos.
 *
 * O pa11y do CI usa HTML_CodeSniffer e roda só no tema claro, então uma
 * regressão de contraste no tema escuro passava pelo build sem ser notada.
 * Este script cobre essa lacuna sem duplicar a suíte: roda apenas a regra
 * `color-contrast` do axe-core, em oito páginas que representam as famílias
 * de layout, nos dois idiomas quando o arquétipo difere entre eles.
 *
 * Uso:  node scripts/audit_dark_contrast.mjs [baseUrl]
 * Em CI, defina PUPPETEER_EXECUTABLE_PATH para o Chrome do runner.
 *
 * Limite conhecido: quando o fundo é um gradiente, o axe classifica o caso
 * como "incomplete" em vez de violação. Esses trechos exigem conferência
 * manual — ver technical-docs/acessibilidade-linha-de-base.md.
 */
import puppeteer from 'puppeteer';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const axePath = require.resolve('axe-core/axe.min.js');
const base = process.argv[2] || process.env.CEDIS_AUDIT_BASE || 'http://127.0.0.1:4173';

// Um arquétipo por família de layout, nos dois idiomas onde o template difere.
const PAGES = [
  '/',                                  // capa
  '/pt/',                               // capa PT
  '/about/',                            // institucional (fallback _default/single)
  '/pt/history/',                       // institucional com métricas
  '/categories/knowledge_areas/',       // catálogo/taxonomia
  '/pt/defesas/',                       // catálogo com filtros e estado vazio
  '/people/sergio_freitas/',            // perfil de pesquisador
  '/pt/mapa/',                          // mapa
];

const browser = await puppeteer.launch({
  executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || undefined,
  headless: true,
  args: ['--no-sandbox', '--disable-dev-shm-usage', '--lang=en-US', '--accept-lang=en-US'],
  protocolTimeout: 180000,
});

let total = 0;
const failures = [];

for (const path of PAGES) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 1000 });
  await page.evaluateOnNewDocument(() => {
    try { localStorage.setItem('color-theme', 'dark'); } catch (e) { /* ignore */ }
  });
  await page.goto(base + path, { waitUntil: 'networkidle2' });
  await page.evaluate(() => new Promise((r) => setTimeout(r, 400)));

  const isDark = await page.evaluate(() => document.documentElement.classList.contains('dark'));
  if (!isDark) {
    failures.push(`${path}: o tema escuro não foi aplicado (classe .dark ausente)`);
    await page.close();
    continue;
  }

  await page.addScriptTag({ path: axePath });
  const violations = await page.evaluate(async () => {
    const result = await window.axe.run(document, { runOnly: { type: 'rule', values: ['color-contrast'] } });
    return result.violations.flatMap((v) =>
      v.nodes.slice(0, 5).map((n) => ({
        target: n.target.join(' '),
        summary: (n.failureSummary || '').replace(/\s+/g, ' ').slice(0, 160),
      })),
    );
  });

  total += violations.length;
  if (violations.length) {
    failures.push(`${path}: ${violations.length} violações de contraste em modo escuro`);
    for (const v of violations) failures.push(`    ${v.target} :: ${v.summary}`);
  }
  console.log(`  ${violations.length === 0 ? 'OK  ' : 'FALHA'} ${path}`);
  await page.close();
}

await browser.close();

if (failures.length) {
  console.error('\nERRO: contraste insuficiente em modo escuro\n');
  for (const f of failures) console.error(f);
  process.exit(1);
}
console.log(`\nContraste em modo escuro OK: ${PAGES.length} arquétipos, 0 violações.`);
