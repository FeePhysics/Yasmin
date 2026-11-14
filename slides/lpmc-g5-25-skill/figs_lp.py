# รูปประกอบ (SVG) สำหรับข้อสอบ LPMC ป.5 ครั้งที่ 25
import math
# ลายเส้นแบบข้อสอบต้นฉบับ: เส้นดำ พื้นขาว แรเงาเทา
NAVY = '#111111'; BLUE = '#111111'; SKY = '#FFFFFF'; PURP = '#111111'; PURPL = '#FFFFFF'; SHADE = '#A8A8A8'

def _svg(w, h, body):
    return f'<svg class="img" viewBox="0 0 {w:.0f} {h:.0f}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def cards(nums):
    w, g = 54, 12
    b = ''
    for i, n in enumerate(nums):
        x = 4 + i * (w + g)
        b += (f'<rect x="{x}" y="4" width="{w}" height="66" rx="8" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
              f'<text x="{x + w / 2}" y="50" font-family="sans-serif" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}">{n}</text>')
    return _svg(len(nums) * (w + g) - g + 8, 74, b)

def _shape(kind, x, base, s):
    st = f'fill="#fff" stroke="{NAVY}" stroke-width="3"'
    if kind == 'tri': return f'<polygon points="{x},{base} {x + s},{base} {x + s / 2},{base - s}" {st}/>'
    if kind == 'sq': return f'<rect x="{x + 2}" y="{base - s + 4}" width="{s - 4}" height="{s - 4}" {st}/>'
    if kind == 'cir': return f'<circle cx="{x + s / 2}" cy="{base - s / 2}" r="{s / 2 - 1}" {st}/>'
    cx, cy, R, r = x + s / 2, base - s / 2, s / 2, s / 2 * 0.45
    pts = ' '.join(f'{cx + (R if i % 2 == 0 else r) * math.cos(-math.pi / 2 + i * math.pi / 5):.1f},{cy + (R if i % 2 == 0 else r) * math.sin(-math.pi / 2 + i * math.pi / 5):.1f}' for i in range(10))
    return f'<polygon points="{pts}" fill="{PURPL}" stroke="{PURP}" stroke-width="3"/>'

def balances(scales):
    unit, s, b = 230, 40, ''
    for i, (items, w, label) in enumerate(scales):
        cx = i * unit + unit / 2
        x = cx - (len(items) * (s + 4) - 4) / 2
        for k in items:
            b += _shape(k, x, 60, s); x += s + 4
        b += (f'<rect x="{cx - 95}" y="60" width="190" height="8" rx="3" fill="{NAVY}"/><rect x="{cx - 4}" y="68" width="8" height="14" fill="{NAVY}"/>'
              f'<polygon points="{cx - 70},82 {cx + 70},82 {cx + 95},145 {cx - 95},145" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'
              f'<rect x="{cx - 48}" y="94" width="96" height="38" rx="5" fill="#fff" stroke="{NAVY}" stroke-width="2.5"/>'
              f'<text x="{cx}" y="121" font-family="sans-serif" font-size="22" font-weight="700" text-anchor="middle" fill="{NAVY}">{w} kg</text>'
              f'<text x="{cx}" y="175" font-family="sans-serif" font-size="22" font-weight="700" text-anchor="middle" fill="{BLUE}">{label}</text>')
    return _svg(len(scales) * unit, 185, b)

def squares3(A, B, C, px=300):
    a, b, c = (int(round(math.sqrt(v))) for v in (A, B, C)); S = a + b + c; k = px / S; P = 6
    r = lambda x, y, w, h, f: f'<rect x="{P + x * k:.1f}" y="{P + y * k:.1f}" width="{w * k:.1f}" height="{h * k:.1f}" fill="{f}" stroke="{NAVY}" stroke-width="3"/>'
    t = lambda x, y, w, h, v: f'<text x="{P + (x + w / 2) * k:.1f}" y="{P + (y + h / 2) * k + 9:.1f}" font-family="sans-serif" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}">{v}</text>'
    g = (r(0, 0, S, S, SHADE) + r(a, 0, S - a, a, SHADE) + r(0, a, a, S - a, SHADE) + r(a + b, a, c, b, SHADE) + r(a, a + b, b, c, SHADE)
         + r(0, 0, a, a, '#fff') + r(a, a, b, b, '#fff') + r(a + b, a + b, c, c, '#fff') + t(0, 0, a, a, A) + t(a, a, b, b, B) + t(a + b, a + b, c, c, C))
    return _svg(px + 2 * P, px + 2 * P, g)

