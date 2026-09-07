# Binary-secret rank-one RLWE: finite exploration

**COMPLETED EARLY — 2026-09-06 10:53:58 UTC.** The finite research schedule finished before the launcher-owned deadline of 15:11:38 UTC. [status.json](status.json) records research completion; [shutdown.json](shutdown.json) records zero active workers and experiments.

The session found a useful conditional extraction statement, sharper distinctions within the lossiness framework, and a quantitative noise-conversion lemma. None supplies a hardness theorem for the reference problem from an independently supported source assumption. Two structural directions survived bounded nonauthor criticism and reconciliation. The third’s independent hardness explanation was retired, with its checked transfer lemma preserved. [Criticism and reconciliation](reconciliation.md) record the strongest objections and corrections.

## Reference problem and evidence

The reference is search RLWE in
\[
R_q=\mathbb Z_q[X]/(X^n+1),\quad
S_j\overset{\$}{\leftarrow}\{0,1\},\quad
(A_i,B_i=A_iS+E_i),
\]
with growing power-of-two degree, rank one, coefficient basis, odd polynomial-size modulus, independent uniform ring multipliers, and up to polynomially many independent ring samples. Errors have independent coefficient law \(D_\sigma(z)\propto e^{-\pi z^2/\sigma^2}\), with \(q/\sigma\ge n^c\). Here \(\sigma\) is a width, not a standard deviation. This comparison region is not asserted to be uniformly hard. All modular likelihoods use the wrapped law \(W_{\sigma,q}\); ring rotations never become independent samples. [Full contract](target.md).

Evidence labels distinguish **source-verified results**, **fully written small calculations**, **experiments**, **refuted claims**, and **unresolved bridges**. Agent agreement is not confirmation. Most positive statements below are our calculations using explicitly checked source theorems, not claims made by those authors. Average-case search, decision, worst-case assumptions, and restricted algorithm models remain separate.

## Approach map

Twelve fresh scouts covered different mechanisms; six initially saw only the formal target for ten minutes, and six also saw the barrier inventory. All later checked the baseline. [Inventory](inventory.md), [selection reasons](selection.md), and [rejected/deferred record](rejected-or-deferred.md) preserve minority findings.

| Scout | Mathematical object | Main finding |
|---|---|---|
| [S01](scouts/S01.md) | Wrapped posterior and planted partition function | Statistical quiet planting to uniform fails in the reference small-noise comparison; computational hardness remains separate. |
| [S02](scouts/S02.md) | Simulation between secret-prior experiments | Posterior transport is exact but computationally circular; public marginals do not preserve the original witness. |
| [S03](scouts/S03.md) | Ring towers and binary packing | Extension packing needs correlated response components absent from the source oracle; trace gives the reverse arrow. |
| [S04](scouts/S04.md) | Fourier mass of ideal projections | Conditional extraction through a binomial quotient; entropy alone does not guarantee extraction. |
| [S05](scouts/S05.md) | Norms, Boolean fibers, algebraic codes | Field kernel dimension need not produce binary collisions; simple public masks can be decoded. |
| [S06](scouts/S06.md) | Occupied lattice cosets and guessing | Sampler coins add no posterior information under the fixed-kernel hypothesis; precursors can over-observe. |
| [S07](scouts/S07.md) | Joint likelihood moments | Pairwise agreement with independent matrices breaks at three-point correlations. |
| [S08](scouts/S08.md) | Exact public group actions | Noise-preserving affine actions mix only within small orbits; exact reversal restrictions do not exclude approximation. |
| [S09](scouts/S09.md) | Residual characters and Boolean algebra | A precise low-rank Fourier witness would give an attack; no target witness was found. |
| [S10](scouts/S10.md) | Planted coding and knapsack sources | Coding lifts lose recovery or introduce carries; knapsack transport works but its exact source is tailored. |
| [S11](scouts/S11.md) | Quantum Fourier sampling of sample lists | The direct sparse-state Fourier measurement has a polynomial classical simulation. |
| [S12](scouts/S12.md) | Control: revisit old lossiness | The precursor leaks cosets before the final index bound; low-index replacements still need pseudorandomness. |

## C01: conditional extraction through a ring quotient

**Retained as an extraction diagnostic, with an unresolved bridge.** Let \(q\equiv1\pmod{2n}\) be prime and polynomially bounded. Choose a power-of-two divisor \(L=\Theta(\log^3 n)\), put \(d=n/L\), and let \(a\) have order \(2L\). For \(J=(X^d-a)\), the quotient groups binary coefficients into independent weighted blocks. Add the explicitly auxiliary observation \(Y=S+G_\tau\bmod q\), where \(\tau\ge\tau_0>0\) and the Gaussian coefficients are independent.

