# C03 review — noise, implementation, multiple samples and recovery

**Disposition:** the detailed completion, sampler, common-K hybrid, leakage and recovery arguments survive this bounded independent audit. One exact ledger statement was false because its domain guard was omitted: C03-O01 rejects the literal frozen NC1 v1 sentence. The separately supplied NC1 v2 correction closes that objection. Its A2 and prescribed-polynomial-m applications are unchanged. This review supplies no evidence of computational hardness for either correlated source.

This is a fresh nonauthor mathematical review, not formal certification or an independent statistical vote. No experiment, implementation project, worker, external execution or continuation was used. The reviewer verified affirmative launch authorization and deadline-supervisor verification, the frozen run identity/paths/model, start and all phase times. The run starts 2026-09-06T14:21:13.181175+00:00, with workers stopping at 19:06:13.181175 UTC and hard stop 19:21:13.181175 UTC. C03's earlier research stop is 16:10 UTC and task deadline 16:15 UTC; the bounded checks were exhausted earlier.

## Frozen inputs and versions

The PLAN, BRIDGE_CONTRACT, TASK_TEMPLATE, run configuration, mathematical-proof-audit skill and its probability regressions, and the complete frozen known-counterexample registry were read first. The full prior C02 checks-and-regressions note was also read. Every one of the 36 files listed in the review-v1 manifest matched its SHA-256 hash. The exact paths, complete hashes and primary-source inventory are saved in [review-inputs.json](review-inputs.json).

All following paths are relative to `snapshots/review-v1/`. These are the mathematical files actually reviewed, with abbreviated hashes only for convenient identification; the companion inventory contains the full hashes.

| File | SHA-256 prefix |
|---|---|
| claims.json | 4c1194bb72d934fd |
| known-counterexamples.md | d2fb558136f7d100 |
| foundations/F02-review-packet.md | 80e4b719b6539138 |
| foundations/F02-completion.md | 392bff6701967ba5 |
| foundations/F02.md | bfe968ec19716444 |
| foundations/F01-theorem-v1.md | e8b8218ca2bb2d85 |
| foundations/F01.md | c6a09c470a6d2e8b |
| development/D03.md | 28bf75236f664642 |
| development/D03-common-k.md | 7ba3052a8358f37f |
| refinement/R03-interface-audit.md | ff47bae8fabbcac4 |
| candidates/A.md | f97e502a68671c5a |
| parameter-table.md | cba87cbe8ca21acf |
| multi-sample.md | 8c464cd2b82e4f1a |
| bridge.md | c14f0ec141c471be |

The separately requested correction is `corrections/NC1-v2-and-dependencies.md`, SHA-256 `a801c12d79a1d74093cc0a7ab265e2d4580521dafaf823694bc905011f15cad1`. Its statement, rather than any subsequently edited live ledger, is the NC1 v2 reviewed here. No frozen author note was edited.

## Independent completion and sampler checks

Let M be integer p-by-n, B=sigma^2 I_p-tau^2 MM^T>0 and Theta=tau^2 I_n-tau^4 M^TM/sigma^2. Woodbury gives Theta^(-1)=tau^(-2)I+M^T B^(-1)M and mu_z=tau^2 M^T z/sigma^2. Expanding independently yields

    ||g||^2/tau^2+(z-Mg)^T B^(-1)(z-Mg)
      =||z||^2/sigma^2+(g-mu_z)^T Theta^(-1)(g-mu_z).