def dots(rows, cols):
    g, P = 64, 22
    b = ''.join(f'<circle cx="{P + j * g}" cy="{P + i * g}" r="9" fill="{NAVY}"/>' for i in range(rows) for j in range(cols))
    return _svg(2 * P + (cols - 1) * g, 2 * P + (rows - 1) * g, b)

def poly_chain(sides, count, size):
    R = size / (2 * math.sin(math.pi / sides))
    start = -3 * math.pi / 4 if sides == 4 else -math.pi / 2
    polys = [[(R * math.cos(start + i * 2 * math.pi / sides), R * math.sin(start + i * 2 * math.pi / sides)) for i in range(sides)]]
    for _ in range(1, count):
        cur = polys[-1]
        i = max(range(sides), key=lambda i: round((cur[i][0] + cur[(i + 1) % sides][0]) / 2, 6))
        p, q = cur[i], cur[(i + 1) % sides]; m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
        polys.append([(2 * m[0] - v[0], 2 * m[1] - v[1]) for v in cur])
    xs = [v[0] for pl in polys for v in pl]; ys = [v[1] for pl in polys for v in pl]
    mx, my, P = min(xs), min(ys), 12
    W, H = max(xs) - mx + 2 * P + 50, max(ys) - my + 2 * P
    b = ''
    for pl in polys:
        for i in range(sides):
            p, q = pl[i], pl[(i + 1) % sides]
            b += f'<line x1="{p[0] - mx + P:.1f}" y1="{p[1] - my + P:.1f}" x2="{q[0] - mx + P:.1f}" y2="{q[1] - my + P:.1f}" stroke="#111" stroke-width="2.4" stroke-linecap="round"/>'
            b += f'<circle cx="{p[0] - mx + P:.1f}" cy="{p[1] - my + P:.1f}" r="4" fill="#111"/>'
    b += f'<text x="{W - 42:.0f}" y="{H / 2 + 10:.0f}" font-family="sans-serif" font-size="34" font-weight="700" fill="{NAVY}">…</text>'
    return _svg(W, H, b)

def fig19(ea, cg, s):
    k, P = 22, 30; W, H = (ea + s) * k, (s + cg) * k
    X = lambda v: P + v * k
    L = lambda x, y, t, a='middle', c=NAVY: f'<text x="{x:.0f}" y="{y:.0f}" font-family="sans-serif" font-size="22" font-weight="700" text-anchor="{a}" fill="{c}">{t}</text>'
    b = (f'<rect x="{P}" y="{P}" width="{W}" height="{H}" fill="{SHADE}" stroke="{NAVY}" stroke-width="3"/>'
         f'<rect x="{X(ea)}" y="{P}" width="{s * k}" height="{s * k}" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
         + L(P - 6, P - 8, 'E', 'end') + L(X(ea), P - 8, 'A') + L(X(ea + s) + 6, P - 8, 'B', 'start') + L(X(ea) - 6, X(s) + 22, 'D', 'end')
         + L(X(ea + s) + 8, X(s) + 8, 'C', 'start') + L(P - 6, X(s + cg) + 22, 'F', 'end') + L(X(ea + s) + 6, X(s + cg) + 22, 'G', 'start')
         + L(X(ea / 2), P - 8, ea, c=PURP) + L(X(ea + s) + 10, X(s + cg / 2) + 8, cg, 'start', PURP))
    return _svg(W + 2 * P + 30, H + 2 * P + 10, b)

