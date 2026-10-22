#!/usr/bin/env python3
"""Independent exact checks from the authorized statement-only data."""
import itertools as it
import json
from collections import defaultdict, Counter
from fractions import Fraction as F
from pathlib import Path
from math import comb

ROOT=Path(__file__).resolve().parent
checks={}
def vectors(q,n=2): return list(it.product(range(q),repeat=n))
def add(a,b,q): return tuple((x+y)%q for x,y in zip(a,b))
def sub(a,b,q): return tuple((x-y)%q for x,y in zip(a,b))
def mul(a,b,q):
 n=len(a); c=[0]*n
 for i,x in enumerate(a):
  for j,y in enumerate(b): c[(i+j)%n] += x*y*(1 if i+j<n else -1)
 return tuple(x%q for x in c)
def zc(x): return x.count(0)
def tv(a,b): return sum(abs(a.get(k,F(0))-b.get(k,F(0))) for k in a.keys()|b.keys())/2
def law(q,secret,scalar):
 vs=vectors(q); ans={}
 for a,b in it.product(vs,repeat=2):
  r=sub(b,mul(a,secret,q),q); p=F(1,len(vs))
  for x in r:p*=scalar[x]
  ans[(a,b)]=p
 return ans
def push(p,K):
 ans=defaultdict(F)
 for x,px in p.items():
  for y,k in K[x].items(): ans[y]+=px*k
 return dict(ans)

xs=vectors(3); ys=vectors(2); inputs=list(it.product(xs,repeat=2)); outputs=list(it.product(ys,repeat=2))
secrets=ys
edges=[]
for u in secrets:
 for i in range(2):
  if u[i]==0:
   v=list(u);v[i]=1;edges.append((u,tuple(v)))
nu3={x:F(7,8)**zc(x)*F(1,16)**(2-zc(x)) for x in xs}
nu2={y:F(3,4)**zc(y)*F(1,4)**(2-zc(y)) for y in ys}
rad=json.loads((ROOT/'allowed-input/radial-kernel-tables.json').read_text())
Hs=[{x:{y:F(A[zc(x)][zc(y)],rad['entry_denominator']) for y in ys} for x in xs} for A in rad['per_atom_numerators']]
for H in Hs:
 assert all(sum(row.values())==1 and min(row.values())>=0 for row in H.values())
 assert push({x:F(1,9) for x in xs},H)=={y:F(1,4) for y in ys}
 assert push(nu3,H)==nu2
checks['radial']={'kernels':len(Hs),'rows':36,'uniform_and_noise_exact':True}

tab=json.loads((ROOT/'allowed-input/compact-selector-table.json').read_text())
g=defaultdict(dict)
for ci,vi,w in tab['entries']:
 c=tuple(tab['classes'][ci]);v=tuple(tab['variants'][vi]); assert v not in g[c]
 g[c][v]=F(w);assert F(w)>=0
G={c:sum(row.values()) for c,row in g.items()}
K={}
for a,b in inputs:
 row=defaultdict(F);norm=F(0)
 for u,v in edges:
  r0=sub(b,mul(a,u,3),3);r1=sub(b,mul(a,v,3),3);cl=(zc(a),zc(r0),zc(r1))
  norm+=G.get(cl,F(0))
  for (j,k),w in g[cl].items():
   for c,d in outputs:
    t0=sub(d,mul(c,u,2),2);t1=sub(d,mul(c,v,2),2)
    row[(c,d)]+=w*Hs[j][r0][t0]*Hs[k][r1][t1]/4
 assert norm==4 and sum(row.values())==1 and min(row.values())>=0
 K[(a,b)]=dict(row)
for s in secrets:
 assert push(law(3,s,[F(7,8),F(1,16),F(1,16)]),K)==law(2,s,[F(3,4),F(1,4)])
assert push({x:F(1,81) for x in inputs},K)=={y:F(1,16) for y in outputs}
expected=F(31747846170836756094431065767102005668874369915000841877198843,11688058834193179864192788149647847121368047468795377899320297)
assert max(G.values())==expected and expected<3
checks['compact']={'entries':len(tab['entries']),'input_rows':len(K),'all_fixed_secret_endpoints':4,'uniform_exact':True,'max_G':str(expected)}

