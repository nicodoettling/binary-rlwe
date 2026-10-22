# FULL-FRONTIER1 source, effectiveness and resource review

## Source inputs and exact versions

SV-PRIME-SUPPORT-v1 depends on the exact ordinary-basis algorithm and radius guard of SV-SUBFIELD-v2. SV-ALL-SUBFIELDS-v1 uses the fixed-lattice construction of SV-SYMDESC-v2 for its enumeration implementation; its field-containment and norm inequality are directly proved. The four dependency file hashes match coordinator/acceptance-v3.json: SUBFIELD statement 9157018baf8fa6d4e6fc3f3e889f3ba6fd07ce206175be4f37508553593c2bae, proof bd394211a85a33ed1566aba5232300db46bc24462777186d8c7f38a24967d9d8; SYMDESC statement 087405376d31699635e87d954eaaa9305da4635b61f2b572205ba89db533cddf, proof 4a8e0b32f33c7121517108e9e1b63ff3eb9d2a50f0afea1e5c70c4e0eaa5df2a. Their frozen provisional banners do not override the later exact-hash acceptance. This review does not re-certify the entire inherited DD decoder.

The original SV-BDD-CLASS theorem/proof and the DD FIXED-MAIN-v2 statement, AM-MAIN-v3 guards, and FULL2 source/resource report were read for the actual radius. No broader hardness foundation is inherited from those conditional results. The present source statements supply an ordinary nonsingular integer ideal basis; factorization, a short member, a short basis, or an ideal-Gaussian sampler is not extra advice.

## Primary source observations and access limits

I directly read the publisher's primary PDF text for Xylouris, Acta Arithmetica 150 (2011), Theorem 1.1, printed pp.65-66. It provides an effective least-prime bound with exponent 5.18, hence the weaker exponent 6 used here. The residue classes in the new construction are positive and coprime to their moduli. This is an imported theorem, not a new proof or a computed practical constant. [Primary publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/83078).

I directly read Milne's primary course-note PDF, Proposition 4.1(a), its proof, and Proposition 4.2 on printed p.69 (PDF page index70), for the ideal-extension norm and numerical-index identification. The hypotheses are finite separable extensions of Dedekind domains and their integral closures; there is no unramified restriction. The author proof reconstructs the needed prime-factor argument. Cyclotomic integer-ring, splitting and ramification inputs remain those of the exact accepted SUBFIELD/SYMDESC dependencies, whose primary-source exposure records were also read. [Milne, Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf).

I directly read the primary publisher abstract of Kannan-Bachem's normal-form paper. It states polynomial operation and intermediate-bit bounds, including transformation matrices, for binary-encoded integer input. The full article was not read in this review; access exposed the abstract and an access gate. This is a disclosed source-access limitation, and the normal-form theorem is also an unchanged accepted dependency. [Kannan and Bachem](https://epubs.siam.org/doi/abs/10.1137/0208040?journalCode=smjcat).

For Gaussian Fourier manipulations I checked the transform, determinant cancellation and absolutely convergent theta expansions explicitly in probability-audit-v1.md. No new smoothing or Gaussian-completion theorem is imported. For finite-field factorization effectiveness the elementary Frobenius-fixed algebra argument below suffices; a black-box efficient factorization claim in log p is not required.

## Factorization-free contraction and decoding

From an input basis A, the quotient exponent is the lcm of the reduced denominators in A^-1. Setting a=2^v2(e) and m=e/a is a unique operation, not arbitrary advice. The eligible norm bound forces a<=2. Computing J_o=J+mR via integer normal forms removes the ramified part, and a J_o subset J. The inherited rejected arbitrary-factor choice is not revived.

For each standard subfield, its basis inclusion V_g is explicit. After clearing a denominator s in A_o^-1 V_g, the exact index is product_i s/gcd(s,c_i), where c_i are the Smith diagonal entries. Normal forms and rational arithmetic have costs polynomial in full input bits. Output logs and matrix entries have polynomial bit bounds. There are only log2 n such subfields. None of these computations factors the ideal or its norm.

Enumeration of d_g+1 binary vectors does cost polynomial in the numeric d_g. A repeated residue gives a nonzero ternary member v, and f=a v has coefficient norm at most 2sqrt(g). Multiplication fT, coefficient rounding and division by nonzero f are rational operations in the cyclotomic field. The strict condition 16r^2 g<1 makes every coefficient error less than 1/2. Input and output lengths are charged, and ordinary-field inversion is polynomial in them. Equal endpoints are not silently rounded correctly.

At the actual accepted DD radius,

    r=epsilon_* ell^2/(1024 n K chi Qmax),
    Qmax>=8 n^3 ceil(sqrt(Kn)) ell^4,

with epsilon_*<1 and chi>=1. Thus

    r<1/(8192 n^4 K ceil(sqrt(Kn)) ell^2)<1/(4sqrt(n)).

Since g<=n, the strict guard follows. K is the physical source sample count. The bounds keep Qmax, K, chi and the advantage factor. No comparison with a wide DGS sampler or existential short vector substitutes for this decoder.

