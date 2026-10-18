# H relation test: an executable LLL combination and its actual guarantee

Status PROVISIONAL author analysis. This is ONE constructive escape test for the existing restricted DGS interface. It is not a new hardness assumption, a general impossibility theorem, or a claim that LLL fails on typical inputs. All source/comparator laws are the exact laws (C3)-(C4) in shifted-cosets-v1.md, including retained X values, residue-conditioned normalizers and FAIL.

## 1. Executable integer-relation algorithm

Fix I,F,s as in H-ALIGNv1 and choose 1<=m<=n. Obtain m fresh independent original X_j~D_(F,s), without rejecting zero or conditioning on rank. Let S be their n-by-m coefficient matrix and A_j=X_j mod I in V=R/I. If rank_Q(S)<m, output FAIL. Otherwise construct the full integer relation lattice

    L_A={c in Z^m: sum_j c_j A_j=0 in V}.              (R1)

It contains p Z^m, where p is the residue characteristic, so it has full rank. By the first isomorphism theorem,

    det(L_A)=[Z^m:L_A]=h_A=|<A_1,...,A_m>_add|<=M.    (R2)

More precisely, M=p^f and h_A=p^r for the F_p-linear rank r of the residue columns. It equals M only when these columns span V over F_p; replacing h_A by M everywhere as an equality would be false. Compute L_A by ordinary HNF/SNF on the integer congruence system defined by I's basis and the columns S. This requires polynomial bit complexity and no factoring oracle, short ideal basis, uniform-residue promise, or SIS oracle.

Run standard LLL with Lovasz parameter3/4 on L_A and take its first vector 0!=c in Z^m. Output Y=S c. It lies in F and reduces to zero modulo I, hence Y belongs to F intersect I=FI. On the rank-passing branch it is nonzero, because S is injective over Q. Return the coefficient vector Y and, if the replacement mechanism is desired, compute C=(Y)F^-1 and the exact integer-cleared ideal as before. Norm descent/eligibility remains an additional test, never an automatic consequence of Y in FI.

This algorithm is finite apart from the conditional DGS interface. If approximate oracle outputs can be off-lattice, verify X_j in F and return FAIL on such outputs. Their total statistical effect is charged by the full-kernel TV budget. No rank-conditioned oracle law is substituted into the proof.

## 2. Exact LLL constant and source check

