import html
from fractions import Fraction as Fr
from math import gcd
src=open('/home/user/Yasmin/.claude/skills/CreatedbookbyYasmin/gen3.py').read().split('\n')
seg='\n'.join(src[86:src.index([l for l in src if l.startswith('def sol')][0])])
ns={'html':html};exec(seg,ns)
# operand: (whole, num, den); whole-only => (w,0,1); fraction => (0,n,d)
def P(s):
    s=s.strip()
    if ' ' in s: w,f=s.split(); n,d=f.split('/'); return (int(w),int(n),int(d))
    if '/' in s: n,d=s.split('/'); return (0,int(n),int(d))
    return (int(s),0,1)
RAW='''4/6|8;6/14|15;12/18|9;16/24|32;25/45|15;4 4/8|27;2 2/7|24;3 4/6|33;2 3/9|27;2 10/15|10;
20|16/22;21|42/35;40|50/60;65|26/30;45|27/36;3/7|3/8;4/8|6/10;6/15|12/18;27/33|15/18;55/65|22/26;
5 4/9|7/18;3 4/12|20/48;2 10/15|15/45;2 2/12|13/24;2 7/9|10/27;16|1 6/24;25|2 10/15;32|2 4/8;8|3 1/5;60|1 10/20;
5/15|2 5/10;4/6|1 2/4;12/20|4 8/10;21/27|2 12/15;50|1 10/20;2 2/12|1 7/32;6 3/7|3 9/21;5 4/9|1 2/12;3 4/12|7 3/6;3 3/8|2 8/12'''
Q=[tuple(P(x) for x in it.split('|')) for it in RAW.replace('\n','').split(';')]
assert len(Q)==40
def fr(n,d,cls=''): return f'<span class="fr {cls}"><span>{n}</span><span>{d}</span></span>'
def opnd(o):
    w,n,d=o
    if n==0: return f'<span class="wh">{w}</span>'
    return (f'<span class="wh">{w}</span>' if w else '')+fr(n,d)
def imp(o): w,n,d=o; return (w*d+n,d)
def mixed(f):
    if f.denominator==1: return f'<span class="wh">{f.numerator}</span>'
    w,r=divmod(f.numerator,f.denominator)
    return (f'<span class="wh">{w}</span>' if w else '')+fr(r,f.denominator)