jt=json.loads((ROOT/'allowed-input/joint-rank-table.json').read_text())
h=defaultdict(dict)
for ix,w in jt['entries']:
 cl,out=divmod(ix,9);za,z=divmod(cl,9);z0,z1=divmod(z,3);w0,w1=divmod(out,3)
 assert (w0,w1) not in h[(za,z0,z1)]
 h[(za,z0,z1)][w0,w1]=F(w); assert F(w)>=0
assert len(h)==27 and all(sum(v.values())==1 for v in h.values())
srcshell={z:[x for x in xs if zc(x)==z] for z in range(3)}
tgtshell={z:[y for y in ys if zc(y)==z] for z in range(3)}
KR={}
for a,b in inputs:
 row=defaultdict(F)
 for u,v in edges:
  r0=sub(b,mul(a,u,3),3);r1=sub(b,mul(a,v,3),3);z0,z1=zc(r0),zc(r1)
  M=len(srcshell[z0])*len(srcshell[z1]);R=srcshell[z0].index(r0)*len(srcshell[z1])+srcshell[z1].index(r1)
  for (w0,w1),prob in h[(zc(a),z0,z1)].items():
   N=len(tgtshell[w0])*len(tgtshell[w1])
   for T in range(N):
    J=(N*R+T)//M;j0,j1=divmod(J,len(tgtshell[w1]));t0=tgtshell[w0][j0];t1=tgtshell[w1][j1]
    matches=[(c,d) for c,d in outputs if sub(d,mul(c,u,2),2)==t0 and sub(d,mul(c,v,2),2)==t1]
    assert len(matches)==1;row[matches[0]]+=prob/(4*N)
 assert sum(row.values())==1
 KR[(a,b)]=dict(row)
for s in secrets:
 assert push(law(3,s,[F(7,8),F(1,16),F(1,16)]),KR)==law(2,s,[F(3,4),F(1,4)])
assert push({x:F(1,81) for x in inputs},KR)=={y:F(1,16) for y in outputs}
checks['joint_rank']={'entries':len(jt['entries']),'class_rows':len(h),'input_rows':len(KR),'all_fixed_secret_endpoints':4,'uniform_exact':True}

