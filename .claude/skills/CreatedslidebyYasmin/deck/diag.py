import html, math
def PAL(kind):
    return dict(main='#F28C28',light='#FFD9A8',dk='#D9701A') if kind=='real' else dict(main='#4FAE6B',light='#CFE8BC',dk='#2F8A4E')
YEL='#FFD84D'; INK='#4A2F17'
def T(x,y,s,sz=30,anchor='middle',fill=INK,wt=700):
    return f'<text x="{x:.0f}" y="{y:.0f}" font-size="{sz}" font-weight="{wt}" text-anchor="{anchor}" fill="{fill}" font-family="Mali">{html.escape(str(s))}</text>'
def R(x,y,w,h,fill,sw=3,dash=False,rx=8,stroke=INK):
    d=' stroke-dasharray="9 7"' if dash else ''
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def BR(x1,x2,y,up=True,s=14,col=INK):
    m=(x1+x2)/2;k=-1 if up else 1
    d=f'M{x1:.0f},{y-k*s:.0f} Q{x1:.0f},{y:.0f} {x1+s:.0f},{y:.0f} L{m-s:.0f},{y:.0f} Q{m:.0f},{y:.0f} {m:.0f},{y+k*s:.0f} Q{m:.0f},{y:.0f} {m+s:.0f},{y:.0f} L{x2-s:.0f},{y:.0f} Q{x2:.0f},{y:.0f} {x2:.0f},{y-k*s:.0f}'
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="3.5" stroke-linecap="round"/>'
def SVG(w,h,body): return f'<svg class="img" viewBox="0 0 {w} {h}">{body}</svg>'
fm=lambda n:f"{n:,}"
# ---------- 23 additive bar ----------
def d23(segs,unit,kind):
    p=PAL(kind);tot=sum(v for _,v in segs);x0=60;W=880;u=W/tot;y=118;h=72;o=[]
    x=x0
    for i,(lab,v) in enumerate(segs):
        last=i==len(segs)-1
        o.append(R(x,y,v*u,h,YEL if last else (p['light'] if i%2==0 else '#FFF3D6' if kind=='real' else '#E6F4D8')))
        o.append(T(x+v*u/2,y+h/2+11,f"{v}",34)); o.append(T(x+v*u/2,y+h+34,lab,23,fill=p['dk']))
        x+=v*u
    o.append(BR(x0,x0+W,y-14,True)); o.append(T(500,y-48,f"เดิมมี ? {unit} = {tot} {unit}",32,fill=p['dk']))
    o.append(T(500,y+h+88," + ".join(str(v) for _,v in segs)+f" = {tot} {unit}",30))
    return SVG(1000,290,''.join(o))
# ---------- 15 fraction bar ----------
def d15(T_,d,n,known,ask,room,kind):
    p=PAL(kind);x0=60;W=880;u=W/d;y=130;h=84;o=[];v=T_//d
    for i in range(d):
        isk=i<n
        o.append(R(x0+i*u,y,u,h,p['light'] if isk else YEL)); o.append(T(x0+i*u+u/2,y+h/2+11,v,32))
    o.append(BR(x0,x0+W,y-14,True)); o.append(T(500,y-46,f"{room} ทั้งหมด {T_} คน",32,fill=p['dk']))
    o.append(BR(x0,x0+n*u,y+h+14,False)); o.append(T(x0+n*u/2,y+h+64,f"{known} {n}/{d} = {n} ส่วน",27,fill=p['dk']))
    o.append(BR(x0+n*u,x0+W,y+h+14,False)); o.append(T(x0+n*u+(W-n*u)/2,y+h+64,f"{ask} {d-n} ส่วน = ? คน",27,fill=p['dk']))
    o.append(T(500,y+h+112,f"1 ส่วน = {T_} ÷ {d} = {v} คน",30))
    return SVG(1000,330,''.join(o))
