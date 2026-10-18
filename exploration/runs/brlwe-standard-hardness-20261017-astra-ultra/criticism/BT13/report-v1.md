# BT13: independent blind reconstruction, sealed version 1

## Verdict and exact scope

**SUPPORTED, within the declared finite scalar-input model, for the core pointwise classical BDD assertion in theorem v8 and algorithm v2.** I found no counterexample or remaining obstruction in those two frozen inputs. The reconstruction below supplies a causal walk argument and checks the finite samplers and rational final test without importing the author proof. This is a human-readable mathematical audit, not formal verification.

This verdict does **not** certify the separate fractional-composition/B bridge, coherent quantum access, a quantum BDD-to-DGS implementation, arbitrary-family worst-case hardness, or the original computational hardness objective. The cited external sources were unavailable under the blind-input rule and were not checked. Same-model role diversity provides correlated scrutiny, not formal verification or statistical independence.

Authorized scientific inputs, read completely:

* `input/multiplier-ohcp-theorem-v8.md`: SHA256 `857a62e9f4a937a80e5cb3b115c8b132abf122c16665d29b39dcb62bde86fe0a`.
* `input/multiplier-ohcp-algorithm-v2.md`: SHA256 `4361c90a7fa7cfe25d0ab3e8cd5c5333fb474cf1fb764375e10c29fca5102735`.

Assignment: SHA256 `770c548574e889c9c53d042b7379f81170047b53c287db22cc198ac563991445`.

The assignment and both input hashes were verified before mathematical work. No author proof, sibling review, ledger, status, additional scientific file, web page, MCP resource, session, or model configuration was inspected. The two input documents themselves mention earlier versions and outcomes; those references were not followed. Exposure record: **none beyond the authorized packet and the coordinator's reservation/logistical messages**. No substantive result was sent before completion and hashing of this report.

## 1. Exact interface, quotient, and cancellation

Use the real orthonormal version of the full canonical embedding; a conjugate pair has coordinates sqrt(2) times its real and imaginary parts. The coefficient-to-canonical matrix is sqrt(n) times an orthogonal matrix. Thus coefficient covolume of J is D, coefficient covolume of J inverse is 1/D, and canonical covolumes acquire the common factor n^(n/2).

The finite quotient exists with exactly the stated order. The integral ideal identity D J inverse subset R gives L=q J inverse subset (q/D)R subset h Z^n. Consequently

    |h Z^n / L| = (q^n/D)/h^n = q^n D^(n-1) P^n.

Nearest-grid rounding commutes with translation by L, including the specified deterministic ties. HNF/SNF therefore gives a common finite representative convention in GP, U, and all reduction queries. Haar measure on the continuous torus R^n/L rounds to uniform measure on this finite quotient: every grid class has an equal-volume rounding cell. This fact, followed by data processing, is used for the comparator; it does not replace the exact finite GP law by a continuous-input law for A.

For every exact integral r, including zero and every nonunit, r lambda belongs to q J inverse. Hence

    r(T_bdd-g)+G_w = r(e-g)+G_w modulo L.

Neither multiplication by an inverse of r nor division by an embedding of e-g is used. The cancellation holds before rounding, and rounding respects the quotient. The private multiplier, auxiliary Gaussian, and sampling coins are never appended to A's input. The public ideal and all other metadata are identical in the two distinguishing experiments. No assumption on an ideal distribution is introduced.

The ideal inverse and quotient computations need no factorization of D: the trace-dual identity in this power-of-two ring expresses the inverse ideal through an ordinary rational dual basis and conjugation. Ordinary rational linear algebra and integer normal forms suffice, with bit lengths controlled by the input basis.

## 2. Gaussian normalizers and the physical-to-proxy comparison

Write epsilon=epsilon0. Let Acoef be the positive coefficient squared-width matrix Vcoef, and let H be an exact continuous Gaussian of squared width Acoef-a^2 I. Its positivity is uniform: Acoef has minimum eigenvalue at least v0^2/n >= 4a^2.

