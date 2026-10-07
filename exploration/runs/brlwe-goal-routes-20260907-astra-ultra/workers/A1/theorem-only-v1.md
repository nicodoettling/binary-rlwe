# A1-T1 — theorem-only candidate packet for blind review

Purpose: prove, refute, or isolate the minimal missing hypothesis of the following finite and asymptotic statements. This packet gives definitions and statements only. All variables, costs, and source/sample restrictions below are part of the claim. No computational hardness assumption is claimed to be established from worst-case lattice problems.

## Exact finite definitions

Let n>=2 be a power of two, let q be an odd prime with q=1 modulo 2n, and let R=F_q[X]/(X^n+1), represented in the coefficient basis of degree below n. A public complete list of the n roots of X^n+1 in F_q may be included in the common parameter description. Set ell=ceil(log2 n), and fix an integer d with 0<=d<=n.

For t>0, define the integer discrete Gaussian D_t(k)=exp(-pi k^2/t^2)/Z_t, where Z_t=sum_(j in Z) exp(-pi j^2/t^2). Gaussian errors in ring elements always mean independent integer coefficient draws reduced modulo q. This is the exp(-pi x^2/t^2) parameter convention.

Define one source challenge as follows. Sample a uniformly random d-element subset T of the n CRT roots. Let I_T be the ideal whose CRT coordinates vanish outside T. Conditional on T, sample U_1,U_2 independently uniform in I_T, including all zero-coordinate possibilities. Independently sample F_1,F_2 with iid coefficient D_ell laws. Publish exactly

    Base_2(n,q,d) = (A_1,A_2)=(U_1+F_1,U_2+F_2) in R^2.

Its comparator is exactly two independent uniform elements of R. T,U_1,U_2,F_1,F_2 remain hidden. The same hidden T is used for both ideal points. The source contains no secret input, target response, noise completion, or source oracle. Its computational assumption, if invoked, states indistinguishability of these two fully specified pair distributions.

Fix m in {1,2}. Let sigma_m=2sqrt(m)n ell^3. The m-sample target law is:

- S has independent uniform coefficients in {0,1};
- a_1,...,a_m are independent uniform R;
- E_1,...,E_m have independent iid coefficient D_sigma_m laws;
- the entire tuple (a_1,...,a_m,S,E_1,...,E_m) has this product law;
- publish X=((a_i,a_iS+E_i))_(i=1)^m.

For a uniform randomized algorithm Q outputting an element of R, let epsilon_m=Pr[Q(X)=S]. Its coins are independent of all experiment variables. This is equality to the sampled coefficient-binary witness, not merely consistency with the equations. Invalid outputs count as failure.

For a source bit test T, define Adv_Base_2(T)=|Pr[T(Base_2)=1]-Pr[T(Unif(R^2))=1]|.

The public test T_m associated to Q receives one source challenge pair (a_1,a_2), independently samples its own coefficient-binary S and its own m iid coefficient D_sigma_m errors, invokes Q once on ((a_i,a_iS+E_i))_(i=1)^m, and returns 1 exactly if Q's output equals this sampled S. When m=1 the entire second source element is ignored. T_m has no source-sampler or hidden-variable access.

For t>0 define

    kappa(t)=2sum_(j>=1) exp(-pi t j^2),
    Delta_N=(1+kappa(3ell^2/4))^n-1,
    eta_N = min(1,Delta_N/(1-Delta_N)) if Delta_N<1,
            1 otherwise,
    delta_F,m = min(1,mn exp(-pi ell^2)/(pi ell)).

## Finite claim A1-T1.F

For every n,q,d,m and every Q as specified above,

    epsilon_m <= Adv_Base_2(T_m)
                 + q^d ((1+D_ell(0))/2)^n
                 + eta_N + delta_F,m.                 (F)

The reduction uses exactly one source challenge containing two ring elements, uses its first m elements as target first components, and invokes Q once. No other challenge or target sample is produced. The exact arithmetic runtime overhead is at most

    T_S+T_(E_1,...,E_m)+m(T_mult+T_add)+T_equal.