X=' <span class="op">×</span> ';D=' <span class="op">÷</span> ';E=' <span class="op">=</span> '
def solve(a,b):
    segs=[('โจทย์',opnd(a)+D+opnd(b))]
    A,B=imp(a);C,Dd=imp(b)
    if a[0] or b[0]:
        note=[]
        for o in (a,b):
            if o[0] and o[1]: note.append(f'{o[0]}×{o[2]}+{o[1]}')
        segs.append(('แปลงเป็นเศษเกิน'+(f' ({", ".join(note)})' if note else ''),fr(A,B)+D+fr(C,Dd)))
    segs.append(('÷ เป็น × กลับเศษเป็นส่วน',fr(A,B)+X+fr(Dd,C)))
    N,M=A*Dd,B*C
    segs.append(('คูณเศษ คูณส่วน',fr(f'{A} × {Dd}',f'{B} × {C}')+E+fr(N,M)))
    g=gcd(N,M);f=Fr(N,M)
    assert f==Fr(a[0]*a[2]+a[1],a[2])/Fr(b[0]*b[2]+b[1],b[2])
    if g>1: segs.append((f'ทำเป็นอย่างต่ำ (÷ {g})',mixed(Fr(N//g,1)) if M//g==1 else fr(N//g,M//g)))
    if f.denominator!=1 and f.numerator>f.denominator: segs.append(('เขียนเป็นจำนวนคละ',mixed(f)))
    return segs,f
css=ns['css']+'''
.bar .main{font-size:15pt}
.list{flex:1;display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:repeat(8,1fr);gap:2.2mm;min-height:0;margin-bottom:3.5mm}
.fq{position:relative;border:1.3px solid #c6d4ee;border-left:1.8mm solid var(--c);border-radius:3.4mm;background:rgba(255,255,255,.62);display:flex;align-items:center;padding:1mm 3mm 1mm 11mm;min-height:0}
.fq .n{left:2.4mm;top:50%;transform:translateY(-50%)}
.chain{flex:1;min-width:0;display:flex;align-items:stretch;flex-wrap:wrap;row-gap:1.2mm;align-content:center}
.sg{display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding:0 1.3mm;border-right:1px dashed #cfdbef}
.sg:last-child{border-right:0}
.sg .lb{font-size:6.3pt;font-weight:700;color:#4a6aa8;white-space:nowrap;background:#e8eefb;border-radius:1.6mm;padding:0 1.4mm;margin-bottom:.8mm}
.sg:first-child .lb{background:#1c3a6b;color:#fff;padding:.7mm 1.6mm .1mm}
.ex{flex:1;display:flex;align-items:center;font-family:Mali;font-weight:700;color:#10244a;font-size:10.6pt;white-space:nowrap}
.fr{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 .6mm;line-height:1.05}
.fr span:first-child{border-bottom:1.3px solid #10244a;padding:0 .8mm}
.fr span{padding:0 .8mm}
.wh{margin-right:.3mm;font-size:1.1em}.op{color:#4a6aa8;margin:0 .6mm}
.ans{margin-left:2mm;display:flex;flex-direction:column;align-items:center;justify-content:center;background:#f5b800;border-radius:2.6mm;padding:1mm 3mm;font-family:Mali;font-weight:700;color:#1c3a6b;font-size:11.5pt;min-width:16mm;flex:0 0 auto}
.ans small{font-size:6.6pt}.av{display:flex;align-items:center;white-space:nowrap}.ans .fr span:first-child{border-color:#1c3a6b}
'''
def header(right):
    return f'<div class="bar"><span></span><div class="ttl"><span class="main"><b>2</b>การหารเศษส่วน</span><span class="lev">(เฉลยแบบละเอียด · ทดสอบ 2 · 40 ข้อ)</span></div><span class="pill">{right}</span></div>'
tip='<div class="tip"><b>หลักการ</b> · ① จำนวนคละ / จำนวนนับ → เศษเกิน (จำนวนนับ n = n/1) ② เปลี่ยน ÷ เป็น × แล้วกลับตัวหาร (สลับเศษกับส่วน) ③ คูณเศษกับเศษ ส่วนกับส่วน ④ ทำเป็นเศษส่วนอย่างต่ำ ⑤ ถ้าเป็นเศษเกิน เขียนเป็นจำนวนคละ</div>'
cards=[];ANS=[]
for i,(a,b) in enumerate(Q):
    segs,f=solve(a,b);ANS.append(f)
    ch=''.join(f'<div class="sg"><span class="lb">{l}</span><div class="ex">{("" if k==0 else E)+x}</div></div>' for k,(l,x) in enumerate(segs))
    cards.append(f'<div class="fq c{(i//10)%3}"><span class="n">{i+1}</span><div class="chain">{ch}</div><div class="ans"><small>ตอบ</small><span class="av">{mixed(f)}</span></div></div>')
out=''
for p in range(5):
    out+=f'<div class="pg"><img class="wm" src="logo.png">{header("เฉลยละเอียด")}{tip if p==0 else ""}<div class="sec"><span class="p">ข้อ {p*8+1}–{p*8+8}</span><span class="h">แสดงวิธีทำทีละขั้น</span></div><div class="list">{"".join(cards[p*8:p*8+8])}</div>{ns["footer"](p+1)}</div>'
open('fracdetail.html','w').write(f'<!doctype html><meta charset=utf-8><style>{css}</style>'+out)
for i,f in enumerate(ANS):
    w,r=divmod(f.numerator,f.denominator); print(i+1, f, f'= {w} {r}/{f.denominator}' if w and r else '')
