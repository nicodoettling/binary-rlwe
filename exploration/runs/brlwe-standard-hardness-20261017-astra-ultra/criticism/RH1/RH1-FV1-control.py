#!/usr/bin/env python3
"""Independent residue-degree-two full-law falsification control."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import itertools,json,resource,time
resource.setrlimit(resource.RLIMIT_AS,(67108864,67108864))
start=time.monotonic()
root=Path(__file__).resolve().parent
cfg=json.loads((root/'RH1-FV1-input.json').read_text())
points=list(itertools.product(range(-3,4),repeat=2))
residues=list(itertools.product(range(3),repeat=2))
assert len(points)==49
def det(x,y):return x[0]*y[1]-x[1]*y[0]
def norm2(x):return sum(a*a for a in x)
def addc(x,y,c):return tuple(c[0]*a+c[1]*b for a,b in zip(x,y))
def residue(x):return tuple(a%3 for a in x)
coeffs=sorted((c for c in points if c!=(0,0)),key=lambda c:(norm2(c),c))
relations={}
rank_counts=defaultdict(int)
for a,b in itertools.product(residues,repeat=2):
    image={residue(addc(a,b,c)) for c in residues}
    kernel={c for c in residues if residue(addc(a,b,c))==(0,0)}
    h=len(image)
    rank=0 if a==b==(0,0) else (2 if det(a,b)%3 else 1)
    assert h==3**rank and h*len(kernel)==9
    chosen=next(c for c in coeffs if residue(addc(a,b,c))==(0,0))
    assert norm2(chosen)**2<=2*h*h
    relations[(a,b)]=(chosen,h)
    rank_counts[rank]+=1
assert dict(rank_counts)=={0:1,1:32,2:48}
assert det((1,0),(0,3))==3
assert relations[((1,0),(0,0))][1]==3
cases=0
outputs=[]
for tb in cfg['weight_bases']:
    t=Q(*tb)
    weights={x:t**norm2(x) for x in points}
    z=sum(weights.values(),Q(0))
    cosets={a:sum((weights[x] for x in points if residue(x)==a),Q(0)) for a in residues}
    assert all(v>0 for v in cosets.values())
    pi={a:v/z for a,v in cosets.items()}
    src,cmp=defaultdict(Q),defaultdict(Q)
    hsrc,hcmp=defaultdict(Q),defaultdict(Q)
    hpass=defaultdict(Q)
    input_tv=Q(0)
    zero_before_screen=Q(0)
    for x,y in itertools.product(points,repeat=2):
        cases+=1
        a,b=residue(x),residue(y)
        ps=weights[x]*weights[y]/z**2
        pc=weights[x]*weights[y]/(81*cosets[a]*cosets[b])
        assert ps==pc*81*pi[a]*pi[b]
        input_tv+=abs(ps-pc)/2
        c,h=relations[(a,b)]
        hsrc[h]+=ps;hcmp[h]+=pc
        image=addc(x,y,c)
        assert residue(image)==(0,0)
        assert norm2(image)<=norm2(c)*(norm2(x)+norm2(y))
        if image==(0,0):zero_before_screen+=ps
        if det(x,y)==0:
            label='FAIL'
        else:
            assert image!=(0,0)
            label=str(image)
            hpass[h]+=ps
        src[label]+=ps;cmp[label]+=pc
    residue_tv=sum((abs(pi[a]*pi[b]-Q(1,81)) for a,b in itertools.product(residues,repeat=2)),Q(0))/2
    output_tv=sum((abs(src[a]-cmp[a]) for a in set(src)|set(cmp)),Q(0))/2
    assert input_tv==residue_tv
    assert output_tv<=input_tv
    assert sum(src.values())==sum(cmp.values())==1
    assert dict(hcmp)=={1:Q(1,81),3:Q(32,81),9:Q(48,81)}
    assert hsrc[1]==pi[(0,0)]**2
    assert hpass[3]>0 and hpass[9]>0
    assert zero_before_screen>0 and src['FAIL']>0
    original_nonzero_alignment=(cosets[(0,0)]-1)/z
    conditioned_nonzero_alignment=(cosets[(0,0)]-1)/(z-1)
    assert conditioned_nonzero_alignment>original_nonzero_alignment>0
    outputs.append({
      'weight':str(t),'normalizer':str(z),
      'residue_masses':{str(a):str(v) for a,v in pi.items()},
      'source_index_law':{str(a):str(v) for a,v in hsrc.items()},
      'comparator_index_law':{str(a):str(v) for a,v in hcmp.items()},
      'source_index_and_rank_pass_mass':{str(a):str(v) for a,v in hpass.items()},
      'full_input_TV':str(input_tv),'residue_TV':str(residue_tv),'output_TV':str(output_tv),
      'source_FAIL':str(src['FAIL']),'comparator_FAIL':str(cmp['FAIL']),
      'zero_image_without_screen':str(zero_before_screen),
      'original_nonzero_alignment':str(original_nonzero_alignment),
      'zero_conditioned_alignment':str(conditioned_nonzero_alignment),
      'source_output_including_FAIL':{a:str(v) for a,v in sorted(src.items())},
      'comparator_output_including_FAIL':{a:str(v) for a,v in sorted(cmp.items())}
    })
assert cases==4802<=cfg['max_pairs']
print(json.dumps({'status':'PASS_FINITE_SCOPE_ONLY','reservation':cfg['reservation'],
  'cases':cases,'rank_matrix_counts':dict(rank_counts),'laws':outputs,
  'infinite_Gaussian_certified':False,'hardness_evidence':False,
  'wall_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2,sort_keys=True))
