import math,html
INK='#10244a';NAVY='#1C3A6B';BL='#2F5FA8';LB='#CFE0F6';GY='#9AA7BC';CR='#F3E7C9'
def T(x,y,s,sz=22,anchor='middle',fill=INK,wt=700):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{sz}" font-weight="{wt}" text-anchor="{anchor}" fill="{fill}" font-family="Mali">{html.escape(str(s))}</text>'
def SV(w,h,body,cls='img'): return f'<svg class="{cls}" viewBox="0 0 {w} {h}">{body}</svg>'
def shoelace(p): 
    n=len(p);return abs(sum(p[i][0]*p[(i+1)%n][1]-p[(i+1)%n][0]*p[i][1] for i in range(n)))/2
# ---------- bar chart ----------
def bars(vals,ymax,step,show=False,title="แผนภูมิแสดงยอดเงินสะสมรายเดือนของนที"):
    W,H=560,330;x0,y0,x1,y1=70,50,540,270;h=y1-y0;n=len(vals);bw=(x1-x0)/n
    o=[T(W/2,28,title,19,fill=NAVY)]
    s=y0
    for v in range(0,ymax+1,step):
        y=y1-h*v/ymax
        o.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{GY if v else INK}" stroke-width="{2 if v else 2.5}"/>')
        o.append(T(x0-10,y+6,v,18,'end'))
    cols=['#1C3A6B','#2F5FA8','#4A86D8','#7FA6D8','#9AA7BC']
    for i,v in enumerate(vals):
        bx=x0+i*bw+bw*.22;bh=h*v/ymax
        o.append(f'<rect x="{bx:.1f}" y="{y1-bh:.1f}" width="{bw*.56:.1f}" height="{bh:.1f}" fill="{cols[i%5]}" rx="3"/>')
        if show: o.append(T(bx+bw*.28,y1-bh-8,v,20,fill=NAVY))
        o.append(T(x0+i*bw+bw/2,y1+30,f"เดือนที่ {i+1}",19))
    return SV(W,H,''.join(o))
# ---------- shaded grid ----------
def gridfig(N,shaded,lines,u=22,gridc='#C8D2E2'):
    W=N*u+24;H=N*u+24;X=lambda x:12+x*u;Y=lambda y:12+y*u
    o=[f'<rect x="12" y="12" width="{N*u}" height="{N*u}" fill="#fff"/>']
    for p in shaded:
        o.append('<polygon points="%s" fill="#8393AD"/>'%' '.join(f'{X(a):.1f},{Y(b):.1f}' for a,b in p))
    for i in range(N+1):
        o.append(f'<line x1="{X(i)}" y1="{Y(0)}" x2="{X(i)}" y2="{Y(N)}" stroke="{gridc}" stroke-width="1"/><line x1="{X(0)}" y1="{Y(i)}" x2="{X(N)}" y2="{Y(i)}" stroke="{gridc}" stroke-width="1"/>')
    for p in lines:
        o.append('<polygon points="%s" fill="none" stroke="#10244a" stroke-width="3" stroke-linejoin="round"/>'%' '.join(f'{X(a):.1f},{Y(b):.1f}' for a,b in p))
    return SV(W,H,''.join(o))
def pattern(N,corners,quads,halves):
    """diamond+inner square pattern. corners: subset of 'TL','TR','BR','BL'; quads: subset of inner-square quadrants;
    halves: subset of 'T','R','B','L' meaning which triangle's (clockwise-side) half shaded. returns shaded polys,lines,area"""
    h=N/2;q=N/4;m=3*N/4
    C={'TL':[(0,0),(h,0),(0,h)],'TR':[(h,0),(N,0),(N,h)],'BR':[(N,h),(N,N),(h,N)],'BL':[(0,h),(h,N),(0,N)]}
    Q={'TL':[(q,q),(h,q),(h,h),(q,h)],'TR':[(h,q),(m,q),(m,h),(h,h)],'BR':[(h,h),(m,h),(m,m),(h,m)],'BL':[(q,h),(h,h),(h,m),(q,m)]}
    Hh={'T':[(h,0),(m,q),(h,q)],'R':[(N,h),(m,q),(m,h)],'B':[(h,N),(q,m),(h,m)],'L':[(0,h),(q,m),(q,h)]}
    polys=[C[c] for c in corners]+[Q[c] for c in quads]+[Hh[c] for c in halves]
    lines=[[(h,0),(N,h),(h,N),(0,h)],[(0,0),(N,0),(N,N),(0,N)],[(q,q),(m,q),(m,m),(q,m)]]
    # inner dividers
    lines+= [[(h,0),(h,N)] if False else [(h,0),(h,0),(h,0)]]
    return polys,lines,sum(shoelace(p) for p in polys)
