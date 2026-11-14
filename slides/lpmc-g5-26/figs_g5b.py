# รูปประกอบ Mock Test (SVG ลายเส้นแบบข้อสอบต้นฉบับ) — LPMC ป.5 ครั้งที่ 26 (2568)
import math
from figs_base import card_rows, _svg, _t, K, G   # ใช้ซ้ำจากชุด ป.6

def rect_mid(shade):
    """สี่เหลี่ยมผืนผ้า ABCD, E กลาง AD, F กลาง DC, G กลาง BC — shade = รายชื่อจุดของรูปที่แรเงา"""
    W, H, P = 360, 160, 34
    pt = {'A': (P, P), 'B': (P + W, P), 'C': (P + W, P + H), 'D': (P, P + H), 'E': (P, P + H / 2), 'F': (P + W / 2, P + H), 'G': (P + W, P + H / 2)}
    b = f'<polygon points="{" ".join(f"{pt[c][0]},{pt[c][1]}" for c in shade)}" fill="#D9D9D9" stroke="{K}" stroke-width="2.5"/>'
    b += f'<rect x="{P}" y="{P}" width="{W}" height="{H}" fill="none" stroke="{K}" stroke-width="3"/>'
    off = {'A': (-14, -8), 'B': (14, -8), 'C': (14, 22), 'D': (-14, 22), 'E': (-18, 8), 'F': (0, 26), 'G': (18, 8)}
    for k, (dx, dy) in off.items(): b += _t(pt[k][0] + dx, pt[k][1] + dy, k, 22)
    return _svg(W + 2 * P, H + 2 * P, b)

def scouts(rows_shown=3):
    """แถวลูกเสือ: เลขเรียงทีละแถวจากซ้ายไปขวา แต่ละคอลัมน์คือหมู่"""
    b = ''; r = 16; gx = 52; gy = 58; x0 = 110; y0 = 60
    for j in range(3): b += _t(x0 + j * gx, 26, f'หมู่ {j + 1}', 15) + f'<line x1="{x0 + j * gx}" y1="31" x2="{x0 + j * gx}" y2="{y0 - r - 3}" stroke="{K}" stroke-width="2"/>'
    for i in range(rows_shown):
        y = y0 + i * gy
        b += _t(40, y + 6, f'แถว {i + 1}', 16) + f'<line x1="68" y1="{y}" x2="{x0 - r - 4}" y2="{y}" stroke="{K}" stroke-width="2"/>'
        for j, x in enumerate([x0, x0 + gx, x0 + 2 * gx, x0 + 4 * gx, x0 + 5 * gx]):
            b += f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{K}" stroke-width="2.5"/>'
            if i == 0 and j < 3: b += _t(x, y + 6, j + 1, 16)
        b += _t(x0 + 3 * gx, y + 6, '• • •', 16)
        if i < rows_shown - 1:
            ye = y + gy / 2; b += f'<polyline points="{x0 + 5 * gx},{y + r} {x0 + 5 * gx},{ye} {x0},{ye} {x0},{y + gy - r - 2}" fill="none" stroke="{K}" stroke-width="2.5"/>'
    b += _t(x0 + 2.5 * gx, y0 + rows_shown * gy - 8, '⋮', 24)
    return _svg(x0 + 5 * gx + 30, y0 + rows_shown * gy, b)

def shapes11(kind):
    """m1: วงกลม 3 วง + สี่เหลี่ยมยาว · m2: วงกลม 1 วง + เส้นหักรูปตัว W"""
    b = ''
    if kind == 'm1':
        b += f'<rect x="20" y="70" width="420" height="70" rx="12" fill="none" stroke="{K}" stroke-width="3"/>'
        for cx in (100, 230, 360): b += f'<circle cx="{cx}" cy="105" r="55" fill="none" stroke="{K}" stroke-width="3"/>'
        return _svg(460, 180, b)
    b += f'<circle cx="110" cy="100" r="70" fill="none" stroke="{K}" stroke-width="3"/>'
    b += f'<polyline points="160,30 220,170 280,40 340,170 400,30" fill="none" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>'
    return _svg(430, 200, b)

def chains(k, L):
    b = ''; x = 10
    for _ in range(k):
        for j in range(L):
            b += f'<rect x="{x + j * 26}" y="10" width="40" height="22" rx="11" fill="none" stroke="{K}" stroke-width="5"/>'
            b += f'<rect x="{x + j * 26}" y="10" width="40" height="22" rx="11" fill="none" stroke="#fff" stroke-width="1.5"/>'
        x += L * 26 + 14 + 34
    return _svg(x, 42, b)

