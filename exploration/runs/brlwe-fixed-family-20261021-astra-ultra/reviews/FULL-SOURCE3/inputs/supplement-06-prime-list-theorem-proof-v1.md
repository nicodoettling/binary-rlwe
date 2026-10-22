# DD2-PRIMES-v1: polynomial-value distinct split-prime lists

Status: PROVISIONAL, exact finite construction plus an imported effective Linnik bound. No numerical prime experiment has run. This supplies prime lists, not a distinguisher promise on those lists.

## Frozen statement

Let n≥2 be a power of two, M≥1 and Qmin≥3 integers. Let J be integral with 1≤D=N(J)<2^n, supplied by an ordinary basis. There is a deterministic algorithm producing M distinct odd primes q≡1 mod2n, all q≥Qmin and gcd(q,D)=1. For one fixed effectively computable absolute C≥1,

    q ≤ C [4n(M+n+t0+2)]^6,
    t0 = max(1,ceil((Qmin−1)/(2n))).

Its runtime is polynomial in the numerical values n,M,Qmin and in the basis encoding length. In particular these primes have polynomial VALUE whenever those three inputs do; a mere polynomial encoding-length conclusion is not being substituted. The construction first makes a list independent of J and then deletes divisors of D and truncates, so its J-dependence is explicit. The exact algorithm below does not need to know the numerical value of C to run; its stopping time is bounded by that fixed polynomial.

## Primary-source input

Xylouris, *On the least prime in an arithmetic progression and estimates for the zeros of Dirichlet L-functions*, Acta Arithmetica150(2011), Theorem1.1, printed p.66, states P(a,m)≤C m^5.18 for coprime positive a,m, with an effectively computable absolute C. Printed p.65 states the general effective-constant Linnik formulation. We use only the weaker exponent6, after increasing C to at least1. This source is a primary research paper and its theorem statement was inspected directly: [publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83078), DOI10.4064/aa150-1-4. The older [arXiv thesis](https://arxiv.org/pdf/0906.2749) gives5.2; the published statement is the designated source. We do not claim a new proof of Linnik's theorem or a practical bound for its constant.

## Construction and proof

Set R0=M+n, B=R0+t0+2. By Bertrand's postulate choose an odd prime p with B<p<2B; find one by increasing integer trial division. Since p is odd and n is a power of two, gcd(p,2n)=1. For t=t0,...,t0+R0 form

    a_t=1+2nt,  m=2np.

Because t0+R0<p, these a_t are distinct integers strictly between1 and m. Each is at least Qmin and congruent1 modulo2n. At most one of these R0+1 t-values has p|a_t; discard it if present and keep the first R0 remaining classes. Each kept a_t is coprime to m.

For each kept class, enumerate a_t, a_t+m, a_t+2m,... until its first prime q_t is found, using exact integer primality testing (even trial division suffices for the stated numerical polynomial bound). Linnik gives

    a_t ≤ q_t ≤ C m^6 ≤ C(4nB)^6.

All q_t are distinct because they lie in different residue classes modulo m; all are odd, split completely in R, and exceed Qmin−1. Trial division and enumeration cost at most a fixed polynomial in that upper bound, so this is polynomial in n,M,Qmin. No use of a prime-density asymptotic, random-prime sampler, or unbounded expected retry is needed.

Compute D by the exact determinant of the supplied basis. Test gcd(q_t,D) for each resulting prime and delete those dividing D. As D<2^n, it has fewer than n distinct prime divisors (the coarser bound n is enough). At least M of the R0=M+n primes survive. Keep the first M in the fixed initial order. Gcd and determinant bit costs are polynomial in the actual supplied basis/ideal encoding; no factorization of D is required.

## Boundary and composition conditions

- n≥2, Qmin≥3 ensure all moduli and auxiliary primes exceed the small exceptional cases; C can absorb the finitely many small moduli in the imported theorem.
- If only D≤2^(ρn), ρ<1, the stricter D<2^n hypothesis holds. General larger D can be handled by R0=M+ceil(log2D), but then that numerical input must be charged.
- Exact roots may be found by testing all residues in each F_q. This is polynomial because q is polynomial in value, but no claim polynomial only in logq is made for enumeration.
- Choosing Qmin≥nσ is legal only after σ and the sample count are frozen. If sample count depends on logQmax, a separate explicit noncircular parameter witness is required; this lemma does not solve that inequality automatically.
- An RLWE distinguisher for one externally fixed q is not thereby a distinguisher for the constructed average-modulus ensemble. Any average or all-q oracle promise must appear in the final theorem.
