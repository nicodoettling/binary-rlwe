import json,math,time
start=time.monotonic()
def prime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
def rank(A,p):
 A=[x[:] for x in A];r=0
 for c in range(len(A[0]) if A else 0):
  k=next((k for k in range(r,len(A)) if A[k][c]%p),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];a=pow(A[r][c],-1,p);A[r]=[a*x%p for x in A[r]]
  for k in range(len(A)):
   if k!=r:
    a=A[k][c];A[k]=[(x-a*y)%p for x,y in zip(A[k],A[r])]
  r+=1
 return r
def subgroup(a,b,M):
 seen={1};todo=[1]
 while todo:
  z=todo.pop()
  for k in [a,b]:
   w=z*k%M
   if w not in seen:seen.add(w);todo.append(w)
 return tuple(sorted(seen))
def fixed_basis(n,H):
 seen=set();out=[]
 for i in range(n):
  if i in seen:continue
  vals={i:1};todo=[i];ok=True
  while todo:
   j=todo.pop()
   for a in H:
    k=a*j%(2*n);sgn=1 if k<n else -1;k%=n;v=vals[j]*sgn
    if k in vals:
     if vals[k]!=v:ok=False
    else:vals[k]=v;todo.append(k)
  seen.update(vals)
  if ok:out.append([vals.get(j,0) for j in range(n)])
 return out
rows=[];chainchecks=0;allchecks=0
for n in [4,8,16,32]:
 p=next(p for p in range(2*n+1,10000,2*n) if prime(p));alpha=next(a for a in range(1,p) if pow(a,n,p)==p-1)
 G=list(range(1,2*n,2));Hs=set(subgroup(a,b,2*n) for a in G for b in G)
 for t in range(1,n,2):
  T={2*j+1 for j in range(t)};stab=[a for a in G if {a*x%(2*n) for x in T}==T];assert stab==[1]
  gs=[2**i for i in range(1,n.bit_length())];ds=[]
  for g in gs:
   A=[[pow(alpha,(2*j+1)*(n//g)*k,p) for k in range(g)] for j in range(t)]
   r=rank(A,p);assert r==min(t,g);chainchecks+=1
   if p**r<2**g:ds.append(p**r);assert g>t*math.log2(p)
  if p**t<2**n:
   assert ds and min(ds)==p**t
   dall=[]
   for H in Hs:
    basis=fixed_basis(n,H);g=len(basis);assert g*len(H)==n
    A=[[sum(v[k]*pow(alpha,(2*j+1)*k,p) for k in range(n))%p for v in basis] for j in range(t)]
    r=rank(A,p)
    if p**r<2**g:dall.append(p**r)
    allchecks+=1
   assert dall and min(dall)<=p**t<=min(dall)**2
   rows.append({'n':n,'p':p,'t':t,'index':p**t,'d_star':min(ds),'d_all':min(dall),'subfields':len(Hs),'stabilizer':stab})
# Boundary: odd t is essential for the cardinality proof, not an all-even converse.
n=8;T={1,9};stab=[a for a in range(1,16,2) if {a*x%16 for x in T}==T];assert stab==[1,9]
print(json.dumps({'status':'PASS','chain_rank_cases':chainchecks,'all_subfield_cases':allchecks,'eligible_rows':rows,'even_support_control':{'n':8,'roots':sorted(T),'stabilizer':stab},'arithmetic':'exact integers and finite fields; logarithm used only redundant diagnostic inequality','scope':'bounded structural controls, not infinite asymptotics or hardness','wall_seconds':time.monotonic()-start},indent=2))
