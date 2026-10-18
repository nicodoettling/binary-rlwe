# Primary-literature compatibility ledger

2026-10-17T20:53Z. PROVISIONAL import audit, not a new hardness claim. Exact desired source/target and direct packing gap are in first-partial-v1.md. Source hardness remains OPEN.

## Actual binary module reductions

[Boudgoust–Jeudy–Roux-Langlois–Wen2021](https://cjeudy.github.io/assets/pub/BJRW21_Hardness_bin-MLWE.pdf), Definition1/Theorem2 and Section3.3, gives a decision reduction preserving field degree, modulus and sample count, increasing module rank from k to d at least (k+1)log2(q)+omega(log n). The target is binary in the dual coefficient basis with bounded elliptical continuous noise. Its power-of-two instantiation uses a restricted splitting regime. This is a structured reduction, but not the requested rank-one binary target. See the first partial for the error ratio.

[Jeudy2024 thesis, Chapter2](https://cjeudy.github.io/assets/pub/manuscript.pdf), Theorems2.1–2.2, contains the2023 journal extension *On the Hardness of Module Learning With Errors with Short Distributions*. Search rank satisfies d >= k log_(2eta+1)(q)+log_(2eta+1)(t' n); decision rank satisfies d >= (k+1)log_(2eta+1)(q)+omega(log_(2eta+1)n). Degree/modulus are preserved. Secret coefficients uniform in[-eta,eta] include ternary at eta=1, not the requested binary law. Decision retains number-theoretic and continuous-error restrictions; search allows monogenic rings and discrete errors. Neither theorem removes rank growth. Full splitting cannot simply be inserted into the decision theorem's restricted regularity hypotheses.

[Lin–Wang–Zhuang–Wang2024](https://pure.tudelft.nl/ws/portalfiles/portal/186654080/1-s2.0-S0304397524001683-main.pdf), Definition9, Lemma18: primal decision RLWE of degree n, modulus q, canonical discrete width beta implies search binary module-LWE of rank d>11log2(q), m>n, same degree/modulus, canonical continuous width alpha>6c sqrt(m) beta, dual secret S/n in power-of-two rings. Conservatively require m>=d, used by underlying Lemma11. This is the strongest direct binary-module search statement checked here, not a claim of exhaustive priority. Lemmas20–21 keep degree n, replace modulus q by q^d, and replace the secret tuple by sum_j q^j s_j. Theorem10's rank-one entropy requirement exceeds n log2(q), excluding n binary bits when q>2. Decision Theorem8 additionally requires enough entropy in every prime-ideal component. This audit checks these interfaces, not every proof in that paper.

## Our scaling and algebra checks

For power-of-two R_n, canonical norm is sqrt(n) times coefficient norm and R_n^dual=(1/n)R_n. Thus the2024 source width beta equals coefficient width tau=beta/sqrt(n). Multiplying its response by n converts S/n to coefficient-binary S and converts canonical continuous error alpha to coefficient continuous width sqrt(n)alpha > 6c n sqrt(m)tau. Definition9 uses responses modulo qR_n^dual, so this conversion multiplies by n, not nq. The target is still module rank d and still continuous. Any claim of the exact independent coefficient discrete Gaussian law requires an additional justified discretization step.

The gadget sum sum_j q^j S_j has nd binary choices but n coefficients in base q, degree n, and modulus q^d. It is not an element with nd independently binary coefficients in a degree-nd cyclotomic ring. In the true tower R_n[Y]/(Y^d-X), evaluation Y to q would send Y^d-X to -X modulo q^d. Since X is a unit, this is not a ring homomorphism. Relabeling digit coordinates does not preserve products or response equations. Also q^d is composite for d>1, whereas the original target requires a split odd prime.

For a fully split q, one prime-ideal component of a rank-d module secret has at most d log2(q) bits. Consequently a condition demanding at least n k log2(q+1) component entropy forces approximately d>=nk even before positive slack. This is a limitation of that published sufficient decision criterion, not a universal impossibility claim.

The2024 Lemma18 proof writes scaled-isometry and R^dual=R/n identities for cyclotomics generally. We only use the power-of-two case where both identities hold. Its use of Lemma11 also requires m>=d; choosing m accordingly is permitted. These caveats do not repair the rank-one target mismatch.

## Scalar LWE and orders

[BLPRS2013](https://arxiv.org/pdf/1306.0281), Theorem4.1, converts scalar LWE dimension k to binary dimension roughly(k+1)log2(q), same modulus/sample count with noise growth. Its public matrix is uniformly unstructured. [Micciancio2018](https://theoryofcomputing.org/articles/v014a013/v014a013.pdf), Corollary3.4, improves a scalar binary-secret reduction and explicitly leaves structured extensions for future work. Neither statement asserts preservation of a ring multiplication matrix. Their existence cannot justify applying an ordinary LWE oracle to the correlated coefficient expansion of RLWE.

[BBPS2019](https://iacr.org/archive/asiacrypt2019/119210284/119210284.pdf), Theorem5.1, changes orders while preserving the chosen secret distribution and combining errors. Corollary5.2 yields a uniform suborder-coset secret from Order-LWE under its order hypotheses; it does not turn uniform q-valued coefficients into iid bits. The small-norm-secret application in Section7 uses an additional assumption. The standard ideal-offset route has already been separately frozen and reviewed in workers/D/ideal-theta-proof-v1.md; it is not reopened by this ledger.

## Outcome

No inspected theorem supplies the original rank-one, full-uniform-multiplier, iid coefficient-binary secret and iid discrete error law. This is a precise gap among checked transformations, not evidence that no future reduction exists and not evidence of security. A controls the independent direct-radix response-programming audit. No experiment was run for this ledger.
