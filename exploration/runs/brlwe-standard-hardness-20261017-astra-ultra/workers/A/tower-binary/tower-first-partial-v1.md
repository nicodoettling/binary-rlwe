# A-TOWER v1: radix encoding in an actual cyclotomic tower

Status PROVISIONAL. Exact endpoint calculation and scoped obstruction; no independent review completed. Source computational hardness remains OPEN. The assignment is preserved in assignment-v1.md.

## 1. Rings, parameters, and complete oracle law

Let n>=2 and r>=2 be powers of two, N=nr, and

    R=Z[X]/(X^n+1),
    S=Z[Y]/(Y^N+1).

The inclusion R->S sends X to Y^r. It is well defined because (Y^r)^n+1=Y^N+1. Every element of S is uniquely sum_(j=0)^(r-1) Y^j z_j(X), z_j in R. This is a free rank-r R-module and an actual power-of-two cyclotomic extension. The relation is Y^r=X, not Y^r=2^r.

Take a supplied prime q congruent to 1 modulo 2N. Thus q splits both rings and q>=2N+1. Polynomial q in N and also q of polynomial bitlength are meaningful parameter cases; no unproved efficient prime-family search is assumed. Standard base RLWE inputs are iid uniform a_i in R_q with responses b_i=a_i s+e_i, one common uniform s in R_q, and the exact declared iid coefficient error law mu. Their comparator has iid uniform responses. There may be polynomially many such input samples.

The desired target recovery oracle is over S_q. Its samples have iid uniform full-ring A_l in S_q, one fresh uniform coefficient-binary secret Z in {0,1}^N, and iid coefficient D_sigma errors G_l, independent jointly of all multipliers and Z. Write

    A_l=sum_j Y^j A_lj,   Z=sum_j Y^j Z_j,

where all Nr coefficients of A_l and all N bits of Z have their required independent laws. Its responses must contain ALL r blocks:

    B_lk = sum_(j=0)^k A_lj Z_(k-j)
           + X sum_(j=k+1)^(r-1) A_lj Z_(r+k-j) + G_lk.    (1)

Each G_lk has n independent coefficient D_sigma entries, independently across k,l. Every multiplication in (1) is in R_q and the factor X is essential.

For r=2 this is

    B_0=A_0 Z_0+X A_1 Z_1+G_0,
    B_1=A_1 Z_0+A_0 Z_1+G_1.                              (2)

## 2. A completely simulatable tower endpoint, with the wrong secret

Grouping r independent base samples per target row gives

    A_l=sum_j Y^j a_lj,
    B_l=sum_j Y^j b_lj = A_l embed(s)+E_l.

This has EXACT iid uniform full-ring multipliers, exact uniform full-ring comparator, and, when mu=D_tau, exact iid coefficient D_tau errors in the extension. The source budget is r times the number of output rows. The common secret is embed(s), uniform on the n-dimensional subring and supported only on extension block zero. It is not a fresh N-bit binary secret. Merely calling this secret a digit vector changes the product and loses (1).

## 3. Radix digit law: defect and an honest entropy repair

The radix map is the R_q-linear map

    G_2(sum_j Y^j Z_j)=sum_j 2^j Z_j mod q.                (3)

If 2^r>=q, the canonical r-bit expansion of each coefficient of uniform s is uniform on q strings rather than all 2^r strings. The joint digit vector is uniform on q^n strings, and its total variation distance from uniform N-bit Z is exactly

    1-(q/2^r)^n.                                         (4)

Leading zero padding generally makes this worse; it does not make the bits independent.

There is a legitimate distributional repair that does not require the reduction to know s. Put M=floor(2^r/q)>=1. For each base coefficient choose a known independent k_t uniform in {0,...,M-1}, and define the latent integer x_t=s_t+q k_t, using the standard lift s_t in {0,...,q-1}. Let Z be its r-bit encoding. Then x_t is exactly uniform in {0,...,qM-1}, the coefficients are independent, G_2(Z)=s, and

    TV(Law(Z),U({0,1}^N))
       =1-(qM/2^r)^n <= n q/2^r.                         (5)

