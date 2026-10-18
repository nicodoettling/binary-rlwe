# BT5 blind referee report — frozen B v2 and C v5

Status: COMPLETE referee report, with a specifically identified source-level finite-OHCP verification limitation. Findings are SEALED until the coordinator unseals them. This is correlated same-model scrutiny, not formal verification.

## 1. Inputs, isolation, and disposition

The full exact assignment is preserved in `assignment.txt`. The only local mathematical inputs read were:

- `workers/B/ideal-denominator/gaussian-periodic-theorem-v2.md`, SHA256 `be7f05d67fc8f2b24fc6b93321c95005f4d7f6e24bab513b2cbaf35c82aeaad7`.
- `workers/C/periodic-hardness/multiplier-ohcp-theorem-v5.md`, SHA256 `2e7f13cc08d5173a9b028b9d757e7c038220cdbbfe83380c6e57320ddc52a38b`.

Both hashes matched. No author proofs, linked histories, prior reports, project ledgers, status files, or other workers' mathematical material were read. No worker was contacted and no subagent was spawned. No mathematical computation or experiment was run; the finite checks below were done by hand. Shell/Python operations only preserved or inspected authorized artifacts and computed hashes.

The permitted [BRST PDF](https://arxiv.org/pdf/2005.09595) was accessible. Definition 3.7 and Lemma 3.8 supply the local OHCP interface and its polynomial-time search theorem. Direct access to the permitted [PRS PDF](https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf) failed twice; subsequent direct finds for Definition 4.3 and Lemma 6.9 also failed. No alternate source or search was used. The procedural audit skill was read, but importing project regressions would violate the blind assignment and was not done.

**B v2:** I reconstructed the statistical claims, exact comparator including fallback, and expected polynomial implementation. I found no counterexample. The full rational encoding-length qualification is material and adequate. There is a minor implementation literalization point about ceilings of transcendental expressions, described below; it does not threaten the estimates or exact comparator.

**C v5:** I reconstructed the Gaussian completion, shifted center, starting excursion, local-domain construction, one-plane full-Haar limit with quantitative decay, Lipschitz estimate, recovery, and global adaptive oracle-error accounting. These close under the statement's declared finite primary-OHCP contract `T_H`. I found no mathematical counterexample. I cannot independently certify the stronger assertion that the primary theorem itself supplies all the finite query-description/internal bit-operation bounds included in that contract: BRST's available restatement asserts polynomial time and bounded logscale indices, but does not spell out that implementation; PRS was inaccessible. This is a precisely delimited verification limitation, not evidence that the finite implementation is impossible.

**Composition:** The statistical interfaces and canonical/coefficient scaling match when their parameters are chosen compatibly. A directly composed B algorithm has expected runtime. A strictly bounded-time composition needs to cap B's exact uniform rejection and charge an additional small error; exact comparator equality then becomes approximate. This is compatible with a reduction with positive residual advantage, but must be said explicitly.

**Scope:** No standard hardness assertion, restricted-ideal-family hardness assertion, or missing binary/fractional completion dependency is certified here. No such premise was needed for the two conditional reductions.

## 2. B: lattice, quotient, and representation facts

Write `Lambda=J^{-1}` in coefficient coordinates. Since the cyclotomic ring is the full integer ring and `J` is integral,

\[
\mathbb Z^n\subseteq\Lambda\subseteq D^{-1}\mathbb Z^n,
\qquad \det(\Lambda)=D^{-1},
\qquad |\Lambda/\mathbb Z^n|=D.
\]

Consequently `q Lambda` is contained in `h Z^n` for `h=1/(DP)`, and

\[
|h\mathbb Z^n/q\Lambda|
=\frac{q^n/D}{h^n}=q^nD^{n-1}P^n.
\]

Inverse bases, quotient presentations, HNF/SNF calculations, and the determinant use polynomially many bits in the ordinary input basis. There is no enumeration of `D` cosets. When `gcd(D,q)=1`, multiplication by `D^{-1} mod q` on the numerator identifies `Lambda/q Lambda` with `R/qR`. Its kernel is exactly `q Lambda`: if `Da` vanishes modulo `qR`, then `a` lies in `(q/D)R`, and invertibility of multiplication by `q` on `Lambda/R` gives the required membership. Equivalently, localizing at the primes dividing `q` makes `J` the unit ideal. No primality of `q` is needed.

Nearest-grid rounding descends to the torus because it commutes with the grid lattice. Pushing Haar measure through rounding gives exactly uniform measure on the finite quotient: its grid cells have equal measure and tile the torus up to null boundaries.

## 3. B: exact comparator survives every finite-sampler branch

Let `K(y,.)` be the output law before reduction modulo `q Lambda`, with uniform `u` in `Lambda/Z^n`. Take any `ell in Lambda`. Reindex the coset choice by

\[
u'=\operatorname{rep}(u+\ell),\qquad b=u+\ell-u'\in\mathbb Z^n.
\]

The new scalar centers are `y+ell-u'=y-u+b`. The stipulated scalar sampler translates its output exactly by `b`, because its fractional center, trial interval, deterministic exponential approximation, Bernoulli rule, and fallback are unchanged. Thus its resulting lattice output translates exactly by `ell`.

This proves covariance under every translation in `Lambda`, not just under integer translations. Taking `ell in q Lambda` proves independence of the input representative. Uniform input on the finite group is invariant under `Lambda` translations, while `Lambda/q Lambda` acts transitively on the output group. Therefore the output is exactly uniform. No closeness-to-Gaussian argument is needed for this endpoint.

A hand finite check stresses the fallback: take `n=1`, `J=3Z`, `q=2`, `P=1`, and replace the scalar sampler entirely by its equivariant fallback `floor(c)`. For the two inputs `0,1/3` and three equally likely cosets `-1/3,0,1/3`, the six outputs modulo `(2/3)Z` consist of three copies of each class. This checks that fallback bias does not by itself break the group argument. It is not a simulation or a proof substitute.

Exact uniform sampling of arbitrary finite invariant factors uses expected-time rejection. A fixed worst-case number of fair random bits cannot in general produce a uniform distribution on a group of odd order. B explicitly claims expected polynomial time, so this is consistent rather than a defect.

## 4. B: both planted normalizers and the rounding loss

Poisson summation and the stated lower bound on `r` give, uniformly in the shift `c`,

\[
(1-\epsilon)r^n\leq\rho_r(\mathbb Z^n-c)
\leq(1+\epsilon)r^n.
\]

For example, putting `tau=exp(-pi r^2)<=epsilon/(8n)`, the one-dimensional dual theta tail is bounded by `2 tau/(1-tau^3)`, and its `n`-fold product is comfortably below the supplied error bound. Since `Lambda^*` is a sublattice of `Z^n`, the same argument gives

\[
(1-\epsilon)Ds^n\leq\rho_s(\Lambda)
\leq(1+\epsilon)Ds^n,
\qquad s^2=w^2+r^2.
\]

Before rounding and finite scalar approximation, the probability of `a in Lambda` is

\[
\frac1D\int_{\mathbb R^n}
\frac{\rho_w(y)}{w^n}
\frac{\rho_r(a-y)}{\rho_r(\mathbb Z^n+u(a)-y)}\,dy.
\]

Replacing only the denominator by its bounds and integrating the Gaussian product gives an unnormalized mass proportional to `rho_s(a)/(D s^n)`. Dividing by the *actual* `rho_s(Lambda)` gives pointwise ratios between `(1-epsilon)/(1+epsilon)` and `(1+epsilon)/(1-epsilon)`. In particular, the theorem's `2 epsilon/(1-epsilon)` single-sample allowance is conservative. This calculation is for the actual lattice Gaussian; it does not replace the output with a uniform-coset mixture.

For the rounding term, the scalar discrete Gaussian mass function satisfies

\[
\frac{d}{dc}\log p_c(m)=\frac{2\pi}{r^2}(m-\mathbb E_c M).
\]

A uniform bound `E_c |M-c| <= 2r` for `r>=1` follows by bounding the shifted Riemann sum of `|x| exp(-pi x^2/r^2)` by its integral plus its total variation, and dividing by the lower theta bound. Hence the scalar total-variation derivative is at most `4 pi/r`. A center displacement at most `h/2` costs at most `2 pi h/r`. Tensorization over coordinates, `D>=1`, and then samples gives the claimed `2 pi kn/(Pr)` allowance. Scalar approximation contributes at most `kn nu`.

These are conditional-on-`J` estimates. Mixing over any common ideal/metadata law preserves them, even though samples are correlated after marginalizing the ideal. Discarding `J` also preserves the bound by data processing. This establishes the full-joint interpretation and the stated advantage loss.

## 5. B: explicit scalar sampler and bit complexity

For `nu<=1/4`, its `K` is at least 8. With `N=ceil(rK)+1`, the proposal size satisfies

\[
2N+1\leq 3rK.
\]

The omitted Gaussian tail is much smaller than `nu`, since every omitted point is at distance greater than approximately `rK` and the tail is bounded by a constant times `exp(-pi K^2)`. The full scalar Gaussian mass is at least `3r/4`. The sum of dyadic weight errors is at most

\[
(2N+1)2^{-p}\leq
\frac{3rK\,\nu}{1024(K+1)}.
\]

Thus the accepted truncated law differs from the true law by much less than `nu/4`, and the acceptance probability is at least `1/(5K)`. The chance of exhausting the `L` trials is at most

\[
\exp(-L/(5K))\leq(\nu/16)^8.
\]

The total is below `nu` with substantial slack. Clipping dyadic approximations to `[0,1]` is harmless and part of the specification.

The interval may have numerically huge length, but sampling a uniform integer from it costs only its bit length in expected time. `K,p,L` are polynomial in `log(1/nu)`; `N` has bit length polynomial in `log r` and the input. The normalized exponential argument has magnitude `O(K^2)`, and rational centers are reduced to an exact integer part and fractional part. Counting both numerator and denominator lengths therefore fixes the important bit-model issue. Widths or centers of bounded numerical magnitude can still carry long input encodings, and those lengths are now charged.

Implementation literalization: an implementation should explicitly use conservatively rounded integer control parameters for the natural-log ceiling in `L`, or justify its exact ceiling computation. For instance, replacing it by the easy integer upper bound `40K ceil(log_2(16/nu))` preserves all conclusions and equivariance. This changes the literal finite kernel slightly, so should be identified if used. I have not found a lower-bound obstruction to the original exact ceiling; this is a small implementation specification qualification, not a statistical counterexample, and is not a claim that exact ceiling evaluation is intractable.

Conditional challenge generation also has a polynomial implementation: truncate scalar Gaussian tails to the requested error, sample the resulting rounded grid law by certified CDF inversion with sufficiently many random bits, and reduce using the quotient presentation. The support can be exponentially large in input length, but its *index bit length* and the CDF precision needed to charge all cell errors are polynomial. Exact uniform quotient sampling remains expected polynomial. Sampling `J` itself additionally requires efficient `Gen`, as the statement now says.

## 6. C: the physical query and Gaussian completion

Let `h=e-g(z)`, and let `V` have canonical widths `v_j=v0 exp(t)` on the selected conjugate pair and `v_i=v0` elsewhere. Since `r` is integral and `L=qJ^{-1}` is an `R`-module,

\[
r\lambda\in L,
\qquad Q_h(r(T-g(z))+G_w)\bmod L
=Q_h(r(e-g(z))+G_w)\bmod L.
\]

Here the occurrence of `h` as the grid-spacing subscript is distinct from the error vector just defined. Cancellation holds before any approximation of the Gaussian law and survives rounding because `L` lies in the grid lattice.

For an exact lattice multiplier `r~D_{R,V}`, define canonical widths

\[
S_i^2=w^2+v_i^2|h_i|^2,
\qquad U_i^{-2}=v_i^{-2}+|h_i|^2/w^2.
\]

Completing the square gives the density identity

\[
f(x)=\frac{\rho_S(x)}{w^n\rho_V(R)}\,
\rho_U(R-\mu(x)).
\]

Both lattice normalizers are essential. Since `det U/det V=w^n/det S`, uniform smoothing of the numerator and denominator makes this density close to `rho_S(x)/det S`, with ratio in the usual `(1±epsilon0)/(1∓epsilon0)` range.

On the proposed local region `|h_j|<=8d0`, and with `|e_i|<=d0` elsewhere,

\[
\min_i U_i\geq
\frac{v0}{\sqrt{1+(8v0d0/w)^2}}
\geq\frac{v0}{\sqrt2}\geq\sqrt{2n}\,a.
\]

This holds for every `t>=0`; increasing the selected multiplier width does not destroy posterior smoothing. The canonical lattice `R` is a rotated, scaled copy of `Z^n` with scale `sqrt(n)`. Its theta bounds therefore follow from the scalar bounds at width `a`, with room in the given constants. The physical one-sample law and the continuous elliptical comparison law are within `2 epsilon0/(1-epsilon0)`, before or after grid rounding and reduction modulo `L`.

This distinction matters: the full-Haar limit needed below is a property of the continuous comparison oracle. An exact discrete multiplier need not have an exact Haar limit for every special algebraic error. The bounded comparison error, rather than an unproved exact limit for the physical multiplier, is what makes the reduction work.

## 7. C: shifted center, local oracle, and OHCP conditions

For the selected complex coordinate,

\[
h_j=d0(z^*-z),\qquad z^*=2+e_j/d0,
\qquad 1\leq |z^*|\leq3.
\]

The comparison law's selected width is

\[
\sqrt{w^2+h0^2\exp(2t)|z-z^*|^2},
\qquad h0=v0d0,
\]

while all nuisance widths are fixed. Its acceptance probability therefore depends on the required radial variable. The shift handles exactly zero and arbitrarily tiny error coordinates; no lower-bound assumption on their size is needed.

The relevant primary OHCP contract uses a center whose norm is between an exponentially small multiple of the scale and the scale, radial dependence on a neighborhood of the center, a positive starting excursion, exponential decay along the origin ray, and Lipschitz dependence on logscale on an origin-centered neighborhood. It returns exponentially accurate recovery with exponentially small failure in polynomial time. BRST Lemma 3.8 states these conditions and bounds the logscale indices of its calls. The following checks are independent derivations for this instance.

**Local extension.** Define a mathematical reference oracle equal to the continuous elliptical law when `|z-z*|<=8`, and equal to the exact physical oracle outside that set. The reference need not be implementable; it is used for a coupling. The center-local OHCP radial domain at scale 3 is contained in this set. So is the origin-centered Lipschitz domain, because

\[
|z|\leq3(1+1/\kappa),\ |z^*|\leq3
\quad\Longrightarrow\quad |z-z^*|<8.
\]

Outside the patch the two oracle laws agree exactly; inside, the smoothing estimate applies. Thus a uniform comparison bound holds for *all* query positions. No confinement of unknown adaptive queries is being assumed. Reading the primary's radial condition as global would invalidate this patch, so the local domain in Definition 3.7 is a real dependency.

**Starting excursion.** At `z=0,t=0`, every additional canonical width is at most `3h0`. Viewing the comparison Gaussian as `G_w` plus an independent small Gaussian and using the translated-Gaussian variation bound yields, for `k` samples, a difference at most

\[
3k\sqrt n\,h0/w=3\delta/(32\sqrt n)<\delta/8.
\]

Hence one of the two global orientations has excursion at least `7 delta/8`, exceeding `1/kappa` since `kappa>=2/delta`. One may take the starting logscale to be zero. The nuisance widths do not consume the distinguishing gap.

**Lipschitz property.** Only one two-real-dimensional Gaussian plane changes with `t`. Its log-width derivative lies in `[0,1]`. Integrating the absolute Gaussian score gives a total-variation derivative bounded by 2, uniformly in the center and width. Applying rounding, reduction, and `A` cannot increase this. For `k` samples the bound is `2k<=kappa`, including on the required origin-centered domain.

## 8. C: one growing plane really reaches full Haar

For this power-of-two cyclotomic field, the canonical Euclidean dual is

\[
L^*=\frac1{nq}\,\overline J.
\]

A nonzero dual character is represented by a nonzero field element. Every embedding is nonzero, and its product satisfies

\[
\prod_{i=1}^n |y_i|\geq D/(nq)^n.
\]

The divisibility by `D` follows because a nonzero principal ideal contained in `J` has norm at least `D`. At `z=0`, the selected pair has width at least `h0 exp(t)` and the remaining widths are at least `w`. The arithmetic-geometric mean inequality therefore gives, for every nonzero dual vector,

\[
\|S_t y\|_2\geq\sqrt n\,a0\exp(2t/n).
\]

This proves considerably more than just nonvanishing of the selected embedding. Let `lambda_t` denote the right side. A packing argument bounds the dual theta tail by

\[
\sum_{m\geq1}(2m+3)^n\exp(-\pi m^2\lambda_t^2).
\]

For `lambda_t^2>=n>=2`, this is at most `exp(-lambda_t^2)`: use `log(2m+3)<=m^2 log 5`, then sum a rapidly decreasing series.

When `t>=kappa/2`, the specified bound on `kappa` gives `t>=2S+2n+2log(k+1)+10`, and hence

\[
\lambda_t^2\geq n\exp(2t/n)\geq2t+n.
\]

The rounded `k`-sample law is then within `k exp(-lambda_t^2)/2 <= exp(-t)` of uniform. For `t<kappa/2`, the trivial bound 1 is already at most `2 exp(-t/kappa)`. This proves the advertised OHCP decay with the supplied conservative constants.

Rounding Haar gives exactly uniform measure on the finite group. Thus its limiting acceptance is exactly `A`'s finite-uniform baseline. The conclusion uses the field property; an analogous claim for a product ring could fail because a nonzero character could have zero selected component.

## 9. C: recovery, verification, and both orientations

Apply the primary search separately to each of the `n/2` pairs in each of the two orientations. The correct orientation has all the conditions above. With scale 3, the recovered coordinate error is at most `3d0 exp(-kappa)` using the looser confidence level; the stated extra `log 4` leaves additional slack.

The inverse Fourier embedding has coefficients of modulus `1/n`. Consequently the same maximum embedding error bounds every coefficient error. Since

\[
L\subseteq(q/D)\mathbb Z^n,
\qquad 3d0e^{-\kappa}<3we^{-\kappa}<q/(8D),
\]

one recovers the exact lattice candidate by rounding coefficient coordinates to multiples of `q/D`, reserving additional error room for certified embedding evaluation. This does not use a short basis or a closest-vector oracle.

Membership in `L` is an exact rational basis computation. Distance verification should use a separated threshold, for example `2d0`, rather than try to decide equality with `d0`. Every nonzero vector of `L` has canonical infinity norm at least `q/D^{1/n}`. Therefore, under the stated strict bound on `d0`, the correct candidate is within `d0`, while every distinct lattice candidate is farther than `3d0`. Certified evaluation to error below `d0/4` suffices to separate them. This also avoids an undecidable equality test for a general certified scalar representation.

An incorrect orientation can fail to satisfy the OHCP promise. A time/query/logscale/description cap must therefore apply to *every* invocation, not merely to correct-orientation runs. The frozen statement explicitly adds these caps. With `n` total invocations and the given per-run call bound, the total is at most `Q_*`. A correctly verified candidate is unique, regardless of which orientation produced it.

## 10. C: finite sampling and adaptive errors

A finite sampler for the multiplier does not require a short basis of `J`. Use the ordinary public coefficient basis of `R`, viewed in the inverse elliptical metric. Its Gram-Schmidt lengths are at most `sqrt(n)/v0`, so its scalar Gaussian widths are at least `v0/sqrt(n)>=2a`.

Sequential scalar Gaussian sampling in this basis produces a mass proportional to the desired elliptical Gaussian divided by a product of scalar coset normalizers. Those normalizers have uniformly small theta variation. Correct them by rejection, using their product divided by a known uniform upper bound as the acceptance probability. The acceptance probability is bounded away from zero uniformly in all intermediate centers. The scalar theta series can be evaluated to any requested accuracy via their rapidly convergent dual series. Truncate all rejection loops, approximate Bernoulli probabilities, and allocate the failure/error within the sample's numerical budget. This yields an arbitrarily accurate bounded-time lattice Gaussian sampler using public data only; it is not necessary to leave a fixed additional multiplier-sampling bias uncharged.

For a generated sample, compute `rT` exactly in coefficient coordinates and approximate `rg(z)` to absolute error small compared with the coefficient Gaussian width times the numerical budget. The required precision increases by `O(t)` and the bit lengths of the bounded query and multiplier. A truncated Gaussian tail bounds multiplier bit lengths. Since logscale and query descriptions are capped, even the wrong orientation has polynomially bounded required precision. Coordinate CDF inversion then samples the *rounded* Gaussian law directly; it need not represent an infinite-precision real sample first. The number of possible grid cells can be huge, but its logarithm is bounded by the input and precision parameters. CDF and uniform-bit precision can include that logarithm.

The error allocation must cover the whole generated sample, splitting its budget among scalar samplers, rejection cutoffs, mean/width approximation, and CDF inversion. Under this interpretation, the given global counter is sufficient. Conditional on every adaptive transcript, each next call has the same uniform local/extended comparison estimate, and its finite implementation has its assigned numerical error. Coupling successive conditional kernels therefore bounds full transcript variation by the sum of those errors. No independence after transcript conditioning is assumed.

In particular,

\[
2kQ_*\epsilon0/(1-\epsilon0)<\zeta/16,
\qquad
\sum_{j\geq0}\frac{\zeta}{16(j+1)^2}<\zeta/8.
\]

There is substantial remaining room within `zeta` for the other explicitly bounded finite operations. A union bound over correct-orientation coordinate searches gives the stated `(n/2) exp(-kappa)` term, again conservatively. The wrong orientation is controlled by caps, not by an inapplicable success theorem.

**Unclosed source-level verification:** These arguments construct finite query simulation *given* a primary algorithm with the finite query/time contract called `T_H`. They do not independently reconstruct that primary algorithm's own random choices, internal comparisons, and representation bounds. The accessible BRST restatement supplies polynomial time and a polynomial logscale-index bound but not those implementation details. Because the PRS source failed to load and source widening was forbidden, I cannot honestly certify that strengthened import from its implementation. If `T_H` is taken as an explicit finite-algorithm hypothesis, the conditional proof above closes; if the packet is intended to prove that hypothesis from the primary paper, this review leaves that exact dependency unverified. Under the usual Turing interpretation of polynomial time, polynomial query-length bounds are implicit; I am not claiming that the primary theorem lacks such an interpretation. The unresolved point is verification of that interpretation for its real-domain oracle implementation from the restricted accessible sources. The absence of an independently stated numerical polynomial exponent is not itself a flaw. A uniform bound on the runtime of A on every valid finite input tuple is also the natural meaning of the A-runtime term; a source-distribution-only average runtime bound would not control all simulated queries without an additional cap.

## 11. Finite composition, scaling, and classical/quantum scope

For a fractional-Gaussian distinguisher with pointwise advantage `delta_F`, B gives a distinguisher for C's finite input with advantage at least

\[
\delta_C=\delta_F-\Delta>0,
\qquad w_C=\sqrt n\,w_B,
\qquad s^2=w_B^2+r_B^2.
\]

The grid and public ideal are exactly the same. To target a preselected fractional width `s`, one must have `s>r_B` and choose compatible positive `w_B`; that feasibility condition cannot be skipped. B's supplied widths are rational, whereas C also permits algebraic/certified widths. Choosing rational `w_B` and taking `w_C=sqrt(n) w_B` is therefore a clean exact composition. An arbitrary independently prescribed C width need not give rational `w_B`; any approximation in the reverse direction needs its own charge.

B's exact uniform rejection is expected-time. To obtain a bounded-time distinguisher for a fully bounded C implementation, cap the elementary uniform-rejection loops in B and assign total failure at most `eta` for each complete call. This produces a finite map within `eta` on *every input*. It may lose exact comparator equality, and its guaranteed advantage is at least `delta_F-Delta-2eta`. Choosing this residual advantage positive and using it as C's declared `delta` resolves the issue. Repeated adaptive calls can use fixed finite caps defining one distinguisher, or charge any additional implementation error through a properly specified transcript budget. Merely describing the direct composition as bounded time without this step would be inaccurate.

All guarantees are pointwise implications for the supplied `J`. An average signed advantage over `Gen` gives a good-ideal statement, not success on every ideal. For example, average advantage `delta` yields a positive fraction of ideals with signed advantage at least `delta/2`; the elementary bound is at least `delta/(2-delta)`. The global orientation may be reversed if the average sign is negative. This extraction does not expand the ideal family.

The periodic-decision-to-BDD reduction uses only classical arithmetic, sampling, oracle calls, and lattice membership. The optional BDD-to-DGS step is quantum. Formally, the Euclidean BDD radius `d0` on `L` is available because Euclidean norm at most `d0` implies infinity norm at most `d0`. A dual DGS width `sqrt(n)/(sqrt(2)d0)` on `L^*`, followed by multiplication by `nq` and conjugation, gives the stated canonical width

\[
\frac{nq\sqrt n}{\sqrt2\,d0}
\]

on `J`. This is an algebraic normalization check; the requested PRS Lemma 6.9 import itself could not be inspected. Such an import preserves the same family of ideals. It supplies neither the missing arbitrary-ideal worst-case-family edge nor any omitted fractional/binary completion theorem.

## 12. Final referee disposition

There is no discovered counterexample to either frozen statistical theorem. B's group and Gaussian arguments survive its finite sampler and fallback, and its expected-time/encoding scope is substantially supported. C's multiplicative construction, all three OHCP analytic conditions, its local comparison extension, norm-based full-Haar smoothing, and adaptive finite oracle simulation admit the independent reconstruction above.

I do **not** promote the combined packet to an unconditional fully certified finite-bit theorem on the strength of this review alone. The exact remaining dependency is the primary OHCP algorithm's finite internal representation/runtime contract, whose strengthened form is declared in `T_H` but was not independently verified from an accessible implementation. The optional PRS DGS import also remains source-unchecked. These limitations should not be converted into an assertion of falsity. Under the explicitly declared finite `T_H` contract, the reconstructed conditional BDD result is supported.

The two practical qualifications for integration are to preserve B's expected-runtime label or boundedify it with an extra advantage/error charge, and to preserve the pointwise/good-ideal quantifier and coefficient/canonical width conversion. No hardness conclusion outside that scope has been established.

Report completed and frozen on 2026-10-17 before the 21:35Z target. Input and access records are preserved alongside this report.
