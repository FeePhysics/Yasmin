# รูปประกอบ/ภาพอธิบายสำหรับเด็ก ป.2 — LPMC ครั้งที่ 23 (2565) ข้อ 16–30
import math
K = '#111111'; OL = '#5E6E2B'; YL = '#F2C230'; YLL = '#FFF1B8'; GRN = '#DDE8B8'; RED = '#D9534F'; GR = '#A8A8A8'
F = 'font-family="Mali, sans-serif" font-weight="700"'

def svg(w, h, body): return f'<svg class="img" viewBox="0 0 {w:.0f} {h:.0f}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'
def T(x, y, s, size=22, anchor='middle', fill=K): return f'<text x="{x:.1f}" y="{y:.1f}" {F} font-size="{size}" text-anchor="{anchor}" fill="{fill}">{s}</text>'

# ---------- 16: วงกลมมีเส้น (bit1 = เส้นตั้ง, bit2 = เส้นนอน, bit4 = ทแยง \, bit8 = ทแยง /) ----------
def sym(bits, cx, cy, r=18, sw=3):
    b = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{K}" stroke-width="{sw}"/>'
    if bits & 1: b += f'<line x1="{cx}" y1="{cy - r}" x2="{cx}" y2="{cy + r}" stroke="{K}" stroke-width="{sw}"/>'
    if bits & 2: b += f'<line x1="{cx - r}" y1="{cy}" x2="{cx + r}" y2="{cy}" stroke="{K}" stroke-width="{sw}"/>'
    d = r * 0.707
    if bits & 4: b += f'<line x1="{cx - d}" y1="{cy - d}" x2="{cx + d}" y2="{cy + d}" stroke="{K}" stroke-width="{sw}"/>'
    if bits & 8: b += f'<line x1="{cx - d}" y1="{cy + d}" x2="{cx + d}" y2="{cy - d}" stroke="{K}" stroke-width="{sw}"/>'
    return b
def overlay_table(heads, target=None, filled=True):
    n = len(heads); c = 62; P = 6; b = ''
    W = (n + 1) * c
    for i in range(n + 1):
        for j in range(n + 1):
            x, y = P + j * c, P + i * c
            res = None if (i == 0 or j == 0) else heads[i - 1] | heads[j - 1]
            fill = YL if (res is not None and target is not None and res == target and filled) else ('#F3F1E2' if i == 0 or j == 0 else '#fff')
            b += f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{fill}" stroke="{K}" stroke-width="1.5"/>'
            if i == 0 and j == 0: b += T(x + c / 2, y + c / 2 + 10, '★', 30)
            elif i == 0: b += sym(heads[j - 1], x + c / 2, y + c / 2)
            elif j == 0: b += sym(heads[i - 1], x + c / 2, y + c / 2)
            elif filled: b += sym(res, x + c / 2, y + c / 2)
    b += f'<line x1="{P + c}" y1="{P}" x2="{P + c}" y2="{P + W}" stroke="{K}" stroke-width="4"/><line x1="{P}" y1="{P + c}" x2="{P + W}" y2="{P + c}" stroke="{K}" stroke-width="4"/>'
    return svg(W + 2 * P, W + 2 * P, b)

# ---------- 17: จุดแบ่งกลุ่ม ----------
def dot_groups(sizes, label=''):
    r = 11; g = 26; b = ''; x = 14; H = 0
    cols = [YLL, GRN]
    for k, s in enumerate(sizes):
        per = 3 if s <= 6 else 4; rows = math.ceil(s / per); w = per * g + 12; h = rows * g + 14
        b += f'<rect x="{x}" y="10" width="{w}" height="{h}" rx="12" fill="{cols[k % 2]}" stroke="{OL}" stroke-width="2"/>'
        for i in range(s): b += f'<circle cx="{x + 18 + (i % per) * g}" cy="{10 + 19 + (i // per) * g}" r="{r}" fill="{OL}"/>'
        b += T(x + w / 2, 10 + h + 24, s, 20)
        x += w + 12; H = max(H, h)
    if label: b += T(x / 2, H + 66, label, 20)
    return svg(x + 4, H + (76 if label else 50), b)

