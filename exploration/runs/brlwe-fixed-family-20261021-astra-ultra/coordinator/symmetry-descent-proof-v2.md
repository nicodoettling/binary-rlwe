# SV-SYMDESC-v2 exact definition repair

Throughout this proof, a=2^{v_2(e)} and m=e/a. No arbitrary factorization with odd m is permitted. All other mathematical steps below are preserved from v1; acceptance requires exact repair review.

# Proof of SV-SYMDESC v1

Frozen author proof, PROVISIONAL. There is no new probabilistic lemma.

## The2-part and its effective removal

The ring is the full cyclotomic integer ring. Its only ramified rational prime is2, and 2R=mathfrak p_2^n, N(mathfrak p_2)=2. If J's2-part is mathfrak p_2^c, then c<=log2D<=rho n<n. Thus its additive quotient exponent is1 if c=0 and2 otherwise. The odd-primary factors of the quotient have odd exponents. Hence e=a*m with a∈{1,2}, m odd.

At any prime over2, the ideal mR has valuation0; at an odd prime, mR has valuation at least that of J by the definition of quotient exponent. Taking valuations of the sum J+mR therefore removes exactly the2-part and leaves the odd part J_o. This also proves aJ_o⊂J. Computing the sum uses the ordinary rectangular generator matrix [A,mI] and HNF; m is obtained from e by exact divisions by2, not integer factorization.

## Computing the symmetry and fixed integer lattice

Each sigma_u is a signed permutation matrix P_u in the power basis. It preserves R and determinant magnitude. For a basis A_o of J_o, containment sigma_u(J_o)⊂J_o holds exactly when every entry of A_o^-1P_uA_o is integral. Since the ideals have equal index, containment implies equality. There are n candidates u, so these exact tests find H in polynomial bit time. H is a subgroup because stabilizers are subgroups.

Build a graph on the n coefficient positions using every signed permutation in H. Propagate signs from one vertex in each connected orbit. If a closed path gives inconsistent signs, the invariant coefficient at that vertex must equal its negative and hence vanish; the whole orbit contributes no vector. Otherwise it contributes one signed indicator vector, with initial coefficient+1. The vectors have disjoint supports and form exactly the integer fixed lattice R^H: an invariant integral coefficient vector is an arbitrary integer multiple of each consistent signed indicator. No index or denominator saturation is missing from this basis. Their Q-span is the fixed field L=K^H. Fundamental Galois theory gives [L:Q]=g=n/h.

For completeness d_H can be computed without using the forthcoming root identity. Let V be the integer n by g matrix of signed indicators and clear denominators in A_o^-1V: choose s>0 so C=s A_o^-1V is integral. Then

    J_o intersect R^H = V {z∈Z^g : Cz≡0 mod s}.

An exact Smith form of the full-rank n by g matrix C gives diagonal entries c_1,...,c_g. Unimodular row and column operations preserve the congruence problem, so

    d_H=product_(i=1)^g s/gcd(s,c_i).

Normal forms, inversion and gcds have polynomial bit complexity; the accepted RH M1 normal-form input is sufficient at its exact scope. Log d_H<=log D_o because reduction V→R/J_o has image of orderd_H. A common denominator, all matrices and their normal forms have polynomial bit size in the complete original input. No loop of lengths or numeric Gaussian widths is hidden here.

## Why the contracted index is a root of D_o

Every rational prime supporting J_o is odd and is unramified in K/Q, hence also in K/L. In a Galois extension K/L with groupH, H acts transitively on the primes over a given prime of L. Since J_o is H-invariant, its exponents are equal on each such orbit. Relative ramification indices are1, so there is an integral L-ideal I with

    J_o=IR,    I=J_o intersect O_L.

This is immediate from the prime-ideal valuation factorizations: assign to the contracted prime the common exponent of its orbit. Since O_L=R^H, its index is [O_L:I]=d_H. Taking absolute norms of ideal extension gives

    D_o=N_K(IR)=N_L(I)^[K:L]=d_H^h.

The exact Galois transitivity and norm-extension inputs are Milne Theorem3.34 (proof) and Proposition4.1(a), read at primary PDF printed pp.59–60 and69. The power-of-two ramification input is Proposition6.2, already checked in primary-source-check-v1.md. These facts are used as algebraic identities, not as algorithms that factor the input. Because D_o<=D<=2^(rho n), the identity gives d_H<=2^(rho n/h)=2^(rho g)<2^g.

## Effective collision and decoding

Put t=ceil(log2(d_H+1))<=g. The2^t binary sums of b_1,...,b_t are all distinct because the signed indicators are independent. They have onlyd_H residues modulo J_o. Enumerating d_H+1 of them and comparing exact keys A_o^-1v mod Z^n gives a collision. Its nonzero difference v has coefficients in{−1,0,+1}, since the basis supports are disjoint, and therefore ||v||²<=n. Multiplying by a produces f∈J and norm<=2sqrt(n). Costs are polynomial in numericd_H and full input bits, with O(d_H) keys; neither an ordinary short basis nor a short member is assumed in advance.

For T=lambda+w, the coefficients of fw have magnitude at most ||f||₂||w||₂<=2sqrt(n)r<1/2 by negacyclic Cauchy–Schwarz and Parseval. The exact product f lambda is integral. Thus rounding fT yields f lambda, and field division gives lambda. The stronger explicit DD radius bound

    r<1/(8192 n⁴ K ceil(sqrt(Kn))ell²)

from source-classification-proof-v1.md is strictly less than1/(4sqrt(n)) for n>=2. All arithmetic is rational; off-promise behavior is irrelevant to promised correctness.

For J=mathfrak p^b with p odd, an automorphism fixes J if and only if it fixes mathfrak p, so H is exactly the decomposition group. Its order is the residue degree f_res because p is unramified. Hence d_H^f_res=D=p^(b f_res), giving d_H=p^b. The quotient exponent is also p^b by valuation of pR. The prime-ideal special case b=1 matches the separately frozen direct Frobenius proof. For pure2-primary J, m=1 and J_o=R, so H is the whole group and d_H=1.

## Scope and mandatory challenges

The theorem gives a publicly computable numerical invariant d_H and an actual decoder when that invariant is polynomial value. Its ordinary-input acquisition step is the substantive difference from existential-short-vector or supplied-generator criteria. It does not prove that all eligible ideals have polynomial d_H. Generic split primes have f_res=1 and d_H=p, leaving superpolynomial p outside the polynomial guarantee. Likewise composite ideals may have trivial stabilizer. No source-hardness conclusion is inferred from these failures.

Review should target: signed-orbit consistency and integral saturation; equality of containment and automorphism stability; removing2 with m rather than2; unramified descent versus the excluded ramified step; Smith congruence index; numeric costs; and the exact DD radius. Full/blind review remains required for these exact bytes.
