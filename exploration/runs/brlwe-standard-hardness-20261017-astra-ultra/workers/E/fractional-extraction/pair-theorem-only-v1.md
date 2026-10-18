# Quotient-pair extraction from a fractional discrete Gaussian

Let n>=2 be a power of two, K=Q(zeta_(2n)), and R=Z[zeta_(2n)]. Identify K with its rational coefficient vectors in the power basis and use the coefficient Euclidean norm. Let I,H be nonzero integral ideals, let D_I=N(I) and D_H=N(H), and let c>=1 be an integer satisfying cR subset I. Put J=IH/c, L=I intersect J, and G=J/L. For W>0 define the exact centered discrete Gaussian on J by

    D_(J,W)(x) = exp(-pi ||x||²/W²) / sum_(z in J) exp(-pi ||z||²/W²).

Fix gamma>=0 and an integer m>=2. All public ideal data and parameters are fixed before sampling. Let X_1,...,X_m be independent with law D_(J,W). A selector may inspect all sample values, their labels in G, all norms, arbitrary fixed public advice, and independent private randomness. It either fails or returns one signed pair difference X_j-X_i, with i<j and equal labels in G. A useful output is nonzero and has norm at most gamma c.

Define

    b = min(1, D_H ((D_I^(1/n)/c+2gamma)/W)^n).

Then

    Pr[exists i<j: X_j-X_i in I and ||X_j-X_i||<=gamma c]
      <= min(1, binom(m,2)b).

The event includes zero differences. Consequently the useful-output probability of every selector described above has the same upper bound, even though its selected pair can depend on the entire sample list.

The following sequential version also holds. Let the next sample be generated after the full prior transcript, possibly with adaptive stopping before m samples. The transcript includes all retained classical choices, sample values, private coins and state relevant to future choices. For each j>=2 and every positive-probability prior branch at which that trial is attempted, suppose the conditional law of X_j has total variation distance at most eta_j from D_(J,W), where eta_j is a deterministic nonnegative bound. The distribution of X_1 may be arbitrary. Missing or aborted trials contribute no pair event. Samples outside J may be rejected by a quotient-based selector; alternatively a selector may directly test whether a returned difference is in I. Then

    Pr[exists an attempted pair i<j with X_j-X_i in I
       and ||X_j-X_i||<=gamma c]
      <= min(1, binom(m,2)b + sum_(j=2)^m eta_j).

Any selector returning a tested pair difference has useful-output probability at most this quantity. No conditional guarantee is assumed after conditioning on future successful pairs.

In particular, for gamma=1, D_H<=2^(rho n), 0<=rho<1, and W>=32sqrt(2)n², the parameter satisfies b<=(6/W)^n. Polynomially bounded m and negligible total conditional sampling error give negligible useful-output probability as n tends to infinity through powers of two. For exact sampling, useful success probability at least epsilon>0 requires

    binom(m,2) >= epsilon (W/6)^n,

and in particular m >= sqrt(2epsilon)(W/6)^(n/2).