# ---------- 18: ตาราง 3×3 ----------
def grid3(nums, marks=None, title=''):
    c = 64; P = 8; b = ''; marks = marks or {}
    for r in range(3):
        for cc in range(3):
            x, y = P + cc * c, P + 30 + r * c; m = marks.get((r, cc))
            b += f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{YL if m else "#fff"}" stroke="{K}" stroke-width="2"/>'
            t = nums[r][cc] if nums else ''
            b += T(x + c / 2, y + c / 2 + 8, t, 24)
            if m: b += T(x + c - 10, y + 18, m, 16, fill=RED)
    if title: b += T(P + 1.5 * c, P + 20, title, 18)
    return P + 3 * c + P, P + 30 + 3 * c + P, b
def grid_pair(a, b_, ta, tb, arrow):
    w1, h1, s1 = grid3(*a, title=ta); w2, h2, s2 = grid3(*b_, title=tb)
    gap = 110
    body = s1 + f'<g transform="translate({w1 + gap},0)">{s2}</g>'
    body += f'<line x1="{w1 + 12}" y1="{h1 / 2 + 15}" x2="{w1 + gap - 14}" y2="{h1 / 2 + 15}" stroke="{OL}" stroke-width="4"/><polygon points="{w1 + gap - 14},{h1 / 2 + 7} {w1 + gap - 2},{h1 / 2 + 15} {w1 + gap - 14},{h1 / 2 + 23}" fill="{OL}"/>'
    body += T(w1 + gap / 2, h1 / 2 + 2, arrow, 15, fill=OL)
    return svg(w1 + gap + w2, max(h1, h2), body)

# ---------- 19: ป้าย ----------
def cards(labels, vals=None):
    w = 70; g = 26; b = ''
    for i, L in enumerate(labels):
        x = 10 + i * (w + g)
        b += f'<rect x="{x}" y="10" width="{w}" height="70" rx="6" fill="#fff" stroke="{K}" stroke-width="3"/>' + T(x + w / 2, 55, L, 28)
        if vals: b += f'<rect x="{x + 8}" y="92" width="{w - 16}" height="46" rx="8" fill="{YL}"/>' + T(x + w / 2, 124, vals[i], 26)
    return svg(20 + len(labels) * (w + g) - g, 150 if vals else 90, b)

# ---------- 20: วงล้อ ----------
def pie(vals, hl=None, darts=0):
    cx = cy = 150; r = 130; n = len(vals); b = ''
    for i, v in enumerate(vals):
        a0, a1 = -90 + i * 360 / n, -90 + (i + 1) * 360 / n
        p0 = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))); p1 = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
        fill = YL if hl is not None and i == hl else '#fff'
        b += f'<path d="M{cx},{cy} L{p0[0]:.1f},{p0[1]:.1f} A{r},{r} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} Z" fill="{fill}" stroke="{K}" stroke-width="3"/>'
        am = math.radians((a0 + a1) / 2); b += T(cx + r * 0.62 * math.cos(am), cy + r * 0.62 * math.sin(am) + 9, v, 24)
    if darts and hl is not None:
        a0 = -90 + hl * 360 / n; a1 = a0 + 360 / n
        for k in range(darts):
            am = math.radians(a0 + (k + 1) * (a1 - a0) / (darts + 1)); rr = r * 0.85
            b += f'<circle cx="{cx + rr * math.cos(am):.1f}" cy="{cy + rr * math.sin(am):.1f}" r="7" fill="{RED}" stroke="#fff" stroke-width="2"/>'
    return svg(300, 300, b)

