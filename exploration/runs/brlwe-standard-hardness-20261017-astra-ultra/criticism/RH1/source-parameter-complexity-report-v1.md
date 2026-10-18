# RH1 source, parameter and complexity review

Independent NONAUTHOR recommendation: main H-ALIGN v1 and the mathematical shifted-coset/relation statements are supported within their explicit scopes. Parameter-v2 lower bounds are supported; its isolated upper-width implication is rejected and preserved. The separately authorized parameter-v3 repair is supported in parameter-v3-recheck-v1.md. No acceptance authority is exercised.

## Primary LLL source

Independently opened the [CWI March 1982 LLL preprint](https://ir.cwi.nl/pub/9304/9304D.pdf), 36 PDF pages. Printed pp. 3–5, equations (1.4)–(1.5), Proposition 1.6 and equation (1.9), give size reduction \(1/2\), Lovász parameter \(3/4\), and first-vector bound \(2^{(m-1)/4}\det(L)^{1/m}\) in ordinary Euclidean norm. Printed pp. 11–12, Proposition 1.26, gives polynomial arithmetic and bit bounds for integral bases. The PDF text is readable at those locations. This source supplies a worst-case guarantee and polynomial algorithm, not success on random modular relations. The companion's independent Gram–Schmidt derivation matches the source's ordinary-norm exponent; it does not confuse it with a squared-norm approximation ratio.

No anonymous secondary source, experimental LLL heuristic, SIS assumption, or exact-real computational primitive is imported. The main all-width estimate is established by its supplied elementary proof, not attributed to a paper with unspecified constants.

## Norms and actual width substitution

C8 means exactly theorem-v8 / algorithm-v2 / proof-v9, with hashes recorded in H's companion and in the RH1 input record. Its lower bound is \(v_0\ge2\sqrt n\,a\), with its actual certified Up-defined \(a\), and its canonical radius is \(d_0=\delta w_C/(32nkv_0)\). The finite quantum interface supplies coefficient width \(s_J=nq/(\sqrt2d_0)\), while \(w_C=\sqrt n\,w_B\). Direct substitution gives
\[
 s_J=16\sqrt2\,n^{3/2}kv_0q/(\delta w_B)
 \ge32\sqrt2\,n^2kaq/(\delta w_B).
\]
This confirms (W1), with no coefficient/canonical factor omitted.

A's permitted parameter file gives \(w_B=\ell^2\), \(\sigma=8n^2\lceil\sqrt{kn}\rceil\ell^4\), and supplied \(q\ge n^c\sigma\), \(c>0\). Its role here is just that width window; its older expected-time bridge discussion is not substituted for the current bounded bridge. This yields exactly (W3) and \(s_J/(512n^2)>1\), with a very loose minimum factor \(16\sqrt2\). Increasing \(v_0\) or \(q\) only strengthens that **lower** width bound.

The norm convention is central. H's \(s\) is the final coefficient width, not B's source width, A's target-noise width, or a smoothing ratio. The principal all-width estimate depends on that absolute \(s\).

## Upper width, modulus magnitude, and repaired scope

Parameter-v2 incorrectly treated polynomial-time scalar evaluation as enough for polynomial numerical output width. The saved family \(v'_0=2^nv_0\), \(d'_0=2^{-n}d_0\) preserves the C8 prerequisites with only \(O(n)\) additional bits but multiplies \(s_J\) by \(2^n\). The rejection is limited to that inference. It does not affect (W1)–(W3), H-ALIGN, or short-relation-v2's explicitly conditional assumption that \(s\) is polynomial in \(n\).

Parameter-v3 now states the additional magnitude premise and separately supplies a sufficient polynomial-value \(\kappa,\chi\) schedule with \(v_0=2\sqrt n\,\chi\), \(\chi\ge a\). That repair is supported; it is not silently applied back to v2.

Polynomial bit length of \(q\) does not imply polynomial absolute \(s_J\). A factorial-prime existence argument, where used in the permitted background, supplies only polynomial bit length and no efficient factoring/search algorithm. H's width discussion retains the separate polynomial-value premise. All statements concern supplied parameters: changing a modulus for a new input ideal requires a recovery premise for that selected modulus in any upstream composition.

## Deterministic relation algorithm and bit model

The relation matrix contains actual coefficient samples. The quotient map into \(R/I\) is determined from an ordinary basis. HNF/SNF on the integral congruence system computes the full relation lattice without factoring \(M\). Its determinant is \(h_A=|\operatorname{im}|\le M\), exactly. If the residue field is \(\mathbb F_{p^f}\), then \(h_A=p^r\), where \(r\) is the actual residue-column rank over \(\mathbb F_p\).

LLL runs on this full-rank integral lattice. Its input coefficients and output arithmetic have polynomial bit complexity in the ordinary ideal basis, sample encodings, and \(\log M\); no numerical \(M\)-sized enumeration is required. The finite relation test is classical. H supplies no new coherent or quantum procedure; the DGS oracle is a separate conditional input interface.

Under an exact infinite Gaussian oracle, returned integer vectors have no deterministic bounded support. Accordingly the stated postprocessing complexity is polynomial in their actual encodings, and the procedure is explicitly finite apart from that oracle. A bounded end-to-end implementation additionally uses the upstream finite sampler/output bounds or a separately charged tail truncation. H does not prove an exact finite-machine Gaussian sampler or a polynomial rare-event retry mechanism.

Given a nonzero finite-bit \(X\), inverse ideals, ordinary products, membership, and least scalar clearing can be implemented by polynomial-bit rational lattice arithmetic. The valuation proof of the denominator identity does not require an executable prime-ideal factorization. In particular, the least integer \(d\) can be obtained from denominators of an ordinary rational basis of the fractional ideal.

## Full probability and resource ledger

| Object | Full-law statement / cost |
|---|---|
| One original exact alignment | \([\rho_s(FI)-1]/\rho_s(F)\le B\) |
| One approximate conditional draw | event mass at most \(\min(1,B+\epsilon)\) |
| \(T\) adaptive active draws | expected sum of the actual predictable bounds; all attempts paid |
| Zero-conditioned exact draw | denominator \(\rho_s(F)-1\); geometric cost explicitly separate |
| Selected pair differences | at most \(\binom m2\max_a\pi(a)\); equal-vector output excluded |
| Rank screening, \(m\le n\) | original failure at most \(4m\sqrt n/s\) |
| Sample norm screening | original failure at most \(2mn e^{-\pi L^2}\) |
| Relation successful branch | \(0\ne Y\in FI\), norm certificate (R8)–(R9) |
| Implemented source transcript | conditional per-draw errors sum; FAIL remains in the output law |
| Analytic uniform-residue comparator | exact conditional lifts, not a promised efficient sampler |
| Optional source/comparator smoothing | TV at most \(\min(1,m\epsilon_K)\) under its stated threshold |

The relation algorithm takes \(m\) original samples and one lattice reduction. Zero/rank/tail failures are retained and their original probabilities add. Conditioning on relation success requires its actual success normalizer; no quoted TV or tail bound survives such conditioning unchanged.

## Approximation factor versus encoded input size

V2's corrected target is a polynomial-in-\(n\) approximation factor with polynomial runtime in the full encoded input. Under \(h_A=M\), the available determinant certificate has factor
\[
 g_m=2^{(m-1)/4}M^{1/m-1/n}.
\]
Its \(\exp(\Omega(\sqrt n))\) lower bound at \(M>2^{\rho n}\) rules out a polynomial-in-\(n\) value for this **certificate**. It does not rule out a polynomial-in-\((n,\log M)\) value for arbitrary huge \(\log M\), as the retained \(m=n,\log_2M\ge2^n\) example shows. The additional \(\log M\le n^C\) regime correctly restores the encoded-size superpolynomial conclusion. None of these calculations is a lower bound on actual LLL output or on the optimal relation.

The determinant-one all-zero residue case and intermediate residue ranks are retained. For degree-one primes, \(h_A=M\) outside the explicitly computed all-zero event; for higher residue degree the packet asserts no unproved adverse rank distribution. The independent \(\mathbb F_9\) control confirms why this distinction matters.

The main theorem and all companions leave the arbitrary-ideal standard-family connection open. They neither assume that the restricted sampler is unconditionally available nor exclude a different class-transfer or correlated short-image algorithm.
