// แปลง slides.html → PDF และตรวจว่าไม่มีเนื้อหาล้นสไลด์
// ใช้: node render.js slides.html out.pdf
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [input, output] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
  await page.waitForFunction(() => window.__fitted === true, null, { timeout: 60000 });

  const report = await page.evaluate(() => {
    const out = [], small = [];
    document.querySelectorAll('.slide').forEach((s, i) => {
      const sr = s.getBoundingClientRect();
      s.querySelectorAll('.card, .fit, .ans, .figbox, .fig, .steps, .hint, .ansrow, .sum div').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.bottom > sr.bottom - 40 || r.right > sr.right - 1)
          out.push(`slide ${i + 1}: ${el.className.baseVal ?? el.className} past slide edge`);
      });
      s.querySelectorAll('.fit').forEach(el => {
        if (el.scrollHeight > el.clientHeight + 1) out.push(`slide ${i + 1}: text clipped (font ${el.dataset.final}px)`);
        if (+el.dataset.final < 18) small.push(`slide ${i + 1}: font ${el.dataset.final}px`);
      });
      s.querySelectorAll('.card').forEach(el => {
        if (el.scrollHeight > el.clientHeight + 1) out.push(`slide ${i + 1}: card content clipped`);
      });
    });
    return { out, small, n: document.querySelectorAll('.slide').length };
  });

  await page.pdf({ path: output, preferCSSPageSize: true, printBackground: true });
  await browser.close();
  if (report.small.length) console.log('small text:\n  ' + report.small.join('\n  '));
  if (report.out.length) { console.error('OVERFLOW:\n  ' + report.out.join('\n  ')); process.exit(1); }
  console.log(`ok: ${output} — ${report.n} slides, no overflow`);
})();
