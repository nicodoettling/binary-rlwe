# DD2 review of AM-MAIN-v2: source law and complexity

Review completed 2026-10-21, after rereading both complete v2 files at 12:56 UTC. Verdict: **favorable crosscheck, no critical defect found; NOT ACCEPT**. DD2 did not author the main composition or DD1 extractor, but did author the strengthened AM1, prime-list construction and optional parameter witness. This report is neither an independent review of those DD2 components nor a fresh blind review. The whole theorem still needs the prescribed external gates.

## Frozen objects

All paths below are relative to this run unless prefixed OLD, meaning `exploration/runs/brlwe-standard-hardness-20261017-astra-ultra`.

| Object | SHA256 |
|---|---|
| `coordinator/am-main-theorem-v2.md` | `bac9219db980fa85f0a29a6cc9957a9f57eb8281b3bdfff595b2f327bb2ba34d` |
| `coordinator/am-main-proof-v2.md` | `dee6af4bb9255a73ed85cf448251470986252ba7b1e71fcbf8b36fa004ac7edd` |
| `workers/DD1/extraction-theorem-v1.md` | `c8ad79f0f681e346e149749d46c3bb98ff5e2e6a2ef5cbc406a47f8c2abf0e38` |
| `workers/DD1/extraction-proof-v1.md` | `4a599d9eed5dfefca4b3d0bbcd1402aaba2e709310e7eaa62feb36d5b6b3f357` |
| `workers/DD2/am1-strengthened-theorem-v1.md` | `3500de1a74555ecbf8102d4fb52a87f6a0d87c7f9cdcca22e849f7a2812d870d` |
| `workers/DD2/am1-strengthened-proof-v1.md` | `d1d22c6a34776a493b7d43611abb076c8e97f07542ad48da33d5072683766e43` |
| `workers/DD2/prime-list-theorem-proof-v1.md` | `c54f0a6e37aa6ed6a13bb9cf387f98ce99fb12311a517c6fec32e3e32188d6cf` |
| `workers/DD2/parameter-witness-v1.md` | `792ec5df84dbd8dc2c8a00ac7e20441091b0eefa0a7936ece77b408baa2b88d6` |

The inherited interface sheet is `OLD/workers/RF4/same-j-composition/interface-statements-v1.md`. Its mathematical statements and the exact A-FRAC proof, B-GP-v2 interface and C8 theorem-v8/algorithm-v2/proof-v9 were checked. `OLD/coordinator/samej-acceptance-v1.md` certifies those inherited versions, not the new selected-functional composition. Main v2 explicitly binds them without promoting changed premises to old acceptance.

## Target, extraction and averaging

The target has one uniform binary S shared by all k0 samples, iid uniform A, iid coefficient integer Gaussian errors, and fresh code coins for every invocation. The q law is the fixed master list Q0, independent of J; any J metadata has the same law in both worlds, and the advantage premise is pointwise in the supplied J. There is no invocation of a uniform-multiplier distinguisher promise on a fractional source.

The master-list signed average advantage implies the average of absolute per-q gaps. Retaining M of M+n entries deletes exactly n entries in total, including the fewer than n possible divisors of D. The lost absolute-gap mass is at most n. M>=2n/epsilon0 therefore gives final average absolute gap at least epsilon=epsilon0/2. This does not infer average advantage from one fixed-q promise.

The extractor has disjoint calibration and test banks. Conditioning on a fixed S and then the calibration transcript preserves the iid test-bank law. Its selected root is determined before that bank is inspected. Reuse across candidate values requires a union bound over finitely many tests, not independence of their outputs. Wrong-root masks retain the complete coefficient error vector; they never replace correlated CRT errors by independently sampled CRT marginals. All field draws have pointwise first-failure cap bounds. The lower bound is at least epsilon/2-eta_ext-nu_ext=15epsilon/32.