def fig30():
    P, B, s = 10, 200, 160; o = (B - s) / 2
    b = (f'<rect x="{P}" y="{P}" width="{B}" height="{B}" fill="{SHADE}" stroke="{NAVY}" stroke-width="3"/>'
         f'<rect x="{P + o}" y="{P}" width="{s}" height="{s}" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
         f'<line x1="{P + o}" y1="{P}" x2="{P + o + s}" y2="{P}" stroke="#fff" stroke-width="5"/>'
         f'<line x1="{P + o}" y1="{P}" x2="{P + o + s}" y2="{P}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="12 9"/>')
    return _svg(B + 2 * P, B + 2 * P, b)

def _fan():
    sq = [(30, 150), (76, 150), (76, 196), (30, 196)]; apex = (53, 84); A, B = (30, 150), (76, 150)
    ang = 2 * math.asin(23 / math.hypot(23, 66))
    rot = lambda p, t: (apex[0] + (p[0] - apex[0]) * math.cos(t) - (p[1] - apex[1]) * math.sin(t), apex[1] + (p[0] - apex[0]) * math.sin(t) + (p[1] - apex[1]) * math.cos(t))
    tris, prev = [[apex, A, B]], B
    for i in range(1, 4):
        nx = rot(B, -ang * i); tris.append([apex, prev, nx]); prev = nx
    return [sq] + tris
_CROSS = [[(70, 70), (118, 70), (118, 118), (70, 118)], [(70, 70), (118, 70), (94, 8)], [(118, 70), (118, 118), (180, 94)], [(70, 118), (118, 118), (94, 180)], [(70, 70), (70, 118), (8, 94)]]
_THREE = [[(30, 70), (78, 70), (78, 118), (30, 118)], [(30, 70), (78, 70), (54, 8)], [(78, 70), (78, 118), (140, 94)], [(30, 118), (78, 118), (54, 180)]]
_BOW = [[(30, 70), (78, 70), (78, 118), (30, 118)], [(30, 70), (78, 70), (54, 8)], [(78, 70), (78, 118), (140, 94)], [(140, 94), (202, 70), (202, 118)], [(30, 118), (78, 118), (54, 180)]]
_N2 = [[(30, 20), (78, 20), (78, 68), (30, 68)], [(78, 20), (78, 68), (144, 44)], [(144, 44), (210, 20), (210, 68)], [(30, 68), (78, 68), (54, 134)], [(30, 68), (8, 134), (54, 134)]]
_N3 = [[(20, 20), (68, 20), (68, 68), (20, 68)], [(68, 20), (68, 68), (134, 44)], [(134, 44), (200, 20), (200, 68)], [(20, 68), (68, 68), (44, 134)], [(44, 134), (20, 200), (68, 200)]]
_N4 = [[(40, 80), (88, 80), (88, 128), (40, 128)], [(40, 80), (88, 80), (64, 14)], [(88, 80), (88, 128), (154, 104)], [(40, 128), (88, 128), (64, 194)], [(88, 128), (126, 158), (64, 194)]]

def nets(options):
    """options: list of polygon lists; drawn side by side with labels 1., 2., ..."""
    b, x0, H = '', 0, 0
    for i, polys in enumerate(options):
        xs = [p[0] for pl in polys for p in pl]; ys = [p[1] for pl in polys for p in pl]
        dx, dy = x0 + 34 - min(xs), 14 - min(ys)
        b += f'<text x="{x0 + 4}" y="40" font-family="sans-serif" font-size="26" font-weight="700" fill="{BLUE}">{i + 1}.</text>'
        for pl in polys:
            pts = ' '.join(f'{p[0] + dx:.1f},{p[1] + dy:.1f}' for p in pl)
            b += f'<polygon points="{pts}" fill="{SKY}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
        x0 += 34 + (max(xs) - min(xs)) + 40; H = max(H, max(ys) - min(ys) + 28)
    return _svg(x0, H, b)

def nets27(): return nets([_fan(), _N2, _N3, _N4])
def nets27m(): return nets([_THREE, _BOW, _CROSS])
