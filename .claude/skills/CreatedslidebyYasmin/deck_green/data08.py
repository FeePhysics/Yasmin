import math
from fractions import Fraction as F
from lib import fr
import fig08 as fg
def g(x):
    if isinstance(x,F): x=float(x)
    return (f"{x:,.4f}".rstrip('0').rstrip('.')) if abs(x-round(x))>1e-9 else f"{int(round(x)):,}"
def I(q,steps,ans,chk,qimg='',aimg='',fs=None,note=''):
    return dict(q=q,steps=steps,ans=str(ans),chk=chk,qimg=qimg,aimg=aimg,fs=fs,note=note)
P=[]
def add(no,topic,tip,warn,*items): P.append(dict(no=no,topic=topic,tip=tip,warn=warn,items=list(items)))
PI227=fr(22,7)
# ---------------- 26 ----------------
def item26(s,pi):
    A=s*s
    if pi=='22/7':
        assert s%7==0;ans=F(22,7)*A;pis=f"{PI227}";pit=f"(ให้ π = {PI227})"
    else:
        ans=F(str(pi))*A;pis=str(pi);pit=f"(ให้ π = {pi})"
    assert ans.denominator==1;ans=int(ans)
    R2=2*A
    q=f"หากสี่เหลี่ยม DEFG มีพื้นที่ {A} ตารางหน่วย และ F เป็นจุดกึ่งกลางวงกลม จงหาว่าพื้นที่ที่แรเงาจะมีขนาดกี่ตารางหน่วย {pit}"
    st=[f"DEFG เป็นสี่เหลี่ยมจัตุรัส พื้นที่ {A} → ด้านยาว {s} × {s} = {A} → วงกลมเล็กมีรัศมี r = {s} หน่วย",
        f"รัศมีวงกลมใหญ่ R = FA → R² = {s}² + {s}² = {R2}",
        f"พื้นที่แรเงา = π × R² − π × r² → π × ({R2} − {A}) = π × {A}",
        f"{pis} × {A} = {ans} ตารางหน่วย"]
    chk=f"ตรวจ: พื้นที่วงกลมใหญ่ π × {R2} มากกว่าวงกลมเล็ก π × {A} อยู่ π × {A} = {ans} ✓ (แรเงา = π × พื้นที่ DEFG เสมอ)"
    return I(q,st,ans,chk,qimg=fg.ring(s,A),aimg=fg.ring_ans(s,A),note="ตีความ: ABCD เป็นสี่เหลี่ยมจัตุรัส วงกลมเล็กสัมผัสด้านทั้งสี่ และวงกลมใหญ่ผ่านจุด A, B, C, D ส่วนแรเงาคือส่วนระหว่างวงกลมใหญ่กับวงกลมเล็ก")
add(26,"พื้นที่ส่วนแรเงา: วงกลมกับสี่เหลี่ยมจัตุรัส","พื้นที่แรเงา = π × (R² − r²) และ R² − r² เท่ากับพื้นที่สี่เหลี่ยม DEFG พอดี","R และ r ต้องยกกำลังสอง ไม่ใช่นำรัศมีมาลบกัน",item26(7,'22/7'),item26(14,'22/7'),item26(10,'3.14'))
# ---------------- 27 ----------------
def item27(r=None,d=None):
    if d: r=d//2;assert d%2==0
    per=6*r
    if d: q=f"จงหาเส้นรอบรูปของรูปหกเหลี่ยมด้านเท่าที่แนบในวงกลมซึ่งมีเส้นผ่านศูนย์กลาง {d} หน่วยว่ามีค่าเท่าใด"
    else: q=f"จงหาเส้นรอบรูปของรูปหกเหลี่ยมด้านเท่าที่แนบในวงกลมรัศมี {r} หน่วยว่ามีค่าเท่าใด"
    st=[]
    if d: st.append(f"รัศมี = {d} ÷ 2 = {r} หน่วย")
    st+= [f"ลากรัศมีไปยังมุมทั้ง 6 → ได้สามเหลี่ยมด้านเท่า 6 รูป",f"ด้านของหกเหลี่ยม = รัศมี = {r} หน่วย",f"เส้นรอบรูป = 6 × {r} = {per} หน่วย"]
    chk=f"ตรวจ: {r} + {r} + {r} + {r} + {r} + {r} = {per} ✓"
    return I(q,st,per,chk,qimg=fg.hexa(r,d),aimg=fg.hexa(r,d,True),note="ตีความ: รูปหกเหลี่ยมด้านเท่ามีมุมเท่ากันทุกมุม จุดยอดทั้ง 6 อยู่บนวงกลม")
