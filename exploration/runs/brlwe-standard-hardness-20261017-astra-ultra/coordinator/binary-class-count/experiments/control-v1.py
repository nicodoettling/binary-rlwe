import itertools,json,math,resource,signal,time
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
signal.alarm(60)
started=time.monotonic()
def mul(a,b):
 n=len(a);c=[0]*n
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   z=i+j;c[z%n]+=x*y*(1 if z<n else -1)
 return c
def norm(a):
 if len(a)==1:return a[0]
 e=a[::2];o=a[1::2];ee=mul(e,e);oo=mul(o,o);shift=[-oo[-1]]+oo[:-1]
 return norm([x-y for x,y in zip(ee,shift)])
def det(a):
 n=len(a);cols=[]
 for j in range(n):
  b=[0]*n;b[j]=1;cols.append(mul(a,b))
 m=[[cols[j][i] for j in range(n)] for i in range(n)];prev=1;sgn=1
 for k in range(n-1):
  if not m[k][k]:
   z=next((j for j in range(k+1,n) if m[j][k]),None)
   if z is None:return 0
   m[k],m[z]=m[z],m[k];sgn=-sgn
  pivot=m[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    v=m[i][j]*pivot-m[i][k]*m[k][j]
    assert v%prev==0;m[i][j]=v//prev
  for i in range(k+1,n):m[i][k]=0
  prev=pivot
 return sgn*m[-1][-1]
def factors(m):
 ans=[];p=2
 while p*p<=m:
  v=0
  while m%p==0:m//=p;v+=1
  if v:ans.append((p,v))
  p+=1
 if m>1:ans.append((m,1))
 return ans
def order(p,m):
 x=p%m;r=1
 while x!=1:x=x*p%m;r+=1
 return r
rows=[]
for n in [2,4,8]:
 B=n**(n//2);vmax=(n//2)*(n.bit_length()-1);u=0
 while (2*n+1)**(u+1)<=B:u+=1
 bound=(vmax+1)*2**u;count=0;maxnorm=0;maxdivbound=0;sumdivbound=0;detchecks=0
 for a in itertools.product([-1,0,1],repeat=n):
  if not any(a):continue
  count+=1;z=norm(a);assert 1<=z<=B
  if n<=4 or count%31==0:
   assert det(a)==z;detchecks+=1
  e2=0;omega=0
  for p,v in factors(z):
   if p==2:e2=v
   else:
    f=order(p,2*n);assert p**f>=2*n+1;assert v%f==0;omega+=v//f
  assert (2*n+1)**omega<=z
  db=(e2+1)*2**omega;assert db<=bound
  maxnorm=max(maxnorm,z);maxdivbound=max(maxdivbound,db);sumdivbound+=db
 assert count==3**n-1
 rows.append(dict(n=n,states=count,B=B,vmax=vmax,umax=u,per_polynomial_bound=bound,max_norm=maxnorm,max_norm_based_divisor_bound=maxdivbound,sum_norm_based_divisor_bounds=sumdivbound,global_count_bound=(3**n-1)*bound,independent_determinant_checks=detchecks))
assert norm([1,1])==2
result={'status':'PASS','seed':'none; exhaustive lexicographic support','rows':rows,'total_states':sum(x['states'] for x in rows),'wall_seconds':time.monotonic()-started,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'precision':'exact Python integers; timing only is floating point','limits':{'wall_seconds':60,'address_space_bytes':268435456},'scope':'Norm and multiplicity/count controls only, not exact enumeration of all ideal classes or a hardness/asymptotic certificate'}
print(json.dumps(result,indent=2))
