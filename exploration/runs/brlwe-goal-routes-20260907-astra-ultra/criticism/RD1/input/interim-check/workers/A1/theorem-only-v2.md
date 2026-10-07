# Finite source-to-recovery statement

Let n>=2 be a power of two, let q be an odd prime satisfying q=1 modulo 2n, and let R=F_q[X]/(X^n+1), represented by its n coefficients. A public full list of the roots of X^n+1 in F_q may be included in the common parameter description. Set ell=ceil(log2 n), and fix d in {0,...,n}.

For t>0 define the integer discrete Gaussian

    D_t(k)=exp(-pi k^2/t^2)/Z_t,
    Z_t=sum_(j in Z) exp(-pi j^2/t^2).

A ring element with coefficient Gaussian error of parameter t means n independent integer D_t coordinates, reduced modulo q.

Define a source distribution Base_2(n,q,d) on R^2. Choose a uniformly random d-element subset T of the n CRT roots. Let I_T be the ideal of elements whose CRT coordinates vanish outside T. Conditional on T, choose U_1,U_2 independently uniform in I_T. Independently of them and of T, choose F_1,F_2 with independent iid coefficient D_ell errors. The source output is

    (A_1,A_2)=(U_1+F_1,U_2+F_2) in R^2.

Only this pair and the common public parameters are released. The comparator is exactly the uniform distribution on R^2, with its two coordinates independent. A source distinguisher receives one challenge pair and has no source-sampling oracle. For a bit algorithm B, write

    Adv_Base_2(B)=|Pr[B(Base_2)=1]-Pr[B(Unif(R^2))=1]|.

Fix m in {1,2} and set sigma_m=2sqrt(m)n ell^3. The target experiment independently draws S uniformly from {0,1}^n, a_1,...,a_m uniformly from R, and E_1,...,E_m with iid coefficient D_sigma_m errors. These are all independent jointly. It releases

    X=((a_i,a_i S+E_i))_(i=1)^m.

A randomized algorithm Q outputs an element of R. Its target success is epsilon_m=Pr[Q(X)=S], with independent algorithmic coins. Equality means the actual sampled binary secret S. Invalid outputs fail.

Define the source algorithm B_m from Q. Given its sole challenge pair (a_1,a_2), B_m samples a fresh S uniformly from {0,1}^n and fresh independent E_1,...,E_m with iid coefficient D_sigma_m errors, independently of its challenge. It calls Q once on ((a_i,a_i S+E_i))_(i=1)^m, and returns 1 exactly if Q outputs this sampled S. When m=1 it ignores the entire second source element.

Put

    kappa(t)=2sum_(j>=1) exp(-pi t j^2),
    Delta_N=(1+kappa(3ell^2/4))^n-1,
    eta_N=min(1,Delta_N/(1-Delta_N)) if Delta_N<1,
          1 otherwise,
    delta_F,m=min(1,mn exp(-pi ell^2)/(pi ell)).

Claim: for every n,q,d,m and Q satisfying the definitions,

    epsilon_m <= Adv_Base_2(B_m)
                 +q^d ((1+D_ell(0))/2)^n
                 +eta_N+delta_F,m.                       (F)

The test uses one challenge pair, its first m components, and one Q invocation. Its arithmetic and local-sampling overhead is at most

    T_S+T_(E_1,...,E_m)+m(T_mult+T_add)+T_equal.

Let xi_alg bound total variation between a finite implementation of B_m's full independent (S,E_1,...,E_m) sampler and the exact product law. Let xi_source bound total variation between the actual planted pair and Base_2, with the comparator still exact Unif(R^2). Let xi_target bound total variation between an actual target's full witness/transcript law and the specified target. The implementation claim is

    epsilon_actual <= Adv_actual-source(B_m,impl)
       +q^d ((1+D_ell(0))/2)^n+eta_N+delta_F,m
       +xi_source+2xi_alg+xi_target.                      (I)

For fixed m and K, q<=n^K, and these widths, the local independent Gaussian samplers can achieve negligible xi_alg with deterministic polynomial runtime and polynomial bit precision.

# Fixed polynomial-parameter consequence

Let n tend through powers of two. Let q be the least prime congruent to 1 modulo 2n^3. Use the prime-existence statement that for a fixed constant C and all sufficiently large M, the least prime congruent to 1 modulo M is at most C M^5.18. Consequently this sequence satisfies

    2n^3+1<=q<=n^16 eventually,
    q/sigma_m>=n eventually for m in {1,2}.

The common ring parameters have polynomial-size representations and permit polynomial-time arithmetic. All parameter functions and constants are chosen before Q or its success exponent.

For d(n), either take

    d(n)=floor(sqrt(n)/ell^4),

or take any fixed uniformly computable sequence satisfying

    1<=d(n)<=floor(n/(64ell)) eventually.

For each d(n) choice separately, assume Base_2(n,q,d(n)) is computationally indistinguishable from uniform R^2 for every uniform randomized polynomial-time distinguisher. Claim: every uniform randomized polynomial-time Q has negligible target recovery success for each fixed m in {1,2}, with sigma_m as defined above. Quantitatively, the algorithm B_m,impl satisfies

    Adv_Base_2(B_m,impl) >= epsilon_m-negl(n).            (A)

Changing d(n) changes the explicitly assumed source distribution. No implication between those source assumptions is included. The theorem includes exactly one or two target ring samples with one common binary secret and fully independent coefficient Gaussian errors. It includes no conclusion about more target samples, target decision advantage, or a derivation of the computational source assumption.
