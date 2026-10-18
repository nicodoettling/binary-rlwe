from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import json, random, hashlib, time

cfg=json.loads(Path('finite-controls-input-v1.json').read_text())
started=time.monotonic()
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def av(A,x,q): return tuple(dot(row,x)%q for row in A)
def det(A):
    if len(A)==1: return A[0][0]
    return sum((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A)))
def nearest(x): return (x.numerator*2+x.denominator)//(2*x.denominator)
def gs(b):
    star=[]; mu=[[F(0) for _ in b] for _ in b]
    for i,row in enumerate(b):
        v=list(map(F,row))
        for j,old in enumerate(star):
            mu[i][j]=F(dot(row,old),dot(old,old))
            v=[x-mu[i][j]*y for x,y in zip(v,old)]
        star.append(v)
    return star,mu
def lll(b):
    b=[row[:] for row in b]; k=1; iterations=0
    while k<len(b):
        iterations+=1
        assert iterations<10000
        for j in range(k-1,-1,-1):
            star,mu=gs(b); z=nearest(mu[k][j])
            b[k]=[a-z*c for a,c in zip(b[k],b[j])]
        star,mu=gs(b)
        if dot(star[k],star[k]) >= (F(3,4)-mu[k][k-1]**2)*dot(star[k-1],star[k-1]): k+=1
        else:
            b[k],b[k-1]=b[k-1],b[k]; k=max(1,k-1)
    star,mu=gs(b)
    assert all(abs(mu[i][j])<=F(1,2) for i in range(len(b)) for j in range(i))
    return b
def babai(b,v):
    star,_=gs(b); residual=list(map(F,v)); w=[0]*len(v)
    for i in range(len(b)-1,-1,-1):
        z=nearest(F(dot(residual,star[i]),dot(star[i],star[i])))
        residual=[x-z*y for x,y in zip(residual,b[i])]
        w=[x+z*y for x,y in zip(w,b[i])]
    return [int(F(x)-y) for x,y in zip(v,w)]
def normalize(A,q):
    r=len(A); D=len(A[0]); M=[row[:] for row in A]; transform=[[int(i==j) for j in range(r)] for i in range(r)]
    piv=[]; row=0
    for col in range(D):
        p=next((i for i in range(row,r) if M[i][col]%q),None)
        if p is None: continue
        M[row],M[p]=M[p],M[row]; transform[row],transform[p]=transform[p],transform[row]
        inv=pow(M[row][col],-1,q)
        M[row]=[x*inv%q for x in M[row]]; transform[row]=[x*inv%q for x in transform[row]]
        for i in range(r):
            if i==row: continue
            z=M[i][col]
            M[i]=[(x-z*y)%q for x,y in zip(M[i],M[row])]
            transform[i]=[(x-z*y)%q for x,y in zip(transform[i],transform[row])]
        piv.append(col); row+=1
        if row==r: break
    if row<r: return None
    order=piv+[i for i in range(D) if i not in piv]
    C=[[M[i][j] for j in order[r:]] for i in range(r)]
    columns=[]
    for j in range(r): columns.append([q*int(i==j) for i in range(r)]+[0]*(D-r))
    for j in range(D-r): columns.append([-C[i][j] for i in range(r)]+[int(i==j) for i in range(D-r)])
    return order,transform,columns

