# BT10 blind referee report, version 1

**Verdict: ACCEPT the core finite, pointwise BDD assertion for the two exact input files identified below, under their expressly declared scalar-evaluation and bounded-oracle-runtime model.** I independently reconstructed a correctness argument for the specified finite algorithm, including a causal guided-walk argument. I found no counterexample to this assertion. This verdict does not certify the unread author proof, the separate bridge called B, coherent quantum implementation, or an arbitrary-ideal standard-hardness theorem.

This is a fresh same-model blind review, not formal verification and not statistically independent evidence. The complete report is to be SHA256-sealed before any substantive result is sent to the coordinator. After sealing, this version must not be modified.

The exact reviewed scientific inputs are:

- `input/multiplier-ohcp-theorem-v8.md`, SHA256 `857a62e9f4a937a80e5cb3b115c8b132abf122c16665d29b39dcb62bde86fe0a`.
- `input/multiplier-ohcp-algorithm-v2.md`, SHA256 `4361c90a7fa7cfe25d0ab3e8cd5c5333fb474cf1fb764375e10c29fca5102735`.

I also read the administrative assignment. I did not read the author proof, prior reviews, run summaries, status files, ledgers, or other worker files. No other local scientific input was used.

## 1. Scope and exact finite laws

Write `E` for the real canonical embedding, with the real coordinates of each complex pair multiplied by `sqrt(2)`. Then `E^T E=nI`. Consequently a canonical width-w spherical Gaussian has independent coefficient coordinates of width `b=w/sqrt(n)`. This interpretation also makes the companion's normalized transform `U=E/sqrt(n)` orthogonal and gives its stated multiplier covariance matrix.

Since J is an integral ideal of index D, `D J^-1` is contained in R. Hence `L=qJ^-1` is contained in `(q/D)R`, which is contained in `hZ^n`, where `h=1/(DP)`. The coefficient covolume of L is `q^n/D`. Therefore

`|hZ^n/L|=(q^n/D)/h^n=q^n D^(n-1)P^n`.

Nearest-grid rounding with the specified tie rule commutes with translations by every element of L. Haar measure on the real torus modulo L therefore rounds to exactly uniform measure on F: the grid cells have equal volume and tile that torus. Thus the comparison distribution in the theorem really is the exact finite uniform distribution, not a continuous surrogate silently given to A.

For every exact integral multiplier r, including zero and nonunits, `r lambda` belongs to L. Thus

`Q_h(r(T_bdd-g)+G_w) mod L = Q_h(r(e-g)+G_w) mod L`.

No cancellation by division, invertibility of r, short ideal basis, or coprimality condition is used. The implemented approximation to the mean is charged before rounding and reduction, so it does not have to preserve that identity exactly at the numerical level. The integral multiplier itself does preserve it on every branch, including all fallbacks.

The source GP is an exact probability law on a finite set; its cell probabilities can be irrational. The reduction only approximates the physical sampling law. This distinction is legitimate because the approximation errors are explicitly bounded in total variation, including when A is an arbitrary bounded randomized function of the whole k-tuple.

## 2. All Gaussian normalizers

Work temporarily in coefficient coordinates. Let A be the positive multiplier width matrix, so `A^2=Vcoef`, let H be the real multiplication matrix for `e-g`, and put

`S^2=b^2 I+H A^2 H^T`,

`Cpost^2=(A^-2+b^-2 H^T H)^-1`,

`mu=Cpost^2 H^T y/b^2`.

For a positive width matrix W, define `rho_W(x)=exp(-pi ||W^-1 x||^2)` and `theta_W(c)=rho_W(Z^n-c)/det(W)`. Completing the square gives the exact physical density

`f(y)=[rho_S(y)/det(S)] * theta_Cpost(mu)/theta_A(0)`.

In particular, the numerator is the full shifted posterior lattice sum, and the denominator is the full original discrete-Gaussian normalizer. Neither is omitted. The formula uses `det(Cpost) det(S)=det(A) b^n`. It remains valid when H has zero eigenvalues, including H=0; only A and the added Gaussian width need be positive.

The chosen a gives `|theta_W(c)-1|<=epsilon0` for every shift c whenever the smallest singular value of W is at least a. One elementary derivation is Poisson summation followed by the bound on the nonzero Gaussian mass of `Z^n`. If `u=exp(-pi a^2)<=epsilon0/(8n)`, the one-dimensional sum is at most `1+3u`, and `(1+3u)^n-1<epsilon0`. This also applies to non-diagonal W by singular-value domination.