# ---------- 13 percent bars ----------
def d13(P,pct,up,y3,kind):
    p=PAL(kind);ex=P*pct//100;y2=P+ex if up else P-ex;mx=max(P+ex,y3,y2);x0=190;W=620;s=W/mx;o=[]
    rows=[(24,'ปีแรก'),(96,'ปีที่ 2'),(168,'ปีที่ 3')];h=50
    for yy,lab in rows: o.append(T(20,yy+h/2+10,lab,27,'start',p['dk']))
    o.append(R(x0,rows[0][0],P*s,h,p['light'])); o.append(T(x0+P*s/2,rows[0][0]+h/2+10,fm(P),28))
    if up:
        o.append(R(x0,rows[1][0],P*s,h,p['light'])); o.append(R(x0+P*s,rows[1][0],ex*s,h,YEL))
        o.append(T(x0+P*s/2,rows[1][0]+h/2+10,fm(P),28)); o.append(T(x0+P*s+ex*s/2,rows[1][0]+h/2+10,f"+{pct}%",26))
        o.append(T(x0+(P+ex)*s+12,rows[1][0]+h/2+10,f"= {fm(y2)}",28,'start',p['dk']))
    else:
        o.append(R(x0,rows[1][0],y2*s,h,p['light'])); o.append(R(x0+y2*s,rows[1][0],ex*s,h,'#fff',dash=True))
        o.append(T(x0+y2*s/2,rows[1][0]+h/2+10,fm(y2),28)); o.append(T(x0+y2*s+ex*s/2,rows[1][0]+h/2+10,f"−{pct}%",26))
    o.append(R(x0,rows[2][0],y3*s,h,p['light'])); o.append(T(x0+y3*s/2,rows[2][0]+h/2+10,fm(y3),28))
    lo,hi=sorted([y2,y3])
    o.append(f'<line x1="{x0+lo*s:.0f}" y1="{rows[1][0]+h+4}" x2="{x0+lo*s:.0f}" y2="{rows[2][0]+h+22}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 6"/>')
    o.append(f'<line x1="{x0+hi*s:.0f}" y1="{rows[1][0]+h+4}" x2="{x0+hi*s:.0f}" y2="{rows[2][0]+h+22}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 6"/>')
    bx1,bx2=x0+lo*s,x0+hi*s
    o.append(BR(bx1-2,bx2+2,rows[2][0]+h+34,False,s=10)); o.append(T(500,rows[2][0]+h+92,f"ปีที่ 2 ต่างจากปีที่ 3 = {fm(hi-lo)} บาท",30,fill=p['dk']))
    return SVG(1000,320,''.join(o))
# ---------- 19 columns ----------
def d19(n,base,ex,nb,ne,unit,kind):
    p=PAL(kind);cw=min(46,880/n);gap=cw*0.14;x0=500-(n*cw)/2;s=cw-gap;ybase=262;o=[]
    legs=n*base+ex
    o.append(T(500,34,f"ช่องสีอ่อน = {unit}ที่ทุกตัวมี ({n} × {base} = {n*base} {unit})",25,fill=p['dk']))
    o.append(T(500,72,f"ช่องสีเหลือง = {unit}ที่เพิ่มของตัวที่มีมากกว่า ({legs} − {n*base} = {ex} {unit})",25))
    for i in range(n):
        x=x0+i*cw
        for b in range(base): o.append(R(x+gap/2,ybase-(b+1)*s,s,s,p['light'],sw=2.5,rx=5))
        if i>=n-ex: o.append(R(x+gap/2,ybase-(base+1)*s,s,s,YEL,sw=2.5,rx=5))
    nm=n-ex
    o.append(BR(x0+gap/2,x0+nm*cw-gap/2,ybase+16,False,s=12)); o.append(T(x0+nm*cw/2,ybase+66,f"{nb} {nm} ตัว",27,fill=p['dk']))
    o.append(BR(x0+nm*cw+gap/2,x0+n*cw-gap/2,ybase+16,False,s=12)); o.append(T(x0+nm*cw+ex*cw/2,ybase+66,f"{ne} {ex} ตัว",27,fill=p['dk']))
    o.append(T(500,ybase+118,f"ต่างกัน {abs(nm-ex)} ตัว",32,fill=p['dk']))
    return SVG(1000,400,''.join(o))
# ---------- 22 ages ----------
def d22(yr,big,small,nb,ns,t,kind):
    p=PAL(kind);diff=big-small;mx=big+t;s=300/mx;o=[]
    def panel(x0,title,b,sm,double):
        o.append(T(x0+150,34,title,28,fill=p['dk']))
        if double:
            o.append(R(x0,60,diff*s,46,p['light'])); o.append(R(x0+diff*s,60,diff*s,46,p['light']))
            o.append(T(x0+diff*s/2,92,diff,28)); o.append(T(x0+diff*s*1.5,92,diff,28))
        else:
            o.append(R(x0,60,b*s,46,p['light'])); o.append(T(x0+b*s/2,92,b,28))
        o.append(R(x0,116,sm*s,46,YEL)); o.append(T(x0+sm*s/2,148,sm,28))
        o.append(T(x0-10,92,nb,22,'end',p['dk'])); o.append(T(x0-10,148,ns,22,'end',p['dk']))
    panel(135,f"ปี {yr} (ตอนนี้)",big,small,False)
    o.append(BR(135+small*s,135+big*s,182,False,s=10)); o.append(T(135+(small+big)*s/2,236,f"ต่างกัน {diff} ปี (คงที่)",25))
    panel(655,f"ปี {yr+t} (อีก {t} ปี)",big+t,small+t,True)
    o.append(T(655+150,236,f"{nb}อายุ 2 เท่าของ{ns}",25)); o.append(T(655+150,268,f"{ns}อายุ {diff} ปี",25,fill=p['dk']))
    o.append(f'<line x1="520" y1="26" x2="520" y2="280" stroke="{INK}" stroke-width="2.5" stroke-dasharray="5 7"/>')
    return SVG(1000,290,''.join(o))
