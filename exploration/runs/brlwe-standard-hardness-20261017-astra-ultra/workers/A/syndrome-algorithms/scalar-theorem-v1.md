# A-SCALAR v1: executable partial syndromes and a scoped comparison

Status: PROVISIONAL, authored by A; no independent review completed. This is an algorithm with a conservative certificate and an explicit comparison attack. It is not a lower bound against actual LLL outputs, block algorithms, or every partial-syndrome map. Source computational hardness remains OPEN.

## Exact contract and dimensions

Let n>=2 be a power of two and q an odd prime splitting X^n+1. The public parameters include its n distinct roots. Write R_q=F_q[X]/(X^n+1). An efficient law chooses a root subset T of cardinality d independently of all samples; fixed and nonuniform laws are allowed. Let I_T be the CRT-supported ideal of dimension d, r=n-d, and pi_T:R_q->F_q^r evaluation on the complementary roots. The law of T cannot depend on sample multipliers in this theorem.

There are D auxiliary ordinary RLWE samples (a_i,b_i) and m designated samples (a'_j,b'_j), so N=D+m. Each a is independent uniform R_q. The planted responses have one common arbitrary secret s, independent iid coefficient-error vectors e~mu^n, and b=a s+e mod q. The comparator has independent uniform a,b. No secret-distribution assumption is needed for the endpoint identities. The source hardness theorem, if any, must separately cover this exact secret/error/sample law.

Choose D>=n+ell, ell=ceil(log_2 n), and an integer B>=1 with 2B+1<=q. Let

    Gamma=2^(D/2), H=(2B+1)^D,
    eta_r=(1/2)sqrt((q^r-1)/H),
    rank_r=(q^r-1)/(q^D(q-1)),
    rho_r=min(1,rank_r+m eta_r).

For r=0 use rank_r=eta_r=0. The main algorithm is needed only when r>0; r=0 can directly return all-zero coefficients. The lattice dimension is D, not nD; it uses scalar integers as constant ring polynomials. The distinct input sample budget is N, the output count is m, and the target binary-secret dimension remains n.

## Algorithm SCALAR-SYN