Here A has smallest singular value at least `v0/sqrt(n)>=2a`. In canonical coordinates the posterior width in embedding i is

`(v_i^-2+|e_i-g_i|^2/w^2)^(-1/2)`.

For the selected pair `|e_j-g_j|<=8d0`, and for the other pairs `|e_i-g_i|<=d0`. Consequently its coefficient minimum width is at least

`v0/[sqrt(n) sqrt(1+(8v0 d0/w)^2)] > a`,

because `8v0d0/w=delta/(4nk)<=1/8`. This estimate is uniform for all `t>=0`. The full-normalizer formula consequently bounds the physical-versus-continuous-proxy variation distance by `epsilon0/(1-epsilon0)` per sample; rounding and reduction can only decrease it.

There is another normalizer in the integral-multiplier implementation. Let `B^2=A^2-a^2 I`, draw continuous `H0` of width matrix B, and then draw independent integers from the shifted scalar Gaussians of width a and means `H0_l`. The denominator in this conditional law is `rho_a(Z^n-H0)`, not a constant. Replacing it by `a^n` makes the marginal unnormalized mass of r equal to `rho_A(r)/det(A)`. Retaining it and comparing the resulting normalized law with `D_{Z^n,A}` gives another error at most `epsilon0/(1-epsilon0)`. This uses both `theta_a(H0)` and `theta_A(0)`; it is not an assertion that the convolution is exactly discrete Gaussian.

The sum of these two fixed approximation errors over all generated samples is bounded by

`2 k Q_* epsilon0/(1-epsilon0) <= zeta/30 < zeta/16`.

No exact endpoint limit for the physical discrete multiplier is needed or proved.

## 3. The radial proxy and its endpoint

For a pair, put `u=z/3` and `u*=z*/3`. Then `1/3<=||u*||<=1`. The selected displacement is `3d0(u*-u)`. The continuous proxy therefore has selected canonical width

`W_j(s)=sqrt(w^2+9h0^2 exp(2s))`, where `s=t+log||u-u*||`,

and nuisance widths `sqrt(w^2+v0^2 |e_i|^2)`. Its acceptance probability is a function p(s). The nuisance widths remain fixed throughout that pair's walk. At the exact center the selected width is w; formulas using logarithmic distance are only needed at nonzero distance.

At s=0 all extra Gaussian widths are at most `3h0`. Coupling this proxy with the original width-w Gaussian by adding the extra Gaussian bounds one-sample variation distance by

`3 h0 sqrt(n/(2pi))/w = 3delta/[32k sqrt(2pi n)] <= delta/(32k)`.

Thus the k-tuple changes A's acceptance probability by at most `delta/32`. Choose the single global orientation for which A's GP-minus-U gap is positive. It gives `p(0)-p_infinity>=delta/2>=1/kappa` for every pair. This is the same orientation for all pairs; no coordinatewise sign selection is hidden here. The algorithm also runs the other orientation, which only affects the number of calls and the verification step.

Only the selected two-dimensional Gaussian factor changes with s. Its logarithmic width derivative is at most one. Differentiating its density shows that its variation distance is at most the change in s; tensoring k samples gives a Lipschitz constant at most k, safely below kappa. Rounding, modular reduction, and applying A do not increase this bound.

For endpoint smoothing, the Euclidean dual of L in canonical coordinates is `(1/(nq)) conjugate(J)`. For every nonzero a in J, `|N(a)|>=D`. If W is the proxy width operator, AM-GM applied to all n embeddings therefore gives, for every nonzero dual vector y,

`||Wy||^2 >= n a0^2 exp(4s/n) >= n exp(4(s-S)/n)`.

The discarded factor `3^(4/n)` only strengthens this inequality. This explicitly explains why increasing one conjugate pair can smooth the whole torus: a nonzero field element has no zero embedding, and its algebraic norm controls the product of the dual coordinates.

For a lattice whose shortest vector has squared norm at least `n v`, with `v>=1`, a disjoint-ball count in successive shells bounds its nonzero Gaussian mass by

`sum_{m>=1}(2m+3)^n exp(-pi m^2 n v) <= 2 exp(-n v)`.

