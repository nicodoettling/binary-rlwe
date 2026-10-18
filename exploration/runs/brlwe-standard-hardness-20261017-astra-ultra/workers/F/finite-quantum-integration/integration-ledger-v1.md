# F: exact same-integral-ideal integration audit, version 1

**NONBLIND review. Classical A/B-bounded/C8 composition is supported with the ledger below. The proposed coherent adapter is new and UNACCEPTED. A fully explicit finite quantum state-preparation/gate ledger is still OPEN. The original computational foundation remains OPEN, independently, because no standard arbitrary-ideal family reaches this bounded-norm integral family.**

This document replaces the old composition packet's C-v5 dependency only for this review: the actual inspected dependency is theorem-v8 / algorithm-v2 / proof-v9. It does not modify those bytes or their coordinator-owned status. BT13's sealed report supports the finite classical core and explicitly excludes this composition and quantum step. The older metadata in claims.json still called C8 provisional at intake; this reviewer does not reconcile the coordinator's claim graph.

## 1. Frozen objects and executable access

Let n>=2 be a power of two and R=Z[X]/(X^n+1). Let q be a supplied odd split prime, k>=1, and J one supplied nonzero INTEGRAL ideal with D=N(J)<=2^(rho n), fixed rho<1, gcd(D,q)=1. Set Lambda=J^-1 and L=qLambda. The exact recovery target has iid uniform a_i in R/qR, one independent uniform coefficient-binary S, and independent coefficient integer D_sigma errors, all with the same optional public J metadata. Rec is one explicitly given bounded classical randomized algorithm with success epsilon_rec on that exact target and a time bound on every valid input. For a pointwise statement, Rec ignores J or its success lower bound must hold for every supplied J; an average over J does not suffice.

Every ideal uses an ordinary integer basis. Rational vectors and scalars use full signed-numerator/positive-denominator binary encodings. Any nonrational scalar has a fixed certified polynomial-time evaluation program; its description and every actual evaluation cost are charged. Use fixed HNF/SNF finite representatives. No witness for A's short basis, G, H, source good event or Gaussian sampler on J is executable advice. Rec's full finite code is needed for the quantum candidate; a service that only returns classical answers is insufficient.

For P>=1 put h=1/(DP) and F=h Z^n/L in coefficient coordinates. Since R subset Lambda subset D^-1 R, the group has order q^n D^(n-1)P^n. The isomorphism Lambda/qLambda -> R/qR sends v/D to v D^{-1} mod q. It is exact because gcd(D,q)=1. All rounds and reductions use the same representative/tie convention.

## 2. One compatible parameter family

For fixed rho<1 and polynomial k, choose

    ell=ceil(log2(2nk)),  tau2=2n^2,  t=2n^2 ell,
    w_B=r_B=ell^2,  s=sqrt(2) ell^2,
    sigma=8n^2 ceil(sqrt(kn)) ell^4,
    epsilon_B=nu=eta_cap=2^(-ell^2),  P=2^(2ell^2).

Here s is a mathematical source width, with an explicit algebraic representation if evaluated. All executable B widths and the target sigma are rational/integer. A's geometric existence bound n^2 D^(1/n)<=2n^2 and its completion inequality sigma>=2ts sqrt(kn)ell hold. Also r_B>=max(1,sqrt(log(8n/epsilon_B)/pi)).

Write

    delta_tail=min(1,4kn exp(-pi ell^2)),
    beta=min(1, exp(-(1-rho)n log 2 + 1/(2n ell))),
    theta_A=2 sum_(j>=1) exp(-pi(3ell^2/4)j^2),
    Delta_A=(1+theta_A)^n-1,
    eta_A=min(1,Delta_A/(1-Delta_A)) if Delta_A<1, else 1,
    Delta_B=2k epsilon_B/(1-epsilon_B)+2pi kn/(P r_B)+kn nu.

These are explicit analytic bounds; eta_A is not sampled. They are negligible as n grows for fixed rho<1 and polynomial k. Require a supplied positive rational delta with

    delta <= epsilon_rec-delta_tail-beta-eta_A
             -2k epsilon_B/(1-epsilon_B)-2pi kn/(P r_B)-3kn nu-2eta_cap.   (GAP)

