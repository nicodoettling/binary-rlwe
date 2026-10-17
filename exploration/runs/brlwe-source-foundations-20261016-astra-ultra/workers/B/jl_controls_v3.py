from fractions import Fraction as Q
from itertools import product, combinations
from math import comb, exp, pi
import json, resource, time
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
t0=time.monotonic()

def invmat(M,q):
 n=len(M);A=[list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(M)]
 for i in range(n):
  z=next(j for j in range(i,n) if A[j][i]%q);A[i],A[z]=A[z],A[i]
  z=pow(A[i][i],-1,q);A[i]=[x*z%q for x in A[i]]
  for j in range(n):
   if j!=i:
    z=A[j][i];A[j]=[(x-z*y)%q for x,y in zip(A[j],A[i])]
 return [row[n:] for row in A]
def matvec(M,v,q):return tuple(sum(a*b for a,b in zip(row,v))%q for row in M)
def roots(n,q):return [x for x in range(q) if pow(x,n,q)==q-1]
def rank(M,q):
 A=[list(r) for r in M];k=0
 for j in range(len(A[0]) if A else 0):
  p=next((i for i in range(k,len(A)) if A[i][j]%q),None)
  if p is None:continue
  A[k],A[p]=A[p],A[k];z=pow(A[k][j],-1,q);A[k]=[x*z%q for x in A[k]]
  for i in range(k+1,len(A)):
   z=A[i][j];A[i]=[(x-z*y)%q for x,y in zip(A[i],A[k])]
  k+=1
  if k==len(A):break
 return k

def autom(h,a):
 n=len(h);out=[0]*n
 for i,x in enumerate(h):
  e=(a*i)%(2*n);out[e%n]+=x if e<n else -x
 return tuple(out)