Poisson summation then bounds the proxy's distance from Haar by `exp(-n v)`. For `s>=kappa/2`, the parameter inequalities imply `S<=s/2`, `n<=s/2`, and `log k<=s/2`; hence

`k exp[-n exp(4(s-S)/n)] <= exp(-s/kappa)`.

For smaller s, the bound `2exp(-s/kappa)` is at least one until a range already covered by that estimate. Therefore, for all real s,

`|p(s)-p_infinity| <= 2exp(-s/kappa)`.

Rounding Haar gives exactly U, as established above. The endpoint here belongs to the continuous proxy. As a negative control, for `n=2`, `J=Z[i]`, `q=2`, `P=1`, and physical displacement 2, every integral r satisfies `2r=0 mod 2Z[i]`. The physical output is then exactly GP for every multiplier width. Taking, for example, `w=1/4` makes its rounded law plainly nonuniform. This exact identity would refute an unqualified physical-Haar endpoint assertion, but that assertion is explicitly excluded in the reviewed theorem. It is not a counterexample to the theorem's local approximation argument.

Define an analysis oracle equal to the proxy inside selected-displacement radius `8d0` and equal to the exact physical kernel outside it. This gives a globally defined oracle whose distance from the physical oracle is uniformly bounded, even at unknown or erroneous query positions. Its behavior is radial on the entire region needed for the walk. Its boundary need not be continuous.

## 4. The exact empirical comparison

Let `lambda=Lambda_walk`, `Lcmp=Lambda_cmp`, and define

`Hscore(s)=max_{t>=0}(1+t)|p(s+t)-p_infinity|`.

This maximum exists by the tail bound. Directly shifting the same evaluation point shows Hscore is nonincreasing. If `s1<=0`, then `Hscore(s1)>=1/K` by the gap at zero. For `s1>=-lambda`, every maximizer lies below M: the bound

`(1+t)|p(s1+t)-p_infinity| <= 2e(1+t)exp(-t/C)`

for `t>=M` is much smaller than `1/K` with the stated M. If `s2<=s1-1/lambda`, evaluating at the shifted maximizer consequently yields

`Hscore(s2)-Hscore(s1) >= 1/[lambda K(1+M)] > 8/Lcmp`.

The last strict inequality follows from `Lcmp=10000 C^4`, `lambda,K<=C`, and `M=100 C ceil(log2(10000 C^5))`; already for `C>=200`, `1+M<1250 C^2` suffices. In the actual parameter range C is far larger.

The exact identity `G Delta=M` holds. Set `eta=1/(100 Lcmp M)`. For either queried position, Hoeffding's bound and a union bound over all sampled points show that every empirical frequency is within eta of its true mean, except with probability at most

`4(G+1) exp[-2(C+ceil(log2(8(G+1))))] < exp(-C)`.

The endpoint bias is at most eta. The Lipschitz and grid errors, after multiplying by `1+t`, are below `1/Lcmp` in total, including the omitted tail beyond M. One can use the bounds `6M eta` for the two sampled frequencies plus endpoint bias, `3MC Delta` for interpolation, and `1/(100Lcmp)` for the omitted tail. These are collectively well below `1/Lcmp`.

Thus the two computed scores each approximate Hscore within `1/Lcmp`. The strict decision threshold `4/Lcmp` rejects every nonimproving proposal on this good event. It accepts every proposal improving log distance by at least `1/lambda`. Correlations caused by reusing the empirical endpoint inside a score do not matter: the proof uses simultaneous frequency bounds, not independence of score differences.

These guarantees are conditional on every fixed past transcript and the current two positions. Fresh samples and fresh A coins are exactly what permits the same Hoeffding bound after adaptive selection of positions.

## 5. Causal guided-walk argument

The following is an independent argument for the supplied loops. It does not condition a fresh step on all future comparisons succeeding and does not multiply marginal progress probabilities.

First consider real uniform X and the exact physical/patched oracle. Define a corrected walk only for analysis: if an empirical comparison would accept a nondecreasing-distance move, force rejection; if it would reject a move whose log-distance improvement is at least `1/lambda`, force acceptance. In the intermediate range retain the empirical decision. This corrected walk is defined on every past history, is always nonincreasing in distance, and guarantees acceptance of the specified progress moves. It is not an implemented distance test.

Let `r_i=||u_i-u*||`. Initially `1/3<=r_0<=1`, and the corrected walk keeps `r_i<=1`. The maximum step is `1/(K sqrt(2))`, so every proposed distance is at most `1+1/K` and remains well inside the radial patch.

