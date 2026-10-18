# RH1 independent full-proof review

Reviewer role: NONAUTHOR for H-ALIGN and its companions. This reviewer did not originate the alignment estimate. The separate RF4 same-J author packet and prior RF4 reviews remain frozen. Only the assigned H packet, permitted mathematical sources, and administrative live cap were read; no other referee or blind report was consulted.

## Scoped recommendation

| Frozen object | Recommendation |
|---|---|
| H-ALIGN theorem-only-v1 / proof-v1 | SUPPORTED as the stated all-width, original-law, one-step necessary-event bound |
| parameters-v2, (W1)–(W3) and \(s_J\ge512n^2\) | SUPPORTED |
| parameters-v2 assertion that polynomial-time scalar parameters ensure polynomial absolute width | NOT SUPPORTED without a numerical upper-width premise or specified bounded-value schedule |
| shifted-cosets-v2, (C1)–(C6), selected-pair consequence | SUPPORTED |
| short-relation-v2, deterministic algorithm, original-law rank/tail bounds, exact index and norm formulas | SUPPORTED |
| short-relation-v2 scope-repaired polynomial-in-\(n\) certificate limitation | SUPPORTED, conditional on its explicit width assumptions and limited to the numerical worst-case upper certificate |

These are recommendations for reconciliation, not acceptance actions. The narrow parameter objection is preserved before repair in parameter-scope-counterexample-v1.md. It does not invalidate the main theorem or the separately assumed polynomial-width relation statement.

Exact main hashes:

- theorem-only-v1.md: e2265238d7240a1fae85fa952c7996e0ad7ec20bc8697870da18fca9b4c6be18
- proof-v1.md: 0f2eb5103e3fb274a9ae87213555e7e530dc0b628b7d57a04804b28a7698a96a

The assignment-pinned companion and packet hashes all match; intake-hashes-v1.json records them.

## 1. Full original law and coefficient normalization

The experiment samples one original \(X\) from the normalized infinite coefficient Gaussian on \(F\), including zero. Since \(FI\subset F\), its nonzero alignment mass is exactly
\[
 [\rho_s(FI)-1]/\rho_s(F).
\]
The numerator subtraction is correct and the denominator remains the original one. No shifted-coset equality, conditioning on nonzero, or replacement by a spherical Gaussian on another ideal is used.

The power-basis Fourier identity gives \(\sum_\sigma|\sigma(x)|^2=n\|x\|_{\rm coef}^2\). AM–GM therefore gives \(|N(x)|^{1/n}\le\|x\|_{\rm coef}\), with no extra \(\sqrt n\) on the right. For nonzero \(x\in L\), \((x)L^{-1}\) is an integral ideal, so \(|N(x)|\ge N(L)\). For \(y\in L^*=\overline L^{-1}\), \((y)\overline L\) is integral, so \(|N(y)|\ge1/N(L)\). Thus the primal/dual minimum bounds are exactly \(N(L)^{1/n}\) and its reciprocal in coefficient norm.

The direct duality argument is valid: the constant coefficient of \(x\overline y\) is the coefficient inner product. Testing every negacyclic rotation of \(x\in L\) tests all coefficients of that product. This proves the full inverse-conjugate identity, rather than merely one trace condition. It agrees with the trace/codifferent derivation and avoids importing the canonical trace-dual factor \(n\).

## 2. Packing, shells, and all widths

The balls of radius \(\lambda/2\) about distinct lattice points have disjoint interiors. Balls about points of norm at most \(t\) lie in the radius-\(t+\lambda/2\) ball. The count \((1+2t/\lambda)^n\) follows by volume comparison; boundaries do not change the volume argument.

The layer-cake expression includes the zero point for every positive integration radius. Applying \((1+x)^n\le2^{n-1}(1+x^n)\), then the exact Gaussian integral, gives
\[
 \rho_s(L)\le2^{n-1}\bigl[1+(2s/(\sqrt\pi\lambda))^n\Gamma(n/2+1)\bigr].
\]
Since \(n\) is even, \(\Gamma(n/2+1)=(n/2)!\le(n/2)^{n/2}\). The stated loose bound \([4\sqrt n\max(1,s/\lambda)]^n\) follows. It is an upper bound on the full theta series, not a finite truncation.

With \(r=N(L)^{1/n}\), \(s\ge4\sqrt n\,r\) and \(\lambda_1(L^*)\ge1/r\), shell \(k\) contributes at most \((2k+3)^n e^{-16\pi nk^2}\). The inequalities \(2k+3\le5^k\), \(k^2\ge k\) give a geometric sum \(a/(1-a)<1\), \(a=(5e^{-16\pi})^n\). This proves the explicit smoothing threshold for every stated \(n\), not only asymptotically.

