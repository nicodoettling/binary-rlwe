# Full nonauthor review of C theorem v7 / algorithm v1 / proof v8

Reviewer: worker A. Completed 2026-10-17 22:01 UTC. This is a full review of the supplied proof, not a blind review. The reviewer did not author this theorem, sampler specification, or proof. The earlier C7 causal review does not confer acceptance on this version. No upcoming blind report or blind status was read. The coordinator owns final reconciliation.

## 1. Exact inputs and verdict

All paths below are relative to OUTPUT. Author files were read completely, their hashes independently checked twice, and not edited.

| Input | SHA256 |
| --- | --- |
| workers/C/periodic-hardness/multiplier-ohcp-theorem-v7.md | 68ac0c763ebb1daa9ae4a0e8bf5d3c1fb665c130b37f36cfdb6ade0bcbcd56f2 |
| workers/C/periodic-hardness/multiplier-ohcp-algorithm-v1.md | 9fe1353d605a94cb82842626b305c018b045106daec1fd16581c8bc588f94c65 |
| workers/C/periodic-hardness/multiplier-ohcp-proof-v8.md | 508fba4aff482971a65a48e17730454c91f4f18fce35155899a00486a4bd4dd0 |

**Verdict: REJECT the exact triple as a complete, bounded finite-algorithm specification; one narrow implementation gap remains. The analytic BDD implication survives this review, subject to repairing that gap and the coordinator's remaining gates.** This is not a mathematical refutation of the promised BDD recovery bound, nor acceptance of any standard-hardness implication.

Defect C8-FV1 is in algorithm Section 8, repeated in proof Sections 7.4–7.5: an interval upper endpoint U is rational, but the input model allows d0 to be a general certified computable real. The displayed predicate U <= 2d0 is therefore not a specified rational comparison. Neither a rational replacement threshold nor a bounded certified interval-decision rule is defined. The algorithm additionally claims bounded bit budgets on every target, including off-promise targets without a separation gap. Up handles integer precision/cutoff expressions, not this predicate. The exact defect was frozen before any proposed repair in finite-verification-gap-before-repair-v1.md, SHA256 5650f1953f8d46fcf1ecab0b83fab26d5fc00ce169c82f77bf9c1932828fd433.

The failure is confined to the literal finite specification. On promised inputs the true candidate has residual <=d0, and every wrong lattice candidate has residual >3d0. This large gap supports a separately specified rational-threshold repair. No repair is silently substituted in this verdict.

## 2. Model, laws, and normalization

The statement is pointwise in an ordinarily represented integral ideal J. Its premise is a bounded randomized algorithm on k independent samples from the exact finite rounded spherical Gaussian law versus exact uniform on F=h Z^n/(q J^-1), with the same public J and all other public metadata. It is not merely an average over a distribution of ideals. Every invocation has fresh private coins; no multiplier or sampler randomness is published.

The quotient is well-defined because D J^-1 is contained in R, so q J^-1 is contained in h Z^n for h=1/(DP). In coefficient coordinates det(q J^-1)=q^n/D, giving |F|=q^n D^(n-1) P^n. Nearest-grid rounding with a fixed tie convention commutes with grid translations. Haar followed by this observation kernel is exactly uniform on F. Rounding is only applied after continuous-law comparisons, so its discontinuity does not invalidate data processing.

The coefficient/canonical factor sqrt(n) is consistent throughout: canonical Gaussian width w is coefficient width w/sqrt(n); the real orthogonal Fourier transform U gives Vcoef=U^T diag(v_i^2) U/n. Multiplication by an element h has canonical singular values |sigma_i(h)|. Full canonical norm counts both conjugate embeddings. No coefficient norm is silently substituted for canonical infinity norm.

Exact cancellation r lambda in q J^-1 holds for every integral multiplier r, including zero, nonunits and all finite sampler fallback outputs. The approximate rational mean contributes a separately charged TV error; it is not claimed to preserve the identity exactly before that charge.

## 3. Gaussian comparison and complete spectral endpoint

