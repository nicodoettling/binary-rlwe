# C01 blind-to-author-proof check, frozen 2026-09-06 15:39 UTC

This report was saved before opening F01.md, D01.md, candidate A, the prime-regime note, compatibility note, canonical bridge, claims ledger or dependencies. It is blind to the proposed proofs, not to the required bridge contract, plan and complete shared counterexamples. Preserve this file unchanged during stage 2. This is bounded mathematical checking, with no allocated CPU experiment and no formal certification.

## Authorization and frozen inputs

Read the absolute active run manifest first. It records launch_authorized=true and deadline_supervisor_verified=true, run_id=brlwe-joint-ideal-20260906-astra-ultra, output_directory=/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-joint-ideal-20260906-astra-ultra, start_utc=2026-09-06T14:21:13.181175+00:00 and hard_deadline_utc=2026-09-06T19:21:13.181175+00:00. Checked every phase deadline against its launch-relative offset; workers_stop is 19:06:13.181175 UTC. This assignment ends earlier at 16:15 UTC, with research stop at 16:10. Model policy is Astra ultra; no workers, continuation, goals or experiments were started.

The theorem packets under snapshots/review-v1 are:

- foundations/F01-theorem-v1.md, SHA256 e8b8218ca2bb2d851b6068b4456983739cf5188bd4f12c49d880054064068852.
- development/D01-theorem-v1.md, SHA256 83f76af8f9a8364dcef3937df0ca0bf70c7745f8c5ab78e65e8cc823d7a2f3df.

Also read REVIEW_INSTRUCTIONS.md, assignment.md, PLAN.md, BRIDGE_CONTRACT.md, TASK_TEMPLATE.md, run-config.json, known-counterexamples.md in full, and the mathematical-proof-audit skill with both mandatory protocol references.

## Independent reconstruction of the bridge

Write Gamma=(J,U,F,H), and sample S,G independently of Gamma and each other. Noise comparison may adjoin independent S to (J,U,F,FG+H), then apply the map (J,U,F,S,e) -> (U+F,(U+F)S+e). It must average H; attempting to retain H here would impose an unnecessary stronger assumption. The resulting second coordinate is US+FY+H.

Extraction retains Gamma,Y and therefore permits replacing U*S by the well-defined image U*Z. Put K=Z-pi_J(Y). Conditional on Gamma,Y, K is uniform in R/J. If multiplication by U is bijective, V'=U*K is uniform in I_J with a law depending only on J. Thus V' is conditionally independent of Gamma,Y given J, and the transcript equals (A,A*Y+C), where (A,C) has the specified source law and Y is independent. This is the required independence argument; no hidden quotient or completion algorithm enters the test.

B1 uses fresh public S,E and discards c. Its two challenge endpoints are exactly target versus the first altered multiplier law. B2 uses fresh public S0,G0, so Y has the right public marginal without latent source information. On a uniform pair, (a,aY+c) is uniform for every fixed Y. These are two potentially different tests against the same pair assumption. The triangle bound with the sum of their two source advantages and eta_noise+eta_ext follows. It does not establish that source assumption.

Without bijectivity, V' is uniform on UR; its exact TV from uniform I is 1-|UR|/|I|. Averaging this conditional discrepancy yields eta_iso. Conditioning the source U instead changes the source law and cannot be silently substituted.

Implementation accounting is consistent: source-law replacement can affect both source endpoints, yielding 2 xi_src; B1's S,E sampler affects both its uniform and source endpoints, yielding 2 xi_1. B2's uniform endpoint remains exactly uniform for every independent implemented Y, so only xi_2 is needed. An altered target contributes xi_tgt.

## Exact finite controls

1. Equal marginals: (A,C)=(a,a), with a uniform in a finite ring, has uniform marginals but pair equality probability one; the independent-pair equality probability is 1/|R|. A two-endpoint argument cannot replace source-pair hardness by marginal hardness.
2. Hidden auxiliary dependence: allowing G to depend on source coins, for example storing G among them and setting H=E-FG, defeats the public Y sampler. It violates this packet's actual independence premise and is correctly excluded.
3. Retained H: extraction ignoring H need not survive if H reveals S. The packet both retains H in extraction and requires Gamma independent of S,G. It does not confuse this with the weaker noise comparison that drops H.
4. Nonunit U: in R=F_q^d, setting one active coordinate of U to zero makes UR a proper subgroup of index q. The conditional distance is 1-1/q, agreeing with eta_iso rather than a negligible blanket estimate.
5. Shared K: applying the construction twice gives V_i=U_i K. Nonzero active coordinates satisfy V_1/U_1=V_2/U_2; this is not the fresh-independent ideal-point law. Nothing in the one-sample packet removes this obstruction.
6. One-sample self-verification: in the uniform game, acceptance implies existence of a binary s with b-a*s in T. A union bound over 2^n s gives at most 2^n |T|/|R| even for an adaptive Rec. In the planted game, exact recovery and E in T intersect with probability at least epsilon_rec-delta_T; multiplication would be unjustified. This does not require a held-out sample. Held-out verification instead consumes m+ell samples and uses fresh conditional independence.
7. The imported CP-1 example gives 0.0105>0.01 through posterior support removal. No step above multiplies selected-stage marginal bounds. Fixed independent coefficient factorization below is a different claim.

