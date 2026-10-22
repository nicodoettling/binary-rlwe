# SV-SUBFIELD-v2 author proof

First compute e as the smallest positive integer with eA^-1 integral. This is equivalent to eZ^n subset J, hence eR_n subset J. The unique prime over2 is totally ramified with ramification degree n. If its exponent in J is b, then 2^b divides N(J), so b<=rho n<n. Its contribution to e is therefore at most2. Thus the uniquely defined a=2^{v_2(e)} satisfies a<=2, with m=e/a odd. Ideal valuations show J_o=J+mR_n removes the2-primary factor and keeps every odd factor; aJ_o subset J. These facts include J_o=R_n.

For a given g, let V_g be the n-by-g matrix whose columns are the unit vectors with indices j*n/g, 0<=j<g. If A_o is an ordinary basis of J_o and s is a common positive denominator of A_o^-1, put C=s A_o^-1 V_g, an integer matrix. A vector z in Z^g represents an element of J_o precisely when Cz=0 modulo s. Smith normal form of C over integers, with invariant factors c_1,...,c_g (zeros allowed), gives

    d_g=product_(i=1)^g s/gcd(s,c_i),

where gcd(s,0)=s. Unimodular row and column changes are invertible modulo s, so this equals the exact image size of the congruence map. Computing these normal forms, all inverses and the ordinary ideal sum basis uses polynomial bit complexity. The integer output lengths are polynomial in the complete input lengths. At g=n, d_n=N(J_o)<=N(J)<2^n, so the feasible set is nonempty. All g indices are computed before enumeration; choosing a minimum incurs no search through an exponential number of subfields.

For d_g<2^g, h0=ceil(log2(d_g+1))<=g. There are d_g residue classes, so d_g+1 binary vectors on those h0 coordinates yield a collision. Their difference v is nonzero and ternary in R_g, with coefficient norm at most sqrt(h0)<=sqrt(g), and belongs to J_o. Thus f=a v is nonzero in J with norm <=2sqrt(g). A residue key is A_o^-1 V_g z modulo Z^n. Every exact rational key and each inversion/product has bit length polynomial in the inputs and log d_g. Enumeration time/storage are polynomial in numeric d_g, not merely its logarithm.

For T=lambda+w, f lambda belongs to R_n because f belongs to J. The coefficient norm of fw is at most ||f||_coef,2*||w||_canonical,infinity, by the unitary scaled Fourier embedding of power-of-two cyclotomics and pointwise multiplication. Hence every coefficient error has magnitude <=2sqrt(g)r<1/2 under the guard. Coefficient rounding recovers f lambda exactly. Nonzero f is invertible in the fraction field, so exact division recovers lambda; its rational encoding and arithmetic costs are charged.

For the family guarantee, use the mathematical factorization J_o=product_(i=1)^t' P_i^(b_i), t'<=t, over odd rational primes p_i. Let f_i=ord_(2n)(p_i) and f_i'=ord_(2g)(p_i) be the residue degrees in R_n and R_g. The cyclotomic order formula for odd p gives

    f_i' <= (g/n)f_i+2.

To verify: write n=2^(N-1), g=2^(G-1) with 2<=G<=N. If p=1 mod4, ord_(2^L)(p)=2^max(0,L-v2(p-1)); if p=3 mod4, ord_(2^L)(p)=2^max(1,L-v2(p+1)) for L>=2. In either case the order is max(c,2^(L-v)) for c=1 or2, yielding ord_(2^G)(p)<=max(2,2^(G-N)ord_(2^N)(p))<=(g/n)f_i+2.

All odd primes are unramified in the relative cyclotomic extension. Thus contraction of P_i^(b_i) has exponent b_i. Contraction commutes with intersection; when distinct P_i contract to the same prime, the resulting exponent is their maximum, at most their sum. Therefore

    log2 d_g <= sum_i b_i f_i' log2 p_i
             <= (g/n) sum_i b_i f_i log2 p_i +2 sum_i b_i log2 p_i
             <= rho g +2t log2 e.

For the last step p_i^(b_i) divides e, since the rational prime is unramified in R_n; each b_i log2 p_i<=log2 e, even if several factors share p_i. This uses t', not the number of rational characteristics alone.

Choose the smallest power-of-two g>=2 strictly larger than (2t C/(1-rho))*log2 n. For sufficiently large n it is at most n and O(log n). Since log2 e<=C log2 n, the displayed upper bound is strictly less than g. Consequently d_g<2^g and d_g is polynomial numeric in n. The computed minimizer has d_*<=d_g, so its enumeration is polynomial too; no factorization/t,C,rho are required at execution time.

The stated family does not require a nontrivial stabilizer of J. For example, the odd ideal can combine a prime over3 of residue degree n/2 with a prime over a polynomial-value completely split characteristic. The split prime has trivial stabilizer; the product then has trivial stabilizer, while the first factor makes the ideal norm exponential. For any fixed rho>log2(3)/2, its norm remains below2^(rho n) for large n. Both factors have polynomial numeric exponent if the split characteristic does. This example demonstrates scope only; no source-hardness implication is drawn, and an exact ordinary-basis implementation or external acquisition cost remains distinct.
