# D-SREL-CRT-1: sparse relations in the actual uniform CRT ideal family

Status: new provisional theorem and proof, requiring independent review. It neither asserts source hardness nor attacks the source. This is separate from the earlier determinant obstruction and from the provisional conditional-guessing lemma. No computational experiment was run.

## Exact family and theorem

Let n be a power of two, q0 an odd prime with q0=1 mod2n, and Omega the n distinct roots of X^n+1 in F_q0. Choose T uniformly among the d-subsets of Omega, where 1<=d<=n, and publish
  J_T={f in R: f(omega)=0 modq0 for all omega in T}.
Thus [R:J_T]=q0^d. Conjugating or permuting the roots gives the same ideal distribution. This includes the ordinary integral ideal underlying K_T(q0) when its d zero coordinates are indexed consistently. The theorem is about this exact uniform-subset law, not arbitrary ideals of this index.

For 1<=w<=n, let E_w be the event that J_T contains a nonzero coefficient-ternary element of weight at most w. Then
 Pr[E_w] <= min(1, sum_(j=1)^w 2^j binom(n,j)
             binom(n-ceil(n/j),d)/binom(n,d))
          <= min(1, sum_(j=1)^w 2^j binom(n,j) exp(-d/j)).
The numerator binomial is zero when its upper argument is below d.

In particular, if q0 is polynomial in n, d=Theta(n/log q0), and w<=C log n for a fixed C, then
  Pr[E_w] <= exp(-Omega(n/log² n)).
The conclusion applies whether q0^d is below or above2^n. The event concerns existence; no efficient recognition algorithm is assumed.

## Proof

Fix a nonzero ternary f of weight j. Modulo the odd q0 it still has exactly j nonzero coefficients. Let M_f be its n-by-n negacyclic multiplication matrix over F_q0. Every row and every column has exactly j nonzero entries, since they are signed permutations of f.

Let r=rank(M_f) and select r rows forming a row-space basis. Their supports must together cover all n columns: otherwise the uncovered column is zero in every basis row, hence zero in every row of M_f, contradicting the nonzero entries in each column. Each selected row covers at most j columns. Therefore n<=rj, or r>=ceil(n/j).

The split CRT diagonalizes multiplication by f, so r equals the number of omega in Omega with f(omega)!=0. Hence f vanishes at no more than n-ceil(n/j) roots. Uniform sampling of T now gives
  Pr[f in J_T] = binom(z_f,d)/binom(n,d)
              <= binom(n-ceil(n/j),d)/binom(n,d).
If z_f>=d, writing the ratio as a product gives an upper bound (z_f/n)^d <= (1-1/j)^d <= exp(-d/j); if z_f<d the probability is zero. There are exactly 2^j binom(n,j) ternary vectors of weight j. A union bound proves the finite statements. No independence of different root evaluations or different f events is used.

For the asymptotic statement, split q0>=2n+1 and polynomial q0 imply log q0=Theta(log n). Use d>=a n/log n and w<=C log n. For j<=w,
  2^j binom(n,j) <= (2en/j)^j <= (2en/w)^w,
because x log(2en/x) increases for 1<=x<=n. Also exp(-d/j)<=exp(-d/w). Thus the log of the sum is at most
  log w + w log(2en/w)-d/w
  <= O(log² n) - (a/C)n/log² n.
For all sufficiently large n this is -Omega(n/log² n).

## Whole joint source law and transfer consequence

Fix a distinct source modulus q with gcd(q,q0)=1. Given T (equivalently its public ideal), the proposed fractional source is
  a_1,...,a_k iid D_(J_T^-1,s), A_i=pi_q(a_i),
versus A_1,...,A_k iid uniform R_q, with the SAME T/J_T law in both experiments. Fresh binary S and independent target errors, if subsequently sampled, are independent of T and all source samples. The existence event E_w depends only on J_T, so it has the same negligible probability in both endpoints.

A generator that always privately knows a nonzero ternary f of weight<=w in its output J cannot produce this uniform-root ideal law within small statistical distance: its ideal marginal is supported on E_w, whereas the genuine marginal gives E_w the probability bounded above. The TV distance is at least 1-Pr[E_w]. Erasing f does not remove this ideal-marginal discrepancy. Rejection to condition genuine uniform T on E_w has expected trial count at least 1/Pr[E_w], whenever E_w is nonempty and testable by the procedure.

This does NOT exclude computationally indistinguishable biased ideal distributions, a class-changing standard reduction, a different structured family, or a stronger guessing argument requiring no sparse relation. Such a result must establish its own full joint law. It also does not prove that recognizing E_w or recovering f is polynomial-time.

## Exact finite hand controls

1. Weight-one f has no zero CRT roots. Weight-two ternary f also has none in this negacyclic ring: a root omega has exact order2n, and omega^(u-v)=+/-1 with0<|u-v|<n is impossible. Thus the rank/union bound is deliberately conservative for j=2.

2. n=8,q0=17, f=1+X+X^4 has weight3. In root order
  omega=(3,10,5,11,14,7,12,6),
its evaluations are
  (0,15,2,16,11,12,9,11) mod17.
Thus rank(M_f)=7, agreeing with the general lower bound ceil(8/3)=3. Its membership probability is exactly1/8 for d=1 and zero for d>=2. Treating these evaluations as independent uniform F17 values would give a different law. These are finite symbolic substitutions, not an unreserved executable experiment.

## Relevance

The new sparse-relation guessing estimate can apply to specially generated hidden-relation ideals, but this exact uniform CRT family almost never supplies the needed logarithmic-weight relation at d=Theta(n/log n). Thus simply replacing the determinant budget by the new sparse bound does not widen the existing uniform-root source family. Standard hardness for a biased hidden-relation family remains OPEN.
