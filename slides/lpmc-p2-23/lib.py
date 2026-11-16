import math, html
from fractions import Fraction as F
fmt=lambda n:f"{n:,}"
def fr(a,b): return f'<span class="fr"><i>{a}</i><i>{b}</i></span>'
def mix(w,a,b): return f'{w}{fr(a,b)}'
DOTS='<span class="dots">· · ·</span>'
NW=lambda t:f"<span class='nw'>{t}</span>"
# ---------- pie ----------
def pie_svg(slices,right_angle=None,w=520,h=380,title=None):
    cx,cy,r=w/2,h/2+34,118
    out=[f'<svg viewBox="0 0 {w} {h}" class="img">']
    a0=-90.0
    for name,pct,col,show in slices:
        a1=a0+pct*3.6
        x0,y0=cx+r*math.cos(math.radians(a0)),cy+r*math.sin(math.radians(a0))
        x1,y1=cx+r*math.cos(math.radians(a1)),cy+r*math.sin(math.radians(a1))
        large=1 if pct>50 else 0
        out.append(f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f} Z" fill="{col}" stroke="#fff" stroke-width="2.5"/>')
        if show:
            am=math.radians((a0+a1)/2)
            lx,ly=cx+(r+30)*math.cos(am),cy+(r+26)*math.sin(am)
            anchor='start' if math.cos(am)>0.2 else ('end' if math.cos(am)<-0.2 else 'middle')
            out.append(f'<text x="{lx:.1f}" y="{ly+5:.1f}" text-anchor="{anchor}" class="pl">{pct}%</text>')
        a0=a1
    if right_angle:
        s=18
        out.append(f'<path d="M{cx+s},{cy} L{cx+s},{cy-s} L{cx},{cy-s}" fill="none" stroke="#7a4a1e" stroke-width="2.5"/>')
    items=list(slices);rows=[items[:3],items[3:]]
    for ri,row in enumerate(rows):
        widths=[24+len(n)*16+30 for n,_,_,_ in row];tot=sum(widths)-30;lx=(w-tot)/2
        for (name,pct,col,show),wd in zip(row,widths):
            out.append(f'<rect x="{lx:.0f}" y="{10+ri*32}" width="20" height="20" fill="{col}"/><text x="{lx+27:.0f}" y="{27+ri*32}" class="lg">{html.escape(name)}</text>')
            lx+=wd
    out.append('</svg>')
    return ''.join(out)
# ---------- icons ----------
def icon(kind,size=34,col=None):
    s=size
    if kind=='sun':
        rays=''.join(f'<line x1="20" y1="20" x2="{20+17*math.cos(math.radians(a)):.1f}" y2="{20+17*math.sin(math.radians(a)):.1f}" stroke="#f0a500" stroke-width="3" stroke-linecap="round"/>' for a in range(0,360,45))
        return f'<svg class="ic" width="{s}" height="{s}" viewBox="0 0 40 40">{rays}<circle cx="20" cy="20" r="9" fill="#ffd23f" stroke="#e09b00" stroke-width="2"/></svg>'
    if kind=='moon':
        return f'<svg class="ic" width="{s}" height="{s}" viewBox="0 0 40 40"><path d="M27 5 A16 16 0 1 0 35 27 A13 13 0 0 1 27 5Z" fill="#ffd23f" stroke="#e09b00" stroke-width="2" stroke-linejoin="round"/></svg>'
    if kind=='star':
        pts=' '.join(f'{20+17*(1 if i%2==0 else .45)*math.cos(math.radians(-90+36*i)):.1f},{20+17*(1 if i%2==0 else .45)*math.sin(math.radians(-90+36*i)):.1f}' for i in range(10))
        return f'<svg class="ic" width="{s}" height="{s}" viewBox="0 0 40 40"><polygon points="{pts}" fill="#ffd23f" stroke="#e09b00" stroke-width="2" stroke-linejoin="round"/></svg>'
    if kind=='circle': return f'<svg class="ic" width="{s}" height="{s}" viewBox="0 0 40 40"><circle cx="20" cy="20" r="15" fill="#6CBF6A" stroke="#7a4a1e" stroke-width="2.5"/></svg>'
    if kind=='tri': return f'<svg class="ic" width="{s}" height="{s}" viewBox="0 0 40 40"><polygon points="20,5 36,34 4,34" fill="#FFC93C" stroke="#7a4a1e" stroke-width="2.5" stroke-linejoin="round"/></svg>'
    if kind=='square': return f'<svg class="ic" width="{s}" height="{s}" viewBox="0 0 40 40"><rect x="6" y="6" width="28" height="28" rx="3" fill="#F28C28" stroke="#7a4a1e" stroke-width="2.5"/></svg>'
