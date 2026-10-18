# Proof of the provisional same-class counting obstruction

All logarithms below are natural. Put K=Q(zeta_(2n)) and F=K^+, of degrees n and n/2. The power-two cyclotomic discriminants are |Delta_K|=n^n and Delta_F=n^(n/2)/2. For completeness, the first follows from the discriminant of X^n+1. For the second, write t=zeta+zeta^-1. The integral rings are Z[zeta] and Z[t], with Z[zeta]=Z[t]+zeta Z[t]. This follows by reducing powers with zeta²=t zeta-1, and the equality for the fixed ring follows by conjugation and the rank count (or the usual explicit real cyclotomic integral basis). The relative quadratic discriminant is (zeta-zeta^-1)². Its absolute ideal norm in F is 4: the absolute norm in K of 1-zeta² is 4, since zeta² has conductor n and K has relative degree two over that cyclotomic field. The tower discriminant identity gives the displayed Delta_F. These identities include n=2, and only the asymptotic n>=4 matters.

Both K and F are abelian and hence normal over Q. Their degree-to-log-discriminant ratios tend to zero. The imported normal-field Brauer-Siegel theorem therefore gives

    log(h_K Reg_K)= (1/2)n log n+o(n log n),
    log(h_F Reg_F)= (1/4)n log n+o(n log n).

The regulator ratio has logarithm O(n), independently of any unproved real cyclotomic class-number assertion. Indeed every unit u in K has u/conjugate(u) a root of unity: it is an algebraic integer unit with every conjugate of modulus one, so Kronecker's theorem applies. Thus u² is a root of unity times the totally real unit u conjugate(u). Modulo roots of unity, the real-unit subgroup contains twice the full free unit lattice. Its index Q lies between 1 and 2^r, where r=n/2-1. Standard weighted logarithmic embeddings multiply each real row by two on embedding into K, so Reg_K/Reg_F=2^r/Q. Consequently its logarithm lies in [0,r log2]. Combining the two Brauer-Siegel formulas,

    log(h_K/h_F)=(1/4)n log n+o(n log n).

Since h_F>=1, h_K>=exp((1/4+o(1))n log n). No assertion that h_F=1 is needed.

For any number field K of degree n and B>=1, let A_K(B) count integral nonzero ideals of norm at most B. Positivity of the Dedekind zeta series at 2 gives A_K(B)<=B² zeta_K(2). The Euler factor at a rational prime p is the product of (1-p^(-2f_i))^-1 over prime ideals above p. There are at most n factors and each is at most (1-p^-2)^-1. Therefore zeta_K(2)<=zeta(2)^n, including ramified primes. It follows that

    A_K(exp(cn)) <= exp((2c+log zeta(2))n).

Every ideal class counted by C_n(c) has at least one such integral representative, so |C_n(c)|<=A_K(exp(cn)). Dividing by the class-number lower bound proves the theorem. Multiplication by a nonzero field element preserves the ordinary ideal class, which proves the final restricted impossibility statement.

The only probabilistic language is the fraction under the uniform distribution on the finite class group; no efficient class sampler is asserted. The Euler-factor count is exact and does not rely on a numerical experiment. An exact finite-support control can test these local factors and the discriminant identities, but cannot certify the analytic asymptotic. The Brauer-Siegel o(1) is not given an effective threshold by this proof.
