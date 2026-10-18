Current leading direction graph, 2026-10-17 21:07 UTC. All new positive arrows remain provisional pending their separate gates; computational foundation OPEN.

| Given algorithm | Constructed algorithm | Both endpoints, samples and advantage | Complexity/family boundary |
|---|---|---|---|
| Actual binary-secret recovery Rec, success epsilon on uniform multipliers and coefficient D_sigma errors | FG distinguisher for each eligible J | Same public J; planted iid a_i~D_(J^-1,s) mod q versus iid uniform ring elements. One Rec call, k source points. Advantage >=epsilon-delta_tail-beta-eta-2delta_wrap | Classical expected polynomial wrapper; short basis/G/H exist only in proof. D<=2^(rho n), gcd(D,q)=1. A-FRAC v1; full/source reviews favorable, blind open |
| FG distinguisher of advantage delta | Finite periodic-Gaussian distinguisher | Planted Q_(1/(DP))(G_w) mod qJ^-1 versus exact uniform finite group. Actual implemented output comparator EXACT uniform; planted error <=2k epsilon_b/(1-epsilon_b)+2pi kn/(Pr)+kn nu. Same k input points | Classical expected polynomial bit complexity, ordinary HNF/SNF and scalar samplers. B-GP v1; independent blind gate open |
| Pointwise periodic-Gaussian distinguisher on fixed J | Proposed BDD solver on qJ^-1 | Multiplicative query cancels lattice point exactly, residual plus smooth Gaussian approximates a radial hidden-center oracle; benchmark spherical Gaussian versus Haar/its common finite observation. One-pair widening tends full Haar by ideal norm bound | C v1 proof rejected; v2+domain addendum analytic review survives, coherent finite v3 in preparation. Radius d0=delta*w_can/(32nk v0); polynomial OHCP calls and implementation losses must be charged |
| BDD solver on qJ^-1 | Standard quantum BDD-to-DGS consequence on conjugate J/(nq), if hypotheses verified | Same ideal up to dual/scalar, sampling width sqrt(n)/(sqrt(2)d0), hence on J width n q sqrt(n)/(sqrt(2)d0) | This does NOT remove the bounded-index family restriction. No standard arbitrary-ideal normalization edge exists in the current packet |
| Succinct/decomposed-LWE solver in the new paper | SuperSVP solver through the paper's stated intermediate reductions | General matrix/hint laws, auxiliary decisional LWE and quantum dependencies must be kept | Literature navigation only. No ring-source map or binary-law foundation imported; new SuperSVP premise alone is partial progress |

The first three arrows compose in the algorithm direction shown. They do not run FG sampling backwards, and a hard-looking output does not prove a hard input. C's pointwise ideal premise is available from A/B only when Rec ignores J or has an explicit pointwise target guarantee. An average-over-ideals gap is insufficient. Coefficient/canonical widths differ by sqrt(n).

Earlier direction graph and chronology (statuses are historical):

| Given algorithm | Constructed algorithm | Endpoint and cost | Status |
|---|---|---|---|
| Binary actual-secret recovery at EX-v2 target | Base2 distinguisher at exact EX-v2 source family | One source pair, one solver call; epsilon minus exact guessing/completion/mask/expansion losses | Inherited accepted conditional implication only |
| Binary recovery at A-ADM target | Distinguisher for specified (P,Q) and executable K | One solver call; subtract delta_cmp+delta_bad+beta+eta | A-ADM-v1 provisional; source hardness open |
| Distinguisher for B's broad-mask output | Ordinary RLWE distinguisher | n+2 input samples; exact comparator; one output test; no advantage multiplier | Correct-looking identity but wrong/no-lossy planted geometry; first-test-v1 |
| Public-ideal noisy-point distinguisher for C's actual rounded elliptical law | Ideal-secret RLWE / ideal-modulus Order-LWE distinguisher | Same chosen public ideal; fresh ideal offsets; exact uniform comparator; published quantum reduction/advice parameters retained | C-IDEAL-MAP-v1; source-noise/binary-entropy intersection empty for displayed chain |
| Hidden-ideal distinguisher | Known-ideal distinguisher | Discard public ideal; same advantage | Formal direction only; no average-case hardness theorem is manufactured |

Dense erasure/projection, unrestricted extension of exact-comparator entropy no-go, and ring-tower packing remain failed/scoped controls. More standard input samples remain allowed. No algorithm distinguishing original narrow Base2 has yet been turned into a solver of an established standard-hardness problem at compatible parameters.


Current two-route graph additions (all below provisional unless expressly stated):
| Given algorithm | Algorithm constructed | Endpoints / losses / samples | Open edge |
|---|---|---|---|
| Distinguisher for B-LSW Gaussian ideal source | Ordinary RLWE distinguisher | N=k+m inputs, one call; >=(1-rho)Delta−normalizer_loss−precision; comparator exact | Repaired simulation v2 under audit; dense noise unusable |
| Binary recovery oracle | Possible short-syndrome programmer | A must calculate actual planted-query density; arbitrary responses are off-promise | No algorithm yet |
| Short-vector oracle on one lifted prime | Base prime-ideal short vector by relative norm | DimensionN=r*n0; normp unchanged; approximation factor exponentiates | Source-family modulus restriction and approximation/norm self-consistency |
| Distinguisher for fractional-ideal ratio source | Intended standard ideal-lattice solver | No direction-correct computational map yet | Nonprincipal ideal sampler/short basis and standard hardness absent |

The accepted D-THETA theorem is an analytic statement about an endpoint, not a hardness arrow. C's low-index, dimension-lift and ideal-family notes remain provisional. Published LSW exact reverse-factorization claim failed a theta-normalizer counterexample; version1 is retained, version2 has a new explicit proof. Do not inherit source constants merely because a numerical bound reappears.
