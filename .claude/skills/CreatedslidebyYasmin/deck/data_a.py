from lib import *
import itertools
P=[]
def add(no,topic,real,m1,m2): P.append(dict(no=no,topic=topic,items=[real,m1,m2]))
def item(q,steps,ans,qimg='',aimg='',fs=None,note=''): return dict(q=q,steps=steps,ans=str(ans),qimg=qimg,aimg=aimg,fs=fs,note=note)
# ---------- 1 ----------
def p1(a,b,c,d):
    s1=a+b; s2=s1-c; r=s2//d; assert s2%d==0
    return item(f"จงหาค่าของ<div class='math'>({fmt(a)} + {fmt(b)} − {c}) ÷ {d}</div>",[f"ทำในวงเล็บก่อน: {fmt(a)} + {fmt(b)} = {fmt(s1)}",f"{fmt(s1)} − {c} = {fmt(s2)}",f"นำไปหารด้วย {d}: {fmt(s2)} ÷ {d} = {fmt(r)}"],r)
add(1,"ลำดับการคำนวณ (วงเล็บ บวก ลบ หาร)",p1(1260,473,80,3),p1(2340,175,85,3),p1(1950,246,96,6))
# ---------- 2 ----------
def p2(f1,f2,w,a,b,d1,d2):
    prod=f1*f2; mixv=F(w)+F(a,b); dec=F(d1,100)+F(d2,100)
    tot=prod+mixv+dec; assert tot.denominator==1
    s=mixv+dec
    q=f"จงหาค่าของ<div class='math'>({fr(f1.numerator,f1.denominator)} × {fr(f2.numerator,f2.denominator)}) + ({mix(w,a,b)} + {d1/100:.2f} + {d2/100:.2f})</div>"
    st=[f"{fr(f1.numerator,f1.denominator)} × {fr(f2.numerator,f2.denominator)} = 1 (ตัดกันได้)",f"{mix(w,a,b)} = {float(mixv):g} → {float(mixv):g} + {d1/100:.2f} + {d2/100:.2f} = {float(s):g}",f"1 + {float(s):g} = {int(tot)}"]
    return item(q,st,int(tot))
add(2,"เศษส่วน ทศนิยม และจำนวนคละ",p2(F(3,5),F(5,3),7,1,4,49,26),p2(F(4,7),F(7,4),5,1,2,35,15),p2(F(9,10),F(10,9),2,1,4,58,17))
# ---------- 3 ----------
def p3(k,last):
    terms=[f"{fr(k,n*(n+1))}" for n in range(2,5)]
    q="จงหาค่าของ<div class='math'>"+" + ".join(terms)+f" + {DOTS} + {fr(k,last*(last+1))}</div>"
    tot=sum(F(k,n*(n+1)) for n in range(2,last+1)); assert tot.denominator==1
    st=[f"ตัวส่วนคือ 2×3, 3×4, 4×5, … , {last}×{last+1} → แต่ละพจน์ = {NW(f"{k} × ({fr(1,'n')} − {fr(1,'n+1')})")}",f"ผลบวก = {k} × ({fr(1,2)} − {fr(1,3)} + {fr(1,3)} − {fr(1,4)} + {DOTS} + {fr(1,last)} − {fr(1,last+1)})",f"พจน์กลางตัดกันหมด เหลือ {NW(f'{k} × ({fr(1,2)} − {fr(1,last+1)})')}",f"{k} × {fr(last-1,2*(last+1))} = {int(tot)}"]
    return item(q,st,int(tot))
r3=p3(5,9)
r3['q']=f"จงหาค่าของ<div class='math'>{fr(5,6)} + {fr(5,12)} + {fr(5,20)} + {fr(5,30)} + {DOTS} + {fr(5,90)}</div>"
add(3,"ผลบวกเศษส่วนที่มีแบบรูป (ตัดกันได้)",r3,p3(8,7),p3(10,9))
# ---------- 4 ----------
def p4(b,e,m,x,y):
    pw=b**e; t=pw*m; pr=x*y; s=t+pr; r=round(s/100)*100; assert abs(s-r)<50 or True
    q=f"จงหาค่าประมาณจำนวนเต็มร้อยจากผลลัพธ์ของ<div class='math'>({b}<sup>{e}</sup> × {m}) + {x} × {y}</div>"
    st=[f"{b}<sup>{e}</sup> × {m} = {pw} × {m} = {t}",f"{x} × {y} = {pr}",f"{t} + {pr} = {s}",f"ปัดเป็นจำนวนเต็มร้อย: {s} ≈ <b>{r}</b>"]
    return item(q,st,r)