# ---------- 17 timeline ----------
def d17(cyc,start,kind):
    p=PAL(kind);l=cyc[0]
    for c in cyc[1:]: l=l*c//math.gcd(l,c)
    x0,x1=290,960;s=(x1-x0)/l;o=[];ys=[80,138,196]
    for yy,c,i in zip(ys,cyc,range(3)):
        o.append(T(10,yy+8,f"เครื่องที่ {i+1}: {c:,} วิ",25,'start',p['dk']))
        o.append(f'<line x1="{x0}" y1="{yy}" x2="{x1}" y2="{yy}" stroke="{INK}" stroke-width="3"/>')
        k=0
        while k*c<=l:
            x=x0+k*c*s;last=k*c==l
            o.append(f'<line x1="{x:.1f}" y1="{yy-(18 if last else 11)}" x2="{x:.1f}" y2="{yy+(18 if last else 11)}" stroke="{p["dk"] if not last else INK}" stroke-width="{4 if last else 3}"/>')
            k+=1
    o.append(f'<line x1="{x1}" y1="42" x2="{x1}" y2="222" stroke="{p["main"]}" stroke-width="4" stroke-dasharray="8 7"/>')
    o.append(f'<line x1="{x0}" y1="42" x2="{x0}" y2="222" stroke="{p["main"]}" stroke-width="4" stroke-dasharray="8 7"/>')
    o.append(T(x0,30,f"เริ่มพร้อมกัน {start} น.",25,'middle')); o.append(T(990,30,"เสร็จพร้อมกันครั้งที่ 2",25,'end'))
    o.append(R(250,246,500,50,YEL,rx=14)); o.append(T(500,281,f"ค.ร.น. = {l:,} วินาที = {l//60} นาที",30))
    return SVG(1000,310,''.join(o))
DIAG={}
def put(no,k,fn): DIAG[(no,k)]=fn
for k,a in enumerate([(10200,50,True,14770),(8400,25,True,9860),(12600,20,False,11000)]): put(13,k,lambda kind,a=a:d13(*a,kind))
for k,a in enumerate([(57,3,2,'ชาย','หญิง','ห้อง ป.5/6'),(54,9,5,'ชาย','หญิง','ห้อง ป.6/2'),(36,4,3,'หญิง','ชาย','ห้อง ป.4/2')]): put(15,k,lambda kind,a=a:d15(*a,kind))
for k,a in enumerate([((300,200,260),'16:00'),((240,150,180),'09:00'),((360,240,180),'13:00')]): put(17,k,lambda kind,a=a:d17(*a,kind))
for k,a in enumerate([(18,3,8,'โต๊ะ 3 ขา','โต๊ะ 4 ขา','ขา'),(20,3,12,'เก้าอี้ 3 ขา','เก้าอี้ 4 ขา','ขา'),(22,2,13,'จักรยาน 2 ล้อ','สามล้อ 3 ล้อ','ล้อ')]): put(19,k,lambda kind,a=a:d19(*a,kind))
for k,a in enumerate([(2568,53,23,'อาเล็ก','หลานชาย',7),(2568,49,19,'ป้าอ้อ','หลานสาว',11),(2568,60,28,'ลุงต้อม','หลานชาย',4)]): put(22,k,lambda kind,a=a:d22(*a,kind))
SEG=[([('น้องสาว',3),('พ่อ',2),('แม่',2),('เพื่อน ๆ',6),('เหลือ',2)],'กก.'),
     ([('ย่า',5),('พี่ชาย',3),('น้องสาว',3),('เพื่อนบ้าน',8),('เหลือ',4)],'กก.'),
     ([('ลุง',6),('ป้า',4),('น้า',4),('เพื่อน ๆ',9),('เหลือ',5)],'กก.')]
for k,(sg,u) in enumerate(SEG): put(23,k,lambda kind,sg=sg,u=u:d23(sg,u,kind))
if __name__=='__main__':
    import sys
    body=''.join(f'<div style="width:1000px;border:1px solid #ccc;margin:6px;background:#fffdf6">{DIAG[key](kd)}</div>' for key in [(13,0),(13,2),(15,0),(15,2),(17,0),(19,0),(19,2),(22,0),(23,0)] for kd in ['real'])
    open('diag_test.html','w').write(f'<!doctype html><meta charset=utf-8><style>@font-face{{font-family:Mali;font-weight:700;src:url(ff/mali-thai-700-normal.woff2);unicode-range:U+0E01-0E5B}}@font-face{{font-family:Mali;font-weight:700;src:url(ff/mali-latin-700-normal.woff2);unicode-range:U+0000-00FF,U+2212}}svg{{width:100%;height:auto}}</style>'+body)
