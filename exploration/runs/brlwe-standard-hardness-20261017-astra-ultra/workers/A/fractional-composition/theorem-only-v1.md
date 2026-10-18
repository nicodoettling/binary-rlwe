# A-FRAC v1: finite actual-secret recovery from fractional Gaussian source

Status: PROVISIONAL author theorem, pending independent proof/source/complexity reviews. This theorem is a conditional source-to-target composition, not a standard computational foundation. All Gaussians in the target and proof below are explicitly discrete; no TCC Gaussian law is imported.

Let n>=2 be a power of two, R=Z[X]/(X^n+1), q an odd split prime, and k>=1. Work in coefficient Euclidean coordinates. Let Gen output one nonzero integral ideal J with D=[R:J], gcd(D,q)=1, and D<=D_max. Put Lambda=J^-1. Assume each possible J has SOME row basis B_J with ||B_J||_op<=tau2. This is an existence hypothesis; no algorithm, oracle or public metadata receives B_J. An ordinary HNF description of J may be public. The same metadata is retained in both experiments.

The source FG_s is (J,A_1,...,A_k), where conditional on J, independently a_i~D_(Lambda,s), and A_i=a_i mod qLambda identified with R_q through inclusion R subset Lambda. Here D_(L,s)(x)=exp(-pi||x||²/s²)/rho_s(L). The comparator U is the SAME J~Gen and k independent uniform A_i in R_q, independent conditional on J. J can instead be discarded consistently from both worlds. Unwrapped a_i, a short basis, and auxiliary proof variables are not public.

Let L>0, t>0, and target width sigma>0 satisfy

    sigma >= 2 t s sqrt(kn) L.

Define

    delta_tail = min(1,4kn exp(-pi L²)),
    kappa(x) = 2 sum_(j>=1) exp(-pi x j²),
    Delta = (1+kappa(3t²/(4tau2²)))^n-1,
    eta = min(1,Delta/(1-Delta)) if Delta<1, otherwise 1,
    p_t = (1+D_t(0))/2,
    beta = min(1,D_max p_t^n).

The target distribution samples the same optional metadata J, k independent uniform multipliers in R_q, one independent uniform coefficient-binary S in {0,1}^n, and kn independent coefficient D_sigma integer errors. A target recovery algorithm Rec has actual-secret success epsilon in this distribution. The public wrapper D_Rec, on a source tuple, samples its OWN fresh S and these independent errors, constructs (A_i,A_i S+E_i), calls Rec once and accepts exactly when its answer equals the ACTUAL S. Under ideal exact wrapper sampling,

    epsilon <= Adv_(FG_s,U)(D_Rec) + delta_tail + beta + eta.       (F1)

Adv is the absolute difference of acceptance probabilities. The full comparator completion is EXACTLY the target joint law, including S for the acceptance experiment and any retained J. The full planted completion is EXACTLY the same wrapper with fractional-Gaussian source multipliers. The three errors in (F1) arise only in the planted analytic bound. If the entire implemented wrapper law is within delta_wrap of the ideal wrapper for every challenge, the executable distinguisher instead satisfies (F1) with +2delta_wrap.

The conclusion is pointwise in J when Gen is concentrated on any admissible J. If Rec ignores metadata J, its epsilon is the original target success for EVERY such J, so the resulting advantage lower bound is uniform in J. No average-case ideal-family premise is needed for this implication.

For every integral ideal J in this power-of-two ring one has the unconditional EXISTENCE bound

    tau2 <= n² D^(1/n).                                       (F2)

Thus choosing the common numerical upper bound tau2=n² D_max^(1/n) always satisfies the geometry hypothesis. This does not imply that a corresponding basis can be found or published efficiently. A public short basis can distinguish FG in this parameter range, as B separately demonstrated.

For B's periodic bridge, set s=sqrt(w²+r²), r>=eta_(epsilon_b)(Z^n). Its source GP has conditional-J iid continuous G_w mod qLambda; its comparator is Haar on R^n/qLambda. If the bridge's full implemented endpoint losses sum to at most 2k epsilon_b/(1-epsilon_b)+delta_num, then the composed executable GP distinguisher obeys

    epsilon <= Adv_GP + delta_tail + beta + eta
                 + 2k epsilon_b/(1-epsilon_b) + delta_num
                 + 2delta_wrap.                             (F3)

This last statement explicitly depends on B's separate simulator theorem. No assertion is made here that GP is hard from ordinary RLWE, Order-LWE, worst-case BDD or ideal-SVP. A verified reduction to that exact pointwise or Gen-distributed GP experiment remains necessary for a standard foundation.