The scalar conditional law in the exact convolution construction has denominator rho_a(Z-H_l), so the joint conditional denominator is rho_(a I)(Z^n-H). This denominator cannot be deleted. Poisson summation gives, uniformly in the translate,

    |rho_(a I)(Z^n-H)/a^n - 1|
      <= (1+2 sum_(m>=1) exp(-pi a^2 m^2))^n - 1 < epsilon.

Indeed exp(-pi a^2) <= epsilon/(8n), the one-dimensional tail is at most twice its first term, and epsilon<=1/16. The extra unit in a only improves this bound. The same estimate holds for every coefficient squared-width matrix with minimum eigenvalue at least a^2, by bounding its dual quadratic form below by a^2 times the ordinary squared norm.

Replacing the conditional denominator by a^n and integrating the two Gaussians gives the unnormalized mass

    f0(r) = det(Acoef)^(-1/2) exp(-pi r^T Acoef^(-1) r).

Its sum Z_V lies in [1-epsilon,1+epsilon]. Retaining both this sum and the conditional denominator shows that the exact convolution multiplier law is within epsilon/(1-epsilon) in total variation of D_(Z^n,Acoef). For example, compare the convolution mass first to f0, then to f0/Z_V; the two half-L1 bounds sum to at most epsilon/(1-epsilon). This is the first fixed normalization charge.

Now use the exact discrete multiplier D_V and let hvec=e-g. Multiplication by hvec is a normal real operator, diagonal by conjugate pairs. Completing the square in the joint density of the multiplier and added G_w gives the continuous proxy whose canonical squared widths are

    w^2 + v_i^2 |hvec_i|^2.

The posterior multiplier squared-width operator is

    Sigma^(-2) = V^(-2) + |hvec|^2/w^2

in the simultaneous canonical diagonalization. Its center may vary arbitrarily. The exact density ratio is the posterior theta factor divided by the original multiplier theta factor. Both must be retained. No inverse of hvec occurs, so zero coordinates and singular multiplication operators are included.

If the selected |hvec_j|<=8d0 and all nuisance |e_i|<=d0, then every canonical posterior width is at least

    v0/sqrt(1+(8v0d0/w)^2) >= v0/2 >= sqrt(n) a.

Here v0d0/w=delta/(32nk), n>=2, and k>=1. The coefficient posterior minimum width is therefore at least a. Both theta factors differ from 1 by at most epsilon, uniformly in the posterior center and every t>=0. The second total variation charge is at most epsilon/(1-epsilon). Rounding and quotienting preserve these bounds.

For arbitrary selected positions one can define an analysis-only oracle equal to this radial proxy inside |e_j-g_j|<=8d0 and equal to the exact physical law outside. Its per-call discrepancy is uniformly bounded; no regularity is required at the boundary. This local extension is never queried as a real oracle. The walk argument below uses only its radial region. Position coupling is performed through the globally Lipschitz physical law, not through this possibly discontinuous extension.

The cumulative two-normalizer cost is exactly bounded as stated:

    2 k Q_* epsilon/(1-epsilon) < zeta/16.

This uses epsilon<=zeta/(64kQ_*) and epsilon<=1/16. There is no unsupported exact physical endpoint claim.

## 3. Starting gap, all-frequency proxy smoothing, and the zero branch

Fix a selected pair. Define a proxy profile p(s) in which that pair's additional canonical width is h0 exp(s), while each nuisance additional width is v0 |e_i|. The normalizing shift for a normalized walk position u is

    s = log(3 ||u-u_*||) + t,       u_*=z_*/3.

The nuisance widths stay fixed throughout the suffix profile. The comparison against Haar is a comparison of the actual k-sample input distributions to A, after rounding and quotienting.

For normalized radius at most 1, the selected additional width at t=0 is at most 3h0 and the other additional widths are at most h0. A Gaussian-translation bound followed by averaging gives one-sample distance from G_w at most 3n h0/w = 3delta/(32k). One way to see the translation bound is to integrate the directional derivative of a width-w Gaussian; its total variation displacement is at most the Euclidean displacement divided by w. The deliberately looser coordinate sum above suffices. The k-sample proxy is therefore within 3delta/32 of GP. Consequently its starting acceptance gap from the uniform comparator has magnitude at least delta/2 >= 1/kappa >= 1/C. The chosen global orientation can make this gap positive. The absolute value in the score actually makes the quantitative comparison invariant under complementation, but running both specified orientations remains valid and incurs exactly the stated count.