# ---------- 21: วงกลมสองวงซ้อน ----------
def two_rings(vals=None, hl=()):
    pos = {'TL': (70, 60), 'BL': (70, 200), 'a': (200, 60), 'b': (200, 200), 'TR': (330, 60), 'BR': (330, 200)}
    b = f'<ellipse cx="135" cy="130" rx="125" ry="95" fill="none" stroke="{K}" stroke-width="4"/><ellipse cx="265" cy="130" rx="125" ry="95" fill="none" stroke="{K}" stroke-width="4"/>'
    for k, (x, y) in pos.items():
        b += f'<circle cx="{x}" cy="{y}" r="28" fill="{YL if k in hl else "#fff"}" stroke="{K}" stroke-width="3"/>'
        t = vals[k] if vals else (k if k in 'ab' else '')
        b += T(x, y + 9, t, 26)
    return svg(400, 260, b)

# ---------- 22: พับกระดาษ ----------
def square_holes(holes, folds=(), size=200, label=''):
    P = 12; s = size; b = f'<rect x="{P}" y="{P}" width="{s}" height="{s}" fill="#fff" stroke="{K}" stroke-width="3"/>'
    L = {'d1': (0, 1, 1, 0), 'd2': (0, 0, 1, 1), 'v': (.5, 0, .5, 1), 'h': (0, .5, 1, .5)}
    for f in folds:
        x0, y0, x1, y1 = L[f]; b += f'<line x1="{P + x0 * s}" y1="{P + y0 * s}" x2="{P + x1 * s}" y2="{P + y1 * s}" stroke="{OL}" stroke-width="2.5" stroke-dasharray="9 7"/>'
    for (x, y) in holes: b += f'<circle cx="{P + x * s:.1f}" cy="{P + (1 - y) * s:.1f}" r="9" fill="{K}"/>'
    if label: b += T(P + s / 2, P + s + 30, label, 20)
    return svg(s + 2 * P, s + 2 * P + (36 if label else 0), b)
def options_squares(opts):
    """opts: list of hole lists → แถวของสี่เหลี่ยมพร้อมเลขข้อ"""
    s = 150; P = 12; b = ''; x = 0
    for i, holes in enumerate(opts):
        b += T(x + 14, 30, f'{i + 1}.', 22, 'start')
        b += f'<rect x="{x + 40}" y="{P}" width="{s}" height="{s}" fill="#fff" stroke="{K}" stroke-width="3"/>'
        for (hx, hy) in holes: b += f'<circle cx="{x + 40 + hx * s:.1f}" cy="{P + (1 - hy) * s:.1f}" r="7" fill="{K}"/>'
        x += 40 + s + 30
    return svg(x, s + 2 * P, b)
def fold_steps(steps):
    """steps: list of (shape_points(list in 0..1 coords), dashed_line or None, holes, caption)"""
    s = 150; P = 14; b = ''; x = 0
    for i, (pts, dash, holes, cap) in enumerate(steps):
        X = lambda p: x + P + p[0] * s; Y = lambda p: P + (1 - p[1]) * s
        b += f'<polygon points="{" ".join(f"{X(p):.1f},{Y(p):.1f}" for p in pts)}" fill="#fff" stroke="{K}" stroke-width="3"/>'
        if dash: b += f'<line x1="{X(dash[0]):.1f}" y1="{Y(dash[0]):.1f}" x2="{X(dash[1]):.1f}" y2="{Y(dash[1]):.1f}" stroke="{OL}" stroke-width="2.5" stroke-dasharray="8 6"/>'
        for h in holes: b += f'<circle cx="{X(h):.1f}" cy="{Y(h):.1f}" r="7" fill="{K}"/>'
        b += T(x + P + s / 2, P + s + 28, cap, 17)
        if i < len(steps) - 1:
            ax = x + 2 * P + s + 4; b += f'<polygon points="{ax},{P + s / 2 - 8} {ax + 22},{P + s / 2} {ax},{P + s / 2 + 8}" fill="{OL}"/>'
        x += 2 * P + s + 34
    return svg(x - 30, s + 2 * P + 36, b)