The reduction knows k but need not know x or Z; a recovered Z would reveal s through (3). With r the next power of two above log_2 q+ceil(log_2 n)^2, this loss is negligible and N remains polynomial for polynomial-bit q. This repairs the SECRET LAW only. It supplies no missing target responses.

## 4. Radix evaluation is not a ring homomorphism

Direct calculation in the actual tower gives

    G_2(Y Z)=2G_2(Z)+(X-2^r)Z_(r-1).                     (6)

In particular G_2(Y^r)=X whereas G_2(Y)^r=2^r. Since n>=2, X is not the scalar 2^r in R_q. Replacing the relation by Y^r=2^r would change the ring. The polynomial Y^r-2^r also has different algebraic structure and is not the stated cyclotomic extension.

Suppose target response programming uses arbitrary many base responses by public R-linear/extension-linear combinations and adds noise independent of s. Its secret-dependent part in one extension output is necessarily

    C s,   C in S_q,

because sum_i C_i b_i has secret part (sum_i C_i a_i)s. If it were to match A Z for every digit vector with s=G_2(Z), then Z=1 gives C=A and Z=Y gives

    A(Y-2)=0 in S_q.                                    (7)

Equivalently the full twisted-circulant multiplication matrix must factor as the rank-one R_q matrix c(1,2,...,2^(r-1)). More source samples merely change C; they do not change this factorization requirement.

The CRT consequence is exact. Since Y^N+1 splits simply,

    dim_Fq Ann_(S_q)(Y-2)
      = 0 if 2^N+1 is nonzero mod q,
      = 1 if q divides 2^N+1.                            (8)

In the exceptional case A is supported only at the single CRT root Y=2. Hence a uniform full-ring A satisfies (7) with probability q^(-N) or q^(1-N), respectively. It is not a uniform extension multiplier. No replacement of 2 by a formally named variable removes this constraint.

The same exact restriction survives the randomized lift in (5), even if response coefficients and added offsets depend on the known k. Fix k and all public multipliers. On one base coefficient, s runs over q consecutive integers x=qk,...,qk+q-1. Because q>=17 here, this interval contains both a binary increment 00->01 and an increment 01->10. For an affine source response C s+d, both increments are the same C. For the required product A Z they are A and A(Y-1), respectively (multiplication by the relevant X^t is invertible). Equating them again gives (7). Thus knowing the lift interval does not linearize binary carries.

## 5. Known independent noise cannot repair these affine responses at useful width

The following is a quantitative version for the concrete affine programming class. Assume A is uniform S_q conditional on the known lift k, public-programming choices are independent of the unknown base secret, and one target response has the form

    B=C s+V,

where C may depend on all public data and k, and V has ANY distribution independent of s conditional on those data. It may contain arbitrary linear combinations of the ordinary source errors and extra known noises. This grants more freedom than simply adding a Gaussian. The desired recovered secret remains the digit vector Z of (5).

Let K>=1, 4K<(q-1)/2, and consider the event that every centered coefficient of the actual target error B-AZ has absolute value <=K. Fix one base coefficient s_t and all others, public data, k, and V. Every triple of consecutive integers

    x=4h, 4h+1, 4h+2

inside its lift interval has low-bit patterns 00,01,10 and unchanged higher bits. The second finite difference of Z across the triple is X^t(Y-2). The affine source term and the fixed V have zero second difference. Therefore, if all three target errors were in the K-box, every centered coefficient of A X^t(Y-2) would be in the 4K-box. Multiplication by X^t=Y^(rt) is a signed coefficient permutation, so it preserves the box.

There are at least floor((q-3)/4) disjoint such triples in every interval of q consecutive integers. Consequently, whenever A(Y-2) lies outside the 4K-box, at least the fraction

    c_q=floor((q-3)/4)/q

of the possible s_t values yield an error outside the K-box. For q>=17, c_q>=3/17.

If Y-2 is a unit, A(Y-2) is uniform S_q. If it is a zero divisor, its image is the codimension-one subspace of polynomials vanishing at 2; any N-1 coefficient coordinates parameterize that subspace bijectively. In both cases,

    Pr[A(Y-2) belongs to the 4K-box]
       <= ((8K+1)/q)^(N-1).                              (9)

Thus the actual affine-programmed joint law satisfies

    Pr[||center(B-AZ)||_infinity>K]
       >=c_q [1-((8K+1)/q)^(N-1)].                      (10)

