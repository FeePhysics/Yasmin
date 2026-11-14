// SVG figure helpers for the tutoring slides
const C = { navy: '#1e2a5a', blue: '#2f6fb5', sky: '#4aa3df', skyL: '#e3f1fb', purple: '#6b4fbb', purpleL: '#efe9fb', gray: '#6b7280', grayL: '#e5e7eb', shade: '#b9c4d6' };

function svg(w, h, body, maxW) {
  return `<svg class="fig" viewBox="0 0 ${w} ${h}" style="max-width:${maxW || w}px" xmlns="http://www.w3.org/2000/svg">${body}</svg>`;
}

/* บัตรตัวเลข */
function cards(nums) {
  const w = 54, g = 12, W = nums.length * (w + g) - g + 8;
  let b = '';
  nums.forEach((n, i) => {
    const x = 4 + i * (w + g);
    b += `<rect x="${x}" y="4" width="${w}" height="66" rx="8" fill="#fff" stroke="${C.navy}" stroke-width="3"/>` +
         `<text x="${x + w / 2}" y="50" font-size="32" font-weight="700" text-anchor="middle" fill="${C.navy}">${n}</text>`;
  });
  return svg(W, 74, b, W);
}

/* รูปทรงบนตาชั่ง */
function shape(kind, x, base, s) {
  const st = `fill="#fff" stroke="${C.navy}" stroke-width="3"`;
  if (kind === 'tri') return `<polygon points="${x},${base} ${x + s},${base} ${x + s / 2},${base - s}" ${st}/>`;
  if (kind === 'sq') return `<rect x="${x + 2}" y="${base - s + 4}" width="${s - 4}" height="${s - 4}" ${st}/>`;
  if (kind === 'cir') return `<circle cx="${x + s / 2}" cy="${base - s / 2}" r="${s / 2 - 1}" ${st}/>`;
  if (kind === 'star') {
    const cx = x + s / 2, cy = base - s / 2, R = s / 2, r = R * 0.45;
    let p = [];
    for (let i = 0; i < 10; i++) {
      const a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? r : R;
      p.push(`${(cx + rr * Math.cos(a)).toFixed(1)},${(cy + rr * Math.sin(a)).toFixed(1)}`);
    }
    return `<polygon points="${p.join(' ')}" fill="${C.purpleL}" stroke="${C.purple}" stroke-width="3"/>`;
  }
  return '';
}
function balances(list) {
  const unit = 230, s = 40;
  let b = '';
  list.forEach((sc, i) => {
    const ox = i * unit, cx = ox + unit / 2, n = sc.items.length, totalW = n * (s + 4) - 4;
    let x = cx - totalW / 2;
    sc.items.forEach(k => { b += shape(k, x, 60, s); x += s + 4; });
    b += `<rect x="${cx - 95}" y="60" width="190" height="8" rx="3" fill="${C.navy}"/>` +
         `<rect x="${cx - 4}" y="68" width="8" height="14" fill="${C.navy}"/>` +
         `<polygon points="${cx - 70},82 ${cx + 70},82 ${cx + 95},145 ${cx - 95},145" fill="${C.skyL}" stroke="${C.navy}" stroke-width="3"/>` +
         `<rect x="${cx - 48}" y="94" width="96" height="38" rx="5" fill="#fff" stroke="${C.navy}" stroke-width="2.5"/>` +
         `<text x="${cx}" y="121" font-size="22" font-weight="700" text-anchor="middle" fill="${C.navy}">${sc.w}</text>` +
         `<text x="${cx}" y="175" font-size="22" font-weight="600" text-anchor="middle" fill="${C.gray}">${sc.label}</text>`;
  });
  return svg(list.length * unit, 185, b, list.length * unit);
}

/* จัตุรัสสามรูปในจัตุรัสใหญ่ (ข้อ 9) */
function squares3(A, B, Cc, px) {
  const a = Math.sqrt(A), b = Math.sqrt(B), c = Math.sqrt(Cc), S = a + b + c, k = px / S, P = 6;
  const r = (x, y, w, h, fill) => `<rect x="${P + x * k}" y="${P + y * k}" width="${w * k}" height="${h * k}" fill="${fill}" stroke="${C.navy}" stroke-width="3"/>`;
  const t = (x, y, w, h, v) => `<text x="${P + (x + w / 2) * k}" y="${P + (y + h / 2) * k + 9}" font-size="26" font-weight="700" text-anchor="middle" fill="${C.navy}">${v}</text>`;
  let g = r(0, 0, S, S, C.shade) + r(0, 0, a, a, '#fff') + r(a, a, b, b, '#fff') + r(a + b, a + b, c, c, '#fff') +
          r(a, 0, S - a, a, C.shade) + r(0, a, a, S - a, C.shade) + r(a + b, a, c, b, C.shade) + r(a, a + b, b, c, C.shade);
  g += t(0, 0, a, a, A) + t(a, a, b, b, B) + t(a + b, a + b, c, c, Cc);
  return svg(px + 2 * P, px + 2 * P, g, px + 2 * P);
}

