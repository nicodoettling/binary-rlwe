# A-ADM v1: finite admissible-source recovery interface

Status: **PROVISIONAL**. This is an author generalization of accepted EX-v2 §§6–7, not a source-hardness theorem and not a minimality claim. No new acceptance is inherited from EX-v2.

Fix n>=2 a power of two, a split odd prime q, m>=1, t>0 and sigma>0. Use coefficient coordinates in R=F_q[X]/(X^n+1). For t>0 let D_t(z) be proportional to exp(-pi z²/t²) on the integers. Let P and Q be two distributions of the same public challenge X. Let K be an executable randomized public map, with independent local randomness, producing (V,C_1,...,C_m) from X. Its comparator requirement is the full joint bound

    TV(K(Q), mu_V tensor Unif(R)^m) <= delta_cmp.

The baseline target samples V~mu_V, independent uniform a_1,...,a_m, a uniform coefficient-binary S, and mn independent coefficient D_sigma errors E, all jointly independent, and gives (V,(a_j,a_j S+E_j)_j) to a solver. An omitted V is the singleton case. Nonindependent target metadata can instead be treated only by freezing its exact target joint law and verifying the corresponding full comparator; it is outside this displayed product version.

The planted map law K(P) admits a latent random variable Z determining V, an arbitrary subset T of the CRT roots, arbitrary U_j in the SAME I_T, and arbitrary integer coefficient vectors F_j such that C_j=U_j+F_j modulo q. Every dependence within Z is permitted. Neither Z nor its components need be recoverable from X. This entire planted latent law is independent of the wrapper's fresh S and a proof-only G~D_t^n. Good is measurable from Z alone. On Good require

    ||M(Z)||_op <= sigma/(2t),

where M is the complete mn-by-n integer matrix stacking negacyclic multiplication by the F_j. Let delta_bad>=Pr[not Good]. The norm is on the whole stack, including cross-row dependence. Set

    kappa(x)=2 sum_(k>=1) exp(-pi x k²),
    Delta_t=(1+kappa(3t²/4))^n-1,
    eta_t=min(1,Delta_t/(1-Delta_t)) if Delta_t<1, else 1,
    p_t=(1+D_t(0))/2.

For each latent z let D_z be the cardinality of the image of

    {0,1}^n -> R^m,  s -> (U_1(z)s,...,U_m(z)s).

Thus D_z<=min(2^n,q^|T(z)|). Define

    beta = E[1_Good min(1,D_Z p_t^n)].

The source test B_Q receives its sole X, runs K, samples its own independent S and iid coefficient D_sigma errors, calls the target solver once, and accepts exactly if the returned vector equals the ACTUAL S. If epsilon is baseline target success, then the claimed finite conclusion is

    epsilon <= Adv_(P,Q)(B_Q) + delta_cmp + delta_bad + beta + eta_t.

In particular, if |T|<=d on Good, replace beta by min(1,q^d p_t^n). Random, deterministic, nonuniform, hidden or published T are all analytically permitted. No uniform ideal points, uniform support prior, Gaussian masks, or independent masks are required. Their entire joint law and the bad-event probability still must be specified by a concrete source experiment.

Extra metadata V may be any function of Z for the planted bound. Its safe retention in the full reduction additionally requires the stated comparator and an executable K. Proof-only H from Gaussian completion is NOT part of that comparator. Expansion randomness can be revealed only within the planted guessing proof unless a separate joint comparator proves otherwise. All latent/public metadata must remain jointly independent of the fresh S,G.

Runtime is one solver call plus K, n secret bits, mn target Gaussian draws, m ring multiplications and equality testing. No latent ideal, mask, norm witness, or completion sampler is algorithmically accessed. Uniform polynomial time follows only when K, the public parameter family and bounded full-law samplers have that property. Approximate implemented laws pay their own full-law TV losses. This interface proves only target recovery => source distinguishing; the missing source distinguisher => standard RLWE/Order-LWE/worst-case solver edge is a separate obligation.
