# FF1-MR-WITNESS-v1 (author candidate)

Status: PROVISIONAL; requires fresh exact-version review. This is an obstruction for the named deterministic nearest-integer modulus channel, not a fixed-family impossibility theorem and not an efficient sample-only distinguisher.

Let n>=2, q>=max(4,n sigma) be integers except the real sigma>=1, and define

    R0=2 exp(-pi sigma^2)/(1-exp(-pi sigma^2)),
    Rt=2 exp(-pi sigma^2(1-1/q)^2)/(1-exp(-pi sigma^2)).

Suppose R0+Rt<=1/(16q^2). Let P_{n,q,sigma,k} be the exact q-RLWE planted law retaining the one uniform binary S, all k public A'_i and responses B'_i, with coefficient D_(Z,sigma) errors. Let C_{n,q,sigma,k} be the following continuous-input rounding channel's law, also retaining S:

* S is uniform binary once.
* Independently for each sample, A_i is uniform on the coefficient torus (R/qR)_continuous, represented in [0,q)^n; G_i has independent continuous coefficient density sigma^{-1} exp(-pi x^2/sigma^2).
* B_i=A_i S+G_i modulo q; output A'_i=rnd(A_i), B'_i=rnd(B_i), modulo q, with rnd(x)=floor(x+1/2).

The channel's comparator, formed by replacing B_i by independent uniform coefficient-torus points before rounding, is exactly the q comparator. The full retained-S planted laws satisfy

    TV(P,C) >= 1-2 exp(-k/(2048 q^4)).                         (W1)

For the finite MR-v1 channel from modulus Q>=q, with source width sigma_Q=Q sigma/q, let F_Q denote its full retained-S planted output. Then

    TV(F_Q,C) <= min(1,8 k n(n+1) q/Q),                      (W2)

and hence TV(P,F_Q)>=1-2exp(-k/(2048q^4))-8kn(n+1)q/Q.

In particular, for a fixed polynomial-value q(n), polynomial width sigma(n) growing sufficiently fast that the displayed tail guard eventually holds, and q>=n sigma, the polynomial sample choice k=ceil(2048q^4 n) and sufficiently large polynomial-value Q make the retained-S distance bounded away from zero (indeed arbitrarily close to one by increasing Q). Increasing Q alone cannot provide negligible whole-batch simulation for every polynomial k.

The lower bound uses S to compute residuals. It does not by itself establish any efficient distinguishing gap between the sample-only marginals, or rule out a different kernel, nonstatistical transfer, or the fixed-family objective.
