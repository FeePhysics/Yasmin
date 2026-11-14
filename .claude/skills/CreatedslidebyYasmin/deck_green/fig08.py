import math,html
INK='#1E3A28';GR='#2F7D4B';DG='#1F5C37';SH='#9AD2A8';YL='#F6E58D';RD='#D9534F';HI='#C9A22A'
def T(x,y,s,sz=22,anchor='middle',fill=INK,wt=700):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{sz}" font-weight="{wt}" text-anchor="{anchor}" fill="{fill}" font-family="Mali">{html.escape(str(s))}</text>'
def SV(w,h,body,cls='img'): return f'<svg class="{cls}" viewBox="0 0 {w:.0f} {h:.0f}">{body}</svg>'
def P(x,y): return f'{x:.1f},{y:.1f}'
# ---------- Q26 : วงแหวน ----------
def ring(s,area,hide=False):
    sc=95/s;S=2*s*sc;R=s*math.sqrt(2)*sc;r=s*sc
    W=2*R+110;H=2*R+70;cx=W/2+5;cy=H/2
    x0,y0,x1,y1=cx-S/2,cy-S/2,cx+S/2,cy+S/2
    o=[f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{R:.1f}" fill="{SH}" stroke="{INK}" stroke-width="3"/>',
       f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{S:.1f}" height="{S:.1f}" fill="none" stroke="{INK}" stroke-width="3"/>',
       f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#fff" stroke="{INK}" stroke-width="3"/>',
       f'<line x1="{x0:.1f}" y1="{y1:.1f}" x2="{x1:.1f}" y2="{y0:.1f}" stroke="{INK}" stroke-width="3"/>',
       f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{cx:.1f}" y2="{y1:.1f}" stroke="{INK}" stroke-width="3"/>',
       f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x1:.1f}" y2="{cy:.1f}" stroke="{INK}" stroke-width="3"/>',
       f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{S/2:.1f}" height="{S/2:.1f}" fill="{YL}" opacity=".7"/>',
       f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="{INK}"/>']
    o.append(T(cx+S/4,cy+S/4+9,area,26,fill=INK))
    lab=[('B',x0-16,y0-6),('C',x1+16,y0-6),('A',x0-16,y1+22),('D',x1+16,y1+22),('E',cx,y1+22),('F',cx-16,cy-8),('G',x1+14,cy-8)]
    for t,x,y in lab: o.append(T(x,y,t,22))
    if hide==False: pass
    return SV(W,H,''.join(o))
def ring_ans(s,area):
    sc=95/s;S=2*s*sc;R=s*math.sqrt(2)*sc
    base=ring(s,area)
    W=2*R+110;cx=W/2+5;cy=(2*R+70)/2
    ex=T(cx+S/4,cy+S/4-8,f'{s}',20,fill=DG)+T(cx+S/4,cy-S/2-0,'',1)
    # side labels s on EF and FG
    ex=T(cx-10,cy+S/4+7,f'{s}',22,anchor='end',fill=DG)+T(cx+S/4,cy-8,f'{s}',22,fill=DG)
    return base.replace('</svg>',ex+'</svg>')
# ---------- Q27 : หกเหลี่ยมในวงกลม ----------
def hexa(r,diam=None,show=False):
    sc=105/1;W=400;H=300;cx=200;cy=150;R=105
    pts=[(cx+R*math.cos(math.radians(60*i)),cy-R*math.sin(math.radians(60*i))) for i in range(6)]
    o=[f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{INK}" stroke-width="3"/>',
       f'<polygon points="{" ".join(P(*p) for p in pts)}" fill="{SH}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>']
    for p in pts: o.append(f'<line x1="{cx}" y1="{cy}" x2="{p[0]:.1f}" y2="{p[1]:.1f}" stroke="{INK}" stroke-width="2" stroke-dasharray="6 5"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="{INK}"/>')
    if diam:
        o.append(f'<line x1="{pts[3][0]:.1f}" y1="{pts[3][1]:.1f}" x2="{pts[0][0]:.1f}" y2="{pts[0][1]:.1f}" stroke="{RD}" stroke-width="4"/>')
        o.append(T(cx,cy-12,f'{diam}',26,fill=RD))
    else:
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{pts[0][0]:.1f}" y2="{pts[0][1]:.1f}" stroke="{RD}" stroke-width="4"/>')
        o.append(T(cx+55,cy-8,f'{r}',24,fill=RD))
    if show:
        for i in range(6):
            a=pts[i];b=pts[(i+1)%6];mx,my=(a[0]+b[0])/2,(a[1]+b[1])/2
            dx,dy=mx-cx,my-cy;n=math.hypot(dx,dy)
            o.append(T(mx+dx/n*22,my+dy/n*22+7,f'{r}',22,fill=DG))
    return SV(W,H,''.join(o))
