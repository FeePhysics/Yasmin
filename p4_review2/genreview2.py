import html,re,random
src=open('/home/user/Yasmin/.claude/skills/CreatedbookbyYasmin/gen3.py').read().split('\n')
seg='\n'.join(src[86:src.index([l for l in src if l.startswith('def sol')][0])])
ns={'html':html};exec(seg,ns)
ORIG='''96 = 25 + Y|61 − X = −14|Y + 48 = 74|52 = −27 + X|−Y + 40 = −48|31 − X = −50|−60 = 34 − X|56 = −22 + X|69 = Y − 19|−Y + 74 = 48|−57 = −Y − 25|−47 + X = 35|−79 = −Y − 48|33 = Y − 19|54 + X = 85|−54 + X = 37|990 = 132 + Y|−770 = −Y − 429|−354 = −Y − 110|418 + X = 665|−373 = −947 + X|−536 = Y − 976|−409 = Y − 530|351 − X = −136|243 = 989 − X|−784 + X = 176|261 = −563 + X|Y + 214 = 406|424 − X = 279|−Y + 683 = −107|−Y + 772 = 498|−685 + X = −314|Y + 1868 = 7060|2946 − X = −4016|−1335 = −5233 + X|−Y + 6319 = −3370|−4944 = Y − 9411|4889 = −4554 + X|1980 = Y − 7507|−3385 = 4605 − X|−Y + 4792 = −2985|−8247 = −Y − 1761|−8378 + X = −1210|−1411 + X = 4749|5521 + X = 9471|7587 = 1135 + Y|−7238 = −Y − 2655|4836 − X = 2487'''.split('|')
assert len(ORIG)==48
def parse(e):
    sides=[]
    for side in e.split('='):
        toks=re.findall(r'([+−]?)\s*(X|Y|\d+)',side.replace(' ',''))
        terms=[];first=True
        for sg,v in toks:
            s=-1 if sg=='−' else 1
            terms.append([s,v]);first=False
        sides.append(terms)
    return sides
def val(terms,var,a): return sum(s*(a if v in 'XY' else int(v)) for s,v in terms)
def fmt(sides):
    out=[]
    for terms in sides:
        p=''
        for k,(s,v) in enumerate(terms):
            if k==0: p+=('−' if s<0 else '')+v
            else: p+=(' − ' if s<0 else ' + ')+v
        out.append(p)
    return ' = '.join(out)
def solve(sides):
    # flatten L - R
    flat=[(s,v) for s,v in sides[0]]+[(-s,v) for s,v in sides[1]]
    sv=[s for s,v in flat if v in 'XY'][0]; var=[v for s,v in flat if v in 'XY'][0]
    cs=[(s,int(v)) for s,v in flat if v not in 'XY']
    return var,sv,cs
rnd=random.Random(3141)
band=lambda i:(10,99,18) if i<16 else ((100,999,180) if i<32 else (1000,9999,1800))
NEW=[]
for i,e in enumerate(ORIG):
    sd=parse(e); var,sv,cs=solve(sd)
    a0=-sum(s*c for s,c in cs)*sv  # sv*a + sum = 0 -> a = -sum/sv
    lo,hi,d=band(i)
    idx=[(si,k) for si in (0,1) for k,(s,v) in enumerate(sd[si]) if v not in 'XY']
    assert len(idx)==2
    for _ in range(10000):
        a=a0+rnd.randint(-d,d)
        (p0,k0),(p1,k1)=rnd.sample(idx,2)
        c1=int(sd[p0][k0][1])+rnd.randint(-d,d)
        if not(lo<=a<=hi and lo<=c1<=hi): continue
        nd=[[t[:] for t in s] for s in sd]; nd[p0][k0][1]=str(c1); nd[p1][k1][1]='0'
        # solve c2 so that L=R
        L=val(nd[0],var,a);R=val(nd[1],var,a)
        s2=nd[p1][k1][0]*(1 if p1==0 else -1)
        c2=-(L-R)//s2 if (L-R)%s2==0 else None
        if c2 is None or not(lo<=c2<=hi) or c2==int(sd[p1][k1][1]) or a==a0: continue
        nd[p1][k1][1]=str(c2)
        if val(nd[0],var,a)==val(nd[1],var,a): break
    else: raise Exception(i)
    e2=fmt(nd); _,_,cs2=solve(nd)
    # unique check
    sols=[x for x in range(1,10000) if val(nd[0],var,x)==val(nd[1],var,x)]
    assert sols==[a],(i,e2,sols)
    t=[(-s*sv,c) for s,c in cs2]; t.sort(key=lambda z:-z[0])
    expr=''.join((f'{c}' if k==0 else f' {"+" if s>0 else "−"} {c}') for k,(s,c) in enumerate(t))
    assert t[0][0]>0 and eval(expr.replace('−','-'))==a
    NEW.append((e2,var,a,f'{var} = {expr}'))
