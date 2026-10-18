# RF3 fractional endpoint objections before repair

Added input: coordinator/binary-class-count/fractional-escape-test-v1.md, claimed SHA256 13975760fadda817b0a338f260cb72983562c0f14cf19f5f09fce26ef04ba0ca. This note was authorized after the main binary-collision reports were written. It is a separate provisional endpoint test and is not a dependency of their favorable conclusion. No coordinator file is edited here.

Status of the final v1 scale guarantee: **REJECTED as a standalone implication from its written hypotheses**. Its algebraic and Gaussian-tail subclaims are assessed separately. A later repair does not erase this v1 verdict or counterexample.

**FEP-1: the displayed scale formulas omit a needed parameter bound.** The implication from q/s>=1 to W_J>1 does not follow from the note's displayed hypotheses alone. Take its exact degree-2 example P=(2+i), p=5, H=R, D_H=1, and choose

    n=2, k=1, delta=1/2, v0=1/1024,
    q=s=w_B=3.

Then q is prime to pD_H, q/s=1, w_B<=s, and every displayed positive parameter condition holds. However,

    d0 = (delta sqrt(n) w_B)/(32 n k v0)=24 sqrt(2),
    W_J = n q/(sqrt(2)d0)=1/8.

This is an exact parameter counterexample to that standalone implication, not a claim that this parameter tuple satisfies an unspecified prior GP/BDD theorem. If the intended chain separately imposes v0>=1 and 0<delta<=1, or an equivalent lower bound on k v0/delta, the tuple is excluded; that hypothesis must be stated or precisely imported. No numerical experiment is needed for this arithmetic.

**FEP-2: a width does not define every valid output-radius guarantee.** The phrase asserting that any ordinary Gaussian norm bound B_J exceeds 1 should specify the actual deterministic formula for the certified radius and the nonzero-output/success convention. A wide lattice can have a centered Gaussian concentrated at zero even when its width parameter exceeds 1, so radius zero can bound the sampled norm with high probability; such a sample does not solve nonzero-vector search. A conventional certificate B_J>=W_J would support the intended comparison, but it is an extra statement about the chosen guarantee, not a consequence of the word Gaussian alone.

**FEP-3: the final short-generator observation is conditional.** If H=(f), then f Lambda=pP^(-1) is integral and f is invertible modulo q, since q is prime to N(H). These exact facts alone do not give a useful short-residue test for every s. The quantitative inequality is ||f x||_coeff <= sqrt(n)||f||_coeff ||x||_coeff; a proposed test needs a Gaussian norm threshold and sufficient separation from the q-scale. I treat the note's final sentence as an informal possible test, not a proved distinguishing guarantee.

The algebraic endpoint identities, minimum-norm estimate, shell tail, and finite hand control are not refuted by any of these observations. The explicit v1 scale-to-triviality conclusion is rejected as a standalone guarantee; a repaired version must specify its inherited parameter bounds and chosen radius certificate and receive an exact recheck. No other route is pursued.
