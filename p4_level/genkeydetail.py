import html,re
code=open('genlevel.py').read(); code=code[:code.index('for i,q in enumerate(Q)')]
ns={};exec(code,ns);Q=ns['Q'];base=ns['ns']
M=lambda n:('−' if n<0 else '')+str(abs(n))
def terms(side):
    return [((-1 if s=='−' else 1),t) for s,t in re.findall(r'([+−]?)\s*([XY]|\d+)',side.replace(' ',''))]
def steps(e,V,x):
    L,R=[s.strip() for s in e.split('=')]
    out=[]
    if V not in L:
        L,R=R,L; out.append(('สลับข้าง ให้ตัวแปรอยู่ซ้าย',f'{L} = {R}'))
    tl=terms(L);tr=terms(R)
    sv=[s for s,t in tl if t==V][0]
    c=[(s,int(t)) for s,t in tl if t!=V][0]; d=[(s,int(t)) for s,t in tr][0]
    vt=('−' if sv<0 else '')+V
    rhs=d[0]*d[1]; mv=-c[0]*c[1]
    op='−' if mv<0 else '+'
    out.append((f'ย้ายข้าง {c[1]} ({"+" if c[0]>0 else "−"} เป็น {op})',f'{vt} = {M(rhs)} {op} {abs(mv)}'))
    val=rhs+mv
    out.append(('คำนวณ',f'{vt} = {M(val)}'))
    if sv<0: out.append(('เปลี่ยนเครื่องหมายทั้งสองข้าง',f'{V} = {M(-val)}'))
    assert sv*x==val
    # check
    L0,R0=[s.strip() for s in e.split('=')]
    sub=lambda s:s.replace(V,str(x))
    ev=lambda s:eval(s.replace('−','-'))
    side,other=(L0,R0) if V in L0 else (R0,L0)
    assert ev(sub(side))==ev(other)
    chk=f'{sub(side)} = {M(ev(sub(side)))} ✓'
    return out,chk
css=base['css']+'''
.bar .main{font-size:15pt}
.kgrid{flex:1;margin-bottom:3.5mm;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);grid-auto-flow:column;grid-template-rows:repeat(5,1fr);gap:3mm 3.4mm;min-height:0}
.dq{position:relative;border:1.3px solid #c6d4ee;border-top:1.6mm solid var(--c);border-radius:4mm;padding:2.4mm 4mm 2mm 10mm;background:rgba(255,255,255,.6);display:flex;flex-direction:column;gap:.5mm;min-height:0}
.dq .n{left:-1.2mm;top:-1.4mm}
.de{display:flex;align-items:center;font-family:Mali;font-weight:700;font-size:13.5pt;margin-bottom:1mm;color:#10244a}
.de b{margin-left:auto;background:#f5b800;color:#1c3a6b;border-radius:2.4mm;padding:0 2.4mm;font-size:11pt}
.st{display:grid;grid-template-columns:5mm 1fr auto;align-items:center;gap:1.6mm;font-size:9pt;padding:.4mm 0;border-bottom:1px dashed #dbe4f4}
.st i{font-style:normal;width:4.4mm;height:4.4mm;border-radius:50%;background:#e8eefb;color:#1c3a6b;text-align:center;line-height:4.4mm;font-size:7pt;font-weight:700}
.st span{color:#4a6aa8;font-weight:600;white-space:nowrap}.st code{font-family:Mali;font-weight:700;color:#10244a;font-size:11pt;white-space:nowrap}
.ck{margin-top:auto;font-size:9.4pt;font-weight:700;color:#1f8a4c;background:#e9f7ef;border-radius:1.8mm;padding:.3mm 2mm;white-space:nowrap;overflow:hidden}
'''
def card(i):
    e,V,x,_=Q[i]; ss,chk=steps(e,V,x)
    rows=''.join(f'<div class="st"><i>{k+1}</i><span>{html.escape(a)}</span><code>{html.escape(b)}</code></div>' for k,(a,b) in enumerate(ss))
    return f'<div class="dq c{(i//5)%3}"><span class="n">{i+1}</span><div class="de">{html.escape(e)}<b>{V} = {x}</b></div>{rows}<div class="ck">แทนค่า : {html.escape(chk)}</div></div>'
def header(right):
    return f'<div class="bar"><span></span><div class="ttl"><span class="main"><b>1</b>การแก้สมการที่เป็นบวกลบ</span><span class="lev">(เฉลยแบบละเอียด · คณิตศาสตร์ ป.4)</span></div><span class="pill">{right}</span></div>'
tip='<div class="tip"><b>หลักการ</b> · ① ให้ตัวแปรอยู่ทางซ้าย ② ย้ายตัวเลขที่อยู่ข้างเดียวกับตัวแปรไปอีกข้าง แล้วเปลี่ยนเครื่องหมาย (+ ↔ −) ③ ถ้าตัวแปรติดลบ ให้เปลี่ยนเครื่องหมายทั้งสองข้าง ④ แทนค่าตรวจคำตอบ</div>'
pages=[(0,10),(10,20),(20,30)];out=''
for pi,(a,b) in enumerate(pages):
    out+=f'<div class="pg"><img class="wm" src="logo.png">{header("เฉลยละเอียด")}{tip if pi==0 else ""}<div class="sec"><span class="p">ข้อ {a+1}–{b}</span><span class="h">แสดงวิธีทำทีละขั้น พร้อมตรวจคำตอบ</span></div><div class="kgrid">{"".join(card(i) for i in range(a,b))}</div>{base["footer"](pi+1)}</div>'
open('lvdetail.html','w').write(f'<!doctype html><meta charset=utf-8><style>{css}</style>'+out)