def gridpat(N,corners,quads,halves):
    polys,lines,area=pattern(N,corners,quads,halves)
    h=N/2;q=N/4;m=3*N/4
    lines=lines[:3]
    f=gridfig(N,polys,lines)
    # add divider lines
    extra=f'<line x1="{12+h*22}" y1="{12}" x2="{12+h*22}" y2="{12+N*22}" stroke="#10244a" stroke-width="3"/><line x1="12" y1="{12+h*22}" x2="{12+N*22}" y2="{12+h*22}" stroke="#10244a" stroke-width="3"/>'
    f=f.replace('</svg>',extra+'</svg>')
    return f,area
# ---------- concentric circles tangent at right ----------
def circles(radii,paint,a=None,unit='ซม.',labels=True):
    """radii: outer->inner (4 values). paint: list of fills outer->inner e.g. ['#8393AD','#fff','#8393AD','#fff']"""
    R=radii[0];s=170/R;W=2*R*s+40;H=2*R*s+40;cy=H/2;cx_r=W-20
    o=[]
    for r,f in zip(radii,paint):
        cx=cx_r-r*s
        o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r*s:.1f}" fill="{f}" stroke="{INK}" stroke-width="2"/>')
    if labels:
        lefts=[cx_r-2*r*s for r in radii]
        for i in range(3):
            x1,x2=lefts[i],lefts[i+1]
            o.append(f'<line x1="{x1+3:.1f}" y1="{cy:.1f}" x2="{x2-3:.1f}" y2="{cy:.1f}" stroke="{INK}" stroke-width="2"/><polygon points="{x1+3:.1f},{cy:.1f} {x1+12:.1f},{cy-5:.1f} {x1+12:.1f},{cy+5:.1f}" fill="{INK}"/><polygon points="{x2-3:.1f},{cy:.1f} {x2-12:.1f},{cy-5:.1f} {x2-12:.1f},{cy+5:.1f}" fill="{INK}"/>')
            o.append(T((x1+x2)/2,cy-9,'a',22))
    return SV(W,H,''.join(o))
