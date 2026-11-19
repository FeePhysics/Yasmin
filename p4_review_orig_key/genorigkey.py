import re
src=open('/home/user/Yasmin/p4_review/genreview.py').read()
head=src[:src.index('rnd=random.Random')]
tail=src[src.index("css=ns['css']"):]
code=head+'''
NEW=[]
for i,e in enumerate(ORIG):
    sd=parse(e); var,sv,cs=solve(sd)
    a=-sum(s*c for s,c in cs)*sv
    sols=[x for x in range(1,10000) if val(sd[0],var,x)==val(sd[1],var,x)]
    assert sols==[a],(e,sols)
    t=sorted([(-s*sv,c) for s,c in cs],key=lambda z:-z[0])
    expr=''.join((f'{c}' if k==0 else f' {"+" if s>0 else "−"} {c}') for k,(s,c) in enumerate(t))
    assert eval(expr.replace('−','-'))==a
    NEW.append((e,var,a,f'{var} = {expr}'))
'''+tail
code=code.replace("open('review.html','w').write(w(out));open('reviewkey.html','w').write(w(key))","open('origkey.html','w').write(w(key))")
code=code.replace('header("เฉลย")','header("เฉลย")')
exec(code,{})