The source bank size is K=k0(Ncal+Ntest), while the number of code calls is (n+1)Ncal+qNtest. Those are different quantities throughout v2. Whole-bank TV is charged before the bounded extractor kernel, hence only once per test. The cap cost nu_ext is paid in the uniform success lower bound; the fractional endpoint bounds any resulting capped predictor and needs no repeated cap penalty.

## Fractional source and selected-functional bound

At the analytic fractional endpoint the a_i are coefficient D_(J^-1,s), not uniform and not independently uniform CRT coordinates. The latent G is exact D_(J,t). On the good source event the stacked Kn-by-n multiplication matrix has operator norm at most s sqrt(Kn) ell. With t=2n^2 ell and s=sqrt(2)ell^2,

    2 t s sqrt(Kn) ell = 4 sqrt(2)n^2 sqrt(Kn)ell^4 <= sigma.

The existential short basis bound gives tau_2<=n^2D^(1/n)<=2n^2; thus the inherited theta expression is bounded by the specified theta_A with exponent 3ell^2/4. These bases are not advice to the executable decoder. G and H are proof variables only. H is independent of S,G conditional on source state, and is integrated out before comparison with independent target errors. Revealing source state,H,Y=S+G for an upper bound retains the original conditional product law of S,G; revealing S itself would invalidate the bound and is not done.

For each fixed q, maximizing the full posterior success over selected pairs (j,v) gives the displayed exact sum over y and binary b. Both rho_t(J) and the wider theta normalizer are retained. Completing the square with r0=t gives the factor

    exp(pi n/(4t)) (1+1/t)^(n/2) <= exp((pi/8+1/4)/(n ell))=Gamma.

Only the common residue partition b modJ is averaged over q. For a nonzero binary difference f, split-prime multiplication nullity m_q equals the number of zero evaluations. Smith normal form implies q^m_q divides the nonzero determinant N(f); distinct q then give sum m_q log q <= log|N(f)| <= (n/2)log n. The diagonal within each fiber is counted once, not once per root. The resulting mean bound sqrt(D/2^n)+sqrt(mu), with mu=n log n/(2M log Qmin), has no missing factor n. Repeated primes or ramified root multiplicity would break this accounting; the theorem excludes both.

## GP bridge and exact v2 normalization

v2 now expressly uses coefficient G_(w/sqrt(n)). Since w=sqrt(n)ell^2, this is precisely coefficient width ell^2=w_B. The bridge adds coefficient width r_B=ell^2, producing s=sqrt(2)ell^2. This checks the repaired v1 notation against the inherited canonical/coordinate normalization. No continuous Gaussian is identified with coefficient discrete Gaussian: the public bridge supplies that conversion with the finite TV charges.

The planted bridge charge is Delta_B+Kn nu+eta_cap with Delta_B=2K eps_B/(1-eps_B)+2pi Kn/(P r_B)+Kn nu. The uniform charge is Kn nu+eta_cap. Thus their sum is exactly E_bridge, including three Kn nu terms and two cap terms. Both endpoints retain S, all K samples and metadata. Combining the uniform lower bound and the fractional upper bound gives 15epsilon/32-epsilon/8=11epsilon/32. This is a full test gap, not a per-C8-call simulation loss.

The executable wrapper uses ordinary basis arithmetic, finite quotient/coordinate samplers, the known fresh binary S, and D_alg. It never samples D_J,t or D_J^-1,s as advice. The ideal Gaussian endpoint exists solely in the analysis. This removes the supplied-Gaussian-advice defect of DD2's earlier integral-cancellation attempt.

## Bounded decoding and verification

Qmax gives a common upper scale Smax; Qmin gives the common reconstruction guard. The good modulus q_* is fixed existentially after the oracle laws and parameters are fixed. It is not selected using an unavailable fractional-source experiment. Every one of the M schedules runs, and the inherited C8 procedure is bounded even for bad moduli, wrong orientations and off-promise transcripts.

