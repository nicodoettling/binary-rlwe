# Ideal-ring-SIS v1 adversarial full-proof review

2026-10-17T21:20:26Z tool clock at final pass. PROVISIONAL nonblind review; no acceptance authority. No experiment. Frozen statement SHA2563c2215998c6e836936badea6bfa2d79011e3d2cbc8abb7ad4eea66b84e468b08 and proof SHA256728fe625ad3ae134d798342e9045b82b4e73beca9c1d7ff06839f8b73867ed05 match newly computed hashes. Both files were read in full. The exact ring-extraction dependency and repaired elliptical sampler were also read; see RF2/b-elliptical-v2-recheck-v1.md.

## Disposition

No defect found in the natural-inclusion algebra, full public-law comparison, rank-posterior treatment, adaptive nonzero proof or simultaneous operator-norm bound. Recommend this ONE-VECTOR restricted-ideal-to-ring-SIS construction for a fresh independent review, with the explicitly stated Gaussian/preimage implementation dependencies retained. This is not a standard worst-case hardness theorem, a binary-secret conversion, or a proof that the resulting absolute output radius is nontrivial on any chosen input family. The source/parameter instantiation must be audited separately.

## 1. Exact natural inclusion and residual encoding

Coprimality gcd([R:J],q)=1 gives J intersect qR=qJ, hence the natural map J/qJ to R/qR is bijective. This is stronger and more appropriate than an arbitrary basis-coordinate identification: multiplication by ring masks keeps J/q stable, and qQx in J intersect qR implies Qx in J. No field structure modulo q is needed for this lift.

To encode u, choose integer ztilde with B ztilde=u modq and x=B ztilde/q. Then qx=u modq. Rounding x to u' leaves error at most sqrt(n)/2. Quotient encoding gives u'-sum g_l z3_l in J. Since each b'_l is in J/q, rcorr is in J/q and q rcorr+C z3=u modq. The subsequent integer z1 and signed binary z2 exactly account for the remaining carry:

    q B^-1 rcorr = K z1+G z2,
    BK z1+BG z2+C z3 = u modq.

Entrywise K rounding gives ||DeltaK||op<=n/2 and the displayed Zrem bound. The nearest-plane distance bound follows from at most half the Gram-Schmidt parallelepiped diagonal and is bounded by sqrt(n)||B||op/(2q). None of the quotient bits is asserted uniform or additive; the residual columns are indispensable.

For gadget target2^j, z0=-R1z1-R2z2-Sz3 cancels the mask contribution exactly. Because the other entries are INTEGER CONSTANTS in the ring, each coefficient of z0 is at most ||z1||1+b+k<=sqrt(n)Z1+b+k. No hidden negacyclic-convolution factor is missing in this particular bound. Multiplication by X^a merely permutes/signs coefficients, so the expanded trapdoor has the same maximum entry bound.

## 2. Public law and both response endpoints

The initial Gaussian residue law on(J/q)/J is uniform over its q^n cosets reweighted by rho_sigma(c+J), with its ACTUAL expectation as denominator. The h-sample replacement costs h epsilon/(1-epsilon); it is not an exact convolution assertion.

For uniform A0 and independent coefficient-sign columns, the exact CRT-support collision formula bounds the retained-key distance by gamma_hash. Conditional on A0 the t+k mask columns are independent. A product hybrid followed by expectation costs(t+k)gamma_hash. It never substitutes the product of average collision probabilities for the conditional law. Fixed residual offsets preserve the bound.

The uniform rank failure is at most n q^-m. Real rank success is at least alpha, and conditioning both complete public laws on the SAME rank event costs at most2delta_pub/alpha. In the ideal law, the event involves only A, preserving independence of W. In the real law, every latent is retained under its actual posterior. First success among independently redrawn attempts has this conditional law; the all-fail event costs(1-alpha)^a. Failed rows are not reused.

Canonical preimage replacement holds per fixed complete private state. After this replacement, the public hint depends only on A,W and the declared width/targets, so it may be appended as a common channel to the public-law comparison. Private B,V,masks,Q and the construction trapdoor are discarded from the solver's view. Revealing them would be a different joint law.

The fixed independent Secret and error laws are appended only afterward, giving each full planted and uniform-response endpoint the same Delta bound. This preserves any already supplied secret law; it supplies no reduction from uniform secrets to bits. The comparator response is exactly uniform in the real construction conditional on its public key, while the complete public-key distribution is only approximately the target law. Those two statements are kept distinct.

## 3. Nonzero proof under adaptive solver output

Let c=x0+R1x1+R2x2. When x1=x2=0 and x is valid, c=x0 is nonzero. Otherwise choose any mask column whose associated solver coefficient is nonzero. Fix A0, S, all other mask columns, and canonical-hint/solver random tapes BEFORE rank conditioning. The remaining column affects the public key, rank event and output only through one Rq-valued hash, with at most q^n values. For each hash the output is fixed. Since R embeds into a characteristic-zero NUMBER FIELD, multiplication by its nonzero coefficient is injective and c=0 determines at most one entire sign column in R^h. Each such column has probability2^(-nh). Union over t columns and divide by the rank-success lower bound, obtaining t q^n 2^(-nh)/alpha.