for M in range(1,25):
 for N in range(1,25):
  counts=Counter((N*r+t)//M for r in range(M) for t in range(N))
  assert counts=={j:M for j in range(N)}
checks['rank_transport']={'M_and_N_range':[1,24],'exact_pairs':24**2}

twoevents=0
for a in range(1,4):
 u=F(a,4)
 for b in range(1,9):
  p=F(b,8)
  if not u<p:continue
  for j in range(1,16):
   N=[F(j,16),1-F(j,16)];V=[F(1,2)]*2;L=[2*x for x in N]
   if min(L)<(1-p)/(1-u) or max(L)>p/u:continue
   g1=[((1-u)*x-(1-p)*v)/(p-u) for x,v in zip(N,V)]
   g0=[(p*v-u*x)/(p-u) for x,v in zip(N,V)]
   assert min(g1+g0)>=0 and sum(g1)==sum(g0)==1
   assert [p*x+(1-p)*y for x,y in zip(g1,g0)]==N
   assert [u*x+(1-u)*y for x,y in zip(g1,g0)]==V
   if p>=F(3,4) and u<=F(1,4):
    assert (p-u)/(1-u)>=F(2,3) and (p-u)/p>=F(2,3)
   twoevents+=1
checks['twoevent_grid']={'admissible_cases':twoevents,'denominators':[4,8,16]}

twosecret=0
for q in [2,3,4,5]:
 for s0,s1 in it.permutations(range(q),2):
  if __import__('math').gcd(s1-s0,q)!=1:continue
  for t0,t1 in it.permutations(range(q),2):
   if __import__('math').gcd(t1-t0,q)!=1:continue
   for aweight in [F(0),F(1,2),F(1)]:
    H={u:{v:aweight*int(v==u)+(1-aweight)/q for v in range(q)} for u in range(q)}
    nu={x:F(int(x==0)) for x in range(q)};target=H[0]
    for label in [None,0,1]:
     out=defaultdict(F)
     for a,b in it.product(range(q),repeat=2):
      px=F(1,q*q) if label is None else F(int((b-a*[s0,s1][label])%q==0),q)
      for u1,v1 in it.product(range(q),repeat=2):
       c=(u1-v1)*pow((t1-t0)%q,-1,q)%q;d=(u1+c*t0)%q
       out[c,d]+=px*H[(b-a*s0)%q][u1]*H[(b-a*s1)%q][v1]
     expectedlaw={(c,d):(F(1,q*q) if label is None else target[(d-c*[t0,t1][label])%q]/q) for c,d in it.product(range(q),repeat=2)}
     assert out==expectedlaw;twosecret+=1
checks['twosecret']={'endpoint_cases':twosecret,'rings':[2,3,4,5],'H_mixture_weights':['0','1/2','1']}

selectors=0
for cls in it.product(range(2),repeat=4):
 for weights in it.product([F(0),F(1,2),F(1),F(3,2),F(2)],repeat=4):
  M=max(weights)
  if not M:continue
  Q=[[F(0)]*4 for _ in range(2)]
  for x,e in it.product(range(2),repeat=2):
   c=cls[2*x+e];Q[x][2*e+c]=weights[2*e+c]/2
  if any(sum(row)!=1 for row in Q):continue
  for prior0 in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
   prior=[prior0,1-prior0]
   guess=sum(max(prior[s]*Q[s][y] for s in range(2)) for y in range(4))
   assert guess<=min(1,2*M*max(prior))
   assert all(v<=M/2 for row in Q for v in row)
   selectors+=1
checks['compressed_selectors']={'admissible_prior_cases':selectors,'inputs':2,'proposals':2,'classes':2,'exact_density_and_guessing_bounds':True}

# Correlated public information and randomized class: exact accepted law.
publiccases=0
for k in range(5):
 joint={(0,0):F(k,8),(1,0):F(4-k,8),(0,1):F(4-k,8),(1,1):F(k,8)}
 # M=1 and class C=S is allowed, L=2. Random class is a fresh noisy copy.
 for a in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
  guess=F(0)
  for z,c in it.product(range(2),repeat=2):
   guess+=max(joint[s,z]*(a if c==s else 1-a) for s in range(2))
  bound=2*sum(max(joint[s,z] for s in range(2)) for z in range(2))
  assert guess<=bound;publiccases+=1
checks['public_randomclass']={'cases':publiccases,'joint_priors':'correlated S,Z grid','fresh_class_kernel':True}

# ENUM: bounded finite surrogate noise, exact endpoint failure probabilities.
enumcases=0
for q in [7,17]:
 vs=vectors(q);ss=vectors(2);T=1
 noise={e:F(1,2)**zc(e)*F(1,4)**(2-zc(e)) for e in it.product([0,1,q-1],repeat=2)}
 isbox=lambda r:all(min(c,q-c)<=T for c in r)
 beta=F(4*3**2,q*q);eta=F(3*5**2*2,q*q)
 count=0;bad={s:F(0) for s in ss}
 for a,b in it.product(vs,repeat=2):
  survivors=[s for s in ss if isbox(sub(b,mul(a,s,q),q))]
  count+=len(survivors)==1
  for s in ss:
   e=sub(b,mul(a,s,q),q)
   if e in noise and survivors!=[s]:bad[s]+=noise[e]/(q*q)
 assert F(count,q**4)<=beta
 assert all(v<=eta for v in bad.values())
 enumcases+=4
checks['enumeration_surrogate']={'fixed_secret_cases':enumcases,'Q':[7,17],'n':2,'T':1,'finite_noise':'(1/2,1/4,1/4) on 0,+1,-1','finite_model_only':True}

def shift(v):return (-v[-1],)+tuple(v[:-1])
def rmul(a,b):
 n=len(a);out=[0]*n
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[(i+j)%n]+=x*y*(1 if i+j<n else -1)
 return tuple(out)
affinecases=0
for n in [4,8]:
 for delta in [tuple([1]+[0]*(n-1)),tuple([1]*n),tuple([1,-1]+[0]*(n-2))]:
  orbit=[];v=delta
  for _ in range(2*n):orbit.append(v);v=shift(v)
  for center in [F(0),F(1,2),F(1)]:
   laws={}
   for s in vectors(2,n):
    row=defaultdict(F)
    for d in orbit:
     z=rmul([center]*n,d);md=rmul(s,d);w=tuple(x-y for x,y in zip(z,md));row[w]+=F(1,len(orbit))
    laws[s]=dict(row)
   R2=max(sum(x*x for x in w) for row in laws.values() for w in row)
   delta2=sum(x*x for x in delta)
   for Y in [laws[tuple([0]*n)],{tuple([0]*n):F(1)}]:
    tvcube=sum(tv(row,Y) for row in laws.values())/2**n
    assert tvcube>=F(delta2,n**3)/R2
    for w in range(2,n-1):
     subset=[row for s,row in laws.items() if sum(s)==w]
     pw=F(4*w*(w-1)*(n-w)*(n-w-1),n*(n-1)*(n-2)*(n-3))
     assert sum(tv(row,Y) for row in subset)/len(subset)>=4*pw*delta2/(n**3*R2)
    for cut in [R2/4,R2/2,R2]:
     eta=lambda row:sum(prob*sum(x*x for x in v) for v,prob in row.items() if sum(x*x for x in v)>cut)
     rhs=(F(delta2,n**3)-sum(eta(row) for row in laws.values())/2**n-eta(Y))/cut
     assert tvcube>=rhs
    affinecases+=1
checks['bounded_affine']={'law_families':affinecases,'n':[4,8],'cube_and_all_nontrivial_slices':True,'tail_versions':True}

# RS code: independently derive Fourier support and enumerate all codewords.
rs=[]
for n,p,ts in [(4,17,[1,2,3]),(8,17,[1,2])]:
 alpha=next(a for a in range(1,p) if pow(a,n,p)==p-1)
 for t in ts:
  distance=n
  for coeff in it.product(range(p),repeat=t):
   vec=[]
   for k in range(n):
    xx=pow(alpha,-2*k,p)
    val=sum(c*pow(xx,j,p) for j,c in enumerate(coeff))%p
    vec.append(val*pow(alpha,-k,p)%p)
   if any(coeff):distance=min(distance,sum(x!=0 for x in vec))
   for j in range(t,n):
    assert sum(vec[k]*pow(alpha,(2*j+1)*k,p) for k in range(n))%p==0
  assert distance==n-t+1
  rs.append({'n':n,'p':p,'t':t,'minimum_distance':distance,'codewords':p**t})
checks['rs_codes']=rs

# CP-1 negative control: the forbidden marginal product must be rejected.
A=F(21,2200);C=F(1,11);D=F(879,1100)
vk=2*A+C+D
assert vk==F(10,11)
apost=A/vk;cpost=C/(2*vk);dpost=D/vk
assert (apost,cpost,dpost)==(F(21,2000),F(1,20),F(879,1000))
assert 2*cpost==F(1,10) and apost+cpost==F(121,2000)
event=2*apost/2;conditional=apost/(apost+2*cpost)
assert event==F(21,2000)>F(1,100)
assert conditional==F(21,221)<F(1,10)
checks['CP1']={'posterior_A_each':str(apost),'posterior_C_each':str(cpost),'posterior_D':str(dpost),'event':str(event),'forbidden_product':'1/100','residual_after_hit':str(conditional),'old_product_claim_rejected':True,'cause':'support restriction and posterior renormalization'}

print(json.dumps({'status':'ALL_EXACT_CHECKS_PASSED','checks':checks},indent=2))
