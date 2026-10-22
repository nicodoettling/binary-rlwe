# Constructive good-secret preselection with a charged prior change

Exploratory alternative under the existing all-input bounded, fresh-execution distinguisher model. It is not accepted as a new reduction and does not repair the fixed-family noise quantifiers.

Let g(s) be the signed acceptance gap of supplied distinguisher code on a full promised k-sample batch conditional on secret s, with fresh independent uniform multipliers, exact/charged coefficient errors, and the comparator having uniform responses. If E_uniformS g(S)>=epsilon>0 and -1<=g<=1, then

 Pr[g(S)>=epsilon/2] >=epsilon/(2-epsilon)>=epsilon/2.

A wrapper which knows its own generated S can estimate g(S) using synthetic full target and comparator batches. A finite number O(epsilon^-2 log(1/delta)) of independent code executions gives estimation error at most epsilon/8 with probability at least1-delta (each execution still contains one shared S). Accept S if its estimated gap is at least3epsilon/8. If g(s)>=epsilon/2 its acceptance probability alpha(s) is at least1-delta; if g(s)<epsilon/4 it is at most delta. These are full fresh-execution statements, not amplification of one cached transcript. Finite Gaussian approximation must be charged across every synthetic sample; all code costs depend on the supplied resource bounds.

Draw a fresh uniform S and fresh estimation randomness on every one of R attempts, retaining only the first accepted S and discarding the synthetic transcript. Let a=E alpha(S). For delta<=1/2, a>=epsilon/4. Exactly, the probability of no acceptance is(1-a)^R. Conditional on acceptance within any fixed R>=1, the retained secret has law

                 pi(s)=2^-n alpha(s)/a,

so pi(s)<=4*2^-n/epsilon. Its probability of g(s)<epsilon/4 is at most delta/a<=4delta/epsilon. To justify the geometric formula, every full-history conditional trial draws a new S and new independent code/sampler randomness; reusing a hidden calibration tape is excluded. The synthetic calibration is independent of the later source public data. The output transcript must not provide extra S-dependent advice to the source estimator.

This supplies a real possible good-secret amplification mechanism in the wrapper, beyond refreshing only decision coins. It changes the secret prior and must charge that change. For any fixed nonnegative event functional f(s), E_pi f<=4 E_uniform f/epsilon. The same likelihood-ratio bound applies to full joint events when the conditional source law given s is unchanged. Consequently an inherited small statistical guessing upper bound can grow by the factor4/epsilon. The method does not turn a uniform-secret source bound into a pointwise secret bound for free.

In particular, the inherited fixed-family obstruction is not removed: each promised execution still consumes k physical samples, and its source completion still has a sqrt(K) floor before any additional calibration cost. The target's coefficient-Gaussian width remains fixed before all k exponents; preselection alone changes neither that floor nor the exact fractional-public endpoint. The finite preselection runtime and prior factor can be useful only inside a genuinely different source comparison or shared-secret synthesis argument. A possible use is to strengthen a conditional extractor after a separate completion breakthrough; no such breakthrough is supplied here.

The signed orientation can be tried in two separate bounded branches when only an absolute gap is promised. Mixing branches or selecting a branch from a cached adaptive transcript requires its own accounted schedule. This note does not quietly assume all secrets have a gap or that source observations can be conditioned on acceptance without changing their posterior.
