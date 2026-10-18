# Planted information retention for binary-injective ideals, theorem v1

PROVISIONAL author theorem. This is an information-theoretic test of one exact inverse-ideal source/target wrapper, not computational hardness, an efficient public recovery algorithm, or a universal barrier to different sources.

Let n>=2 be a power of two, R=Z[X]/(X^n+1), and J a nonzero integral ideal of normD>=2. Assume the coefficient-binary map{0,1}^n->R/J is injective. Let a row basis j_1,...,j_n of J exist with coefficient matrix operator norm<=tau. It need not be supplied or efficiently found. Let q be an odd split prime coprimeD, k>=1, source widths>0, target widthsigma>0 and L>0. SetLambda=J^-1 and assume

    q > 2 tau sqrt(n) L (n s+sigma).

Sample independent a_i~D_(Lambda,s), public A_i their natural reductions toR/qR; independent uniform binaryS and independent coefficient discrete-Gaussian E_i~D_(R,sigma); publish(A_i,B_i=A_i S+E_i modq)_i. The comparator replaces the A_i with iid uniformR/qR, retaining exactly the same independent S/error laws and identical optional J metadata. This theorem bounds ONLY the planted optimal guessing probability; it asserts no comparator recovery value.

Define kappa_s=2 sum_(m>=1)exp(-pi s²m²), Delta_s=(1+kappa_s)^n-1, and eps_s=min(1,Delta_s/(1-Delta_s)) ifDelta_s<1, otherwise1. Let

    chi_J(k)=sum_(prime ideals P dividingJ) N(P)^(-k),
    delta_tail=min(1,8kn exp(-pi L²)).

Then the planted optimal actual-secret guessing success from the public tuple, with J supplied, is at least

    max(0,1-delta_tail-chi_J(k)-k eps_s).

The exact ideal sum may be replaced by the explicit upper bound

    1_(2 dividesD) 2^(-k)
      + (log D/log(2n+1)) (2n+1)^(-k).

No factorization algorithm is required by this bound. The decoder in the proof may enumerate short bases and all2^n secrets; no polynomial runtime is claimed.

More generally Gen may choose J from any countable family of ideals satisfying these hypotheses before S, with a common tau,Dmax,q,s,sigma,k,L and a common upper boundchi. The same success bound holds for the full averaged planted experiment even if J is discarded: conditioned on publicA, the response channel and secret prior are independent ofJ, so J supplies no additional INFORMATION aboutS after(A,B). This does not say that J or a short basis cannot supply additional computational help. The theorem is pointwise/averaged information retention, not an efficient algorithm or a distributional hardness theorem.

For scope, accepted existence geometry permits tau=n²D^(1/n). Thus forD^(1/n) bounded by a polynomial and q sufficiently larger than sigma by the displayed polynomial factor, the test has a nonempty large-modulus window whenever supplied split primes meet it. Choosing s to makeeps_s negligible and L to makedelta_tail negligible leaves the explicit prime-divisor loss. No claim that every parameter window in the original binary problem meets the unwrapping inequality is made. No theorem about source indistinguishability is inferred.
