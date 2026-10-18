# BT18 independent composition reconstruction, completed v1

Verdict: **conditional pass**. I found no mathematical mismatch in the displayed pointwise binary-recovery to ordinary same-ideal DGS composition, when the four displayed interface contracts are assumed exactly as instructed. This is a reconstruction of the composition, not a proof of those interfaces, an audit of their linked implementations, or a standard worst-case hardness theorem. No source repair is used below.

This completed report also serves as the requested partial checkpoint. Its complete contents and the accompanying exposure log are frozen and hashed before the verdict or any findings are sent to the parent.

## 1. Scope and fixed inputs

The only mathematical inputs were the three frozen files in this directory's `inputs/` subdirectory. Their hashes are:

- Theorem: `96b88a725cc5dc4f8c943275d3b8788fdb9e6ac108c72fe62b383af9614e5e62`.
- Specification: `d5f1a120bf48a90c1f1fa80029dc00ee693b7df031207d15ebff0fcda6c8cb23`.
- Interfaces: `25a78ebcc36d3cd31568f12dd36ee233490509dab8684d4656002a528bb0fab8`.

The assignment hash is `5de3a6f45d93c9c2eb3c7e4239ea12deaab4810f903fbb52023833e80dc010d9`. The separate exposure log records the complete exposure history. In particular, I did not open the longer specifications named by the interfaces. Their existence, exact definitions, and stated guarantees are explicit assumptions for this task.

The proof uses interface I for the fractional-source actual-secret acceptance bound and its basis-existence result; II for the finite bridge, its scalar kernels, exact uniform endpoint, and cap guarantee; III for the finite pointwise BDD algorithm, including all-input termination and total physical-simulation error; and IV for the finite quantum dual sampler and its actual-circuit resource bounds. Every subsequent step is a composition check or elementary algebra stated here.

## 2. Ideal arithmetic, the group, and the retained metadata

Let \(C\) denote coefficient conjugation. It fixes the constant coefficient and sends the coefficient of \(X^i\), for \(1\le i<n\), to its negative in position \(n-i\). Thus \(C=C^{-1}=C^T\) is an integral orthogonal signed permutation.

For every full fractional ideal \(I\), coefficient duality gives

\[
 I^*=\overline{I^{-1}}.
\]

Here is a direct verification that also fixes the normalization. The coefficient inner product of \(z\) and \(x\) is the constant coefficient of \(z\bar x\). If that inner product is integral for every \(x\in I\), apply it also to every \(X^j x\in I\). The resulting constant coefficients extract, up to signs, every coefficient of \(z\bar x\). Consequently \(z\bar I\subset R\), which is exactly \(z\in\overline{I^{-1}}\). The converse follows by taking the constant coefficient. There is no canonical-inner-product factor in this identity.

For an ordinary column basis \(B_J\) of \(J\), one may therefore compute

\[
 J^{-1}=C B_J^{-T}\mathbb Z^n,
 \qquad B=q C B_J^{-T}
\]

as an ordinary rational basis of \(L=qJ^{-1}\). This gives an effective inverse-ideal construction by rational linear algebra, without a short basis or ideal Gaussian sampler. It also gives \(\det(J^{-1})=1/D\).

Since the additive quotient \(R/J\) has order \(D\), \(DR\subset J\). Thus \(R\subset J^{-1}\subset D^{-1}R\), and \(L\) is a sublattice of \((DP)^{-1}\mathbb Z^n\). The finite group in the theorem is consequently well-defined, with

\[
 |F|=\frac{\det(qJ^{-1})}{\det((DP)^{-1}\mathbb Z^n)}
 =\frac{q^n/D}{(DP)^{-n}}=q^nD^{n-1}P^n.
\]

The map \(v/D\mapsto vD^{-1}\pmod q\) on \(J^{-1}\) has kernel \(qJ^{-1}\) and is onto \(R/qR\). For the kernel claim, if \(Dx\in qR\), choose integers \(a,b\) with \(aD+bq=1\); then \(x=aDx+bqx\in qJ^{-1}\). Surjectivity follows from \(R\subset J^{-1}\). This checks the precise quotient used by both endpoints.

Any supplied basis metadata that Rec receives remains the original fixed metadata. Computing other bases for the reduction does not replace that metadata in its calls. No proof variable is appended to Rec's input. The required recovery premise is therefore pointwise for the actual supplied \(J\) and, when relevant, its actual supplied basis.

## 3. Interface I applies with the stated parameters

Since \(n\ge2\), \(k\ge1\), we have \(\ell\ge2\). The assumed basis-existence statement in I supplies a row basis of operator norm at most