An inverse-polynomial epsilon_rec permits delta=epsilon_rec/2 once the displayed loss is sufficiently small. A known lower bound on epsilon_rec can be substituted so the parameter is executable.

A concrete nonempty asymptotic choice is rho=1/2, k=n, epsilon_rec>=1/n and delta=1/(2n), for sufficiently large n, with q>=n sigma. Suitable supplied split primes have polynomial bit length without an algorithmic prime-generation assumption: for polynomial integer threshold T>n sigma, any prime divisor q of (T!)^n+1 exceeds T and is 1 mod 2n. The bit length is O(nT log T). The family is nonempty because J=R is admissible; this example asserts compatibility, not hardness. Other J retain the separate gcd(D,q)=1 condition. This argument does not claim q has polynomial value; that stronger statement is unnecessary for bit complexity and is not imported here.

## 3. Exact endpoints, including both bounded-sampling charges

The finite GP challenge is k iid Q_h(G_(w_B)) modulo L, versus k iid uniform F, with the same supplied J. In C's convention its canonical width is

    w_C=sqrt(n) w_B.

Define ONE algorithm A_J on a finite tuple: run B-v2's public bridge; sample independent fresh binary S and approximate coefficient D_sigma errors; run Rec on the completed samples; accept precisely when its output equals that actual S. Use the complete-call uniform-integer cap below. All coins are private and fresh. The source itself is not appended to Rec's coins or to proof auxiliaries.

| Interface | Planted full law | Comparator full law |
|---|---|---|
| Exact A wrapper | A's fractional-Gaussian multipliers completed with fresh exact S,E | Exactly the original binary-recovery target |
| B-v2 before target completion/caps | Distance at most Delta_B from k iid D_(Lambda,s) mod qLambda | Exactly iid uniform R/qR |
| Add target-noise approximation, before elementary-loop caps | Distance at most Delta_B+kn nu from exact A planted completion | Distance at most kn nu from exact recovery target |
| Complete bounded A_J | Distance at most Delta_B+kn nu+eta_cap from exact A planted completion | Distance at most kn nu+eta_cap from exact recovery target |

Thus the endpoint sum is Delta_B+2kn nu+2eta_cap, yielding (GAP). In particular there are three kn nu terms after expanding Delta_B. The capped comparator is approximate. Exact comparator equality applies only to the uncapped expected-time B map, including its equivariant scalar fallback; capped quotient sampling need not preserve it.

The complete bound uses

    K_B=ell^2+6,
    Lplus=40(ell^2+6)(ell^2+4),
    Uall=kn(1+2Lplus),
    Bcap=ell^2+ceil(log2 Uall).

Each elementary uniform-integer rejection loop has at most Bcap attempts and fixed valid fallback. Uall covers coset choices, B's scalar proposals and target-noise proposals. Conditional on every prior history its failure probability is at most 2^(-Bcap). First-disagreement coupling and a union bound give at most eta_cap for each entire call, in each world. The exact natural-log ceiling in B-v2 is retained using the checked ceiling addendum; v3 is not substituted.

The source-gap inequality is about the exact acceptance probabilities of this fixed implemented A_J. It is paid ONCE to establish delta. C8 does not replace A_J by an ideal circuit on every call, so multiplying this loss by Q_* would analyze a different hybrid. C8's own query-simulation errors are separate, and are multiplied/summed as specified there.

## 4. Actual C8 substitution, parameters and conditional error

Use C8 with the same J,L,F,k,P and w=w_C, advantage delta from (GAP), and A=A_J. Its metadata and output laws match exactly. Its finite physical queries always reduce to valid F tuples, including the wrong orientation. B's full-input cap and Rec's full-input bound are consequently sufficient. No source-distribution promise is needed merely for termination.

Choose a rational 0<zeta<=1/8 first. Put h0=delta w_C/(32nk),

    a0=D^(1/n) w_C^(1-2/n) h0^(2/n)/(nq),
    S=max(0,(n/2) log(1/a0)).