The completion identity retains both theta normalizers. With P=(V^-1+M_h^T M_h/w^2)^-1 and C=w^2 I+M_h V M_h^T, the normalized density ratio is the translated P theta factor divided by the original V theta factor. Under the displayed smoothing bounds, P >= 2 eta^2 I. Both factors lie in [1-epsilon0,1+epsilon0], implying TV <= epsilon0/(1-epsilon0), uniformly in the selected width and shift. No posterior factor is dropped.

The chosen integer a is enough for coefficient smoothing. To check the implicit bound directly, x=exp(-pi a^2)<=epsilon0/(8n); the one-dimensional nonzero theta tail is at most 2x/(1-x^3), and the n-dimensional product is below 1+epsilon0. Thus eta_epsilon0(R)<=sqrt(n) a in canonical coordinates, consistent with v0>=2 sqrt(n) a. The guard |h_j|<=8d0 is much smaller than the required w/(2 eta), including nuisance residuals.

The shifted center 2+e_j/d0 has modulus in [1,3], even when e_j=0. At the origin the covariance increase is at most 9[delta/(32nk)]^2. The stated Gaussian KL and Pinsker calculation gives a k-sample discrepancy below delta/16. Hence the same global orientation, chosen relative to the common spherical benchmark, has starting gap at least 15delta/16 for every conjugate pair. There is no need to infer a separate sign from each coordinate.

The Euclidean dual is conjugate(J)/(nq). A nonzero dual element has absolute algebraic norm at least D/(nq)^n. Multiplying by the diagonal Gaussian widths and applying AM–GM gives minimum at least sqrt(n)c, with the stated c. The shell count (2m+3)^n is a valid packing upper bound. For A0=pi-1-log(5)>1/2, the inequality pi c^2 m^2-log(2m+3)>=c^2+A0 m holds for c>=1 and m>=1. The resulting geometric sum is below one because n>=2. This bounds the entire nonzero theta sum by exp(-n c^2), and proxy-to-Haar TV by half that quantity. It is not a one-character estimate.

The decay and Lipschitz hypotheses follow with the displayed S and kappa. The nonnegative starting shift log|z*| is essential and is retained. The selected complex plane contributes at most 2 to the Gaussian TV derivative in log width; tensorization yields 2k. Fixed nuisance widths do not erase the initial excursion.

The exact-Haar endpoint is correctly restricted to the continuous proxy. The proof does not assert that an increasingly wide discrete integral multiplier itself converges to Haar. A simple independent character check illustrates why: in R=Z[i], a rational multiplier displacement can make a nonzero torus character identically one on every integral multiplier, leaving the added Gaussian's nonzero Fourier coefficient unchanged at every width. The constant epsilon0 comparison allows this persistent, small discrepancy. This regression remains binding.

## 4. Comparison, causal walk, and probability regressions

The weighted suffix functional H is nonincreasing. The post-current-shift excursion supplies the quantitative YES gap. The mesh, finite endpoint and empirical-error estimates have ample slack: 2 N b^2=2[C+ceil(log2(8(G+1)))], so the union over both profiles and G+1 grid points has the claimed exponentially small failure. Interpolation, endpoint replacement and the omitted tail each fit their allowances. The exact threshold 4/Lambda_cmp separates the promised YES and NO cases; arbitrary intermediate cases need no correctness promise.

The corrected reference process is causal. Its filtration contains the complete past but excludes the new proposal and new empirical coins. It forces only the two geometric cases, retaining the empirical decision in the intermediate region. Its radius cannot increase. Conditional on any past before reaching exp(-K), choosing a largest coordinate, favorable sign and the displayed X interval has probability at least 1/(10 K d_H). The resulting squared-radius and log-radius decreases are valid. The interval is contained in [0,1] under r>exp(-K).

Azuma applies to bounded martingale differences I_i-E[I_i|F_i], not to independent indicators conditioned on global success. For T=10^6 K^3 d_H^4 the lower count is 10000 K^2 d_H^2(10d_H-1), which exceeds the number needed to force the target radius. Once the target is reached, counting all later indicators as successes is adapted and legitimate.