# ---------- isometric voxels ----------
def iso_svg(vox,hl=(),cx=22,w=None,h=None,pad=10):
    cy=cx*0.58; ch=cx*1.2
    cubes=sorted(vox|set(hl),key=lambda v:(-(v[0]+v[1]),v[2]))
    pts=[]
    def anchor(a,b,z): return ((b-a)*cx,-(a+b)*cy-z*ch)
    allp=[anchor(*v) for v in cubes]
    minx=min(p[0] for p in allp)-cx-pad; maxx=max(p[0] for p in allp)+cx+pad
    miny=min(p[1] for p in allp)-ch-2*cy-pad; maxy=max(p[1] for p in allp)+pad
    out=[f'<svg class="img" viewBox="{minx:.0f} {miny:.0f} {maxx-minx:.0f} {maxy-miny:.0f}">']
    for v in cubes:
        x,y=anchor(*v); new=v in hl and v not in vox
        top,left,right=('#ffe27a','#f2b705','#f7cb3a') if new else ('#c9c9c9','#6c6c6c','#9b9b9b')
        out.append(f'<polygon points="{x},{y-ch} {x-cx},{y-ch-cy} {x},{y-ch-2*cy} {x+cx},{y-ch-cy}" fill="{top}" stroke="#111" stroke-width="2" stroke-linejoin="round"/>')
        out.append(f'<polygon points="{x},{y} {x-cx},{y-cy} {x-cx},{y-cy-ch} {x},{y-ch}" fill="{left}" stroke="#111" stroke-width="2" stroke-linejoin="round"/>')
        out.append(f'<polygon points="{x},{y} {x+cx},{y-cy} {x+cx},{y-cy-ch} {x},{y-ch}" fill="{right}" stroke="#111" stroke-width="2" stroke-linejoin="round"/>')
    out.append('</svg>')
    return ''.join(out)
# ---------- grid polygon ----------
def grid_svg(poly,xr,yr,u=26,shade=True,mark=()):
    x0,x1=xr;y0,y1=yr
    W=(x1-x0)*u+60;H=(y1-y0)*u+40
    X=lambda x:30+(x-x0)*u; Y=lambda y:15+(y1-y)*u
    o=[f'<svg class="img" viewBox="0 0 {W} {H}">']
    for x in range(x0,x1+1): o.append(f'<line x1="{X(x)}" y1="{Y(y0)}" x2="{X(x)}" y2="{Y(y1)}" stroke="#EBD9B4" stroke-width="1"/>')
    for y in range(y0,y1+1): o.append(f'<line x1="{X(x0)}" y1="{Y(y)}" x2="{X(x1)}" y2="{Y(y)}" stroke="#EBD9B4" stroke-width="1"/>')
    o.append(f'<line x1="{X(x0)}" y1="{Y(0)}" x2="{X(x1)}" y2="{Y(0)}" stroke="#8a6a45" stroke-width="1.6"/><line x1="{X(0)}" y1="{Y(y0)}" x2="{X(0)}" y2="{Y(y1)}" stroke="#8a6a45" stroke-width="1.6"/>')
    for x in range(x0,x1+1):
        if x!=0: o.append(f'<text x="{X(x)}" y="{Y(0)+14}" text-anchor="middle" class="gt">{x}</text>')
    for y in range(y0,y1+1):
        if y!=0: o.append(f'<text x="{X(0)-6}" y="{Y(y)+4}" text-anchor="end" class="gt">{y}</text>')
    pts=' '.join(f'{X(a)},{Y(b)}' for a,b in poly)
    o.append(f'<polygon points="{pts}" fill="{"rgba(245,184,0,.28)" if shade else "none"}" stroke="#111" stroke-width="3" stroke-linejoin="round"/>')
    for (a,b,t) in mark: o.append(f'<text x="{X(a)+6}" y="{Y(b)-6}" class="gt2">{t}</text>')
    o.append('</svg>');return ''.join(o)
