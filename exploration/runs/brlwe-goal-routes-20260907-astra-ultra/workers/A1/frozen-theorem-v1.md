# A1-T0 — frozen direct-search statement, version 1

Frozen before proof at 2026-09-07, worker A1. Status PROVISIONAL; depends on the exact completion premise below. Intended m is 1 or 2, with the source budget fixed accordingly. This is a formal conditional reduction and does not assume source hardness is proved in literature.

Let R be a finite effectively represented commutative ring, and let S have a fixed efficiently samplable law P_S on R. Draw C=(J,U_1,...,U_m,F_1,...,F_m) from a specified law mu, with J an ideal, U_i in Ann(J), and |R/J|<=L. The entire tuple C is jointly independent of independent S~P_S and G~P_G. Define Y=S+G. Conditional on C, draw proof-only H=(H_1,...,H_m) from a fixed kernel K_C independently of (S,G). Let E=(E_1,...,E_m) have a fixed public law P_E jointly independent of C,S,G,H. No H sampler is provided to the reduction. Assume precisely

  TV((C,(F_i G+H_i)_{i=1}^m),(C,E)) <= eta_N.             (A1-N0)

H and G are integrated out on the first side; neither is retained in this comparison. Define planted responses B_i=(U_i+F_i)S+E_i. Target public first elements a_i are independent uniform R, independent of S and E. The target solver Q sees only ((a_i,a_i S+E_i))_i and outputs one element of R. Its success epsilon is exact equality to S. Algorithmic coins are independent of all challenge variables.

Computational source worlds consist of exactly one challenge tuple:

  Src_m: (A_1,...,A_m)=(U_1+F_1,...,U_m+F_m),
  Unif_m: m independent uniform R elements.

For m=1 this can be the first marginal of a two-element source challenge; the unused second element remains part of that source experiment. For m=2 these are the actual two independent noised ideal points sharing one hidden ideal. Conditional independence between source elements is unnecessary for the abstract inequality, but is specified explicitly for the intended source instantiation. No fresh source oracle or common-K source sampler is assumed.

Define the source test T: receive its one challenge tuple (a_i), sample own S and E independently, call Q on ((a_i,a_i S+E_i))_i, and accept iff the returned element equals this sampled S. Claim to prove/refute:

  P_guess(S | ((U_i+F_i,B_i))_i) <= L P_guess(S|Y)+eta_N;
  epsilon <= Adv_Src(T)+L P_guess(S|Y)+eta_N.             (A1-T0)

Here source advantage is the absolute acceptance-probability gap, not target decision advantage. The promised reduction is uniform, uses one challenge and one Q invocation, and costs T_Q+T_S+T_E+m(T_mult+T_add)+T_equal; all samplers must have explicit finite precision costs. Statistical input, target, and sampler errors will be charged by total variation, with exact coefficients stated in the proof.

Intended coefficient binary specialization: R=F_q[X]/(X^n+1), n a growing power of two, odd prime q polynomially bounded, S uniform in {0,1}^n, G iid integer D_tau reduced mod q. Then

  P_guess(S|Y) <= ((1+D_tau(0))/2)^n.

With source masks |(F_i)_j|<=b, stack the integer negacyclic multiplication matrices M_i vertically into M in Z^(mn by n), set sigma_m=2 sqrt(m) n b tau and B=sigma_m^2 I_(mn)-tau^2 MM^t. The intended E has independent iid coefficient D_sigma_m errors in every sample. Exact H~D_B exists only inside the proof. The rectangular completion identity, dimensions, normalization, and all finite smoothing guards must be checked before asserting (A1-N0).

Asymptotic target: fixed m in {1,2}, ell=ceil(log2 n), tau=ell, source F_i iid D_ell conditioned coefficientwise to [-ell^2,ell^2], b=ell^2, sigma_m=2 sqrt(m)n ell^3; quotient cardinality L=q^D, with D ln q <= (ln 2-delta)n for fixed delta>0. Seek q/sigma_m>=n^c for fixed c>0 and q<=n^K for fixed K chosen before solver. Source law uses uniform hidden rich CRT support of size D in fully split R, and U_1,U_2 independently uniform in its supported ideal. No active-U conditioning, quotient-uniformity, or extractor premise is allowed.

Intended source comparison: the independently defined equal-small-noise pair (U_1+F_1^infty,U_2+F_2^infty), F_i^infty iid D_ell, versus uniform pair. Its m=1 use ignores the second component; its m=2 use takes both. Conditioning the relevant m masks on the box incurs delta_F,m, and no actual second component is reinterpreted as H. Expected implementation inequality: epsilon_actual <= Adv_actual-source(T_impl)+L P_guess(S|Y)+eta_N+delta_F,m+xi_source+2xi_alg+xi_target, with every xi referring to a specified full joint law.

Boundary cases to test: degenerate U=0; arbitrary nonuniform quotient of binary S; S-dependent H (must violate premise); Gaussian marginals with S-dependent target E (must violate full product law); same common G across two samples (must use full stacked H); quotient size 1 and |R|; degenerate b=0 handled separately or excluded from sigma formula. No tensorization across samples is asserted. The product over secret coordinates is permitted only after proving their full joint independence.