# ---------- garden (rect + semicircles) ----------
def garden(w,h,sides,unit='หน่วย',u=None,pi_note=True):
    """rectangle w x h with semicircles on the listed sides ('T','B','L','R')."""
    u=u or 250/max(w+ (h if 'L' in sides else 0),1)
    u=min(u,260/(w+ (h if 'L' in sides and 'R' in sides else 0)+ (w if False else 0)+1)) if False else u
    sc=min(300/(w+(h if 'L' in sides else 0)+(h if 'R' in sides else 0)),240/(h+(w if 'T' in sides else 0)+(w if 'B' in sides else 0)))
    ex_l=(h/2*sc if 'L' in sides else 0);ex_r=(h/2*sc if 'R' in sides else 0);ex_t=(w/2*sc if 'T' in sides else 0);ex_b=(w/2*sc if 'B' in sides else 0)
    W=w*sc+ex_l+ex_r+60;H=h*sc+ex_t+ex_b+60
    x0=30+ex_l;y0=30+ex_t;ww=w*sc;hh=h*sc
    o=[f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{ww:.1f}" height="{hh:.1f}" fill="#CFE0F6" stroke="{INK}" stroke-width="3"/>']
    f='#EAD9AC'
    if 'T' in sides: o.append(f'<path d="M{x0:.1f},{y0:.1f} A{ww/2:.1f},{ww/2:.1f} 0 0 1 {x0+ww:.1f},{y0:.1f} Z" fill="{f}" stroke="{INK}" stroke-width="3"/>')
    if 'B' in sides: o.append(f'<path d="M{x0:.1f},{y0+hh:.1f} A{ww/2:.1f},{ww/2:.1f} 0 0 0 {x0+ww:.1f},{y0+hh:.1f} Z" fill="{f}" stroke="{INK}" stroke-width="3"/>')
    if 'L' in sides: o.append(f'<path d="M{x0:.1f},{y0:.1f} A{hh/2:.1f},{hh/2:.1f} 0 0 0 {x0:.1f},{y0+hh:.1f} Z" fill="{f}" stroke="{INK}" stroke-width="3"/>')
    if 'R' in sides: o.append(f'<path d="M{x0+ww:.1f},{y0:.1f} A{hh/2:.1f},{hh/2:.1f} 0 0 1 {x0+ww:.1f},{y0+hh:.1f} Z" fill="{f}" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{ww:.1f}" height="{hh:.1f}" fill="none" stroke="{INK}" stroke-width="3"/>')
    o.append(T(x0+ww/2,y0+hh/2-4,'บ่อน้ำ',22,fill=NAVY)+T(x0+ww/2,y0+hh/2+22,f'{w} × {h}',20,fill=NAVY))
    return SV(W,H,''.join(o))
# ---------- trapezoid ----------
def trap(acute,obt):
    o=['<polygon points="90,170 330,170 280,60 140,60" fill="#CFE0F6" stroke="#10244a" stroke-width="3" stroke-linejoin="round"/>']
    o.append(T(75,166,'',1))
    o.append(T(128,158,f'{acute}°' if acute else 'x',22,fill=NAVY));o.append(T(296,158,f'{acute}°' if acute else 'x',22,fill=NAVY))
    o.append(T(160,100,f'{obt}°' if obt else '',22,fill=NAVY));o.append(T(262,100,f'{obt}°' if obt else '',22,fill=NAVY))
    o.append('<text x="215" y="50" font-size="18" text-anchor="middle" fill="#2F5FA8" font-family="Mali" font-weight="700">ด้านขนาน</text><text x="210" y="198" font-size="18" text-anchor="middle" fill="#2F5FA8" font-family="Mali" font-weight="700">ด้านขนาน</text>')
    return SV(420,210,''.join(o))
# ---------- clocks ----------
def clock(h,m,cx,cy,r=80,show=True):
    ha=(h%12)*30+m*0.5;ma=m*6
    o=[f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{NAVY}" stroke-width="4"/>']
    for k in range(12):
        a=math.radians(k*30-90);o.append(f'<line x1="{cx+r*.86*math.cos(a):.1f}" y1="{cy+r*.86*math.sin(a):.1f}" x2="{cx+r*.95*math.cos(a):.1f}" y2="{cy+r*.95*math.sin(a):.1f}" stroke="{NAVY}" stroke-width="3"/>')
        if k%3==0: o.append(T(cx+r*.72*math.cos(a),cy+r*.72*math.sin(a)+6,12 if k==0 else k//3*3 if False else (k if k else 12),17,fill=NAVY))
    def hand(ang,l,w,c):
        a=math.radians(ang-90);return f'<line x1="{cx}" y1="{cy}" x2="{cx+l*math.cos(a):.1f}" y2="{cy+l*math.sin(a):.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
    o.append(hand(ha,r*.5,7,NAVY));o.append(hand(ma,r*.78,4,'#4A86D8'))
    o.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{NAVY}"/>')
    d=abs(ha-ma)%360;ang=min(d,360-d)
    if show:
        a1,a2=sorted([ha,ma]) if d<=180 else sorted([ha,ma],reverse=True)
        # arc from smaller-angle hand to other via short way
        s=ha;e=ma
        diff=(e-s+540)%360-180   # signed shortest
        a_s=math.radians(s-90);a_e=math.radians(s+diff-90);rr=r*.36
        sweep=1 if diff>0 else 0
        o.append(f'<path d="M{cx+rr*math.cos(a_s):.1f},{cy+rr*math.sin(a_s):.1f} A{rr},{rr} 0 0 {sweep} {cx+rr*math.cos(a_e):.1f},{cy+rr*math.sin(a_e):.1f}" fill="none" stroke="#C9A24A" stroke-width="5"/>')
    return ''.join(o),ang,ha,ma
def clocks(t1,t2):
    c1,a1,_,_=clock(*t1,110,115);c2,a2,_,_=clock(*t2,350,115)
    o=c1+c2+T(110,226,f'{t1[0]:02d}.{t1[1]:02d} น. → {a1:g}°',20,fill=NAVY)+T(350,226,f'{t2[0]:02d}.{t2[1]:02d} น. → {a2:g}°',20,fill=NAVY)
    return SV(460,245,o),a1,a2
if __name__=='__main__':
    open('figtest.html','w').write('<!doctype html><meta charset=utf-8><style>svg{width:300px;border:1px solid #ccc;margin:4px}</style>'+bars([80,100,110,40],120,20,True)+gridpat(20,['TL','BR'],['TL','BR'],['R','B','L','T'])[0]+circles([8,6,4,2],['#8393AD','#fff','#8393AD','#fff'])+garden(7,7,'TBLR')+trap(60,120)+clocks((17,15),(7,5))[0])