## Independent extraction calculation

For a scalar wrapped auxiliary law W, Y has mass (W(y)+W(y-1))/2, and the posterior bit has p_y=W(y-1)/(W(y)+W(y-1)). Draw S,S' independently conditional on the same Y. Their difference has mass beta/4 at each sign and 1-beta/2 at zero, where beta=4 E p_Y(1-p_Y). Independent coefficient laws of Y imply an exact product ternary law after averaging. No original-law versus posterior-law swap is used.

For a fixed support T, normalized averaged posterior collision is q^d Pr[Delta(r)=0 for all r in T]. For uniform T this is q^d E[binom(z(Delta),d)/binom(n,d)], including Delta=0. Cauchy-Schwarz on each output fiber followed by Jensen yields the claimed one-half square-root bound; its inside quantity is nonnegative because every posterior collision is at least q^-d. The finite formula is consistent.

An independent lower bound for beta is useful: beta=2 sum_y W(y)W(y-1)/(W(y)+W(y-1)) >= sum_y min(W(y),W(y-1)) = 1-TV(W,W shifted by one). Wrapping contracts TV. For an integer centered unimodal discrete Gaussian the shift-TV equals its mass at zero, at most 1/ell using the Gaussian Poisson sum. Thus beta>=1-1/ell, so a fixed rho is available for large n. The squared ternary norm is 1-beta+3 beta^2/8. Controls: W concentrated at zero gives beta=0 and no claimed mixing; uniform W gives beta=1, the ordinary difference of two fair bits.

Sign pair test: for roots r,-r, the evaluations are E(r^2)+r O(r^2) and E(r^2)-r O(r^2), where even and odd coefficient polynomials are independent. Since q is odd, the linear transformation is invertible; no deterministic equal-coordinate law follows. Inverse roots similarly create correlations, not equality. A theorem for the full tuple is required. Distinct nonzero roots meet the genericity condition in the imported joint theorem; neither sign nor inverse pairs are excluded there. Small n examples whose Boolean image is too short do not meet the asymptotic degree gates.

## Primary-source and asymptotic checks made while blind

Directly opened Breuillard--Varju arXiv:1810.13360v2 Section 5, especially its setup, Definition 22 and Proposition 23, and Voutier arXiv:1211.3110 Corollary 2. The former statement is unconditional and applies to arbitrary subsets of admissible generic tuples, including a singleton. These checks did not use its RH-dependent irreducibility conclusions. Sources: https://arxiv.org/pdf/1810.13360v2 and https://arxiv.org/pdf/1211.3110.

My substitution is M=1, V=F_q^d, D=d, Q=q and walk index n-1. The logarithmic size is Lambda=d log q, not log q. The absolute sum error becomes q^d/(n)_d times that error after averaging ordered distinct root tuples and normalizing collision; a singleton instead costs q^d. The packet states these factors correctly.

To certify all roots, choose kappa of order (log n)^-3, small enough relative to the maximum degree L=floor(3 Lambda). An integer polynomial of Mahler measure below 2 has unit content. Every nonzero noncyclotomic irreducible factor of degree >=2 has logarithmic Mahler measure >2/(log(3L))^3 by Voutier; a degree-one noncyclotomic primitive factor has measure >=2. Thus small-measure polynomials factor into powers of X and cyclotomic factors. Every root r of X^n+1 has exact order 2n. If a cyclotomic index is q^a s with q not dividing s, its reduction has roots of order s, even when a>0. Therefore it could vanish at r only for s=2n, forcing its degree phi(2n q^a)>=n. When L<n, no such polynomial vanishes. This handles integer content and indices divisible by q, rather than assuming all cyclotomic indices are coprime to q.

Put t=log n. Uniformly for q<=n^K, the duration gate is bounded by O_K(d^2 t^7). At d<=sqrt(n)/t^4 it is O_K(n/t)=o(n). The normalized error exponent is at least c_K n/(d t^6), before paying log(q^d)<=Kdt. Their ratio is at least a constant times n/(d^2 t^7)>=t; hence the positive normalization term can be absorbed eventually. This gives TV at most one-half exp(-c'_K n/(d t^6)), as asserted after adjusting constants. Also L=O_K(d t)=o(n), while Lambda/(log Lambda)^3 tends to infinity, so the remaining admissibility gates hold. The worst displayed exponent is of order sqrt(n)/t^2 and is negligible. The lower d bound ensures no bounded-dimensional edge branch is accidentally used. The range is eventually nonempty.

## Blind disposition and pending stage 2

No counterexample to the stated conditional bridge or joint-extraction packet was found by these exact hand checks. Provisional assessment: the bridge is valid with its explicit samplers and statistical premises; the extractor has a viable direct derivation using the actual joint Proposition 23. Source hardness is not proved by either statement. There is no independent multiple-sample result here.

Stage 2 must check the actual author versions, all hashes/claim dependencies, the exact choice of kappa and every finite gate, prime existence and samplability, candidate-A retained-variable laws, and whether canonical summaries overstate the conditional result. The Gaussian completion proof itself is assigned to C03; this critic will audit its interface only.
