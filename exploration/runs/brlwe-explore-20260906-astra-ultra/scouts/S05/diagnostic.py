"""Bounded n=8, q=7 ideal/cube diagnostic; run only after coordinator allocation."""
import itertools, json, math
from collections import Counter

N, Q = 8, 7

def mul(a,b,mod=None):
    out=[0]*N
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            k=i+j
            out[k%N] += x*y*(1 if k<N else -1)
    return tuple(x%mod for x in out) if mod else tuple(out)

def star(a):
    return (a[0],)+tuple(-a[N-j] for j in range(1,N))

def rank(mat):
    a=[list(row) for row in mat]
    r=0
    for j in range(N):
        p=next((k for k in range(r,N) if a[k][j]%Q),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        inv=pow(a[r][j],-1,Q)
        a[r]=[x*inv%Q for x in a[r]]
        for k in range(N):
            if k!=r:
                t=a[k][j]
                a[k]=[(x-t*y)%Q for x,y in zip(a[k],a[r])]
        r+=1
    return r

conference=[]
for signs in itertools.product((-1,1),repeat=N-1):
    c=(0,)+signs
    if mul(c,star(c))==(Q,)+(0,)*(N-1):
        conference.append(c)
c=conference[0]
cols=[mul(c,tuple(int(i==j) for i in range(N)),Q) for j in range(N)]
r=rank(list(zip(*cols)))
image_size=Q**r

def dist(values):
    counts={(0,)*N:1}
    for col in cols:
        new=Counter()
        for x,mass in counts.items():
            for v in values:
                new[tuple((a+v*b)%Q for a,b in zip(x,col))]+=mass
        counts=new
    return counts

binary=dist((0,1))
result={"n":N,"q":Q,"conference_count_zero_at_0":len(conference),"c":c,
        "rank_c":r,"binary_fiber_histogram":dict(sorted(Counter(binary.values()).items())),
        "binary_image_size":len(binary),"empty_field_fibers":image_size-len(binary),
        "binary_secrets_in_nontrivial_fibers":sum(v for v in binary.values() if v>1),
        "box_perturbations":[]}
for h in range(4):
    counts=dist(tuple(range(-h,h+1)))
    denom=(2*h+1)**N
    tv=(sum(abs(mass/denom-1/image_size) for mass in counts.values())+(image_size-len(counts))/image_size)/2
    small=lambda x: min(x,Q-x)<=1
    result["box_perturbations"].append({"H":h,"support":len(counts),"quotient_TV":tv,
        "fixed_collision_coordinate_probability_within_1":sum(mass for x,mass in counts.items() if small(x[0]))/denom,
        "fixed_collision_all_coordinates_probability_within_1":sum(mass for x,mass in counts.items() if all(small(z) for z in x))/denom,
        "unwrapped_collision_RMS":math.sqrt((N-1)*h*(h+1)/3)})
print(json.dumps(result,indent=2))