The original [LLL preprint, section1](https://ir.cwi.nl/pub/9304/9304D.pdf), conditions(1.4)-(1.5), Proposition(1.6), equation(1.9), uses coefficient Euclidean length and parameter3/4. Proposition(1.26) gives polynomial bit complexity for integral bases. This primary source was opened and checked; the version has36 PDF pages, and the relevant printed pages are3–5 and11–12. The formula is also derived here, so no unexplained change between squared and ordinary norm is imported.

For an LLL-reduced basis b_1,...,b_m, size reduction and the Lovasz condition imply ||b_i^*||^2>=(1/2)||b_(i-1)^*||^2. Thus

    h_A=product_i ||b_i^*||
        >=||b_1||^m 2^(-m(m-1)/4).

Consequently the computed c=b_1 satisfies

    ||c||_2 <=2^((m-1)/4) h_A^(1/m).                  (R3)

The primary polynomial-time claim applies directly because L_A is an integral full-rank lattice in Z^m. Its HNF can be represented with bit length polynomial in m and log h_A, and the input quotient computation is polynomial in the given ideal/sample bit lengths. The binary length, rather than the numerical size of M or p, controls those arithmetic costs.

## 3. Nonzero output and the original wide-sample law

A separate probabilistic argument is needed to justify passing the rank check. Existence of a relation does not itself imply Y!=0.

There exists a nonzero f in F of coefficient norm <=sqrt(n)D_F^(1/n), by applying Minkowski to the coefficient cube and passing to the closed boundary. Its n negacyclic rotations lie in F, have the same length and are Q-linearly independent. This is an existence argument, not short-basis advice. Therefore, for every proper real linear subspace H of R^n, some v in F outside H has

    ||v|| <=sqrt(n)D_F^(1/n)<2sqrt(n).

The lines x+Z v for x in F intersect H are disjoint subsets of F. Completing the square on each line gives

    sum_(k in Z) rho_s(x+k v)
      =rho_s(proj_(v-perp)x) rho_(s/||v||)(Z+alpha_x)
      >=rho_s(x) s/(2||v||),                          (R4)

provided s/||v||>=1. The last scalar inequality is uniform in the actual center alpha_x: scalar Poisson gives a lower bound u[1-2sum_(k>=1)exp(-pi u^2 k^2)]>=u/2 for u>=1. Indeed the omitted sum is at most 2exp(-pi)/(1-exp(-3pi))<1/2. This retains the center-dependent normalizer and uses a uniform bound, rather than declaring it constant.

Summing (R4) over x in F intersect H yields

    Pr[X in H] <=2||v||/s <4sqrt(n)/s                 (R5)

when s>=2sqrt(n). For each fresh sample, conditional on the COMPLETE previous samples, their span is a fixed proper subspace while j<=m<=n. A union bound therefore gives

    Pr[rank_Q(S)<m] <=4m sqrt(n)/s.                    (R6)

No posterior independence after rank screening is used. At the actual s>=512n^2, the right side is at most1/(128sqrt(n)). A Gaussian coordinate moment bound, derived by completing the square and using the centered-theta maximum, also gives

    Pr[exists j: ||X_j||>s sqrt(n)L] <=2mn exp(-pi L^2). (R7)

Here L>0 is a declared tail parameter. Both bad events are retained; their unconditional masses are added. Per-call conditional implementation errors contribute their additional hybrid sum. The source tails and ranks are not inferred from the uniform-residue comparator. This proof is uniform in F and does not require computing f or v.

## 4. Norm transfer supplied by this algorithm

On the complement of the two bad events, Cauchy-Schwarz and (R3) give

    ||Y|| <=||c||_2 (sum_j||X_j||^2)^(1/2)
           <=s sqrt(mn)L 2^((m-1)/4) h_A^(1/m).       (R8)

The resulting normalized certificate is

    ||Y||/M^(1/n)
      <=G_A:=s sqrt(mn)L 2^((m-1)/4)
                                      h_A^(1/m)/M^(1/n).       (R9)

Since lambda_1(I)>=M^(1/n), G_A is a valid ideal-SVP approximation certificate on that branch. This is the directly useful endpoint; a second DGS call is unnecessary if G_A is already polynomial.

There is also a corresponding replacement-distortion certificate. Because Y in FI, |N(Y)|>=D_F M, and ||M_Y||_op<=sqrt(n)||Y||. The distortion in A's replacement formula therefore satisfies

    b(Y)D_F^(1/n)
       <=sqrt(n)||Y||/M^(1/n) <=sqrt(n)G_A.            (R10)

Thus polynomial relative output norm would give a polynomial geometric transfer. It would still not guarantee that denominator clearing makes I'' eligible or even strictly smaller. All factors of C and the exact scalar d matter. Multiplying an arbitrary old point by p is a simple warning against equating congruence with descent.

## 5. Actual-wide-width parameter intersection

Assume the actual finite chain supplies polynomial absolute s, as in the polynomial-VALUE modulus regime specified in parameters-v1.md, and choose polynomial m,L. The factor s sqrt(mn)L is then polynomial. To get a polynomial certificate from the WORST-CASE h_A=M substitution, one must control

    g_m=2^((m-1)/4) M^(1/m-1/n).                      (R11)

For m=O(log n), the first factor is polynomial, but the second is polynomial only in the restricted range log M=O(m log n)=O(log^2 n), up to fixed polynomial exponents. For the target prime inputs M>2^(rho n) with fixed rho>0, this sufficient range is absent. The restriction is even stronger when the desired factor is a preassigned polynomial rather than an unspecified one.

No other m<=n fixes the worst-case certificate. Put a=log(2)/4 and z=log M. Then

    log g_m=a(m-1)+z(1/m-1/n).

For m<=n the coefficient of z is nonnegative, so for z>=rho n log2 its minimum is bounded below by

    a(m-1)+(rho n log2)/m-rho log2
      >=2sqrt(a rho n log2)-a-rho log2
       =(log 2) sqrt(rho n)-(log 2)/4-rho log 2.        (R12)

This is Omega(sqrt(n)) for fixed rho>0. The continuous optimizer for z of order n is m of order sqrt(n), giving a subexponential rather than polynomial guarantee. At m=n, (R11) is the familiar2^((n-1)/4). These are LOWER BOUNDS ON THE NUMERICAL WORST-CASE UPPER CERTIFICATE g_m, not lower bounds on the actual output of LLL or on the shortest relation. An instance can perform much better; the present guarantee does not prove that it does.

The h_A=M case is real, not an unjustified universal equality. When I has residue degree f=1, every nonzero residue already generates its additive group. Thus h_A=M unless all A_j=0. Under the actual original iid source the exceptional probability is pi(0)^m, at most b^m by(C2). This product is under the declared original iid law, before any selected conditioning. For larger f, h_A is an actual random rank parameter; lower values may improve(R9), and no adverse rank distribution is asserted without calculating it.

The method does not intrinsically use the extra oracle power: setting F=R and taking m independent coordinate unit vectors deterministically gives the same h<=M relation lattice and no rank/tail loss. Its output obeys ||Y||/M^(1/n)<=g_m. This deterministic baseline can achieve the same subexponential certificate in moderate-index ranges. The present wide Gaussian samples multiply that worst-case guarantee by s sqrt(mn)L. Hence this test has not established a new arbitrary-ideal implication from the restricted DGS oracle.

## 6. Why taking more than n samples is not a free repair

For m>n, rank_Q(S)<=n, so the exact integer kernel K_0={c in Z^m:S c=0} has rank at least m-n and is contained in L_A. Nonzero vectors in K_0 satisfy every modular relation but output the zero ring element. The guarantee(R3) concerns LLL's first short coefficient vector and does not ensure it lies outside K_0. Making M^(1/m) smaller while ignoring this kernel is invalid.

The smallest hand control already exposes this: for any nonzero x in F, take X_1=X_2=x. The coefficient vector(1,-1) is a nonzero, short congruence relation, but its ring output is0 for every I. A ring-linear analogue is (c_1,c_2)=(X_2,-X_1), also always zero. Gaussian sampling assigns equal-vector events positive mass, and m>n forces exact dependencies regardless of equality.

One may compute a basis of L_A and search its image, or quotient out K_0, but then the relevant problem is shortness in the image seminorm c ->||S c||, subject to S c!=0. The image is

    S(L_A)=S(Z^m) intersect FI,

a lattice of rank at most n. If S(Z^m) has full rank, its determinant is bounded above by the product of lengths of any n independent sample columns, at most(s sqrt(n)L)^n on the tail event. The image has index at most M in S(Z^m), so direct n-dimensional LLL gives at best the general certificate

    ||Y||/M^(1/n) <=2^((n-1)/4) s sqrt(n)L.            (R13)

This statement is only a conservative bound, not a claim that it is tight. Saturating all the way to the known ideal F merely returns the ordinary basis of FI, whose generic LLL factor is likewise exponential in n. No m>n polynomial relation guarantee follows from the determinant-M observation alone.

## 7. Trivial scalar relations, existence, and the precise remaining target

For every I over p, c=p e_j is an executable relation, giving Y=p X_j. Its relative norm on the sample tail event is at most

    s sqrt(n)L p/M^(1/n)=s sqrt(n)L p^(1-f/n).         (R14)

The ideal itself already contains the scalar p, with relative norm p^(1-f/n). Therefore cases where this ratio is polynomial have a simple deterministic baseline and do not demonstrate new oracle power. Conversely, large p and small residue degree can make it nonpolynomial. The special principal ideal I=(p), when prime, is also easy; it cannot serve as a universal obstruction example.

Pigeonhole arguments can produce coefficient relations when a bounded coefficient box has more than M points, but enumerating that box may be exponential. They also need nonzero IMAGE, not merely nonzero coefficients. Neither that witness argument nor finite-field Gaussian elimination yields a general short integer lift: elimination can output coefficients of size p.

The next missing problem for this exact route is therefore:

    From ordinary I,F and original iid X_j~D_(F,s), find with
    inverse-polynomial original success probability a coefficient vector c
    satisfying 0!=S c in FI and ||S c||<=poly(n,log M) M^(1/n),
    in time polynomial in the stated input length, at the actual delivered s.

All zero, rank, selected-branch and TV losses must be charged under(C3). One sufficient certificate would be ||c||_2<=poly(n,log M)M^(1/n)/(s sqrt(mn)L) together with a nonzero-image guarantee, but the direct image norm is the actual requirement. No algorithm meeting it was established here. Adding it as a new SIS/short-relation assumption would add an unproved foundation; it is not licensed by mere kernel existence or the conditional restricted DGS interface.

This conclusion is scoped to the analyzed integer-relation/LLL certificate and its stated baseline. It does not exclude other correlated oracle queries, stronger reduction algorithms, or a different family-transfer mechanism. Existing balanced-product and tower routes have not been reintroduced.
