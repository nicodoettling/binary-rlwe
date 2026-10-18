# A-SCALAR v1 proof and audit obligations

Status PROVISIONAL. Exact claim file: scalar-theorem-v1.md. The arguments below are new A-authored mathematics except the cited LLL algorithm and complexity theorem. Independent review is required.

## 1. Quotient law and exact kernel

For every fixed T, pi_T is a surjective F_q-linear map, so its value on each independent uniform ring element is independent uniform F_q^r. The scalar matrix A therefore has independent uniform entries, even though the underlying ring has n coefficients. The designated syndromes are iid uniform and independent of A. Mixing any sample-independent law of T preserves these conditional statements.

Expose rows of A. Conditional on i independent prior rows, the next row lies in their span with probability q^(i-D). A union bound gives rank failure at most sum_(i=0)^(r-1)q^(i-D)=(q^r-1)/(q^D(q-1)). This also follows from the exact full-rank probability product_(i=0)^(r-1)(1-q^(i-D)).

After invertible row operations and a column permutation, the equations are x_p+C x_f=0 mod q. Every integer solution is uniquely x_p=qz-Cx_f, which proves the displayed K is a lattice basis. Its triangular block determinant is exactly q^r. A centered lift of the transformed target gives the specified particular vector v.

Determinant alone does NOT imply a covering bound det(Lambda)^(1/D). For example A=[1,0] modulo q=101 yields Lambda=101Z x Z, and target (50,0) has distance 50 although det(Lambda)^(1/2)=sqrt(101). The next argument establishes average-case existence separately.

## 2. Exact collision identity and simultaneous existence

Let X be uniform on {-B,...,B}^D, a set of H distinct vectors modulo q. For any two distinct box vectors x,y, their difference is nonzero modulo q; hence Pr_A[A(x-y)=0]=q^(-r). Consequently

    E_A sum_z Pr[AX=z|A]^2 = 1/H+(1-1/H)q^(-r),
    E_A chi^2(Law(AX|A),U(F_q^r))=(q^r-1)/H.

The total variation distance is at most half the square root of chi^2. Jensen's inequality bounds its expectation by eta_r. For fixed A, the uniform probability of a syndrome outside the box image is no greater than that total variation distance, since the box-image distribution assigns zero mass there. Therefore each independent designated syndrome has no box preimage with probability at most eta_r, averaged over A. A union bound over m targets gives m eta_r; no independence of these failure events is assumed. Adding rank failure gives rho_r. This only proves existence, which is used as a premise for the actual nearest-plane approximation below.

## 3. Babai approximation with explicit factor

Let b_1,...,b_D be a delta=3/4 LLL-reduced basis, with Gram-Schmidt vectors b_i*. Size reduction and the Lovasz condition imply ||b_i*||^2<=2^(j-i)||b_j*||^2 for i<=j. Babai's backwards nearest-plane rounding leaves every final orthogonal coefficient in [-1/2,1/2].

Let w be its output on v, and w_opt a closest lattice point. If they coincide there is nothing to prove. Otherwise let j be the largest basis index at which their integer basis coefficients differ. At steps above j the subtractions agree, so the residual projection onto b_j* before rounding is common. Because Babai chooses a nearest integer at that step, the different integer chosen by w_opt leaves a b_j* coefficient of absolute value at least 1/2. Thus dist(v,Lambda)^2>=||b_j*||^2/4.

The components of v-w and v-w_opt above j agree. The squared norm of the former's components at indices <=j is at most

    (1/4)sum_(i<=j)||b_i*||^2
       <=(2^j-1)||b_j*||^2/4
       <=(2^j-1)dist(v,Lambda)^2.

Adding the common higher-component norm, bounded by dist(v,Lambda)^2, gives ||v-w||<=2^(D/2)dist(v,Lambda). Fixed deterministic tie breaking is harmless. A box solution is an element x=v-z with z in Lambda and ||x||<=sqrt(D)B, so Babai's output passes the squared-norm check whenever such a solution exists. Cauchy-Schwarz gives ||x||_1<=Gamma D B.

## 4. Polynomial bit complexity