# ---------- rows (queue) ----------
def rows_svg(n,p,mid,hi_back=True,labels=True):
    r=10;gap=26;W=n*gap+90;H=150
    o=[f'<svg class="img" viewBox="0 0 {W} {H}">']
    o.append(f'<text x="6" y="28" class="gt2">แถวหลัง</text><text x="6" y="108" class="gt2">แถวหน้า</text>')
    for i in range(n):
        x=80+i*gap
        col='#FFE9A8'
        if i+1==p: col='#E8794A'
        if i+1==mid: col='#f5b800'
        o.append(f'<circle cx="{x}" cy="30" r="{r}" fill="{col}" stroke="#7a4a1e" stroke-width="2"/>')
        o.append(f'<circle cx="{x}" cy="105" r="{r}" fill="{"#7bd389" if i==0 else "#E4F3D6"}" stroke="#7a4a1e" stroke-width="2"/>')
        if i+1 in (p,mid) or i==0: pass
    o.append(f'<text x="{80+(p-1)*gap}" y="62" text-anchor="middle" class="gt2">โมนา</text><text x="{80+(mid-1)*gap}" y="62" text-anchor="middle" class="gt2">มิกิ</text><text x="80" y="140" text-anchor="middle" class="gt2">มารี</text>')
    o.append('</svg>');return ''.join(o)
# ---------- letters ----------
LET={
'E':[[(0,0),(60,0),(60,16),(18,16),(18,42),(52,42),(52,58),(18,58),(18,84),(60,84),(60,100),(0,100)]],
'L':[[(0,0),(18,0),(18,84),(60,84),(60,100),(0,100)]],
'T':[[(0,0),(60,0),(60,16),(39,16),(39,100),(21,100),(21,16),(0,16)]],
'H':[[(0,0),(18,0),(18,42),(42,42),(42,0),(60,0),(60,100),(42,100),(42,58),(18,58),(18,100),(0,100)]],
'Z':[[(0,0),(60,0),(60,16),(26,84),(60,84),(60,100),(0,100),(0,84),(34,16),(0,16)]],
'N':[[(0,0),(18,0),(42,64),(42,0),(60,0),(60,100),(42,100),(18,36),(18,100),(0,100)]],
'V':[[(0,0),(18,0),(30,66),(42,0),(60,0),(38,100),(22,100)]],
'A':[[(22,0),(38,0),(60,100),(42,100),(38,82),(22,82),(18,100),(0,100)],[(30,28),(36,60),(24,60)]],
'I':[[(0,0),(18,0),(18,100),(0,100)]],
}
def classify(poly):
    n=len(poly)
    area=sum(poly[i][0]*poly[(i+1)%n][1]-poly[(i+1)%n][0]*poly[i][1] for i in range(n))
    sgn=1 if area>0 else -1
    ac=ob=rt=rf=0
    for i in range(n):
        p,c,q=poly[i-1],poly[i],poly[(i+1)%n]
        v1=(p[0]-c[0],p[1]-c[1]);v2=(q[0]-c[0],q[1]-c[1])
        dot=v1[0]*v2[0]+v1[1]*v2[1];cr=v1[0]*v2[1]-v1[1]*v2[0]
        th=math.degrees(math.atan2(abs(cr),dot))
        # turn direction of path p->c->q
        e1=(c[0]-p[0],c[1]-p[1]);e2=(q[0]-c[0],q[1]-c[1])
        turn=e1[0]*e2[1]-e1[1]*e2[0]
        convex=(turn*sgn)>0
        ang=th if convex else 360-th
        if abs(ang-90)<0.6: rt+=1
        elif ang<89.4: ac+=1
        elif ang<180: ob+=1
        else: rf+=1
    return ac,ob,rt,rf
def letters_svg(word,scale=1.6,stroke=3.4):
    gap=22;x=10;parts=[];W=0
    for ch in word:
        polys=LET[ch];wd=max(px for pl in polys for px,_ in pl)
        for pl in polys:
            pts=' '.join(f'{x+px:.1f},{10+py:.1f}' for px,py in pl)
            parts.append(f'<polygon points="{pts}" fill="#fff" stroke="#111" stroke-width="{stroke/scale*1.0:.2f}" stroke-linejoin="round"/>')
        x+=wd+gap
    W=x
    return f'<svg class="img" viewBox="0 0 {W:.0f} 120">{"".join(parts)}</svg>'
def letter_counts(word):
    res=[]
    for ch in word:
        a=o=0
        for pl in LET[ch]:
            ac,ob,_,_=classify(pl);a+=ac;o+=ob
        res.append((ch,a,o))
    return res
if __name__=='__main__':
    for w in 'EALTHZNVI':
        print(w,letter_counts(w))