This argument does not assume the hidden column remains uniform after conditioning on its hash. It counts possible columns before that conditioning. Mod-q zero divisors do not contradict the characteristic-zero injectivity used in the count.

When c!=0, its first nonzero index is determined by A0, the masks and the solver's public transcript. Conditional on those quantities and all other V columns, the remaining v_i has exactlyD_(v0+J,sigma), because the residue fiber from A0_i is one coset of J. Rank and the canonical hint reveal no further within-fiber information. The equationQx=0 is affine in v_i with a nonzero field coefficient, so at most one point can satisfy it.

Partitioning this coset into2^n cosets modulo2J and using sigma/2 at smoothing bounds each atom by2^-n(1+epsilon)/(1-epsilon). This proves the second nonzero loss without a union over potentially many solver outputs or a false posterior-independence step.

## 4. Simultaneous norm and implementation accounting

For the CENTERED lattice Gaussian on J/q, the exponential moment follows from shifted theta mass being at most centered mass. The coefficient tail2exp(-pi ell^2) is valid without a random-lattice assumption. Union over hn coordinates and conditioning on rank costs beta_tail.

On this event, the ring row V has coefficient-expanded operator norm at most sigma n sqrt(h)ell. The combined sign-mask matrix has Frobenius norm n sqrt(ht), so[I|R1|R2] has operator norm at most sqrt(1+n^2ht). The deterministic ring-row contribution is at mostsqrt(n)||[BK|BG]||F/q. Hence H bounds the FULL map Q on every possible adaptive x, with no omitted cross-block terms.

Validity, nonzero and norm are one event. Passing from exact canonical accepted construction to the implemented construction therefore charges delta_impl only once. Initial Gaussian errors are summed over all ah attempted draws, not only accepted draws. The final output is checked for exact membership, nonzeroness and norm.

The ordinary-basis initial Gaussian implementation uses Vcoord=sigma^2 M^-1 M^-T for M=B/q, which is the correct inverse quadratic form. Its stated floor makes Vcoord>=2a0^2I, permitting the repaired public-integer elliptical sampler. This does not pretend to sample at smoothing from an arbitrary basis. Complete rational encoding lengths and expected runtime are explicit. Numerical preimage error delta_pre remains a separately supplied implementation charge under the imported sampler, not an unproved zero.

## 5. Primary SamplePre dependency

Independently read [WWW25 author full version](https://www.cs.utexas.edu/~dwu4/papers/MultiPreimage.pdf), Theorem3.9 and its definitions on printed pages10 and12, plus supplied2026/2443 Lemma3.6. The source uses maximum-entry matrix norm, accepts every supplied valid gadget trapdoor, requires coefficient dimension N>=3n ceil(logq), and gives error2^-n at widthN||T||logn. Here N=n(m+k) and h>=3ceil(logq) meet that dimension condition. No random-matrix hypothesis is required for this sampler. Padding the trapdoor with zero columns matches its padded gadget convention.

The source defines its canonical preimage through an INTEGER discrete Gaussian conditioned on the modular equation, although the later sampler syntax writes Z_q. The reviewed construction uses the explicitly stated retained-integer convention of2026/2443; reducing a canonical integer hint and substituting arbitrary representatives would not preserve its declared law. This audit verifies the primary formulation and hypotheses; it does not rederive the underlying MP12 implementation. A numerical implementation must preserve this convention and charge its stated delta_pre.

## 6. Claim-specific regression controls

| Control | Disposition |
|---|---|
| CP1, R18, C03-HC6 | Conditional rank posteriors are retained; no success/bad-event product or sequential marginal multiplication. |
| N03-SCAL-POSTERIOR | Gaussian residue reweighting uses its actual normalizer; hidden sign counting occurs before hash conditioning. |
| EX-PUBLIC-TAPE, D-THETA-RETAIN-U | Public solver sees only A,W,T; the discarded construction tape is not included in the uniform endpoint. |
| EX-RETAINED-M3, B-JL-REDRAW-T | Shared public key and rank event stay fixed; fresh attempts redraw every latent and do not reuse failed rows. |
| EX-M3-CROSSBLOCK, RECT-ALG-1 | Operator H controls the entire stacked map, including all mask cross-blocks. |
| N02-DUAL-NUMBER, R14 | Natural inclusion uses gcd(D,q)=1; zero/nonunit residues remain allowed. Characteristic-zero injectivity is distinguished from mod-q zero divisors. |
| D-LSW-THETA-1 | No exact Gaussian convolution is imported; initial residue and finite sampler normalizers are charged. |
| C-TOWER-RELATION, A-TOWER-LAW | No radix map is asserted multiplicative; all residual columns are explicitly retained in a fixed ring. |
| R03, PAIRWISE-SE-F3 | Full same-key product conditionals are proved; response secret and error are sampled jointly independently of construction. |
| UNIFORM-APPROX-COLLAPSE | Exact conditional response comparator is distinguished from approximate full public-key endpoint. |
| SOURCE-SMALL-D, C01-ATT, R16 | No restricted-family security or standard hardness is inferred from this construction. |
| A-PPT-LEDGER-SCOPE | Full input encodings, ordinary-basis sampling floor and explicit preimage primitive are retained. |

No counterexample was found in this pass. This verdict is scoped to the stated conditional theorem; it must not certify an unreviewed ring Fourier/search reduction or the low-index standard-hardness edge.
