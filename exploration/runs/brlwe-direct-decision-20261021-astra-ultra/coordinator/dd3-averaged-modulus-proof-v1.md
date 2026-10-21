# DD3-AM-v1 candidate proof, initial frozen derivation

PROVISIONAL. See separate statement for scope and unclosed interfaces.

For each occupied coset c of J, let B_c be its binary vertices, m_c=|B_c|. For fixed q put

    T_c(q)=sum_j #{(b,b') in B_c^2:b!=b', b(zeta_j)=b'(zeta_j)}.

For every j,v, N_q(c,j,v)^2 <= sum_v N_q(c,j,v)^2
 = m_c + number of ordered distinct pairs colliding at j <= m_c+T_c(q).
Therefore max_(j,v) N_q(c,j,v)<=sqrt(m_c+T_c(q)). Diagonal m_c is counted ONCE; the overestimate of off-diagonal collisions alone is summed over roots.

For b!=b', f=b-b' is a nonzero element of the number field with coefficients in {-1,0,1}. Its nonzero integral algebraic norm satisfies

    1<=|N(f)|<=||f||_coef^n<=n^(n/2).

If f vanishes at any root of X^n+1 modulo a split prime q, then q divides the resultant N(f). At most log|N(f)|/log Qmin of the distinct primes in Q can divide this integer. Each such q contributes at most n roots. Thus, for EVERY pair b,b',

    (1/M) sum_q sum_j 1[f(zeta_j)=0]
       <= nu := n^2 log n/(2 M log Qmin).

This uses only distinctness, primality, splitting and a common lower bound; no random-prime equidistribution theorem is invoked in the inequality. It remains true for a list selected after J, since it is a deterministic divisor-count bound for every f.

Consequently E_q T_c(q)<=nu m_c(m_c-1). Jensen followed by sqrt(x+y)<=sqrt(x)+sqrt(y) gives

    E_q max_(j,v)N_q(c,j,v)<=sqrt(m_c)+sqrt(nu)m_c.

Sum over c, divide by 2^n, use sum_c m_c=2^n and Cauchy
sum_c sqrt(m_c)<=sqrt(C_J 2^n). This proves AM1 as written.

AM2 is exactly the selected-functional envelope in dd3-selected-functional-v1.md, with full normalizers. The full observation can reveal more than c, but its guessing success is bounded by the common pointwise Gaussian envelope; no assertion of posterior uniformity is made.

The source completion uses the full stacked multiplication matrix for ALL extractor challenge samples. It is the inherited A-FRAC full-law comparison (including S) with proof G,H integrated as specified. Since the extractor's final output is an index/value pair and acceptance compares to actual S, revealing (source state,H,Y) can only increase its success. Conditional on source state,H, S,G retain their original product law. Apply AM2 there, then charge bad-source and completion errors once. The source sample count is the number of actual challenge samples consumed/reused, not the potentially much larger number of D calls.

The extraction, prime-list complexity and final favorable-q decoder selection are not proved by this initial file. They remain explicit pending edges and must be frozen with exact constants before review.