For the tail, the canonical dual of L is

    L^* = (1/(nq)) conjugate(J).

Every nonzero x in it has algebraic norm at least D/(nq)^n. If W is the diagonal proxy width operator, weighted arithmetic-geometric mean gives

    ||W x|| >= sqrt(n) a0 exp(2s/n).

The selected pair contributes two factors; all other factors are at least w. This proves the bound with exactly

    a0 = D^(1/n) w^(1-2/n) h0^(2/n)/(nq).

It also shows why expansion in one conjugate pair controls the whole dual spectrum: a nonzero field element cannot have a zero selected embedding. A coordinatewise assertion about only some Fourier characters would not suffice.

Put S=max(0,(n/2)log(1/a0)). For s>=S+n, the minimum distance of W L^* is at least sqrt(n) exp(2(s-S)/n). A direct packing-shell estimate gives

    sum_(x in L^*, x!=0) exp(-pi ||W x||^2)
       <= 2 exp(-(pi/2)n exp(4(s-S)/n)).

For completeness, count points in the shell [m lambda,(m+1)lambda) by (2m+3)^n, use 2m+3<=5^m, absorb this factor in half the Gaussian exponent, and sum the resulting m^2 tail. The displayed minimum is more than sufficient for all these inequalities. Since n exp(4(s-S)/n)>=4(s-S), the k-sample total variation distance to rounded Haar is at most

    k exp(-2pi(s-S)).

In particular, uniformly for radii >=exp(-C), the acceptance tail at suffix time t>=2C is bounded by exp(-t). To check the constants, s>=t-C, while S,n,log(k) are each at most C/4. The lower cutoff s>=S+n and the inequality log(k)-2pi(t-C-S)<=-t both hold for t>=2C. The extra factor 3 in s only helps.

At exact zero radius the selected branch does not expand, and its physical or proxy endpoint need not be uniform. At nonzero radius the proxy tends to Haar by the preceding whole-spectrum bound. The exact discrete-multiplier physical law can retain characters for rational displacements; it is only uniformly close to this proxy. These distinctions are essential. The finite walk below explicitly avoids needing a uniform endpoint assertion at zero or at arbitrarily tiny radii. The shift by 2 ensures its initial normalized radius lies in [1/3,1].

The scalar profile is Lipschitz in s with constant at most 2k<=kappa<=C. This follows by differentiating the two-dimensional selected Gaussian density with respect to its log width, whose width derivative is at most 1; rounding, taking a k-fold product, and applying A preserve the stated conservative bound.

## 4. Exact empirical comparison and its constants

For r>0 define the analysis score

    H(r)=sup_(t>=0) (1+t)|p(log(3r)+t)-p_infinity|.

If r2<r1 and b=log(r1/r2), shifting a suffix by b gives

    H(r2) >= H(r1) + b |p(log(3r1)+t_*)-p_infinity|

at a maximizer t_* for H(r1). Thus H never increases with radius. For r1<=1 and r1>=exp(-C), H(r1)>=1/C. The tail after 2C is at most (1+t)exp(-t), so a maximizer lies before 2C. Its unweighted gap is at least 1/[C(1+2C)] >= 1/(3C^2). Hence a logarithmic radial improvement at least 1/C increases H by at least 1/(3C^3), far above 4/Lambda_cmp.

This argument does not require the profile itself to be monotone. The supremum of weighted suffix gaps provides the needed monotonicity.

The finite score in the algorithm approximates H for every r>=exp(-C). The following conservative constants suffice:

* M>=2C, and (1+M)exp(-M) is much smaller than 1/(100 Lambda_cmp). Truncating the supremum at M and replacing p_infinity by p(log(3r)+M) therefore costs less than 1/(50 Lambda_cmp).
* On [0,M], the weighted profile is 4CM-Lipschitz or better. The mesh Delta=1/(100 C Lambda_cmp M) costs at most 1/(25 Lambda_cmp).
* If every empirical frequency is within eta=1/(100 Lambda_cmp M) of its true mean, replacing both frequencies in the score costs at most 2(1+M)eta <=1/(25 Lambda_cmp).

