# รูปประกอบ Mock Test (SVG ลายเส้นแบบข้อสอบต้นฉบับ: เส้นดำ พื้นขาว แรเงาเทา) — LPMC ป.6 ครั้งที่ 26
import math
K = '#111111'; G = '#A8A8A8'; FONT = 'font-family="sans-serif" font-weight="700"'

def _svg(w, h, body):
    return f'<svg class="img" viewBox="0 0 {w:.0f} {h:.0f}" xmlns="http://www.w3.org/2000/svg">{body}</svg>'
def _t(x, y, s, size=22, anchor='middle'):
    return f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}" text-anchor="{anchor}" fill="{K}">{s}</text>'

def wall(R, C, widths):
    """ผนังแบ่ง R×C ช่อง (เส้นประ) + ภาพเขียนกว้าง w ช่อง สูง 1 ช่อง"""
    u = 70; P = 14; b = ''
    W0, H0 = C * u, R * u
    b += f'<rect x="{P}" y="{P + 10}" width="{W0}" height="{H0}" fill="#fff" stroke="{K}" stroke-width="3"/>'
    for c in range(1, C): b += f'<line x1="{P + c * u}" y1="{P + 10}" x2="{P + c * u}" y2="{P + 10 + H0}" stroke="{K}" stroke-width="2" stroke-dasharray="7 6"/>'
    for r in range(1, R): b += f'<line x1="{P}" y1="{P + 10 + r * u}" x2="{P + W0}" y2="{P + 10 + r * u}" stroke="{K}" stroke-width="2" stroke-dasharray="7 6"/>'
    for x in (P + 8, P + W0 - 8): b += f'<rect x="{x - 4}" y="{P}" width="8" height="{H0 + 50}" rx="4" fill="#fff" stroke="{K}" stroke-width="2.5"/>'
    x0 = P + W0 + 50; y = P + 10; x = x0; maxx = x0
    for i, w in enumerate(widths):
        ww = w * 62
        if x + ww > x0 + 330: x = x0; y += 70
        b += f'<rect x="{x}" y="{y}" width="{ww}" height="56" fill="#fff" stroke="{K}" stroke-width="4"/><rect x="{x + 6}" y="{y + 6}" width="{ww - 12}" height="44" fill="none" stroke="{G}" stroke-width="3"/>'
        b += _t(x + ww / 2, y + 36, f'ภาพ {i + 1}', 18)
        x += ww + 16; maxx = max(maxx, x)
    return _svg(max(maxx, x0 + 200) + 10, max(H0 + 70, y + 76), b)

def card_rows(rows):
    """rows: [(name, [(text, black?), ...]), ...]"""
    cw, gap, P, lw = 56, 12, 10, 92; b = ''
    for i, (name, cards) in enumerate(rows):
        y = P + i * 82
        b += f'<text x="{P}" y="{y + 46}" font-family="Mali" font-weight="700" font-size="26" fill="{K}">{name}</text>'
        for j, (t, blk) in enumerate(cards):
            x = P + lw + j * (cw + gap)
            b += f'<rect x="{x}" y="{y}" width="{cw}" height="66" fill="{G if blk else "#fff"}" stroke="{K}" stroke-width="2.5"/>'
            if t != '': b += _t(x + cw / 2, y + 44, t, 26)
    n = max(len(c) for _, c in rows)
    return _svg(P + lw + n * (cw + gap) + 4, P + len(rows) * 82, b)

def para(shade, labels=True):
    """สี่เหลี่ยมด้านขนาน ABCD, E บนเส้น CB ต่อออกไป, DE ตัด AB ที่ F; shade = รายการสามเหลี่ยมที่แรเงา"""
    D, C, A = (40, 300), (300, 300), (110, 140); B = (A[0] + C[0] - D[0], A[1])
    t = 1.75; E = (C[0] + t * (B[0] - C[0]), C[1] + t * (B[1] - C[1]))
    s = (A[1] - D[1]) / (E[1] - D[1]); Fp = (D[0] + s * (E[0] - D[0]), A[1])
    pt = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': Fp}
    b = ''
    for tri in shade:
        b += f'<polygon points="{" ".join(f"{pt[c][0]:.1f},{pt[c][1]:.1f}" for c in tri)}" fill="{G}" stroke="{K}" stroke-width="2"/>'
    L = lambda p, q, w=4: f'<line x1="{pt[p][0]:.1f}" y1="{pt[p][1]:.1f}" x2="{pt[q][0]:.1f}" y2="{pt[q][1]:.1f}" stroke="{K}" stroke-width="{w}"/>'
    b += L('A', 'B') + L('B', 'C') + L('C', 'D') + L('D', 'A') + L('A', 'E') + L('B', 'E') + L('D', 'E', 2.5) + L('F', 'C', 2.5)
    off = {'A': (-18, -10), 'B': (20, 12), 'C': (8, 30), 'D': (-14, 30), 'E': (16, -6), 'F': (-14, 30)}
    for k, (dx, dy) in off.items(): b += f'<text x="{pt[k][0] + dx:.1f}" y="{pt[k][1] + dy:.1f}" font-family="serif" font-size="28" text-anchor="middle" fill="{K}">{k}</text>'
    return _svg(E[0] + 40, 345, b)

