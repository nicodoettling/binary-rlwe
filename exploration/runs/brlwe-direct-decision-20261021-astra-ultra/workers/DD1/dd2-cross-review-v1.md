# DD1 nonauthor cross-review: DD2-AM1-SNF-v1 and DD2-PRIMES-v1

2026-10-21, nonblind review. Reviewer DD1 is not the author of these DD2 statements, but is a coauthor of the separate extractor and has seen coordinator synthesis. This is correlated same-model scrutiny, not an independent statistical or formal certificate. Inputs read in full: DD2 am1-strengthened-theorem-v1.md, am1-strengthened-proof-v1.md, prime-list-theorem-proof-v1.md, am-v1-review-report.md and the complete DD2-AM-FV1 output. Verdict: favorable within their exact scopes; no final ACCEPT or whole-main review is claimed.

## Strengthened root collision bound

The Smith-normal-form argument correctly charges each DISTINCT root zero by one q-factor in the integral multiplication determinant. Irreducibility of X^n+1 over Q ensures the determinant is nonzero for a nonzero ternary difference. Because q is split and odd, the mod-q algebra is a product of n fields; its multiplication-map nullity is the number of root zeros. Integer unimodular matrices stay invertible modulo q, so at least that many Smith invariants are divisible by q. Distinct primes multiply without double counting. Thus the strengthened numerator n log n/2, rather than n² log n/2, is valid.

The optional subtraction of log D also checks: for f in J, D divides |N(f)|; and since each selected q is coprime to D, its required q-power divides |N(f)|/D. The non-singleton premise supplies a nonzero f and therefore D<=n^(n/2). The main designated dependency wisely omits this optional refinement.

The selected-root maximum is in the correct place. For each fixed coset, apply the norm bound to the same ordered pairs across all q, then Jensen BEFORE summing fibers. This yields sqrt(m_c)+sqrt(nu)m_c and avoids a spurious extra C_J factor. A q-dependent partition would invalidate that pairwise interchange; the theorem explicitly excludes it. A list chosen jointly with one fixed partition is fine, because the divisor bound is deterministic for every list. Repeated primes and ramified q2 are correctly rejected by the finite negative controls. The finite output tests6648 nonzero ternary vectors in degrees2,4,8; it is evidence for arithmetic and max-order issues, not a proof of the infinite theorem.

## Prime-list algorithm and primary-source check

I independently opened the [published Xylouris paper](https://www.impan.pl/shop/en/publication/transaction/download/product/83078). Printed pp.65–66 define the coprime-progression problem and state Theorem1.1 with exponent5.18 and an effectively computable absolute constant. Replacing this exponent by6 and increasing the fixed constant is legitimate. This review verifies that imported statement and its application; it does not independently reprove analytic number theory.

With R0=M+n and B=R0+t0+2, Bertrand gives B<p<2B. The candidate t interval has R0+1 entries, is shorter than p, and lies below p. Therefore at most one a_t=1+2nt is divisible by p, and each retained a_t is a nonzero reduced residue modulo m=2np. All lie strictly below m and at least Qmin. Their least progression primes cannot collide because their residues modulo m differ. Linnik bounds their VALUE by C(4nB)^6. Enumerating each progression and trial-dividing candidates therefore has a deterministic polynomial bound in numerical n,M,Qmin; it is not a polynomial-in-logQmin claim. Removing prime divisors of D discards fewer than n entries because D<2^n. No factorization of D is needed.

The unspecified but effective constant C is adequate for the stated asymptotic polynomial algorithm and eventual termination; a final theorem that requires an explicit numerical all-input compilation cap must also fix a certified C or an explicit procedure for its effective bound. The source does not provide a small practical constant, and this review supplies none. Prime generation is outside the coherent decoder body unless separately compiled.

## Main-composition cautions, not defects in these lemmas

1. The sample budget K depends on log Qmax while Qmin must exceed n sigma(K); the separate noncircular numerical parameter witness is still necessary.
2. The average decision promise must be on the actual post-filtering list, or pay the removed-list fraction. Neither theorem creates a promise from one externally fixed modulus.
3. The all-q decoder approach is sound only with the same conservative radius r=d0/Qmax and exact membership/distance verification. One fixed favorable q suffices; there is no reason to multiply failure bounds across q or charge all bad-q calls as statistical simulation errors.
4. The source wrapper's selected root must be one final pair based only on its sample transcript and extractor coins. The wrapper may use its actual generated S only in the final success test, not expose it to the extractor.
5. Finite field sampler caps and both GP endpoint losses must be paid explicitly. Full completion uses K raw samples; repeated D queries consume code time without enlarging the stacked source matrix.

Fresh whole-main nonauthor and theorem-only blind reviewers remain necessary. These favorable checks do not certify the changed averaged-modulus premise as fixed-modulus binary-RLWE hardness.
