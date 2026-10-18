import itertools, json, math, resource, time
resource.setrlimit(resource.RLIMIT_AS, (268435456,268435456))
start=time.monotonic()

def subspaces(n,m,q):
    for piv in itertools.combinations(range(n),m):
        free=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
        for values in itertools.product(range(q),repeat=len(free)):
            rows=[[int(j==p) for j in range(n)] for p in piv]
            for (i,j),v in zip(free,values): rows[i][j]=v
            yield piv,rows

def member(v,piv,rows,q):
    v=list(v)
    for p,row in zip(piv,rows):
        a=v[p]
        if a:v=[(x-a*y)%q for x,y in zip(v,row)]
    return not any(v)

results=[]
for n,m,q in [(2,1,5),(4,2,17)]:
    count=stable=0;examples=[]
    for piv,rows in subspaces(n,m,q):
        count+=1
        if all(member([-row[-1]%q]+row[:-1],piv,rows,q) for row in rows):
            stable+=1;examples.append(rows)
    num=den=1
    for i in range(m):num*=q**(n-i)-1;den*=q**(m-i)-1
    assert num%den==0 and count==num//den
    assert stable==math.comb(n,m)
    results.append(dict(n=n,m=m,q=q,total=count,invariant=stable,exact_probability=f'{stable}/{count}',examples=examples))
print(json.dumps(dict(results=results,wall_seconds=time.monotonic()-start,maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,seed=None,arithmetic='exact integer modular',assertions='passed'),indent=2))
