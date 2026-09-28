#!/usr/bin/env node
/**
 * Contraste sobre fundos em GRADIENTE, nas superfícies em que o site os usa:
 * cabeçalho, rodapé, heroes e pills.
 *
 * Por que existe: quando o fundo é um gradiente, o axe não consegue decidir e
 * classifica o caso como "incomplete" em vez de violação — foi assim que os
 * rótulos do rodapé ficaram em 1,6:1 sem que o CI reclamasse. Aqui o cálculo
 * é feito contra CADA parada de cor declarada no gradiente do ancestral mais
 * próximo, que é a técnica manual usual, e reporta o pior caso.
 *
 * Uso: node scripts/audit_gradient_contrast.mjs [baseUrl]
 */
import puppeteer from 'puppeteer';

const base = process.argv[2] || 'http://127.0.0.1:4173';
const PAGES = ['/', '/pt/', '/pt/history/', '/pt/about/', '/pt/junte-se/mestrado/', '/pt/defesas/', '/people/sergio_freitas/', '/pt/mapa/'];

const browser = await puppeteer.launch({
  executablePath: process.env.PUPPETEER_EXECUTABLE_PATH || undefined,
  headless: true,
  args: ['--no-sandbox', '--disable-dev-shm-usage', '--lang=en-US', '--accept-lang=en-US'],
  protocolTimeout: 180000,
});

const rows = [];
for (const path of PAGES) {
  for (const theme of ['light', 'dark']) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 1000 });
    await page.evaluateOnNewDocument((t) => { try { localStorage.setItem('color-theme', t); } catch (e) {} }, theme);
    await page.goto(base + path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.evaluate(() => new Promise((r) => setTimeout(r, 600)));

    const found = await page.evaluate(() => {
      const cv = document.createElement('canvas'); cv.width = 1; cv.height = 1;
      const cx = cv.getContext('2d', { willReadFrequently: true });
      const toRGB = (s) => { cx.clearRect(0, 0, 1, 1); cx.fillStyle = s; cx.fillRect(0, 0, 1, 1); const d = cx.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2]]; };
      const lin = (c) => { c /= 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
      const L = ([r, g, b]) => 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b);
      const ratio = (a, b) => { const x = L(a), y = L(b); const hi = Math.max(x, y), lo = Math.min(x, y); return (hi + 0.05) / (lo + 0.05); };

      // ancestral mais próximo cujo background-image é gradiente, e as suas paradas
      const opaque = (c) => { const m = c.match(/[\d.]+/g); return m && (m.length < 4 || Number(m[3]) >= 0.99); };
      const gradStops = (el) => {
        let n = el;
        while (n && n.nodeType === 1) {
          const cs = getComputedStyle(n);
          const bi = cs.backgroundImage;
          if (bi && bi.includes('gradient')) {
            // Só as paradas OPACAS descrevem o fundo efetivo. As translúcidas
            // (véus radiais como rgba(197,39,47,0.12) e o `transparent` que o
            // navegador expande para rgba(0,0,0,0)) são tingimentos sobre a
            // base; tratá-las como cor cheia produzia razões falsas de ~1:1.
            const stops = [...bi.matchAll(/rgba?\([^)]*\)|#[0-9a-f]{3,8}\b/gi)]
              .map((m) => m[0])
              .filter((c) => { const n = c.match(/[\d.]+/g); return !c.startsWith('rgba') || (n && Number(n[3]) >= 0.95); });
            if (stops.length) return stops.map(toRGB);
          }
          // Um ancestral com cor de fundo OPACA encerra a busca: é ele o fundo
          // real, e qualquer gradiente mais acima está encoberto. Sem esta
          // guarda o cálculo comparava o texto com o gradiente da página,
          // produzindo razões falsas de 1,00:1.
          if (cs.backgroundColor && cs.backgroundColor !== 'transparent' && opaque(cs.backgroundColor)) return null;
          n = n.parentElement;
        }
        return null;
      };

      // superfícies auditadas: cabeçalho, rodapé, heroes e pills
      const SURFACES = [
        ['cabeçalho', 'div.top-0 a, div.top-0 button, div.top-0 span'],
        ['rodapé', 'footer a, footer p, footer div, footer span'],
        ['hero', 'main > section:first-of-type h1, main > section:first-of-type p, main > section:first-of-type span, article > section:first-of-type h1'],
        ['pills', '[class*="rounded-full"][class*="border"], [class*="rounded-full"][class*="bg-"]'],
      ];
      const out = [];
      for (const [surface, sel] of SURFACES) {
        document.querySelectorAll(sel).forEach((el) => {
          if (el.children.length) return;
          const txt = (el.textContent || '').trim();
          if (txt.length < 2) return;
          const r = el.getBoundingClientRect();
          if (r.width < 4 || r.height < 4) return;
          const stops = gradStops(el);
          if (!stops) return;
          const cs = getComputedStyle(el);
          const fg = toRGB(cs.color);
          const worst = Math.min(...stops.map((s) => ratio(fg, s)));
          const px = parseFloat(cs.fontSize);
          const large = px >= 24 || (parseInt(cs.fontWeight) >= 700 && px >= 18.66);
          const need = large ? 3 : 4.5;
          out.push({ surface, txt: txt.slice(0, 38), px, need, worst: +worst.toFixed(2), ok: worst >= need });
        });
      }
      return out;
    });

    for (const f of found) rows.push({ path, theme, ...f });
    await page.close();
  }
}
await browser.close();

const fails = rows.filter((r) => !r.ok);
const bySurface = {};
for (const r of rows) {
  bySurface[r.surface] ??= { n: 0, fail: 0, min: Infinity };
  bySurface[r.surface].n++;
  if (!r.ok) bySurface[r.surface].fail++;
  bySurface[r.surface].min = Math.min(bySurface[r.surface].min, r.worst);
}
console.log(`elementos de texto sobre gradiente medidos: ${rows.length}`);
for (const [s, v] of Object.entries(bySurface)) {
  console.log(`  ${s.padEnd(12)} medidos=${String(v.n).padStart(4)}  abaixo do exigido=${String(v.fail).padStart(3)}  pior razão=${v.min.toFixed(2)}:1`);
}
if (fails.length) {
  console.log('\npiores casos:');
  fails.sort((a, b) => a.worst - b.worst).slice(0, 12).forEach((f) =>
    console.log(`  ${f.worst}:1 (precisa ${f.need}) ${f.px}px [${f.theme}] ${f.path} ${f.surface} ${JSON.stringify(f.txt)}`));
}
process.exit(fails.length ? 1 : 0);
