"""Independent deterministic finite controls. No claim of infinite certification."""
from fractions import Fraction as F
from collections import defaultdict, Counter
from itertools import product
import json, math, time
start=time.monotonic()
def rnd(x):
    return (2*x.numerator+x.denominator)//(2*x.denominator)
def mul(a,b):
    n=len(a); out=[F(0) for _ in a]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[(i+j)%n]+=x*y*(1 if i+j<n else -1)
    return tuple(out)
def identity(a,s,e,Q,q,rounder=rnd):
    lam=F(q,Q); C=tuple(rounder(lam*x) for x in a)
    de=tuple(F(x)-lam*y for x,y in zip(C,a)); shift=mul(de,s)
    b=tuple(int(x+y)%Q for x,y in zip(mul(a,s),e))
    lhs=tuple(rounder(lam*x)%q for x in b)
    rhs=tuple(int(x+rounder(lam*y-z))%q for x,y,z in zip(mul(C,s),e,shift))
    return lhs,rhs,shift
checks=0; ties=0; witnesses=[]; fibers=[]
for Q,q in [(5,4),(7,4),(8,4),(9,6),(13,6),(13,8),(16,8)]:
    lam=F(q,Q); counts=Counter(rnd(lam*a)%q for a in range(Q))
    tv=sum(abs(F(counts[a],Q)-F(1,q)) for a in range(q))/2
    assert all(counts[a] in (Q//q,(Q+q-1)//q) for a in range(q))
    assert tv<=lam/2
    fibers.append({'Q':Q,'q':q,'counts':dict(counts),'TV':str(tv)})
    for a,s,e in product(product(range(Q),repeat=2),product((0,1),repeat=2),product((-1,0,1),repeat=2)):
        lhs,rhs,shift=identity(a,s,e,Q,q)
        assert lhs==rhs and max(map(abs,shift))<=1
        ties+=sum((lam*x-y).denominator==2 for x,y in zip(e,shift)); checks+=1
for Q,q in [(9,6),(16,8)]:
    for a,s,e in product([(0,1,Q-2,Q-1),(Q-1,)*4,(1,2,3,4)],product((0,1),repeat=4),product((-1,0,1),repeat=4)):
        lhs,rhs,shift=identity(a,s,e,Q,q)
        assert lhs==rhs and max(map(abs,shift))<=2; checks+=1
for Q in range(2,13):
    for q in range(2,Q+1):
        for a,s,e in product(range(Q),(0,1),range(-3,4)):
            lhs,rhs,_=identity((a,),(s,),(e,),Q,q)
            assert lhs==rhs; checks+=1
            if not witnesses:
                l,r,_=identity((a,),(s,),(e,),Q,q,round)
                if l!=r: witnesses.append({'Q':Q,'q':q,'a':a,'s':s,'e':e,'mapped':l,'wrong_even_tie_identity':r})
assert witnesses

# Entire retained (S,A'_1,A'_2,B'_1,B'_2) law at composite target4.
Q,q=7,4; lam=F(q,Q); ep=[(-1,F(1,4)),(0,F(1,2)),(1,F(1,4))]
joint=defaultdict(F); conditional=defaultdict(F)
for s,a1,a2,x,y in product((0,1),range(Q),range(Q),ep,ep):
    mass=F(1,2*Q*Q)*x[1]*y[1]; apr=(rnd(lam*a1)%q,rnd(lam*a2)%q)
    direct=(rnd(lam*((a1*s+x[0])%Q))%q,rnd(lam*((a2*s+y[0])%Q))%q)
    residual=tuple(identity((a,),(s,),(e,),Q,q)[1][0] for a,e in [(a1,x[0]),(a2,y[0])])
    joint[(s,)+apr+direct]+=mass; conditional[(s,)+apr+residual]+=mass
assert joint==conditional and sum(joint.values())==1
# Equal one-sample marginals do not determine a batch's shared-secret law.
shared=defaultdict(F); fresh=defaultdict(F)
for a,b,s in product(range(4),range(4),(0,1)): shared[(a,b,a*s%4,b*s%4)]+=F(1,32)
for a,b,s,t in product(range(4),range(4),(0,1),(0,1)):fresh[(a,b,a*s%4,b*t%4)]+=F(1,64)
tv_shared=sum(abs(shared[k]-fresh[k]) for k in set(shared)|set(fresh))/2
assert tv_shared>0
for pos in (0,1):
    m1=defaultdict(F); m2=defaultdict(F)
    for z,p in shared.items():m1[(z[pos],z[2+pos])]+=p
    for z,p in fresh.items():m2[(z[pos],z[2+pos])]+=p
    assert m1==m2

# CP-1, all five traces times all32 independent binary oracle assignments.
prior=[('A0',F(21,2200)),('A1',F(21,2200)),('C0',F(1,11)),('C1',F(1,11)),('D',F(879,1100))]
atoms=[]; vk=F(0)
for label,mass in prior:
    for h in product((0,1),repeat=5):
        w=mass/32; ok=not label.startswith('C') or h[0]==int(label[-1])
        if ok:atoms.append((label,h,w));vk+=w
assert vk==F(10,11)
post=defaultdict(F)
for label,h,w in atoms:post[label]+=w/vk
assert post=={'A0':F(21,2000),'A1':F(21,2000),'C0':F(1,20),'C1':F(1,20),'D':F(879,1000)}
matched=sum(w/vk for label,h,w in atoms if label.startswith('A') and h[0]==int(label[-1]))
assert matched==F(21,2000)>F(1,100)
inc={'x':post['C0']+post['C1'],'e0':post['A0']+post['C0'],'f0':post['A0']}
assert all(p<=F(1,10) for p in inc.values())
later=(post['A0']/2)/(post['A0']/2+post['C0'])
assert later==F(21,221)<F(1,10)

# Width affects proposal encodings, not K_B,p_B or trial bound Lplus.
ell=7; KB=ell*ell+6; Lplus=40*(ell*ell+6)*(ell*ell+4)
widths=[F(1),F(3,2),F(2**128),F(2**256+1,3)]
width_rows=[]
for width in widths:
    N=math.ceil(width*KB)+1; interval=2*N+1
    width_rows.append({'width_num_bits':width.numerator.bit_length(),'width_den_bits':width.denominator.bit_length(),'proposal_bits':(interval-1).bit_length(),'KB':KB,'Lplus':Lplus})
assert width_rows[-1]['proposal_bits']>250 and len(set(x['Lplus'] for x in width_rows))==1
print(json.dumps({'status':'PASS','identity_cases':checks,'half_integer_coordinates_n2':ties,'composite_public_fibers':fibers,'bankers_tie_counterexample':witnesses[0],'retained_joint_support':len(joint),'shared_versus_fresh_secret_TV':str(tv_shared),'CP1':{'normalizer':str(vk),'posterior':{k:str(v) for k,v in post.items()},'initial_incidence':{k:str(v) for k,v in inc.items()},'two_hits':str(matched),'false_product':'1/100','later_incidence':str(later),'inflated_envelope':'221/2000'},'width_encoding_controls':width_rows,'seconds':time.monotonic()-start},indent=2))