Use centered or nonnegative lifts of C. Each initial basis vector has squared norm at most Dq^2; its entries and the particular targets have O(log q) bits. Proposition 1.26 of the original LLL preprint gives O(D^4 L) integer arithmetic operations on O(DL)-bit integers and O(D^6 L^3) bit operations with classical arithmetic, for L=ceil(log_2(2Dq^2)). This is the only imported quantitative algorithm theorem here. [LLL primary preprint, Proposition 1.26, printed pp.11-12](https://ir.cwi.nl/pub/9304/9304D.pdf).

For completeness, a deliberately loose exact-rational Babai implementation remains within the claimed polynomial bound. The output integer basis has O(DL)-bit coordinates. Every Gram matrix entry then has O(DL) bits; a minor of order at most D has O(D^2 L) bits by the determinant expansion/Hadamard bound. Exact Gram-Schmidt coefficients and vectors are ratios of these minors or equivalent Schur complements, so reduced numerators and denominators have O(D^2 L) bits. They can be computed by rational Gaussian elimination with reduction, or fraction-free elimination followed by division, in O(D^3) arithmetic operations on polynomially bounded integers. The ordinary Euclidean gcd and classical multiplication/division give a conservative O(D^9 L^3) budget including this setup.

Babai's backwards integer coefficients also have polynomial bitlength. The triangular basis change has rational entries bounded in bitlength as above; solving it on the O(log q)-bit target bounds exact real coordinates by 2^(O(D^3 L)), and backwards rounding propagates at most a further product of D size-reduced coefficients (each at most 1/2) and additions. Equivalently, the recurrence |c_i|<=|t_i|+(1/2)sum_(j>i)|c_j|+1 gives only an extra O(D) bits beyond the exact coordinate bound. O(D^3 L)-bit intermediate integers and O(D^2) rational scalar operations per target fit O(D^9 L^3). This bound is intentionally loose, but counts bit operations and uses no search exponential in D or log q.

Forming all CRT evaluations costs O((D+m)nr) field operations by direct evaluation; pivot elimination and applying the inverse cost O(r^2 D+mr^2). Modular arithmetic has polynomial, conservatively O((log q)^2), bit cost per multiplication or inversion. Since r<=n<=D, these setup terms fit the stated combined bound after increasing its constant. The public roots are part of the input; no unproved deterministic primitive-root algorithm is imported.

Babai's primary publication confirms polynomial-time nearest-lattice approximation on rational input; the exact Gamma constant above was derived here rather than read out of an inaccessible full article. [Babai, Combinatorica 6 (1986), 1-13](https://link.springer.com/article/10.1007/BF02579403).

## 5. Full joint endpoint law and mask bound

Success and every scalar coefficient depend only on T and the multipliers. In the comparator, condition on these, on success, and on all auxiliary responses. Each designated response remains independent uniform with coefficient one in its own output; it appears in no other output. Adding independent offsets preserves exact independent uniformity. The failure branch is also exact uniform, conditional on T. This proves both discarded-T and retained-T comparator contracts without exposing source-specific Gaussian augmentation coins.

In the planted law, subtracting responses gives the stated V+F identity. Conditional on T, all multipliers, all errors, the common source secret and the coefficients, the independent U_j uniformly translate their ideal. Thus the conditional V law is the same product-uniform ideal law regardless of those conditioned values. Integrating shows independence from all masks conditional on T and success. The success event does not select errors, because its inputs exclude responses. Sharing auxiliary errors creates mask dependence that is retained in the statement.

Each scalar combination has coefficient absolute value at most E(1+||x_j||_1). For any integer polynomial f with coefficients bounded by b0, the negacyclic multiplication operator has norm <=||f||_1<=n b0. Stacking m such operators gives <=sqrt(m)n b0. The displayed sigma makes this <=sigma/(2ell), exactly the direct completion norm condition. Downstream S,G are sampled independently after the complete source map; no source-conditioning argument changes that independence.

For D_tau, Poisson summation gives rho_tau(Z)>=tau. Monotonicity and the elementary Gaussian tail bound give

    Pr[|e|>E] <=(2/tau)int_E^infinity exp(-pi x^2/tau^2)dx
               <=tau/(pi E) exp(-pi E^2/tau^2)
               <=exp(-pi ell^2)/(pi ell).

The union bound is over all Nn source coefficients. For rounded continuous Gaussian, |round X|>ceil(tau ell+1/2) implies |X|>tau ell; the same continuous tail bound applies. No distributional equivalence is asserted.

## 6. Entropy-budget inequality and larger modulus

Put Q=log_2 q. Since B>=1, 2B+1<=3B, and H>=q^(n-d) yields log_2 B>=(n-d)Q/D-log_2 3. If d>=1 and dQ<=rho n, then Q<=rho n<n and (n-d)Q>=nQ-rho n. Set t=D/n>=1 and c=Q/n<=1. Therefore

    D/2+(n-d)Q/D-Q
      >=n(t/2+c/t-c)-rho/t
      >=n(t/2+1/t-1)-rho
      >=(sqrt(2)-1)n-rho.

Adding log_2 D-log_2 3 proves the bound. The second inequality uses 1/t-1<=0; the third is AM-GM. For polynomial q the simpler Gamma>=2^(n/2) already proves the stated certificate failure.

For the large-q illustration Q~n^2, choose D~sqrt(2nQ) and the least B satisfying the stronger entropy-size inequality. Then log_2 B=(nQ+2ell^2)/D+O(1), so log_2(Gamma D B)=sqrt(2nQ)+o(n^(3/2)). D and Q are polynomial in n and 2B+1<=q eventually. The log q term dominates this exponent, giving a numerical window with polynomial E,m. Since any d>=1 would have dQ>rho n, only d=0 is available under that budget. This is not a hard source.

## 7. Exact full-syndrome distinguisher

Let lambda=q^(d/D)>=1. The integer ceil(lambda(B+1/2)) satisfies 2B_*+1>=lambda(2B+1); by minimality,

    B_*<=lambda B+lambda/2+1<=3lambda B.

The last inequality uses B>=1 and lambda>=1. It follows that H_*=(2B_*+1)^D>=q^d H and eta_n^*<= (1/2)sqrt(q^r/H). Under H>=q^r 2^(2ell^2), this is at most 2^(-ell^2-1). The rank term is at most q^(-ell)/(q-1). The full coefficient matrix is iid uniform because each full ring coefficient vector is iid uniform, so Sections 1-3 apply with r=n. The least B_* can be computed exactly by integer exponentiation and binary search; no real-root oracle is needed.

Full syndromes make the common-secret term vanish exactly, including for nonuniform s. No ideal offset is used. On success and the input-error cutoff, every integer coefficient of C before reduction lies in [-W,W]. If W<(q-1)/2, the centered lift is that integer vector. The comparator C is exactly uniform, including fallback. Its n coefficients are independent uniform F_q, so the coefficient-box acceptance probability is exactly ((2 floor W+1)/q)^n. Union bounding planted failures gives the displayed advantage without conditioning the errors on a success probability.

If q^d<=n^(n/2) and D>=n, lambda<=sqrt n. Hence

    W<=3lambda E(1+Gamma D B),
    W/q<=[3/(2sqrt(mn)ell)]sigma/q.

For sigma/q<=n^(-c), W/q tends to zero, which ensures W<(q-1)/2. Also W>=Gamma D B_* (because E>=1), so B_*/q tends to zero and 2B_*+1<=q eventually. Thus the distinct-box condition needed by the collision argument is satisfied rather than assumed silently. Polynomially many source-error coefficients have negligible delta_e for the displayed cutoff. The advantage is 1-negligible.

Finally the invocation of A-BIN is explicitly a dependency on A's provisional binary-image-obstruction-v1.md. Given m iid uniform ideal points, each of d active CRT coordinates is absent from their union with probability q^(-m), independently across coordinates. Full union support has probability (1-q^(-m))^d. On that event, q^d>n^(n/2) implies binary injectivity by the nonzero algebraic-norm bound for a {-1,0,1} coefficient difference. This only excludes the corresponding revealed-ideal guessing certificate; it does not establish a universal attack against high-d public source points.

## 8. Adversarial checks required

Review the exact collision identity including the zero vector; distinction between average-case box existence and deterministic determinant bounds; orientation of coset v-Lambda; the largest-differing-index nearest-plane argument; bit growth in exact rational arithmetic; designated-response independence when all target multipliers influence coefficients; retention of shared source errors; the B_*<q/2 condition; actual integer coefficient-box acceptance; and the stated scope of the A-BIN dependency. Finite controls can refute errors but do not certify these arguments.