The posterior bits remain independent. If \(p_y=\Pr[S_j=1\mid Y_j=y]\) and \(\beta=4\mathbb E[p_Y(1-p_Y)]\), an exact Fourier calculation gives
\[
q^d\mathbb E\operatorname{Coll}(S\bmod J\mid Y)=(1+k_L)^d,
\qquad
k_L=\sum_{t\ne0}\prod_{k<L}
\left(1-\beta\sin^2(\pi ta^k/q)\right).
\]
The factors are squared Fourier coefficients of an effective biased Bernoulli law; this changes only the calculation, not the true binary secret. An unconditional uniform affine-walk bound then yields
\[
\operatorname{TV}\big((S\bmod J,Y),(U_{R_q/J},Y)\big)=\operatorname{negl}(n).
\]
This is our deduction from [Breuillard–Varju, Theorem 5](https://arxiv.org/pdf/1909.09053), with exact quantifiers and width dependence in the [C01 dossier](candidates/C01.md).

The mechanism supplies a distribution-sensitive statement for a quotient of dimension \(\Theta(n/\log^3 n)\). Multiplication by an element of the complementary ideal depends only on this extracted quotient, giving a precise possible role in a decision hybrid. A simple leakage chain rule already preserves linear residual entropy for any quotient this small; C01’s extra content is conditional uniformity, rather than a new search-lossiness entropy budget.

**Strongest objection:** the obvious sampler is efficiently distinguishable. If \(g=(X^n+1)/(X^d-a)\), then \((gP)_{j+kd}=a^{L-1-k}P_j\). For \(A=gP+F\) with small coefficient errors, enumeration of \(P_j\in\mathbb F_q\) checks each block in polynomial time. Uniform false acceptance is at most \(q^d(s/q)^n\) when each error coefficient lies in a set of size \(s\). Hiding \(a\) among polynomially many choices does not remove the test.

Thus the tailored hidden-binomial-ideal source is **refuted in that regime**. The independently studied HLBDD assumption does not immediately substitute: its ideal family, noise-swallowing conditions, and active-coordinate invertibility step differ from this lemma's polynomial-modulus setting. [Order-LWE, Section 7](https://eprint.iacr.org/2018/494.pdf).

The unresolved bridge is a pseudorandom public sampler and response simulator preserving the actual iid target errors. Auxiliary \(Y\) is not an RLWE transcript; no sample-count or secret-recovery reduction is completed. The critic has supplied a bounded-auxiliary-width extension: if the auxiliary Gaussian keeps its iid law conditional on public-sampler coins, and an independent additive completion matches the target noise, a single-coordinate Fourier bound forces the perturbation coefficients to be small. This defeats that completion template as well. Allowing the coins to encode the auxiliary noise makes the unrestricted formulation false. The next question is the corresponding bound for growing auxiliary widths; it remains unresolved.

## C02: actual-transcript lossiness and the control track

**Retained as a structural diagnostic, with an unresolved bridge.** The exact quantity to bound is
\[
g(a)=2^{-n}\sum_y\max_s
\prod_{i,j}W_{\sigma,q}\big(y_{i,j}-(a_is)_j\big).
\]
A source-based lossiness argument needs this guessing probability small for an appropriate fraction of an efficiently sampled, computationally pseudorandom public tuple. The [C02 dossier](candidates/C02.md) defines the old DSPR ratio source, Hermite-form RLWE source, sampler, and hybrid separately from the desired binary target. This is a concrete missing entropy statement, not an assumed binary-RLWE hardness theorem.

Two exact calculations distinguish necessary loss from an analysis artifact. First, when sampler coins \(T\) choose \(A\) independently of the secret and the entire fixed error kernel, \(S\perp T\mid(A,B)\). Revealing those coins cannot change statistical guessing. Second, a secret-dependent precursor can reveal much more: the old continuous precursor discloses \(S\bmod\Lambda\) on an explicitly bounded no-wrap event, before the final determinant estimate is used.

For an exact lattice-coset observation,
\[
\widetilde H_\infty(S\mid S\bmod\Lambda)
=n-\log_2N_{\rm occ},
\]
where \(N_{\rm occ}\) counts cosets meeting the Boolean cube. This is the relevant partition size. It can still equal \(2^n\), for example when \(\sigma_{\min}(M_f)>\sqrt n\); tightening the determinant bound then cannot restore precursor entropy.

Conversely, exact accounting can change the regime. The fixed denominator \(f=1-X-X^2\) has quotient \((\mathbb Z/L_{n/2}\mathbb Z)^2\), where \(L_k\) is a Lucas number. Its index is about \(\varphi^n\), leaving at least approximately \(0.306n\) bits under exact-coset disclosure, while its exponent is exponential. This refutes an inference that positive coset entropy must imply a small scalar denominator-clearing attack. Nevertheless, the known polynomial \(f\) itself exposes short numerators, so it supplies no pseudorandom sampler.

The bounded wrapped experiment [E04](experiments/wrapped_precursor.json) also demonstrates strict over-observation. With fixed \(A=1\), the discrete precursor \(K=(q+1)S+E\bmod2q\) maps to \(B=K\bmod q\). At \(n=16,q=257,\sigma=16\), the public transcript retains about 14.6 bits, while the precursor nearly determines \(S\). Printed zeros reflect numerical precision. Fixed \(A\) is an explicit departure from uniform public RLWE.

**Strongest objection:** none of these controls produces a public tuple that is both pseudorandom and lossy under the exact reference errors. The old theorem gives a mild search implication under its own definitions, not automatically negligible average success, decision hardness, or arbitrary finite Gaussian sample budgets. [Brakerski–Döttling, Definition 4.1/Theorem 4.2](https://eprint.iacr.org/2020/1185.pdf).

A source-import norm qualification is preserved: deterministic inverse-event injection is sound, but the probability transfer between canonical and coefficient conventions was not certified. Separately normalized deductions and unit-conditioning restrictions appear in the dossier, using [Stehlé–Steinfeld, Sections 2.2 and 4.1](https://eprint.iacr.org/2013/004.pdf). This session did not become a source-proof audit. Critic-owned [E05](criticism/C02/boolean_fibers.json) found \(N_{\rm occ}=8,48,2208\) at degrees 4, 8, and 16: exactly one class, represented by \(2+X\), is missing. Full occupancy is therefore refuted already at degree 4. The next small lemma asks whether the index-minus-one formula holds for every growing power-of-two degree; three examples do not establish it.

## C03: a retained transport lemma, without an independent hardness explanation

The independently described planted source publishes \(t=a_1x+a_2y\), with uniform ring weights and two independent binary blocks. On the unit branch for \(a_2\), write \(A=a_2^{-1}a_1\), \(C=a_2^{-1}t\), and \(H=1+X+\cdots+X^{n-1}\). The public map
\[
A'=2A,\qquad B'=2C-H+G_\sigma
=A'x+(2y-H)+G_\sigma
\]
preserves rank, degree, odd modulus, coefficient basis, and the original binary secret \(x\). It produces exactly one ring sample, with sign-plus-Gaussian error rather than exactly Gaussian error. Recovering \(x\) gives the original \(y=C-Ax\).

**Fully written calculation:** if a one-sample target solver succeeds with probability \(\epsilon\), the centered simulation recovers the planted source with probability at least
\[
\rho_q\epsilon^2
\left[1+e^{\pi/\sigma^2}
\bigl(\cosh(2\pi/\sigma^2)-1\bigr)\right]^{-n},
\]
where the unit probability \(\rho_q\) is inverse-polynomial for every reference odd modulus. The proof uses the reverse order-two Rényi moment of the joint secret-and-input experiment; coefficient products tensorize and wrapping contracts it. It retains the original witness, avoiding posterior-resampling circularity. [Dossier and full calculation](candidates/C03.md).

The loss is polynomial when \(n/\sigma^4=O(\log n)\), improving an uncentered \(n/\sigma^2\) certificate. No negligible-TV claim is needed. [E03](experiments/centered_noise_renyi.json) checks scalar identities numerically and records that centering is worse at the smallest tested widths; it is secondary evidence only.

**Decisive objection:** on units, this source is exactly binary-secret/binary-error RLWE after normalization. The checked compact-knapsack inversion result needs different coefficient widths and unbounded block count; the negacyclic result supplies collision hardness under compression conditions absent here. Neither supports this exact planted source. [Micciancio, Theorems 4.2/4.8](https://cseweb.ucsd.edu/~daniele/papers/Cyclic.pdf); [Lyubashevsky–Micciancio, Theorem 5.1](https://cseweb.ucsd.edu/~daniele/papers/IdealHash.pdf).

The independent hardness explanation is therefore retired. The quantitative lemma remains useful, with one-sample scope and no decision reduction. A solver using many independent samples is not covered. The next small question is whether adjusting the added Gaussian variance cancels the leading term and improves the scalar moment to \(1+O(\sigma^{-8})\). This is unproved and would improve transport parameters, not validate the source assumption.

## Negative findings and limits

The strongest negatives are explicit failures of mechanisms: a statistical planted/null separation, missing correlated tower responses, efficient tests against particular ideal samplers, and a nearby source assumption without a supporting reduction. Exact symmetry restrictions and sparse quantum simulation apply only to their specified models. Three-point likelihood discrepancies do not become attacks; raw moments may be dominated by rare events. Finite arithmetic examples do not establish an asymptotic family or cryptographic hardness.

Six bounded experiments completed, with code, parameters, cutoffs or exact arithmetic, failures, and timeouts in the [registry](experiments/registry.json). They support diagnostics, never hardness. Public-source access failures and the norm qualification are recorded in [source notes](sources/index.md); [sources.bib](sources.bib) preserves the bibliography. Novelty claims are deliberately limited. The eventual source bridges, precise sample extensions, and decision implications remain unresolved.

**Execution record:** twelve scouts, three investigators, three nonauthor critics, and six bounded experiments completed. Phases advanced early; the manifest and its deadlines were unchanged. [Artifact checks](artifact-checks.json) passed, and no research continuation remains. Reviews were bounded and nonblind; one critic consulted proof-audit guidance but no formal audit was undertaken. Shared sources and later exchanged notes limit independence. One discovery scout reported accidentally opening the coordinator source index; its findings were not treated as independent confirmation. The launcher owns its process-exit record, which is finalized after the coordinator returns; this report records the completed research schedule, not an unobserved launcher exit.
