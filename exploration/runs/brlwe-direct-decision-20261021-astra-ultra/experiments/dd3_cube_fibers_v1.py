"""Exact bounded binary-cube CRT fibers for ramified ideals (2,(X+1)^a)."""
import json, math, time
from collections import Counter
from fractions import Fraction

def prime(n):
    if n<2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0:return n==p
    d=n-1;s=0
    while d%2==0:s+=1;d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        a%=n
        if a==0:continue
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True

def split_prime(n,low):
    q=max(1,(low-1+2*n-1)//(2*n))*2*n+1
    for _ in range(100000):
        if prime(q):return q
        q+=2*n
    raise RuntimeError('bounded prime search exhausted')

def roots(n,q):
    for g in range(2,100002):
        z=pow(g,(q-1)//(2*n),q)
        if pow(z,n,q)==q-1:
            return [pow(z,2*j+1,q) for j in range(n)]
    raise RuntimeError('bounded root search exhausted')

def residue(b,a):
    if a==0:return 0
    f=sum(1<<j for j in range(a+1) if (j & a)==j)
    while b.bit_length()>a:
        b^=f << (b.bit_length()-1-a)
    return b

def main():
    start=time.monotonic();results=[]
    for n in (2,4,8,16):
        ell=(2*n-1).bit_length();sigma=8*n*n*math.isqrt(n)**1*ell**4
        if math.isqrt(n)**2<n:sigma=8*n*n*(math.isqrt(n)+1)*ell**4
        for qkind,low in [('small_split_control',2*n+1),('inherited_q_lower_bound',n*sigma)]:
            q=split_prime(n,low);zs=roots(n,q)
            levels=sorted(set((0,n//4,n//2,3*n//4,n-1)))
            residues={a:[residue(b,a) for b in range(1<<n)] for a in levels}
            best={a:[0]*(1<<a) for a in levels};fixed={a:[] for a in levels}
            for z in zs:
                coeff=[pow(z,i,q) for i in range(n)];vals=[0]*(1<<n)
                for b in range(1,1<<n):
                    bit=b & -b;vals[b]=(vals[b^bit]+coeff[bit.bit_length()-1])%q
                for a in levels:
                    counts=Counter(zip(residues[a],vals));mx=[0]*(1<<a)
                    for (c,v),count in counts.items():mx[c]=max(mx[c],count)
                    fixed[a].append(sum(mx))
                    best[a]=[max(x,y) for x,y in zip(best[a],mx)]
            for a in levels:
                total=sum(best[a]);den=1<<n
                assert len(set(residues[a]))==1<<a
                results.append({'n':n,'a':a,'ideal':'(2,(X+1)^a)','norm':1<<a,'rho':str(Fraction(a,n)),'qkind':qkind,'q':q,'sigma':sigma,'ell':ell,'q_ge_n_sigma':q>=n*sigma,'root_count':len(zs),'cube_count':den,'residue_guess':str(Fraction(1<<a,den)),'selected_root_guess':str(Fraction(total,den)),'fixed_root_success_range':[str(Fraction(min(fixed[a]),den)),str(Fraction(max(fixed[a]),den))],'max_fiber_size':max(best[a]),'minimum_fiber_size':min(best[a]),'exact':True})
    print(json.dumps({'hypothesis':'Selected-root guessing requires a different fiber statistic from whole-secret guessing; ramified ideal controls measure its size.','seed':'deterministic exhaustive; no randomness','results':results,'wall_seconds':time.monotonic()-start,'limitations':'Finite dimensions only; small-split cases do not meet inherited noise/q parameters; no Gaussian theorem or asymptotic bound certified.'},indent=2))

if __name__=='__main__':main()