\[
 n^2D^{1/n}\le n^2 2^\rho<2n^2=\tau_2.
\]

This is an analytic witness; the algorithm does not need to find or receive it. Set \(D_{\max}=2^{\rho n}\), \(t=t_A=2n^2\ell\), \(L_A=\ell\), and \(s=\sqrt2\ell^2\). Then

\[
 2ts\sqrt{kn}L_A=4\sqrt2\,n^2\sqrt{kn}\,\ell^4
 \le8n^2\lceil\sqrt{kn}\rceil\ell^4=\sigma.
\]

The theta series in I now has exponent \(-\pi(3\ell^2/4)j^2\), exactly the stated \(\theta_A\). Its \(\Delta\), piecewise \(\eta\), and tail term are exactly \(\Delta_A,\eta_A,\delta_{\rm tail}\), including the branches at and above \(\Delta_A=1\).

To check the replacement of \(\beta_{\rm exact}\), the one-dimensional Gaussian Poisson identity gives

\[
 \sum_{z\in\mathbb Z}e^{-\pi z^2/t^2}
 =t\sum_{z\in\mathbb Z}e^{-\pi t^2z^2}\ge t.
\]

Thus \(D_{\mathbb Z,t}(0)\le1/t\), and \(1+x\le e^x\) yields

\[
 D_{\max}\left(\frac{1+D_{\mathbb Z,t}(0)}2\right)^n
 \le \exp\left(-(1-\rho)n\log2+\frac nt\right)
 =\exp\left(-(1-\rho)n\log2+\frac1{2n\ell}\right).
\]

Taking \(\min(1,\cdot)\) preserves the inequality, so \(\beta_{\rm exact}\le\beta\). Interface I therefore bounds the exact planted actual-secret acceptance by

\[
 \alpha:=\delta_{\rm tail}+\beta+\eta_A.
\]

The exact uniform-multiplier completion is precisely the target recovery experiment and has actual-secret acceptance at least \(\epsilon_{\rm rec}\). These statements compare full experiments with the secret retained for the acceptance predicate, which is essential here.

## 4. Interface II, the complete wrapper, and both endpoints

The bridge widths \(w_B=r_B=\ell^2\) are rational, and \(s^2=w_B^2+r_B^2=2\ell^4\). Also \(\epsilon_B=\nu=2^{-\ell^2}\le1/16\). To check the smoothing lower bound, \(n\le2^{\ell-1}\), so

\[
 \log(8n/\epsilon_B)\le(\ell^2+\ell+2)\log2
 \le2\ell^2\log2<\pi\ell^4.
\]

Hence \(r_B\ge\max(1,\sqrt{\log(8n/\epsilon_B)/\pi})\), as required by II.

The exact scalar-kernel parameter is

\[
 \lceil\log_2(64/\nu)\rceil=\ell^2+6=K_B.
\]

Its trial count satisfies

\[
 L_B=\lceil40K_B(\ell^2+4)\ln2\rceil
 \le40K_B(\ell^2+4)=L_+.
\]

The specification retains this exact \(L_B\); it uses \(L_+\) only as an upper bound. This does not change the stipulated finite scalar kernel or its equivariance.

There are at most \(kn\) elementary quotient draws, \(knL_+\) bridge integer draws, and \(knL_+\) target-error integer draws. Dyadic Bernoulli decisions use fixed fair bits. Thus \(U_{\rm all}=kn(1+2L_+)\) is sufficient, and

\[
 U_{\rm all}2^{-B_{\rm cap}}
 \le U_{\rm all}2^{-\ell^2}2^{-\lceil\log_2U_{\rm all}\rceil}
 \le\eta_{\rm cap}.
\]

The complete cap must be charged in both worlds. Interface II gives the following comparison for the fixed implemented test, including its generated secret, errors, and retained metadata:

\[
 e_P=\Delta_B+kn\nu+\eta_{\rm cap},\qquad
 e_U=kn\nu+\eta_{\rm cap}.
\]

The \(kn\nu\) inside \(\Delta_B\) is the bridge approximation; the added \(kn\nu\) in each endpoint is the independently generated target error. Exact binary secret bits add no approximation. Appending fresh recovery coins and applying its actual-secret acceptance predicate cannot increase TV.

If \(P_P,P_U\) are the implemented planted and uniform acceptance probabilities, respectively, then

\[
 P_P\le\alpha+e_P,
 \qquad P_U\ge\epsilon_{\rm rec}-e_U.
\]

Consequently

