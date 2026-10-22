import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy import sparse
import itertools,json,math,time,hashlib
from fractions import Fraction as F
P=Path(__file__).resolve().parent;O=P.parent;start=time.monotonic();n=4;N=n+1;G=N**3;NH=N*N
src=O/'workers/FF3/experiments/joint-rank-n4-integer-system-fv17.npz'
z=np.load(src);aa=z['A'];bb=z['b'];q=2**n;NY=q*q
vs=list(itertools.product(range(2),repeat=n));index={v:i for i,v in enumerate(vs)}
def mul(a,b,mod=None):
 out=[0]*n
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[(i+j)%n]+=x*y*(1 if i+j<n else -1)
 return tuple(x%mod for x in out) if mod else tuple(out)
def auto(a,k,mod=None):
 out=[0]*n
 for i,x in enumerate(a):
  j=i*k%(2*n);out[j%n]+=x*(1 if j<n else -1)
 return tuple(x%mod for x in out) if mod else tuple(out)
def mono(j):
 out=[0]*n;j%=2*n;out[j%n]=1 if j<n else -1;return tuple(out)
parent=list(range((q+1)*NY))
def find(i):
 while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
 return i
def join(i,j):
 i=find(i);j=find(j)
 if i!=j:parent[max(i,j)]=min(i,j)
permutations=[]
for k in range(1,2*n,2):
 for j in range(2*n):
  T=mono(j);Ti=mono(-j);Lone=mul(T,auto((1,)*n,k));v=tuple(int(x<0) for x in Lone)
  smap=[]
  for s in vs:
   ls=mul(T,auto(s,k));gs=tuple(x+y for x,y in zip(ls,v));assert gs in index;smap.append(index[gs])
  assert len(set(smap))==q
  ymap=[]
  for c in vs:
   cp=mul(auto(c,k),Ti,2)
   for d in vs:
    dp=tuple((x+y)%2 for x,y in zip(auto(d,k,2),mul(cp,v,2)))
    ymap.append(index[cp]*q+index[dp])
  assert len(set(ymap))==NY
  perm=[]
  for si in range(q+1):
   sp=smap[si] if si<q else q
   for yi in range(NY):
    a=si*NY+yi;b=sp*NY+ymap[yi];join(a,b);perm.append(b)
    assert int(bb[G+a])==int(bb[G+b])
  permutations.append(perm)
assert len(permutations)==2*n*n
orbits={}
for r in range((q+1)*NY):orbits.setdefault(find(r),[]).append(r)
assert all(len(x)<=len(permutations) for x in orbits.values())
# Closure and uniform multiplicity: the explicit group average equals each orbit average.
for r in range((q+1)*NY):
 counts={}
 for perm in permutations:counts[perm[r]]=counts.get(perm[r],0)+1
 assert set(counts)==set(orbits[find(r)]) and len(set(counts.values()))==1
A=[aa[i] for i in range(G)];b=list(map(int,bb[:G]))
for orb in orbits.values():
 assert int(aa[G:].max())*len(orb)<2**63
 A.append(aa[[G+x for x in orb]].sum(axis=0));b.append(int(bb[G+orb[0]])*len(orb))
A=np.array(A,dtype=np.int64);b=np.array(b,dtype=np.int64)
np.savez_compressed(P/'symmetrized-rank-fv1-system.npz',A=A,b=b)
(P/'symmetrized-rank-fv1-orbits.json').write_text(json.dumps(list(orbits.values()))+'\n')
af=sparse.csr_matrix(A.astype(float)/b[:,None]);bf=np.ones(len(b))
rec={'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'n':n,'group_size':len(permutations),'endpoint_orbits':len(orbits),'variables':len(A[0]),'equations':len(b),'exact_group_laws_and_rhs_invariance':True}
print(json.dumps(rec),flush=True)
lp=linprog(np.zeros(A.shape[1]),A_eq=af,b_eq=bf,bounds=(0,None),method='highs',options={'threads':1,'time_limit':35.0,'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
rec.update(LP_status=int(lp.status),LP_message=lp.message,exact_verified=False)
if lp.x is not None:
 np.save(P/'symmetrized-rank-fv1-weights.npy',lp.x);supp=[j for j,x in enumerate(lp.x) if x>1e-9];rec.update(support=len(supp),max_error=float(np.max(np.abs(af@lp.x-1))))
(P/'symmetrized-rank-fv1-summary.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
if lp.success:
 vals=[F(float(x)).limit_denominator(10**12) for x in lp.x]
 ok=all(sum(int(row[j])*vals[j] for j in supp)==int(v) for row,v in zip(A,b))
 if ok:
  rec['exact_verified']=True;(P/'symmetrized-rank-fv1-certificate.json').write_text(json.dumps({'kind':'rational_weights','weights':[[j,str(vals[j])] for j in supp]},indent=2)+'\n')
else:
 dual=linprog(np.ones(len(b)),A_ub=-af.T,b_ub=np.zeros(A.shape[1]),bounds=[(-1,1)]*len(b),method='highs',options={'threads':1,'time_limit':35.0})
 rec['dual_status']=int(dual.status)
 if dual.success:
  D=math.lcm(*map(int,b));rr=np.array([int(round(float(v)*2**48))*(D//int(bi)) for v,bi in zip(dual.x,b)],dtype=object)
  cs=[]
  for j in range(0,A.shape[1],64):cs.extend((A[:,j:j+64].astype(object).T@rr).tolist())
  eta=max(0,-min(cs));rr[:G]+=eta;cs=[]
  for j in range(0,A.shape[1],64):cs.extend((A[:,j:j+64].astype(object).T@rr).tolist())
  bd=sum(int(x)*int(y) for x,y in zip(b,rr));ok=min(cs)>=0 and bd<0
  cert={'kind':'integer_farkas','dual_integer':list(map(str,rr)),'normalizer_safety_shift':str(eta),'min_Atz':str(min(cs)),'b_dot_z':str(bd),'exact_verified':ok}
  (P/'symmetrized-rank-fv1-certificate.json').write_text(json.dumps(cert,indent=2)+'\n');rec.update(exact_verified=ok,min_Atz=str(min(cs)),b_dot_z=str(bd))
rec['seconds']=time.monotonic()-start;(P/'symmetrized-rank-fv1-summary.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
