# H final author packet: all-width alignment and one LLL escape test

2026-10-18. Status PROVISIONAL. The selected H task is complete at author level; independent nonauthor, source and fresh-blind gates remain open. The underlying standard-hardness foundation is still OPEN.

The proposed all-width estimate survives with a stronger author constant:

    Pr_(X~D_(F,s))[0!=X in FI]
      <=min(1,2/N(I)+(32n/s)^n).

The standalone theorem and proof specify coefficient norms, full infinite Gaussian normalizers, zero rejection, exact ideal clearing, almost-sure complete histories, arbitrary later selection paid over every actual attempt, and bounded conditional TV errors. The proof uses ideal duality plus disjoint-ball packing and a two-regime Poisson argument. The original constant256 follows immediately. The concrete A/B/C parameter substitution proves s_J>=512n^2 using C's explicitly chosen v0 floor and A's actual width window; it does not assume a hidden floor or confuse polynomial-bit and polynomial-value parameters.

A separate shifted-coset companion extends the upper bound to every residue atom and gives BOTH complete source and uniform-residue/conditional-lift comparator laws. Uniformity is asserted only with an explicit smoothing error, never from a small alignment probability. The conditional-lift comparator is an analysis law, not a new simulator promised by the oracle.

The selected constructive escape is an executable integer-relation/LLL procedure. With m<=n fresh samples, the relation lattice has actual determinant h=|image|<=M; full rank of the sample matrix is tested and its failure probability is bounded directly under the original Gaussian law. The output satisfies

    ||Y||/M^(1/n)
      <=s sqrt(mn)L 2^((m-1)/4) h^(1/m)/M^(1/n).

The worst-case h=M certificate has no polynomial parameter intersection for M>2^(rho n), fixed rho>0. Taking m=O(log n) gives a polynomial certificate only in the restricted log M=O(log^2 n) range. Taking m>n introduces a forced exact kernel that can produce zero. Trivial scalar-p relations and the deterministic coordinate-vector baseline are retained. This is a failure of the available worst-case guarantee, not a claim that actual LLL fails or that general short-relation search is impossible. The exact next missing original-law nonzero short-image problem is stated in short-relation-v1.md.

Two parent-reserved exact finite controls passed:8 finite laws,143,144 point pairs each,296 packing counts in the first job, exact original and conditioned normalizers, mandatory CP-1, actual relation-index distributions, nonzero/rank guards, full retained input TV equality and complete output TV contraction. Original stdout/stderr and resources are preserved. Neither finite truncation proves the infinite Gaussian statements.

Files for review are theorem-only-v1.md, proof-v1.md, parameters-v1.md, shifted-cosets-v1.md, short-relation-v1.md, lll-source-check-v1.md, finite-report-v1.md, gaps-and-regressions-v1.md and claim-graph-v1.json. The exact global regression intake is snapshotted. packet-hashes-v1.sha256 and freeze-receipt-v1.json identify the frozen bytes. No experimental job or reservation remains active. Do not infer certification from the author report or root's co-origin check.
