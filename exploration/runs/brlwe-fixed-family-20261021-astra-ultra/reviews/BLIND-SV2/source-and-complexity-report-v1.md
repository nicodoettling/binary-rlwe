# BLIND-SV2 source and bit-complexity audit

## Primary source access

Only the two permitted primary-source families were opened. No author proof or other review was used.

1. James S. Milne, *Algebraic Number Theory*, version 3.08, July 19, 2020, [full PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf). The browser provided the full document and the relevant theorem/proof text. Proposition 6.2 is at printed pages 96–98; Theorem 3.34 and its Galois transitivity proof are at printed pages 59–60; decomposition/inertia material, including Proposition 8.10 and Remark 8.12, is at printed pages 139–140. PDF page indices are one greater than printed pages. These supply the cyclotomic integer-ring/ramification facts and standard prime-decomposition facts. Ideal descent, contraction, norm identities and order-tower estimates were reconstructed in the independent report.
2. Ravindran Kannan and Achim Bachem, *Polynomial Algorithms for Computing the Smith and Hermite Normal Forms of an Integer Matrix*, SIAM J. Comput. 8(4), 499–507 (1979), [publisher page](https://epubs.siam.org/doi/abs/10.1137/0208040?journalCode=smjcat), DOI 10.1137/0208040. The publisher abstract explicitly establishes polynomial counts of operations and intermediate binary digits, including transformation matrices. **Full text was unavailable in this review.** The SIAM PDF URL redirected to the abstract. Both `https://people.tamu.edu/~rojas/kannanbachemhermitesmith79.pdf` and its HTTP variant returned 404; the `www.math.tamu.edu` variant also returned 404. A search index displayed an extract of the original paper, but that is not described here as having obtained the full paper.

The imported complexity theorem is used at its stated exact integer HNF interface. The review does not audit Kannan–Bachem's internal algorithm or assert a more specific running-time exponent. An authoritative abstract confirms the needed polynomial bound, but full-proof access remains explicitly unverified.

The initial broad search for the permitted paper returned snippets or bibliographic hits for other works. A publisher page also included a citing-article list. Those incidental snippets were neither opened as sources nor used. `primary-source-exposure-v1.json` preserves a later exact browser response containing the relevant allowed-source excerpts. `intake-exposure-seal-v1.json` records the initial file exposures and this search limitation.

## A square, nonsingular HNF interface suffices

It is unnecessary to assume a rectangular/rank-deficient extension of a quoted normal-form result. Suppose `A` is an invertible `n` by `n` integer basis and `B` is an `n` by `g` integer matrix of additional generators. Form the invertible square matrix

```
C = [ A  B ]
    [ 0  I_g ].
```

Compute its lower-triangular column HNF by the imported polynomial algorithm. Projection of its lattice to the first `n` coordinates is `A Z^n + B Z^g`. Because the HNF is lower triangular, the final `g` columns have zero first `n` coordinates, and the first `n` projected columns form a nonsingular basis of that image. Thus one square HNF of dimension at most `2n` computes every full-rank lattice sum used in the proof. Different row/column or upper/lower HNF conventions can be handled by transpose and coordinate reversal, which are exact polynomial-time operations.

This construction covers both `J+mR` and `J_o+L` for a fixed lattice or displayed subfield. No kernel-basis complexity assumption is needed. In particular

`d_L = [L:L intersect J_o] = |det A_o| / |det basis(J_o+L)|`

is an exact positive integer computed from ordinary integer bases.

## Accounting for all remaining operations

Let `L` bound the bit length of an original matrix entry. Hadamard bounds on determinants and minors show that the entries of an inverse matrix have numerator and denominator lengths `O(n(L+log n))` before reduction. Fraction-free rational elimination and gcd/lcm arithmetic therefore have polynomial bit cost. The lcm used for the exponent divides `D`; it has no more than `log2 D+1` bits, even if the input basis is badly skewed. Extracting its largest power of 2 is a binary operation and does not factor its odd part.

The `n` automorphisms are explicitly enumerable signed permutation matrices. Testing whether `A_o^-1 S_u A_o` is integral costs polynomially many exact rational operations. Its determinant has absolute value 1; hence an integral test result is sufficient for ideal equality. Signed connected components involve at most `n` vertices and `n|H|` signed edges. The basis vectors have coefficients 0 and plus/minus 1, so their representations are small. This is actual acquisition of the required invariant basis, with all signs retained.

Subfield inclusion matrices consist of standard coordinate columns. All `log2 n` contraction indices are computed before minimization. This precomputation is polynomial in `n` and the complete basis encoding, even if their values are exponential. There is no factorization, finite-field construction, unknown subfield representation, or uncharged short-vector oracle in this precomputation.

For an index `d`, collision enumeration uses `d+1` vectors. Their exact quotient keys have polynomial bit length in `n`, the ordinary basis encoding, and the vector encoding. Deterministic sorting costs polynomial time in the **value** `d`, and storing the vectors/keys costs polynomial space in that value. Even a quadratic comparison loop suffices for the stated theorem. The arguments never infer polynomial runtime from polynomial `log d`.

The resulting multiplier has coefficients in `{0,+1,-1}` or `{0,+2,-2}`. Negacyclic multiplication is exact integer/rational convolution. Rounding is rational integer division implementing the displayed half-up rule. Division by a nonzero multiplier is inversion of a nonsingular `n` by `n` rational multiplication matrix. Its determinant/minor bit lengths are polynomial by the same bounds. The target and output lengths are explicitly charged, so large coordinates of the promised inverse-ideal member do not invalidate the accounting.

The universal algorithm need not know the family constants `rho,t,C`. Under a promised family bound on its computed numeric index, the same universal numeric-index runtime becomes polynomial in `n` and the entire input encoding. If the basis encoding is itself superpolynomial in `n`, no polynomial-in-`n`-alone conclusion is asserted.

## What the finite program checks

The program is a small exact regression harness, not the production decoder and not an implementation of Kannan–Bachem. It checks signed actions, image ranks over explicitly small prime fields, exact rational matrix exponents, and one full collision/rounding/division path. Split root ideals use the distinct roots of `X^n+1` at the explicit primes 5, 17, 97, 257. Their primality is elementary. For the three nonsplit controls at `p=3`, the two displayed degree-`n/2` factors multiply to `X^n+1`; the residue order `ord_(2n)(3)=n/2` shows each factor is irreducible. Prime powers use a verified lifted simple root modulo `97^2`, so the evaluation kernel is the stated unramified prime square.

The large-index stress cases compute contraction images only; the harness does not enumerate their exponential number of candidates. The sole collision enumeration is bounded by 9410 vectors. Every assertion is exact. Timing floats are used solely for resource reporting. The recorded exit status is 0; stdout is complete, stderr empty, and peak RSS is preserved in the external resource log.

No source hardness statement, prime-construction claim, probabilistic composition theorem, or ordinary-basis acquisition procedure for an external reduction was imported or certified.