Together these errors are at most 1/(10 Lambda_cmp), with room in the first item. All comparisons of empirical scores and the threshold 4/Lambda_cmp are exact rational comparisons. No estimate of an unknown limiting probability is requested from the implementation.

For each comparison, Hoeffding and a union bound over both positions and all G+1 frequencies give

    Pr(any frequency error > eta)
      <=4(G+1) exp(-2[C+ceil(log2(8(G+1)))])
      <=exp(-2C)/16.

This holds conditional on the complete preceding execution because the calls in that comparison use fresh independent bits. It requires neither independence between separate adaptive comparisons nor conditioning on future comparisons.

On this empirical event, a YES cannot increase the radius. A proposed logarithmic improvement of at least 1/C, from radius <=1 with both radii >=exp(-C), must be accepted. For the latter claim, 1/(3C^3)>5/Lambda_cmp follows directly from Lambda_cmp=10000C^4. The weaker bound obtained by placing a maximizer anywhere up to M also works: M<=100C^2 and the same constants still leave ample margin. The actual parameters have C far above 64; ceil(log2(10000C^5))<=C already suffices for that bound.

Each comparison performs exactly 2(G+1)N calls. Endpoint samples are included, even though the endpoint's own weighted difference is zero. The loops do not depend on the sign, any radial promise, or any answer sequence.

## 5. Causal adaptive walk: no future conditioning

First analyze the ideal continuously sampled step length

    ell=exp(-2K X)/(K sqrt(2)),       X uniform on [0,1].

Its density on its support is 1/(2K ell), with maximum sqrt(2)exp(2K)/2. Conditional on any past and on a chosen coordinate/sign, the probability that a proposed point lies within exp(-C) of the center is at most sqrt(2)exp(2K-C): intersecting a coordinate line with that ball produces an interval of length at most 2exp(-C). A union bound over the T_walk+1 proposals therefore bounds any such tiny-radius event by

    2(T_walk+1)exp(2K-C).

The initial radius is at least 1/3. The displayed Lambda_walk makes this probability less than exp(-kappa)/8, with a very large margin. This anti-concentration step is necessary: the finite endpoint score is not valid at radius zero, and a proof that simply treats zero as an ordinary suffix profile would fail.

Use the following corrected process only as an analysis object. It uses the same fresh steps and comparison samples. It rejects a proposed radius increase even if the sampled comparison says YES. If the current radius is above exp(-kappa) and a geometric progress proposal described below occurs, it accepts that proposal even if the sampled comparison says NO. Otherwise it follows the implemented rule. Thus the corrected radius never increases, and a geometric progress event always gives its stated contraction. No correction is made in the implemented algorithm.

Before the first discrepancy, the corrected and actual ideal walks coincide. Every corrected-walk point has radius <=1 and every proposed point has radius less than 2. Its physical selected displacement is consequently below 6d0, within the 8d0 proxy region. Unless a tiny-radius event or an empirical error occurs, Section 4 guarantees that the corrections never activate. Their total probability is bounded by the tiny-radius union bound plus (T_walk+1)exp(-2C)/16, less than exp(-kappa)/4.

Here is an explicit progress event, with deliberately weaker constants than the available ones. At radius r in [exp(-kappa),1], choose a coordinate with absolute error at least r/sqrt(2), take its favorable sign, and choose

    ell in [r/(4K), r/(2K)].

This interval is inside the log-uniform support: its upper end is below 1/(K sqrt(2)); its lower end exceeds exp(-2K)/(K sqrt(2)). The coordinate/sign choice has probability at least 1/4, and the length interval has probability log(2)/(2K). Conditional on **every past**, the event therefore has probability at least 1/(12K).

For such a proposal,

    r_new^2/r^2 <= 1 - 1/(4K),
    log(r/r_new) >= 1/(8K) >= 1/C.

The first inequality follows even if 1/sqrt(2) is weakened to 7/10: use ell/r between 1/(4K) and 1/(2K), and K>=3. The second shows the comparison accepts this proposal outside its error event. At most ceil(8K kappa) progress events are needed to reach exp(-kappa).

