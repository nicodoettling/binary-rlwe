# Candidate A, version A1 — rich supports with discrete completion

Disposition at initial gate: **develop with extraction and source hardness unresolved**. No source-supported binary-RLWE theorem is claimed. Author components: F02 completion, F03 source interface; coordinator specification below. Evidence awaits fresh nonauthor review.

For power-of-two n let ell=ceil(log2 n), d=max(1,floor(n/ell^3)), gamma=tau=ell, b=ell^2 and sigma=2n ell^3. Require an odd prime q=1 mod 2n with sigma n^c<=q<=n^K for fixed positive c,K. Parameters are public. The statement is along qualifying split-prime sequences; no prime-generation result is asserted here.

Sampler, with no binary secret input:

1. Sample T uniformly among all d-subsets of the n CRT roots. Let J be the ideal vanishing on T, and I=Ann(J), supported on T.
2. Sample U directly with independent uniform nonzero active CRT coordinates and zeros elsewhere. Sample V independently with uniform active field coordinates, zeros elsewhere. The quotient and I both have dimension d; multiplication by U is a bijection between them.
3. Independently sample iid coefficient F_j from D_gamma conditioned on |F_j|<=b. The actual finite-precision version remains in this coefficient box. Its exact law and approximation budget are part of this source assumption.
4. Form the integer negacyclic matrix M_F and B=sigma^2 I-tau^2 M_F M_F^T. Draw H=H_impl using the adaptive LDL discrete-Gaussian kernels and explicit tail/precision policy of foundations/F02-completion.md, with fresh coins. This source algorithm uses F and public widths, never the reduction's G or S.
5. Publish only (A,C)=(U+F,V+H) mod q. The source comparison is with two independent uniform elements of R_q.

Since ||M_F||<=nb, B>=3sigma^2 I/4. The completed error F G+H, for independent G~D_tau^n, is within delta/(1-delta)+eta_seq+eta_impl of wrapped iid D_sigma, jointly with J,U,F and integrating H, where delta<=(1+kappa(3ell^2/4))^n-1 and kappa(s)=2 sum_(j>=1)exp(-pi s j^2). These errors are negligible under the written sampler proof. Exact discrete covariance is not claimed to equal its exponent matrix. This is a noise feasibility result only.

The public reduction samples Y=S0+G0 using a fresh coefficient-binary S0 and independent D_tau^n G0. For extraction the mathematical Y=S+G uses that same public G law. Source independence means a valid bound jointly with (J,Y) extends to (J,U,F,H,Y). The required extraction bound for random T is still OPEN; the exact moment to bound is in foundations/coordinator-extraction-gate.md.

Actual entropy records: log2 binom(n,d) support bits, d log2(q-1) bits for U, d log2 q for V; F has at most n log2(2b+1) bits and actual per-coordinate entropy of its conditioned DG law. S supplies exactly n bits before Y. H is an explicitly generated correlated noise vector, not independent coefficient D_sigma; its exact sampler entropy and finite output support are not replaced by a marginal-width heuristic. F's untruncated Gaussian variant differs by a charged negligible tail; a Rademacher variant changes the exact source assumption even though the same completion proof applies.

Known attacks: binomial control is polynomially distinguishable; arbitrary supports admit the provisional grouped-super-support attack in F03-attacks.md under q^(1-d/r)>=8n^(1+epsilon)b, with runtime exp(O(r/epsilon)) for r=Theta(d). This is polynomial at d=O(log n) and superpolynomial at the initial d. Exact support/noise enumeration and short-multiplier/pair-combination attacks remain relevant. None of their current bounds proves hardness when they are superpolynomial.

Unresolved dependencies: joint extractor X0 at the same tau,d,q; exact correlated source assumption P0; any matching multiple-sample source and full joint noise law. A conditional bridge assuming P0 does not support P0. A comparison with independent-noise HLBDD does not establish this F-conditioned kernel's hardness.
