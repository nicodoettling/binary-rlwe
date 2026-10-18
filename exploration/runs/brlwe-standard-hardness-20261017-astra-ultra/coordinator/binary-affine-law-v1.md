# Exact binary-law constraint on affine rerandomization

Status: PROVISIONAL author calculation, no independent acceptance. Frozen 2026-10-17. This is a scoped algebraic check for the tower repair, not a barrier to nonlinear or computational simulation.

Let q be an odd prime, N>=1, C={0,1}^N inside F_q^N. Let M be invertible over F_q and t in F_q^N. Suppose MS+t is exactly uniform on C when S is uniform on C. Then M is a signed permutation matrix, with each entry of t equal to zero for its positive row and one for its negative row. Conversely those maps preserve the uniform law on C.

Proof. Since the map is injective on F_q^N, equality of the distributions implies MC+t=C as sets. Fix a row. If it contains two nonzero entries a,b, fixing the other bits leaves coordinate values c,c+a,c+b,c+a+b, all of which would need to lie in {0,1}. For odd characteristic a,b nonzero give at least three distinct values: if b differs from both a and -a, the first three are distinct; if b=a, the values c,c+a,c+2a are distinct; if b=-a, the values c-a,c,c+a are distinct. This is a contradiction. Each row therefore has at most one nonzero entry, and invertibility gives one per row in distinct columns. The two possible coordinate values force its entry to be +1 with shift0 or -1 with shift1. The converse is direct.

In the power-of-two cyclotomic coefficient basis, multiplication by a unit u in R_q is an invertible negacyclic matrix M_u. If it admits an affine shift t preserving the exact coefficient-binary law, then its first column has only one nonzero coefficient, equal to +1 or -1. Thus u=+/-X^j. Conversely each such negacyclic shift can be corrected with the row-wise affine shift above. There are exactly2N such multiplier units for q odd and N>=1.

For a fixed multiplier A, multiplying by a binary-law-preserving scalar unit can therefore produce at most2N values. If that orbit is used as the entire multiplier randomization, its total variation distance from uniform R_q is at least1-2N/q^N. This last bound is purely support counting and applies even when the orbit distribution is nonuniform. Known additive randomization of A requires a corresponding response term involving the unknown S and is not provided by this observation.

This does not exclude changing the secret distribution approximately, conditioning with a paid success probability, programming additional responses, nonlinear transformations, or maps using the recovery oracle. It identifies why an arbitrary random ring unit cannot be used for free while retaining a coefficient-binary target secret.