# Exact hypergeometric tail comparison: fourth powers eliminate the irrational bound.
occ=0
for n in (2,4,8,16,32):
 for r in (1,2,4,8,16,32):
  if r>n:continue
  for s in range((r+1)//2,r+1):
   S=s*n//r
   for d in range(1,n):
    J=d//4
    count=sum(comb(S,j)*comb(n-S,d-j) for j in range(J+1) if j<=S and 0<=d-j<=n-S)
    p=Q(count,comb(n,d));assert p**4<=Q(16,27)**d
    occ+=1

# Direct rank-one row counts retain every zero row.
rank_rows=[]
for q,m in [(5,0),(5,1),(5,2),(5,3),(17,2)]:
 count=0
 for flat in product(range(q),repeat=2*m):
  rows=list(zip(flat[::2],flat[1::2]));nz=next((z for z in rows if z!=(0,0)),None)
  if nz is None or all((nz[0]*b-nz[1]*a)%q==0 for a,b in rows):count+=1
 expected=1+(q+1)*(q**m-1)
 assert count==expected
 rank_rows.append({'q':q,'rows':m,'enumerated_amplitude_tuples':q**(2*m),'rank_at_most_one_count':count,'probability':str(Q(count,q**(2*m)))})

# Full small coefficient norm/support and fixed-space counting control.
n=4;q=17;rr=roots(n,q);V=[[pow(t,j,q) for j in range(n)] for t in rr];W=invmat(V,q)
G=(1,3,5,7);Hs=[]
for mask in range(1<<len(G)):
 H={G[i] for i in range(len(G)) if mask>>i&1}
 if 1 in H and all((a*b)%8 in H for a in H for b in H):Hs.append(H)
fixed=[];normchecks=0
for H in Hs:
 hs=[h for h in product((-1,0,1),repeat=n) if all(autom(h,a)==h for a in H)]
 r=n//len(H);assert len(hs)<=3**r
 for h in hs:
  if any(h):
   s=sum(x!=0 for x in matvec(V,h,q));assert s>n/2;normchecks+=1
 fixed.append({'H':sorted(H),'index':r,'bounded_fixed_vectors':len(hs),'count_bound':3**r})
# Uniform image pivot bound for every ideal and B in {0,1,2}.
pivot=[]
for s in range(n+1):
 for T in combinations(range(n),s):
  counts=[0,0,0]
  for vals in product(range(q),repeat=s):
   crt=[0]*n
   for i,x in zip(T,vals):crt[i]=x
   u=matvec(W,crt,q);mx=max(min(x,q-x) for x in u)
   for B in (0,1,2):counts[B]+=mx<=B
  for B,count in enumerate(counts):assert count<=(2*B+1)**s
  pivot.append({'support':T,'dimension':s,'box_counts_B012':counts})

# Pure polynomial lemma: field F_5, four distinct nonzero evaluation points.
# This checks the algebraic supplement, not a split n=4 source at q=5.
q0=5;k=2;T=(1,2,3,4);d=4;bad=0
for flat in product(range(q0),repeat=2*d):
 M=[[flat[2*i],flat[2*i]*t%q0,flat[2*i+1],flat[2*i+1]*t%q0] for i,t in enumerate(T)]
 bad+=rank(M,q0)<2*k
pbad=Q(bad,q0**(2*d));assert pbad<=Q(k*q0**(2*k-d),q0-1)

# Fully retained coefficient product noise, n=2,q=97,d=1,r=1,C=1,B=0,b=1.
# Public acceptance is A1=0 or A2=0 or A1=A2 or A1=-A2.
n=2;q=97;rr=roots(n,q);V=[[1,t] for t in rr];W=invmat(V,q)
bases=[tuple(W[j][i] for j in range(n)) for i in range(n)]
errors=list(product((-1,0,1),repeat=n));weight={-1:1,0:2,1:1}
assert n*(0+2*n*1*1)**2<q # square of the exact strict norm gate for d=1,n=2
sets={}
for i in range(n):
 for f in errors:sets[i,f]={tuple((a*b+e)%q for b,e in zip(bases[i],f)) for a in range(q)}
counts_same=0;counts_redrawn=0;gauss_same=0.0;gauss_redrawn=0.0;first_redrawn_counterexample=None
Z=1+2*exp(-pi)
for i,j in product(range(n),repeat=2):
 for f,g in product(errors,repeat=2):
  S1=sets[i,f];S2=sets[j,g];z1=(0,0) in S1;z2=(0,0) in S2
  diag=S1&S2;anti=S1&{tuple(-x%q for x in y) for y in S2}
  ct=q*int(z1)+q*int(z2)+len(diag)+len(anti)-3*int(z1 and z2)
  w=1
  for x in f+g:w*=weight[x]
  counts_redrawn+=w*ct
  gw=exp(-pi*sum(x*x for x in f+g))/Z**4
  gauss_redrawn+=gw*ct
  if i==j:
   counts_same+=w*ct;gauss_same+=gw*ct
   # Every accepted fixed direction must cancel F and U separately under the strict gate.
   if any(f):assert not z1
   if any(g):assert not z2
   if f!=g:assert not diag
   if any(a+b for a,b in zip(f,g)):assert not anti
  elif first_redrawn_counterexample is None and anti and any(a+b for a,b in zip(f,g)):
   A1=next(iter(sorted(anti)));A2=tuple(-x%q for x in A1)
   U1=tuple((x-e)%q for x,e in zip(A1,f));U2=tuple((x-e)%q for x,e in zip(A2,g))
   assert all((a+b+c+e)%q==0 for a,b,c,e in zip(U1,U2,f,g))
   first_redrawn_counterexample={'T1_root':rr[i],'T2_root':rr[j],'F1':f,'F2':g,'U1_coeff_mod_q':U1,'U2_coeff_mod_q':U2,'A1':A1,'A2':A2,'multiplier_pair':[1,1],'public_sum_zero':True,'hidden_sum_nonzero':any((a+b)%q for a,b in zip(U1,U2))}
assert first_redrawn_counterexample['hidden_sum_nonzero']
public={'n':n,'q':q,'d':1,'r':1,'C':1,'b':1,'B':0,'roots':rr,'same_T_acceptance_rational_toy':str(Q(counts_same,2*256*q*q)),'redrawn_T_acceptance_rational_toy':str(Q(counts_redrawn,4*256*q*q)),'uniform_acceptance_exact':str(Q(4*q*q-3,q**4)),'Gaussian_truncated_same_T_float':gauss_same/(2*q*q),'Gaussian_truncated_redrawn_T_float':gauss_redrawn/(4*q*q),'Gaussian_four_coefficient_tail_bound':8*exp(-4*pi)/(1-exp(-5*pi)),'Gaussian_qualification':'D_1 conditioned on [-1,1] in every coefficient; probability decimals have unbounded floating rounding; displayed whole-source tail bound is analytic.','redrawn_support_counterexample':first_redrawn_counterexample,'scope':'Finite boundary control. r=o(d) does not hold; no new attack claimed.'}
# CP-1 arithmetic, rejecting the false sequential product inference.
assert Q(21,2000)>Q(1,10)**2 and Q(21,221)<Q(1,10)
print(json.dumps({'status':'PROVISIONAL','seed':None,'exact_occupancy_checks':occ,'rank_row_controls':rank_rows,'fixed_space_controls':fixed,'short_multiplier_norm_controls':normchecks,'uniform_pivot_controls':pivot,'low_degree_rank_control':{'field':5,'evaluation_points':T,'k':2,'d':4,'tuples':5**8,'deficient_count':bad,'deficient_probability':str(pbad),'bound':str(Q(1,2)),'scope':'Pure algebraic lemma, not a split n=4 q=5 source'},'public_coefficient_noise_control':public,'cp1_matching_probability':'21/2000','elapsed_seconds':time.monotonic()-t0},indent=2))