\[
\begin{aligned}
 P_U-P_P\ge{}&\epsilon_{\rm rec}-\delta_{\rm tail}-\beta-\eta_A\\
 &-\frac{2k\epsilon_B}{1-\epsilon_B}
 -\frac{2\pi kn}{Pr_B}-3kn\nu-2\eta_{\rm cap}
 \ge\delta.
\end{aligned}
\]

This reconstructs every coefficient in (G). It proves a signed gap, and therefore the claimed absolute gap. No approximate error is silently substituted for the exact target experiment. If (G) cannot hold for a particular parameter choice, that choice simply does not satisfy the theorem's hypotheses.

The resulting \(A_J\) is a single fixed bounded algorithm on every valid \(F^k\) input. Its definition is not restricted to inputs independently sampled in the two reference experiments. This totality is what permits its use in the adaptive BDD reduction.

## 5. Interface III and the rational BDD radius

The bridge's coefficient width is \(\ell^2=w/\sqrt n\), so its exact finite planted law is precisely the law required by III. The ideals, group, rounding rule, metadata, and number of components are also unchanged. The “source gap” is the above property of the fixed implemented \(A_J\), established once.

All parameters before \(a\) are explicit finite quantities in the stipulated order. In particular \(Q_*\) is fixed before \(\epsilon_0\), and \(\epsilon_0\) before \(a\) and \(\chi\). There is no circular choice. The definition of Up is valid: if \(|c_x-x|\le1/8\), then \(x\le c_x+1/8\le x+1/4\), so its ceiling is between \(\lceil x\rceil\) and \(\lceil x\rceil+1\). A fixed certified evaluator makes this an actual deterministic integer procedure.

Cancellation of the two \(\sqrt n\) factors gives exactly

\[
 d_0=\frac{\delta\ell^2}{64nk\chi}\in\mathbb Q_{>0},
 \qquad d^2=\frac{d_0^2}{n}\in\mathbb Q_{>0}.
\]

The required radius upper bound follows comfortably from the supplied hypotheses. Since \(D^{1/n}<2\), \(\chi\ge1\), and \(\delta\le1\),

\[
 d_0\le\frac{\ell^2}{64nk}
 <n^3\lceil\sqrt{kn}\rceil\ell^4
 \le\frac q8<\frac q{4D^{1/n}}.
\]

The conditions on \(\kappa\) can be met by certified sufficient upper evaluations with slack. In particular, increasing an integer \(\kappa\) eventually satisfies the strict exponential inequality. No test of equality at an unspecified real boundary is needed. The numerical inequality (G) remains a supplied mathematical promise.

Interface III now supplies the actual C8 bounded bit program, with error

\[
 p=(n/2)e^{-\kappa}+\zeta.
\]

From \(\kappa\ge\log(8n/\zeta)\),

\[
 0<p\le\zeta/16+\zeta=17\zeta/16\le17/128<1.
\]

The explicit posterior allowance is consistent with the finite error account:

\[
 \frac{2kQ_*\epsilon_0}{1-\epsilon_0}
 \le \frac{\zeta}{32}\frac{16}{15}
 =\frac{\zeta}{30}<\frac{\zeta}{16}.
\]

The remaining conditional budgets, the single global sample counter, both orientations, and the finite walk/candidate verification rules are covered by the assumed interface III guarantee. Their total extra error is \(\zeta\). The theorem does not demand an exactly Haar physical multiplier endpoint: III explicitly compares that physical kernel with a proxy. Nor is the original source-gap loss multiplied by the number of oracle calls. Those are different comparisons.

The all-input bound applies even to the wrong orientation and targets outside the decoding promise. This matters for circuit compilation and cannot be replaced by an expected runtime or an on-promise bound.

## 6. Conversion of the BDD promise to interface IV

For a coefficient vector \(e\), each complex embedding is a sum of its coefficients times unit-modulus roots. Therefore

\[
 \|e\|_{\infty,\mathrm{canonical}}
 \le\sqrt n\|e\|_{2,\mathrm{coefficient}}.
\]

A rational target within coefficient distance \(d=d_0/\sqrt n\) is thus inside C8's closed canonical-infinity promise. There is no rounding of that target. In particular, the actual quantum input labels produce the exact rational targets \(Bv/H\).

For completeness, the required shortest-vector inequality follows from ideal arithmetic, not from the existence of a short supplied basis. If \(0\ne x\in J^{-1}\), then \(xJ\subset R\), so

\[
 |N(x)|D=[R:xJ]\ge1.
\]

Parseval for the \(n\) cyclotomic embeddings and the arithmetic-geometric mean inequality give

