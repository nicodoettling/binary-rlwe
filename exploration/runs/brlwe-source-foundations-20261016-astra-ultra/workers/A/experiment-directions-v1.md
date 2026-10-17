# Exact experiments and directions — A v1

Status: **PROVISIONAL**, author calculation, not reviewed. Parameters and Base2 are exactly SC-v1. `U_2` denotes product uniform on `R_q^2`. All errors here are coefficient-product `D_ell` unless otherwise stated. There is one two-sample challenge, no oracle.

| Experiment | Published input | Hidden randomness | Comparator | Direction actually available |
|---|---|---|---|---|
| SC-v1 Base2 | `A_1,A_2` | One uniform d-support T; independent uniform `U_i in I_T`; independent `F_i` | `U_2` | Assumed pseudorandomness implies accepted m=1,2 exact binary recovery hardness by A-PPT v2 |
| Ordinary primal integral RLWE with uniform secret | `(a_i,b_i)_i`, `b_i=a_i*s+F_i` | Shared uniform `s in R_q`; independent uniform `a_i`; independent errors | All four ring entries independent uniform | Erasing `a_i` produces the support-size mixture below, not fixed-d Base2 |
| RLWE with a uniform fixed-rank CRT secret | Same as preceding row | Uniform d-support T; `s` uniform among generators of `I_T`; other variables unchanged | Same four-entry uniform comparator | Erasing multipliers produces Base2 exactly; this is a strengthened source whose independent hardness is OPEN |
| Known-ideal noisy points | `(T,A_1,A_2)` or basis of inverse-image ideal | Same as Base2 | Same T and independent uniform pair | Forgetting T gives Base2; hardness of easier-to-observe known-ideal problem would imply Base2 hardness, but no such theorem is imported |
| Order-LWE Section 7 HLBDD specialization | Two noised points from one intermediate ideal quotient | Uniform ideal from prescribed product-prime family, uniform quotient points, ambient canonical discrete Gaussian | Resolved by H4 as uniform ring pair | Contract motivated by primary definitions/hybrid; this is not a worst-case-hardness reduction |

## A-H1 v1: deletion map and both endpoint laws

Let `R_q = F_q^n` through CRT. The algorithm `K` returns `(b_1,b_2)` and uses no coins. Under the ordinary uniform comparator it returns exactly `U_2`.

For each fixed secret s, define `T(s)={j:s_j != 0}`. The multiplication map `a -> a*s` surjects onto `I_T(s)`. Its fibers all have cardinality `q^(n-|T(s)|)`, so independently uniform `a_1,a_2` map to independently uniform ideal points. Their errors remain jointly independent of both points conditional on s. Moreover this law depends on s only through T(s), so conditioning on T(s) instead gives the same full product law. No generator assumption is imposed on the resulting points; they may vanish at active coordinates.

For uniform s, each support indicator is independent with probability `1-1/q`. For every subset T,

    Pr[T(s)=T] = (q-1)^|T| / q^n.

Writing `Base2_t` for SC-v1 with support size t, the exact planted output is

    K(RLWE_uniform-secret) = sum_(t=0)^n p_t Base2_t,
    p_t = binom(n,t) (q-1)^t / q^n.

Because `Base2_n=U_2`,

    TV(K(RLWE_uniform-secret), U_2)
       <= 1-(1-1/q)^n <= n/q.

This is an upper bound, not a statement that the secret's nonunit event is publicly observable. At SC-v1 q>=2n^3+1 it is at most 1/(2n^2). A fixed sparse d has mixing weight p_d, exponentially small in n for both baseline d families. A reduction cannot simply condition the source on that hidden rare event. Even an oracle revealing the event would require expected 1/p_d independent source challenges to rejection sample it.

For a secret drawn uniformly among all elements of CRT rank d, the same proof gives exactly Base2_d and exactly U_2 on the comparator. This proves only a direction from a different RLWE source assumption; proving that assumption from ordinary uniform-secret RLWE is an open obligation and is not solved by this identity.

## Preserved failed endpoint

The candidate claim “drop a from ordinary RLWE to obtain Base2_d” is **REJECTED**. The computed endpoint has binomial support size centered near n. The corrected exact mixture identity is PROVISIONAL. No generic impossibility for all public reductions is claimed.

## A-H2 v1: public projection collapses the endpoints

Independently choose uniform d-support T and its CRT idempotent e_T. Given the same two RLWE samples, output

    C_i=e_T*b_i+G_i,

where G_i are independent fresh coefficient D_ell masks. On the uniform comparator, each e_T*b_i is independent uniform I_T conditional on T, so the output is **exactly Base2_d**, not uniform R_q².

On the planted input, C_i=e_T*a_i*s+e_T*F_i+G_i. Let E be the event that every s_j is nonzero for j in T. Its probability is `(1-1/q)^d`. Conditional on T,E and any source-error realizations, the e_T*a_i*s are independent uniform I_T. Adding e_T*F_i translates within I_T and hence leaves their full law unchanged. The fresh G_i are independent. Therefore the planted endpoint conditional on T,E is also the corresponding Base2_d conditional law. Since Pr[E|T] is constant across T, conditioning on E keeps T uniform. Consequently the two public endpoints have TV at most

    1-(1-1/q)^d <= d/q.

This failure does not involve a changed Gaussian convention: the distorted source errors are absorbed exactly into independent uniform ideal points on E. It is the uniform comparator that has become the same lossy law. The candidate claim “project ordinary RLWE to fixed-d Base2 while retaining a uniform comparator” is **REJECTED** for this explicit map.

## Stronger scoped obstruction A-H3

The separate frozen statement and proof entropy-budget-theorem-only-v1.md and entropy-budget-proof-v1.md propose an information-theoretic obstruction for *all* exactly uniform-comparator-preserving randomized maps consuming only two ordinary RLWE samples. It does not claim an impossibility for unrestricted reductions.
