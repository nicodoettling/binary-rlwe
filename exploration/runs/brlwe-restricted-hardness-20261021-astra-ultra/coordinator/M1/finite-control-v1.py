from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
out=Path(__file__).with_name('finite-output-v1.json')
def q(x):return str(x)
rows=[];negative=None
M=10
for a,d in product(range(1,5),repeat=2):
 for b in range(a):
  for base in [F(1,2),F(15,16)]:
   ys=[y for y in range(-M,M+1) if y%d==0];wy={y:base**(y*y) for y in ys};zy=sum(wy.values());laws={};weights={};normalizers=[]
   for y in ys:
    xs=[x for x in range(-M,M+1) if (x-b*(y//d))%a==0];z=sum(base**(x*x) for x in xs);normalizers.append(z)
    for x in xs:
     laws[(x,y)]=wy[y]/zy*base**(x*x)/z;weights[(x,y)]=base**(x*x+y*y)
   ztarget=sum(weights.values());target={x:w/ztarget for x,w in weights.items()};assert sum(laws.values())==1 and sum(target.values())==1
   tv=sum(abs(laws[x]-target[x]) for x in laws)/2;ratio=max(normalizers)/min(normalizers);assert tv<=min(F(1),ratio-1)
   e=next(e for e in range(1,a*d+1) if e%a==0 and e%d==0 and (b*(e//d))%a==0);assert e%a==e%d==0
   row={'H':[[a,b],[0,d]],'base':q(base),'support':len(laws),'TV':q(tv),'density_ratio_bound':q(ratio),'scalar_normalizers':[q(z) for z in sorted(set(normalizers))],'additive_exponent':e,'probability_mass':q(sum(laws.values()))};rows.append(row)
   if (a,b,d,base)==(2,1,2,F(1,2)):
    assert tv>0;negative={'case':row,'full_joint':[{'x':list(x),'Q':q(laws[x]),'target':q(target[x])} for x in sorted(laws)],'rejected_claim':'Conditional scalar normalizers can be ignored or treated as constant.'}
# Exact elementary Gram-Schmidt for triangular matrices.
def gs(cols):
 orth=[]
 for c in cols:
  v=list(map(F,c))
  for w in orth:
   dot=sum(x*y for x,y in zip(v,w))/sum(x*x for x in w);v=[x-dot*y for x,y in zip(v,w)]
  orth.append(v)
 return [sum(x*x for x in w) for w in orth]
families=[]
for n in [4,8,16]:
 k=n//2;g=[0]*(k+1);g[0]=-1;g[n//4]=1;g[k]=1
 cols=[]
 for i in range(k):v=[0]*n;v[i]=3;cols.append(v)
 for i in range(n-k):v=[0]*n;v[i:i+k+1]=g;cols.append(v)
 norms=gs(cols);assert norms==[F(9)]*k+[F(1)]*(n-k)
 def rem(v):
  v=[x%3 for x in v]
  for j in range(n-1,k-1,-1):
   t=v[j]
   for h in range(k+1):v[j-k+h]=(v[j-k+h]-t*g[h])%3
  return v[:k]
 for v in cols:assert not any(rem(v));assert not any(rem([-v[-1]]+v[:-1]))
 assert 3**(5*k)<2**(4*n)
 families.append({'n':n,'basis_columns':cols,'index':3**k,'GS_squared':[q(x) for x in norms],'annihilator':3,'ideal_rotation_checks':2*n})
# Original CP1 ambient law, all160 atoms, selected posterior recomputed exactly.
atoms=[];prior={'A0':F(21,2200),'A1':F(21,2200),'C0':F(1,11),'C1':F(1,11),'D':F(879,1100)}
for name,mass in prior.items():
 for bits in product([0,1],repeat=5):
  x,e0,e1,f0,f1=bits;b=int(name[-1]) if name!='D' else None;trace=[] if name=='D' else ([1+b,3+b] if name[0]=='A' else [1+b,0]);vk=name[0]!='C' or x==b
  atoms.append({'trace_type':name,'bits':bits,'trace':trace,'mass':mass/F(32),'vk':vk})
z=sum(a['mass'] for a in atoms if a['vk']);assert z==F(10,11)
pinc=[sum(a['mass'] for a in atoms if a['vk'] and i in a['trace'])/z for i in range(5)];assert pinc==[F(1,10),F(121,2000),F(121,2000),F(21,2000),F(21,2000)]
hit=sum(a['mass'] for a in atoms if a['vk'] and a['trace_type']=='A'+str(a['bits'][0]))/z;assert hit==F(21,2000)>F(1,100)
matching=[a for a in atoms if a['vk'] and a['bits'][0]==0 and 1 in a['trace']];res=sum(a['mass'] for a in matching if 3 in a['trace'])/sum(a['mass'] for a in matching);assert res==F(21,221)<F(1,10)
for a in atoms:a['mass']=q(a['mass'])
result={'status':'PASS','model':'Exact finite truncated lattice Gaussian analogues; no claim that finite controls prove infinite Gaussian/hardness','support_bound':M,'deterministic':True,'matrix_law_cases':len(rows),'rows':rows,'normalizer_negative_control':negative,'exponential_index_family_controls':families,'CP1':{'ambient_atoms':atoms,'selected_mass':q(z),'incidences':list(map(q,pinc)),'two_stage_probability':q(hit),'invalid_product':q(F(1,100)),'residual_after_selected_prefix':q(res)}}
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'PASS','matrix_law_cases':len(rows),'normalizer_negative_TV':negative['case']['TV'],'family_dimensions':[x['n'] for x in families],'CP1_atoms':len(atoms)}))
