import resource, signal, time, json
from fractions import Fraction
from pathlib import Path
resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024))
resource.setrlimit(resource.RLIMIT_CPU,(18,18))
signal.setitimer(signal.ITIMER_REAL,20)
start=time.monotonic()
base=Path(__file__).parent
inp=json.loads((base/'entropy-control-v1-input.json').read_text())
ops=0

def determinant(A):
 global ops
 A=[r[:] for r in A];n=len(A);sign=1;prev=1
 for k in range(n-1):
  if A[k][k]==0:
   j=next(j for j in range(k+1,n) if A[j][k]);A[k],A[j]=A[j],A[k];sign=-sign
  p=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=A[i][j]*p-A[i][k]*A[k][j];assert num%prev==0
    A[i][j]=num//prev;ops+=1
  for i in range(k+1,n):A[i][k]=0
  prev=p
 return sign*A[-1][-1]

def inverse(A):
 global ops
 n=len(A);B=[[Fraction(v) for v in A[i]]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
 for k in range(n):
  j=next(j for j in range(k,n) if B[j][k]);B[k],B[j]=B[j],B[k]
  p=B[k][k];B[k]=[x/p for x in B[k]];ops+=2*n
  for i in range(n):
   if i!=k:
    p=B[i][k];B[i]=[B[i][j]-p*B[k][j] for j in range(2*n)];ops+=2*n
 return [r[n:] for r in B]

out=[]
for f in inp['candidates']:
 n=len(f)
 cols=[]
 for j in range(n):
  col=[0]*n
  for k,a in enumerate(f):col[(j+k)%n]+=a*(-1 if j+k>=n else 1)
  cols.append(col)
 A=[[cols[j][i] for j in range(n)] for i in range(n)]
 det=determinant(A);inv=inverse(A)
 classes={}
 for v in range(1<<n):
  bits=[(v>>j)&1 for j in range(n)]
  key=tuple(sum(inv[i][j]*bits[j] for j in range(n))%1 for i in range(n));ops+=n*n
  classes.setdefault(key,[]).append(v)
 hist={}
 for vs in classes.values():hist[len(vs)]=hist.get(len(vs),0)+1
 pairs=[]
 for col in cols:
  assert all(abs(v)==1 for v in col)
  pos=sum((1<<i) for i,v in enumerate(col) if v==1)
  neg=sum((1<<i) for i,v in enumerate(col) if v==-1)
  assert any(pos in vs and neg in vs for vs in classes.values())
  pairs.append([pos,neg])
 assert len({x for pair in pairs for x in pair})==2*n
 out.append({'f':f,'matrix_columns':cols,'determinant':det,'above_binary_cube':abs(det)>(1<<n),'class_count':len(classes),'fiber_size_histogram':hist,'rotation_collision_pairs':pairs,'all_coset_classes':[{'key':[str(x) for x in key],'binary_labels':vs} for key,vs in sorted(classes.items())]})
assert ops<100000
result={'input':inp,'results':out,'arithmetic_cells_counted':ops,'status':'PASS','scope':'Exact finite determinant and binary quotient classes only; Gaussian guessing proved analytically, no hardness claim.'}
(base/'entropy-control-v1-output.json').write_text(json.dumps(result,indent=2)+'\n')
res={'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'address_space_limit':256*1024*1024,'wall_limit_seconds':20,'cpu_limit_seconds':18,'processes':1,'arithmetic_cells_counted':ops}
(base/'entropy-control-v1-resources.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'status':'PASS','summary':[{k:v for k,v in r.items() if k in ['determinant','class_count','fiber_size_histogram','rotation_collision_pairs']} for r in out],'resources':res}))
