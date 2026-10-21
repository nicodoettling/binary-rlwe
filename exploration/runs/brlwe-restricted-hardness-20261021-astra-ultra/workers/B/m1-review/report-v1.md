# M1 nonauthor full-proof, source and complexity report, v1

Reviewer: worker B, same model and run lineage as author; correlated scrutiny, not statistical independence or formal verification. This is not the fresh-blind role. Verdict: no load-bearing mathematical defect found in M1 theorem-only-v1/proof-v1 under the specified global-zero fallback choice. Keep status PROVISIONAL until root reconciliation, fresh-blind and artifact gates. B-M1-FALLBACK-1 preserves one minor algorithm-selection ambiguity before correction.

## Frozen inputs and predecessor

Read complete M1 theorem-only-v1.md (SHA256320164e4e692ce801f2fde10a3deb7279629b9ff467bf4a155aa0828bba11845), proof-v1.md (dc52a6987a17f51d1996d561ba396404f64cd3852676e81735709f68c8d3c606), source-access-v1.md, complete finite-control-v1.py, finite-input/command/exit/resource/stdout/stderr records, and all80 finite output row summaries with their exact arithmetic representation retained. Read all160 CP1 atom records and all three explicit ideal-family matrices. The initial raw output was too large for one display; subsequent compact reads covered every matrix case and CP1 atom without deleting exact fractions from the input artifact. Full input hashes are in input-hashes-v1.sha256.

Also read historical workers/A/class-changing/small-index-simulation-v1.md and its finite-controls-report-v2.md plus the preserved finite-v1 failure record. M1 retains that predecessor's conditional-normalizer method, strengthens its collision-basis Gram–Schmidt bound, makes scalar sampling bounded with explicit costs, substitutes the final accepted width exactly, and adds the HNF/exponent criterion. It does not treat the old provisional banner as acceptance.

## 1. Exact sequential law and normalization

For the reverse basis sampler, every integer coordinate tuple maps bijectively to a lattice point. Successive orthogonal residual projections give product numerator rho_s(x) exactly. The denominators Z_i(c_i) depend on all earlier choices, and the proof retains them. Uniform shifted-theta bounds put each Z_i(c_i)/t_i in [1-eps,1+eps] on every actual history, including histories that would be rare or selected. Writing T=product t_i, the full unnormalized numerator bounds imply rho_s(J)/T lies in [(1-eps)^n,(1+eps)^n]. Consequently the actual normalized density ratio lies in [R^-1,R], R=((1+eps)/(1-eps))^n. This proves the displayed TV bound without multiplying marginal probabilities or pretending the denominators are constant.

For u>=1, the theta tail is at most4 exp(-pi u^2): use j^2>=1+3(j-1) and sum the geometric series. eps=eta/(32n)<=1/256; logR<=3n eps and exp(3eta/32)-1<=eta/8 for eta<=1/4. The proof's constants leave room for eta/2 scalar implementation error.

## 2. Finite scalar construction

All widths appear through rational squares. R=ceil(Kt) is computable by exact rational square comparisons, avoiding transcendental equality decisions. Reducing a rational center to integer offset plus c0 in[0,1) is exact. A uniform proposal over [-R,R+1] needs O(logR) random bits per bit-rejection attempt, even when R has exponential numerical value. The number of attempts is bounded by b and the number of proposals by T=1000K^2.

The proposal range contains at least t integers within distance t from c0. Their weights are at least exp(-pi)>1/24. Since N=2R+2<=(2K+4)t, acceptance is at least1/(144K), hence1/(200K). Thus exhaustion costs at most exp(-5K). The omitted Gaussian mass is at most4 exp(-pi(K-1)^2). One direct derivation bounds each omitted discrete tail by the corresponding integral starting one unit earlier and uses Z(t,c)>=t/2. The dyadic-acceptance and uniform-proposal-cap discrepancies each contribute at mostT2^(-b), uniformly in c0. The claimed total is below eta/(2n) with the stated conservative K,b.

A certified exponential interval of width2^(-b-2) can be converted to a dyadic acceptance probability within2^(-b) by rounding its midpoint to the nearest dyadic and clipping to[0,1]. This makes the prose implementation effective without exact equality decisions. All evaluated exponent magnitudes are O(K^2), because |z-c0|<=Kt+2 and t>=1. Ordinary rational Taylor/range reduction gives polynomial precision cost. The center's integer offset may be large but its bit length, rather than magnitude, is charged.

On any cap or exhaustion failure, choose global final-output zero. Continuing after scalar fallback0 would fail the theorem's literal fallback description; the proof already lists the global option, and B-M1-FALLBACK-1 records the alternative branch. The existing coupling/error charge covers global fallback without an extra loss.

## 3. Worst-case bit growth and normal-form source

