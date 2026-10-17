# Exact inherited ATT and source scope

These are reconstruction notes, not a new review or certification. Authoritative local inputs read:

- ../../brlwe-joint-ideal-20260906-astra-ultra/corrections/ATT-v3.md (from the run root, use the full path named in assignment.md).
- That run's criticism/C01/ATT-recheck.md, including exact solver policy, input correction and finite controls.
- brlwe-goal-routes-20260907-astra-ultra/criticism/RS1/report-v1.md, especially Section 5's current source specialization and qualifiers.
- That run's final.md and reconciliation.md; the joint-foundations inputs/frozen/W2-final-v1-note.md; consolidated joint-ideal record and the additive-completion regression.

The generic ATT-v3 finite theorem requires n power of two, odd completely split prime q, integer coefficient box radius b>=1, public CRT roots, and a power-of-two r dividing n with 2d<=r<=n and strict q^(1-d/r)>2nb. Its deterministic algorithm uses only A_1. It enumerates subgroup-orbit supersupports, forms complementary integral ideals, uses deterministic exact SVP on rank<=r fixed-field lattices, lifts a nonzero inverse-ideal vector, performs exact rational dual rounding, and verifies. It accepts every planted first component with support<=d and error in the box. Uniform acceptance is at most min(1,2^r(2b+1)^n/q^(n(1-d/r))). Runtime exp(O(r))*poly(n,log q,log b), exponential memory allowed; no concrete implementation or bit-security claim.

The public-root input repairs the generic deterministic root-setup gap. At current q<=n^16, exhaustive root generation is polynomial in n, so no separate oracle is needed. The exact C01 recheck accepts this explicit deterministic policy and its corrected input; it does not assign success to the earlier unspecified randomized solver. RS1 retains that version-specific reviewed scope while the old run's broader status is provisional.

For current q>=2n^3+1 and b=ell^2, choose r the least power of two >=2d. Then r<4d, and q^(1-d/r)>=sqrt(q)>sqrt(2)n^(3/2)>2nell^2 eventually. Thus the optimized archived comparison already uses 2d, not the earlier conservative C0=8. Its source tail is at most n exp(-pi ell^2)/(pi ell); its uniform false acceptance is exp(-Omega(n log n)). At d=O(log n) its runtime is polynomial. At both displayed growing d families it is superpolynomial and subexponential as an upper bound. This is no proof of computational hardness there.

SC-v1 uses two independent uniform ideal points, with zero active values allowed, and two independent coefficient D_ell errors, all conditional on the same one T. The earlier W2 source instead had an active first point and a correlated second Gaussian kernel. Its scalar ratio calculation cannot silently replace the SC-v1 source. The present work conditions only on SC-v1. Neither Base_m nor resampling, hidden bases, support witnesses or completion samplers are available to algorithms.

Historical obstructions retained: strict rounding/injection/root gates; small fixed-field coverage only for its specific branch family; covariance and pairwise independence do not prove full laws; latent separation may disappear under projection; fixed-character bias does not prove pseudorandomness; ratio conditioning changes law; singleton/binomial attacks and their failures are existing work. The present proposed short joint-relation obstruction is distinct from the old scalar shear and ATT zero-set branch classes, but remains a restricted method result.