SEL=[0,1,4,6,7,9,10,12,13,15, 17,19,20,21,23,24,25,29,30,31, 33,34,35,36,37,39,40,41,42,46]
NEW=[NEW[i] for i in SEL]
assert len({n[0] for n in NEW})==30 and not {n[0] for n in NEW}&set(ORIG)
for i,n in enumerate(NEW): print(i+1,n[0],'|',n[3],'=',n[2])
css=ns['css']+'''
.bar .main{font-size:15pt}
.cmd{font-weight:700;font-size:9.6pt;color:#10244a;padding:0 1mm}.cmd b{background:#1c3a6b;color:#fff;border-radius:2mm;padding:.2mm 2mm;margin-right:1.5mm}.cmd i{font-style:normal;color:#4a6aa8}
.grid{grid-template-rows:repeat(5,1fr);gap:2.2mm 3.4mm}
.q{padding:2mm 3mm 2mm 9.5mm;gap:1.4mm}
.eqr{display:flex;align-items:center;gap:2mm}
.eq{font-family:Mali,sans-serif;font-weight:700;font-size:13.5pt;color:#10244a;letter-spacing:.2mm;white-space:nowrap}
.ab{margin-left:auto;display:flex;align-items:center;gap:1.5mm;font-weight:700;font-size:11pt;color:#1c3a6b;white-space:nowrap}
.ab span.bx{display:inline-block;width:20mm;height:7mm;border:1.3px solid #7c97c8;border-radius:2mm;background:#eef3fc}
.w{margin-top:2.6mm;display:flex;flex-direction:column;padding:3mm 3.5mm 1.6mm}.w i{flex:1;border-bottom:1.1px solid #b9c9e6}
.sec .lv{background:#1c3a6b;color:#fff;border-radius:6mm;padding:.8mm 4mm;font-weight:700;font-size:10.4pt}
.ks{font-size:8.8pt}.ke{font-size:7.6pt}.kg{grid-template-rows:repeat(15,1fr)}.ks{font-size:10pt}.ke{font-size:8.4pt}
.legend{display:flex;gap:3mm;font-weight:700;font-size:9pt}.legend span{border-radius:4mm;padding:.6mm 3.4mm;background:#e8eefb;border:1px solid #c6d4ee}
'''
LV=['หลักสิบ','หลักร้อย','หลักพัน']
HINT=['คำตอบเป็นจำนวนสองหลัก','คำตอบเป็นจำนวนสามหลัก','คำตอบเป็นจำนวนสี่หลัก']
def header(right):
    return f'<div class="bar"><span></span><div class="ttl"><span class="main"><b>1</b>การแก้สมการบวกลบ</span><span class="lev">(คณิตศาสตร์ ป.4 · ทบทวนก่อนสอบ ชุดที่ 2)</span></div><span class="pill">{right}</span></div>'
def card(i):
    e,v,a,s=NEW[i];lvc=['หลักสิบ','หลักร้อย','หลักพัน'][i//10]
    return f'<div class="q c{i%3}"><span class="n">{i+1}</span><div class="eqr"><span class="eq">{html.escape(e)}</span><span class="ab">{v} =<span class="bx"></span></span></div><div class="w"><span>วิธีคิด</span><i></i><i></i><i></i><i></i></div></div>'
out=''
for p in range(3):
    a=p*10
    top=''
    if p==0:
        top='<div class="info"><span>ชื่อ - นามสกุล</span><span class="fill" style="flex:1"></span><span>เลขที่</span><span class="fill" style="width:16mm"></span><span>ห้อง</span><span class="fill" style="width:18mm"></span><span>คะแนน</span><span class="fill" style="width:16mm"></span><span>/ 30</span></div><div class="cmd"><b>คำสั่ง</b>ให้นักเรียนหาค่าของตัวแปรในแต่ละสมการ พร้อมแสดงวิธีคิด <i>(คำตอบทุกข้อเป็นจำนวนบวก)</i></div>'
    out+=f'<div class="pg"><img class="wm" src="logo.png">{header("ทบทวน ชุดที่ 2")}{top}<div class="sec"><span class="lv">{" · ".join(dict.fromkeys(LV[i//10] for i in range(a,a+10)))}</span><span class="d">ข้อ {a+1}–{a+10}</span><span class="h">ย้ายข้างแล้วเปลี่ยนเครื่องหมาย · คำตอบเป็นจำนวนบวก</span></div><div class="grid">{"".join(card(a+j) for j in range(10))}</div>{ns["footer"](p+1)}</div>'
def kcell(i):
    e,v,a,s=NEW[i]
    return f'<div class="kq c{i//10}"><span class="n">{i+1}</span><div class="kt"><div class="ke">{html.escape(e)}</div><div class="ks">{html.escape(s)} = <b>{a}</b></div></div></div>'
tip='<div class="tip"><b>วิธีอ่านเฉลย</b> · ย้ายตัวเลขไปอีกข้างของ = แล้วเปลี่ยนเครื่องหมายเป็นตรงข้าม (บวก ↔ ลบ) ให้ตัวแปรเป็นบวก · ตัวเลขในช่องเหลืองคือคำตอบ</div><div class="legend"><span>ข้อ 1–10 หลักสิบ</span><span>ข้อ 11–20 หลักร้อย</span><span>ข้อ 21–30 หลักพัน</span></div>'
key=f'<div class="pg"><img class="wm" src="logo.png">{header("เฉลย ชุดที่ 2")}{tip}<div class="kg">{"".join(kcell(i) for i in range(30))}</div>{ns["footer"]()}</div>'
w=lambda b:f'<!doctype html><meta charset=utf-8><style>{css}</style>'+b
open('review2.html','w').write(w(out));open('review2key.html','w').write(w(key))
