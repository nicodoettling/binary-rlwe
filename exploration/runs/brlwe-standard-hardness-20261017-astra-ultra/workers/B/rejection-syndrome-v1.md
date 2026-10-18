# B-SYN rejection programming: exact cost of a named executable attempt

Status **PROVISIONAL**. This is a scoped runtime failure of response-independent trial generation, not an impossibility for all adaptive public algorithms.

Fix T of size d and the k auxiliary multipliers A. Before inspecting a designated multiplier a', generate M coefficient vectors r^(1),...,r^(M), by any joint law depending on A,T and independent coins. These vectors may be correlated, need not be uniform, and can satisfy any desired small coefficient bound. The executable sampler returns the first r^(t) for which a'-A r^(t) lies in I_T, or fails. The designated a' is independently uniform R; it comes with its externally supplied response b' and is not changed.

Conditional on A,T and the entire trial list, each successful set of a' values is exactly the coset A r^(t)+I_T, of cardinality q^d. Therefore

    Pr[success | A,T,list] = |union_t (A r^(t)+I_T)|/q^n
                           <= min(1,M q^(-(n-d))).

This is pointwise. It neither multiplies conditional probabilities nor assumes independence of successive failed trials. The exact success event concerns the union of cosets; repeated trials can only reduce coverage. A pool of J independent externally supplied designated pairs increases the probability that any pair matches to at most JM q^(-(n-d)) by a union bound. The corresponding true source map keeps the exact comparator from B-SYN and pays failure probability at least 1-JM q^(-(n-d)). Thus polynomial M,J yield an almost-always-fallback source in the intended d=o(n), q=poly(n) regime.

There is an actual algorithmic parameter intersection only if this runtime cost is paid: roughly q^(n-d) response-independent candidate trials are needed for substantial average success. At q>=n² and d<=n/2, any such upper-bound-compatible trial count is at least n^n times a constant success factor. The algorithm is not uniform polynomial time in n. This does not rule out a solver whose candidate list depends algebraically on a' before it is fixed, nor a nontrial inverse construction.

If the ideal is chosen after seeing each residual v=a'-Ar, but must have support size at most d, a trial succeeds exactly when the CRT support size of v is at most d. Under the same response-independent list condition each residual is uniform R, so

    Pr[any trial succeeds] <= min(1,M q^(-n) sum_(t=0)^d binom(n,t)(q-1)^t).

This pays for all possible support choices rather than fixing one. For q>=n² and d=o(n), the reciprocal probability is still exp(Ω(n log n)). It gives no bound for adaptive r depending on a'.

Forward Gaussian/box regularity may show a trial distribution covers nearly every syndrome after averaging its output, but obtaining a *particular supplied syndrome* by these trials retains the inverse image mass q^(-(n-d)). Quantum measurement of a freshly prepared forward superposition likewise produces a new syndrome; identifying it with the external a' without a conditional preparation algorithm is not justified. No general quantum lower bound is asserted here.