Choose integer kappa at least all C8 lower bounds

    4S+4n+4log(k+1)+20, 2k, 2/delta, 20log3, log(8n/zeta),

and with 3w_C exp(-kappa)<q/(8D). One can use certified upper evaluations with positive slack to make this a bounded choice. Do not impose zeta=exp(-kappa). Then define the exact loop counts

    K=kappa+200, d_H=2,
    T_walk=10^6 K^3 d_H^4,
    Lambda_walk=10K d_H^2 ceil(log2(2T_walk)), C=K+Lambda_walk,
    Lambda_cmp=10000 C^4,
    M=100C ceil(log2(C Lambda_cmp)),
    Delta=1/(100C Lambda_cmp M), G=100C Lambda_cmp M^2,
    N=10000 Lambda_cmp^2 M^2 [C+ceil(log2(8(G+1)))],
    Q_H=2(T_walk+1)(G+1)N, Q_*=n Q_H.

Now choose

    epsilon0=min(1/16,zeta/(64kQ_*)),
    a=Up(sqrt(log(8n/epsilon0)/pi))+1,
    v0>=2sqrt(n)a,
    d0=delta w_C/(32nkv0),

enlarging v0 for d0<q/(4D^(1/n)). For the explicit q>=n sigma family v0=2sqrt(n)a already suffices, and d0=delta ell^2/(64nk a) is rational. Kappa and Q_* precede a,v0, so no circular choice arises. All nonrational rounding is the frozen algorithm's bounded Up rule; the last verification uses its rational c_test threshold, not an exact comparison to 2d0.

For every rational target T=lambda+e with lambda in L and canonical infinity norm <=d0, the exact finite routine returns lambda with probability at least 1-p_BDD, where

    p_BDD=(n/2) exp(-kappa)+zeta.                           (BDD-ERR)

Its final verifier makes any accepted candidate correct on promised targets; failure is allowed. It has at most Q_* calls to A_J and hence Q_* calls to Rec. The count holds on all targets and all answer sequences.

The fixed multiplier/posterior comparisons cost at most 2kQ_*epsilon0/(1-epsilon0)<zeta/16. The walk-position comparison uses the global physical-kernel Lipschitz bound, not continuity of the analytic patch. The single global sample counter has tau_c=zeta/[16(c+1)^2], c>=1, across both orientations; the conditional numerical charges sum below zeta/16. Other conservative allowances are within C8's total zeta. Only the continuous proxy tends to Haar; the actual multiplier endpoint is not claimed uniform.

The adaptive proof is causal: new coins have their stipulated law conditional on each past transcript; the corrected walk is an analysis process; first-disagreement and union bounds pay errors. No step conditions a proposal on all future comparisons succeeding. The CP-1 selected-hit control remains 0.0105>0.01 and therefore still rejects the old product argument. The present composition only uses pointwise kernels, conditional couplings and union bounds.

## 5. Full finite classical resource ledger

Let H_in denote the total supplied bit length: n,k,q,P; all entries of the ordinary J basis; all metadata actually read/copied; all scalar numerators/denominators or evaluation-program descriptions; and the current rational BDD target. Let E_C be the total actual certified-evaluation cost prescribed by C8 on its worst bounded transcript at this input length. Let T_Rec be the supplied worst-case recovery bound at the finite ring-sample encoding length. Neither magnitude logs alone nor an unspecified real arithmetic oracle replace these costs.

Let T_AB be the deterministic maximum steps of the complete fixed capped A_J program at the HNF representative bound. It satisfies

    T_AB <= T_Rec + poly(H_in,n,k,ell,log q,log P),

with B's exact-ceiling computation and the displayed Uall,Bcap included. Each A_J consumes k input F samples and calls Rec once. The number of random bits and output bits is bounded by its step bound. None depends on D in unary or on an ideal-Gaussian sampler.

The C8 machine has a constructible bound

    T_BDD <= Q_* T_AB + E_C
               + poly(H_in,n,k,kappa,1/delta,log(1/zeta)),