Centered Poisson has positive dual terms, hence \(\rho_s(F)\ge s^n/D_F\) at every width. For \(L=FI\), the upper-width regime gives \(\rho_s(L)<2s^n/(D_FM)\), and thus event mass at most \(2/M\). In the lower-width regime, \(\lambda_1(L)\ge r\) and \(s<4\sqrt n\,r\) give \(\rho_s(L)\le(16n)^n\). Dividing by the same lower denominator and using \(D_F<2^n\) gives \((32n/s)^n\). The sum of those regime bounds and the cap at one establish (T1). Replacing \(\rho_s(L)-1\) by \(\rho_s(L)\) only enlarges an upper bound. In particular the zero-dominated regime is harmless, though the estimate can be vacuous there.

The probability proof needs no primality of \(I\), consistent with the separate general-integral-ideal statement.

## 3. Honest least clearing and descent necessity

For original nonzero \(X\in F\), \(C=(X)F^{-1}\) is integral. If \(B=\gcd(I,C)\), the denominator ideal of \(IC^{-1}\) has valuations \(\max(v_{\mathfrak p}(C)-v_{\mathfrak p}(I),0)\), hence is \(CB^{-1}\). Since the clearing integer satisfies \(dR\subset CB^{-1}\), taking norms gives \(d^n\ge N(C)/N(B)\), so \(N(dIC^{-1})\ge M/N(B)\).

For prime \(I\), \(B\) is \(R\) or \(I\). Strict descent requires the latter, equivalently \(X\in FI\). This is only necessary. A congruence relation can still fail to descend after honest integer clearing, and any second zero output or eligibility test can further reduce original success. The proof uses no favorable conditional renormalization.

No ideal factorization algorithm is required to execute this algebra: the valuation argument proves the identity, while ordinary basis inversion/intersection/HNF and rational denominator clearing compute the operations. Approximate off-lattice samples must be rejected by membership checks or charged through their TV error; no algebraic integrality claim applies to an arbitrary off-lattice vector.

## 4. Complete histories, selected attempts, and zero conditioning

At each active history the ideal and width are fixed before the fresh draw. The supplied conditional kernel contract then gives the original event bound almost surely, and TV changes its mass by at most the predictable \(\epsilon_j\). Multiplying by the predictable activity indicator proves (T2).

Every later-selected alignment is pointwise one of the original active alignments. Its indicator is at most the sum of all active alignment indicators. Taking expectations and the tower rule gives (T3), even for stopped, randomized, or hindsight selection. No independence of selected events is claimed. Uniform bounds yield (T4) by monotonicity and the stated almost-sure error-budget bound.

The optional full-transcript coupling assumes its kernel contract on relevant complete histories and deterministic per-stage tolerances. Coupling while histories agree and summing first-disagreement probabilities is valid; discarded failure labels or hidden-state marginal promises would not replace that contract.

Zero rejection has probability \(1-1/\rho_s(F)\), giving the stated denominator \(\rho_s(F)-1\) and expected geometric retry count. Since \(s>0\) and \(F\) contains nonzero vectors, that denominator is positive. The theorem does not claim a deterministic cap on this geometric procedure or preserve the original event bound after conditioning.

The asymptotic negligibility statement correctly restricts to fixed \(\rho>0\), \(s\ge512n^2\), polynomially many attempts and negligible total conditional error. At \(\rho=0\) its exponential-index conclusion is not asserted.

## 5. Shifted cosets and complete comparator

Because \(N(I)>N(F)\) and \(I\) is prime, \(I\nmid F\), so \(F+I=R\), \(F\cap I=FI\), and \(F/FI\simeq R/I\). The shifted theta formula (C1) is exact and each infinite coset mass is positive.

The packing count applies to a translate using the same separation, even without a zero point. At large width, shifted Poisson and the triangle inequality bound each shifted theta by the centered theta. At small width the same layer-cake estimate applies. Thus (C2) bounds every atom; it does not say the residue law is uniform.

The source joint law retains \(A=X\bmod I\). The analytic comparator first chooses a uniform residue and then uses the normalized Gaussian conditional lift for that residue. Conditional lifts coincide in the two experiments; their supports are disjoint across residue labels. This proves both the likelihood ratio and the exact TV equality (C5). Independently adjoining a uniform residue to the original vector would violate the constraint and is correctly excluded.

For the optional smoothing comparison, shifted Poisson supplies errors \(|e_a|\le\epsilon_K\). Summing over cosets gives \(\bar e\ge0\) from centered Poisson on \(F\). Then
\[
 \frac1{2M}\sum_a\frac{|e_a-\bar e|}{1+\bar e}
 \le\epsilon_K.
\]
Product coupling gives the \(m\epsilon_K\) bound. The box-concentration example correctly shows why max-atom bounds alone do not imply small TV. Pair collision is \(\sum_a\pi(a)^2\le\max_a\pi(a)\); excluding exact equal vectors only lowers its nonzero-image event. The union over all pairs pays for later selection.