The near-center exceptional step is bounded before conditioning on acceptance. On a chosen line intersecting the epsilon ball, positive endpoint product is r^2-epsilon^2; the ratio is largest on a radial line. This proves the log-uniform interval estimate also off a radial line. When the current radius is very small, the minimum step is too long to enter the much smaller exceptional ball. Union over first bad events and erroneous promised comparisons is valid conditional on every earlier legal history. The actual and corrected processes coincide until that first event. There is no conditioning on all future comparisons being correct.

The historical CP-1 regression is disposed of by this filtration and additive coupling, not ignored. In CP-1 the sequentially selected two-hit mass 21/2000 exceeds the naive product 1/100; posterior normalizers and support restrictions matter. No such marginal-product inference appears here. Likewise the C03-HC6 success/bad-noise dependence is handled by subtracting total exceptional mass, not by multiplying recovery success and a noise-good probability.

The finite transcript control in C/periodic-hardness/ohcp2-control was read as supplementary evidence: it reports 60 exact piecewise-profile cases and 343 exact two-step adaptive systems. Its scope is interpolation/order and adaptive-TV addition, not Gaussian sampling or the guided-walk theorem. It does not replace the analytic checks above. No new machine experiment was run during this review.

## 5. Finite samplers and computable arithmetic

Up is a valid fixed-error operation: evaluating x within 1/8 and taking ceil(c+1/8) lies between ceil(x) and ceil(x)+1. It avoids exact comparison against an integer boundary. Its occasional extra unit only increases the cutoff/precision bounds used in the sampler analyses.

Std compares a dyadic midpoint against approximate CDF values with an explicit ambiguity rule. If delta_p=2^-p, midpoint error is at most delta_p/2. A nonambiguous comparison with separation greater than 2 delta_p has the same sign as the true CDF comparison. On an early ambiguous return the true probability argument differs by at most 3.5 delta_p; the chosen p makes this much smaller than eps times the minimum density ell. Thus the returned location is close to the coupled true quantile except in the explicitly bounded tail. The remaining bisection interval is short enough. This is a positional coupling, never a false raw-TV comparison between rational outputs and an absolutely continuous Gaussian.

The fixed CDF series order and guard precision are sufficient: on the unclipped interval |x|=O(p), the Taylor order is O(p^2) with a large constant, while the exponential-series remainder decays below the required 2^-p after allowing the exp(pi x^2) scale. The much larger guard precision covers cancellation and pi/input approximation. Clipped arguments have a negligible Gaussian tail. The specification does not require indefinite CDF refinement at a tie.

For the elliptical multiplier, W=Vcoef-a^2 I>=3a^2 I. On the stated Gaussian cutoff event the Bhat entry errors and positional Std errors each contribute at most xi/4 in l1. Their exceptional events fit alpha_H. The ideal continuous-center/discrete-scalar construction is checked as follows: divide the scalar kernel by a^n times its translated theta factor; integrating without the theta factor gives the normalized continuous Vcoef density at each integer. Its lattice sum is the second theta factor. Therefore the ratio to the normalized target discrete Gaussian lies between (1-epsilon0)/(1+epsilon0) and its reciprocal. This verifies the full distribution, not only its covariance.

For shifted scalar means, differentiation of normalized probabilities and the translated-theta mgf bound give the conservative 4pi/a TV derivative. The scalar proposal support has uniformly small Gaussian tails; rho_a(Z-f)>=0.9a follows directly from the one-dimensional theta series at a>=1. The retained mass bound 0.85a, weight-error allowance, acceptance lower bound 1/(5 Ks), and rejection-cap failure all hold with slack. A capped-uniform failure returns an integer and costs at most tau/16 over n Ls proposals. Integer shift equivariance survives the half-integer centering tie and fallback.