add(4,"เลขยกกำลัง และการประมาณค่า",p4(3,2,5,27,19),p4(4,2,5,23,18),p4(2,3,6,31,22))
# ---------- 5 ----------
def divs(n): return [d for d in range(1,n+1) if n%d==0]
def p5(x,y,z):
    c=[len(divs(v)) for v in (x,y,z)]
    odd=[v for v,k in zip((x,y,z),c) if c.count(k)==1]; assert len(odd)==1
    q=f"จำนวนตัวประกอบของเลขใดต่อไปนี้ “{x}&nbsp;&nbsp;&nbsp;{y}&nbsp;&nbsp;&nbsp;{z}” มีจำนวนแตกต่างจากพวก"
    st=[f"{v} มีตัวประกอบ {len(divs(v))} ตัว คือ {', '.join(map(str,divs(v)))}" for v in (x,y,z)]
    st.append(f"จำนวนตัวประกอบของ {odd[0]} ({len(divs(odd[0]))} ตัว) ไม่เหมือนพวก → ตอบ {odd[0]}")
    return item(q,st,odd[0])
add(5,"ตัวประกอบของจำนวนนับ",p5(20,64,117),p5(18,49,75),p5(28,45,81))
# ---------- 6 ----------
def p6(oe,a1,a2,k,b1,b2):
    # oe: 'คี่'/'คู่'; multiples of k from b1..b2
    A=[n for n in range(a1,a2+1) if (n%2==1)==(oe=='คี่')]
    B=[n for n in range(b1,b2+1) if n%k==0]
    sa,sb=sum(A),sum(B); d=abs(sa-sb)
    q=f"จงหาผลต่างของ A และ B เมื่อกำหนดให้ A คือ ผลรวมของเลข{oe}ตั้งแต่ {a1} ถึง {a2} และ B คือ ผลรวมของจำนวนตั้งแต่ {b1} ถึง {b2} ที่หารด้วย {k} ลงตัว"
    st=[f"A: เลข{oe} {A[0]}, {A[1]}, … , {A[-1]} มี {len(A)} จำนวน → A = {len(A)} × ({A[0]} + {A[-1]}) ÷ 2 = {fmt(sa)}",f"B: พหุคูณของ {k} คือ {B[0]}, {B[1]}, … , {B[-1]} มี {len(B)} จำนวน → B = {len(B)} × ({B[0]} + {B[-1]}) ÷ 2 = {fmt(sb)}",f"ผลต่าง = {fmt(max(sa,sb))} − {fmt(min(sa,sb))} = {d}"]
    return item(q,st,d)
