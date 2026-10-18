import itertools,json,resource,time
from collections import Counter
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t0=time.monotonic();q=17;n=1;r=2
zs=[(0,0),(1,0),(0,1),(1,1)];counts={z:Counter() for z in zs}
structured=0;zero=0;rank2=0
for a,b,c,d in itertools.product(range(q),repeat=4):
 for z in zs:counts[z][((z[0]*a+z[1]*c)%q,(z[0]*b+z[1]*d)%q)]+=1
 structured+=int(d==a and c==(-b)%q)
 zero+=int(a==b==c==d==0)
 rank2+=int((a*d-b*c)%q!=0)
assert structured==q*q and zero==1
for z in zs[1:]:assert len(counts[z])==q*q and set(counts[z].values())=={q*q}
assert counts[(0,0)]=={(0,0):q**4}
# The n1 tower is R=F17 with X=-1, S=F17[Y]/(Y²+1).
# Both roots4,13 exist. Row-oriented multiplication has C(A)=[[a0,a1],[-a1,a0]].
product_checks=0
for a0,a1,z0,z1 in itertools.product(range(q),repeat=4):
 actual=((a0*z0-a1*z1)%q,(a1*z0+a0*z1)%q)
 row=((z0*a0+z1*(-a1))%q,(z0*a1+z1*a0)%q)
 assert actual==row;product_checks+=1
print(json.dumps({'input':{'n':n,'r':r,'q':q,'k':2,'U':'identity2','seed':None,'scope':'scalar-base algebra surrogate; not n>=2 hardness family'},'precision':'exact integer counts','W_states':q**4,'product_orientation_checks':product_checks,'nonzero_binary_z_rows':3,'image_size_for_each_nonzero_z':q*q,'fiber_size_for_each_nonzero_z':q*q,'zero_binary_z_probability':'1/4','structured_residual_count':structured,'structured_residual_probability':'1/289','zero_residual_count':zero,'zero_residual_probability':'1/83521','rank2_matrix_count':rank2,'elapsed_seconds':time.monotonic()-t0,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2,sort_keys=True))