\[
 \|x\|_2^2=\frac1n\sum_\sigma|\sigma(x)|^2
 \ge|N(x)|^{2/n}\ge D^{-2/n}.
\]

Hence

\[
 \lambda_1(L)\ge qD^{-1/n}>4d_0\ge4d.
\]

The promised lattice point is unique and is the closest coefficient-Euclidean lattice point. Exact membership checking and conversion to integer \(B\)-coordinates leave every successful C8 answer unchanged. Malformed or nonmember answers may be assigned a fixed output; their correctness is not assumed. The BDD hypotheses of IV, including \(0\le p\le1\), are therefore met.

## 7. Finite parameters and coherent call layout

The basis \(B\) is rational and nonsingular. Clearing its supplied denominators gives an integer nonsingular \(A=bB\), and \(U,V\) are finite positive integers. The least-power-of-two choice of \(H\) is an exact comparison between rational squares. It terminates, and its exponent has finite polynomial bit length in the supplied rational data and precision exponents. The same applies to \(N_g\) and \(\lceil cd\rceil\); evaluating a rational square root as an exact real primitive is unnecessary. Every other ceiling of a base-two logarithm in the register formulas can be determined by integer comparisons. The typed encodings count actual numerators, denominators, and list contents.

The finite-register input grid \(L/H\) does not have to equal the source-test group \(F\). Interface III converts a fixed test on \(F\) into a rational-target decoder on \(L\); IV then asks that decoder about finitely encoded \(L/H\) targets. This is a sequential interface composition, not an identification of the two grids or provision of an external sample oracle.

At those finite target widths, the bounded program has a finite bit-operation bound. Its number of recovery invocations is at most \(Q_*\) on every target and tape. The specified dispatcher turns this into a structural bound: each of \(Q_*\) slots runs the bounded nonrecovery computation until the next call or termination, exposes one valid sample input, executes one recovery block, and routes its result. Terminated branches instead expose a valid fixed dummy input and ignore the result. A final bounded segment finishes the computation after the slots.

Every active recovery input is a valid ring-sample tuple of the stipulated input length, with the same fixed metadata. Dummy inputs are also valid. The supplied all-valid-input, all-tape recovery runtime therefore suffices, including coherent branches. One can cap its compiled execution at that bound on all bit strings without changing its action on any reachable valid input. A malformed returned object is processed as failure.

Padding preserves the law of the original active computation: each active invocation obtains fresh independent fair coins, and dummy results have no effect. The circuit also contains exact lattice membership and modular conversion to the required \(m=nb_u\) output bits. Their cost is part of \(S_{\rm dec}\), not an uncounted verifier.

This call-slot construction is stronger than a classical pathwise call bound. A layout-preserving compilation has exactly \(Q_*\) recovery blocks per forward decoder execution, and its reversal has the same number. Keeping all coins and intermediate bits permits reversible execution of the full classical code. No single random tape good for every target is required; IV assumes only the pointwise success probabilities and explicitly covers this coherent use.

An explicit bit-machine tableau unrolling supplies the stated polynomial host construction and a bound of the displayed form. With \(s=P_{\rm dec}+T_{\rm dec}+nh_Q+m+1\), there are at most polynomially many tape cells, state bits, and transition entries bounded by \(s\). A direct bit-level transition lookup and update uses \(O(s^3)\) Boolean gates per step and at most \(s\) steps. The constant \(2^{20}\) is ample for an ordinary explicit binary-tape AND/XOR/NOT implementation of these selectors and updates. Applying the unrolling separately to the bounded slot segments and the exposed recovery blocks retains their layout with the same fourth-power bound. Fresh fair-bit consumption is at most \(T_{\rm dec}\). This is an existence construction for the stated bit-machine model, not a count for arbitrary code generators, arbitrary high-level operations, or merely the unpadded active path. The alternative use of the actual emitted circuit counts is explicit in the theorem.

No source code or emitted circuit was an allowed input to this audit. Thus this paragraph verifies the mathematical availability and proper scope of the compilation step; it does not certify a particular compiler output or serialization time.

## 8. Dual sampler, the final same-ideal map, and every output branch

Applying IV with the preceding rational basis, \(d^2\), bounded decoder, and prescribed finite registers yields a classical law on

\[
 \Gamma=(qJ^{-1})^*=q^{-1}\bar J
\]

at coefficient Gaussian width

\[
 s_\Gamma=\frac{\sqrt n}{\sqrt2d}
 =\frac n{\sqrt2d_0}.
\]

Its TV bound is exactly

\[
 \min\{1,\varepsilon+2\sqrt p+E_n\},\qquad
 E_n=2\sqrt{\tau_n}+2\sqrt{2(\tau_n+2^{-16n})}+\tau_n.
\]

