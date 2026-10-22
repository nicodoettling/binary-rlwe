import itertools as it
import json
import math
import random
from fractions import Fraction as F

def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def tr(A):return [list(x) for x in zip(*A)]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def neg(A):return [[-x for x in a] for a in A]
def sub(A,B):return add(A,neg(B))
def mul(A,B):return [[sum(x*y for x,y in zip(a,b)) for b in zip(*B)] for a in A]
def scale(c,A):return [[c*x for x in a] for a in A]
def fn2(A):return sum(x*x for a in A for x in a)
def trace(A):return sum(A[i][i] for i in range(len(A)))
def shift(n):
    T=[[0]*n for _ in range(n)]
    for j in range(n):T[(j+1)%n][j]=-1 if j==n-1 else 1
    return T
seed=20261021;rng=random.Random(seed)
counts={'secrets':0,'faces':0,'PSD_cases':0,'spectral_trace_bound_cases':0}
for n in [4,8]:
    I=eye(n);T=shift(n);powers=[I]
    for i in range(1,n):powers.append(mul(powers[-1],T))
    for case in range(4):
        R=[[rng.randrange(-2,3) for _ in range(n)] for _ in range(n)]
        C=mul(R,tr(R));A=[[rng.randrange(-1,2) for _ in range(n)] for _ in range(n)]
        B=add(mul(mul(A,C),tr(A)),I)
        target=add(B,scale(trace(C),I))
        K=add(mul(T,C),mul(C,tr(T)))
        assert fn2(K)*n**3>=16*trace(C)**2
        counts['spectral_trace_bound_cases']+=1
        V={};dist={}
        for s in it.product([0,1],repeat=n):
            M=[[0]*n for _ in range(n)]
            for b,P in zip(s,powers):
                if b:M=add(M,P)
            diff=sub(A,M);V[s]=add(mul(mul(diff,C),tr(diff)),I)
            dist[s]=fn2(sub(V[s],target));counts['secrets']+=1
        for rest in it.product([0,1],repeat=n-2):
            keys=[(a,b)+rest for a,b in [(0,0),(1,0),(0,1),(1,1)]]
            second=add(sub(sub(V[keys[3]],V[keys[1]]),V[keys[2]]),V[keys[0]])
            assert second==K
            assert 16*max(dist[k] for k in keys)>=fn2(K)
            counts['faces']+=1
        assert 4*sum(16*x>=fn2(K) for x in dist.values())>=2**n
        counts['PSD_cases']+=1

# Required excluded-degree control: nonzero C and all four equal covariances.
n=2;I=eye(n);T=shift(n);C=I;B=I;H=scale(F(1,2),sub(I,T));Vs=[]
for s in it.product([0,1],repeat=2):
    M=add(scale(s[0],I),scale(s[1],T))
    V=sub(sub(add(B,mul(mul(M,C),tr(M))),mul(M,H)),mul(tr(H),tr(M)))
    assert V==I
    Vs.append(V)
assert sub(B,mul(tr(H),H))==scale(F(1,2),I)

# Bounded scalar Fourier diagnostic; exact inequality proved analytically.
float_checks=0
for L in [1,2,10,1000]:
    for i,j in it.product(range(11),repeat=2):
        v=L*i/10;w=L*j/10
        lhs=abs(math.exp(-v/(2*L))-math.exp(-w/(2*L)))
        rhs=math.exp(-0.5)*abs(v-w)/(2*L)
        assert lhs+1e-14>=rhs
        float_checks+=1
print(json.dumps({'seed':seed,'exact_counts':counts,'n2_exception':'nonzero C=I, all four covariances=I, PSD joint covariance checked by Schur complement','scalar_fourier_diagnostics':float_checks,'precision':'Core exact integers/Fraction. Scalar exp checks binary64 and diagnostic only; no tails or infinite distribution enumerated.','conditional_scope':'Uniform cube faces partition all S; at least1/4 of secrets have stated covariance discrepancy. Gaussian characteristic argument remains analytic, not inferred from finite controls.','CP-1':'No sequential event product; previous exact21/2000>1/100 regression remains binding.'},indent=2))