There is a uniform small-ball estimate for each new real step. Put `epsilon=exp(-lambda)`. If its proposed position is within epsilon of the center, its length must lie in `[r_i-epsilon,r_i+epsilon]`. When `r_i<=10exp(-lambda/2)`, the minimum permitted step length `exp(-2K)/(K sqrt(2))` is larger than that interval's upper endpoint. Otherwise, log-uniformity of the step length bounds the conditional probability of this event by

`epsilon/[K(r_i-epsilon)] <= exp(-lambda/2)`.

This estimate is valid given the complete past and does not involve future correctness. Until the first such event, both current and proposed log distances are at least `-lambda`, so each erroneous forced correction has conditional probability at most `exp(-C)`. A first-failure union bound therefore couples the actual and corrected walks except with probability at most

`(T_walk+1)[exp(-lambda/2)+exp(-C)]`.

Now analyze progress in the corrected walk, without any conditioning on that coupling event. While `r_i>exp(-K)`, a coordinate of `y=u*-u_i` satisfies `|y_j|>=r_i/sqrt(2)`. With conditional probability

`(1/2)(1/2) log(2)/(2K) = log(2)/(8K) > 1/(20K)`,

the step selects that coordinate, its correct sign, and an exponential numerator between `|y_j|/2` and `|y_j|`. The corresponding X interval lies in `[0,1]`, since `r_i<=1` and `r_i>exp(-K)`. On this event the norm decreases by a log amount at least `1/(16K)`, which exceeds `1/lambda`. The corrected walk must accept it.

Let an indicator be one whenever this progress event occurs or the walk has already reached `exp(-K)`. Given the complete past, its conditional success probability is at least `p=1/(20K)`. Iterated conditional expectation gives the usual Bernoulli exponential-moment bound, hence a lower-tail probability at most `exp[-(T_walk+1)p/8]` for fewer than `(T_walk+1)p/2` successes. This is a conditional-probability argument, not an independence assumption. The supplied `T_walk=16*10^6 K^3` makes that number vastly exceed `16K^2+1`, which is sufficient to reach radius `exp(-K)` from radius at most one. Thereafter monotonicity retains the radius bound.

The explicit lambda and C make the coupling failure and this progress failure collectively less than `exp(-kappa)` for one pair. For example, each is far smaller than `exp(-K)/4` in the allowed range, and `K=kappa+200`. This proves the necessary real-walk success bound with substantial slack. A union bound over the n/2 pairs of the good global orientation gives the theorem's `(n/2)exp(-kappa)` term. Nothing is assumed about the incorrect orientation's answers.

## 6. Finite scalar sampling and numerical errors

The scalar specifications terminate on every branch. Their approximation claims can be established without an exact-real sampling primitive.

**CDF evaluation.** The integrated exponential series with the supplied order is ample. On the unclipped interval, write `v=pi x^2`; the order is at least `25v` and at least `100p`. Factorial bounds make the Taylor remainder much smaller than `2^-p`. The prescribed guard precision dominates cancellation and arithmetic errors. For `|x|>=p+4`, the Gaussian tail is smaller than the requested accuracy. Argument approximation is harmless because the width-one CDF is 1-Lipschitz. A bounded rational comparison after argument approximation, or evaluation on the small boundary overlap, avoids any real equality test. The other elementary functions likewise require only ordinary certified precision computations.

**Std.** Couple its p-bit midpoint uniform to a continuous uniform with discrepancy at most `2^(-p-1)`. Outside the Gaussian tail of mass at most alpha, the inverse CDF lies in `[-H,H]`, where its density is at least ell. An early return has CDF discrepancy at most `3.5*2^-p`, so its value error is less than eps by the definition of eta. Every non-early comparison has the correct sign relative to the continuous quantile. The fixed number L of bisections then gives value error below eps. Endpoint clipping is also covered by the same tail/error estimate. No indefinite precision-refinement loop occurs.

**Scalar.** The shifted Gaussian normalizer for `a>=1` is at least `0.9a`. The omitted mass outside `[-Ns,Ns]` is less than `nu/16`. The sum of all weight approximation errors is at most `5a Ks 2^-ps`; normalization changes the accepted distribution by less than `nu/100`. Its per-trial acceptance probability is at least `1/(15Ks)`, so the Ls cap has probability less than `nu/16`. Together these errors are below nu. This argument analyzes the normalized accepted distribution; it does not incorrectly multiply weight error by an arbitrarily long rejection time. The centering convention and all fallbacks are exactly equivariant under integer shifts of the mean.

