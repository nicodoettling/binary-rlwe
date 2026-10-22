from fractions import Fraction as F
from itertools import product
import json
count=0
for N in [2,3,4]:
 for alpha in product([F(0),F(1,4),F(1,2),F(1)],repeat=N):
  a=sum(alpha)/N
  if not a:continue
  for R in range(1,6):
   masses=[sum((1-a)**j*alpha[s]/N for j in range(R)) for s in range(N)]
   den=1-(1-a)**R
   assert sum(masses)==den
   assert all(masses[s]/den==alpha[s]/(N*a) for s in range(N))
   assert max(masses)/den<=F(1,N)/a
   count+=1
assert F(21,2000)>F(1,100)
print(json.dumps({'status':'PASS','cases':count,'precision':'exact Fraction','tails':'none','scope':'finite fresh rejection law and density ratio, not distinguisher/calibration asymptotics','CP1_negative':True},indent=2))
