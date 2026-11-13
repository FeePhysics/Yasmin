// แปลง HTML → PDF และตรวจว่าไม่มีกล่องล้นหน้า
// ใช้: node render.js exam.html exam.pdf
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [input, output] = process.argv.slice(2);
  if (!input || !output) {
    console.error('usage: node render.js <in.html> <out.pdf>');
    process.exit(2);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(input), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);

  // ตรวจทุกกล่องในแต่ละ .page ว่าไม่เลยขอบล่าง/ขวาของหน้า
  const problems = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((pg, i) => {
      const pr = pg.getBoundingClientRect();
      pg.querySelectorAll('.box, .head, img, svg, table').forEach((el) => {
        if (el.classList.contains('wm')) return;
        const r = el.getBoundingClientRect();
        if (r.bottom > pr.bottom - 1 || r.right > pr.right - 1) {
          out.push(`page ${i + 1}: ${el.className || el.tagName} overflows by ` +
            `${Math.max(r.bottom - pr.bottom, r.right - pr.right).toFixed(1)}px`);
        }
      });
      pg.querySelectorAll('.box').forEach((b, j) => {
        if (b.scrollHeight > b.clientHeight + 1 || b.scrollWidth > b.clientWidth + 1)
          out.push(`page ${i + 1}: box #${j + 1} content clipped inside its frame`);
      });
      if (pg.scrollHeight > pg.clientHeight + 1)
        out.push(`page ${i + 1}: content taller than page (${pg.scrollHeight} > ${pg.clientHeight})`);
    });
    return out;
  });

  await page.pdf({ path: output, preferCSSPageSize: true, printBackground: true });
  await browser.close();

  if (problems.length) {
    console.error('OVERFLOW:\n  ' + problems.join('\n  '));
    process.exit(1);
  }
  console.log(`ok: ${output} (no overflow)`);
})();
