# FULL-SV1 source and complexity report

Reviewer: FF1. Scope: the exact SV-BDD-CLASS-v1, SV-FROB-PRIME-v1 and SV-SYMDESC-v1 statement/proof pairs in the input manifest. This FULL review had author-summary exposure. It is not formal verification or a hardness certification.

## Primary source access and imported facts

Read Milne, *Algebraic Number Theory*, primary PDF, relevant statement/proof passages: Theorem3.34, printed59–60; Proposition4.1(a) and Proposition4.2(a), printed69; Proposition6.2 and its proof, printed96–98; the decomposition/Frobenius discussion and Example8.18, printed141–143. These establish Galois prime transitivity, ideal-extension norms, cyclotomic integral bases, unique total ramification at2, and Frobenius action at odd primes. The uses satisfy the field, integral-closure and unramified hypotheses. The numeric absolute norm is explicitly linked to index by Proposition4.2(a). [Milne primary PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf).

For normal forms, the Kannan–Bachem1979 publisher abstract explicitly covers polynomial operation counts, intermediate binary lengths and multiplier matrices. This matches the limited imported bit-complexity fact. The full paper was not accessible: publisher PDF redirected to the abstract; two TAMU PDF addresses returned404; the ETH address was inaccessible. No full-paper inspection is claimed. [Kannan–Bachem primary publisher page](https://epubs.siam.org/doi/10.1137/0208040). The same access boundary was recorded in the inherited RH M1 source report. No unavailable Gaussian-sampling result is imported here.

## Algebraic hypothesis translation

For n a power of two, X^n+1 is the relevant cyclotomic polynomial and R is the full integer ring. This supplies field division for every nonzero acquired f. The ordinary ideal basis is a promise on input, not a claimed polynomial-time recognition or primality test. Exact ideal closure can be tested by the negacyclic shift if desired; none of the promised correctness statements require that test.

For odd prime ideals, sigma_p fixes the prime and induces Frobenius. Its fixed-field degree is n/ord_(2n)(p). An invariant integral element reduces to a root of Y^p−Y; constants make the image exactly F_p. This uses primality and cannot be relabelled for an arbitrary composite quotient.

For general J, eligibility forces the ramified exponent c<n, so the 2-primary additive exponent is at most2. Writing e=a*m with m odd, valuations of J+mR erase exactly the 2-part. The odd part is unramified over its stabilizer fixed field. Equal valuations on each stabilizer orbit therefore descend to an integral ideal I, and contraction recovers I. The norm identity becomes N(J_o)=N(I)^|H|. The identification O_(K^H)=R^H follows because being integral over Z is unchanged by viewing the same element in the overfield. These steps do not assume an effective factorization algorithm.

## Ordinary-basis computation and bit costs

Let L denote the full input encoding length. Determinants/cofactors bound the bit lengths in A^-1 by a polynomial in n and L. Computing the least common multiple of all reduced denominators gives e with polynomial bit length and cost. No iteration up to e is used for this computation. Exact automorphism membership tests A_o^-1 P_u A_o use n candidates, and equality follows from containment plus equal finite index. Signed-orbit propagation has polynomial size and produces integral saturated fixed vectors directly.

The rectangular normal-form uses introduce no hidden short-basis assumption. They can even be reduced to the nonsingular-square interface explicitly retained by RH M1. For a full-row-rank integer generator matrix [B,C] with nonsingular B, the square matrix [[0,I],[B,C]] is nonsingular; the bottom-right block of its upper-column HNF generates the projected lattice BZ^n+CZ^k. Rational elimination finds B if it is not already supplied. This handles [A,mI]. For the congruence C z=0 mod s, the image size is s^n/det(CZ^g+sZ^n), another full-row-rank lattice computation with the known independent columns sI. It equals the stated Smith product. Thus the claimed bit complexity does not depend on assuming that naive unbounded Euclidean elimination has controlled intermediates.

For the stated Smith argument directly, unimodular row operations preserve congruence to zero modulo s, and unimodular column operations biject Z^g. Each diagonal constraint c_i z_i=0 mod s has index s/gcd(s,c_i). The product is exact, and no zero diagonal arises because A_o^-1V has full column rank. The alternative computation above is explanatory support, not a change to candidate bytes or a new source premise.

Enumeration loops are polynomial in numeric D, p or d_H, respectively; theorems correctly do not promise polynomial time merely in log D, log p or log d_H. Exact rational residue keys have polynomial bit length; deterministic sorting gives bounded comparison cost. The acquired vectors have coefficients at most2 in absolute value. Multiplying T and solving the nonsingular multiplication matrix of f have polynomial bit and output cost in the full encoded target. The strict squared guards are rational tests. No inaccessible lambda, Gaussian oracle, unknown short basis, randomized success condition or secret-dependent advice is required.

## Inherited radius and scope

DD FIXED-MAIN-v2 fixes epsilon0=epsilon_*/2 and invokes AM-MAIN-v3 with epsilon=epsilon_*/4 and delta=epsilon_*/16. Its d0=delta ell²/(64 nKchi) is exactly epsilon_*ell²/(1024 nKchi); division by Qmax yields the displayed source radius. Since Qmax>=Qmin>=8n³ ceil(sqrt(Kn))ell⁴, epsilon_*<1 and chi>=1,

    r < 1/(8192 n⁴ K ceil(sqrt(Kn))ell²) < 1/(4sqrt(n)).

This is a finite implication under the exact inherited guards, not a replacement of Qmax by an asymptotic estimate. If FF supplies any changed source radius or different ideal family, this classification needs fresh comparison. Its elementary standalone rounding theorems remain governed by their own explicit strict radius premises.

The older M1 theorem supplies an easy wide-DGS criterion, with a different conclusion. These SV results instead construct actual ideal members and directly recover every promised target. The substantive acquisition step is the finite quotient collision in an explicitly computed invariant lattice. The supplied-element decoder itself is correctly acknowledged as overlapping older integral cancellation. None of these facts establishes hard residual ideals or settles the one-fixed-target FF quantifiers.
