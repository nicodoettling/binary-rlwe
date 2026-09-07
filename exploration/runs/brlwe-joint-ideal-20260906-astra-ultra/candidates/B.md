# Candidate B, version B1 — source-inherited public shear

Disposition at initial gate: **test or retire as a completion family**. It is distinct from candidate A because its correlation is produced by a public transform of an existing independent-noise source. The exact scope and any successful width choice remain for D02.

Fix public n,q,d, a support law, first and second Gaussian widths gamma,eta, a public shear law P_L and optional independent public broadening law P_W. A base sampler picks hidden J,I, U according to its specified law, V0 independently uniform I given J, and independent coefficient F~D_gamma^n, H00~D_eta^n. The base challenge is (a,c0)=(U+F,V0+H00). The nearest HLBDD comparison has uniform d-subsets, uniform U in I (not active-unit conditioning), and eta=gamma. All laws are wrapped modulo q and approximations must be charged.

The new public source is obtained by independently sampling L,W from the named public laws and publishing (a,c0+La+W). Thus V=V0+LU is uniform independent of (U,F,H) given J and H=H00+LF+W. For every source test D, the public composed test on the base challenge has exactly the same advantage; a uniform pair remains uniform for each fixed a,L,W. This source transfer preserves the base U law. Uniform-U bridge use pays eta_iso=1-(1-1/q+1/q^2)^d; conditioning to active units changes the source.

The main cancellation test sets L=-G' for a fresh independent copy of the auxiliary G. Then the bridge sees FG+H=H00+W+F(G-G'). It uses a fresh G, because the public reduction must sample its own Y without hidden source coins. The known C=G counterexample prohibits identifying these two draws.

For independent centered unwrapped Gaussian L,W,H00, the source shear adds positive semidefinite covariance. This is only a diagnostic. D02 must derive a wrapped/discrete obstruction or a fully correct completion at exact widths, and must not infer a general public-simulator impossibility from covariance alone. Allowing a new F-dependent hidden kernel is a change back to candidate A's unsupported source, not an inherited public transform.

The same rich-support extraction question, common parameter table, exact sample count and task distinction remain mandatory. A correct source transform alone is not a candidate construction if the required target noise cannot be obtained.

## Development disposition, version B1-D

D02 retires the tested negligible-error completion route. For gamma=tau=ell, sigma=2n ell³ and q>=8sigma, the required retained-(J,U,F) noise distance is at least

    (1-pi/16) exp(-2pi) / (96 n² ell⁴ (1+ell)).

This is inverse-polynomial, including an arbitrarily smaller base H00 width and arbitrary independent broadening W. The proof compares the wrapped F0=0 and F0=1 fibers with a coefficient character near 1/(4sigma); it handles complex phases from all other coordinates. Wrapped residue masses dominate the displayed integer Gaussian masses. For iid Gaussian shear L, including L=0, the multiplicative factor cannot make both fibers equal the target character. D02 also states a scoped iid-shear extension.

The exact source transform remains valid. This is a failure of the sufficient strong latent noise premise, not a public source attack, an impossibility for all simulators, or an exclusion of a separately quantified finite-advantage transfer. Letting H depend privately on F to complete the noise returns to A's distinct unsupported source law. See development/D02.md and refinement/R01-compatibility.md for precise scopes; fresh criticism is pending.