For the required target joint law with iid coefficient D_sigma errors, K=max(1,ceil(sigma ceil(log_2 N))) gives tail delta_target<=N exp(-pi ceil(log_2 N)^2)/(pi ceil(log_2 N)). If sigma>=1 and q/sigma>=N^c for fixed c>0, the right side of (10) is asymptotically at least 3/17-o(1). Hence its distance from the required joint (A,Z,B) law is at least 3/17-o(1)-delta_target. This rules out a negligible joint-law repair by independent noise within this explicit affine class. It is not a theorem against arbitrary nonlinear response processing or every possible encoding.

The uniform-A condition is conditional on the known lift. A scheme that correlates A with that lift must separately prove the target requirement that A and the binary secret are independent; it is not covered silently by this calculation.

## 6. Exact comparator bookkeeping for affine response maps

With h base responses and m extension outputs, a public affine map has an F_q-linear response matrix H:R_q^h->S_q^m. Conditional on H and added independent offsets, the uniform comparator is uniform on an affine translate of im H. If H is surjective, its output is exactly uniform S_q^m and h>=rm is necessary. The grouping construction in Section 2 realizes this endpoint exactly.

If H is not surjective, independent extra noise can change its marginal law, but exact uniformity does not follow from the source comparator alone. In every case the planted secret-dependent part of each output is C_l s, which is why even a perfectly uniform comparator does not solve Sections 4-5. The failure is not a mere count of available source samples.

## 7. A genuine algebraic repair, and its remaining missing coordinates

Since q splits S, one can choose gamma in R_q with gamma^r=X: at each base CRT root choose one of its r extension-root preimages and interpolate. Then

    phi_gamma:S_q->R_q, Y->gamma,

is an actual R_q-algebra surjection. The map sum gamma^j Z_j is not scalar binary radix encoding. Its distribution for uniform binary Z and an efficient coupling to uniform source s would need a new proof; (5) does not apply to it.

Even granting that source-secret coupling, a base sample supplies only the projection

    phi_gamma(B)=phi_gamma(A)s+e.

It does not supply the other N-n response coordinates. Restricting A to Ann(ker phi_gamma) makes A Z determined by phi_gamma(Z), but confines A to an n-dimensional ideal rather than the full N-dimensional ring. Multiplying by public units preserves that ideal support.

Alternatively, lift a uniform base multiplier to a uniform A in its phi_gamma fiber, and lift the base response using fresh uniform randomness in ker phi_gamma. The comparator is then exact uniform full-ring. On the planted side, conditional on A,Z and the projected error, the resulting error is uniform in an affine coset of ker phi_gamma, which has q^(N-n) elements. Its probability of the coefficient K-box is at most

    min(1,(2K+1)^N/q^(N-n)).                             (11)

When r>=log_2 q, (11) is at most [2(2K+1)/q]^N and negligible at the useful target width. Thus uniform completion of the missing coordinates gives the wrong error law. A genuine homomorphism fixes the algebra but not response completion.

## 8. Next repair to test, rather than an asserted solution

A concrete remaining repair would start from a binary module-secret source over R and obtain, for each random extension A, the r CORRELATED module rows equal to the twisted-circulant multiplication matrix in (1), all with one common binary block secret and independent small errors. That would supply exactly the missing responses. Passive standard module-LWE gives independent random rows, and those rows are not automatically twisted-circulant. Selecting or programming the required correlated rows needs an actual reduction with its error cost; the correlation cannot be supplied by renaming the module as a ring.

As a primary-source orientation check, Boudgoust, Jeudy, Roux-Langlois and Wen prove a binary-secret MODULE rank expansion and explicitly retain the ring degree. Their construction does not state that the random module rows are circulant; their paper separately identifies rank one as the ring case. D is auditing the exact source restrictions and related rank-switching literature. [Author PDF, introduction and Theorem 1](https://cjeudy.github.io/assets/pub/BJRW21_Hardness_bin-MLWE.pdf).

The next precise target is therefore a small-noise correlated-row simulator, or a valid recovery-oracle construction for those rows. This is a constructive missing object, not an extra hardness assumption imported as a completed foundation.