The input off-promise tail is already inside the explicit \(\tau_n\) terms supplied by IV. It is not another contribution to \(p\). The finite Gaussian caps, actual measured coset labels, adaptive phase resources, and retained or entangled work are likewise within the stipulated complete-law statement of IV. This audit does not replace that statement with a claim about a pure Gaussian state.

The output map is the bijection \(\phi(z)=q\bar z\) from \(\Gamma\) to the same supplied \(J\). Conjugation preserves coefficient norm and multiplication by \(q\) multiplies it by \(q\). Consequently, including the normalizer,

\[
 \phi_*D_{\Gamma,s_\Gamma}=D_{J,qs_\Gamma},
 \qquad qs_\Gamma=\frac{nq}{\sqrt2d_0}=s_J.
\]

Indeed, the numerator at \(j=\phi(z)\) is \(\exp(-\pi\|j\|_2^2/(q^2s_\Gamma^2))\), and the bijection converts the entire denominator sum to the sum over \(J\). Thus no determinant or extra \(n\) enters the output Gaussian normalizer. TV cannot increase under this deterministic map; for a bijection it is preserved.

Any measured Fourier label, whether produced on a successful decoding branch or not, yields \(B^{-T}t_{\rm cent}\in\Gamma\), so its final image belongs to \(J\). Final cap or failure outputs equal zero and also belong to \(J\). Internal fallback draws need only be the valid values specified by their kernels; the theorem's zero-fallback statement is naturally about final sampler fallbacks. The universal claim that the final output lies in \(J\) does not require every internal fallback integer to be zero.

The coefficient width is \(s_J\), and the full canonical Euclidean convention multiplies it by \(\sqrt n\). Inversion, conjugation, and the factor \(q\) have all been accounted for explicitly.

## 9. Execution resources, setup, and repetition

Interface IV gives the nondecoder allowance \(G_0\), the actual forward/reverse decoder allowance \(4S_{\rm dec}+m+2r_{\rm dec}\), the prescribed gate set, and the memory and measurement bounds. This includes its own finite transcendental and register preprocessing. The call-slot construction gives at most \(2Q_*\) coherent executions of the supplied recovery code, including dummy blocks. Early final failures can only reduce that count. This is coherent execution of known bounded code, not access to a classical remote recovery service.

The ideal/decoder setup and layout-preserving host compilation are different operations. Their actual bit cost \(T_{\rm setup}\), including serialization, must be added for an end-to-end mixed count. The theorem does so explicitly. It does not infer a numeric compilation cost from a circuit gate count, and it does not double-charge IV's preprocessing. The finite input encodings and unrolling bounds are essential complexity parameters. There is no resulting uniform runtime claim for recovery programs without the supplied all-input bound.

Fresh independent preparations and decoder coins produce a product of the one-sample implemented laws. Tensorization, or a product coupling, bounds its distance from the ideal product law by the sum of the one-sample distances. For every integer \(u\ge1\), the stated bound

\[
 \min\{1,u(\varepsilon+2\sqrt p+E_n)\}
\]

and the count \(2uQ_*\) follow. The conclusion concerns ordinary measured samples.

## 10. Adversarial checks and limits of the verdict

I checked the small admissible dimensional endpoint \(n=2\) through the inequalities \(\ell\ge2\), the bridge smoothing bound, \(\epsilon_B\le1/16\), and the strict BDD separation. The inequalities above continue to hold without an asymptotic qualification. I also checked the piecewise cap in \(\eta_A\), the possibility that (G) is unsatisfiable, the closed BDD boundary, malformed decoder outputs, off-promise and wrong-orientation termination, inactive recovery slots, final zero branches, the exact Gaussian normalizer under the output map, and independent repetition. No numerical experiment was needed.

The conditional composition does not prove the four interfaces. In particular, the detailed finite C8 routines, the posterior/physical-query estimates, and the quantum preparation/phase-resource analysis remain assumed. No linked source or actual implementation was inspected. A later audit of those objects could invalidate a dependency without contradicting the present conditional reconstruction.

The output ideal is exactly the supplied \(J\), under the pointwise recovery premise and the norm/coprimality restrictions. Nothing here transforms arbitrary ideal-lattice instances into this eligible family or replaces pointwise success with success averaged over ideals. Therefore the result is a conditional same-ideal ordinary-DGS reduction, not a standard worst-case hardness implication for binary RLWE.

No substantive composition gap or counterexample was found under the four explicit assumptions. Same-model independent review provides correlated scrutiny, not formal verification.