**UniformCap.** Each trial accepts with probability at least one half, and accepted outputs are exactly uniform conditional on success. All-failure probability is at most `2^-Rcap`. There are at most `n Ls` such calls in one physical sample, so the total associated fallback probability is at most `tau/16`. Returning the center on a failure is therefore covered, rather than silently treated as a public abort.

**Elliptical multiplier arithmetic.** Couple the standard Gaussians and their finite approximations. The total Std failure probability is at most `alpha_H/4`, and the probability that any true coordinate exceeds Hcut is at most `alpha_H/8`. On the complementary event, the specified matrix and scalar precisions give `||Hhat-H0||_1<=xi/2`. For a shifted scalar discrete Gaussian of width `a>=1`, differentiating the normalized mass function bounds its variation distance under a mean shift by `(4pi/a)` times the shift. For example, the elementary estimate `E|X-c|<=2a` proves this bound. Hence the joint mean-approximation cost is at most `tau/32`. Together with scalar and uniform-cap errors, the numerical multiplier cost is comfortably below tau.

**GridGaussian.** The chosen support leaves at most `tau/(32n)` tail mass per coordinate. Couple the dyadic uniform with a continuous one. An incorrect threshold decision can occur only when that uniform is within `1.5*2^-p_G` of some true threshold. Union over at most M_G thresholds bounds this probability by `3 M_G 2^-p_G`, even if the approximate threshold list is not monotone. Away from these bands every binary-search decision agrees with the exact CDF, so no monotonicity of the approximations is required. The combined n-coordinate error is below `tau/16`. Only a logarithmic number of thresholds is evaluated; the support is not enumerated.

**Physical mean.** The prescribed coefficient precision before exact negacyclic multiplication gives the displayed l1 mean error. A coefficient Gaussian of width b changes by variation distance at most the l1 mean displacement divided by b. This costs at most `tau/(64pi)`. Rounding and reduction introduce no further distance.

These estimates jointly leave ample room below tau for the numerical error of one complete generated physical sample, in addition to the two fixed normalizer errors already separated above. They hold conditionally on the full transcript, including extreme means, zero multipliers, and every bounded fallback. The global counter implies

`sum_{c>=1} tau_c = (zeta/16) sum_{c>=1} 1/(c+1)^2 < zeta/16`.

The counter is not reset across pairs or orientations. Thus adaptive generation does not consume an unaccounted fresh budget at every restart.

## 7. Finite walk quantization and total success

The globally Lipschitz object used for quantization is the exact physical kernel, not the discontinuously patched oracle. For an exact multiplier, differentiation of its Gaussian normalizer under overall scaling gives

`E ||A^-1 r||^2 <= n/(2pi)`.

Only the selected canonical pair contributes to the change in mean when u changes. Gaussian shift distance and the moment bound yield a k-sample physical acceptance Lipschitz bound no larger than

`[3delta/(32sqrt(2pi n))] exp(t) ||u-u'|| <= exp(M)||u-u'||`.

This is global in u and requires no query-confinement assumption.

Couple real X with its Bbits-bit midpoint. The exact step-length function has derivative bounded by `sqrt(2)`; including the finite exponential evaluation, the per-step length discrepancy is less than `2*2^-Bbits`. As long as accept/reject bits are coupled, accumulated position discrepancy after m steps is at most `2m*2^-Bbits`. The union bound over all Q_* oracle calls therefore gives an additional mismatch probability at most

`2 Q_* (T_walk+2) exp(M) 2^-Bbits < zeta/16`.

The terminal position discrepancy is also much smaller than `exp(-K)`. Since `K=kappa+200`, a successful real walk and its coupled finite walk yield selected-coordinate error at most `3d0 exp(-kappa)`.

The order of this argument matters: finite numerical sampling is compared with the exact physical kernel; finite steps are compared with real steps through that physical kernel; the real physical kernel is then compared with the globally defined patch; and the causal corrected walk is analyzed there. No continuity of the patch and no assumption about all future successful comparisons is used.

The three extra global charges established above are each below `zeta/16`: fixed normalizers, summable finite sampling, and walk quantization. Their sum is below zeta, with substantial unused slack. Adding the good orientation's n/2 walk failure terms yields at least