add(27,"เส้นรอบรูปหกเหลี่ยมด้านเท่าในวงกลม","หกเหลี่ยมด้านเท่าประกอบด้วยสามเหลี่ยมด้านเท่า 6 รูป ความยาวด้าน = รัศมีวงกลม","ถ้าโจทย์ให้เส้นผ่านศูนย์กลาง ต้องหารสองเพื่อหารัศมีก่อน",item27(9),item27(12),item27(d=30))
# ---------------- 28 ----------------
def item28(al,be,ga):
    a=be-al;b=90-a;th=ga-b;X=180-th
    assert a>0 and b>0 and th>0 and X==270-ga-a
    q="เส้นตรงสามเส้นที่ขนานกันและเส้นหักมุมเป็นดังรูป หากมุม a กับมุม b มีค่ารวมกันเป็นมุมฉาก จงหาว่า X มีค่าเท่าใด"
    st=[f"มุมยอด {be}° = {al}° + a → a = {be} − {al} = {a}°",
        f"a + b = 90° → b = 90 − {a} = {b}°",
        f"เส้นขนานผ่านมุม {ga}°: ส่วนบนเท่ากับ b = {b}° → ส่วนล่าง = {ga} − {b} = {th}°",
        f"X อยู่บนเส้นตรงเดียวกับ {th}° → X = 180 − {th} = {X}°"]
    chk=f"ตรวจ: a + b = {a} + {b} = 90 ✓ และ X + {th} = {X} + {th} = 180 ✓"
    return I(q,st,X,chk,qimg=fg.zig(al,be,ga),aimg=fg.zig(al,be,ga,True),note=f"ตีความ: มุม {be}° คือมุมยอดของเส้นหัก มุม a คือมุมที่จุดซ้ายกับเส้นขนานกลาง และ X คือมุมใต้เส้นขนานล่างที่วัดจากซ้ายไปถึงเส้นต่อ")
add(28,"มุมระหว่างเส้นขนานและเส้นหักมุม","มุมยอดของเส้นหักระหว่างเส้นขนาน = ผลรวมของมุมที่ทำกับเส้นขนานสองข้าง (ลากเส้นขนานช่วย)","ลำดับการหา a → b → มุมส่วนล่าง → X อย่าข้ามขั้น และ X รวมกับมุมเล็กได้ 180°",item28(30,55,80),item28(20,50,85),item28(25,65,78))
# ---------------- 29 ----------------
def item29(kinds,sums,vals):
    A,B,C=vals;k1,k2,k3=kinds
    pairs=[(A,B),(B,C),(A,C)];assert [x+y for x,y in pairs]==sums
    tot=sum(sums)//2;assert sum(sums)%2==0 and tot==A+B+C
    i1,i2,i3=[fg.ic(k,c) for k,c in zip(kinds,['#E86A6A','#6FB1E8','#F2C94C'])]
    def eq(x,y,v): return f"<div class='eqrow'>{x} + {y} = {v}</div>"
    q=f"กำหนดให้<div class='eqs'>{eq(i1,i2,sums[0])}{eq(i2,i3,sums[1])}{eq(i1,i3,sums[2])}</div>จงหาค่าของ <span class='nw'>{i1} + {i2} + {i3}</span>"
    st=[f"นำสมการทั้ง 3 มาบวกกัน: {sums[0]} + {sums[1]} + {sums[2]} = {sum(sums)}",
        f"แต่ละรูปปรากฏ 2 ครั้ง → 2 × ({i1} + {i2} + {i3}) = {sum(sums)}",
        f"{i1} + {i2} + {i3} = {sum(sums)} ÷ 2 = {tot}"]
    N=dict(heart='หัวใจ',circle='วงกลม',diamond='ข้าวหลามตัด',star='ดาว',square='สี่เหลี่ยม',triangle='สามเหลี่ยม',pentagon='ห้าเหลี่ยม',hexagon='หกเหลี่ยม',cross='กากบาท')
    n1,n2,n3=[N[k] for k in kinds]
    chk=f"ตรวจ: {n1} = {tot} − {sums[1]} = {A}, {n2} = {tot} − {sums[2]} = {B}, {n3} = {tot} − {sums[0]} = {C} → {A} + {B} = {sums[0]} ✓ {B} + {C} = {sums[1]} ✓ {A} + {C} = {sums[2]} ✓"
    return I(q,st,tot,_chk(chk))
