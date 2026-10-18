"""A-tower-finite-1: deterministic, exact finite falsification controls."""
import itertools, json, math, time
from fractions import Fraction

started = time.monotonic()

def add(a,b,q): return tuple((x+y)%q for x,y in zip(a,b))
def scale(a,c,q): return tuple(c*x%q for x in a)
def mul(a,b,q):
    n=len(a); c=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            k=i+j
            c[k%n]=(c[k%n]+(1 if k<n else -1)*x*y)%q
    return tuple(c)
def unit_basis(n,j): return tuple(int(i==j) for i in range(n))
def binary(n): return itertools.product(range(2),repeat=n)
def gadget(a,n,r,q):
    return tuple(sum((2**j)*a[r*t+j] for j in range(r))%q for t in range(n))
def embed(a,r):
    c=[0]*(len(a)*r)
    for t,v in enumerate(a): c[r*t]=v
    return tuple(c)

results={"reservation":"A-tower-finite-1","arithmetic":"exact integers/Fraction","seed":"none; exhaustive deterministic cases"}
tower=[]
for q in (17,41):
    n=r=2; N=4; y=unit_basis(N,1); ym2=(q-2,1,0,0)
    X=unit_basis(n,1)
    # Exhaust all A for q=17, a deterministic grid for q=41; all binary Z.
    arange=range(q) if q==17 else range(3)
    ann=[]; acount=0; productchecks=0
    for A in itertools.product(arange,repeat=N):
        acount+=1
        if mul(A,ym2,q)==(0,)*N: ann.append(A)
        # Separate coefficient-block product check on a deterministic subset.
        if acount<=81:
            A0=(A[0],A[2]); A1=(A[1],A[3])
            for Z in binary(N):
                Z0=(Z[0],Z[2]); Z1=(Z[1],Z[3])
                B0=add(mul(A0,Z0,q),mul(X,mul(A1,Z1,q),q),q)
                B1=add(mul(A1,Z0,q),mul(A0,Z1,q),q)
                assert mul(A,Z,q)==(B0[0],B1[0],B0[1],B1[1])
                productchecks+=1
    if q==17: assert len(ann)==17
    else: assert len(ann)==1
    for Z in binary(N):
        lhs=gadget(mul(y,Z,q),n,r,q)
        Zlast=(Z[1],Z[3])
        rhs=add(scale(gadget(Z,n,r,q),2,q),mul(((q-4)%q,1),Zlast,q),q)
        assert lhs==rhs
    for A in ann:
        for Z in binary(N):
            assert mul(A,Z,q)==mul(A,embed(gadget(Z,n,r,q),r),q)
    tower.append({"q":q,"N":N,"A_checked":acount,"annihilator_count_in_checked_set":len(ann),"product_checks":productchecks,"all_binary_gadget_defects_checked":16})

# A genuine evaluation root, with all base CRT roots checked.
gamma=(5,12); q=17
assert mul(gamma,gamma,q)==(0,1)
assert (gamma[0]+4*gamma[1])%q==2
assert (gamma[0]+13*gamma[1])%q==8
results["tower_controls"]=tower
results["valid_evaluation"]={"q":17,"gamma_coefficients":gamma,"gamma_squared":[0,1],"CRT_values":[2,8]}

# Count every exact pushforward of an invertible affine map in F_q^2.
affine=[]
for q in (3,5):
    good=[]; tested=0
    cube=set(binary(2))
    for a,b,c,d in itertools.product(range(q),repeat=4):
        if (a*d-b*c)%q==0: continue
        for t in itertools.product(range(q),repeat=2):
            tested+=1
            out={((a*x+b*y+t[0])%q,(c*x+d*y+t[1])%q) for x,y in cube}
            if out==cube:
                good.append(((a,b,c,d),t))
    assert len(good)==8
    for mat,t in good:
        rows=(mat[:2],mat[2:])
        assert all(sum(v!=0 for v in row)==1 for row in rows)
        for i,row in enumerate(rows):
            v=next(v for v in row if v)
            assert (v,t[i]) in ((1,0),(q-1,1))
    affine.append({"q":q,"dimension":2,"invertible_affine_maps_tested":tested,"cube_preservers":len(good),"complete_preservers":good})
results["affine_cube_controls"]=affine

# Independent ring-specific enumeration: enumerate all scalars and offsets.
ring=[]
for q in (3,5):
    cube=set(binary(2)); allvectors=list(itertools.product(range(q),repeat=2))
    good=[]; units=0
    for u in allvectors:
        if len({mul(u,x,q) for x in allvectors})!=q*q: continue
        units+=1
        for t in allvectors:
            out={add(mul(u,x,q),t,q) for x in cube}
            if out==cube: good.append((u,t))
    assert len(good)==4
    assert {u for u,t in good}=={(1,0),(q-1,0),(0,1),(0,q-1)}
    ring.append({"q":q,"degree":2,"units":units,"cube_preservers":good})
results["ring_affine_controls"]=ring

# Negative control: characteristic two admits a non-permutation cube map.
cube2=set(binary(2))
out2={((x+y)%2,y) for x,y in cube2}
assert out2==cube2
results["negative_control_char2"]={"matrix":[[1,1],[0,1]],"preserves_cube":True,"signed_permutation":False}

# Exact digit entropy counts in a real split tower n=2,r=8,q=97.
n,r,q=2,8,97; M=(2**r)//q
encoded=[s+q*k for s in range(q) for k in range(M)]
assert sorted(encoded)==list(range(q*M))
tv=1-Fraction(q*M,2**r)**n
assert tv==Fraction(6975,16384)
results["digit_lift"]={"n":n,"r":r,"N":n*r,"q":q,"M":M,"per_coefficient_support":len(set(encoded)),"joint_TV":str(tv),"upper_bound":str(Fraction(n*q,2**r))}

# Count the disjoint finite-difference triples for every interval residue.
triples=[]
for q in (17,41,97):
    counts=[]
    for start in range(4):
        count=sum(1 for x in range(start,start+q-2) if x%4==0)
        assert count>=math.floor((q-3)/4)
        counts.append(count)
    triples.append({"q":q,"counts_by_start_mod4":counts,"claimed_lower_count":math.floor((q-3)/4)})
results["triple_counts"]=triples
results["all_assertions_passed"]=True
results["elapsed_seconds_internal"]=time.monotonic()-started
print(json.dumps(results,indent=2,sort_keys=True))
