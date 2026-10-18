# Exact existing-gadget convention for the quotient-only basis

PROVISIONAL clarification to joint-first-partial-v1.md, whose bytes remain unchanged. Its construction used the binary LENGTH of each invariant factor d_i, permitting a redundant generator when d_i is a power of two. The same short-basis conclusion applies to the existing minimal gadget with k_i=ceil(log2 d_i), without adding any W columns or changing its public law:

- If d_i<2^(k_i), use the k_i-bit expansion of d_i as the final relation.
- If d_i=2^(k_i), use 2 e_(k_i-1) as the final relation.

In either case the first k_i-1 relations are 2e_j-e_(j+1). Eliminating these identifies the quotient with Z/d_i, so the basis determinant has magnitude d_i. The final vector has norm at most max(2,sqrt(k_i)), and the Frobenius norm squared is at most 6k_i. In particular, for d_i=2 and one generator g=1, the correct existing-gadget kernel basis is [2]. All subsequent sublattice/full-kernel HNF arguments use these exact existing blocks and require no added public columns. This is a convention clarification, not a claim that the simultaneous mod-q trapdoor has been constructed.