/* ตารางจุด */
function dots(rows, cols) {
  const g = 64, P = 20;
  let b = '';
  for (let i = 0; i < rows; i++) for (let j = 0; j < cols; j++)
    b += `<circle cx="${P + j * g}" cy="${P + i * g}" r="8" fill="${C.navy}"/>`;
  return svg(2 * P + (cols - 1) * g, 2 * P + (rows - 1) * g, b, 2 * P + (cols - 1) * g);
}

/* รูปหลายเหลี่ยมต่อกัน (ไม้ขีด) — รูปถัดไปได้จากการหมุน 180° รอบจุดกึ่งกลางด้านขวาสุด */
function polyChain(sides, count, size) {
  let pts = [];
  const R = size / (2 * Math.sin(Math.PI / sides));
  const start = sides === 4 ? -Math.PI / 4 * 3 : sides === 6 ? -Math.PI / 2 : -Math.PI / 2;
  for (let i = 0; i < sides; i++) {
    const a = start + i * 2 * Math.PI / sides;
    pts.push([R * Math.cos(a), R * Math.sin(a)]);
  }
  const polys = [pts];
  for (let k = 1; k < count; k++) {
    const cur = polys[k - 1];
    let best = 0, bx = -1e9;
    for (let i = 0; i < sides; i++) {
      const p = cur[i], q = cur[(i + 1) % sides], mx = (p[0] + q[0]) / 2;
      if (mx > bx + 1e-6) { bx = mx; best = i; }
    }
    const p = cur[best], q = cur[(best + 1) % sides], m = [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2];
    polys.push(cur.map(v => [2 * m[0] - v[0], 2 * m[1] - v[1]]));
  }
  let xs = polys.flat().map(v => v[0]), ys = polys.flat().map(v => v[1]);
  const minX = Math.min(...xs), minY = Math.min(...ys), P = 12;
  const W = Math.max(...xs) - minX + 2 * P + 50, H = Math.max(...ys) - minY + 2 * P;
  let b = '';
  polys.forEach(pl => {
    for (let i = 0; i < sides; i++) {
      const p = pl[i], q = pl[(i + 1) % sides];
      b += `<line x1="${p[0] - minX + P}" y1="${p[1] - minY + P}" x2="${q[0] - minX + P}" y2="${q[1] - minY + P}" stroke="#c98b3a" stroke-width="5" stroke-linecap="round"/>`;
      b += `<circle cx="${p[0] - minX + P}" cy="${p[1] - minY + P}" r="5" fill="#d64545"/>`;
    }
  });
  b += `<text x="${W - 40}" y="${H / 2 + 10}" font-size="34" font-weight="700" fill="${C.navy}">…</text>`;
  return svg(W, H, b, W);
}

/* ข้อ 19: สี่เหลี่ยม EFGB มีจัตุรัส ABCD มุมขวาบน */
function fig19(ea, cg, s) {
  const k = 22, P = 30, W = (ea + s) * k, H = (s + cg) * k;
  const X = v => P + v * k, Y = v => P + v * k;
  let b = `<rect x="${X(0)}" y="${Y(0)}" width="${W}" height="${H}" fill="${C.shade}" stroke="${C.navy}" stroke-width="3"/>` +
          `<rect x="${X(ea)}" y="${Y(0)}" width="${s * k}" height="${s * k}" fill="#fff" stroke="${C.navy}" stroke-width="3"/>`;
  const L = (x, y, t, a) => `<text x="${x}" y="${y}" font-size="22" font-weight="700" text-anchor="${a || 'middle'}" fill="${C.navy}">${t}</text>`;
  b += L(X(0) - 6, Y(0) - 8, 'E', 'end') + L(X(ea), Y(0) - 8, 'A') + L(X(ea + s) + 6, Y(0) - 8, 'B', 'start') +
       L(X(ea) - 6, Y(s) + 22, 'D', 'end') + L(X(ea + s) + 8, Y(s) + 8, 'C', 'start') +
       L(X(0) - 6, Y(s + cg) + 22, 'F', 'end') + L(X(ea + s) + 6, Y(s + cg) + 22, 'G', 'start');
  b += `<text x="${X(ea / 2)}" y="${Y(0) - 8}" font-size="22" font-weight="700" text-anchor="middle" fill="${C.purple}">${ea}</text>` +
       `<text x="${X(ea + s) + 10}" y="${Y(s + cg / 2) + 8}" font-size="22" font-weight="700" fill="${C.purple}">${cg}</text>`;
  return svg(W + 2 * P + 30, H + 2 * P + 10, b, W + 2 * P + 30);
}

