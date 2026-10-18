# C-UNI v1: statistically uniform rows cannot be binary-lossy through small additive masks

**PROVISIONAL**, not independently reviewed. This is an obstruction to a specified proof interface, not a computational hardness impossibility or a general attack.

Let n>=2 be a power of two, q an odd completely splitting prime, R_q=F_q[X]/(X^n+1), and k>=1. Let A=(A_1,...,A_k) be any source whose first marginal has total variation distance at most δ from uniform R_q. Consider any joint latent decomposition

    A_j=U_j+F_j mod q,

where U_j∈R_q, F_j∈Z[X]/(X^n+1), with no independence or ideal-distribution assumption. The latent decomposition may depend arbitrarily on the whole source. Let M_Fj be coefficient negacyclic multiplication and M the vertical stack of these matrices. Let Good be any latent event on which ||M||_2≤S, for a fixed real S>=0.

Define Ψ_U:{0,1}^n→R_q^k by Ψ_U(s)=(U_1s,...,U_ks). Then

    Pr[Good and Ψ_U is noninjective]
       ≤ δ + min{1,[2sqrt(e n)/q + 2sqrt(2πe) S/q]^n}.       (UNI)

Here e is Euler's number. The bound is uniform over all latent decompositions and all Good events. It does not require the decomposition to be efficiently computable.

Consequently, if a completion/guessing bound uses

    δ_bad=Pr[not Good],
    β=E[1_Good min{1, |image Ψ_U| p^n}],       p>=1/2,

then

    δ_bad+β ≥ 1-δ-min{1,[2sqrt(e n)/q+2sqrt(2πe) S/q]^n}.   (VAC)

For q>=n², τ>=1, c>0, and S≤σ/(2τ)≤q/(2τ n^c), the bracket is at most

    2sqrt(e)n^(-3/2)+sqrt(2πe)/(τ n^c),

which tends to zero. Its nth power is negligible. Therefore when δ is negligible, this particular completion/guessing upper bound is at least 1-negl. It cannot prove negligible binary recovery. This statement permits any public or hidden ideal family and any alternative mask representative; it concerns the small-mask, full-ideal-image-revelation interface only.

The conclusion remains a proof-method obstruction. It does not recover a binary secret from the public source and does not preclude another proof avoiding the revealed image, another target, or a source that is only computationally pseudorandom rather than statistically close to uniform.
