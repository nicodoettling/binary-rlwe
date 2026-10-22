# FF3-COMPRESSED-SELECTOR-INFORMATION-v1

Let S be uniform on a finite set of N secrets, and let X have any conditional law given S. Let E be a finite proposal set with a fixed distribution mu independent of(S,X). For every x,e compute a deterministic class C=c(x,e) in an alphabet of size at most L. Let nonnegative weights G(e,c)<=M satisfy

 sum_e mu(e) G(e,c(x,e))=1                       for EVERY x.             (N)

The selector draws proposals e~mu and accepts with probability G(e,c(x,e))/M using independent coins, repeating until acceptance. It retains only the accepted E and its class C. The output Y is drawn from a Markov kernel depending ONLY on(E,C), using fresh randomness independent of(S,X) given(E,C). In particular Y cannot also retain full(A,B), fine residual coordinates, an input-correlated continuous state, or hidden advice. Nonuniform precomputed tables are allowed, but their output access is still only(E,C).

Then the expected number of trials is exactly M at every x, and every estimator of S from Y has success probability at most

                       min(1,M*L/N).                                  (G)

More generally, with any prior on S the bound is min(1,M*L*max_s Pr[S=s]). The same result holds for a randomized class if its law R(c|x,e) is declared, (N) averages over that law, the weight bound is pointwise, and the output uses only the accepted(e,c) and fresh coins.

Let a target pair(S,Y_target), with the same uniform S, admit an arbitrary estimator with success at least1-delta. If the retained-secret joint law(S,Y) is within total variation eta of this target, then

                       M*L >= N*(1-delta-eta).                         (T)

The estimator in this statistical bound need not be efficient. Its existence does not give the transfer algorithm a source decoder, secret advice, or the actual S.

A companion information inequality under the same model is

                       I(S;Y) <= log2 M + log2 L.                     (I)

It is supplementary; (T) suffices for the Gaussian corollary and avoids entropy continuity estimates.

Gaussian target corollary: take power-of-two n, uniform binary S in Z[X]/(X^n+1), an odd prime target q, uniform A, and exact independent coefficient D_Z,sigma errors, sigma>=1. Put T=ceil(sigma*n), require4T+1<q, and suppose

 q >=16*n*(4T+1).

The FF3-ENUM statistical estimator has error at most

 delta_n = n*(2+sigma^2/(pi*T))*exp(-pi*T^2/sigma^2)
           +(2^n-1)*((4T+1)*sqrt(n)/q)^n.

For polynomial-value sigma, delta_n is negligible. Consequently every compressed selector satisfying this model and achieving negligible retained-secret target TV eta_n requires

                       M_n*L_n >=2^n*(1-delta_n-eta_n).

In particular, polynomial L_n and polynomial M_n cannot realize this target family. The target parameters precede the selector/adversary exponents. One may choose sigma=n^2 and any fixed effective odd-prime polynomial-value family q(n)>=16n(4ceil(sigma*n)+1); the displayed numerical inequality, not a bare asymptotic q>=n^5 at small n, is authoritative.

The compact zero-count class(zero_count(A),zero_count(r_u),zero_count(r_v)) has L<=(n+1)^3. Output sampling from radial target weight classes and recombining using the accepted edge factors only through edge+class, so (G)-(T) apply. Enlarging the class by any polynomial number of polynomial-value norm/energy statistics still has polynomial L only when the NUMBER of such statistics is fixed; an n-dimensional coordinate vector generally has an exponential alphabet and is not covered. General residual-dependent H, arbitrary input-dependent kernels, and a sampler retaining input information outside the class remain live alternatives.

Exact rational q2 illustration (not Gaussian substitution): for n a power of two, uniform S in R_2 and coefficient Bernoulli(1/4) errors, half the A are units. On those inputs A^-1 B estimates S correctly whenever E=0, so target guessing success is at least(1/2)*(3/4)^n. Every EXACT compressed selector therefore satisfies M L>=(1/2)*(3/2)^n. For merely negligible approximation, this exponentially small event bound alone may be vacuous; (I) combined with I_target>=n*(1-h2(1/4))/2 still gives an exponential M lower bound after an appropriate retained-secret entropy analysis. That approximate q2 corollary is NOT used here.
