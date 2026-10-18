# D-SREL-SUBFIELD-1: growing hidden subfield generators remain easy

Provisional exact family/control, not a general sparse-generator attack. No experiment.

Let n and r be powers of two with r|n and r<=C log n. Embed R_r=Z[Z]/(Z^r+1) into R_n by Z=X^(n/r). Let nu be ANY specified distribution on nonzero coefficient-ternary f in R_r, possibly with norm or weight restrictions, and set J= iota(f) R_n. Publish only HNF(J), not f. Require a distinct odd source prime q coprime to N(J). The two experiments use the identical f,J law:

  planted: a_i|f iid D_(J^-1,s), A_i=pi_q(a_i);
  comparator: A_i|f iid U((R_n)_q).

The reduction may know its sampled f; the oracle need not. Spherical fractional Gaussian depends only on J, so different generators of the same J do not alter this conditional planted law.

Even though r grows and f is hidden, this family is polynomial-time distinguishable when s sqrt(r) sqrt(log n)=o(q). Enumerate the at most3^r-1 nonzero ternary elements of the PUBLIC r-dimensional subfield, embed them, and test membership in J by HNF. At least iota(f) passes. The first passing v is a deterministic function of J; it has weight<=r. Apply D-SREL-ATTACK-1's one-coefficient test with U=sqrt(c log n), obtaining advantage1-o(1), with exact scalar-uniform comparator. Runtime3^r poly(n,input bits)=n^O(1). This does not require identifying the particular sampled f or proving that v generates J.

The conclusion persists if the family hides a monomial translate of the subfield support: try all n translates, still polynomial. Multiplying a sampled generator by an arbitrary unit changes its representation but not its ideal, so it cannot hide an existing sparse subfield associate from this test.

The determinant can exceed2^n: N_(R_n)(iota(f))=N_(R_r)(f)^(n/r), so |N_(R_r)(f)|>2^r suffices. This restriction does not defeat the algorithm. Thus enlarging the prior constant block to a logarithmic-size block, while keeping its support family public, is not a hardness-compatible repair. In contrast, arbitrary unknown support of sizeO(log n) has the quasipolynomial enumeration bound; no polynomial algorithm for that general case is asserted.

This is a complete conditional-joint-law control, independent of whether a proposed sampler for nu has efficient rejection or a proved standard origin. It does not claim every structured ideal arises from a subfield.
