import itertools,json,time,resource
from fractions import Fraction
from collections import defaultdict
start=time.monotonic()
S=list(itertools.product((0,1),repeat=2));G=S;E=list(itertools.product((-1,0,1),repeat=2))
yweights=defaultdict(lambda:defaultdict(int));yhweights=defaultdict(lambda:defaultdict(int));total=0;atoms=0;bad=[]
for s,g,e in itertools.product(S,G,E):
 w=(2 if e[0]==0 else 1)*(2 if e[1]==0 else 1);total+=w;atoms+=1
 y=tuple(s[i]+g[i] for i in range(2));h=tuple(Fraction(e[i])-Fraction(g[i],3) for i in range(2))
 yweights[y][s]+=w;yhweights[y,h][s]+=w
 residue=tuple((3*(Fraction(y[i],3)+h[i])).numerator%3 for i in range(2))
 if residue!=s:bad.append([s,g,e])
p_y=Fraction(sum(max(v.values()) for v in yweights.values()),total)
p_yh=Fraction(sum(max(v.values()) for v in yhweights.values()),total)
assert atoms==144 and total==256 and not bad and p_y==Fraction(9,16) and p_yh==1
print(json.dumps({'id':'ROOT-MASK-RESIDUE-1','atoms':atoms,'total_integer_weight':total,'p_guess_Y':str(p_y),'p_guess_Y_H':str(p_yh),'bad_residue_decodings':bad,'elapsed_seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'scope':'Finite support only, no full Gaussian or public-transcript attack certification'},indent=2))