`1-(n/2)exp(-kappa)-zeta`.

## 8. Reconstruction and the revised final test

On the good event, every canonical coordinate of the estimated error differs from the true error by at most `3d0 exp(-kappa)`. Inverse Fourier conversion has coefficient infinity norm at most canonical infinity norm. Also `d0<w`; hence the theorem's strict condition gives coefficient error less than `q/(8D)`. Adding the specified coefficient-conversion error `q/(64D)` still leaves error strictly below half the grid spacing `q/D`. Since lambda belongs to `(q/D)Z^n`, nearest-grid rounding therefore recovers exactly lambda, not merely a close lattice vector.

For the final test, the fixed Up computation indeed implies `eps_test<=d0/256`, including the `p_test=0` branch. Thus

`(255/256)d0 <= c_test <= (257/256)d0`,

`d_lower>= (127/128)d0>0`.

If the candidate is the true lambda, every canonical residual modulus is at most d0. Its certified rational upper endpoint is at most `d0+d_lower/8`, which is strictly below `3c_test/2` throughout that whole interval for c_test. Therefore the true candidate is accepted, even at the boundary of the BDD promise.

If any candidate passes, its actual residual is at most `(771/512)d0`. A distinct accepted lattice vector and the true lambda would consequently differ by a nonzero element of L with canonical infinity norm at most `(1283/512)d0`. But every nonzero element of L has canonical infinity norm at least `q/D^(1/n)>4d0`: indeed, for nonzero a in `J^-1`, the integral ideal aJ has norm at least one, so `|N(a)|>=1/D`. This is a contradiction.

Thus the other orientation cannot cause an incorrect return on a promised target. Exact membership, rational threshold comparisons, and fixed-width residual enclosures all terminate off promise as well. In particular, this revision contains no comparison of a rational endpoint with an unresolved computable-real boundary.

## 9. Bit complexity and side statements

All A-call counts are exact: a comparison uses `2(G+1)N` calls, a walk uses `Q_H`, and the n walks across both orientations use `Q_*=nQ_H`. Generated sample count is at most `kQ_*`. The n/2 correct-orientation successes are used for probability, whereas both orientations are counted for runtime and all error budgets.

The log-scale grid ends exactly at M. Every walk position, including in the incorrect orientation or on an off-promise target, has norm bounded by its initial norm plus `(T_walk+1)` times the maximum finite step. Thus arithmetic precision and output lengths do not secretly depend on successful confinement. Exponentials up to M have bit length polynomial in M; accumulated rational position denominators have polynomially bounded length. The multiplier sampler has bounded standard-Gaussian outputs, bounded scalar supports around its means, and bounded rejection counts. Its integer output lengths are therefore polynomial in the stated parameter magnitudes and the full scalar encodings. The Gaussian-grid support may be huge, but its binary length and the binary-search cost are the relevant quantities.

HNF/SNF, ideal inverse construction, negacyclic multiplication, exact membership, and all rational operations have ordinary polynomial bit costs in the supplied basis and target encodings and their intermediate bit lengths. The explicit integer quantities are polynomial in kappa; `n<=kappa/4` and `k<=kappa/2` where needed. All numerical precisions are polynomial in M, log of the global sample count, the declared accuracy parameters, and the full relevant scalar bit lengths. The specification explicitly includes certified evaluation costs and assumes polynomial-time scalar representations; I do not replace this with a weaker magnitude-only input model. The Up conventions avoid unbounded exact-real boundary decisions.

For example, simplifying a0 gives `a0=D^(1/n) w (delta/(32nk))^(2/n)/(nq)`. The S condition implies `log(1/w)<=kappa/(2n)+(log D)/n`. Also `delta>=2/kappa` and `log(1/zeta)<=kappa`. These bounds control precision for small positive widths and probabilities even when their certified representations are not explicit rationals. The known positive lower bound on v0 and a rational upper bound obtained by certified evaluation similarly control the precision needed for d0; the cost and output length of that evaluation are expressly counted. None of these computations needs to decide equality of an unspecified real with zero.

The separate compatibility paragraph does not enter any step above. Its equality `w_B=w/sqrt(n)` is consistent with the embedding. If `gcd(D,q)=1`, the natural map `R/qR -> J^-1/qJ^-1` is an isomorphism because the finite additive quotient `J^-1/R` has order D; this checks the stated identification, but does not prove the unspecified bridge B's output law.