The numerical multiplier charge is epsilon0/(1-epsilon0)+tau/4. Mean approximation costs at most tau/32. GridGaussian samples the actual rounded Gaussian law: omitted tails cost at most tau/16, and an exact uniform quantile disagrees with the finite binary search only near a true CDF boundary, whose union mass is at most 8 n M_G 2^-p_G<=tau/32. Approximate thresholds need not be monotone on that already charged exceptional event. The support may be huge, but only O(log M_G) CDF evaluations are used.

The total numerical charge per physical sample is below tau. The global counter is never reset. All bounds are uniform in the entire prior history, sampled multiplier magnitude, and query position, so their sum is a valid adaptive coupling bound. Fixed posterior and sampler normalization errors contribute twice epsilon0 per physical sample and fit zeta/16 over kQ_* samples. There is no uncharged conditioning on a favorable sampler branch.

## 6. Finite walk, counts, reconstruction, and remaining defect

The exact multiplier mgf bound gives E||sigma(r)||_2^2<=2n v_max^2. Gaussian translation then yields the global physical-kernel Lipschitz bound <=exp(M), without a guard restriction. The coupling order is correct: analytic to physical at the ideal real position; physical real to physical dyadic position; then physical to finite sampled kernel. It does not require continuity of the piecewise analytic patch.

The B-bit midpoint/exponential construction perturbs each proposed scalar step by at most 3*2^-B. Until oracle bits disagree, rational comparison scores and decisions coincide, so cumulative positions differ by at most the stated 9(T_walk+2)2^-B after restoring scale 3. The explicit B makes Q_* exp(M) times this discrepancy less than zeta/16. The final center error also fits the exp(-kappa) budget.

Each comparison uses exactly 2(G+1)N calls; each walk T_walk+1 comparisons; all n/2 pairs under both orientations therefore use Q_*=n Q_H calls. These counts are independent of correctness. Actual positions, scalar fallbacks and all finite loops have bounded sizes even for arbitrary answers. Runtime properly includes all scalar encodings and the costs of their certified evaluation; no bound based only on log magnitude is smuggled in.

The reconstruction margin is valid: canonical-coordinate error converts to coefficient error without an extra sqrt(n), and the extra q/(64D) approximation combines with 3d0 exp(-kappa)<q/(8D) to stay below q/(2D). Membership in L is exact. Nonzero elements of L have canonical infinity norm at least q/D^(1/n)>4d0, so the promised BDD solution is unique and every wrong candidate has residual >3d0.

This is where C8-FV1 intervenes. A certified rational residual upper endpoint is finite, but its exact comparison to the general real 2d0 is not. A concrete finite-precision boundary control is U=1 and thresholds x_+=1 versus x_-=1-2^(-B-2). Both admit the same certified B-bit approximation 1, but U<=x has different truth values. More generally a uniformly polynomial-time evaluation routine can encode x_E=1 if machine E never halts and x_E=1-2^(-t-2) if it halts at time t: p-bit evaluation only simulates p steps. Exact comparison 1<=x_E would decide nonhalting. This illustrates why certified evaluation alone is not the missing comparison primitive. It does not claim that the promised BDD instance itself encodes this difficulty; its promise supplies the separation needed for a revised rational test.

## 7. Scope and required next gate

No further defect was found in the reviewed mathematical estimates. The total stated recovery loss (n/2)exp(-kappa)+zeta follows once the final verification operation is made a bounded rational procedure. The exact current package is nevertheless incomplete and is not accepted by this review.

A repair must explicitly define a rational threshold and its required relative approximation, define the residual interval precision using computable input data, state its bounded behavior on off-promise inputs, and update all bound companion references/hashes. The promised true/wrong residual gap must then be rechecked. This reviewer has not authored such a repair here. Coordinator reconciliation must also retain the independent blind gate; a proof review is not a substitute for it.

The proof is self-contained for this classical pointwise BDD implication. This review does not certify the source literature's separate quantum/coherent implementation, B's Gaussian-periodic simulator, A's fractional lossiness theorem, or any reduction from arbitrary ideals into the bounded-index family. The stated downstream same-J Gaussian width is a conditional normalization comment, not a newly accepted quantum theorem. The original standard computational foundation remains OPEN.
