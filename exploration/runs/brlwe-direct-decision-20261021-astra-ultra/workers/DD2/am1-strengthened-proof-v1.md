# Proof of DD2-AM1-SNF-v1

Status: PROVISIONAL; binds `am1-strengthened-theorem-v1.md` exactly. The strengthening removes a factor n from the coordinator's already valid divisor-count estimate. No repeated-stage product bound is used.

## 1. Integer multiplication matrix and its determinant

Fix distinct b,b'∈{0,1}^n and f=b−b'∈R. In the coefficient basis, multiplication by f is an integer n×n negacyclic matrix M_f. Since X^n+1 is the 2n-th cyclotomic polynomial and irreducible over Q, R⊗Q is a field. Thus nonzero f has invertible multiplication and det M_f≠0. Its determinant is the algebraic norm N_(K/Q)(f).

Let ω_1,...,ω_n be the complex roots of X^n+1. The canonical evaluation matrix is scaled unitary, and hence

    sum_i |f(ω_i)|² = n sum_l |f_l|² ≤ n².

AM-GM applied to the n nonnegative squared moduli gives

    1 ≤ |det M_f| = product_i |f(ω_i)|
      ≤ (sum_i |f(ω_i)|²/n)^(n/2)
      = ||f||_coefficient^n ≤ n^(n/2).

All f_i lie in {−1,0,1}; no unproved lower bound on individual complex embeddings is used.

## 2. Every distinct modular root costs a factor q in the norm

For a split odd prime q, q does not divide n. Therefore X^n+1 has no repeated roots modulo q. Evaluation at its n roots gives an algebra isomorphism

    R/qR ≅ F_q^n.

Under this isomorphism multiplication by f is diagonal with diagonal f(ζ_(q,j)). Consequently

    m_q := #{j: f(ζ_(q,j))=0}
         = nullity_(F_q)(M_f mod q).

Take an integer Smith normal form U M_f V=diag(d_1,...,d_n), with U,V unimodular over Z and all d_i nonzero (sign conventions are irrelevant). Modulo q, U,V remain invertible. The nullity m_q is therefore exactly the number of d_i divisible by q. Every such d_i contributes at least one factor q to det M_f. Hence

    q^(m_q) divides |det M_f|.

This argument does not identify multiplicity m_q with the entire q-adic valuation; the valuation may be larger. Distinctness of the primes now gives

    product_(q∈Q) q^(m_q) divides |det M_f|,
    sum_(q∈Q) m_q log q ≤ log |det M_f| ≤ (n/2)log n.

Thus

    (1/M) sum_q sum_j 1[b(ζ_(q,j))=b'(ζ_(q,j))] ≤ ν.

For the optional ideal refinement, f∈J implies (f)⊂J and |N(f)|=D[J:(f)]. Since all q are coprime to D, their product above divides |N(f)|/D, giving the stated subtraction of log D. If a nonzero fiber difference exists, D≤|N(f)|≤n^(n/2), so the logarithmic numerator is nonnegative. No refinement is used for singleton fibers.

## 3. A selected root and value are bounded by all pair collisions

Write B_c=π^(-1)(c), m_c=|B_c|, and

    T_c(q)=sum_j #{(b,b')∈B_c²:b≠b', b(ζ_(q,j))=b'(ζ_(q,j))}.

For each fixed j,

    sum_v N_q(c,j,v)² = m_c + #{ordered distinct pairs in B_c colliding at j}.

The diagonal m_c is counted once in this identity, not n times. Therefore for every j,v,

    N_q(c,j,v)² ≤ m_c+T_c(q),
    max_(j,v) N_q(c,j,v) ≤ sqrt(m_c+T_c(q)).

Each of the m_c(m_c−1) ordered distinct pairs obeys Section2. The common partition is fixed while q is averaged, so finite sum interchange is valid and

    E_q T_c(q) ≤ ν m_c(m_c−1).

Concavity of square root, then sqrt(x+y)≤sqrt x+sqrt y, yield

    E_q max_(j,v)N_q(c,j,v)
      ≤ sqrt(m_c+νm_c(m_c−1))
      ≤ sqrt(m_c)+sqrtν m_c.

Sum this inequality over occupied c, divide by2^n, use sum_c m_c=2^n and Cauchy-Schwarz

    sum_c sqrt(m_c) ≤ sqrt(C_π sum_c m_c)=sqrt(C_π 2^n).

This proves the claimed bound. Independently max_(j,v)N≤m_c implies K_q≤1, so min with1 is valid.

## 4. Conditioning and support audit

The averaging variable q has exactly M equiprobable values. No event is conditioned on after selecting a root, no original marginal law is used as a posterior, and no product of conditional success estimates is asserted. The max is taken inside each fiber before averaging. Diagonal contributions, zero root values, singleton fibers, and primes dividing a nonzero norm with multiplicity are all retained. CP-1's support-renormalization counterexample has no matching product step here; its inequality remains rejected.

The statement bounds only the residue observation. Extending to Y=S+G requires the separate full-observation Gaussian envelope with exact normalizers. Metadata cannot be added unless that envelope's conditional product law survives. An oracle promise averaged over a different or adaptive modulus law cannot be substituted without its own change-of-measure argument.
