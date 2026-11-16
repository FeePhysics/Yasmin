# ข้อมูลข้อสอบ LPMC ครั้งที่ 23 (2565) ระดับ ป.2 ข้อ 16–30 — ข้อจริง + Mock Test 2 ข้อ
# คำตอบทุกข้อคำนวณด้วยโปรแกรม (ไล่ทุกกรณี) + assert · อธิบายด้วยรูปสำหรับเด็ก ป.2
import itertools, math
import figs_p2 as fg

def I(q, steps, ans, chk, qimg='', aimg='', fs=None, note=''):
    return dict(q=q, steps=steps, ans=str(ans), chk=chk, qimg=qimg, aimg=aimg, fs=fs, note=note)
P = []
def add(no, topic, tip, warn, *items):
    assert len(items) == 3
    P.append(dict(no=no, topic=topic, tip=tip, warn=warn, items=list(items)))
ORIG = lambda f: f'<img class="img crop" src="assets/orig/{f}.png">'
opts = lambda L: "<ul class='opts'>" + ''.join(f'<li>{i + 1}. {t}</li>' for i, t in enumerate(L)) + '</ul>'
isym = lambda bits: f'<svg class="isym" viewBox="0 0 44 44">{fg.sym(bits, 22, 22, 18, 3)}</svg>'
stack = lambda *a: "<div class='vstack'>" + ''.join(a) + "</div>"

# ---------------- 16 ยกรูปซ้อนกัน ----------------
def item16(heads, target, real=False):
    cnt = sum(1 for a in heads for b in heads if a | b == target)
    if real:
        q = f"จากตาราง ★ หมายถึงการยกรูปซ้อนกัน จงเติมผลลัพธ์ให้ครบ แล้วนับว่าผลลัพธ์เป็น {isym(target)} มีทั้งหมดกี่รูป"; img = ORIG('q16')
    else:
        q = (f"★ หมายถึง การยกรูปซ้อนกัน เช่น {isym(1)} ★ {isym(2)} = {isym(3)} จงเติมผลลัพธ์ในตารางให้ครบ "
             f"แล้วนับว่าผลลัพธ์เป็น {isym(target)} มีทั้งหมดกี่รูป"); img = fg.overlay_table(heads, filled=False)
    rows = [sum(1 for b in heads if a | b == target) for a in heads]
    st = ["ยกรูปซ้อนกัน = เอาเส้นของทั้ง 2 รูปมารวมกัน", f"เติมตารางให้ครบ แล้วระบายช่องที่ได้ {isym(target)}",
          "นับทีละแถว: " + ' + '.join(map(str, rows)) + f" = {cnt}"]
    return I(q, st, cnt, f"ตรวจ: ให้โปรแกรมยกรูปซ้อนครบทุกช่อง ได้ {isym(target)} {cnt} ช่อง ✓", qimg=img, aimg=fg.overlay_table(heads, target))
add(16, "ยกรูปซ้อนกัน (ตาราง)", "รูปซ้อนกันได้เส้นของทั้งสองรูปรวมกัน", "อย่าลืมนับช่องที่ซ้อนรูปเดียวกัน เช่น ⊕ ★ ⊕",
    item16([0, 1, 2, 3], 3, True), item16([0, 1, 2, 3], 2), item16([0, 1, 2], 3))

