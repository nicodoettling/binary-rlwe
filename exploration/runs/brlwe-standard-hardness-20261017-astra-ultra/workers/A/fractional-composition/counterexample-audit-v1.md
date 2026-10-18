# Counterexample search before composition proof

2026-10-17. These are analytic falsification checks, not an experiment. No experiment reservation was requested or used.

I checked the C finite-coset argument against correlated correction noise. Its Markov step remains valid because E' is drawn from a kernel depending ONLY on K=E mod J. Revealing E' can reveal much about K, but at most D possibilities are charged. The kernel is allowed unbounded support and is not assumed independent of E without conditioning. The elementary sum-of-maxima inequality remains valid under this dependence.

The restriction is necessary. If a purported correction were allowed to depend on the full E, the rule E'=-E would make S+E+E'=S and defeat any small-guessing bound; for J=Z^n, K is constant, so that rule is not an allowed kernel. Likewise a choice of J depending on the fresh S could encode information about S; our actual source law explicitly excludes this. Giving a public short basis changes computational distinguishability, but does not invalidate the fixed-J information proof.

I also checked the more direct Gaussian-on-J route for a normalizer counterexample. One cannot simply claim G~D_(J,t) has the same marginal coordinates as D_t^n. The exact guessing expression contains 1/rho_t(J). The inequality rho_t(Z^n)<=D rho_t(J), proved by shifted theta and a complete coset partition, supplies precisely the required factor D. It is valid even for nonspherical J and below smoothing. Thus no uniform-coset assumption is needed. The distribution of G modulo a proper sublattice may be nonuniform; the proof does not condition a product law on that residue.

As limiting checks: J=Z^n gives equality with p_t^n; t tending to zero gives guessing approaching one and the min(1,Dp_t^n) guard is necessary; a large-index ideal can make the entropy term vacuous; publishing H alongside independent target noise would destroy the claimed noise-comparison joint law, so H is integrated out before comparison and is revealed only in the completed-world guessing proof. These checks found no counterexample within the frozen hypotheses. They do not replace independent review.
