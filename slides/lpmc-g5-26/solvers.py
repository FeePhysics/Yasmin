# ตัวแก้โจทย์แบบไล่ทุกกรณี (ใช้ทั้งตรวจข้อจริงและสร้าง/ตรวจ Mock Test) — LPMC ป.5 ครั้งที่ 26
import itertools

def solve_cards(rows, nums):
    """rows: [[('num',(n,c))|('let',(ch,c))|('hid',(None,c)), ...], ...]  c: 0 ดำ 1 ขาว  (ดำ < ขาว เมื่อเลขเท่ากัน)"""
    key = lambda x: x[0] * 2 + x[1]; order = [(n, c) for n in nums for c in (0, 1)]
    known = {x for r in rows for k, x in r if k == 'num'}
    slots = [(i, j) for i, r in enumerate(rows) for j, (k, x) in enumerate(r) if k != 'num']
    sols = set()
    def ok(a):
        for i, r in enumerate(rows):
            v = [key(x if k == 'num' else a[(i, j)]) for j, (k, x) in enumerate(r) if k == 'num' or (i, j) in a]
            if any(p >= q for p, q in zip(v, v[1:])): return False
        return True
    def bt(n, a, av):
        if len(sols) > 1: return
        if n == len(slots):
            sols.add(tuple(a[s][0] for s in slots if rows[s[0]][s[1]][0] == 'let')); return
        i, j = slots[n]; col = rows[i][j][1][1]
        for x in sorted(y for y in av if y[1] == col):
            a[(i, j)] = x
            if ok(a): bt(n + 1, a, av - {x})
            del a[(i, j)]
    bt(0, {}, set(order) - known); return sols

# ---- ลูกบาศก์: พับรูปคลี่แล้วดูว่าหน้าที่มีจุดอยู่ตรงไหน ----
def fold(cells):
    """cells: set of (r,c). คืน dict cell -> normal (x,y,z) ของหน้าลูกบาศก์ หรือ None ถ้าพับไม่ได้ 6 หน้า"""
    cells = set(cells); start = min(cells)
    # orientation: เก็บ (normal, up, right) แล้วกลิ้งไปทางขวา/ลง
    res = {start: ((0, 0, -1), (0, 1, 0), (1, 0, 0))}  # หน้าเริ่มคือ "ล่าง"
    neg = lambda v: tuple(-a for a in v)
    stack = [start]
    while stack:
        c = stack.pop(); n, up, rt = res[c]
        moves = {(0, 1): (rt, up, neg(n)), (0, -1): (neg(rt), up, n), (1, 0): (neg(up), n, rt), (-1, 0): (up, neg(n), rt)}
        for (dr, dc), (nn, nu, nr) in moves.items():
            d = (c[0] + dr, c[1] + dc)
            if d in cells and d not in res:
                if (dr, dc) == (0, 1): res[d] = (rt, up, neg(n))
                elif (dr, dc) == (0, -1): res[d] = (neg(rt), up, n)
                elif (dr, dc) == (1, 0): res[d] = (neg(up), n, rt)
                else: res[d] = (up, neg(n), rt)
                stack.append(d)
    normals = [v[0] for v in res.values()]
    if len(res) != 6 or len(set(normals)) != 6: return None
    return {c: v[0] for c, v in res.items()}

def dots_ok(cells, dots, want):
    """want='corner3' : จุด 3 หน้าที่ติดกันทั้งหมด (ไม่มีคู่ตรงข้าม) · 'opp2': จุด 2 หน้าตรงข้าม · 'adj2': จุด 2 หน้าติดกัน"""
    f = fold(cells)
    if f is None: return False
    ns = [f[d] for d in dots]
    opp = any(tuple(-a for a in p) == q for p, q in itertools.combinations(ns, 2))
    if want == 'corner3': return len(ns) == 3 and not opp
    if want == 'opp2': return len(ns) == 2 and opp
    if want == 'adj2': return len(ns) == 2 and not opp
