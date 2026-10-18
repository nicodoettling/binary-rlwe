# Quotient gadgets and the low-index fractional source

Status: PROVISIONAL mechanism analysis, not a hardness theorem. Primary locations: Definition3.27/Lemma3.28 and the full encoding equations(20)–(30) in Lemma4.5 of the supplied PDF.

## 1. Two exact small-quotient correspondences

For every integral ideal J, J subset R gives a SuperSVP-style lattice pair with target J, superlattice R, one copy, coefficient superlattice basis I_n, and quotient size D=N(J). This is a restricted IDEAL instance of the paper's general worst-case problem. It does not inherit hardness from the unrestricted problem. Its elementary available solution is m times a unit coefficient vector, where m is the exponent of R/J; using D instead of m may overstate even this elementary bound.

For the fractional source, R subset Lambda=J^-1 and Lambda/R has the same size D. Smith normal form computes generators u_j and invariant factors d_j. Its quotient gadget has k_Gamma=sum_j ceil(log_2 d_j)<=2log_2 D binary columns. This arithmetic is already compatible with B's public Gaussian bridge, which samples invariant factors without enumerating D cosets.

There is a useful explicit bounded-representative version. For every bit position b of invariant factor d_j, reduce 2^b u_j modulo R into the coefficient cube[-1/2,1/2)^n and call the result c_(j,b). Then for every coset u+R there is an efficiently computable bit vector z of length k_Gamma with

    u = sum_(j,b) z_(j,b)c_(j,b) + v,    v in R,

after choosing u's representative in the same cube. Each c_(j,b) has coefficient norm at most sqrt(n)/2, and the carry v has coordinate magnitude at most(k_Gamma+1)/2. This is an exact finite quotient encoding with polynomial-sized carries. It is not a Gaussian distributional identity; uniform invariant-factor values do not imply independent uniform encoding bits when d_j is not a power of two.

## 2. The small quotient is not the full challenge quotient

The fractional challenge is reduced modulo qLambda. That quotient has order q^n, irrespective of D. The denominator quotient Lambda/R has order D. Encoding the latter does not give short preimages for arbitrary elements of Lambda/qLambda, nor for arbitrary CRT syndromes in R_q/I_T.

With only k_Gamma binary columns, at most2^k_Gamma output classes can be represented. Any additional bounded integer carry must be counted separately. In particular a fixed fractional ideal has at most D(2B+1)^n points in a coefficient box[-B,B]^n, up to the elementary integer-endpoint rounding adjustment. If that quantity is negligible compared with q^n, a uniform residue has no such bounded lift except with correspondingly small probability. A gadget representation of the small quotient does not invert this sparse image.

The primary paper explicitly retains the other contributions. Its corrected residual is encoded by an integer z1 after a scale p and by a signed binary z2 for the remaining integer rounding error. The small quotient bits z3 alone do not encode a general target. Omitting z1,z2 would remove the part of the paper's construction that pays for the full target space.

## 3. Where the paper's full construction stops being a standard ring construction

In primary Lemma4.5, Gaussian vectors V in J/q are converted to an ordinary matrix A0=qB_J^-1 V. Its columns are independently sampled. That is a general-matrix distribution. Requiring n columns to be rotations of one ring vector changes their joint law; the result is not an independent uniform matrix. Conversely, keeping the columns independent does not give a rank-one ring multiplication matrix.

One can regard J as a rank-one projective R-module, but writing its elements in an arbitrary integer basis does not make that basis the power basis of R. Multiplication is represented by conjugated ideal-module matrices. Changing back to the standard ring representation transports the secret and error through the basis change. A binary secret in the original coefficient basis need not remain binary, and the noise norm must be charged.

For example, choosing a public u in J that is a unit modulo q identifies J/qJ with R_q by multiplication by u^-1. Such an identification exists when J and q are coprime, but a small usable norm for u and u^-1 is a separate geometric/algorithmic requirement. Choosing the always available scalar u=D generally gives the fractional ideal D^-1J, whose denominator ideal D J^-1 has index D^(n-1). This need not satisfy the original low-index binary budget. No short principal generator or favorable module isomorphism is supplied for free.

The triangular ring lemma repairs a PUBLIC EXTRACTION step once a ring-decomposed input has already been specified. It does not repair these basis, source-law, or secret-law changes in the worst-case construction. In particular the general SuperSVP theorem cannot be imported by replacing each scalar with a ring element.

## 4. Present contribution

The paper's quotient accounting is directly useful: it isolates exactly log D bits of denominator data, uses computable canonical quotient coordinates, and keeps the residual/carry and Gaussian hint law explicit. This supports clearer intermediate source definitions. It currently gives neither a new standard hardness premise for B's fractional source nor an efficient short-preimage solver for the externally supplied ring challenge. Any proposed SuperSVP-based ideal/module analogue must state its new worst-case restriction, public hint, target representation, and all secret/noise changes separately.