There is a direct causal concentration argument. Let the indicator record the geometric event while outside the target radius, and set it to 1 after the target radius is reached. At each step its conditional success probability is at least p=1/(12K). For theta>0, iterated conditional expectation gives

    E exp(-theta sum I_s) <= (1-p+p exp(-theta))^(T_walk+1).

This is a conditional-moment proof, not multiplication of marginal progress probabilities. It does not condition a fresh step on all future successes. Taking theta=log(2), the probability of fewer than ceil(8K kappa) successes is exponentially smaller than exp(-kappa)/4: T_walk=16*10^6 K^3, so p T_walk exceeds 10^6 K^2, whereas ceil(8K kappa)<=9K^2. These inequalities leave several orders of magnitude of numerical slack.

Combining progress, empirical error, and anti-concentration shows that one ideal continuous walk finishes within exp(-kappa) of its normalized center with failure probability below exp(-kappa). The corrected process is used only to justify this bound and the causal couplings. The actual loop remains exactly T_walk+1 steps with the specified accept/reject rule. It has no early stopping or hidden-radius test.

Apply this argument to all n/2 pairs for a favorable global orientation and union bound: geometric/statistical failure is at most (n/2)exp(-kappa). No independence between pair successes is needed. The other orientation can run with all its prescribed calls; the final verifier prevents it from returning an incorrect lattice point on a promised input.

## 6. Every finite scalar sampler and its error charge

All total variation comparisons in this section are conditional on the complete adaptive transcript preceding the physical sample. Therefore the scalar errors can be summed across the global counter even when its associated means and scales depend on previous oracle answers.

### Standard continuous Gaussian approximation

Couple the midpoint U with a continuous uniform variable in its dyadic cell. Their difference is at most 2^(-p-1). On [-H,H], the Gaussian density is at least ell=exp(-pi H^2). At an early-return midpoint, the difference between its true CDF and the continuous uniform is at most (7/2)2^(-p). Because 2^(-p)<=eta/4<=eps ell/256, this implies an output error smaller than eps. If no early return occurs, every retained half-interval contains the exact quantile: the 2^(1-p) safety margin exceeds the combined midpoint-uniform and CDF errors. The final interval length is below eps. Clipping can only introduce the stated Gaussian-tail failure, bounded by alpha with substantial slack from H. Thus Std(eps,alpha) admits a coupling with a true standard Gaussian that is eps-close except with probability alpha. Its loops are fixed finite loops; they never wait for a real equality to be resolved.

The proposed Gaussian CDF evaluation is adequate. For |x|>=p+4 the omitted tail is much smaller than 2^(-p). Otherwise J_eval>=100[p+(|x|+1)^2+1] makes the integrated exponential-series remainder smaller than the requested tolerance: the ratio e*pi*x^2/J_eval is below 0.086, and the order also dominates p. The prescribed guard precision dominates the O(x^2) cancellation loss and the accumulated rational-arithmetic error. Approximating an argument first adds at most its absolute error, since the standard density is at most 1; the five-bit margin covers it. These are ordinary certified elementary evaluations, not an exact-real decision primitive.

### Capped integers and scalar discrete Gaussians

Each successful UniformCap draw is exactly uniform on its requested integer interval. Its failure probability is at most 2^(-Rcap), since a single rejection probability is below 1/2. The H=1 branch is exact. Across all n scalar calls and all their Ls proposals, the total cap-failure probability is at most

    n Ls 2^(-Rcap) <= tau/16.

For Scalar, shifting the rational mean by an integer shifts all outputs, including fallback, by that integer. The explicit upper tie used for z0 is consistent with the centered fraction in [-1/2,1/2); it need not match the separate final grid tie.

The omitted ideal Gaussian tail beyond Ns is negligible relative to nu. For instance its relative mass is at most 5exp(-pi Ks^2), and Ks>=log2(64/nu) makes this much smaller than nu/64 in the physical range. The support has at most 5a(Ks+1) points. The true retained weight is at least 0.8a, using the elementary scalar Poisson bound at a>=1. Consequently the normalized law using the dyadic acceptance weights differs from the retained Gaussian by at most

    5a(Ks+1)2^(-ps)/(0.8a) < nu/128.

