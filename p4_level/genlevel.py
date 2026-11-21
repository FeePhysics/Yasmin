import html,re,random
src=open('/home/user/Yasmin/.claude/skills/CreatedbookbyYasmin/gen3.py').read().split('\n')
seg='\n'.join(src[86:src.index([l for l in src if l.startswith('def sol')][0])])
ns={'html':html};exec(seg,ns)
# forms: (template, solve) with a,b constants, v variable; value of variable computed from a,b
F=[('a + V = b',lambda a,b:b-a),('V + a = b',lambda a,b:b-a),('b = a + V',lambda a,b:b-a),
   ('a − V = b',lambda a,b:a-b),('b = a − V',lambda a,b:a-b),('a − V = −b',lambda a,b:a+b),
   ('−b = a − V',lambda a,b:a+b),('b = −a + V',lambda a,b:a+b),('−a + V = −b',lambda a,b:a-b),
   ('−a + V = b',lambda a,b:a+b),('−b = V − a',lambda a,b:a-b),('b = V − a',lambda a,b:a+b),
   ('−V + a = b',lambda a,b:a-b),('−V + a = −b',lambda a,b:a+b),('−b = −V − a',lambda a,b:b-a),
   ('−b = −V + a',lambda a,b:a+b),('V − a = b',lambda a,b:a+b),('−V − a = −b',lambda a,b:b-a)]
rnd=random.Random(2026)
def rng(i):
    if i<10: return (10,99) if i<6 else (20,300)
    if i<20: return (100,999)
    return (100,4999)
Q=[];used=set();forms=list(range(len(F)))
order=[]
while len(order)<30:
    rnd.shuffle(forms); order+=forms
order=order[:30]
for i,fi in enumerate(order):
    t,f=F[fi];lo,hi=rng(i)
    while True:
        a=rnd.randint(lo,hi);b=rnd.randint(lo,hi)
        if i>=20 and rnd.random()<.35: a=rnd.choice([1000,1500,2000,2500,800,3000])
        x=f(a,b)
        if x<=0 or (a,b) in used or a==b: continue
        if i<10 and x>99: continue
        if 10<=i<20 and not 10<=x<=1999: continue
        break
    used.add((a,b))
    V='X' if i%2==0 else 'Y'
    e=t.replace('a',str(a)).replace('b',str(b)).replace('V',V)
    # verify by brute force
    py=e.replace('−','-').replace(V,'v'); L,R=py.split('=')
    sols=[v for v in range(1,20000) if eval(L,{'v':v})==eval(R,{'v':v})]
    assert sols==[x],(e,sols,x)
    # solution text
    flat=[]
    for side,sg in ((L,1),(R,-1)):
        for s,tok in re.findall(r'([+-]?)\s*(v|\d+)',side.replace(' ','')):
            flat.append(((-1 if s=='-' else 1)*sg,tok))
    sv=[s for s,t in flat if t=='v'][0]
    tt=sorted([(-s*sv,int(t)) for s,t in flat if t!='v'],key=lambda z:-z[0])
    ex=''.join((f'{c}' if k==0 else f' {"+" if s>0 else "−"} {c}') for k,(s,c) in enumerate(tt))
    assert tt[0][0]>0 and eval(ex.replace('−','-'))==x
    Q.append((e,V,x,f'{V} = {ex}'))
for i,q in enumerate(Q): print(i+1,q)
assert len({q[0] for q in Q})==30
css=ns['css']+'''
.bar .main{font-size:15pt}
.cols{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-flow:column;grid-template-rows:repeat(15,1fr);gap:0 6mm;min-height:0}
.it{display:flex;flex-direction:column;justify-content:flex-start;border-bottom:1.1px solid #b9c9e6;padding:1.6mm 0 0;min-height:0}
.row{display:flex;align-items:center;gap:2.4mm}
.it .n{position:static;flex:0 0 7mm;width:7mm;height:7mm;line-height:7mm;font-size:9.4pt}
.eq{font-family:Mali,sans-serif;font-weight:700;font-size:13.5pt;color:#10244a;white-space:nowrap;letter-spacing:.2mm}
.ab{margin-left:auto;display:flex;align-items:flex-end;gap:1.4mm;font-weight:700;font-size:12pt;color:#1c3a6b;white-space:nowrap}
.ab .bl{display:inline-block;width:19mm;border-bottom:1.3px solid #7c97c8;height:5.5mm;text-align:center;color:#d0342c;font-size:12.5pt}
.wk{flex:1;margin:1.4mm 0 1.4mm 9.4mm;border-bottom:1px dashed #cfdbef}
.sol{font-size:9.6pt;color:#4a6aa8;font-weight:600;margin:.8mm 0 0 9.4mm}
.cmd{font-weight:700;font-size:9.6pt;color:#10244a;padding:0 1mm}.cmd b{display:inline-block;background:#1c3a6b;color:#fff;border-radius:2mm;padding:1.2mm 2.4mm .5mm;line-height:1.25;margin-right:1.5mm}.cmd i{font-style:normal;color:#4a6aa8}
'''
def header(right):
    return f'<div class="bar"><span></span><div class="ttl"><span class="main"><b>1</b>การแก้สมการที่เป็นบวกลบ</span><span class="lev">(คณิตศาสตร์ ป.4 · 30 ข้อ)</span></div><span class="pill">{right}</span></div>'
def item(i,key):
    e,V,x,s=Q[i]
    body=f'<div class="sol">{html.escape(s)} = {x}</div>' if key else '<div class="wk"></div>'
    return f'<div class="it"><div class="row"><span class="n c{(i//5)%3}">{i+1}</span><span class="eq">{html.escape(e)}</span><span class="ab">{V} =<span class="bl">{x if key else ""}</span></span></div>{body}</div>'
info='<div class="info"><span>ชื่อ - นามสกุล</span><span class="fill" style="flex:1"></span><span>ชั้น</span><span class="fill" style="width:18mm"></span><span>เลขที่</span><span class="fill" style="width:14mm"></span><span>คะแนน</span><span class="fill" style="width:16mm"></span><span>/ 30</span></div><div class="cmd"><b>คำสั่ง</b>หาค่าของตัวแปรในแต่ละสมการ เขียนวิธีคิดใต้ข้อ <i>(คำตอบทุกข้อเป็นจำนวนบวก)</i></div>'
def page(key):
    return f'<div class="pg"><img class="wm" src="logo.png">{header("เฉลย" if key else "ใบงาน 30 ข้อ")}{"" if key else info}<div class="sec"><span class="p">ตอนที่ 1</span><span class="d">ข้อ 1–30 · เรียงลงมาตามคอลัมน์</span><span class="h">ย้ายข้างแล้วเปลี่ยนเครื่องหมาย</span></div><div class="cols">{"".join(item(i,key) for i in range(30))}</div>{ns["footer"](None if key else 1)}</div>'
w=lambda b:f'<!doctype html><meta charset=utf-8><style>{css}</style>'+b
open('lv.html','w').write(w(page(False)));open('lvkey.html','w').write(w(page(True)))