print('INPUT_SHA256',hashlib.sha256(Path('finite-controls-input-v1.json').read_bytes()).hexdigest())
for q,r,D,B in cfg['collision_cases']:
    box=list(product(range(-B,B+1),repeat=D)); H=len(box); total=q**(r*D)
    chi=F(0); missing=F(0); rankfail=0
    for entries in product(range(q),repeat=r*D):
        A=[list(entries[i*D:(i+1)*D]) for i in range(r)]
        counts=Counter(av(A,x,q) for x in box)
        chi+=F(q**r*sum(c*c for c in counts.values()),H*H)-1
        missing+=F(q**r-len(counts),q**r)
        rankfail+=normalize(A,q) is None
    chi/=total; missing/=total
    expected=F(q**r-1,H)
    assert chi==expected
    assert 4*missing**2<=expected
    expected_rank=1
    for i in range(r): expected_rank*=1-F(q**i,q**D)
    assert F(rankfail,total)==1-expected_rank
    print('COLLISION',json.dumps({'q':q,'r':r,'D':D,'B':B,'matrices':total,'E_chi2':str(chi),'expected':str(expected),'E_missing_mass':str(missing),'rank_failure':str(F(rankfail,total))},sort_keys=True))

p=cfg['nearest_plane']; q,r,D,B=p['q'],p['r'],p['D'],p['box_B']
rng=random.Random(cfg['seed']); cases=0; total_targets=0; max_ratio=F(0)
while cases<p['matrices']:
    A=[[rng.randrange(q) for _ in range(D)] for _ in range(r)]
    setup=normalize(A,q)
    if setup is None: continue
    order,T,basis=setup
    assert abs(det(basis))==q**r
    reduced=lll(basis)
    assert abs(det(reduced))==q**r
    closest={}; box_image=set()
    for x in product(range(-(q//2),q//2+1),repeat=D):
        y=av(A,x,q); norm=dot(x,x)
        closest[y]=min(closest.get(y,norm),norm)
        if max(map(abs,x))<=B: box_image.add(y)
    local_ratio=F(0); certified=0
    for y in product(range(q),repeat=r):
        ty=av(T,y,q); v=[t if t<=q//2 else t-q for t in ty]+[0]*(D-r)
        xp=babai(reduced,v); x=[0]*D
        for i,j in enumerate(order): x[j]=xp[i]
        assert av(A,x,q)==y
        norm=dot(x,x); opt=closest[y]
        assert norm <= 2**D*opt
        if opt: local_ratio=max(local_ratio,F(norm,opt))
        if y in box_image: assert norm<=2**D*D*B*B
        certified += norm<=2**D*D*B*B
        total_targets+=1
    max_ratio=max(max_ratio,local_ratio); cases+=1
    print('BABAI',json.dumps({'case':cases,'A':A,'det':q**r,'max_squared_ratio':str(local_ratio),'certified_targets':certified,'targets':q**r},sort_keys=True))

neg=lll([[101,0],[0,1]]); residual=babai(neg,[50,0])
assert dot(residual,residual)==2500>101
print('DETERMINANT_ONLY_NEGATIVE',json.dumps({'det':101,'target':[50,0],'Babai_residual':residual,'closest_squared_norm':2500,'det_root_squared':101},sort_keys=True))

q=5; shifts=[(3,1),(4,2)]; outputs=Counter()
for b1 in product(range(q),repeat=2):
    for b2 in product(range(q),repeat=2):
        outputs[tuple((b1[t]-shifts[0][t])%q for t in range(2))+tuple((b2[t]-shifts[1][t])%q for t in range(2))]+=1
assert len(outputs)==q**4 and set(outputs.values())=={1}
center=lambda a: a if a<=q//2 else a-q
accepted=sum(all(abs(center(a))<=1 for a in x) for x in product(range(q),repeat=2))
assert F(accepted,q*q)==F(9,25)
print('COMPARATOR',json.dumps({'conditioned_auxiliary_response_shifts':shifts,'designated_tuples':q**4,'distinct_outputs':len(outputs),'each_multiplicity':1,'single_output_box_probability':str(F(accepted,q*q))},sort_keys=True))
print('SUMMARY',json.dumps({'all_assertions_passed':True,'Babai_cases':cases,'Babai_targets':total_targets,'max_squared_approximation_ratio':str(max_ratio),'certified_squared_factor':2**D,'elapsed_seconds':time.monotonic()-started,'scope':'finite controls, not theorem certification'},sort_keys=True))
