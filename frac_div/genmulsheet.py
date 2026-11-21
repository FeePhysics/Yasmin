MRAW='''24|6/8;2/9|12/16;4|2 2/12;2 6/9|2 2/8;35|8/28;8/14|7/15;2 3/5|2;2 3/11|4 2/5;45|12/18;20/30|12/15;
7|2 2/21;2 3/4|2 2/5;121|9/11;12/16|30/50;7|4 2/14;2 4/12|2 6/7;45/60|18;12/20|14/15;11|3 2/22;1 7/17|2 2/16;
32|9/20;10/35|25/30;3 5/8|32;2 10/25|2 10/20;60/150|100;15/20|16/27;2 17/30|15;4 2/7|2 5/15;48|21/36;20/22|12/42;
27|3 3/9;4 5/10|2 5/10;9/60|75;21/27|15/21;21|3 3/7;2 3/11|4 2/5;40|33/96;16/18|27/30;7|2 10/21;3 6/8|6 4/8'''
code=open('genfrac.py').read(); code=code[:code.index("css=ns['css']")]
import re as _r
code=_r.sub(r"RAW='''.*?'''",lambda m:"RAW='''"+MRAW+"'''",code,flags=_r.S)
g={};exec(code,g);Q=g['Q'];opnd=g['opnd'];ns=g['ns']
css=ns['css']+'''
.bar .main{font-size:15pt}
.cmd{font-weight:700;font-size:9.8pt;color:#10244a;padding:0 1mm}.cmd b{display:inline-block;background:#1c3a6b;color:#fff;border-radius:2mm;padding:1.2mm 2.4mm .5mm;line-height:1.25;margin-right:1.5mm}
.cols{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);grid-auto-flow:column;grid-template-rows:repeat(10,1fr);gap:2mm 4mm;min-height:0;margin-bottom:3.5mm}
.it{position:relative;border:1.2px solid #c6d4ee;border-left:1.6mm solid var(--c);border-radius:3mm;background:rgba(255,255,255,.6);display:flex;flex-direction:column;padding:1.4mm 3mm 1.2mm 12.5mm;min-height:0}
.it .n{left:2mm;top:2mm}
.row{display:flex;align-items:center;gap:1.5mm}
.ex{font-family:Mali;font-weight:700;color:#10244a;font-size:13pt;white-space:nowrap;display:flex;align-items:center}
.fr{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 .6mm;line-height:1.05;font-size:.92em}
.fr span:first-child{border-bottom:1.3px solid #10244a}.fr span{padding:0 .8mm}
.wh{margin-right:.3mm;font-size:1.05em}.op{color:#4a6aa8;margin:0 1mm}
.eqs{margin-left:1.5mm;font-family:Mali;font-weight:700;color:#1c3a6b;font-size:13pt}
.bx{margin-left:auto;width:24mm;height:10mm;border:1.3px solid #7c97c8;border-radius:2mm;background:#eef3fc;position:relative}
.bx::before{content:"ตอบ";position:absolute;left:1.4mm;top:-2.4mm;background:#fff;padding:0 1mm;font-size:7pt;color:#4a6aa8;font-weight:700}
.wk{flex:1;margin-top:1mm;border-top:1px dashed #cfdbef}
.wk span{font-size:7pt;color:#9db6e0;font-weight:700}
'''
def header(right):
    return f'<div class="bar"><span></span><div class="ttl"><span class="main"><b>1</b>การคูณเศษส่วน</span><span class="lev">(ทดสอบ 1 · 40 ข้อ)</span></div><span class="pill">{right}</span></div>'
def item(i):
    a,b=Q[i]
    return f'<div class="it c{(i//10)%3}"><span class="n">{i+1}</span><div class="row"><span class="ex">{opnd(a)}<span class="op">×</span>{opnd(b)}</span><span class="eqs">=</span><span class="bx"></span></div><div class="wk"><span>วิธีคิด</span></div></div>'
info='<div class="info"><span>ชื่อ - นามสกุล</span><span class="fill" style="flex:1"></span><span>เลขที่</span><span class="fill" style="width:16mm"></span><span>ห้อง</span><span class="fill" style="width:18mm"></span><span>คะแนน</span><span class="fill" style="width:16mm"></span><span>/ 40</span></div><div class="cmd"><b>คำสั่ง</b>ให้นักเรียนหาผลคูณของเศษส่วนที่กำหนดให้ต่อไปนี้ (ตอบเป็นเศษส่วนอย่างต่ำหรือจำนวนคละ)</div>'
out=''
for p in range(2):
    a=p*20
    out+=f'<div class="pg"><img class="wm" src="logo.png">{header("ทดสอบ 1")}{info if p==0 else ""}<div class="sec"><span class="p">ข้อ {a+1}–{a+20}</span><span class="h">จำนวนคละ → เศษเกิน · ตัดทอน แล้วคูณเศษกับเศษ ส่วนกับส่วน</span></div><div class="cols">{"".join(item(i) for i in range(a,a+20))}</div>{ns["footer"](p+1)}</div>'
open('mulsheet.html','w').write(f'<!doctype html><meta charset=utf-8><style>{css}</style>'+out)