1. Form A=[pi_T(a_1)|...|pi_T(a_D)] and targets y_j=pi_T(a'_j). If rank A<r, report failure.
2. Permute pivot columns and multiply equations by the inverse pivot matrix, obtaining [I_r|C]. With integer lifts of C, form the full-rank integer kernel basis

       K = [q I_r  -C]
           [  0     I_(D-r)].

   Its lattice is Lambda={x in Z^D: A x=0 mod q}; det Lambda=q^r. Form the centered particular lift v_j=(lift(A_pivot^-1 y_j),0).
3. LLL-reduce K with delta=3/4, once. On each v_j run exact rational Babai nearest plane in the reduced basis, obtaining w_j in Lambda. Set x_j=v_j-w_j and undo the coordinate permutation.
4. Verify A x_j=y_j mod q and ||x_j||_2^2<=2^D D B^2 for every j. If any verification fails, report failure. Otherwise return the scalar coefficients x_ji.

This algorithm succeeds with probability at least 1-rho_r over the independent uniform multipliers. On success, ||x_j||_1<=Gamma D B. Its coefficients are computed using only public multipliers and T.

With L=ceil(log_2(2Dq^2)), the LLL stage costs O(D^6 L^3) classical bit operations. Exact rational nearest plane and setup have a conservative combined bound O((m+1)D^9 L^3+(D+m)n^2(log q)^2), with fixed constant arithmetic conventions. In particular the algorithm is polynomial time in n,D,m,log q; exponentially large q of polynomial bitlength does not itself cause exponential runtime. The proof gives the bit-growth accounting rather than treating unit-cost large integers as free.

## Exact source map

On successful SCALAR-SYN, draw U_j independently uniform I_T, independently of all input variables, and output only

    C_j=b'_j-sum_i x_ji b_i+U_j.

On failure output an independent uniform tuple in R_q^m. All multipliers, x, U, success flag and responses are discarded. Retaining T alone is also valid, with comparator Law(T) x U(R_q^m).

The comparator output is exactly independent uniform. On planted success,

    C_j=V_j+F_j,
    V_j=(a'_j-sum_i x_ji a_i)s+U_j in I_T,
    F_j=e'_j-sum_i x_ji e_i in Z^n.

Conditional on T and the success branch, V is exactly iid uniform I_T and independent of the entire correlated mask tuple F. The masks share auxiliary errors, and no independence across masks is claimed. Their law and the source success event are independent of the downstream fresh binary secret and auxiliary Gaussian in A-ADM.

Suppose the actual source error law satisfies

    Pr[max over Nn input coefficients |e|>E]<=delta_e,

for an integer E>=1. Then on the complementary event,

    |F_j,t|<=E(1+Gamma D B)=b0,
    ||stack_j M_Fj||<=sqrt(m)n b0.

For coefficient D_tau one may take E=ceil(tau ell), increased to 1 if necessary, and delta_e<=Nn exp(-pi ell^2)/(pi ell). For a rounded continuous Gaussian of coefficient width tau, use E=ceil(tau ell+1/2), with the same displayed upper bound. These are different error laws.

The direct A-ADM sufficient target choice is

    sigma=2 sqrt(m)n E ell(1+Gamma D B).

It pays rho_r+delta_e, plus the distinct completion and binary-image terms from A-ADM. No source computational-hardness claim follows merely from this map.

## Certified parameter conclusions

To make the preimage-existence loss negligible, one explicit choice is H>=q^r 2^(2ell^2), giving eta_r<=2^(-ell^2-1). If the least such B violates 2B+1<=q, this certificate does not apply.

For polynomial q, D>=n makes the displayed sigma at least exponential in n, for E>=1 and B>=1. Thus this certificate cannot give q/sigma>=n^c for any fixed c>0. This does not say the actual Babai outputs always attain the upper bound.

More generally, suppose d>=1, d log_2 q<=rho n for a fixed 0<rho<1, and H>=q^(n-d). Then

    log_2(Gamma D B/q)
      >=(sqrt(2)-1)n-rho+log_2 D-log_2 3.

This excludes a certified useful target ratio for EVERY modulus satisfying that sufficient entropy budget, including moduli larger than polynomial. The case d=0 is excluded from this inequality: it has no retained ideal entropy and is directly an error-only map.

For illustration of why bitlength alone is insufficient, a public split-prime family with log_2 q asymptotic to n^2, D asymptotic to sqrt(2)n^(3/2), and B chosen from H>=q^n 2^(2ell^2) gives

    Gamma D B=2^((sqrt(2)+o(1))n^(3/2)) << q.

With polynomial E,m it gives a formal target-noise window and polynomial runtime, but the sufficient entropy budget forces d=0, and the source is explicitly distinguishable by the following test. This is a conditional parameter illustration for a supplied split-prime family; no prime-search runtime is asserted.

## Full-syndrome comparison under the weaker binary collision bound

Keep D>=n+ell. Assume the weaker numerical condition q^d<=n^(n/2), and let B_* be the least nonnegative integer such that

    (2B_*+1)^D >= q^d(2B+1)^D.

Then B_*<=3 q^(d/D) B<=3 sqrt(n) B. Assume 2B_*+1<=q. Run the SAME algorithm on the full coefficient syndrome A_0=[a_1|...|a_D] in F_q^(n x D), with radius B_*, using one designated sample. No ideal offset is added. On success output C=b'_1-sum_i x_i b_i; on failure output uniform R_q. Its comparator is exactly uniform and its planted successful output is exactly e'_1-sum_i x_i e_i.

Put

    rho_0=(q^n-1)/(q^D(q-1))+(1/2)sqrt((q^n-1)/(2B_*+1)^D),
    W=E(1+Gamma D B_*).

For W<(q-1)/2, accept iff every centered coefficient of C lies in [-floor W,floor W]. Its distinguishing advantage is at least

    1-rho_0-delta_e-((2 floor W+1)/q)^n.

Moreover, if sigma is the displayed partial-source target choice,

    W/q <= [3/(2 sqrt(mn)ell)] (sigma/q).

Thus H>=q^r 2^(2ell^2), polynomial N,m and a useful certified ratio sigma/q<=n^(-c) imply advantage 1-negl(n). The technical conditions 2B_*+1<=q and W<(q-1)/2 follow for sufficiently large n from E>=1 and this ratio. This is an actual polynomial-time source distinguisher, with exact output coordinates and comparator acceptance mass, not only a comparison of upper bounds.

For the ideal-supported source in this map, A-BIN v1 says q^d>n^(n/2) makes the binary multiplication image injective whenever the output ideal points have full union support. Conditional on success that support event has probability (1-q^(-m))^d. Hence this excluded high-d regime cannot make the existing completion/revelation proof give negligible recovery probability. The numerical condition used by the comparison therefore includes every regime not already excluded by that scoped injectivity test. This conclusion concerns the A-ADM proof strategy and this scalar algorithm; it is not a public recovery attack against every ideal source.

## Scope left open

A fixed, biased, or deterministically chosen T of the same size does not change the scalar random-matrix distribution or these bounds. Adaptively choosing T from the multipliers is outside this theorem. Ring-polynomial combinations create a structured matrix, not the independent-entry matrix used here. A new algorithm may exploit that structure or non-CVP mechanisms. Neither a determinant-root heuristic, an SVP-only block guarantee, nor a forward extractor is a proved inhomogeneous preimage algorithm.
