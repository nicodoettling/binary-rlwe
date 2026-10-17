from fractions import Fraction as Q
from itertools import product, combinations
from math import cos, sin, pi, exp, comb, log2
import json, resource, time
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
t0=time.monotonic()

def add(a,b,q): return tuple((x+y)%q for x,y in zip(a,b))
def dot(a,b,q): return sum(x*y for x,y in zip(a,b))%q

def invmat(M,q):
 n=len(M); A=[list(r)+[int(i==j) for j in range(n)] for i,r in enumerate(M)]
 for i in range(n):
  k=next(k for k in range(i,n) if A[k][i]%q); A[i],A[k]=A[k],A[i]
  z=pow(A[i][i],-1,q); A[i]=[(x*z)%q for x in A[i]]
  for j in range(n):
   if j!=i:
    z=A[j][i]; A[j]=[(x-z*y)%q for x,y in zip(A[j],A[i])]
 return [r[n:] for r in A]

def mul(M,x,q): return tuple(dot(r,x,q) for r in M)
def histchar(P,v,q):
 h=[Q(0)]*q
 for x,p in P.items(): h[dot(v,x,q)]+=p
 return h

def conv(a,b,q):
 c=[Q(0)]*q
 for i,x in enumerate(a):
  for j,y in enumerate(b): c[(i+j)%q]+=x*y
 return c

def ev(h,q): return sum(float(x)*complex(cos(2*pi*i/q),sin(2*pi*i/q)) for i,x in enumerate(h))
def char_equal(a,b):
 # The only rational relation among powers of a primitive prime-q root is all-ones.
 d=[x-y for x,y in zip(a,b)]; return len(set(d))==1

def setup(n,q,d,noise):
 roots=[r for r in range(q) if pow(r,n,q)==q-1]; assert len(roots)==n
 V=[[pow(r,k,q) for k in range(n)] for r in roots]; W=invmat(V,q)
 NP={}
 for vals in product(noise,repeat=n):
  z=tuple(x%q for x in vals); p=Q(1)
  for x in vals:p*=noise[x]
  NP[z]=NP.get(z,Q(0))+p
 Ts=list(combinations(range(n),d)); Is=[]; Ps=[]
 for T in Ts:
  I={}
  for vals in product(range(q),repeat=d):
   z=[0]*n
   for i,x in zip(T,vals):z[i]=x
   u=mul(W,z,q); I[u]=I.get(u,Q(0))+Q(1,q**d)
  P={}
  for u,p in I.items():
   for f,z in NP.items():
    a=add(u,f,q); P[a]=P.get(a,Q(0))+p*z
  assert sum(P.values())==1 and len(I)==q**d
  Is.append(I);Ps.append(P)
 return roots,V,W,NP,Ts,Is,Ps