This is a normalized-weight estimate; multiplying an acceptance-rounding error by every possible trial would be an unnecessarily poor bound. The perturbed acceptance probability is at least 1/(10Ks). Therefore the probability of exhausting Ls trials is at most (nu/16)^4. The truncation, perturbed weights, and final fallback together are bounded by nu, excluding the separately charged UniformCap failures. Summing n such scalar errors gives tau/16.

### Elliptical multiplier arithmetic

Couple the n calls to Std to independent exact standard Gaussians. Their specified failure probabilities and the additional |Z_l|<=Hcut tail failure sum to less than alpha_H=tau/16. On this event, the entrywise Bhat tolerance and eps_Z give

    ||Bhat Zhat - B Z||_1 <= xi/2.

For a scalar D_(Z,a,c), differentiating its normalized weights bounds its total variation Lipschitz constant in c by 4pi/a. One elementary supporting bound is E|X-c|<=2a for a>=1: compare the sum of |x|exp(-pi x^2/a^2) with its integral plus total variation, and use rho_a(Z-c)>=0.9a. Thus the product conditional law changes by at most

    (4pi/a)(xi/2) = tau/32.

Combining these arithmetic/coupling errors with the scalar and integer-cap errors gives less than tau/4 for this part. The fixed convolution normalizer error is separately charged in Section 2. Every output is an exact integer coefficient vector, even on fallback branches.

### Rounded Gaussian and the physical mean

GridGaussian's finite support covers the central standardized interval [-H_G,H_G] with spare grid cells. Its omitted tails have probability at most tau/(64n) per coordinate. Couple its midpoint uniform with a continuous uniform in the same dyadic cell. Outside intervals of combined length at most 3 M_G 2^(-p_G) around all exact thresholds, every comparison has the correct sign, so binary search returns the exact inverse-CDF rounded Gaussian index. This argument includes the possibility of inconsistent approximate thresholds: they can affect the result only on the charged ambiguous event. Its probability is at most 3tau/(256n), and the tails plus this error are below tau/(16n). No enumeration of M_G cells is required or implied.

The physical mean error is at most (w/sqrt(n))tau/(64pi) in coefficient L1 norm. Gaussian translation bounds its total variation effect by tau/(64pi). The example precision in the specification really attains that mean bound: negacyclic multiplication contributes at most n^2 ||r||_infinity times the per-input-coefficient error. Both Gaussian normalizers remain separate from this numerical charge.

These errors sum to less than tau per physical sample, with ample slack. The single global counter starts with c=1 for the first generated sample, so

    sum tau_c = (zeta/16) sum_(c>=1) 1/(c+1)^2 < zeta/16.

This is conditional transcript accounting. Resetting the counter between pairs or orientations would invalidate this displayed bound; the specification explicitly does not reset it.

## 7. Quantized walk coupling through the physical kernel

The finite midpoint quantizer is one-dimensional. Couple its Xhat to a continuous X in the same dyadic cell. The derivative of exp(-2K X)/(K sqrt(2)) has magnitude at most sqrt(2), and the subsequent exponential approximation adds at most 2^(-Bbits). The length error is therefore below 2*2^(-Bbits). With shared accept/reject decisions, normalized position error accumulates to at most 2(T_walk+1)2^(-Bbits); candidate physical positions differ by at most 6(T_walk+2)2^(-Bbits).

For the exact centered discrete multiplier D_V, its moment-generating-function bound is the continuous Gaussian bound: completing the square produces a translated theta mass, which is maximized at zero by Poisson summation. In particular E|r_j|^2<=v0^2 exp(2t)/(2pi). Changing only z shifts the Gaussian mean by the selected pair product r_j d0 Delta z. Gaussian translation, averaging over r, and taking k samples show that the physical acceptance probability is globally Lipschitz in z with constant at most

    k d0 v0 exp(t)/(sqrt(pi) w) <= exp(M).

The bound does not depend on T_bdd, the displacement from the center, or any local proxy patch. Rounding and quotienting again contract total variation.

