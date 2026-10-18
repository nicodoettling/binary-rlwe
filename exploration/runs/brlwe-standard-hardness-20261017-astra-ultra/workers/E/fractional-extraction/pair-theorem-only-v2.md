# Quotient-pair extraction from a fractional discrete Gaussian, v2

Let n>=2 be a power of two, K=Q(zeta_(2n)), and R=Z[zeta_(2n)]. Identify K with its rational coefficient vectors in the power basis inside the common ambient Euclidean space V=ℝ^n, equipped with its Borel sigma-field. Let I,H be nonzero integral ideals, let D_I=N(I) and D_H=N(H), and let c>=1 be an integer satisfying cR subset I. Put J=IH/c, L=I intersect J, and G=J/L. For W>0 let D=D_(J,W) be the probability measure on V supported on J with

    D({x}) = exp(-pi ||x||²/W²) / sum_(z in J) exp(-pi ||z||²/W²),  x in J.

Fix gamma>=0 and an integer m>=2. All these ideal data and numerical parameters are deterministic and fixed before sampling. Set

    b = min(1, D_H ((D_I^(1/n)/c+2gamma)/W)^n).

For independent X_1,...,X_m with law D,

    Pr[exists i<j: X_j-X_i in I and ||X_j-X_i||<=gamma c]
      <= min(1, binom(m,2)b).                                      (1)

This event includes zero differences. A measurable selector may inspect the entire list, its G-labels, all norms, arbitrary fixed advice, and independent private randomness. If it returns a signed pair difference with matching labels, its probability of returning a nonzero vector of norm at most gamma c is bounded by (1). The selected indices may depend on the whole list.

The following sequential formulation also holds, with all sample values in the SAME ambient V. Work on a probability space carrying V-valued random variables X_1,...,X_m and history random variables Z_0,...,Z_m. Each Z_j takes values in a standard Borel space S_j. Every preceding history is a measurable function of the next, so F_j=sigma(Z_j) is an increasing sequence of sigma-fields. Z_j records the complete causal history through stage j, including the attempt indicators and all attempted sample values through j, retained private choices and state, and any other information used to choose subsequent attempts or laws. At a missing stage X_j is assigned a fixed dummy value in V and does not count as a sample. These dummy values are recorded as such.

For each stage j=1,...,m let A_j be its {0,1}-valued attempt indicator. It is F_(j-1)-measurable, so the decision whether to attempt stage j is made before seeing its fresh value. The pair event below uses only indices with A_i=A_j=1. Every generated value is charged as an attempted stage, even if the procedure subsequently rejects, deletes or declines to return it. Stopping based on the value at stage j may affect later attempts but cannot turn that already generated stage into an unattempted one.

X_1 may have ANY V-valued law; no approximation or Gaussian premise is imposed on its attempted value. For each j=2,...,m let K_j(z,.) be a regular conditional probability law of X_j given Z_(j-1)=z, regarded as a probability kernel on V. Let eta_j>=0 be deterministic constants. Require

    TV(K_j(Z_(j-1),.), D) <= eta_j
    almost surely on the event {A_j=1},                          (2)

where TV(P,Q)=sup_{B Borel in V}|P(B)-Q(B)|. Equivalently,

    Pr[A_j=1 and TV(K_j(Z_(j-1),.),D)>eta_j]=0.

There is no requirement on unattempted stages or on a null set of histories, and no condition is stated only on positive-mass history atoms. The regular-conditional requirement (2) applies equally to countable and nonatomic standard Borel histories. It does not condition on future successful pairs.

Then

    Pr[exists i<j with A_i=A_j=1,
       X_j-X_i in I and ||X_j-X_i||<=gamma c]
      <= min(1, binom(m,2)b + sum_(j=2)^m eta_j).                 (3)

Any measurable selector returning a tested signed difference of attempted samples has useful-output probability at most (3), where useful means nonzero, in I, and of norm at most gamma c. A quotient-label implementation rejects any out-of-J sample before asking for its label; alternatively it may directly test the difference for membership in I. Approximate laws and X_1 are allowed to have mass outside J because every law and difference test is defined on V.

In particular, if gamma=1, D_H<=2^(rho n), 0<=rho<1, and W>=32sqrt(2)n², then b<=(6/W)^n. Polynomially bounded m and negligible sum_(j=2)^m eta_j give negligible useful-output probability as n tends to infinity through powers of two. In either (1), or (3) with every eta_j=0, useful success at least epsilon>0 requires

    binom(m,2) >= epsilon (W/6)^n,

and hence m >= sqrt(2epsilon)(W/6)^(n/2).