# ---------- 23: แบบรูปซ้ำ ----------
def pattern(seq, upto, mark):
    k = len(seq); w = 46; b = ''; cols = [YLL, GRN]
    rows = math.ceil(upto / k)
    for i in range(upto):
        r, c = divmod(i, k); x = 10 + c * (w + 4); y = 10 + r * (w + 16)
        fill = YL if i + 1 == mark else cols[r % 2]
        b += f'<rect x="{x}" y="{y}" width="{w}" height="{w}" rx="6" fill="{fill}" stroke="{OL}" stroke-width="{3 if i + 1 == mark else 1.5}"/>' + T(x + w / 2, y + w / 2 + 8, seq[i % k], 22)
        if c == k - 1: b += T(x + w + 28, y + w / 2 + 6, f'{(r + 1) * k}', 15, fill=OL)
    return svg(10 + k * (w + 4) + 48, 10 + rows * (w + 16), b)

# ---------- 24: ลูกเต๋าวางเรียง (มองด้านบน) ----------
def dice_row(n, front, back, mids=None, inner=True):
    c = 92; P = 50; b = ''; mids = mids or []
    for i in range(n):
        x = P + i * c; b += f'<rect x="{x}" y="40" width="{c}" height="{c}" rx="10" fill="#fff" stroke="{K}" stroke-width="3"/>' + T(x + c / 2, 30, f'ลูกที่ {i + 1}', 15, fill=OL)
    b += T(P - 26, 40 + c / 2 + 9, front, 26) + T(P + n * c + 26, 40 + c / 2 + 9, back, 26)
    b += T(P - 26, 40 + c + 28, 'หน้า', 14, fill=OL) + T(P + n * c + 26, 40 + c + 28, 'หลัง', 14, fill=OL)
    for i in range(n if inner else 0):
        x = P + i * c
        left = 7 - front if i == 0 else None; right = 7 - back if i == n - 1 else None
        if i == 0: b += f'<rect x="{x + 4}" y="{40 + c / 2 - 18}" width="34" height="36" rx="6" fill="{YLL}"/>' + T(x + 21, 40 + c / 2 + 9, front, 20)
        if i == 0: b += f'<rect x="{x + c - 38}" y="{40 + c / 2 - 18}" width="34" height="36" rx="6" fill="{YL}"/>' + T(x + c - 21, 40 + c / 2 + 9, 7 - front, 20)
        if i == n - 1: b += f'<rect x="{x + 4}" y="{40 + c / 2 - 18}" width="34" height="36" rx="6" fill="{YL}"/>' + T(x + 21, 40 + c / 2 + 9, 7 - back, 20)
        if 0 < i < n - 1:
            b += f'<rect x="{x + 4}" y="{40 + c / 2 - 18}" width="34" height="36" rx="6" fill="{YL}"/>' + T(x + 21, 40 + c / 2 + 9, '?', 20)
            b += f'<rect x="{x + c - 38}" y="{40 + c / 2 - 18}" width="34" height="36" rx="6" fill="{YL}"/>' + T(x + c - 21, 40 + c / 2 + 9, '7−?', 14)
    return svg(2 * P + n * c, 40 + c + 40, b)

# ---------- 25: ตารางสี่เหลี่ยม ----------
def rect_grid(W, H, rects):
    u = 52; P = 10; b = ''; cols = ['rgba(242,194,48,.55)', 'rgba(140,170,70,.55)', 'rgba(217,83,79,.45)']
    for k, (x, y, w, h) in enumerate(rects):
        b += f'<rect x="{P + x * u + 3}" y="{P + y * u + 3}" width="{w * u - 6}" height="{h * u - 6}" rx="5" fill="{cols[k % 3]}" stroke="{OL}" stroke-width="2.5"/>'
    for i in range(W + 1): b += f'<line x1="{P + i * u}" y1="{P}" x2="{P + i * u}" y2="{P + H * u}" stroke="{K}" stroke-width="1.5"/>'
    for j in range(H + 1): b += f'<line x1="{P}" y1="{P + j * u}" x2="{P + W * u}" y2="{P + j * u}" stroke="{K}" stroke-width="1.5"/>'
    return svg(2 * P + W * u, 2 * P + H * u, b)