Every integer z has h=z-Mg integer, so this computes the convolution for rectangular or singular M without a lattice-index assumption. Poisson summation is on Z^n, giving a factor r_z in [1-delta,1+delta], where delta=sum_(k!=0) exp(-pi k^T Theta k). The normalized output is exactly P(z)r_z/E_P r, P=D_sigma^p. When delta<1, its TV is at most delta/(1-delta); wrapping contracts it. The argument compares full output laws, not covariance matrices. [Peikert's primary Theorem 3.1](https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf) was checked: its second draw is on a shifted lattice depending on the first draw. F02 correctly supplies its own independent-summand proof rather than silently importing a different experiment. Sections 2.4–2.5 also confirm the exponent/covariance convention.

For B=L diag(v_i)L^T, the recursion uses residuals y_i=h_i-c_i, not raw past h_j. Thus y=L^(-1)h and its exact chain probability is exp(-pi h^T B^(-1)h)/product_i Z_i(c_i). Each pivot is a Schur complement and satisfies v_i>=beta=lambda_min(B). The one-dimensional Poisson bound on Z_i(c)/sqrt(v_i) is pointwise for every real c. It therefore controls the entire denominator product even when centers depend on earlier draws. Normalizing once more gives the stated ratio bound and eta_seq when kappa(beta)<1. HC2 in [hand-controls.md](hand-controls.md) explicitly makes the normalizer depend on parity, showing why H_seq cannot be called exact D_B.

The R03 approximation is sufficient without implementing it. At A2 all matrix entries have polynomial bit length; positive principal determinants and rational forward substitution bound the reduced arithmetic sizes. Pivots lie in [3sigma^2/4,sigma^2], and the squared norm of each L row is at most 4/3. On a truncated path, |y_i|<=n sigma+2, so |c_i|<=sqrt(4n/3)(n sigma+2). These are uniform bounds, including rare histories.

The interval radius n sigma+2 permits comparison of each omitted shifted tail to an integral beginning at n sqrt(v_i). Dividing by the Poisson lower normalizer gives the stated per-stage bound 2 exp(-pi n^2)/(pi n). Every truncated table contains a point of weight exceeding 1/4. With N<=N_max and individual weight error at most 2^(1-p), categorical TV is at most 4N*2^(1-p)<=2^(-n)/(128n) under R03's specified p. Summing 2n Gaussian-table errors gives 2^(-n)/64. The at most 5n capped draws add at most 5n*2^(-L_cap); each failure probability is conditional on the whole past. Capped fallbacks preserve support cardinality and active nonzeroness. Machin/Taylor approximation with range reduction has polynomial bit complexity at the bounded exponents. The resulting xi_src<2^(-n) claim is valid for sufficiently large n.

F is exactly the truncated law in A2; G is a fresh full iid D_ell law. Source H_seq depends on F and fresh source coins only. Noise retains J,U,F and integrates H out; extraction retains the entire H,Y tuple. No hidden-G-sampler or changed-law shortcut occurs. Finite source approximations are charged at both computational endpoints. Independently reconstructing the two edges gives xi_src+2xi_1 for B1 and xi_src+xi_Y for B2: its uniform endpoint stays exactly uniform for every independently drawn y. The total 2xi_src+2xi_1+xi_Y is correct. Eta_seq appears only in the mathematical noise edge and is not paid again as an implementation error. Public target TV alone does not transfer an original planted-witness event.

## Wrapped obstruction, deconvolution and Renyi checks

I checked [NIST DLMF identity 20.5.3](https://dlmf.nist.gov/20.5.E3) directly. Dividing the theta product by its zero-frequency value gives positive factors whose coefficients 4v/(1+v)^2 increase with v. Finite products decrease as tau increases; convergence gives the claimed monotonicity for every finite tau>=tau_0 with no upper-width restriction. The discrete MGF proof in HC3 yields Var(D_sigma)<=sigma^2/(2pi) exactly. The +/-1 atoms and sin(pi x)>=2|x| for centered |x|<=1/2 give the factor 16 D_tau0(1). The characteristic-function discrepancy under TV epsilon is at most 2epsilon. These recover NO1's coefficient bound, including its constants. An averaged retained-variable noise bound supplies only an average conditional error; the stated Markov exceptional mass must remain. The zero-error case is simply exact correctness almost surely.

All Gaussian Fourier coefficients here are positive, so exact independent deconvolution has a unique inverse. The inverse must be nonnegative; ratios in (0,1] are insufficient. I recomputed both the wrapped-Gaussian Z/5 contradiction and rational signed-inverse control in HC4, including the claimed fixed 10^(-5) approximate separation. This finite obstruction does not contradict growing-width smoothing. The Renyi inequality has the correct P||Q direction and applies to a positive event in a joint law retaining the secret. The two-point control rejects transfer of signed decision advantage. Only the quantitative TV loss sqrt(M_2-1)/2 gives the indicated general decisional comparison.

## Common-K and multiple samples

KM's source defines V_i=U_i K directly, with one quotient-uniform K independent of the entire Gamma_m conditional on J. U_i in Ann(J) is enough for this definition; individual bijectivity is unnecessary for KM. After full joint noise comparison and one extraction, set K'=Z-pi_J(Y). For every fixed Gamma_m,Y it is quotient-uniform. Since Y is independent of Gamma_m, the whole result is exactly a common-K source followed by the public map (a_i,c_i)->(a_i,a_iY+c_i). This map is a bijection on all 2m ring coordinates for each y, including in rings with zero divisors. The first source edge replaces the whole multiplier vector; no m-fold extraction error or tensor product of one-sample source assumptions is used.

For fixed bijective U_i the ideal tuple has |I| equiprobable points in I^m, giving exactly 1-|I|^(1-m) retained TV from independent ideal points. The F_3 control gives 2/3. Neither quantity is automatically a public distance after adding noise and forgetting U.

For p=mn, the required stacked B has off-diagonal blocks -tau^2 M_Fi M_Fj^T. Its smoothing matrix Theta remains n-dimensional. The complete-square calculation above therefore proves a full p-dimensional product target; it does not infer joint independence from marginals. With sigma_m=2n ell^3 sqrt(m), the operator bound gives Theta>=3ell^2 I_n/4 and B>=3sigma_m^2 I_p/4. The smoothing and p-stage sequential errors are negligible for every prescribed fixed polynomial m(n). The p-dimensional rational arithmetic and O(p^2 sigma_m) table enumeration are polynomial; sigma_m^2 is rational, so the matrix construction does not require an exact irrational square root.

This changes sigma, the common ideal-point law and the full H kernel. It requires its own Pm, including its chosen d and public m(n). At fixed q the condition sigma_m n^c<=q restricts m; for m=n^r the numerical exponent requires K>1+c+r/2, with qualifying split primes still required. It proves neither unchanged-width expansion nor an unlimited sample oracle for one fixed parameter family. A2's full Gamma_m extraction extension is valid as a common independent kernel conditional on T, **if X1 itself is established**; C03 did not audit X1's number-theoretic import.

## Leakage and exact recovery

The unwrapped likelihood ratio for a fair bit is exp((pi/tau^2)(2sum_i y_i-m)). Fixed coefficient channels factor even after the entire observation vector is given. The MGF bound gives per-bit error exp(-pi m/(4tau^2)). Centering is exact on |G_ij|<=(q-3)/2; its complement costs at most 2nm exp(-pi(q-3)^2/(4tau^2)). These reproduce the full-recovery bound. Full recovery, quotient entropy depletion and small information loss are separate claims; neither Shannon entropy alone nor a per-coordinate uniformity assertion proves extraction.

Conditionally couple the real quotient W and uniform Z given J,Y_vec. Fano gives d log2 q<=H(W|J,Y_vec)+h_2(eta)+eta log2(q^d-1). Since H(W|J,Y_vec)<=H(S|Y_vec), the all-distance bound eta>=1-[H(S|Y_vec)+1]/[d log2 q] follows. At A2, d log2 q=Theta(sqrt(n)/(ln n)^3). Substituting m=C tau^2 ln n makes its entropy ratio tend to zero for the stated strict C>2/pi; the refined log-log term also checks. HC7 separately checks A1's C>8/pi threshold at tau^2 ln ln n. These are exposed-auxiliary obstructions, not attacks on an RLWE transcript whose Y is hidden.

REC's same-budget proof correctly subtracts the noise-tail mass from solver success. Under uniform inputs, conditioning on all multipliers, each fixed binary candidate passes all m residual tests with probability v_T^m; a union over 2^n candidates handles any adaptive output. This proves Adv_dec,m>=epsilon_rec-m delta_T-2^n v_T^m. Under q/sigma>=n^c and polynomial q, the box radius ceil(sigma ln n) eventually has 2B+1<q, negligible Gaussian-tail loss and negligible 2^n v_T^m, including m=1.

For held-out verification, conditioning on the complete solver prefix, its tape and S leaves h fresh iid target errors, justifying epsilon_rec(1-delta_T)^h. Under uniform input, the candidate is fixed before the h uniform responses, giving v_T^h without a union over candidates. This consumes m+h samples. The two-atom and cached-prefix controls in HC6 reject multiplication on reused data. Neither verification method identifies a planted witness merely from residual validity, and neither imports mild-search amplification.

## Primary sample-expansion interfaces checked

[Order-LWE Definition 2.13 and Lemma 7.6](https://eprint.iacr.org/2018/494.pdf), printed pages 11 and 39–40, explicitly require negligible swallowing ratios and an additional ordinary-RLWE premise. The expansion multiplies both seed coordinates by a common new z; its error includes the seed error times z and the secret times a fresh perturbation. D03 correctly refuses an unchanged-width import. A joint argument is needed for that pair, not two marginal statements. This limited interface check does not audit or refute the paper's entire theorem.

[Brakerski–Dottling Definitions 3.1–3.3 and Lemmas 3.4–3.5](https://eprint.iacr.org/2020/1185.pdf), printed pages 10–13, were checked in the primary PDF after reading the saved text. Lemma 3.5 uses subset sums of at least log|G|+n log q+omega(log lambda) seeds; its conditional noise law is determined by the seed errors and its bound grows to kB. Lemma 3.4 explicitly uses a fresh-sample oracle. These interfaces do not establish the frozen fixed-sample iid-Gaussian decisional premise. Their full generality and validation subtleties are outside this review.

## Material objection and exact dispositions

**C03-O01:** NC1 v1's literal ledger sentence lacks delta<1. HC1 gives TV=0 with a negative stated upper bound. Its detailed F02/D03 proofs already include the missing hypothesis. Full footprint and proposed repair are preserved in [objections.md](objections.md). The exact frozen direct dependents are AN v1, CHAR v1 and MN v1; the recorded transitive closure also includes A0 v2 and M0 v2. CHAR itself is outside this audit. The correction separately adds the missing instantiated AN dependency to S0. The separately frozen NC1 v2 uses trivial TV<=1 outside delta<1 and kappa(beta)<1. I independently checked all branches and accept that repair. A2/MN meet both guards eventually, so their numerical applications remain unchanged. No other material mathematical objection was found in this scope.

Here ACCEPT means the displayed bounded mathematical statement passed this critic's stated checks; it is not a global formal certificate. ACCEPT_CONDITIONAL identifies a surviving implication or application with named dependencies. DEFER is not an attack or an impossibility result.

| Exact claim/version | Disposition | Scope and remaining dependency |
|---|---|---|
| NC1 v1, literal review-v1 ledger sentence | **REJECT** | False without its omitted guard; detailed guarded F02/D03 theorem survives. |
| NC1 v2, separately hashed correction | **ACCEPT** | Piecewise finite theorem closes C03-O01, including rectangular dimensions and H_seq. |
| NO1 v1 | **ACCEPT** | Exact independent-additive retained-variable setting; conditional iid G law and Markov loss required. |
| DEC v1 | **ACCEPT** | Finite controls and Renyi orientation checked; no broad asymptotic impossibility inferred. |
| KM v1 | **ACCEPT_CONDITIONAL** | Correct finite hybrid under its explicitly stated full joint statistical premises; no hardness premise needed for the inequality itself. |
| MN v1 | **ACCEPT_CONDITIONAL** | Its concrete noise/sampler assertion survives; reconcile its formal dependency to accepted NC1 v2. Prescribed polynomial m and the modulus constraint remain. |
| LEAK v1 | **ACCEPT** | Includes correct A2 threshold, A1 exclusion, wrapping costs and exposed-variable scope. |
| REC v1 | **ACCEPT** | Both finite budget formulas and baseline negligible losses checked. |
| AN v1, sampler/noise portion | **ACCEPT_CONDITIONAL** | A2 construction and approximation are sufficient; update NC1 dependency. Overall AN additionally needs X1 and PR1, not audited here. |
| B0 v1, implementation/recovery interfaces | **ACCEPT_CONDITIONAL** | Accounting and conditional mapping checked; instantiated noise/extraction remain separate obligations. |
| M0 v2 | **ACCEPT_CONDITIONAL** | Valid assessment of what this run proves, with corrected MN dependency and separate unsupported Pm. Not a universal impossibility of sample expansion. |
| S0 v2 | **ACCEPT_CONDITIONAL** | One-sample conditional decision implies same-budget exact recovery. Instantiation needs AN as made explicit in the proposed dependency correction. |
| P0 v2 and Pm v1, hardness assertions | **DEFER** | No computational support established by any check here. |

The correction's proposed AN v2 and MN v2 applications have **unchanged noise/sampler dispositions after NC1 v2**. Its CHAR propagation is outside C03's assigned claim audit. The correction's explicit AN dependency for S0 is appropriate; C03 does not accept an instantiated hardness statement without that dependency and the source premise.

## What may safely appear in the final report

The final report may state a guarded discrete completion theorem with an explicit polynomial approximation, the exact conditional one-sample and new common-K hybrids, the square-root-m width cost and modulus restriction, the separate-Y leakage obstruction, and same-budget exact planted-recovery consequences under a corresponding decision premise. It may report that these sampler/noise/task interfaces are analytically compatible at A2, conditional on the separate extraction and prime checks.

It must retain H_seq as the exact source law, its independence from the bridge G, the distinction between retained noise and extraction tuples, both source-advantage terms, approximation charges, the prescribed sample budget, and separate P0/Pm assumptions. It must preserve the rejected NC1 v1 wording and identify the guarded correction. It cannot claim source hardness, practical security parameters, a tensor-product extension, an unchanged-width polynomial-sample theorem, an attack from hidden auxiliary leakage, or planted-witness identification from verification alone. Failed attacks and these successful analytic checks do not establish hardness or novelty.

Remaining limits: no sampler was executed; no CPU experiment was run; X1's analytic extraction theorem, PR1's prime theorem, source attacks and CHAR were not independently certified by C03. The mathematical claims above were checked by derivation and explicit controls, with primary imports limited to the stated interfaces. Artifacts and the correction hash were checked before completion at 2026-09-06 15:53 UTC. The review ends here with no continuation requested.
