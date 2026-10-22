# Proof of FF3-COMPRESSED-SELECTOR-INFORMATION-v1

Fix x. Equation(N) makes the one-trial acceptance probability1/M, so the accepted edge/class distribution is

 Pr[E=e,C=c|X=x,accepted] = mu(e) R(c|x,e) G(e,c),

with R the point mass at c(x,e) in the deterministic case. Fresh proposal trials give a geometric number of trials with mean M. This is conditional on the full fixed x, so there is no marginal-product or postselection independence assumption.

Averaging only after this exact normalization, for every s,e,c,

 Pr[E=e,C=c|S=s] = mu(e) G(e,c) E[R(c|X,e)|S=s] <= M*mu(e).

Hence the optimal guessing probability from(E,C) is

 sum_(e,c) max_s Pr[S=s,E=e,C=c]
 <= sum_(e,c) max_s Pr[S=s] * M*mu(e)
 <= M*L*max_s Pr[S=s].

A randomized estimator cannot improve over the best deterministic guess in each observed cell. Applying a further Markov kernel Y from(E,C) cannot increase optimal guessing probability: simulate the output and the estimator from(E,C). This proves(G), including the general prior. The estimate is capped at1.

The target estimator is a measurable function(or randomized channel) of Y_target. Applying the same estimator to Y changes the event{estimate=S} by at most the retained-secret joint TV eta. Its success on Y is therefore at least1-delta-eta. Combine with(G) to obtain(T). One cannot replace retained-secret TV by unlabelled Y-marginal TV; that would not control this event.

For(I), summing over c shows Pr[E=e|S=s]<=M mu(e), since E[R(c|X,e)|S=s] sums to1 and every G<=M. Therefore D(P_(E|s)||mu)<=log2 M for every s. The identity

 E_s D(P_(E|s)||mu)=I(S;E)+D(P_E||mu)

gives I(S;E)<=log2 M. Also I(S;C|E)<=H(C|E)<=log2 L. Data processing and the chain rule give(I). No assumption that conditioning on an accepted edge preserves the source noise law is made.

For the intended Gaussian target, run only the STATISTICAL estimator from exhaustive-kernel-statement-v1.md with exhaustive-kernel-proof-v2.md: enumerate all binary t and retain a unique centered T-box residual. The corrected competitor inclusion is A(s-t) in[-T,T]^n-E. The integer determinant/rank estimate and Gaussian tail bound give failure<=delta_n, uniformly in every true s. This is a theorem about the target experiment and may use exponential computation; it is not an algorithm inserted for free in a polynomial-time reduction. The displayed q bound makes delta_n negligible at polynomial-value sigma. Apply(T) with N=2^n.

For the exact q2 illustration, n a power of two gives X^n+1=(X+1)^n over F_2. A is a unit iff A(1)=1, which holds for exactly half the uniform coefficient vectors. On this public event, define the estimator A^-1B; choose any estimate otherwise. Conditional on a unit A, A^-1B=S iff E=0, whose probability is(3/4)^n. This supplies the stated lower success probability. No property of Gaussian errors was used or inferred in this rational example.

Regression obligations: M cannot be omitted (selection can concentrate edges); L cannot be omitted (the class may encode the entire input); output factorization cannot be omitted (outputting X may reveal S even with constant class); and nonuniform S cannot be assigned a uniform1/N maximum atom. CP-1 remains rejected; the only geometric product above is conditional on the whole x with literally fresh trials and pointwise acceptance1/M.
