import json,itertools,time,resource,signal
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
signal.alarm(30)
start=time.monotonic()
queries=('x','e0','e1','f0','f1')
traces=[('A0',('e0','f0'),F(21,2200)),('A1',('e1','f1'),F(21,2200)),('C0',('e0','x'),F(1,11)),('C1',('e1','x'),F(1,11)),('D',(),F(879,1100))]
atoms=[]
for vals in itertools.product(range(2),repeat=5):
 H=dict(zip(queries,vals))
 for name,trace,mass in traces:
  vk=(not name.startswith('C')) or H['x']==int(name[1])
  if vk: atoms.append((H,name,trace,mass/F(32)))
Z=sum(x[3] for x in atoms)
assert Z==F(10,11)
post=[(H,name,trace,mass/Z) for H,name,trace,mass in atoms]
branch={name:sum(w for H,t,tr,w in post if t==name) for name,_,_ in traces}
inc={x:sum(w for H,t,tr,w in post if x in tr) for x in queries}
first=sum(w for H,t,tr,w in post if 'e'+str(H['x']) in tr)
both=sum(w for H,t,tr,w in post if tr==('e'+str(H['x']),'f'+str(H['x'])))
assert branch=={'A0':F(21,2000),'A1':F(21,2000),'C0':F(1,20),'C1':F(1,20),'D':F(879,1000)}
assert max(inc.values())==F(1,10)
assert first==F(221,2000) and both==F(21,2000)>F(1,100)
assert both/first==F(21,221)<F(1,10)
out={'model':'All32 independent binary oracle tables crossed with5 exact trace branches; condition vk=1 explicitly','input_atoms':160,'retained_atoms':len(atoms),'normalizer':str(Z),'posterior':{k:str(v) for k,v in branch.items()},'incidences':{k:str(v) for k,v in inc.items()},'first_selected_hit':str(first),'matching_both_hits':str(both),'false_product':'1/100','later_conditional':str(both/first),'result':'REJECT_OLD_PRODUCT','failure':'Selection removes support; cached-prefix Bayes renormalization changes branch mass. Latent cache-hit status is not observed filtration.','theta_scope':'D-THETA conditions on original ellipse before observations and uses complete iid pair law there; its uniform comparator counting is genuinely product. No selected-stage lightness product.','precision':'exact Fraction and integer enumeration; seed none','resources':{'wall_seconds':time.monotonic()-start,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'wall_limit_seconds':30,'address_space_bytes':268435456}}
print(json.dumps(out,indent=2))