# ---------- Q28 : เส้นขนานหักมุม ----------
def arcp(cx,cy,r,a1,a2,col=INK,w=2.5):
    n=max(2,int(abs(a2-a1)/3));pts=[]
    for i in range(n+1):
        a=math.radians(a1+(a2-a1)*i/n);pts.append((cx+r*math.cos(a),cy-r*math.sin(a)))
    return f'<polyline points="{" ".join(P(*p) for p in pts)}" fill="none" stroke="{col}" stroke-width="{w}"/>'
def lab(cx,cy,r,a1,a2,txt,col=INK,sz=21):
    m=math.radians((a1+a2)/2);return T(cx+r*math.cos(m),cy-r*math.sin(m)+7,txt,sz,fill=col)
def zig(al,be,ga,show=False):
    a=be-al;b=90-a;th=ga-b;X=180-th
    assert a>0 and b>0 and th>0
    ya,H1=0.0,150.0
    ymid=ya+H1
    d1=0.42*H1                       # P below top line
    tr=lambda d:math.tan(math.radians(d))
    dxP=d1/tr(al)                    # P.x - T.x
    dxa=(H1-d1)/tr(a)                # P.x - a.x
    Px=0.0;Tx=Px-dxP;ax=Px-dxa
    bx=Px+105;Lb=70
    Qx=bx-Lb*math.cos(math.radians(b));Qy=ymid+Lb*math.sin(math.radians(b))
    h2=52;ybot=Qy+h2;Rx=Qx+h2/tr(th)
    ext=55;Ex=Rx+ext*math.cos(math.radians(th));Ey=ybot+ext*math.sin(math.radians(th))
    minx=min(Tx,ax)-40;maxx=max(Ex,bx)+50
    W=maxx-minx;Hh=ybot+75-(ya-40)
    ox=-minx;oy=-(ya-40)
    X_=lambda x:x+ox;Y_=lambda y:y+oy
    L=lambda x1,y1,x2,y2,c=INK,w=3.2,d='':f'<line x1="{X_(x1):.1f}" y1="{Y_(y1):.1f}" x2="{X_(x2):.1f}" y2="{Y_(y2):.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"{d}/>'
    o=[]
    o.append(L(Tx-8,ya,bx+30,ya));o.append(L(ax-10,ymid,bx,ymid));o.append(L(Qx-120,ybot,Rx,ybot))
    o.append(L(Tx,ya,Px,ya+d1));o.append(L(Px,ya+d1,ax,ymid));o.append(L(bx,ymid,Qx,Qy));o.append(L(Qx,Qy,Ex,Ey))
    if show: o.append(L(Qx,Qy,Rx+20,Qy,HI,2.5,' stroke-dasharray="7 6"'))
    AR=lambda cx,cy,r,a1,a2,c=INK,w=2.6:arcp(X_(cx),Y_(cy),r,a1,a2,c,w)
    LB=lambda cx,cy,r,a1,a2,t,c=INK,sz=21:lab(X_(cx),Y_(cy),r,a1,a2,t,c,sz)
    G=DG
    o.append(AR(Tx,ya,34,-al,0));o.append(T(X_(Tx)+52,Y_(ya)-10,f'{al}°',24))
    o.append(AR(Px,ya+d1,32,180-al,180+a));o.append(T(X_(Px)-58,Y_(ya+d1)+8,f'{be}°',24))
    o.append(AR(ax,ymid,36,0,a))
    o.append(AR(bx,ymid,34,180,180+b))
    o.append(AR(Qx,Qy,32,-th if show else -th,b) if False else AR(Qx,Qy,30,-th,b))
    # X arc : from 180 through 270 to 360-th
    o.append(AR(Rx,ybot,34,180,360-th))
    ta=f'a = {a}°' if show else 'a'; tb=f'b = {b}°' if show else 'b'; tx=f'X = {X}°' if show else 'X'
    cA=DG if show else INK
    o.append(T(X_(ax)+60,Y_(ymid)+32,ta,24,fill=cA))
    o.append(LB(bx,ymid,0,180,180+b,'',INK,1))
    o.append(T(X_(bx)+14,Y_(ymid)-14,tb,24,anchor='start',fill=cA))
    o.append(T(X_(Qx)+44,Y_(Qy)-30,f'{ga}°',24,anchor='start'))
    o.append(T(X_(Rx)+8,Y_(ybot)+64,tx,26,fill=(RD if show else INK)))
    if show:
        o.append(LB(Qx,Qy,70,-th,0,f'{th}°',HI,19))
        o[-1]=T(X_(Rx)+26,Y_(Qy)+6,f'{th}°',22,anchor='start',fill=HI)
    return SV(W,Hh,''.join(o))
