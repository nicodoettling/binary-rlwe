"""Independent exact selected-functional controls; see preregistration."""
import itertools,json,resource
from collections import defaultdict
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
B=24;Rmax=2*B*B;alpha=F(15,16)
cube=list(itertools.product((0,1),repeat=2))
tail=4*31*alpha**((B+1)**2)/(1-alpha**(2*B+3))
families={
 'identity':lambda s:(s,),
 'coordinate0':lambda s:(s[0],),
 'selected_coordinates':lambda s:(s[0],s[1]),
 'constant':lambda s:(0,),
}
quotients={
 'Z2':lambda z:(0,),
 'even_sum':lambda z:((z[0]+z[1])%2,),
 'even_first':lambda z:(z[0]%2,),
 '2Z2':lambda z:(z[0]%2,z[1]%2),
}
weight_cache={r:15**r*16**(Rmax-r) for r in range(Rmax+1)}
rows=[];values={}
for jname,coset in quotients.items():
 lattice=[(g,weight_cache[g[0]**2+g[1]**2]) for g in itertools.product(range(-B,B+1),repeat=2) if coset(g)==coset((0,0))]
 Z=sum(w for _,w in lattice)
 for fname,funcs in families.items():
  residue=defaultdict(lambda:defaultdict(int))
  for s in cube:
   for j,v in enumerate(funcs(s)):residue[coset(s)][j,v]+=1
  K=F(sum(max(d.values()) for d in residue.values()),4)
  observations=defaultdict(lambda:defaultdict(int))
  for s in cube:
   for g,w in lattice:
    y=(s[0]+g[0],s[1]+g[1])
    for j,v in enumerate(funcs(s)):observations[y][j,v]+=w
  selected=F(sum(max(d.values()) for d in observations.values()),4*Z)
  assert selected>=K,(jname,fname,'lower')
  if K<1:assert selected+tail<=K*F(43,28),(jname,fname,'upper')
  else:assert selected==1
  values[jname,fname]=selected
  rows.append({'J':jname,'functions':fname,'K':str(K),'selected_probability_approx':float(selected),'selected_probability_exact':str(selected),'upper_K_times_43_28':str(min(F(1),K*F(43,28))),'observations':len(observations),'lattice_points':len(lattice)})
assert values['Z2','selected_coordinates']>values['Z2','coordinate0']
print(json.dumps({'test':'DD1-SFUNC-FV1','status':'PASS','cases':len(rows),'tail_upper_approx':float(tail),'tail_upper_exact':str(tail),'max_before_sum_strict_control':True,'rows':rows},indent=2))