Under B(J_o)<=C log2 n, take a power-of-two g strictly greater than 2C log2 n/(1-rho). The next-power-of-two factor only changes a fixed polynomial exponent: eventually g<=2 max(2,2C log2 n/(1-rho)), hence 2^g is polynomial in numeric n. The computed minimizer d_* is no larger than this witness d_g. The algorithm is uniform over the inputs and need not receive C, rho, t or a factorization; its promised-family polynomial bound may have degree depending on the fixed constants. For arbitrary inputs its cost remains explicitly polynomial in numeric d_*.

## Effective growing-support family

For a chosen fixed positive rho, effective Linnik supplies constants C_0 and exponent 6. With k_j=k_0+j, the progression 1+2^k_j modulo 2^(k_j+1) is odd and coprime to its modulus. It enforces the exact valuation v2(p_j-1)=k_j. The bound log2 p_j<=c_0+6(k_j+1) makes the weighted sum with denominators 2^(k_j-1) converge to zero as k_0 grows. A fixed large enough k_0 is therefore effective, albeit with no practicality claim.

For L=floor(sqrt(log2 n)), the sum of log2 p_j is at most L*c_0+6L(k_0+1)+3L(L-1)=O(log n), while each p_j=exp(O(sqrt(log n))). The residue degrees f_j=n/2^(k_j-1) are exact for all sufficiently large n. Thus the first fixed prime contributes a positive constant times n to log2 N(I_n), the total norm density is below rho/2, and the numeric quotient exponent is polynomial. The L rational characteristics are distinct and unbounded in number, with one supported prime ideal over each.

A polynomial-value split q_n>=n^4 can be obtained from the inherited effective construction. As a direct independent check, the residue n^4+1 modulo 2n^4 is odd and coprime; every positive prime in it is at least n^4+1 and congruent to 1 modulo 2n. Linnik bounds the least such prime by C_0(2n^4)^6, a fixed polynomial value. Trial division search therefore has a deterministic polynomial bound in n. This auxiliary observation validates effectiveness and does not change the frozen author's construction. For large n this q_n differs from all p_j. One prime ideal above q_n has trivial Galois stabilizer, and its unique rational characteristic forces any stabilizer of the product to fix it. Adding it increases log norm only by O(log n), preserving eligibility and polynomial exponent.

Prime ideals can be represented using factors of X^n+1 modulo p. Here p is polynomial in numeric n, and the polynomial is squarefree because p is odd. To factor deterministically within polynomial (n,p) cost, compute the kernel of Frobenius minus identity in F_p[X]/(X^n+1). In the mathematical CRT decomposition this kernel consists of arbitrary F_p constants in each irreducible component. A basis therefore separates any pair of different components. For each basis element and each c in F_p, take gcd with its difference from c, refining the current factors. After all basis elements and constants are processed, the factors are irreducible. Modular exponentiation, linear algebra and these at most n*p gcd operations are polynomial in n,p and their bit encodings. This supplies the stated effectiveness without claiming deterministic factoring polynomial only in log p.

Bases of the prime ideals follow from generators p and the factor polynomial. Products and intermediate bases are handled by integer normal forms, with full bit growth charged. No factorization of an externally supplied ordinary J is required by the decoder. Acquiring a source ideal in a separate external hardness reduction would remain a distinct obligation. The example supplies existence and constructibility, not a hardness assumption.

## All subfields and computational scope

The n^2 pairs of automorphisms suffice to enumerate every subgroup of C_2 x C_(n/2). Closing each pair takes polynomially many group operations on O(log n)-bit residues; deduplication is polynomial even without an optimized subgroup-list formula. Signed orbit constraints give an integer basis of the fixed lattice because each consistent orbit carries one arbitrary integer coefficient and every inconsistent-sign orbit must vanish. Since R is the full integer ring, this is O_L, not an unsaturated suborder.

Compute each d_L by the same integer-congruence map. This phase is polynomial in n and full supplied basis length. Its equivalence d_all<=d_*<=d_all^2 shows that a polynomial numeric feasible index from any subfield already produces one in the standard chain. The statement restricts only the particular binary-collision criterion. It gives no barrier against unrelated algorithms and no hardness of ideals with superpolynomial indices.

## Statistical versus computational conclusions

FRAC-INFO has finite alphabets and a finite ML table for each specified parameter tuple. It does not give a uniform finite-precision method to compare arbitrary real Gaussian likelihoods or an efficient search over 2^n secrets. Its exact laws may be mathematically defined without finite sampler code. That is appropriate to its statistical impossibility statement and cannot be promoted to an efficient attack.

GAUSS-AVG, WEIGHT-COV and WEIGHT-GAUSS are mathematical diagnostics of specified continuous affine perturbations. Their proof-selected directions and retained-secret labels do not give executable hidden-secret distinguishers. No change in the target fixed-family quantifier order or any new FF reduction is supplied. The source classifications operate at the inherited radius and strengthen a sufficient easy regime; their complement has no established hardness foundation.
