# W2 checkpoint — 2026-09-06 20:08 UTC

Canonical agent: `/root/w2_structure`. Session/thread UUID is not exposed in the available tool/context interface; none is invented.

Status: core mathematical packet and applicable full controls read; load-bearing bytes hashed in input-hashes.json. New claims remain PROVISIONAL. No experiment started and no content-policy interruption encountered. The `python` executable was absent; the installed `python3` works. This was an ordinary local command error, not a policy interruption.

The source is exactly A2 from target.md: uniform d-subset T, active-nonzero U on T, independent uniform V in I(T), truncated coefficient F, and H_seq conditional F. Corrected ATT-v3 is a deterministic exp(O_c(d))*poly(n,log q) first-component test, not a polynomial refutation at the frozen d. Generic root input and strict rounding must be retained.

Provisional deductions selected for full write-up:

1. W2-ORB-v1: random-support ATT can use r equal root orbits without r>=2d. If E is the empty-orbit count, mu=r*C(n-n/r,d)/C(n,d) and Var(E)<=mu. Enumerating root-zero unions of size >=alpha*n, with strict q^alpha>2nb, succeeds whenever E>=alpha*r. At r=Theta(d), mu/r approaches exp(-d/r). This improves admissible constants but not the exp(Theta(d)) scale.
2. W2-COVER-v1: for any fixed zero set Omega of size >=alpha*n, random T avoids it with probability <=(1-alpha)^d. There are at most n^ell subgroups of the n-element Galois group and at most 2^r unions for subgroup index r. Thus all low-index r<=rmax=o(d) subgroup-union branches combined have valid-branch probability <=n^ell*2^rmax*(1-alpha)^d=exp(-Omega(d)) at A2. This is a method-scope coverage bound, not general computational hardness.
3. W2-SCAL-v1: exact active ratios V_i/U_i are iid uniform F_q. Across every scalar combination C-tA, the number of ideal-coordinate cancellations is the largest multiplicity among d ratios. Probability any t cancels >=k coordinates is <=C(d,k)q^(1-k). Thus even omniscient scalar choice cannot remove a positive fraction of d except with negligible probability. H_seq conditional F is retained; no covariance approximation is used.
4. W2-PV-v1: an active first-component decoder gives a solver for separately defined average-case known-support PV-Knap by filling unknown CRT coordinates uniformly. The simulator is unconditioned U, but exact conditioning on all active coordinates nonzero yields recovery success >=(1-1/q)^d*epsilon. This is only a one-way SEARCH reduction, not decisional support for P0.

Next: exact finite occupancy and scalar-ratio controls in W2-E (timeout <=120 seconds), full proof and explicit strongest objections. Deadline 21:19:15 UTC; stop research for writing by 21:14:15.
