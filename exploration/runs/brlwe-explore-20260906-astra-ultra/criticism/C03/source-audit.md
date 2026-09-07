# C03 primary-source boundary audit

Direct primary-source recheck by the nonauthor critic on 2026-09-06.

## Micciancio: source task requires a wording correction

[Generalized compact knapsacks, cyclic lattices, and efficient one-way functions](https://cseweb.ucsd.edu/~daniele/papers/Cyclic.pdf),
Definition 2.5, printed p. 6; Theorem 4.2, p. 13; Theorem 4.8 and its proof,
pp. 17–18.

The task is **any-preimage inversion on planted-distribution inputs**. Use that
wording in `candidates/C03/source-check.md` in place of “average planted
inversion.” The theorem uses cyclic convolution, prime polynomial p,
polynomially bounded m=omega(1), fixed positive delta, coefficient set
{0,...,floor(p^delta)}, and
p >= (3cmn^(5/2))^(1/(1-delta)); its approximation factor is 3mnp^delta.
The proof transfers to uniform targets using Theorem 4.2.

Our assessment: C03's two binary blocks and negacyclic ring do not instantiate
these hypotheses. The terminology correction reinforces the missing bridge;
it does not invalidate the transport calculation.

## Lyubashevsky–Micciancio: collision result, different parameters

[Generalized Compact Knapsacks are Collision Resistant](https://cseweb.ucsd.edu/~daniele/papers/IdealHash.pdf),
Section 5.1 and Theorem 5.1, printed pp. 6–7.

The theorem concerns collision search for random public weights over
Z_p[X]/(f), with f monic irreducible, coefficient bound d a positive integer,
and expansion bound EF(f,3)<=E. The modulus p is an integer; primality is not
a hypothesis here. It requires m>log p/log(2d) and
p>2Edmn^(3/2)log n, with approximation factor 8E^2dmn log^2 n.
Power-of-two negacyclic f is supported.

At m=2,d=1 the first condition requires p<4, while the second eventually
requires p>4. Thus even the enclosing ternary box cannot instantiate this
theorem at two blocks and growing n. Constant m in the paper uses growing d.

Hardness of collision search on a larger domain does imply hardness of finding
collisions in a subset; the domain difference alone should not be overstated.
The additional missing implication is from binary any-preimage inversion to a
collision. The injective binary-map example in mathematical-checks.md shows why
simply planting a known pair and accepting its returned preimage gives no such
implication. The paper supplies no C03-specific inversion bridge.

## Exact source classification and uniform-target obstruction

These are deductions about C03, not claims attributed to the papers.

Conditional on a_2 being a unit, the source law is exactly an independent
uniform unit a_2 together with uniform A and C=Ax+y, for independent iid
binary x,y. Conversely, a sample (A,C=Ax+y) and an independent uniform unit
V produce the conditional source as (VA,V,VC). Thus the proposed exact
source assumption is tailored relative to the checked evidence: its unit
branch is already the binary-error neighbor of the target.

For each fixed pair of public weights, the planted-target support has at most
4^n elements. The probability that an independent uniform target belongs to
this support is at most (4/q)^n. Therefore the planted and uniform-target
joint laws have statistical distance at least 1-(4/q)^n for q>4. This prevents
an appeal to near-uniformity for this source. It is not an efficient membership
test, an attack, or an impossibility result for every computational reduction.

The source assumption could still be stated explicitly, and either exact
planted-pair hardness or the stronger any-preimage hardness would suffice for
the corresponding conditional implication. No independent justification for
either exact C03 regime is supplied by the checked sources.

## Access and audit limits

Both primary PDFs were opened successfully and the definitions, theorem
hypotheses, and relevant proof steps were readable in text extraction.
Screenshot attempts for Cyclic PDF page index 16 and IdealHash page index 6
failed with cache-miss errors. IdealHash page index 5 returned a screenshot
reference without a visible image block and was not relied upon as visual
evidence. No search-result summary is used as a premise.

This was a recheck of the two sources already selected for C03, not an
exhaustive literature search. It does not establish that no suitable theorem
exists elsewhere. The proposed variance-matching question remains future,
unproved, and outside this review.