/* ข้อ 30: จัตุรัสเล็กวางซ้อนในจัตุรัสใหญ่ ชิดขอบบน */
function fig30() {
  const P = 10, B = 200, s = 160, o = (B - s) / 2;
  const b = `<rect x="${P}" y="${P}" width="${B}" height="${B}" fill="${C.shade}" stroke="${C.navy}" stroke-width="3"/>` +
            `<rect x="${P + o}" y="${P}" width="${s}" height="${s}" fill="#fff" stroke="${C.navy}" stroke-width="3"/>` +
            `<line x1="${P + o}" y1="${P}" x2="${P + o + s}" y2="${P}" stroke="#fff" stroke-width="5"/>` +
            `<line x1="${P + o}" y1="${P}" x2="${P + o + s}" y2="${P}" stroke="${C.navy}" stroke-width="3" stroke-dasharray="12 9"/>`;
  return svg(B + 2 * P, B + 2 * P, b, 190);
}

/* รูปคลี่ */
function net(polys, w, h, label) {
  const st = `fill="${C.skyL}" stroke="${C.navy}" stroke-width="3" stroke-linejoin="round"`;
  let b = polys.map(p => `<polygon points="${p.map(v => v.join(',')).join(' ')}" ${st}/>`).join('');
  return `<div class="netopt"><span>${label}</span>${svg(w, h, b, w)}</div>`;
}
function fanNet() {
  // ฐานจัตุรัสด้านล่าง สามเหลี่ยม 4 หน้าเรียงรอบยอดเดียวกัน
  const sq = [[30, 150], [76, 150], [76, 196], [30, 196]];
  const apex = [53, 84], A = [30, 150], B = [76, 150];
  const ang = 2 * Math.asin(23 / Math.hypot(23, 66));
  const rot = (p, t) => { const dx = p[0] - apex[0], dy = p[1] - apex[1]; return [apex[0] + dx * Math.cos(t) - dy * Math.sin(t), apex[1] + dx * Math.sin(t) + dy * Math.cos(t)]; };
  let tris = [[apex, A, B]], prev = B;
  for (let i = 1; i <= 3; i++) { const nx = rot(B, -ang * i); tris.push([apex, prev, nx]); prev = nx; }
  const r = p => p.map(v => [+v[0].toFixed(1), +v[1].toFixed(1)]);
  return [sq, ...tris.map(r)];
}
const NETS27 = () => [
  net(fanNet(), 190, 205, '1.'),
  net([[[30, 20], [78, 20], [78, 68], [30, 68]], [[78, 20], [78, 68], [144, 44]], [[144, 44], [210, 20], [210, 68]], [[30, 68], [78, 68], [54, 134]], [[30, 68], [8, 134], [54, 134]]], 220, 145, '2.'),
  net([[[20, 20], [68, 20], [68, 68], [20, 68]], [[68, 20], [68, 68], [134, 44]], [[134, 44], [200, 20], [200, 68]], [[20, 68], [68, 68], [44, 134]], [[44, 134], [20, 200], [68, 200]]], 210, 210, '3.'),
  net([[[40, 80], [88, 80], [88, 128], [40, 128]], [[40, 80], [88, 80], [64, 14]], [[88, 80], [88, 128], [154, 104]], [[40, 128], [88, 128], [64, 194]], [[88, 128], [126, 158], [64, 194]]], 170, 205, '4.'),
];
const NETS27A = () => {
  const cross = [[[70, 70], [118, 70], [118, 118], [70, 118]], [[70, 70], [118, 70], [94, 8]], [[118, 70], [118, 118], [180, 94]], [[70, 118], [118, 118], [94, 180]], [[70, 70], [70, 118], [8, 94]]];
  const three = [[[30, 70], [78, 70], [78, 118], [30, 118]], [[30, 70], [78, 70], [54, 8]], [[78, 70], [78, 118], [140, 94]], [[30, 118], [78, 118], [54, 180]]];
  const bow = [[[30, 70], [78, 70], [78, 118], [30, 118]], [[30, 70], [78, 70], [54, 8]], [[78, 70], [78, 118], [140, 94]], [[140, 94], [202, 70], [202, 118]], [[30, 118], [78, 118], [54, 180]]];
  return [net(cross, 190, 190, '1.'), net(three, 150, 190, '2.'), net(bow, 210, 190, '3.')];
};
