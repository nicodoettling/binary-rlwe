import json, math, resource, time
from fractions import Fraction
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
started=time.monotonic()

def mul(a,b):
    n=len(a);c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<n:c[i+j]+=x*y
            else:c[i+j-n]-=x*y
    return c

def determinant(a):
    a=[row[:] for row in a]; n=len(a); last=1;sign=1
    for k in range(n-1):
        if not a[k][k]:
            i=next(i for i in range(k+1,n) if a[i][k])
            a[k],a[i]=a[i],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*pivot-a[i][k]*a[k][j]
                assert z%last==0
                a[i][j]=z//last
            a[i][k]=0
        last=pivot
    return sign*a[-1][-1]

def order(a,m):
    x=a%m;f=1
    while x!=1:x=x*a%m;f+=1
    return f

rows=[]
for n in [2,4,8,16,32,64]:
    m=n//2;N=2*n
    B=2**max(1,n//4)
    spf=list(range(B+1))
    for i in range(2,math.isqrt(B)+1):
        if spf[i]==i:
            for j in range(i*i,B+1,i):
                if spf[j]==j:spf[j]=i
    coeff=[0]*(B+1);coeff[1]=1;local={}
    for k in range(2,B+1):
        p=spf[k];rest=k;e=0
        while rest%p==0:rest//=p;e+=1
        if p==2:v=1
        else:
            if p not in local:local[p]=(order(p,N),None)
            f=local[p][0];g=n//f
            v=math.comb(g+e//f-1,e//f) if e%f==0 else 0
            # Coefficientwise comparison with n independent degree-one factors.
            assert v<=math.comb(n+e-1,e)
        coeff[k]=coeff[rest]*v
    count=sum(coeff)
    bound=Fraction(B*B*5**n,3**n)  # zeta(2)<5/3, proved by integral tail.
    assert count<=bound
    t=[0]*n
    if n>2:t[1]=1;t[n-1]=-1
    powers=[[1]+[0]*(n-1)]
    for i in range(2*m-2):powers.append(mul(powers[-1],t))
    gram=[[m*powers[i+j][0] for j in range(m)] for i in range(m)]
    disc=determinant(gram)
    assert disc==n**m//2
    # Trace form of the full power basis: Tr(X^k)=n at k0, -n at kn.
    gram_full=[[n if i+j==0 else (-n if i+j==n else 0) for j in range(n)] for i in range(n)]
    disc_full=abs(determinant(gram_full))
    assert disc_full==n**n and disc_full==4*disc*disc
    rows.append({'n':n,'norm_cutoff':B,'exact_ideal_count':count,'real_discriminant':disc,'absolute_complex_discriminant':disc_full,'bound_numerator':bound.numerator,'bound_denominator':bound.denominator,'all_checks':True})
print(json.dumps({'schema':1,'seed':None,'arithmetic':'exact integers and fractions','results':rows,'scope':'Euler-factor ideal-count bound and discriminant identities only; no class number, analytic asymptotic, or hardness certification','wall_seconds':time.monotonic()-started,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