Thus the total transcript-coupling loss across Q_* calls is at most

    6 Q_* exp(M)(T_walk+2)2^(-Bbits) < zeta/16.

Use exp(M)<=2^(2M) and the explicit Bbits formula to check the final inequality. There is a factor well above 1,000 of unused slack. This is why continuity of the local analytic extension is unnecessary. A valid order is: couple finite numerical physical samples to exact physical samples; couple the finite and continuous positions through the exact physical kernel; then apply the local proxy/corrected-walk argument. On mismatch charge the corresponding event and stop that coupling. No nonlocal proxy estimate is assumed.

Together, numerical sampling, both fixed normalizer errors, and position discretization cost less than 3zeta/16. The theorem's allowance zeta is conservative and covers these charges without reallocating the exp(-kappa) walk-error term.

## 8. Reconstruction and the repaired rational verifier

Successful normalized walks give physical center error at most 3exp(-kappa), and hence canonical error-estimation error at most 3d0 exp(-kappa) in every pair. Since d0<w, the theorem's condition implies

    3d0 exp(-kappa) < q/(8D).

An inverse canonical transform bounds each coefficient error by the maximum canonical coordinate error. The additional specified coefficient approximation q/(64D) therefore keeps total coefficient error below 9q/(64D), well below half the grid spacing q/D. Since lambda lies in (q/D)Z^n, the rounding step recovers lambda exactly. This uses a full conjugate-symmetric candidate, not independent sign choices between pairs.

The final real-to-rational threshold change resolves the boundary-decision issue within this packet. From the fixed p_test rule,

    eps_test <= d0/256,
    255d0/256 <= c_test <= 257d0/256,
    254d0/256 <= d_lower <= d0,
    (3/2)(255/256)d0 <= threshold_test <= (3/2)(257/256)d0 < 2d0.

The p_test=0 branch also obeys eps_test<=d0/256; that branch can occur only when d0 is sufficiently large. All precision targets and final comparisons are rational. A promised residual has every canonical modulus at most d0, so any certified enclosing interval of width at most d_lower/8 has upper endpoint at most d0+d_lower/8<=9d0/8, below threshold_test. Thus the correct candidate is accepted, including equality at the BDD promise boundary.

An accepted candidate has residual infinity norm below 2d0 and passes exact L membership. If the true promised lambda exists, the difference from it has infinity norm below 3d0. Every nonzero vector of q J inverse has infinity norm at least q/D^(1/n), by the algebraic-norm bound for the fractional ideal. Since d0<q/(4D^(1/n)), the accepted candidate must equal lambda. This establishes that an earlier accepted candidate from the other orientation cannot be wrong on a promised target.

The interval computation and the strict/rational decisions terminate on off-promise targets too. No claim of correct decoding on such targets is needed; bounded runtime is still required and supplied. There is no unbounded refinement around d0, 2d0, or an unspecified real equality.

## 9. Call count and full bit complexity, including wrong-sign executions

There are n walks total: n/2 pairs for each of two orientations. Each has exactly T_walk+1 comparisons, each comparison exactly 2(G+1)N calls. This is exactly Q_*=n Q_H. A calls use fresh private coins. Its supplied bounded runtime on every valid finite input is essential to the conclusion.

All loop lengths are polynomial in the numerical parameter kappa. With d_H=2, K=O(kappa), C=O(K log K), Lambda_cmp=O(C^4), M=O(C log C), G=O(C^7 log^2 C), N=O(C^11 log^2 C), and Q_*=O(n K^3 C^18 log^4 C). The large degree is not an asserted degree for any external paper. Integer counters require logarithms of these quantities in binary storage.

The global sample index is at most kQ_*, so log(1/tau) is polynomial in log(kQ_*), log(1/zeta), and their encodings. The cutoffs and rejection caps are polynomial in these lengths. The scalar support size a Ks is modest; its center may be huge, but integer shifting preserves the law and the bit complexity is measured in the full center encoding. GridGaussian may have enormous M_G, but its binary search uses O(log M_G) iterations, p_G depends on log M_G, and its integer support is stored by binary endpoints. It never expands that support into an array.