# ---------- Q29 : รูปร่าง ----------
def shape(kind,col,size=1.0):
    s=f'fill="{col}" stroke="#1E3A28" stroke-width="2.5" stroke-linejoin="round"'
    if kind=='heart': return f'<path d="M20 35 C2 22 2 8 12 6 C17 5 20 9 20 12 C20 9 23 5 28 6 C38 8 38 22 20 35Z" {s}/>'
    if kind=='circle': return f'<circle cx="20" cy="20" r="15" {s}/>'
    if kind=='diamond': return f'<polygon points="20,3 36,20 20,37 4,20" {s}/>'
    if kind=='star':
        pts=[(20+17*math.cos(math.radians(-90+36*i))*(1 if i%2==0 else .45)*1,20+17*math.sin(math.radians(-90+36*i))*(1 if i%2==0 else .45)) for i in range(10)]
        return f'<polygon points="{" ".join(P(*p) for p in pts)}" {s}/>'
    if kind=='square': return f'<rect x="5" y="5" width="30" height="30" rx="3" {s}/>'
    if kind=='triangle': return f'<polygon points="20,4 37,35 3,35" {s}/>'
    if kind=='pentagon':
        pts=[(20+17*math.cos(math.radians(-90+72*i)),21+17*math.sin(math.radians(-90+72*i))) for i in range(5)]
        return f'<polygon points="{" ".join(P(*p) for p in pts)}" {s}/>'
    if kind=='hexagon':
        pts=[(20+17*math.cos(math.radians(60*i)),20+17*math.sin(math.radians(60*i))) for i in range(6)]
        return f'<polygon points="{" ".join(P(*p) for p in pts)}" {s}/>'
    if kind=='cross': return f'<polygon points="14,3 26,3 26,14 37,14 37,26 26,26 26,37 14,37 14,26 3,26 3,14 14,14" {s}/>'
def ic(kind,col='#1E3A28'): return f'<svg class="shp" viewBox="0 0 40 40">{shape(kind,col)}</svg>'
# ---------- Q30 : ลูกเต๋า ----------
def die(nb,nr,order='bbrr'):
    """nb black, nr red dots in the 2x2 grid; dots fill positions TL,TR,BL,BR in order given: blacks first then reds."""
    pos=[(14,14),(34,14),(14,34),(34,34)]
    cols=['#1E3A28']*nb+['#E0262B']*nr
    # place: spread dots so single dots sit top-left
    use=pos[:nb+nr] if nb+nr in (1,2,4) else pos[:3]
    body=''.join(f'<circle cx="{x}" cy="{y}" r="5.2" fill="{c}"/>' for (x,y),c in zip(use,cols))
    return f'<svg class="die" viewBox="0 0 48 48"><rect x="2" y="2" width="44" height="44" rx="3" fill="#fff" stroke="#1E3A28" stroke-width="3"/>{body}</svg>'
if __name__=='__main__':
    open('figtest.html','w').write('<!doctype html><meta charset=utf-8><style>svg{width:300px;border:1px solid #ccc;margin:4px}.shp,.die{width:40px}</style>'+ring(7,49)+ring_ans(7,49)+hexa(9)+hexa(15,30,True)+zig(30,55,80)+zig(30,55,80,True)+zig(20,50,85,True)+zig(25,65,78,True)+''.join(ic(k,'#8CCB9E') for k in ['heart','circle','diamond','star','square','triangle','pentagon','hexagon','cross'])+die(4,0)+die(1,3)+die(1,2)+die(0,1))