def tri18(La, Ta, x_ang, e_ang):
    """สามเหลี่ยมแบบข้อ 18: มุมที่ L, มุม T (ระหว่าง TL กับ TM), x (ระหว่าง TM กับ TR), มุม e ที่ R"""
    r = math.radians; M_ang = 180 - La - Ta
    TL = math.sin(r(M_ang)) / math.sin(r(Ta)); T = (TL * math.cos(r(La)), TL * math.sin(r(La))); M = (1.0, 0.0)
    dTM = math.atan2(M[1] - T[1], M[0] - T[0]); dTR = dTM + r(x_ang)
    tR = -T[1] / math.sin(dTR); R = (T[0] + tR * math.cos(dTR), 0.0)
    MR = R[0] - M[0]; TM = math.hypot(M[0] - T[0], M[1] - T[1]); Pp = (M[0] + (T[0] - M[0]) * MR / TM, M[1] + (T[1] - M[1]) * MR / TM)
    sc = 420 / R[0]; X = lambda p: 30 + p[0] * sc; Y = lambda p: 30 + (T[1] - p[1]) * sc
    ln = lambda p, q: f'<line x1="{X(p):.1f}" y1="{Y(p):.1f}" x2="{X(q):.1f}" y2="{Y(q):.1f}" stroke="{K}" stroke-width="3.5" stroke-linecap="round"/>'
    Lp = (0.0, 0.0)
    b = ln(Lp, R) + ln(Lp, T) + ln(T, M) + ln(T, R) + ln(Pp, R)
    def tick(p, q):
        mx, my = (X(p) + X(q)) / 2, (Y(p) + Y(q)) / 2; ang = math.atan2(Y(q) - Y(p), X(q) - X(p)) + math.pi / 2
        return ''.join(f'<line x1="{mx + o * math.cos(ang - math.pi / 2) - 8 * math.cos(ang):.1f}" y1="{my + o * math.sin(ang - math.pi / 2) - 8 * math.sin(ang):.1f}" x2="{mx + o * math.cos(ang - math.pi / 2) + 8 * math.cos(ang):.1f}" y2="{my + o * math.sin(ang - math.pi / 2) + 8 * math.sin(ang):.1f}" stroke="{K}" stroke-width="3"/>' for o in (-3, 3))
    b += tick(Pp, M) + tick(M, R)
    def lab(p, d1, d2, s, rad=46):
        a = (d1 + d2) / 2
        return _t(X(p) + rad * math.cos(a), Y(p) - rad * math.sin(a) + 7, s, 19)
    ang = lambda p, q: math.atan2(q[1] - p[1], q[0] - p[0])  # มุมในพิกัดคณิต (แกน y ชี้ขึ้น)
    dTL = ang(T, Lp); dTMs = ang(T, M); dTRs = ang(T, R)
    b += lab(Lp, 0, r(La), f'{La}°', 40) + lab(T, dTL, dTMs, f'{Ta}°', 44) + lab(T, dTMs, dTRs, 'x', 100)
    dRP = ang(R, Pp); dRT = ang(R, T)
    b += lab(R, dRP, dRT, f'{e_ang}°', 92)
    return _svg(X(R) + 34, Y(Lp) + 30, b)

def post(shape, s, rope):
    """ผนัง + เสา (tri/sq) ด้านหนึ่งชิดผนัง + จุดผูกที่มุมขวาล่าง"""
    u = 110 / s; P = 20; W = 520; base = 150; cx = W / 2
    b = f'<line x1="{P}" y1="{base}" x2="{W - P}" y2="{base}" stroke="{K}" stroke-width="5"/>'
    b += ''.join(f'<line x1="{x}" y1="{base + 4}" x2="{x - 14}" y2="{base + 24}" stroke="{K}" stroke-width="4"/>' for x in range(P + 20, W - P, 30))
    w = s * u
    if shape == 'tri':
        pts = [(cx - w / 2, base), (cx + w / 2, base), (cx, base - w * math.sqrt(3) / 2)]
    else:
        pts = [(cx - w / 2, base), (cx + w / 2, base), (cx + w / 2, base - w), (cx - w / 2, base - w)]
    b += f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="#fff" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>'
    b += f'<circle cx="{cx + w / 2:.1f}" cy="{base}" r="7" fill="{K}"/>' + _t(cx + w / 2 + 40, base - 12, f'เชือก {rope} ม.', 18, 'start')
    b += _t(cx, base + 50, f'ด้านยาว {s} ม.', 18)
    return _svg(W, base + 62, b)

def num_tri(rows=4):
    """ตารางตัวเลขแถวละ 2n−1 จำนวน (HTML)"""
    out, k = [], 1
    for n in range(1, rows + 1):
        nums = list(range(k, k + 2 * n - 1)); k += 2 * n - 1
        out.append(f"<div class='ntr'>{''.join(f'<span>{v}</span>' for v in nums)}<em>→ แถวที่ {n}</em></div>")
    return "<div class='ntri'>" + ''.join(out) + "<div class='ntr'><span>⋮</span></div></div>"
