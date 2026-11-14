import numpy as np, random, itertools
from PIL import Image, ImageDraw
def render(vox):
    cx=22;cy=cx*0.58;ch=cx*1.2
    cubes=sorted(vox,key=lambda v:(-(v[0]+v[1]),v[2]))
    S=2;minx=-3*cx-cx;maxx=3*cx+cx;miny=-(4*cy*2)-3*ch-2*cy;maxy=10
    w=int((maxx-minx)*S);h=int((maxy-miny)*S)
    im=Image.new('L',(w,h),255);d=ImageDraw.Draw(im)
    X=lambda v:(v-minx)*S;Y=lambda v:(v-miny)*S
    for a_,b,z in cubes:
        x=(b-a_)*cx;y=-(a_+b)*cy-z*ch
        d.polygon([(X(x),Y(y-ch)),(X(x-cx),Y(y-ch-cy)),(X(x),Y(y-ch-2*cy)),(X(x+cx),Y(y-ch-cy))],fill=200,outline=0)
        d.polygon([(X(x),Y(y)),(X(x-cx),Y(y-cy)),(X(x-cx),Y(y-cy-ch)),(X(x),Y(y-ch))],fill=100,outline=0)
        d.polygon([(X(x),Y(y)),(X(x+cx),Y(y-cy)),(X(x+cx),Y(y-cy-ch)),(X(x),Y(y-ch))],fill=155,outline=0)
    return np.array(im)
def all_required(vox):
    base=render(vox)
    return all(not np.array_equal(render(vox-{v}),base) for v in vox)
def hm_to_vox(h):
    return {(a,b,z) for a in range(3) for b in range(3) for z in range(h[a][b])}
if __name__=='__main__':
    random.seed(7);found=[]
    for _ in range(4000):
        h=[[random.randint(0,3) for _ in range(3)] for _ in range(3)]
        v=hm_to_vox(h)
        if 10<=len(v)<=17 and all_required(v) and max(max(r) for r in h)==3 and h[0][0]>0:
            found.append((len(v),h))
        if len(found)>=30: break
    for n,h in found: print(n,h)
