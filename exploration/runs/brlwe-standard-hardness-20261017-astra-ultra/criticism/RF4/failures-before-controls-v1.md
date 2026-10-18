# RF4 preserved failures before finite controls

No counterexample to frozen F-QFINITE v2 is claimed here. These exact controls reject nearby invalid arguments before checking the proposed replacement.

## RF4-PERIOD-NEG1: small preperiodization squared tail is insufficient

Let one retained basis vector have amplitude 1 in residue0. Let N distinct omitted basis vectors, all in residue1, each have amplitude 1/N. The preperiodization squared norm is Z=1+1/N and the omitted probability is 1/(N+1), tending to zero. Periodization yields F=(1,1), whereas retained periodization is G=(1,0). The squared normalized overlap is exactly1/2 for every N. Thus an error bound tending to zero with only the preperiodization squared tail is false. The exact cross-term ratio is C=||F||²/Z-1=(N-1)/(N+1), which does not tend to zero. The proposed v2 lemma keeps C and does not make the false inference. This finite fixture is an algebraic control, not a Gaussian/lattice counterexample.

## RF4-RETRY-NEG1: unequal phase success probabilities must be retained

With c0=1/2, take c1=1/2 in one preparation and c1=1/4 in another. Single-attempt probabilities are1/4 and5/32. A one-attempt joint success probability is5/128, not1/16. Conditional resource states differ as well: their squared bit probabilities are respectively(1/2,1/2) and(4/5,1/5). A replacement by a phase-independent acceptance probability is invalid. Frozen v2 uses only a uniform lower bound and retains each actual normalized state.

## CP-1, exact old product failure

Prior masses A_0=A_1=21/2200, C_0=C_1=1/11, D=879/1100; oracle x,e0,e1,f0,f1 has independent fair bits. C_b accepts key generation only when H(x)=b. Conditioned on vk=1, masses are A_b=21/2000, C_b=1/20, D=879/1000. At gamma=1/10 all incidences are light (x exactly1/10, e_b=121/2000, f_b=21/2000). The matched two-hit probability is21/2000>1/100, and the subsequent selected residual incidence is21/221<1/10. The support removed by the first selected event changes the normalizer. Independent fresh whole preparations and complete-channel comparisons in v2 do not assert this false marginal product bound.
