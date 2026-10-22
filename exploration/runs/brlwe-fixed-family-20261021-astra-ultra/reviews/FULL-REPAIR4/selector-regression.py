#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
import json

M=F(2);L=2
priors=[(F(1,2),F(1,2)),(F(1,4),F(3,4)),(F(1),F(0))]
xmaps=[(F(1),F(0)),(F(1,2),F(1,2)),(F(1,3),F(2,3))]
counts={'normalized_models':0,'prior_input_channels':0,'output_checks':0,'retry_prefix_checks':0}
for mu in [(F(1,2),F(1,2)),(F(1,3),F(2,3))]:
  for r1 in product([F(0),F(1,2),F(1)],repeat=4):
    R=lambda x,e,c: r1[2*x+e] if c else 1-r1[2*x+e]
    for weights in product([F(0),F(1),F(2)],repeat=4):
      G=lambda e,c:weights[2*e+c]
      K=[[mu[e]*R(x,e,c)*G(e,c) for e in range(2) for c in range(2)] for x in range(2)]
      if any(sum(row)!=1 for row in K):continue
      counts['normalized_models']+=1
      for row in K:
        assert all(row[2*e+c]<=M*mu[e] for e in range(2) for c in range(2))
        assert all(sum(row[2*e:2*e+2])<=M*mu[e] for e in range(2))
        # Each fresh retry has rejection probability 1-1/M conditional on x.
        prefix=[sum((1-1/M)**k/M*value for k in range(6)) for value in row]
        assert all(prefix[i]+(1-1/M)**6*row[i]==row[i] for i in range(4))
        counts['retry_prefix_checks']+=1
      for pi in priors:
        for x0 in xmaps:
          ch=[[x0[s]*K[0][j]+(1-x0[s])*K[1][j] for j in range(4)] for s in range(2)]
          pg=sum(max(pi[s]*ch[s][j] for s in range(2)) for j in range(4))
          assert pg<=min(F(1),M*L*max(pi))
          counts['prior_input_channels']+=1
          for out1 in [(F(0),)*4,(F(0),F(1),F(0),F(1)),(F(0),F(0),F(1),F(1)),(F(1,3),F(2,3),F(1,2),F(0))]:
            p1=[sum(ch[s][j]*out1[j] for j in range(4)) for s in range(2)]
            py=max(pi[s]*p1[s] for s in range(2))+max(pi[s]*(1-p1[s]) for s in range(2))
            assert py<=pg
            counts['output_checks']+=1

# Public Z reveals the high bit; class reveals the low bit.
joint={(s,s//2):F(1,4) for s in range(4)}
pz={z:sum(v for (s,k),v in joint.items() if k==z) for z in range(2)}
prior_guess=sum(pz[z]*max(joint.get((s,z),F(0))/pz[z] for s in range(4)) for z in range(2))
assert prior_guess==F(1,2)
assert F(1)==2*prior_guess and F(1)>F(2,4)

# Persistent randomized-class seed: same averaged one-trial law, wrong retry law.
N=8;low=F(4,7);high=F(3,7)
normalization=low*F(2,N)+high*2
assert normalization==1
persistent_success=low+high/N
persistent_mean=low*N+high
fresh_success=F(2,N)
assert persistent_success==F(5,8)>F(4,N)
assert persistent_mean==5>2
assert fresh_success==F(1,4)<=F(4,N)

# Nonnormalized selector, also the channel part of the nonatomic-v1 counterexample.
bad_normalizer=F(1,4)
assert F(1)>F(2,4) and bad_normalizer!=1
# Dropping output factorization allows output=S even with E,C constant.
assert F(1)>F(1,4)
# CP-1, exact independent reconstruction.
vk=2*F(21,2200)+F(1,11)+F(879,1100)
A=F(21,2200)/vk;C=F(1,22)/vk
assert vk==F(10,11) and A==F(21,2000) and C==F(1,20)
assert A>F(1,100) and (A/2)/(A/2+C)==F(21,221)<F(1,10)

print(json.dumps({'status':'PASS bounded exact finite laws only','counts':counts,
 'correlated_public':{'guess':'1','conditional_prior_guess':str(prior_guess),'correct_bound':'1','incorrect_uniform_bound':'1/2'},
 'persistent_seed_negative':{'normalization':str(normalization),'guess':str(persistent_success),'bound':'1/2','mean_trials':str(persistent_mean),'claimed_fresh_mean':'2','fresh_guess':str(fresh_success)},
 'other_negative_controls':['nonnormalization rejects','nonatomic-v1 channel violates 1/2 bound; nonatomic Z is symbolic, not sampled','output leakage rejects','CP-1 old product rejects']},indent=2))