For q_*, the input error is at most q_*r<=d0. Parseval gives coefficient ||e||_2<=r, so the true answer passes the outer exact rational squared-distance test. If x is a nonzero difference of two candidates in J^-1, xJ is a nonzero integral ideal, hence |N(x)|D>=1. AM-GM/Parseval gives ||x||_2>=D^(-1/n). The guard r<1/(4D^(1/n)) therefore prevents any false candidate from passing. Membership in J^-1 and r^2 are rationally checkable; no comparison of computed approximate embeddings is used by this outer verifier.

Final failure implies failure of the one fixed good-q execution. Its bound is p=(n/2)exp(-kappa)+zeta<=17zeta/16. No union bound in M is needed for failure, no product of marginal probabilities is taken, and no future event is conditioned upon. Runtime does multiply by M. C8's physical multiplier endpoint remains compared with a continuous proxy; its persistent rational characters are not asserted to become exactly Haar.

## Prime construction and resource circularity

The imported primary theorem is Xylouris, Acta Arithmetica150(2011), Theorem1.1: an effective absolute constant bounds the least prime in a reduced progression by C m^5.18. The weaker fixed exponent6 used in DD2-PRIMES-v1 follows after increasing C. The theorem statement was inspected in the [publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83078), DOI10.4064/aa150-1-4. This is an imported analytic-number-theory theorem, not an experimental density assumption.

The auxiliary modulus 2np and distinct reduced classes produce M+n distinct split primes >=Qmin with numerical values <=C[4n(M+n+t0+2)]^6. Exact progression enumeration and even trial division have polynomial runtime in that numerical bound. The master list is constructed before J filtering. Only gcd(q,D), not factorization of D, is needed. The finite main theorem can instead take this entire finite list as supplied input.

For fixed nonnegative INTEGER b,c, main v2 constructs the list from n,M,Qmin before defining K or sigma. It follows that log Qmax=O(log n), Ncal+Ntest=O(n^(2c+2)log n), K=O(n^(b+2c+2)log n), and sigma=O(n^((b+2c+7)/2)(log n)^(9/2)). The exponent b+2c+12 of Qmin exceeds that of n sigma by (b+2c+15)/2>0. Thus Qmin>=n sigma eventually; this is not circular selection of q after a q-dependent sampler cost. The square-root collision term is O(n^(-c-3/2)), while the fixed-rho entropy term and remaining tails are negligible versus epsilon. Main v2's integer-exponent clarification makes the chosen power inputs exactly representable.

The separate `parameter-witness-v1.md` freezes an optional large fixed B-power certification. It is not silently substituted for the main corollary. The finite theorem still requires its actual numerical G-AM guard; neither asymptotic eventuality nor polynomial bit length alone certifies a small finite instance.

Total D_alg calls are bounded by M Q_*[(n+1)Ncal+Qmax Ntest]; root/idempotent enumeration is charged in q in VALUE. All complete bit encodings, evaluation routines, cap lengths, sampler arithmetic and ordinary basis operations are charged. For fixed/inverse-polynomial zeta, kappa and Q_* are polynomial in n, chi=O(sqrt(log n)), and r^-1 is polynomial. This gives no practical claim from the large exponents or effective Linnik constant.

## Evidence and pending gates

`dd2-am-fv1-*` records preregistered exact finite controls: 6648 nonzero ternary differences in dimensions2,4,8; 16 split primes per dimension; exact determinant/root divisibility; 4736 independent modular-nullity checks; eight fiber settings; repeated-prime and ramified-multiplicity negative controls; three small auxiliary-list constructions. These are finite falsification checks, not proofs in arbitrary dimension. They completed exit0 in0.77s, peak RSS12288KiB under512MiB RLIMIT_AS and120s timeout. The separate earlier `dd2-fv1-*` controls also completed; no job remains.

`regressions-intake-v1.json` imports all164 old IDs with source hash and records DD2-scoped provisional applicability. It is not a whole-main reconciliation or acceptance record. Root still must finish the full-main dependency and regression audit and commission a complete nonauthor review and a fresh blind derivation of the exact final version, including independent review of DD2's own components. The restricted ideal family, averaged-modulus premise, classical-only executable interface, and missing unrestricted hardness foundation must remain explicit.