# ---------- 26 / 28: ชิปตัวเลข ----------
def chips(groups):
    """groups: [(หัวข้อ, [ข้อความ, ...]), ...] → HTML"""
    out = ''
    for title, items in groups:
        out += f"<div class='chg'><b>{title}</b>" + ''.join(f"<span class='chp'>{t}</span>" for t in items) + "</div>"
    return f"<div class='chips'>{out}</div>"
def coin(v, x, y, r=26):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{YL}" stroke="#B8901A" stroke-width="3"/>' + T(x, y + 8, v, 20)
def coin_pairs(pairs):
    cols = 2 if len(pairs) > 3 else 1; per = math.ceil(len(pairs) / cols); cw = 60 * max(len(p) for p in pairs) + 150; b = ''
    for i, ps in enumerate(pairs):
        cx0 = 40 + (i // per) * cw; y = 40 + (i % per) * 66; x = cx0
        for v in ps: b += coin(v, x, y); x += 58
        b += T(x - 12, y + 8, '= ' + str(sum(ps)), 22, 'start')
    return svg(cols * cw + 10, 40 + per * 66 - 18, b)

# ---------- 27: กองอิฐ ----------
def pyramid(old, new):
    bw, bh = 54, 30; total = old + new; W = total * bw + 20; b = ''
    for layer in range(1, total + 1):
        y = 10 + (layer - 1) * bh; x0 = (W - layer * bw) / 2
        fill = YL if layer > old else '#fff'
        for k in range(layer): b += f'<rect x="{x0 + k * bw}" y="{y}" width="{bw}" height="{bh}" fill="{fill}" stroke="{K}" stroke-width="2.5"/>'
        if layer > old: b += T(x0 + layer * bw + 22, y + 21, f'{layer} ก้อน', 16, 'start', OL)
    return svg(W + 90, 20 + total * bh, b)

# ---------- 29: เป้าลูกดอก ----------
def target(rings, darts_in=None):
    """rings: ค่าจากนอกเข้าใน"""
    n = len(rings); cx, cy = 130, 130; b = ''
    for i, v in enumerate(rings):
        r = 120 - i * (100 / n)
        b += f'<circle cx="{cx}" cy="{cy}" r="{r:.0f}" fill="{YL if darts_in is not None and i == darts_in else "#fff"}" stroke="{K}" stroke-width="3"/>'
        b += T(cx, cy - r + 30 if i < n - 1 else cy + 9, v, 24)
    if darts_in is not None:
        r = 120 - darts_in * (100 / n) - 12
        for k, a in enumerate((-30, 30)):
            pass
    return svg(260, 260, b)
def target_darts(rings, k):
    s = target(rings, len(rings) - 1)
    marks = ''.join(f'<circle cx="{130 + dx}" cy="{130 + 22}" r="7" fill="{RED}" stroke="#fff" stroke-width="2"/>' for dx in [(-16 * (k - 1) / 2) + 16 * i for i in range(k)])
    return s.replace('</svg>', marks + '</svg>')

# ---------- 30: เส้นเวลา ----------
def timeline(points):
    """points: [(เวลา, ข้อความ), ...] จากซ้ายไปขวา"""
    n = len(points); W = 160 * (n - 1) + 120; b = f'<line x1="60" y1="70" x2="{W - 60}" y2="70" stroke="{OL}" stroke-width="5"/>'
    for i, (t, lab) in enumerate(points):
        x = 60 + i * 160
        b += f'<circle cx="{x}" cy="70" r="12" fill="{YL}" stroke="{OL}" stroke-width="3"/>' + T(x, 40, t, 22) + T(x, 108, lab, 16, fill=OL)
    return svg(W, 125, b)
def seg_labels(svg_str, segs):
    """segs: [(i, ข้อความระหว่างจุด i กับ i+1)]"""
    add = ''.join(T(60 + i * 160 + 80, 62, s, 15, fill=RED) for i, s in segs)
    return svg_str.replace('</svg>', add + '</svg>')
