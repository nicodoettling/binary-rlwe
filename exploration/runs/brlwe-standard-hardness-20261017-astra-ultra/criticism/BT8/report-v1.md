# BT8 independent blind report, v1

Review date: 2026-10-17 UTC. This report is to be sealed before substantive disclosure. No author proof, earlier review, status file, summary, ledger, or other worker's scientific output was read. No experiment was run. The hand calculations below are the finite falsification attempts.

## Exact-byte verdict

**MATHEMATICAL REDUCTION SUPPORTED; GENERAL-SCALAR FINITE SPECIFICATION QUALIFIED.**

I reconstructed the finite same-ideal BDD reduction, including a causal guided-walk argument that does not condition on all future comparison successes. I found no counterexample to the substantive BDD reduction, its Gaussian normalizations, its exact finite source/comparator interface, or its displayed probability and query bounds. The reconstruction below supports the complete claim when the final distance threshold is rational, and supports the advertised general scalar input model after the elementary verification convention stated in Section 2.

I do **not** give an unqualified exact-byte certification of the claim that the companion completely specifies every finite scalar comparison for general polynomial-time computable real inputs. Section 8 calls the test against `2d0` a rational test, although `d0` is not required to be rational. A conservative normalized interval test resolves this without changing any theorem parameter or success bound. The current wording “accept only if” can reasonably be read to permit that implementation; consequently this is a specification qualification, **not a demonstrated counterexample to the existence of the BDD reduction**. If “make this rational upper-bound test” already means a certified normalized comparison, the qualification is discharged by making that convention explicit.

The same-model review is correlated scrutiny, not formal verification or statistical independence. It certifies neither arbitrary-ideal standard hardness nor the separate composition and coherent quantum dependencies.

The exact scientific inputs reviewed were:

| Input | SHA256 |
|---|---|
| `input/multiplier-ohcp-theorem-v7.md` | `68ac0c763ebb1daa9ae4a0e8bf5d3c1fb665c130b37f36cfdb6ade0bcbcd56f2` |
| `input/multiplier-ohcp-algorithm-v1.md` | `9fe1353d605a94cb82842626b305c018b045106daec1fd16581c8bc588f94c65` |

## 1. Access and exposure record

The assignment and the two files above were the only local scientific inputs. The authorized theorem itself mentions previous versions, a causal gap, and an endpoint counterexample. I saw those mentions but did not obtain their underlying records.

Direct web opening of the [PRS author PDF](https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf) returned HTTP 502/internal errors. A direct `curl` to precisely that URL failed with DNS resolution error. Targeted search of that exact primary URL/title supplied indexed primary text for comparison construction, Definition 4.3, Proposition 4.4, and the walk discussion on printed pages 12–15. Searches intended to recover page 16 returned no result. The finite BDD argument below does not leave a step dependent on the inaccessible page: its walk tail bound is reconstructed directly.