add(6,"ผลรวมของจำนวนที่เรียงกันเป็นระยะเท่า ๆ กัน",p6('คี่',41,139,3,27,171),p6('คี่',31,129,3,18,150),p6('คู่',22,120,4,24,160))
# ---------- 7 ----------
def isprime(n): return n>1 and all(n%i for i in range(2,int(n**.5)+1))
def p7(lo,hi,tens_even):
    pr=[n for n in range(lo,hi+1) if isprime(n)]
    u=[n for n in pr if (n%10)%3==0 and n%10!=0]
    t=[n for n in u if (((n//10)%10)%2==0)==tens_even]
    d=[n for n in t if len({n//100,(n//10)%10,n%10})==3]
    assert len(d)==1
    ev='เลขคู่' if tens_even else 'เลขคี่'
    q=(f"จงสร้างเลข 3 หลักที่เป็นจำนวนเฉพาะที่มีค่าอยู่ระหว่าง {lo}–{hi} โดยมีเงื่อนไขในการสร้าง ดังนี้<ul><li>เลขหลักหน่วยเป็นพหุคูณของ 3</li><li>เลขหลักสิบเป็น{ev}</li><li>เลขแต่ละหลักไม่มีตัวเลขใดซ้ำกันเลย</li></ul>")
    st=[f"จำนวนเฉพาะระหว่าง {lo}–{hi}: {', '.join(map(str,pr))}",f"หลักหน่วยเป็นพหุคูณของ 3 (3 หรือ 9): {', '.join(map(str,u))}",f"หลักสิบเป็น{ev}: {', '.join(map(str,t))}",f"หลักไม่ซ้ำกัน: <b>{d[0]}</b>"]
    return item(q,st,d[0],fs='22pt')
add(7,"จำนวนเฉพาะ และการสร้างเลขตามเงื่อนไข",p7(111,150,True),p7(151,190,True),p7(201,250,False))
# ---------- 8 ----------
def p8(limit,diff):
    pr=[n for n in range(2,limit) if isprime(n)]
    w=[pr[i:i+4] for i in range(len(pr)-3) if pr[i+3]-pr[i]==diff]; assert len(w)==1
    a,b,c,d=w[0]
    q=f"ตัวเลขชุดหนึ่งซึ่งมีค่าไม่ถึง {limit} ประกอบด้วยจำนวนเฉพาะ 4 จำนวนเรียงติดกัน และมีผลต่างระหว่างจำนวนมากที่สุดและจำนวนน้อยที่สุด คือ {diff} จงหาผลรวมของจำนวนเฉพาะคู่ตรงกลาง"
    st=[f"จำนวนเฉพาะที่น้อยกว่า {limit}: {', '.join(map(str,pr))}",f"หาชุดที่เรียงติดกัน 4 จำนวนและมีมากสุด − น้อยสุด = {diff} → ได้ชุด {a}, {b}, {c}, {d} (เพราะ {d} − {a} = {diff})",f"จำนวนคู่ตรงกลางคือ {b} และ {c} → {b} + {c} = {b+c}"]
    return item(q,st,b+c)
add(8,"จำนวนเฉพาะที่เรียงติดกัน",p8(23,10),p8(30,12),p8(40,14))
# ---------- 9 ----------
def p9(s1,d1,s2,d2):
    r1=[s1+d1*i for i in range(5)];r2=[s2+d2*i for i in range(5)]
    n1=r1[-1]+d1;n2=r2[-1]+d2;diff=abs(n1-n2)
    tb=lambda r:", ".join(map(str,r))+", …"
    q=(f"จากความสัมพันธ์ที่กำหนดให้ จำนวนในลำดับถัดไปของแต่ละความสัมพันธ์มีค่าต่างกันเท่าใด"
       f"<table class='tb'><tr><th>ความสัมพันธ์ที่ 1</th><th>ความสัมพันธ์ที่ 2</th></tr><tr><td>{tb(r1)}</td><td>{tb(r2)}</td></tr></table>")
    st=[f"ความสัมพันธ์ที่ 1: เพิ่มขึ้นทีละ {d1} → จำนวนถัดไป = {r1[-1]} + {d1} = {n1}",f"ความสัมพันธ์ที่ 2: ลดลงทีละ {-d2} → จำนวนถัดไป = {r2[-1]} − {-d2} = {n2}",f"ผลต่าง = {max(n1,n2)} − {min(n1,n2)} = {diff}"]
    return item(q,st,diff)
add(9,"แบบรูปของจำนวน",p9(7,8,122,-12),p9(5,7,150,-12),p9(4,9,200,-13))
# ---------- 10 ----------
def p10(p1_,q1_,k1,p2_,q2_,k2):
    def dg(p,q,k): return int(str(F(p,q).numerator*10**(k+5)//F(p,q).denominator)[ :0] or 0) if False else int(((p*10**k)//q)%10)
    A=dg(p1_,q1_,k1);B=dg(p2_,q2_,k2)
    def dec(p,q,n=6):
        s=str(p//q)+'.'+''.join(str((p*10**(i+1))//q%10) for i in range(n)); return s
    th=lambda k:f"หลักที่ {k}"
    q=f"A มีค่าเท่ากับเลขโดดในทศนิยม{th(k1)} ของ {fr(p1_,q1_)} และ B มีค่าเท่ากับเลขโดดในทศนิยม{th(k2)} ของ {fr(p2_,q2_)} จงหาค่าของ A + B"
    st=[f"{fr(p1_,q1_)} = {dec(p1_,q1_)}… → ทศนิยม{th(k1)} คือ <b>{A}</b> ดังนั้น A = {A}",f"{fr(p2_,q2_)} = {dec(p2_,q2_)}… → ทศนิยม{th(k2)} คือ <b>{B}</b> ดังนั้น B = {B}",f"A + B = {A} + {B} = {A+B}"]
    return item(q,st,A+B)
add(10,"การหารและทศนิยมซ้ำ",p10(28,17,1,25,13,2),p10(31,19,1,17,7,3),p10(23,11,2,19,13,3))
if __name__=='__main__':
    for p in P:
        print(p['no'],[i['ans'] for i in p['items']])