The downstream stated DGS width has the expected normalization: a Euclidean BDD oracle of radius d0 on L would produce width `sqrt(n)/(sqrt(2)d0)` on `L*=(1/(nq)) conjugate(J)`, and scaling and conjugating gives `nq sqrt(n)/(sqrt(2)d0)` on J. Establishing coherent access and controlling state/gate error remain separate. No change of ideal family follows from this calculation, and no arbitrary-family hardness statement is certified here.

## 10. Finite falsification work and its limits

The coordinator reserved BT10-FV1 before execution: one foreground light Python job, at most 60 seconds and 512 MiB. Its code, embedded exact inputs, invocation, original stdout/stderr, and `/usr/bin/time -v` record are preserved under `experiments/`. It passed 1,636 exact rational/integer checks. The job used 0.04 seconds wall time and 12 MiB peak RSS. No installation, heavy job, detached process, or additional worker was used.

The checks cover:

- Exact grid endpoint and call-count identities at six confidence values, and the conservative comparison/progress margins there.
- Exhaustive cardinality 180 for `hZ[i]/(2/(2+i))Z[i]` with `D=5`, `P=3`, plus exact ideal cancellation and rounding equivariance, including ties, for zero, units, and nonunit multipliers.
- Exhaustive finite capped-uniform rejection trees for 27 small support/cap combinations.
- Exact finite accept/reject mass and normalized accepted-law identities for a dyadic weight table.
- The revised rational verification margins, including the exact false-candidate factor `1283/512`.

These tests did not simulate the complete reduction. For example, already kappa=32 gives a walk length near `2*10^14` and a 501-bit Q_H. Nor did they exhaust all possible distinguishers, ideal inputs, or scalar-evaluation programs. Those universal claims require the analytical arguments above; the finite checks only test tractable component identities and branches. No numerical Gaussian-integration evidence or unreserved experiment is used to establish the verdict.

No fatal counterexample to the reviewed assertion was found, and no repair is proposed. The physical-endpoint negative control in Section 3 is preserved as an exact excluded-claim example, not reclassified as a failure of these bytes.

## 11. Primary access and exposure record

Permitted primary sources were [PRS, Pseudorandomness of Ring-LWE for Any Ring and Modulus](https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf) and [BRST, Continuous LWE](https://arxiv.org/pdf/2005.09595). Direct PRS PDF access returned gateway errors; a local curl attempt failed DNS resolution. Targeted primary-title/URL searches recovered indexed text from the exact PRS primary URL for its comparison construction and pages 12–16, including Definition 4.3 and Proposition 4.4. BRST was directly accessible; Definition 3.7 and Lemma 3.8 were read. The direct PRS PDF binary was not obtained or hashed. The proof in this report is independently reconstructed from the supplied definitions, rather than importing an exact-real bit-complexity contract from either paper. In particular, Section 5 supplies its own causal argument instead of relying on a conditioning shortcut in the indexed walk discussion.

The search engine also returned unrelated snippets despite document-targeted queries. These were visible accidental exposure and were not used as evidence: Michigan Ring-LWE challenge/course pages, lattice-paper snippets from `lwehard-old.pdf`, `toolkit.pdf`, `deniable.pdf`, `circinsec.pdf`, `ideal-lwe.pdf`, `suite.pdf`, and `robustlwe.pdf`; third-party Ring-LWE/signature/twisted-embedding surveys and bibliographies at Springer, ResearchGate, MDPI/PMC, OUCI, Wiley, Studylib, Google Patents, DOI/ACM, and Dokumen; and unrelated Michigan teaching, evolving-algebra, matching, image-processing, text-classification, database, thread-scheduling, sensor-scheduling, signaling-pathway, serial-line, and reliability snippets. Some results contained more than a title/snippet, notably the listed lattice PDFs, but none was imported into the analysis. No search was made for the run, its filenames, reviews, summaries, or workers.

The allowed theorem itself contains revision-history references and mentions earlier defects. Their underlying files were not opened. No prohibited local scientific material was accidentally read. I did not call `list_agents`, spawn an agent, create a goal, start another model session, alter the original goal/cap envelope, or run any experiment other than the reserved BT10-FV1 job.

The assignment's original and resumed administrative deadlines remained in force. This report makes no claim that role separation removes same-model correlation, nor that a successful finite test proves a universal theorem.