where the polynomial is the explicit finite arithmetic/sampler program in algorithm-v2, not a primary exact-real OHCP oracle. The number of generated physical samples is at most kQ_*. Its grid support is binary-searched; its cardinality is not a loop count. Wrong-sign walk positions have bit length O(Bbits+log T_walk), logscale<=M, and Bbits is exactly the algorithm's 2M+2K+Up(log2(256Q_*(T_walk+2)/zeta))+10. Large means, exponents and grid sizes are paid by their binary length. Ordinary basis inversion, HNF/SNF, membership and exact rational comparisons need no factoring or trapdoor.

This review verifies the displayed dependency and endpoint substitution against the current frozen C8 proof. It does not claim to have executed its astronomically large loops. The exact degree of T_Rec and supplied scalar evaluation routines necessarily remains an input parameter. A gate-level circuit can be obtained by bounded unrolling, as specified in the separate proposed adapter.

## 6. Same-J quantum geometry and finite query encodings

Use coefficient Euclidean coordinates to feed a rational lattice basis to the primary quantum lemma. Write mathcalL for the coefficient lattice qJ^-1. Its ordinary Euclidean dual is

    mathcalL* = conjugate(J)/q.

Indeed <x,y>_coef=Tr(x conjugate(y))/n, and R's trace dual is R/n up to its principal unit; for this cyclotomic the ideal identity is exactly R/n. Thus the full canonical dual is conjugate(J)/(nq), as in C8. These descriptions differ by the canonical similarity, not by an ideal-family change.

Let d_Q=d0/sqrt(n). A coefficient Euclidean error <=d_Q has full canonical Euclidean norm <=d0 and therefore canonical infinity norm <=d0. Hence C8 is a BDD routine on mathcalL at radius d_Q. Also

    lambda_1(mathcalL) >= q/(sqrt(n)D^(1/n)),
    d_Q < q/(4sqrt(n)D^(1/n)) <= lambda_1(mathcalL)/4.

The primary uniqueness inequality consequently holds with slack. The radius d_Q and scalar widths are explicitly algebraic in the displayed family; ideal/target coordinates themselves remain rational.

The primary finite decoding register is mathcalL/H modulo mathcalL for an integer H, NOT an arbitrary real input. In basis labels it is B_L u/H, with u an n-vector modulo H and B_L a rational basis of mathcalL. Its reduction to a chosen fundamental parallelepiped and the coefficient target supplied to C8 use exact rational arithmetic. Even if one normalizes the primary proof by sqrt(n)/d_Q, mapping the target back cancels that scalar exactly. There is no need to round an unknown real BDD target near a promise boundary.

For encoding purposes choose an efficiently computed rational U>=max_i ||b_i||_2 of an ordinary basis of mathcalL. A power of two H satisfying

    H >= 2^(4n) n max(1,U/d_Q)

is a conservative sufficient grid-scale upper choice for the inequalities in the normalized primary construction. Its logarithm is polynomial in the basis/radius encodings. It supplies n log2 H Fourier-label qubits. This observation bounds query bit lengths; it is not a replacement proof of the primary state-preparation precision guarantees. Computing an LLL basis internally is allowed, but no such basis is passed to the A wrapper as extra challenge metadata.

Substitution into the primary width formula gives a candidate output on mathcalL*=conjugate(J)/q at coefficient width n/(sqrt(2)d0). Multiplying by q and conjugating gives the ordinary discrete Gaussian on the SAME J at

    s_J,coef = nq/(sqrt(2)d0),
    s_J,canonical = nq sqrt(n)/(sqrt(2)d0).              (DGS-WIDTH)

The output is an ordinary lattice Gaussian, with negligible approximation if the quantum gates close. It is not a super-Gaussian law, exact sampler, new ideal, or arbitrary fractional-padding source. The finite F used by A/B/C and the quantum finite mathcalL/H grid serve different roles and must not be identified.

## 7. Coherent use, query count, and the exact remaining gate