On every walk transcript the accumulated rational position has magnitude at most O(T_walk/K) and precision O(Bbits+log T_walk). The t grid lies in [0,M]. Exponentials of these t values have O(M) magnitude bits. The coefficient square root has a uniform positive spectral margin. All requested embedding, mean, and CDF precisions are explicitly polynomial in these bit lengths and the full input lengths. The inverse ideal, determinant, membership and quotient computations are ordinary polynomial-bit arithmetic. The target numerator and denominator lengths enter the mean and residual costs; no small-target assumption is used for runtime.

The definition permits efficiently evaluable nonrational scalars but does not provide a free unit-cost exact-real oracle. The actual certified evaluation cost at each requested precision is part of the input model and runtime bound. Rational/algebraic representations satisfy the ordinary interpretation. Any claim based only on logarithms of scalar magnitudes, while ignoring large rational denominators or evaluation-program costs, would be stronger and is not established here. The Up operation avoids exact comparisons at a computable-real integer boundary. Each approximation tolerance is positive with an explicitly bounded requested precision under the declared parameter/input measures.

These bounds hold if the orientation is wrong, if A gives adversarial answer bits, or if T_bdd is outside the BDD promise. Such executions may produce poor candidates, but neither the empirical loops nor the sampling caps nor the final rational test can run indefinitely.

## 10. Reserved finite falsification and its limits

The sole experiment was coordinator reservation **BT13-FV1**: one foreground deterministic standard-library Python job, at most 120 seconds, at most 512 MiB address space, n<=8, and at most one million finite cases. A pre-execution reservation/input record was saved. It used no oracle, network, external data, or random seed. Full code, explicit finite input arrays, exact command, original stdout/stderr, and `/usr/bin/time -v` resource output are preserved alongside this report.

Files:

* `BT13-FV1-reservation.md`
* `BT13-FV1.py`
* `BT13-FV1-command.sh`
* `BT13-FV1.stdout`
* `BT13-FV1.stderr`
* `BT13-FV1.resources`

Exit status: 0. Wall time: 0.26 seconds. Maximum RSS: 11,264 KiB. The code performed **50,456 checks**, including **8,020 final-test endpoint cases**, and generated loop-bound integers up to **599 bits**. Exact rational checks covered geometric progress inequalities, fixed-normalizer budget and conservative integer-parameter margins. Final-test checks swept d0 scales from 2^(-200) through 2^200, several rational multipliers, both allowed neighboring Up outcomes, and both extremal certified c_test errors. These were finite falsification controls, not substitutes for the inequalities above.

The scalar-normalizer sweep was ordinary floating-point numerical inspection at a in {1,2,3,4,8}, with means on a 1/32 grid. It found no discrepancy above its stated tolerance. In particular the printed zero error for large a is below floating-point resolution and is not a certificate of zero mathematical error.

Even the small parameter examples have Q_* integers with hundreds of bits. Running the complete prescribed walk or exhausting all its transcripts is infeasible within the reservation, and would not establish the asymptotic theorem anyway. No actual long walk, complete adaptive oracle experiment, exhaustive finite-ring distinguisher search, or computational-hardness experiment was run. The finite experiment certifies only its recorded finite arithmetic predicates; the core verdict rests on the independent reconstruction, with the usual limits of a non-formal proof audit.

## 11. Boundaries of this verdict

Combining the preceding arguments gives successful classical recovery on every promised pointwise input with probability at least

    1 - (n/2)exp(-kappa) - zeta,

and at most Q_* calls to the supplied bounded A. Both the exact GP and exact U laws were used; no side information or altered comparator was substituted. The scalar-evaluation model and all input-bit costs are part of this conclusion.

An average advantage over ideals does not imply a pointwise promise for every ideal. The claimed B compatibility, including its coefficient normalization and coprime quotient identification, is a separate dependency and was not independently certified by this task. The putative downstream quantum step must separately supply coherent access and approximation accounting. Nothing here changes the ideal family, establishes that bounded-index ideals contain an arbitrary worst-case family, or settles the original computational objective. External PRS/BRST attribution remains unaudited source context because the strict blind assignment prohibited retrieving those sources.

This report is complete before its hash is released. Any later correction must be a new version rather than a modification of these sealed bytes.