def _chk(t): return t
add(29,"ระบบสมการจากรูปร่าง","บวกสมการทั้งสามเข้าด้วยกัน แต่ละรูปจะปรากฏ 2 ครั้ง แล้วหารด้วย 2","อย่าลืมหารด้วย 2 หลังบวก และรูปเดียวกันต้องมีค่าเท่ากันทุกสมการ",
    item29(('heart','circle','diamond'),[36,44,52],(22,14,30)),
    item29(('star','square','triangle'),[40,50,54],(22,18,32)),
    item29(('pentagon','hexagon','cross'),[36,54,48],(15,21,33)))
# ---------------- 30 ----------------
def item30(b,r,full,p1,p2,A,B,C,D):
    """full: die with 4 black =4b ; p1: die with (nb,nr) given value; A,B,C,D dice (nb,nr)"""
    v=lambda d:d[0]*b+d[1]*r
    assert 4*b==full[1] if False else True
    gv=lambda d:fg.die(*d)
    n1=4*b;n2=v(p1)
    num=v(A)*v(B);dv=v(C);dd=v(D);assert dv%dd==0
    ans=num+dv//dd
    q=f"กำหนดให้ {fg.die(4,0)} = {n1} และ {fg.die(*p1)} = {n2} จงหาค่าของ<div class='math'>{gv(A)} × {gv(B)} + {gv(C)} ÷ {gv(D)}</div>"
    st=[f"{fg.die(4,0)} = {n1} → จุดดำ 1 จุด = {n1} ÷ 4 = {b}",
        f"{fg.die(*p1)} = {n2} → จุดแดง 1 จุด = ({n2} − {p1[0]*b}) ÷ {p1[1]} = {r}",
        f"{gv(A)} = {A[0]} × {b} + {A[1]} × {r} = {v(A)} , {gv(B)} = {B[0]} × {b} + {B[1]} × {r} = {v(B)}",
        f"{gv(C)} = {C[0]} × {b} + {C[1]} × {r} = {v(C)} , {gv(D)} = {D[0]} × {b} + {D[1]} × {r} = {v(D)}",
        f"{v(A)} × {v(B)} + {v(C)} ÷ {v(D)} = {num} + {dv//dd} = {ans}"]
    chk=f"ตรวจ: {v(A)} × {v(B)} = {num} และ {v(C)} ÷ {v(D)} = {dv//dd} → {num} + {dv//dd} = {ans} (คูณหารก่อนบวก) ✓"
    return I(q,st,ans,chk)
add(30,"โจทย์ลูกเต๋า: หาค่าจุดสีแล้วคำนวณ","หาค่าจุดดำ 1 จุดและจุดแดง 1 จุดก่อน แล้วนับจุดแต่ละสีในแต่ละช่อง","คูณและหารก่อนบวก: 11 × 16 + 12 ÷ 4 ต้องไม่ใช่ (176 + 12) ÷ 4",
    item30(3,4,None,(1,3),None,(1,2),(0,4),(4,0),(0,1)),
    item30(3,6,None,(1,3),None,(1,2),(4,0),(0,4),(1,0)),
    item30(2,5,None,(2,2),None,(2,1),(0,3),(0,4),(1,0)))
assert [p['no'] for p in P]==[26,27,28,29,30]
if __name__=='__main__':
    for p in P: print(p['no'],[i['ans'] for i in p['items']])