def zigzag(a, b_, t2, r, c):
    """โซ่มุมแบบข้อ 20: สามเหลี่ยมซ้าย (a ที่ P, b_ ที่ T1), สี่เหลี่ยมกลาง (t2 ที่ T2, r ที่ R), สามเหลี่ยมขวา (c ที่ B, x ที่ T3)"""
    rad = math.radians
    def inter(p, d1, q, d2):
        den = d1[0] * d2[1] - d1[1] * d2[0]; t = ((q[0] - p[0]) * d2[1] - (q[1] - p[1]) * d2[0]) / den
        return (p[0] + t * d1[0], p[1] + t * d1[1])
    dirn = lambda ang: (math.cos(rad(ang)), math.sin(rad(ang)))
    P = (0.0, 0.0); th = 25.0                      # เส้น P→T2 เอียง 25°
    T1 = (math.cos(rad(th + a)) * 2.2, math.sin(rad(th + a)) * 2.2)
    dPT2 = dirn(th); dT1R = dirn(th + a + 180 + b_)   # มุมที่ T1 ระหว่าง T1P กับ T1R = b_
    X1 = inter(P, dPT2, T1, dT1R)
    R = (X1[0] + dT1R[0] * 1.6, X1[1] + dT1R[1] * 1.6)
    ang_T1R = th + a + 180 + b_; dRT3 = dirn(ang_T1R + 180 - r)   # มุมที่ R ระหว่าง RT1 กับ RT3 = r
    T2 = (P[0] + dPT2[0] * (math.hypot(*X1) + 2.4), P[1] + dPT2[1] * (math.hypot(*X1) + 2.4))
    dT2B = dirn(th + 180 + t2)                      # มุมที่ T2 ระหว่าง T2P กับ T2B = t2 (หมุนทวนเข็ม)
    X2 = inter(R, dRT3, T2, dT2B)
    Bp = (X2[0] + dT2B[0] * 1.5, X2[1] + dT2B[1] * 1.5)
    dBT3 = dirn(th + t2 - c)                        # มุมที่ B ระหว่าง BT2 กับ BT3 = c (หมุนตามเข็ม)
    T3 = inter(Bp, dBT3, R, dRT3)
    pts = [P, T1, R, T3, Bp, T2]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]; mx, Mx, my, My = min(xs), max(xs), min(ys), max(ys)
    sc = 430 / (Mx - mx); X = lambda p: 20 + (p[0] - mx) * sc; Y = lambda p: 20 + (My - p[1]) * sc
    ln = lambda p, q: f'<line x1="{X(p):.1f}" y1="{Y(p):.1f}" x2="{X(q):.1f}" y2="{Y(q):.1f}" stroke="{K}" stroke-width="3.5"/>'
    s = ln(P, T1) + ln(T1, R) + ln(R, T3) + ln(T3, Bp) + ln(Bp, T2) + ln(T2, P)
    def lab(p, q1, q2, txt, d=40):
        a1 = math.atan2(q1[1] - p[1], q1[0] - p[0]); a2 = math.atan2(q2[1] - p[1], q2[0] - p[0])
        m = math.atan2(math.sin(a1) + math.sin(a2), math.cos(a1) + math.cos(a2))
        return _t(X(p) + d * math.cos(m), Y(p) - d * math.sin(m) + 7, txt, 19)
    s += lab(P, T1, T2, f'{a}°', 46) + lab(T1, P, R, f'{b_}°') + lab(T2, P, Bp, f'{t2}°') + lab(R, T1, T3, f'{r}°') + lab(Bp, T2, T3, f'{c}°', 46) + lab(T3, R, Bp, 'x', 44)
    # ตรวจมุม x จากพิกัด
    v1 = (R[0] - T3[0], R[1] - T3[1]); v2 = (Bp[0] - T3[0], Bp[1] - T3[1])
    xdeg = math.degrees(math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / math.hypot(*v1) / math.hypot(*v2)))
    return _svg(470, (My - my) * sc + 40, s), xdeg

def cube_dots(faces):
    """ลูกบาศก์มุมมอง 3 หน้า (บน หน้า ขวา) faces = เซตของหน้าที่มีจุด"""
    b = '<polygon points="60,40 160,40 200,10 100,10" fill="#fff" stroke="#111" stroke-width="3"/>'
    b += '<rect x="60" y="40" width="100" height="100" fill="#fff" stroke="#111" stroke-width="3"/>'
    b += '<polygon points="160,40 200,10 200,110 160,140" fill="#fff" stroke="#111" stroke-width="3"/>'
    if 'top' in faces: b += '<ellipse cx="130" cy="25" rx="30" ry="9" fill="#111"/>'
    if 'front' in faces: b += '<circle cx="110" cy="90" r="32" fill="#111"/>'
    if 'right' in faces: b += '<ellipse cx="180" cy="75" rx="10" ry="32" fill="#111"/>'
    return _svg(220, 150, b)

def nets(options):
    """options: [(cells, dots), ...] วาดเรียงกันพร้อมเลขข้อ"""
    u = 30; b = ''; x0 = 0; H = 0
    for i, (cells, dots) in enumerate(options):
        rs = [r for r, _ in cells]; cs = [c for _, c in cells]
        b += _t(x0 + 12, 22, f'{i + 1})', 20, 'start')
        for (r, c) in cells:
            x = x0 + 40 + (c - min(cs)) * u; y = 10 + (r - min(rs)) * u
            b += f'<rect x="{x}" y="{y}" width="{u}" height="{u}" fill="#fff" stroke="#111" stroke-width="2.5"/>'
            if (r, c) in dots: b += f'<circle cx="{x + u / 2}" cy="{y + u / 2}" r="{u * 0.32}" fill="#111"/>'
        x0 += 40 + (max(cs) - min(cs) + 1) * u + 34; H = max(H, (max(rs) - min(rs) + 1) * u + 20)
    return _svg(x0, H, b)