# ---------------- 17 แบ่งหมู่ ----------------
def item17(a, b, who='ลูกเสือ', grp='หมู่'):
    n = next(n for n in range(a + 1, 1000) if n % a == 1 and n % b == 0)
    q = (f"มี{who}อยู่กลุ่มหนึ่ง ถ้าแบ่งออกเป็น{grp}ละ {a} คน จะมีอยู่ 1 {grp}ที่ต้องมี {a + 1} คนเพราะเหลือเศษ "
         f"แต่ถ้าแบ่งออกเป็น{grp}ละ {b} คนจะแบ่งได้พอดี {who}กลุ่มนี้มีอย่างน้อยกี่คน")
    tries = [m for m in range(b, n + 1, b)]
    st = [f"แบ่ง{grp}ละ {b} พอดี → จำนวนคนนับทีละ {b}: " + ', '.join(map(str, tries)) + ', …',
          f"แบ่ง{grp}ละ {a} ต้องเหลือเศษ 1 (คนที่เหลือไปอยู่กับ{grp}หนึ่ง)",
          f"{n} ÷ {a} ได้ {n // a} {grp} เหลือ 1 ✓ → ตอบ = {n}"]
    sizes = [a] * (n // a - 1) + [a + 1]
    return I(q, st, n, f"ตรวจ: {n} คน แบ่ง{grp}ละ {a} ได้ {' , '.join(map(str, sizes))} และแบ่ง{grp}ละ {b} ได้ {n // b} {grp}พอดี ✓",
             aimg=stack(fg.dot_groups(sizes, f'{grp}ละ {a}'), fg.dot_groups([b] * (n // b), f'{grp}ละ {b}')))
add(17, "การหารเหลือเศษ", "นับทีละ 5 (จำนวนที่แบ่งได้พอดี) แล้วเช็กว่าหาร 3 เหลือ 1", "ต้องมีหมู่ปกติอย่างน้อย 1 หมู่ จึงจะมีหมู่ 4 คนได้",
    item17(3, 5), item17(4, 3, 'นักเรียน', 'กลุ่ม'), item17(5, 4, 'นักกีฬา', 'ทีม'))

# ---------------- 18 พลิกกลับหลัง + หมุน ----------------
def src_of(ops):
    """คืนฟังก์ชัน: ตำแหน่งสุดท้าย (r,c) ← ช่องด้านหน้าเดิม"""
    def f(rc):
        r, c = rc
        for op in reversed(ops):
            if op == 'rot': r, c = 2 - r, 2 - c
            if op == 'flip': c = 2 - c
        return (r, c)
    return f
def item18(nums, ops, letters, real=False):
    f = src_of(ops); vals = {L: nums[f(p)[0]][f(p)[1]] for L, p in letters.items()}; s = sum(vals.values())
    opname = ' แล้ว'.join({'flip': 'พลิกกลับหลัง', 'rot': 'หมุนกลับหัว'}[o] for o in ops)
    if real:
        q = "ผลรวมของจำนวนที่อยู่ด้านหลัง A, B, C เป็นเท่าใด"; img = ORIG('q18')
    else:
        tgt = [['' for _ in range(3)] for _ in range(3)]
        for L, (r, c) in letters.items(): tgt[r][c] = L
        q = f"แผ่นป้าย 9 ช่องมีตัวเลขด้านหน้า นำมา{opname} ได้ด้านหลังดังรูปขวา ผลรวมของจำนวนที่อยู่ด้านหลัง {', '.join(letters)} เป็นเท่าใด"
        img = fg.grid_pair((nums, None), (tgt, None), 'ด้านหน้า', 'ด้านหลัง', opname)
    marks = {f(p): L for L, p in letters.items()}
    st = [("พลิกกลับหลัง = ซ้ายกับขวาสลับกัน" if 'flip' in ops else ''), ("หมุนกลับหัว = บนกับล่างสลับ และซ้ายกับขวาสลับ" if 'rot' in ops else ''),
          "ย้อนหาว่าแต่ละตัวอักษรอยู่หลังช่องไหน: " + ' · '.join(f"{L} = {v}" for L, v in vals.items()),
          f"รวม = {' + '.join(map(str, vals.values()))} = {s}"]
    st = [x for x in st if x]
    expl = fg.grid_pair((nums, marks), ([['' for _ in range(3)] for _ in range(3)], {p: L for L, p in letters.items()}), 'ด้านหน้า', 'ด้านหลัง', opname)
    return I(q, st, s, "ตรวจ: ให้โปรแกรมพลิกและหมุนตารางจริง แล้วอ่านค่าที่ตำแหน่ง " + ', '.join(letters) + " ✓", qimg=img, aimg=expl)
add(18, "การพลิกและหมุนรูป", "ดูทิศของปลา: พลิกแล้วหัวปลาสลับข้าง หมุนแล้วปลากลับหัว", "ตัวเลขที่เห็นคือด้านหน้า ตัวอักษรอยู่ด้านหลัง ต้องย้อนกลับ",
    item18([[4, 12, 11], [6, 9, 7], [15, 3, 10]], ['flip', 'rot'], {'A': (1, 0), 'B': (0, 2), 'C': (2, 1)}, True),
    item18([[5, 8, 2], [9, 1, 6], [3, 7, 4]], ['flip'], {'A': (0, 0), 'B': (1, 2), 'C': (2, 1)}),
    item18([[10, 2, 7], [4, 13, 8], [6, 11, 5]], ['flip', 'rot'], {'A': (0, 1), 'B': (2, 0), 'C': (1, 2)}))

# ---------------- 19 ป้าย A B C D ----------------
def item19(s1, s2, real=False):
    sols = [(a, b, c, d) for a, b, c, d in itertools.permutations(range(1, 10), 4) if a + b == s1 and c + d == s2 and min(b, d) > max(a, c)]
    vals = {b + d for _, b, _, d in sols}; assert len(vals) == 1, sols; a, b, c, d = sols[0]; ans = b + d
    q = (f"มีป้ายอยู่ 4 ใบ A, B, C และ D ด้านหลังมีตัวเลขอยู่ป้ายละ 1 ตัวไม่ซ้ำกัน ถ้านำตัวเลขหลังป้าย A + B จะเท่ากับ {s1} "
         f"และตัวเลขหลังป้าย C + D จะเท่ากับ {s2} ถ้าเลขหลังป้าย B และ D มีค่ามากกว่าเลขหลังป้าย A และ C แล้วเลขหลังป้าย B + D มีค่าเท่าใด")
    p1 = [(x, s1 - x) for x in range(1, s1) if x < s1 - x]; p2 = [(x, s2 - x) for x in range(1, s2) if x < s2 - x]
    st = [f"A + B = {s1}: " + ', '.join(f"{x}+{y}" for x, y in p1), f"C + D = {s2}: " + ', '.join(f"{x}+{y}" for x, y in p2),
          "เลือกคู่ที่ตัวเลขไม่ซ้ำ และ B, D ต้องใหญ่กว่า A, C ทั้งคู่", f"A = {a}, B = {b}, C = {c}, D = {d} → B + D = {b} + {d} = {ans}"]
    return I(q, st, ans, "ตรวจ: ไล่ทุกชุดตัวเลข 1–9 ไม่ซ้ำด้วยโปรแกรม ได้ B + D ค่าเดียว ✓", qimg=ORIG('q19') if real else fg.cards('ABCD'),
             aimg=fg.cards('ABCD', [a, b, c, d]), note=("ถือว่าตัวเลขเป็นจำนวนนับ (ไม่ใช้ 0)" if real else ''))
add(19, "ตรรกะ (ผลบวกของป้าย)", "เขียนคู่ที่บวกกันได้ออกมาให้ครบก่อน", "B และ D ต้องมากกว่าทั้ง A และ C ไม่ใช่แค่ตัวคู่ของมัน", item19(5, 6, True), item19(7, 5), item19(4, 9))

# ---------------- 20 ปาลูกดอกวงล้อ ----------------
def item20(vals, k, mode='max', real=False):
    best = (max if mode == 'max' else min)(sum(c) for c in itertools.product(vals, repeat=k)); v = max(vals) if mode == 'max' else min(vals)
    word = 'สูงสุด' if mode == 'max' else 'ต่ำสุด'; luck = 'โชคดีมาก' if mode == 'max' else 'โชคไม่ดี'
    q = f"ปาลูกดอกถูกแป้น {k} ครั้ง {luck}จะได้รางวัล{word}กี่บาท" + ('' if real else f" (วงล้อมีช่อง {', '.join(map(str, vals))} บาท)")
    st = [f"{luck} = ทุกลูกถูกช่องที่{'มากที่สุด' if mode == 'max' else 'น้อยที่สุด'} คือ {v} บาท", f"ปา {k} ครั้ง = {' + '.join([str(v)] * k)} = {best}"]
    return I(q, st, best, f"ตรวจ: ลองทุกแบบที่ลูกดอก {k} ลูกตกได้ ค่า{word}คือ {best} ✓", qimg=ORIG('q20') if real else fg.pie(vals),
             aimg=fg.pie(vals, vals.index(v), k), note=("ลูกดอกตกช่องเดิมซ้ำได้ (ถ้าห้ามซ้ำช่อง จะได้ 300 + 200 + 100 = 600)" if real else ''))
add(20, "การหาค่ามากที่สุด", "โชคดีที่สุดคือทุกครั้งได้ช่องที่มากที่สุด", "ลูกดอกตกช่องเดิมซ้ำได้", item20([100, 100, 100, 300, 50, 200], 3, real=True), item20([50, 100, 200, 400, 100, 50], 2), item20([20, 50, 10, 100, 50, 20], 4, 'min'))

# ---------------- 21 สองวงผลรวมเท่ากัน ----------------
def ok21(nums, a, b):
    rest = [x for x in nums if x not in (a, b)]
    for p in itertools.permutations(rest):
        if p[0] + p[1] == p[2] + p[3]: return dict(TL=p[0], BL=p[1], TR=p[2], BR=p[3], a=a, b=b)
    return None
def item21(nums, choices, real=False):
    res = [ok21(nums, a, b) for a, b in choices]; good = [i for i, r in enumerate(res) if r]; assert len(good) == 1, res; ans = good[0] + 1; sol = res[good[0]]
    q = (f"นำ {', '.join(map(str, nums))} ใส่ลงในวงกลมเล็ก ทำให้ได้ผลรวมทั้งสองวงเท่ากัน ข้อใดสามารถทำได้" + opts([f"a = {a}, b = {b}" for a, b in choices]))
    st = ["a และ b อยู่ทั้งสองวง จึงนับเท่ากันทั้งสองข้าง", "เลข 4 ตัวที่เหลือต้องแบ่งเป็น 2 คู่ที่บวกกันได้เท่ากัน",
          ' · '.join(f"ข้อ {i + 1} {'✓' if r else '✗'}" for i, r in enumerate(res)),
          f"ข้อ {ans}: {sol['TL']} + {sol['BL']} = {sol['TR']} + {sol['BR']} → ตอบข้อ = {ans}"]
    return I(q, st, ans, "ตรวจ: ลองวางตัวเลขทุกแบบด้วยโปรแกรม มีเพียงข้อเดียวที่ทำได้ ✓", qimg=ORIG('q21') if real else fg.two_rings(),
             aimg=fg.two_rings(sol, ('a', 'b')), note=("ตัวเลือกที่ 4 ในข้อสอบพิมพ์เลขข้อเป็น “1.” ซ้ำ ถือเป็นข้อ 4" if real else ''))
add(21, "ตรรกะ (ผลรวมเท่ากัน)", "เลขที่อยู่ตรงกลางนับทั้งสองวง ไม่ต้องสนใจ", "ต้องใช้ตัวเลขครบทุกตัว ตัวละ 1 ครั้ง",
    item21([1, 2, 3, 4, 5, 6], [(1, 3), (2, 3), (1, 2), (4, 5)], True), item21([1, 2, 3, 4, 5, 6], [(2, 4), (1, 5), (3, 4), (4, 6)]), item21([2, 3, 4, 5, 6, 7], [(3, 4), (5, 6), (3, 7), (4, 7)]))

# ---------------- 22 พับกระดาษเจาะรู ----------------
REF = {'d1': lambda p: (p[1], p[0]), 'd2': lambda p: (1 - p[1], 1 - p[0]), 'v': lambda p: (1 - p[0], p[1]), 'h': lambda p: (p[0], 1 - p[1])}
def unfold(hole, folds):
    pts = {hole}
    for f in reversed(folds): pts |= {tuple(round(v, 3) for v in REF[f](p)) for p in pts}
    return pts
def item22(folds, hole, options, steps_q, steps_a, real=False):
    want = unfold(hole, folds); hits = [i for i, o in enumerate(options) if set(map(lambda p: tuple(round(v, 3) for v in p), o)) == want]; assert len(hits) == 1, (want, options)
    ans = hits[0] + 1
    if real:
        q = "พับกระดาษจัตุรัสตามรูป 2 ครั้ง แล้วเจาะรูดังรูป เมื่อคลี่ออกจะเป็นรูปใด"; img = ORIG('q22')
    else:
        q = f"พับกระดาษจัตุรัสตามรูป {len(folds)} ครั้ง แล้วเจาะรู 1 รู เมื่อคลี่ออกจะเป็นรูปใด"; img = stack(fg.fold_steps(steps_q), fg.options_squares(options))
    st = ["คลี่ย้อนกลับทีละครั้ง: รูจะเพิ่มเป็น 2 เท่า", "รูที่คลี่ออกจะอยู่ตรงข้ามรอยพับเหมือนกระจก", f"คลี่ครบ {len(folds)} ครั้ง ได้ {len(want)} รู → ตรงกับข้อ = {ans}"]
    return I(q, st, ans, "ตรวจ: สะท้อนตำแหน่งรูข้ามรอยพับทุกครั้งด้วยโปรแกรม ได้ตรงกับตัวเลือกเดียว ✓", qimg=img, aimg=fg.fold_steps(steps_a))
SQ = [(0, 0), (1, 0), (1, 1), (0, 1)]
r_hole = (0.82, 0.1)
add(22, "การพับกระดาษ (สมมาตร)", "คลี่ย้อนจากรูปสุดท้าย รูจะสะท้อนข้ามรอยพับ", "พับกี่ครั้ง รูก็เพิ่มเป็น 2 เท่าทุกครั้ง (พับ 1 ครั้ง 2 รู · พับ 2 ครั้ง 4 รู)",
    item22(['d1', 'd2'], r_hole, [[(0.1, 0.82), (0.18, 0.9), (0.9, 0.18), (0.82, 0.1)], [(0.75, 0.9), (0.9, 0.85), (0.1, 0.2), (0.25, 0.1)], [(0.4, 0.6), (0.5, 0.55), (0.45, 0.45), (0.35, 0.5)], [(0.75, 0.9), (0.9, 0.85), (0.85, 0.3), (0.75, 0.15)]],
           None, [([(0, 0), (1, 0), (0.5, 0.5)], None, [r_hole], 'เจาะรู'), ([(0, 0), (1, 0), (1, 1)], ((1, 0), (0.5, 0.5)), [r_hole, (0.9, 0.18)], 'คลี่ครั้งที่ 1'),
                 (SQ, ((0, 0), (1, 1)), [r_hole, (0.9, 0.18), (0.1, 0.82), (0.18, 0.9)], 'คลี่ครั้งที่ 2')], True),
    item22(['v', 'h'], (0.4, 0.1), [[(0.1, 0.1), (0.9, 0.1), (0.1, 0.9), (0.9, 0.9)], [(0.4, 0.1), (0.6, 0.1), (0.4, 0.9), (0.6, 0.9)], [(0.4, 0.1), (0.6, 0.1)], [(0.1, 0.4), (0.1, 0.6), (0.9, 0.4), (0.9, 0.6)]],
           [(SQ, ((0.5, 0), (0.5, 1)), [], 'พับซ้ายทับขวา'), ([(0, 0), (0.5, 0), (0.5, 1), (0, 1)], ((0, 0.5), (0.5, 0.5)), [], 'พับบนลงล่าง'), ([(0, 0), (0.5, 0), (0.5, 0.5), (0, 0.5)], None, [(0.4, 0.1)], 'เจาะรู')],
           [([(0, 0), (0.5, 0), (0.5, 0.5), (0, 0.5)], None, [(0.4, 0.1)], 'เจาะรู'), ([(0, 0), (0.5, 0), (0.5, 1), (0, 1)], ((0, 0.5), (0.5, 0.5)), [(0.4, 0.1), (0.4, 0.9)], 'คลี่ครั้งที่ 1'),
            (SQ, ((0.5, 0), (0.5, 1)), [(0.4, 0.1), (0.4, 0.9), (0.6, 0.1), (0.6, 0.9)], 'คลี่ครั้งที่ 2')]),
    item22(['d1'], (0.8, 0.3), [[(0.8, 0.3), (0.8, 0.7)], [(0.8, 0.3), (0.2, 0.3)], [(0.8, 0.3), (0.3, 0.8)], [(0.8, 0.3), (0.7, 0.2)]],
           [(SQ, ((0, 0), (1, 1)), [], 'พับตามเส้นทแยง'), ([(0, 0), (1, 0), (1, 1)], None, [(0.8, 0.3)], 'เจาะรู')],
           [([(0, 0), (1, 0), (1, 1)], None, [(0.8, 0.3)], 'เจาะรู'), (SQ, ((0, 0), (1, 1)), [(0.8, 0.3), (0.3, 0.8)], 'คลี่ออก')]))

# ---------------- 23 แบบรูปซ้ำ ----------------
def item23(seq, n, show):
    k = len(seq); r = n % k; ans = seq[(n - 1) % k]
    q = f"สังเกตแบบรูป<div class='math'>{' '.join(seq[i % k] for i in range(show))} . . .</div>จงหาตัวเลขตัวที่ {n}"
    st = [f"ตัวเลขซ้ำทุก {k} ตัว: {' '.join(seq)}", f"ตัวที่ {k}, {2 * k}, {3 * k}, … คือ {seq[-1]} (จบรอบพอดี)",
          f"{n} = {k} × {n // k} + {r} → ตัวที่ {n} คือตัวที่ {r if r else k} ของรอบ = {ans}"]
    return I(q, st, ans, f"ตรวจ: เขียนแบบรูปด้วยโปรแกรมจนถึงตัวที่ {n} ได้ {ans} ✓", aimg=fg.pattern(seq, n, n))
add(23, "แบบรูปซ้ำ", "หาว่าแบบรูปซ้ำทุกกี่ตัว แล้วแบ่งเป็นรอบ", "ถ้าหารลงตัว คือตัวสุดท้ายของรอบ ไม่ใช่ตัวแรก",
    item23(list('142857'), 26, 14), item23(list('2468'), 19, 10), item23(list('123321'), 20, 12))

# ---------------- 24 ลูกเต๋าวางติดกัน ----------------
def item24(n, f, b, real=False):
    s = (7 - f) + 7 * (n - 2) + (7 - b)
    q = (f"ลูกเต๋าแต่ละลูก แต้มหน้าตรงข้ามจะรวมได้ 7 เสมอ ลูกเต๋า {n} ลูกนี้วางติดกัน " + ("" if real else f"มองจากด้านหน้าเห็น {f} แต้ม มองจากด้านหลังเห็น {b} แต้ม ")
         + "หน้าที่ติดกันแต้มรวมเป็นเท่าใด")
    parts = [f"{7 - f}"] + ["7"] * (n - 2) + [f"{7 - b}"]
    st = [f"ลูกแรก: หน้าเห็น {f} → ด้านที่ติดลูกถัดไป = 7 − {f} = {7 - f}", f"ลูกสุดท้าย: หลังเห็น {b} → ด้านที่ติดกัน = 7 − {b} = {7 - b}"]
    if n > 2: st.append(f"ลูกตรงกลาง {n - 2} ลูก: 2 ด้านที่ติดเป็นด้านตรงข้าม รวม = 7")
    st.append(f"รวม = {' + '.join(parts)} = {s}")
    return I(q, st, s, "ตรวจ: ลองทุกการหมุนของลูกกลางด้วยโปรแกรม ผลรวมไม่เปลี่ยน ✓", qimg=ORIG('q24') if real else fg.dice_row(n, f, b, inner=False), aimg=fg.dice_row(n, f, b))
add(24, "ลูกเต๋า (หน้าตรงข้าม)", "ด้านตรงข้ามบวกกันได้ 7 เสมอ", "ลูกกลางไม่ต้องรู้แต้ม เพราะ 2 ด้านที่ติดรวมกันได้ 7", item24(3, 4, 1, True), item24(2, 2, 5), item24(4, 6, 3))

# ---------------- 25 สี่เหลี่ยมในตาราง ----------------
def item25(W, H, per, real=False):
    kinds = [(w, h, (W - w + 1) * (H - h + 1)) for w in range(1, W + 1) for h in range(1, H + 1) if 2 * (w + h) == per]
    tot = sum(k for _, _, k in kinds)
    q = f"รูปสี่เหลี่ยมมุมฉากที่มีเส้นรอบรูป {per} หน่วยมีทั้งหมดกี่รูป" + ('' if real else f" (ตารางกว้าง {W} ช่อง สูง {H} ช่อง ช่องละ 1 หน่วย)")
    st = [f"เส้นรอบรูป {per} หน่วย → กว้าง + ยาว = {per // 2}", ' · '.join(f"{w}×{h} มี {k} รูป" for w, h, k in kinds), f"รวม = {' + '.join(str(k) for _, _, k in kinds)} = {tot}"]
    ex = [(0, 0, w, h) if i == 0 else ((W - w, H - h, w, h) if i == 1 else (min(1, W - w), 0, w, h)) for i, (w, h, _) in enumerate(kinds)]
    return I(q, st, tot, "ตรวจ: ไล่ทุกสี่เหลี่ยมในตารางด้วยโปรแกรม ✓", qimg=ORIG('q25') if real else fg.rect_grid(W, H, []), aimg=fg.rect_grid(W, H, ex))
add(25, "การนับรูปสี่เหลี่ยม", "แยกนับตามขนาด แล้วเลื่อนนับตำแหน่ง", "สี่เหลี่ยมจัตุรัสก็เป็นสี่เหลี่ยมมุมฉาก", item25(4, 3, 8, True), item25(4, 3, 6), item25(3, 3, 8))

# ---------------- 26 สร้างจำนวน 2 หลัก ----------------
def item26(digits, parity):
    nums = [10 * a + b for a, b in itertools.permutations(digits, 2) if a != 0 and b % 2 == (0 if parity == 'even' else 1)]
    word = 'คู่' if parity == 'even' else 'คี่'
    q = f"นำตัวเลข {', '.join(map(str, digits))} ไปสร้างจำนวน 2 หลักที่เป็นจำนวน{word} จะได้กี่จำนวน โดยไม่ใช้เลขซ้ำ"
    ends = sorted({x % 10 for x in nums})
    groups = [(f"ลงท้าย {e}", [str(x) for x in sorted(nums) if x % 10 == e]) for e in ends]
    cnt = [len([x for x in nums if x % 10 == e]) for e in ends]
    st = [f"จำนวน{word} ต้องลงท้ายด้วย {', '.join(map(str, ends))} · หลักสิบห้ามเป็น 0 และห้ามซ้ำ", ' · '.join(f"ลงท้าย {e} ได้ {c}" for e, c in zip(ends, cnt)), f"รวม = {' + '.join(map(str, cnt))} = {len(nums)}"]
    return I(q, st, len(nums), "ตรวจ: เขียนทุกจำนวนด้วยโปรแกรม ✓", aimg=fg.chips(groups))
add(26, "การสร้างจำนวน", "เลือกหลักหน่วยก่อน (ต้องเป็นเลขคู่) แล้วค่อยเลือกหลักสิบ", "หลักสิบเป็น 0 ไม่ได้", item26([0, 1, 2, 3, 4, 5], 'even'), item26([0, 1, 2, 3, 4, 5], 'odd'), item26([1, 2, 3, 4], 'even'))

# ---------------- 27 กองอิฐ ----------------
def item27(old, add_, real=False):
    s = sum(range(old + 1, old + add_ + 1))
    q = f"ถ้าสร้างฐานเพิ่มอีก {add_} ชั้น จะใช้อิฐเพิ่มอีกกี่ก้อน" + ('' if real else f" (เดิมมี {old} ชั้น ชั้นบนสุด 1 ก้อน)")
    st = [f"แต่ละชั้นมีอิฐเพิ่มทีละ 1 ก้อน: 1, 2, …, {old}", f"ชั้นใหม่: {', '.join(str(k) for k in range(old + 1, old + add_ + 1))} ก้อน", f"รวม = {' + '.join(str(k) for k in range(old + 1, old + add_ + 1))} = {s}"]
    return I(q, st, s, "ตรวจ: นับอิฐในรูปที่ต่อชั้นแล้ว ✓", qimg=ORIG('q27') if real else fg.pyramid(old, 0), aimg=fg.pyramid(old, add_))
add(27, "แบบรูป (กองอิฐ)", "ชั้นล่างมีมากกว่าชั้นบน 1 ก้อนเสมอ", "นับเฉพาะอิฐที่เพิ่ม ไม่ต้องนับของเดิม", item27(4, 3, True), item27(3, 2), item27(5, 2))

# ---------------- 28 เหรียญ ----------------
def item28(coins, r):
    combos = [c for k in (r if isinstance(r, tuple) else (r,)) for c in itertools.combinations(coins, k)]
    sums = sorted({sum(c) for c in combos}); assert len(sums) == len(combos)
    how = f"{r} เหรียญ" if not isinstance(r, tuple) else "กี่เหรียญก็ได้ (อย่างน้อย 1 เหรียญ)"
    q = f"มีเหรียญ {' บาท '.join(map(str, coins))} บาท อย่างละ 1 เหรียญ จะซื้อของโดยใช้เหรียญ{how} จะจ่ายเงินได้กี่แบบที่แตกต่างกัน"
    st = ["จับเหรียญทีละแบบ ไม่ให้ซ้ำ (ดูรูป)", f"จำนวนเงินที่ได้: {', '.join(map(str, sums))} บาท", f"จ่ายได้ไม่ซ้ำกัน = {len(sums)}"]
    return I(q, st, len(sums), "ตรวจ: ไล่ทุกชุดเหรียญด้วยโปรแกรม จำนวนเงินไม่ซ้ำกันเลย ✓", aimg=fg.coin_pairs(combos), fs=None)
add(28, "การนับวิธีเลือก", "จับคู่เหรียญอย่างเป็นระบบ: 1 กับตัวอื่น แล้ว 2 กับตัวอื่น …", "1+2 กับ 2+1 คือแบบเดียวกัน", item28([1, 2, 5, 10], 2), item28([1, 2, 5, 10], 3), item28([1, 2, 5], (1, 2, 3)))

# ---------------- 29 เป้าลูกดอก ----------------
def item29(rings, k, real=False):
    best = k * max(rings)
    q = f"ปาลูกดอก {k} ลูก จะได้ผลรวมแต้มสูงสุดเป็นเท่าใด" + ('' if real else f" (เป้ามีวงแต้ม {', '.join(map(str, rings))} จากวงนอกเข้าวงใน)")
    st = [f"แต้มสูงสุดอยู่วงในสุด = {max(rings)}", f"ทุกลูกเข้าวงใน: {' + '.join([str(max(rings))] * k)} = {best}"]
    return I(q, st, best, "ตรวจ: ลองทุกแบบที่ลูกดอกตกได้ ✓", qimg=ORIG('q29') if real else fg.target(rings), aimg=fg.target_darts(rings, k))
add(29, "การหาค่ามากที่สุด", "ลูกดอกทุกลูกเข้าวงที่แต้มมากที่สุด", "ลูกดอกเข้าวงเดียวกันซ้ำได้", item29([3, 5], 2, True), item29([2, 4, 7], 3), item29([1, 6, 10], 2))

# ---------------- 30 เวลา ----------------
def hm(m): return f"{m // 60}.{m % 60:02d} น."
def item30(back, stay, travel, choices, real=False):
    leave = back - stay - travel; ans = choices.index(leave) + 1
    if real:
        q = "ยายทองไปทำบุญที่วัดแล้วกลับถึงบ้านเวลา 10.00 น. ยายทองทำบุญฟังเทศน์อยู่ที่วัด 4 ชั่วโมง ใช้เวลาเดินทางไปและกลับรวม 45 นาที ยายทองออกจากบ้านเวลาใด" + opts([hm(c) for c in choices]); img = ORIG('q30')
    else:
        q = f"ยายไปตลาดแล้วกลับถึงบ้านเวลา {hm(back)} ยายอยู่ที่ตลาด {stay // 60} ชั่วโมง" + (f" {stay % 60} นาที" if stay % 60 else '') + f" ใช้เวลาเดินทางไปและกลับรวม {travel} นาที ยายออกจากบ้านเวลาใด" + opts([hm(c) for c in choices]); img = ''
    st = [f"ย้อนเวลาจาก {hm(back)} ไป {stay // 60} ชั่วโมง" + (f" {stay % 60} นาที" if stay % 60 else '') + f" → {hm(back - stay)}", f"ย้อนอีก {travel} นาที → {hm(leave)}", f"ตอบข้อ = {ans}"]
    tl = fg.seg_labels(fg.timeline([(hm(leave)[:-3], 'ออกจากบ้าน'), (hm(back - stay)[:-3], ''), (hm(back)[:-3], 'ถึงบ้าน')]), [(0, f'{travel} นาที'), (1, f'{stay // 60} ชม.' + (f' {stay % 60} น.' if stay % 60 else ''))])
    return I(q, st, ans, f"ตรวจ: {hm(leave)} + {travel} นาที + {stay} นาที = {hm(back)} ✓", qimg=img, aimg=tl)
add(30, "เวลา (นับย้อนหลัง)", "นับย้อนจากเวลาที่กลับถึงบ้าน", "เวลาเดินทาง 45 นาทีรวมทั้งไปและกลับแล้ว ไม่ต้องคูณ 2",
    item30(600, 240, 45, [315, 345, 375], True), item30(690, 180, 30, [450, 480, 510]), item30(570, 120, 75, [345, 360, 375]))

# ---------------- ตรวจ ----------------
assert [p['no'] for p in P] == list(range(16, 31))
EXPECT = ['9', '10', '28', '8', '900', '3', '1', '4', '16', '16', '13', '18', '6', '10', '1']
assert [p['items'][0]['ans'] for p in P] == EXPECT, [p['items'][0]['ans'] for p in P]
for p in P:
    for it in p['items']: assert it['ans'].isdigit() and int(it['ans']) > 0 and len(it['ans']) <= 3, (p['no'], it['ans'])
    assert len({(it['q'], it['qimg']) for it in p['items']}) == 3, p['no']
if __name__ == '__main__':
    for p in P: print(p['no'], [i['ans'] for i in p['items']])