The [BRST PDF](https://arxiv.org/pdf/2005.09595) opened successfully, including Definition 3.7 and Lemma 3.8. I used these for the formulation and normalization cross-check, not as an exact-real bit-complexity contract. The indexed PRS text explicitly contains a sentence conditioning on all comparison answers being correct; I do not import that conditioning into the proof below.

**Ancillary source exposure occurred.** Search queries constrained by the primary URL did not always constrain the search engine's returned documents. Tool responses unexpectedly included unrelated snippets/full indexed extracts, including “The Ring-LWE Problem in Lattice-Based Cryptography: The Case of Twisted Embeddings” (PMC/MDPI/DOI versions), “Classical and Quantum Security of …” (`ecvrf-security.pdf`), `smoothing.pdf`, a production lead-time paper, and unrelated Michigan teaching/research pages. I did not open these results or use them as evidence. Their appearance prevents a claim of zero ancillary web exposure; it did not expose this run, an author proof, or a prior review. Successful later searches used the exact PRS title plus the Michigan domain. No search was made for this run, its filenames, reports, or summaries.

All computations in this report are hand derivations. File reads, writing this report, and SHA256 sealing are not experiments. No experiment reservation was requested or consumed.

## 2. Preserved finite-specification issue, followed by repair

The companion permits computable real `w` and `delta`, and chooses `d0=delta*w/(32*n*k*v0)`. Thus `d0` need not be rational. Its final rule says to compute rational interval upper endpoints for the canonical moduli and test whether they are at most `2d0`, calling this a rational upper-bound test. The threshold is not necessarily rational. A fixed-precision certified interval for the modulus alone does not define an exact comparison against an arbitrary computable real threshold on every unpromised input.

Here is an exact computability obstruction to interpreting that instruction as an unrestricted exact threshold comparison. For a machine E, let theta_E be zero if E never halts, and `2^(-t-10)` if it first halts at step t. This real has polynomial-time certified absolute approximations: simulate only the requested number of steps and bound the remaining possible value. Fix positive rational dbar and set `d_E=dbar*(1-theta_E)`. For the rational endpoint `U=2*dbar`,

    U <= 2*d_E  iff  E never halts.

All values d_E remain in a fixed positive interval. They can be realized by varying w within a fixed narrow interval while keeping the other chosen parameters valid. For n=2, a rational target with a rational real coordinate can have canonical modulus exactly U; an interval `[U,U]` is an allowed certified interval. On an unpromised target the comparison can therefore genuinely lie at this boundary. The algorithm claims bounded behavior on such targets too. This obstruction concerns the exact comparison primitive, not a probability estimate or a failure on a promised BDD instance.

There are two reasons not to overstate this finding. First, the correct BDD candidate has a large margin below the threshold, and every incorrect lattice candidate has a margin above it. Second, “accept only if” permits conservative rejection of unresolved comparisons. The text therefore admits a finite implementation; it does not explicitly give the convention needed for its strongest completeness claim.

**Repair, after preserving the obstruction:** compute a certified rational interval of width at most 1/8 for each normalized modulus

    |sigma_j(T_bdd-lambda_hat)| / d0,

and accept precisely when every rational upper endpoint is at most the rational number 2. This is a bounded rational test on every input. On the correct candidate its upper endpoints are at most 9/8. Any accepted candidate still has residual at most 2d0. No other proof or parameter changes. Alternatively restrict the chosen d0 to be rational, but that restriction is unnecessary.

Everything below uses this conservative interpretation for general real scalars, or the literal test when d0 is rational.

## 3. Exact lattice and finite-law interface

For this power-of-two cyclotomic ring the coefficient embedding satisfies `E^T E=n I`. Hence canonical width w corresponds to coefficient width `b=w/sqrt(n)`. Keeping that factor is necessary throughout.

Because `D R` is contained in J, `D J^-1` is contained in R. Thus

    L=q J^-1 subset (q/D) R subset h Z^n,  h=1/(DP).

The coefficient covolume of J^-1 is 1/D. Consequently

    |h Z^n/L| = (q^n/D) / h^n = q^n D^(n-1) P^n.

Fixed nearest-grid ties are translation equivariant under h Z^n. For every exact integral multiplier r and every lambda in L, `r lambda` belongs to L, so the ideal physical query cancels lambda exactly before taking the finite quotient. The rounded source is exactly the stated rounded Gaussian law; it is not a discrete Gaussian substituted for that law.

Rounding Haar measure on the continuous torus to this grid gives exactly uniform measure on F: every finite coset has the same total cell volume. HNF/SNF representatives give a fixed finite encoding. The multiplier, auxiliary Gaussian, numerical precision choices, and sampling coins are not appended to A's input. The finite sampler's approximation is charged by statistical distance, not silently included in the source promise.

For a nonzero x in J^-1, the integral ideal `(x)J` has positive integral norm, giving `|N(x)|D>=1`. Therefore every nonzero vector of L has canonical infinity norm at least `q/D^(1/n)`. This proves both the relevant uniqueness margin and the final candidate verification argument; no short ideal basis is needed.

## 4. Both completion normalizers, and the multiplier-generator normalizer

Work first in coefficient coordinates. Let V be the positive squared-width matrix `Vcoef`, let A_h be multiplication by the displacement h, and let `b=w/sqrt(n)`. Write

    W=b^2 I + A_h V A_h^T,
    P=(V^-1 + A_h^T A_h/b^2)^-1,
    mu=P A_h^T y/b^2.

For an exact lattice Gaussian `r ~ D_(Z^n,V)`, the density of `A_h r+G_b` is

    f(y) = exp(-pi*y^T W^-1*y)
           * rho_P(Z^n-mu) / (b^n * rho_V(Z^n)).

Here rho_V and rho_P use their respective inverse squared-width quadratic forms. The continuous Gaussian proxy has density

    g(y)=exp(-pi*y^T W^-1*y)/sqrt(det W).

The determinant identity `sqrt(det P)*sqrt(det W)=b^n*sqrt(det V)` yields the full ratio

    f(y)/g(y)
      = [rho_P(Z^n-mu)/sqrt(det P)]
        / [rho_V(Z^n)/sqrt(det V)].

Neither normalizer has disappeared. The denominator is centered and its normalized theta sum lies in `[1,1+epsilon0]`. The numerator is shifted and lies in `[1-epsilon0,1+epsilon0]` once its minimum width is at least a. Integrating the ratio gives, conservatively, statistical distance at most `epsilon0/(1-epsilon0)`.

The uniform posterior bound is particularly comfortable here. When every selected displacement has modulus at most 8d0 and nuisance displacements at most d0,

    sqrt(lambda_min(P))
      >= (v0/sqrt(n)) / sqrt(1+(8*v0*d0/w)^2)
      >= 2a / sqrt(1+1/64) > a.

This uses `v0*d0/w=delta/(32*n*k)` and n>=2. It is uniform in all t>=0. The Gaussian completion remains valid when a selected displacement is zero; then the selected output width is simply w.

There is a further normalizer in generating the multiplier. With `B^2=V-a^2 I`, exact sampling first takes continuous H of width matrix B and then samples each integer coordinate from the width-a Gaussian centered at H. Its conditional denominator is `rho_(a I)(Z^n-H)`, not a constant. Replacing it temporarily by a^n and convolving gives the lattice weights of V. Uniform theta bounds, followed by normalization of those weights, bound the resulting marginal error by `epsilon0/(1-epsilon0)`. This justifies the second fixed error; it does not pretend the mixture is exactly D_(Z^n,V).

The theta bound used in both places follows directly from Poisson summation and the minimum width. For a>=sqrt(log(8n/epsilon0)/pi), put u=exp(-pi*a^2). The nonzero one-dimensional mass is at most `2u/(1-u^3)`, and the n-dimensional product minus one is less than epsilon0 for the specified epsilon0<=1/16. The actual a includes an additional unit, so the bound has slack. V has minimum coefficient width at least 2a, and B is nonsingular with minimum width at least sqrt(3)a.

Thus the fixed total distance over at most kQ_* samples is bounded by

    2*k*Q_* * epsilon0/(1-epsilon0)
      <= zeta/[32*(1-epsilon0)] < zeta/16.

These bounds hold conditionally on the existing transcript. Where the posterior bound is only local, an analysis oracle may use the continuous proxy inside the 8d0 displacement ball and the exact physical law outside. This gives a uniform coupling bound without a confinement assumption on arbitrary executions. The analysis oracle need not be computable and need not be continuous at its boundary. The later finite-position coupling uses the physical kernel, not this patch.

## 5. Profile gap, selected and zero branches, and Haar decay

Fix a coordinate pair. The continuous proxy has canonical widths

    sqrt(w^2+v0^2*exp(2t)*|e_j-g_j(z)|^2)

on that pair and fixed widths `sqrt(w^2+v0^2*|e_i|^2)` elsewhere. It therefore depends on z and t only through `exp(t)*|z-z*|`, with `z*=2+e_j/d0`. Since `|e_j|<=d0`, its norm is in [1,3]. Normalization by 3 puts the hidden center in the annulus [1/3,1]. Zero and arbitrarily tiny original coordinates are covered by the same shift; no division by e_j occurs.

At z=0,t=0, selected displacement is at most 3d0 and all others at most d0. Couple the proxy to G_w by adding an independent Gaussian. Its expected canonical norm is at most `3*sqrt(n/(2*pi))*v0*d0`. Gaussian translation distance is at most the translation norm divided by w. Thus k samples change A's acceptance probability from GP by less than delta/16. One of the two common orientations has positive starting gap at least 15delta/16, which exceeds 1/kappa. The same orientation works for every pair. The absolute comparison score is in fact invariant in distribution under complementation; running both orientations is harmless and avoids requiring that observation for sign calibration.

For Haar decay, the canonical dual is

    L* = (1/(nq)) conjugate(J).

A nonzero beta in J has `|N(beta)|>=D`. If E_s is the proxy width operator at radial log shift s relative to the starting radius, its selected widths are at least `h0*exp(s)` and its other widths at least w. Arithmetic-geometric mean therefore gives

    lambda_1(E_s L*) >= sqrt(n)*a0*exp(2s/n)
                       >= sqrt(n)*exp(2(s-S)/n).

This is why expanding only one conjugate pair can smooth the full torus: a nonzero field element has no zero embedding. It is not an assertion about the exact discrete-multiplier endpoint.

For completeness, a packing bound supplies explicit decay without an additional lattice theorem. A lattice with minimum length R has at most `(2m+3)^n` points in the shell `[mR,(m+1)R)`. For `R^2>=2n*log(5)/pi`, its nonzero Gaussian mass is at most `2*exp(-pi*R^2/2)`. For s>=kappa*log(2), the imposed bound on kappa gives

    s-S >= s/2+n+log(k+1)+5.

Substitution in the preceding packing bound makes the k-sample distance at most `exp(-s/kappa)`. For smaller s, the bound 1 suffices to obtain the advertised envelope `2*exp(-s/kappa)`. Rounding and applying A only decrease distance.

The selected two-dimensional Gaussian's width has logarithmic derivative at most one. Differentiating its density shows total-variation derivative at most 2/e<1. Hence the k-sample profile is k-Lipschitz in radial log shift, and the chosen kappa is more than sufficient. This also applies through zero as the appropriate limiting profile; the comparison proof below only uses logarithms away from a separately charged tiny-radius event.

### Exact finite endpoint falsification attempt

The following independently reconstructed counterexample rules out the stronger physical endpoint claim, and is consistent with the submitted proxy-only wording. Take n=2, J=R=Z[i], q=2, and P=m. Choose the rational displacement eta=2/m and m large enough that eta<=8d0. The query position is rational when d0 is rational and e=0. For the nontrivial finite character

    chi(y)=exp(pi*i*m*y_0),

the exact identity for every integral multiplier is

    chi(Q_(1/m)(eta*r+G)) = (-1)^(round(m*G_0)).

It is independent of the multiplier width. If the coefficient Gaussian has width b, its expectation is

    (4/pi) * sum_(ell>=0) [(-1)^ell/(2ell+1)]
             * exp(-pi*b^2*m^2*(2ell+1)^2/4),

which is strictly positive by the alternating-series bound. Thus the rounded physical law does not tend to uniform. For a local displacement, this character is extremely small and is covered by the fixed smoothing error. No repair is needed to the submitted theorem's explicit proxy-only assertion. The example also checks that it would be wrong to set the physical endpoint equal to U in the comparison analysis.

## 6. Finite empirical comparison

Use the mathematical profile anchored at the initial radius, and define

    H(s)=sup_(t>=0) (1+t)*|p(s+t)-p_infinity|.

It is finite. For s2<s1, shifting a maximizing argument of H(s1) proves H(s2)>=H(s1); this does not require monotonicity of p itself. If s1<=0 and `s1-s2>=1/Lambda_walk`, then `H(s1)>=1/C`. A maximizing t for H(s1) can be taken below `100*C*log(C)`: beyond that value the tail envelope makes the score less than 1/C. Therefore

    H(s2)-H(s1)
      >= 1/[Lambda_walk*C*(1+100*C*log(C))]
      > 1/(101*C^4) > 6/Lambda_cmp.

This proves a usable comparison margin with the submitted constants.

At the G+1 grid points, let `eta_cmp=1/(100*Lambda_cmp*M)`. Conditional on the two positions and the past, each N-call mean uses independent Bernoulli trials. Hoeffding and a union bound over both positions give a failure bound at most

    4*(G+1)*exp(-2*N*eta_cmp^2) < exp(-C).

Reuse of the endpoint empirical frequency causes no problem: it is included in that union bound and no independence of score terms is asserted. The identity `G*Delta=M` is exact. On the concentration event, empirical errors and endpoint substitution contribute less than 1/(10*Lambda_cmp), grid interpolation contributes less than 1/(10*Lambda_cmp), and the omitted tail contributes less than 1/(10*Lambda_cmp). In particular each estimated score is within 1/Lambda_cmp of H(s), uniformly for s>=-C. The inequalities follow from M>=100C log(C Lambda_cmp), the stated Delta, and C>=200.

Consequently, with conditional failure at most exp(-C), comparison returns NO for a nondecreasing distance and YES for a logarithmic decrease at least 1/Lambda_walk, whenever the current radius is at most its starting radius and the queried radii are in the allowed annulus. The strict threshold `>4/Lambda_cmp` is compatible with both margins.

This is a conditional statement about the fresh comparison coins at fixed adaptively selected positions. It is not a statement that all empirical comparisons are independent.

## 7. Causal walk proof, including the lower-radius issue

Write d=2, K=kappa+200, Lambda=Lambda_walk, T=T_walk. Consider an analysis-only corrected real walk. It generates the same fresh proposal and empirical comparison as the algorithm. It forces NO when a proposal does not decrease the true radius; it forces YES when the logarithmic decrease is at least 1/Lambda; in the interval between these cases it uses the actual empirical response. At zero radius it rejects every nonzero move. This construction is causal: it depends on the current state, current proposal, current comparison coins, and hidden center, never on future successes. It is an analysis object, not an instruction for the implemented walk.

The corrected radius is nonincreasing. Its current radius starts in [1/3,1], and every proposed radius is at most `1+1/K`. Conditional on its past, the proposal length has logarithm uniform in an interval of length 2K and minimum `exp(-2K)/(K*sqrt(d))`. Put r=exp(-Lambda). A candidate radius below r requires its length to lie in `[R-r,R+r]`, where R is the current radius. If R<=10sqrt(r), that interval misses the minimum proposal length. Otherwise its conditional probability is at most

    [log(R+r)-log(R-r)]/(2K) <= exp(-Lambda/2).

This bounds each fresh near-center event even for an adaptive current state. Before the first such event, the current and proposed radii lie in the comparison annulus, their relative log shifts are at least -C, and the current radius is at most its starting radius. The conditional probability that correction changes the empirical answer is then at most exp(-C). Sequential union bounds charge at most

    (T+1)*(exp(-Lambda/2)+exp(-C))

for any discrepancy between the corrected and uncorrected real walk. The displayed Lambda makes this less than exp(-K)/4. No conditioning on the event of no future discrepancy has been used.

Now analyze progress of the corrected process unconditionally. While R>exp(-K), choose a largest displacement coordinate, the inward sign, and an exponential numerator in `[|y_j|/2,|y_j|]`. The conditional probability of this event, given its whole past, is at least

    log(2)/(4*K*d) >= 1/(10*K*d) = p0.

On that event the logarithmic radius decreases by at least

    gamma=1/(10*K*d^(3/2)) >= 1/Lambda,

so the corrected process accepts it. Define an indicator to be one on this event before reaching the target and one automatically after the target is reached. Its conditional success probability is always at least p0. For every theta>0, iterated conditional expectation gives

    E exp(-theta*sum I_i)
       <= (1-p0+p0*exp(-theta))^(T+1).

This is the required adapted lower-tail argument. It does not multiply marginal step probabilities or restore independence by conditioning on all future successes. At most `ceil(10*K^2*d^(3/2))` progress events suffice. The mean in the displayed domination is at least `10^5*K^2*d^3`, so the elementary Chernoff bound is less than exp(-K)/4. Combined with the preceding discrepancy bound, one pair fails with probability less than exp(-K), hence less than exp(-kappa).

The local physical/proxy coupling is used only while this good corrected path has displacement below `3d0*(1+1/K)<8d0`. A first-discrepancy coupling, or the patched oracle from Section 4, supplies the fixed statistical error. Incorrect-orientation executions need no geometric guarantee: they still have their exact fixed call bound, and their candidate cannot pass verification incorrectly under the BDD promise.

## 8. Finite position quantization through the physical kernel

A finite dyadic position law and a continuous real position law have total-variation distance one. That is not the coupling used here. Couple the continuous uniform x to its Bbits-bit midpoint. The derivative of `exp(-2Kx)/(K sqrt(2))` is at most sqrt(2); including the exponential evaluation error, one step differs by less than `2*2^(-Bbits)`. If past decisions match, positions after T+1 steps differ by at most `2*(T+1)*2^(-Bbits)`.

For exact physical multipliers, a Gaussian partition-function moment bound gives

    E ||r||_canonical^2 <= n*v0^2*exp(2M).

For example, compare the partition functions at V and 2V and apply Jensen to `exp((pi/2) r^T V^-1 r)`, retaining their bounded theta normalizers. Gaussian translation distance then bounds the k-sample physical acceptance kernel's Lipschitz constant in physical z by

    k*sqrt(n)*v0*d0*exp(M)/w <= exp(M)/32.

This bound is global in the query position. It therefore remains valid for all answer sequences and does not require continuity of the analytic patch. Summing the resulting conditional discrepancies over Q_* calls, with the factor 3 for normalized positions, gives loss less than zeta/16 for the specified Bbits. In particular `exp(M)*2^(-2M)<1`; the additional factors `2^(-2K)`, 256, and 2^10 provide ample slack.

## 9. Scalar sampler and numerical-error audit

The following estimates are per physical sample with its assigned tau. They hold for every previous transcript and every input position, not merely with an average over executions.

**Std.** Couple its dyadic midpoint U to a real uniform in the same dyadic cell. The true Gaussian leaves [-H,H] with probability less than alpha. Inside that interval the density is at least ell. An early CDF decision has probability-coordinate error at most `3.5*2^(-p)<=eta`, and hence spatial error less than eps. Every non-early binary-search branch has the correct sign for the coupled real quantile. The final interval length is less than eps. Thus this primitive supplies spatial coupling, not an impossible TV approximation to a continuous law.

**UniformCap and Scalar.** For a support of length H, rejection probability per uniform proposal is below 1/2, so cap failure is at most `2^(-Rcap)`. All n*Ls potential caps cost at most tau/16. For the scalar Gaussian, centering by z0 is exact even at the explicitly specified half-integer tie. Its width-a normalizer is at least 0.9a for a>=1. Truncation outside `a*Ks+1` has mass much smaller than nu. The truncated normalizer and support size give acceptance probability at least `1/(8Ks)` after the stated dyadic acceptance perturbation. Ls therefore makes exhaustion at most `(nu/16)^5`. Perturbing acceptance weights changes the normalized accepted law by less than nu/16 using `2^(-ps)<=nu/[1024(Ks+1)]`. Together these bounds are less than nu per scalar, besides the separately charged uniform-cap failures. Integer output, fallback behavior, and translation equivariance are exact on every branch.

**Elliptical multiplier arithmetic.** Couple the n Std calls to independent true standard Gaussians Z. The union of their exceptional events has probability at most tau/64. A direct Gaussian tail bound places all true Z coordinates within Hcut except with probability below tau/128. On the remaining event,

    ||Bhat*Zhat-B*Z||_1 <= xi/2.

Indeed each of the two matrix/product errors contributes at most xi/4 from the displayed entry and coordinate tolerances. For width a, the centered one-dimensional discrete Gaussian satisfies the mean-translation variation bound `(4*pi/a)*|Delta mean|`; this follows by differentiating the normalized weights and using `E|X-c|<=2a`. Thus the total mean approximation costs at most tau/32. The n scalar errors cost at most tau/16, and the uniform caps at most tau/16. The fixed multiplier normalizer error was charged separately in Section 4.

**GridGaussian.** The finite support extends beyond the specified H_G Gaussian cutoff on both sides, even with the floor in c_l. Its discarded tails cost less than tau/(32n) per coordinate. Couple the p_G-bit midpoint to a real uniform. An approximate threshold can change a decision only in an interval of length at most `3*2^(-p_G)` around its true threshold. A union bound over all M_G thresholds gives at most `3*M_G*2^(-p_G)<=3*tau/(256n)`. This argument expressly permits inconsistent approximate CDF thresholds; it does not assume they are monotone. Binary search still has bounded depth. Summing over coordinates is less than tau/16. No support of size M_G is enumerated.

**Physical mean.** The given l1 error bound on mhat changes the continuous Gaussian law by at most tau/(64pi), before rounding or reduction. The negacyclic coefficient bound used to request the approximation is sufficient: n output coordinates, n summands each, and the factor `1+||r||_infinity` cover every multiplier branch. Exact r is retained even on fallback events, so the algebraic cancellation is never invalidated.

These bounds sum to less than tau per physical sample, with substantial unused slack. Since the counter starts by incrementing to one,

    sum tau <= (zeta/16)*sum_(c>=1) 1/(c+1)^2 < zeta/16.

A sequential coupling charges this sum conditionally on the transcript. Numerical approximation does not turn the empirical observations into iid samples by assertion; rather it couples them to the exact fresh-coin observations before applying the concentration argument.

**Elementary evaluation.** For the stated CDF routine, clipping beyond p+4 has error smaller than 2^(-p). On the remaining interval, the fixed Taylor order exceeds `100*(|x|+1)^2` and `100p`; the factorial bound makes the exponential-series remainder smaller than the requested error. The specified guard precision dominates both cancellation, of order `exp(pi*x^2)`, and accumulated arithmetic error. The argument approximation is safe because the width-one Gaussian CDF is 1-Lipschitz. This routine needs no real equality test. Up always lies between ceil(x) and ceil(x)+1, so its conservative use increases precision/cutoffs rather than reducing them. The final threshold issue in Section 2 is the sole scalar-comparison qualification found.

## 10. Reconstruction, acceptance, cost, and quantifiers

For a successful normalized walk, each pair's z error is at most `3*exp(-K)` and the corresponding e error at most `3*d0*exp(-K)`. Inverting the canonical embedding bounds every coefficient error by the canonical infinity error. Since d0<w and `3*w*exp(-kappa)<q/(8D)`, adding the conversion error q/(64D) leaves total coefficient error below q/(2D). Every coordinate of lambda belongs to `(q/D)Z`; nearest-grid rounding therefore recovers it exactly.

A returned candidate has exact membership in L and residual at most 2d0. The true lambda has residual at most d0. Their difference, if nonzero, would have infinity norm at most 3d0, strictly below `q/D^(1/n)`. Thus every accepted candidate is the correct one. The correct candidate passes the conservative verification with margin. Incorrect orientation can neither cause an incorrect accepted answer nor prevent the other fixed finite walk from being run.

There are n/2 pairs and two orientations, hence n walks. Each walk has T_walk+1 comparisons, each comparison exactly `2*(G+1)*N` A calls. The resulting bound is exactly Q_*=nQ_H. The maximum logscale is exactly M. All loops remain bounded on every answer sequence, including all NO, all YES, and incorrect-orientation executions. The normalized verification convention is needed to make this statement explicit for arbitrary real scalars on unpromised targets too.

All loop bounds in the comparison/walk are polynomial in kappa. Gaussian widths of order exp(M) require O(M) magnitude bits, not exp(M) operations. The scalar proposal counts are polynomial in logarithmic error budgets; UniformCap is capped; both Gaussian CDF searches are logarithmic in support range. The CDF is evaluated only on a clipped polynomial-size interval. Exact multiplier coefficient sizes, mean precision, inverse embedding precision, and HNF/SNF arithmetic have polynomial bit bounds in the full declared inputs and requested precision. No factorization or short-basis oracle is introduced. The stated inclusion of full scalar encodings and actual certified evaluation costs is essential; I do not replace it by a bound in the logarithm of a displayed scalar value.

There is no parameter cycle: v0*d0=h0 is fixed before choosing v0, and Q_* is fixed before epsilon0. A finite conservative choice of v0 can enforce the strict d0 inequality by an upper approximation plus a positive rational margin. The rounding and sampling grid depends on P through its binary length. No coprimality of D and q is used in this BDD argument.

Union-bound the good orientation's n/2 walk failures and add the global normalization, position-quantization, and numerical couplings. The three latter charges are each below zeta/16, so their sum is less than the advertised zeta. This yields the submitted bound

    Pr[recover lambda] >= 1-(n/2)*exp(-kappa)-zeta.

The assertion is pointwise in J. Average-family advantage does not give it for every ideal. The dual identity above checks the algebraic scaling `nq*sqrt(n)/(sqrt(2)*d0)` for a separately justified BDD-to-DGS import onto J. This review does not supply coherent access, gate-error accounting, the separate composition theorem, or an arbitrary-ideal family reduction.

## 11. Finite falsification dispositions

Each probability family was subjected to a finite-support or exact boundary check where feasible. No numerical experiment was substituted for a probability proof.

| Claim tested | Exact hand falsification attempt | Disposition |
|---|---|---|
| Adaptive progress | Two independent fair bits, then condition on their sum being one. Both conditional marginal success probabilities are 1/2 but simultaneous success has probability zero. | Refutes multiplying marginals or retaining independence after future-success conditioning. The causal corrected process and conditional exponential-moment induction in Section 7 avoid this failure. |
| Empirical comparison | With nondegenerate Bernoulli responses, the finite event that one profile's relevant N bits are all one, its endpoint bits all zero, and the other profile's bits all zero can create a false YES at equal true distance. | Deterministic no-growth is false for the implemented comparison. The theorem retains the required failure allowance; conditional Hoeffding covers this event. |
| Uniform integer cap | H=3,Rcap=1 gives probabilities 1/4 each for 0,1,2 and 1/4 failure. Replacing failure by 0 gives (1/2,1/4,1/4), at distance 1/6 from uniform. | Confirms fallback bias is real and must be charged. It is below the failure bound and the submitted capped-rejection accounting. |
| CDF threshold consistency | Two true equal thresholds at 1/2, approximated by 1/2+eta and 1/2-eta, are nonmonotone. | A monotone-approximation proof would fail. The union of threshold uncertainty intervals used in Section 9 remains valid. |
| Continuous finite quantizers | A finite rational Gaussian output or dyadic walk increment has finite support, whereas its real reference has no atoms. | Their TV distance is one. The argument uses spatial coupling followed by a smooth physical kernel, not a false direct TV bound. |
| Scalar centering/fallback | Means differing by an integer, including half-integer centered means, translate z0, all proposals, and every fallback by exactly that integer. | The stated mixed tie conventions do not break integer equivariance or ring membership. |
| Gaussian normalizers | At a scalar lattice, centered and half-shifted theta sums differ: their difference is a positive sum of odd Fourier terms. | Dropping either denominator would give a false exact identity. Section 4 retains them and bounds their effect. |
| Physical endpoint | The finite character example in Section 5 is independent of multiplier scale and has strictly positive expectation. | Refutes exact physical Haar convergence, which v7 expressly does not claim. The proxy-only claim survives. |
| General-real verification | The computable-real family d_E in Section 2 makes an unrestricted exact rational-endpoint comparison decide nonhalting. | Exposes the final finite-test specification ambiguity. Normalized certified interval comparison resolves it. |
| Global accumulation | Every error bound is conditional on the current transcript; the global counter gives a convergent deterministic budget even on arbitrary answer sequences. | Finite correlated histories cannot defeat the sequential union/coupling bound. No independent-failure product is used. |

The actual empirical and walk supports are astronomically large but finite; exhaustive enumeration is neither feasible nor authorized. Their finite-support lower-tail statements were proved by conditional moment bounds rather than inferred from a tiny simulation. Gaussian tail and lattice-theta bounds concern infinite reference laws; finite truncations cannot certify those laws by enumeration. The explicit tail inequalities and the normalizer/endpoint counterexamples above are the relevant falsification checks for those claims.

## Final disposition

The substantial mathematical reconstruction succeeds, including the potentially delicate causal walk, approximate finite samplers, exact finite interface, and all selected/zero-coordinate cases. The one requested textual completion is to make the final test rational for nonrational d0, preferably by normalizing the certified modulus before comparison. Preserve the computable-real threshold obstruction when making that change. No changes to the stated radius, call count, or probability constants are indicated by this review.

This report ends here. Its sealed bytes must not be edited after the SHA256 receipt is produced.