Primary source verification is in `primary-source-check-v1.md`. Its proof has one logical coherent BDD uncomputation. The bounded code supplied here can be reversibly evaluated; the theorem/proof files for F-QCOH isolate that proposed adapter. For a promised finite query state, its vector-norm replacement error is at most 2sqrt(p_BDD). Off-promise squared mass tau_Q instead gives 2sqrt(p_BDD+tau_Q). Keeping and reversing every random/work register is essential. Measuring/discarding a classical oracle's garbage, assuming one universally good random seed, or charging only p_BDD would fail the preserved finite regressions.

For example choose zeta=2^(-4n-10), then choose kappa by Section 4. Since kappa>=log(8n/zeta), the first term of (BDD-ERR) is <=zeta/16, so

    p_BDD <=17zeta/16,
    2sqrt(p_BDD) <= (sqrt(17)/2) sqrt(zeta).

These choices preserve polynomial bit complexity and a nonzero d0. The loss in d0 through a is explicit and must be retained; an older d0 computed at constant zeta cannot be reused. No extra B source-gap charge occurs during this change of confidence.

Let S_BDD be the chosen bounded Boolean-circuit size at the primary query bit bound. One coherent clean decoder uses O(S_BDD) gates/qubits, one forward and one inverse BDD evaluation, hence at most **2Q_* coherent Rec evaluations per DGS sample**. This assumes executable Rec code. The primary Fourier transform and preparation are additional gates. Repeated independent outputs use fresh state preparations and coins; m outputs require at most 2mQ_* coherent Rec executions and their statistical errors add by product coupling.

The unresolved finite primary interface is now exact:

> Supply a bounded, finite-register implementation of the primary Gaussian-state preparation and Fourier/alias-decoding stages for the rational coefficient lattice mathcalL, scalar d_Q and grid H above. Freeze its finite initial support, every rotation/CDF (or alternative preparation) algorithm and precision, any postselection/retry cap, the total elementary gate count G_Q, and an explicit state/output error eta_Q. Prove the estimate on a common purification or a conditional branchwise state law. Identify whether off-promise mass is included in eta_Q via the truncated ideal reference, or separately give tau_Q. Then reconcile its error with F-QCOH and freeze a complete theorem/proof for fresh review.

Given such a concrete certificate, a valid finite ledger would be

    TV(output, D_(J,s_J,coef))
       <= eta_Q + eta_synth + 2sqrt(p_BDD+tau_Q),
    gates <= G_Q + O(S_BDD),
    coherent Rec executions <=2Q_*.

Here eta_Q must already include the primary state/truncation/aliasing comparisons in the same metric, eta_synth the remaining gate approximation, and tau_Q must not be counted twice. The inspected source gives asymptotic efficient construction and negligible/exponential bounds, but not this frozen finite numerical schedule. In particular Lemma 3.12's sufficient-precision Gaussian-sum step and subsequent gate synthesis cannot be filled by an unspecified free unitary. Naming an unknown polynomial G_Q or an unknown 2^(-Omega(n)) constant is not a completed concrete finite ledger.

This is a finite-implementation/source-parameter obligation, not a counterexample to the published asymptotic quantum theorem or an impossibility of coherently compiling C8. A conditional asymptotic same-J DGS consequence is supported in the usual theorem-level model, pending the new adapter's review. The stronger fully explicit finite assertion requested here is not certified by this packet. No speculative alternate route was begun.

## 8. Preserved failures, scope and terminal disposition

The original B expected-time exact comparator, bounded both-endpoint error, A proof-only geometry, C physical-versus-proxy distinction, C-v5 missing finite contract, C7's exact-real final threshold, and CP-1 future-conditioning failure all remain distinct and are not silently restored. The adapter proof adds FQ-R1 through FQ-R4 for seed selection, square-root coherent error, garbage disposal and off-promise support. No computational experiment was run; the finite controls are hand calculations and require independent checking before acceptance.

Even if the finite quantum gate is later closed, (DGS-WIDTH) holds only for the originally supplied integral J satisfying D<=2^(rho n). Neither coefficient/canonical duality, rational scalar normalization, the Fourier transform nor conjugation maps arbitrary input ideals into that family. The standard-family connection and the complete binary-hardness implication remain OPEN. F's assigned chain is frozen at the precise finite quantum implementation obligation above; this is useful partial progress, not a completed standard hardness proof.
