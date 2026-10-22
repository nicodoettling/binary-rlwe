# SV-PRIME-SUPPORT-v2 author proof

The contraction/order proof of SV-SUBFIELD-v2 gives, BEFORE bounding the number of factors,

    log2 d_g <= (g/n)log2 N(J_o)+2 sum_i b_i log2 p_i.

This follows from ord_(2g)(p)<= (g/n)ord_(2n)(p)+2 and unramified odd-prime contraction; merged contractions take the maximum exponent, at most the sum. The claimed bound follows. Choose the least power-of-two g>=2 strictly above 2C log2(n)/(1-rho). Eventually g<=n, g=O(log n), and d_g<2^g is polynomial numeric. The already specified algorithm computes all d_g by integer normal forms and uses the least feasible value, so no factorization or knowledge of the promise constants is required.

For the second sufficient condition group by rational p. Write bmax(p)=max_(i:p_i=p) b_i. Since odd primes are unramified, the odd part of the exponent is product_p p^bmax(p). With at most t factors over each p,

    B(J_o) <= t sum_p bmax(p)log2 p <= t log2 e.

Thus the first criterion applies with constant tC. This extends bounded TOTAL support to bounded support PER characteristic.

Here is a nonempty family beyond bounded total support and beyond polynomial-index ideals. Effective Linnik supplies absolute C0 and exponent6 so that the least prime in any coprime progression of modulus M is at most C0 M^6. Use the same permitted Xylouris primary theorem and elementary search interpretation as the inherited prime construction. Fix k0>=2 sufficiently large. For j>=0 let k_j=k0+j and take the least prime

    p_j = 1+2^k_j (mod 2^(k_j+1)).

This progression is odd and coprime. Hence v2(p_j-1)=k_j exactly, all p_j are distinct, and log2 p_j <= c0+6(k_j+1), with fixed c0=max(0,log2 C0). Choose k0 so large that

    sum_(j>=0) (c0+6(k_j+1))/2^(k_j-1) < rho/2

for a chosen fixed rho in(0,1). Such a fixed k0 exists by the convergent geometric series. For n a sufficiently large power of two take L=floor(sqrt(log2 n)) and j=0,...,L-1. Since k_j<=log2 n+1 eventually, the residue degree of p_j in R_n is exactly f_j=n/2^(k_j-1). Pick one prime ideal P_j above each p_j, and let I_n=product_j P_j. Then

    log2 N(I_n)/n = sum_j log2(p_j)/2^(k_j-1) < rho/2,
    log2 e(I_n)=sum_j log2 p_j = O(log n).

The first fixed prime gives log2 N(I_n)>=c*n for c=log2(p_0)/2^(k0-1)>0, so the index is exponential. The number L of distinct prime ideals is unbounded. The primes have subpolynomial value exp(O(sqrt(log n))) and their product has polynomial value.

To make the full Galois stabilizer trivial, choose a polynomial-value completely split prime q_n>=n^4 using the already reviewed effective prime construction, and pick one prime ideal Q_n above it. For large n, q_n is distinct from every p_j. Let J_n=I_n*Q_n. The added norm contributes O(log n), so N(J_n)<=2^(rho*n) eventually, and e(J_n)=q_n product_j p_j is polynomial numeric. Every rational characteristic has exactly one supported prime ideal. Since Galois automorphisms preserve rational characteristic, stabilizing J_n forces stabilizing Q_n; its stabilizer is trivial because q_n splits completely. The algorithmic classification therefore covers this family although total support grows and symmetry descent alone has no nontrivial stabilizer to exploit.

This is a family of ordinary ideal inputs: the theorem does not require computing their factorization from J. For effectiveness of constructing examples, the rational primes can be found by deterministic search with trial division in polynomial numeric bounds. Prime ideals above them can be represented by irreducible factors of X^n+1 over F_p and ordinary integer ideal bases; finite-field factorization can be performed in polynomial n,p time (e.g. Berlekamp linear algebra and enumeration of all field constants). Because p is polynomial numeric here, this is polynomial in n. Alternatively the scope statement quantifies over all such supplied ordinary ideal bases and needs no external acquisition procedure. Computing products and normal forms has polynomial bit complexity. None of these scope observations turns the remaining source into an established hardness premise.

At rho=0 the core criterion concerns only J=R; the growing exponential-index example is asserted only for 0<rho<1.