There is no active-U conditioning cost, quotient-extraction premise, second-noise broadening, source expansion, or additional computational hybrid in (F).

## Implementation claim A1-T1.I

The exact Gaussian laws above are mathematical distributions. Let xi_alg bound total variation between the finite implementation of the test's full fresh (S,E_1,...,E_m) sampler and its exact product law. Let xi_source bound TV between the actual supplied planted pair and Base_2, with exact uniform-pair comparator. Let xi_target bound TV between the actual target's full witness/transcript law and the mathematical target. Then

    epsilon_actual <= Adv_actual-source(T_m,impl)
       +q^d ((1+D_ell(0))/2)^n+eta_N+delta_F,m
       +xi_source+2xi_alg+xi_target.                    (I)

For q<=n^K, fixed m and fixed K, one can make all local Gaussian sampling errors negligible with deterministic polynomial running time and polynomial bit precision. No efficient sampler for a correlated matrix Gaussian is an algorithmic premise. The matrix Gaussian, if used in a proof, may remain entirely latent.

## Asymptotic claim A1-T1.A

Take n through growing powers of two and q to be the least prime congruent to 1 modulo 2n^3. The permitted prime-existence import is: there is a fixed constant C such that the least prime 1 modulo M is at most C M^5.18 for sufficiently large M. Hence this choice has

    2n^3+1<=q<=n^16 eventually,
    q/sigma_m>=n eventually for m in {1,2}.

The public ring parameters have polynomial representation and arithmetic complexity. All constants and parameter functions are fixed before the solver or its inverse-polynomial success exponent is chosen.

One baseline dimension choice is

    d=floor(sqrt(n)/ell^4).

A separate, larger dimension choice is any fixed uniformly computable sequence d(n) satisfying

    1<=d(n)<=floor(n/(64ell)) eventually.

For each dimension choice separately, assume the corresponding exact source family Base_2(n,q,d(n)) is computationally indistinguishable from the uniform pair against all uniform randomized polynomial-time tests. Then every uniform randomized polynomial-time algorithm's recovery success in the m-sample target is negligible, for each fixed m in {1,2}, with the width sigma_m specified above. This follows from the stronger quantitative assertion

    Adv_Base_2(T_m,impl) >= epsilon_m-negl(n).           (A)

Changing d changes the computational source assumption. No hardness transfer between different d families is asserted. The source premise is the explicit two-point, same-hidden-ideal specialization of the HLBDD-type source described in Order-LWE Section 7; the exact comparator here is stipulated explicitly as R^2. Whether that premise follows from a more standard or worst-case assumption is outside this statement.

## General numerical entropy gate

For uniform binary S and independent iid D_tau auxiliary G, the associated guessing claim to check is

    P_guess(S|S+G over Z^n)=((1+D_tau(0))/2)^n,
    P_guess(S|S+G modulo q)<=((1+D_tau(0))/2)^n.

For a quotient of size q^D, a sufficient numerical gate for negligible quotient-charged guessing is

    D log2 q+n log2(1+D_tau(0)) <= n-omega(log n).

This gate asserts no quotient uniformity or extractor theorem. At tau=ell, q<=n^16, and d<=n/(64ell), the stated upper bound is

    q^d ((1+D_ell(0))/2)^n <= 2^(-3n/4+n/(ell ln 2)).

## Boundary cases and exclusions

The finite statement must handle d=0, d=n, n=2, zero ideal points, nonuniform quotient images of binary secrets, and Delta_N>=1. The asymptotic claim only uses eventual d>=1 and the displayed prime and width family. No target decision-hardness statement, arbitrary target-sample statement, extraction claim, or independent per-sample completion premise is included. Source and target errors have the full independence explicitly specified above, not merely matching marginals or pairwise independence. A proof must retain S through its noise comparison if it bounds exact witness recovery.

Permitted primary sources: Brakerski–Dottling, ePrint 2020/119 and 2020/1185; Order-LWE, ePrint 2018/494, Section 7; the stated least-prime theorem and its primary source if needed. The reviewer may reconstruct all elementary algebraic and probabilistic lemmas directly.