Rational Gram–Schmidt has polynomial bit growth via determinant bounds. At each of n stages, the current center and chosen integer coefficient are formed from previous represented values using fixed rational basis/Gram–Schmidt data. Nonfailure output distances are bounded by the encoded proposal radii; global failure terminates. Bit length therefore grows by at most a polynomial input-size increment per stage, not by the numerical width. The loops have explicit K,T,b bounds on every tape. Reading/verifying any separately supplied u^2 should be charged in the complete input encoding; alternatively u may remain an analytic promise unused by the implementation. This is a bookkeeping clarification, since the sampler computes its own t_i^2 and never needs numerical u.

I independently verified the normal-form import at the primary SIAM abstract, as recorded in source-review-v1.md. It directly supports polynomial operation and intermediate bit bounds plus multiplier matrices. No full-text or GPV-source inspection is claimed. No hidden geometric lattice algorithm is imported.

## 4. HNF ordering, exponent and effective collision basis

For upper-triangular column HNF H in unchanged Euclidean coordinates, the first j columns span exactly the first j coordinate subspace, so b_j*=H_jj e_j. Because e e_j belongs to J and has zero coordinates beyond j, its coefficient on column j is e/H_jj, an integer; hence H_jj divides e. The largest Smith invariant equals the additive exponent. A lower-triangular matrix in the same column order would not justify the claim; the theorem explicitly fixes this issue. Simultaneous coordinate/basis reversal is an orthogonal permutation and preserves the centered Gaussian law when undone.

For the collision construction, D+1 binary vectors in h0=ceil(log2(D+1))<=n coordinates guarantee a nonzero ternary f. Its rotations form a nonsingular matrix V in the power-of-two field. M=V^-1 J contains Z^n. After clearing denominators, an upper column HNF yields a basis U of M with0<U_jj<=1. Because multiplication by upper-triangular U preserves each prefix span, (VU)_j*=U_jj v_j*, giving maximum Gram–Schmidt length<=||f||<=sqrt(h0). This sharper bound is valid even if off-diagonal entries are large; it does not falsely infer short vectors from arbitrary triangular diagonals. Computing M, denominator clearing and HNF are polynomial-bit operations. Only the D+1 enumeration depends on numerical D, so the theorem correctly restricts that preprocessing to polynomial index or separately supplied f.

## 5. Exact delivered width and example family

Substituting d0=delta ell^2/(64nk chi) gives W=32sqrt(2)n^2k chi q/(delta ell^2). With q>=8n^3 ceil(sqrt(kn))ell^4,

    W>=256sqrt(2)n^5 k chi ceil(sqrt(kn))ell^2/delta >4n sqrt(n).

For eta=2^(-4n), u=4n meets4exp(-pi u^2)<=eta/(32n) for every n>=2. Thus the collision-basis simulation is valid at the actual W. Exponent/HNF simulation has the explicit h<=W/(4n) condition and does not silently replace W by an arbitrarily large width. Requested substantially smaller eta can require a larger u and need not satisfy the same width premise.

For n>=4, g=X^(n/2)+X^(n/4)-1 divides X^n+1 modulo3 because (y^2+y-1)(y^2-y-1)=y^4-3y^2+1. The quotient has F3 dimension n/2, norm3^(n/2), exponent3. The inequality3^5<2^8 gives rho=4/5 eligibility. No claim that this ideal is prime is made. M1-FV1's explicit bases in n=4,8,16 have the stated diagonal Gram–Schmidt lengths and rotation closure.

## 6. Adaptive scope and finite evidence

The transcript simulation uses a coupling conditioned on the entire identical past. Per-call conditional TV errors add through a first-disagreement/union argument. The same-history triangle inequality handles imperfect oracle laws. No marginal-to-joint implication, selected-stage product, reused-randomness assertion or coherent-service substitution appears. If per-call budgets are history-dependent, use a deterministic upper budget or the expectation of their sum; the displayed fixed eta_j formulation is valid as written for uniform bounds.

The full finite code was inspected. Its80 cases are exact *truncated* Gaussian laws and conditional normalizer comparisons; no infinite-tail claim is made. The nonconstant-normalizer example H=[[2,1],[0,2]], base1/2 has exact positive TV about0.010761870523, with the complete joint law retained. The code correctly rejects treating scalar normalizers as constant. M1-FV1 ran with120s/512MiB limits, exit0,0.20s wall,13MiB RSS. Its source hash matches the reserved input. I inspected these records but did not rerun the experiment and do not describe it as independent computational execution.

The160-atom CP1 enumeration gives selected mass10/11, incidences1/10,121/2000,121/2000,21/2000,21/2000, event21/2000>1/100 and residual21/221<1/10. The failure mechanism remains support restriction and posterior normalization. M1's uniform full-density comparison and conditional additive coupling do not assert the rejected product. Historical zero/alignment and skew-normalizer failures remain valid in their original scopes.

## Scope conclusion

M1 provides a convincing candidate classical simulation criterion at its exact width/accuracy conditions. It eliminates computational use of polynomial-index calls, small-HNF/exponent calls and supplied-short-witness calls within that scope. It does not prove simulation for all exponentially indexed ideals, replace a coherent sampler, or provide a standard binary-secret RLWE foundation. No ACCEPT issued by this review.