## 6. Relation algorithm, rank probability, and tails

The relation lattice is the full preimage of zero under an additive map \(\mathbb Z^m\to R/I\). Its index is exactly the additive image size \(h_A=p^r\), not automatically \(M\). HNF/SNF yields a full-rank integral lattice because \(p\mathbb Z^m\) is contained in it. Full rational rank of the sample matrix implies that every nonzero coefficient vector has nonzero image; this is why the original FAIL branch is necessary.

The rank-probability proof is valid. Minkowski's closed-cube argument supplies a nonzero \(f\in F\) with coefficient norm at most \(\sqrt n D_F^{1/n}\). Its \(n\) rotations are independent because multiplication by nonzero \(f\) is invertible in the field. Some such rotation \(v\) lies outside every given proper subspace. For \(x\in F\cap H\), the lines \(x+\mathbb Zv\) are disjoint: otherwise a nonzero multiple of \(v\) would lie in \(H\).

Completing the square and scalar Poisson yield \(\rho_{s/\|v\|}(\mathbb Z+\alpha)\ge s/(2\|v\|)\) when \(s/\|v\|\ge1\), uniformly in the actual center. The bound \(2e^{-\pi}/(1-e^{-3\pi})<1/2\) justifies that scalar constant. Summing the lines gives \(\Pr[X\in H]\le2\|v\|/s<4\sqrt n/s\). Conditional on all past samples, their span is fixed and proper for every \(j\le m\le n\), even if an earlier rank failure occurred. A union bound proves (R6).

For completeness, centered-theta maximality gives
\[
 \mathbb E e^{tX_i}\le e^{t^2s^2/(4\pi)}.
\]
Chernoff with \(t=2\pi L/s\) gives \(\Pr[|X_i|>sL]\le2e^{-\pi L^2}\). The coordinate/sample union proves (R7). These are original-law bounds; no distribution is conditioned on passing rank screening.

The deterministic relation bound and Cauchy–Schwarz give (R8)–(R9). Since \(Y\in I\), the algebraic minimum \(M^{1/n}\le\lambda_1(I)\) makes \(G_A\) a valid upper approximation certificate. In (R10), \(b(Y)=\|M_Y\|_{\rm op}/|N(Y)|^{1/n}\) is the definition in A's permitted replacement source. The facts \(|N(Y)|\ge D_FM\) and \(\|M_Y\|_{\rm op}\le\sqrt n\|Y\|\) give the claimed distortion.

For \(m>n\), exact coefficient dependencies are unavoidable and lie inside the modular relation lattice. Short coefficient vectors need not have nonzero image. The stated image lattice identity and determinant upper bound are correct, and ordinary \(n\)-dimensional LLL gives (R13). The scalar relation \(pe_j\) and the principal-ideal baseline are also correctly separated from a new oracle-assisted guarantee.

## 7. Quantified certificate scope

Writing \(z=\log M\), the coefficient of \(z\) in \(\log g_m\) is nonnegative for \(m\le n\). Substituting \(z\ge\rho n\log2\) and AM–GM gives exactly (R12), with exponent \((\log2)\sqrt{\rho n}-(\log2)/4-\rho\log2\). Thus the numerical worst-case certificate cannot be polynomial in \(n\) for fixed \(\rho>0\).

This is a lower bound on an available **upper certificate**, not an output lower bound or an impossibility result. V2 states that distinction. It also correctly retains the counterexample \(m=n,\log_2M\ge2^n\), where \(g_n\le(\log_2M)^{1/4}\). A superpolynomial-in-full-encoded-size conclusion therefore needs the explicit \(\log M\le n^C\) restriction. The original v1 overreach remains preserved.

The relation companion separately assumes polynomial absolute \(s\). That premise is not derived merely by polynomial-time scalar evaluation; see the preserved parameter objection. Under its explicit premise, the rest of the v2 conditional analysis is sound.

## 8. Finite falsification and limits

Both author control codes, inputs, original JSON outputs, commands and resource reports were inspected. Their 143,144-pair finite laws are distinct normalized truncations and do not certify infinite Gaussian estimates. The first reproduces CP-1 and finite packing; the second retains the full output law with rank FAIL, exact source/comparator lifts and actual relation indices.

Independent reserved RH1-FV1 deliberately tests residue degree two, \(I=(3)\subset\mathbb Z[i]\), instead of repeating those degree-one controls. It passed 4,802 exact point pairs, all conditional-lift/full-output TV checks, index values \(1,3,9\), and nonzero rank-passing images. Exit 0, wall 0.10 s, OS peak 12,288 KiB, empty stderr, within the granted 10 s/64 MiB reservation. The reservation was released. This easy principal ideal is a discriminating bookkeeping control, not hardness evidence. No numerical falsification of the stated current main theorem or companion probability claims was found.
