# Worker B first-test report

PROVISIONAL, 2026-10-21. Original computational foundation OPEN. No experiment active.

The frozen B-CUBE-THETA-v1 theorem and complete proof establish the candidate two-sided full-observation bound

    C_J/2^n <= p_guess(S|S+D_(J,t))
      <= min(1,C_J/2^n exp((pi/4+1/2)n/t)),

where C_J is the exact binary cube image size moduloJ. The sharper free-r formula is in theorem-only-v1.md. At t=2n^2 ell, the multiplicative overhead is1+O(1/(n ell)). This closes the residue-versus-full-observation gap at the analytic level, without smoothing or uniform coset masses. New claims remain provisional pending independent review.

B-FV1 passed:40 exact Gaussian/full-guessing HNF cases with rigorous infinite tail,304 degree-eight ternary signed-rotation classes,152 high-index cases, exact old norm2176/image248 control, and CP1's rejected product bound. Exit0,0.49s,19MiB; all code, inputs, exact fractions, full output, stderr, exit, limits and cap evidence are retained in exact-test-v1-*.

A concrete new control is g=1+Y+Y^2-Y^3+Y^7, J0=(g)=(17,Y^2-5Y+1), norm289, additive exponent17, cube image176 with112 singleton/48 double/16 triple fibers. Orthogonal lifts yield N(J)=289^(n/8)>2^n and guessing within factor exp((pi/4+1/2)n/t) of (11/16)^(n/8). The algebraic norm proof, exact laws and checks are in concrete-family-v1.md.

This concrete family is computationally easy in both required senses: its public five-term generator gives an explicit fractional-source coefficient-box test, and its known short multiplication basis/exponent17 meets the coordinator's classical DGS simulation criterion at the actual delivered width. It is a stronger information-only control, not a new hardness intersection. The prior norm2176 family remains retained as the nearest predecessor and is not presented as novelty.

The exact downstream substitution is checked in downstream-compatibility-v1.md. A positive cube-based gap implies a nonzero ternary ideal element, giving a proof-only basis operator norm<=n^2 and D^(1/n)<=sqrt(n). The old t_A,s,sigma and both GP endpoint costs therefore fit; C8's general norm condition and finite quantum width/error/code contract are preserved. This is candidate compatibility, not an accepted extended composition.

Next discriminating mechanism: a standard-family or noncircular transfer that supplies a small cube image while leaving the public ideal outside computably known short-basis and HNF/exponent simulations. Neither the explicit block route nor hiding its displayed generator provides that mechanism. Stop the explicit-generator route as a hardness direction and use remaining allocation for nonauthor/fresh-blind review or a coordinator-selected task.