noise={-1:Q(1,4),0:Q(1,2),1:Q(1,4)}
rows=[]
for n,q,d in [(2,5,1),(4,17,1),(4,17,2)]:
 roots,V,W,NP,Ts,Is,Ps=setup(n,q,d,noise)
 freqs=list(product(range(q),repeat=n)) if n==2 else [tuple(int(i==j) for i in range(n)) for j in range(n)]
 if n==4:
  # Deliberately include sparse CRT-dual frequencies, unlike coefficient axes.
  for a in [(1,0,0,0),(0,1,0,0),(1,1,0,0),(1,0,1,0),(0,0,0,0)]:
   freqs.append(tuple(sum(V[i][j]*a[i] for i in range(n))%q for j in range(n)))
 H={v:histchar(NP,v,q) for v in freqs}
 zs={v:{i for i in range(n) if sum(W[j][i]*v[j] for j in range(n))%q==0} for v in freqs}
 def prob(Z):return Q(comb(len(Z),d),comb(n,d)) if len(Z)>=d else Q(0)
 checks=0; gaps=[]; maxsingle=0; maxpair=0
 for v in freqs:
  obs=[Q(0)]*q
  for P in Ps:
   h=histchar(P,v,q)
   obs=[x+y/len(Ts) for x,y in zip(obs,h)]
  assert char_equal(obs,[x*prob(zs[v]) for x in H[v]])
  if any(v): maxsingle=max(maxsingle,abs(ev(obs,q)))
  for w in freqs:
   actual=[Q(0)]*q
   indep=[Q(0)]*q
   for It in Is:
    # Includes all q^d ideal points, in particular zero active values.
    iv=histchar(It,v,q); iw=histchar(It,w,q)
    ht=conv(conv(iv,iw,q),conv(H[v],H[w],q),q)
    actual=[x+y/len(Ts) for x,y in zip(actual,ht)]
   pred=[x*prob(zs[v]&zs[w]) for x in conv(H[v],H[w],q)]
   assert char_equal(actual,pred)
   # Independent T expectation computes each marginal separately.
   av=[Q(0)]*q; aw=[Q(0)]*q
   for It in Is:
    iv=histchar(It,v,q); iw=histchar(It,w,q)
    av=[x+y/len(Ts) for x,y in zip(av,iv)]; aw=[x+y/len(Ts) for x,y in zip(aw,iw)]
   indep=conv(conv(av,aw,q),conv(H[v],H[w],q),q)
   expected_ind=[x*prob(zs[v])*prob(zs[w]) for x in conv(H[v],H[w],q)]
   assert char_equal(indep,expected_ind)
   if any(v) or any(w): maxpair=max(maxpair,abs(ev(actual,q)))
   if v==w and 0<prob(zs[v])<1:
    gap=abs(ev(actual,q)-ev(indep,q));gaps.append(gap)
   checks+=1
 assert maxpair <= maxsingle+1e-12
 row={'n':n,'q':q,'d':d,'roots':roots,'supports':len(Ts),'ideal_values_per_support':q**d,'frequencies':len(freqs),'exact_pair_moment_checks':checks,'max_marginal_character_abs_float':maxsingle,'max_pair_character_abs_float':maxpair,'same_T_vs_redrawn_diagonal_gaps_float':gaps}
 if n==2:
  states=list(product(range(q),repeat=n)); mean={x:sum(P.get(x,Q(0)) for P in Ps)/len(Ps) for x in states}
  tv1=sum(abs(mean[x]-Q(1,q**n)) for x in states)/2
  tv2=Q(0);tvcorr=Q(0)
  for x in states:
   for y in states:
    p=sum(P.get(x,Q(0))*P.get(y,Q(0)) for P in Ps)/len(Ps)
    tv2+=abs(p-Q(1,q**(2*n)))/2
    tvcorr+=abs(p-mean[x]*mean[y])/2
  row.update(marginal_TV_exact=str(tv1),pair_TV_exact=str(tv2),same_T_vs_redrawn_TV_exact=str(tvcorr))
 rows.append(row)
# Exact source diagnostic: coefficient D_ell, n=2, ell=1. The sole approximation is Gaussian truncation/floating arithmetic.
n=2;q=5;d=1;ell=1;B=6
weights={z:exp(-pi*z*z) for z in range(-B,B+1)};norm=sum(weights.values());gn={z:w/norm for z,w in weights.items()}
# Convert binary floating masses to rationals for exact subsequent enumeration; this does not certify rounding error.
gnr={z:Q.from_float(w) for z,w in gn.items()};s=sum(gnr.values());gnr={z:w/s for z,w in gnr.items()}
roots,V,W,NP,Ts,Is,Ps=setup(n,q,d,gnr)
v=tuple(V[0]);h=histchar(NP,v,q);psi=ev(h,q).real;p=Q(1,2)
g={'n':n,'q':q,'d':d,'ell':ell,'radius':B,'tail_bound_for_all_2n_coefficients':2*n*exp(-pi*B*B)/(pi*B),'frequency_v':v,'psi_float':psi,'marginal_character_bias_float':psi/2,'joint_diagonal_character_bias_float':psi*psi/2,'same_vs_redrawn_character_gap_float':psi*psi/4,'uniform_character_acceptance':0.5,'same_T_character_acceptance_float':(1+psi*psi/2)/2,'redrawn_T_character_acceptance_float':(1+psi*psi/4)/2,'qualification':'Tail bound rigorous by Gaussian integral and Z_ell>=ell; decimal computations diagnostic, binary floating rounding unbounded.'}
print(json.dumps({'status':'PROVISIONAL','seed':None,'noise_for_exact_checks':'iid coefficient rational {-1:1/4,0:1/2,1:1/4}; not asserted Gaussian','exact_controls':rows,'exact_Gaussian_diagnostic':g,'elapsed_seconds':time.monotonic()-t0},indent=2))
