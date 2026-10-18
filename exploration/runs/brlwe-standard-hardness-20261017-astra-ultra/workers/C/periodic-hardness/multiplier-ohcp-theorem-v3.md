# Finite periodic-Gaussian decision to ideal BDD, v3

PROVISIONAL. This coherent statement/proof replaces the v2-plus-addendum working interface; no previous certification is inherited. V1's exact gap record and all earlier immutable versions remain available. This theorem does not assert standard hardness of a restricted ideal family.

Let n>=2 be a power of two, R=Z[X]/(X^n+1), and use the full canonical Euclidean embedding. Let J be an integral ideal given by an ordinary basis, D=N(J), q>=2, L=qJ^-1, and P>=1. Put h=1/(DP) in coefficient coordinates and F=hZ^n/L. Its order is q^n D^(n-1)P^n. Let Q_h be nearest-grid rounding with a fixed tie convention. Gaussian canonical width w means density proportional to exp(-pi||x||²/w²); coefficient width is w/sqrt(n).

Suppose A distinguishes the following EXACT finite experiments with absolute advantage at least delta>0:

    GP: (J,Y_1,...,Y_k), Y_i=Q_h(G_w) mod L independently;
    U:  same J, Y_i independently uniform in F.

All metadata is the same in both worlds. No ideal distribution, short basis, trapdoor, or advice is supplied. The statement is pointwise for every such J. An average-family advantage only yields the corresponding good-ideal conclusion.

Let 0<zeta<=1/8. Fix the primary OHCP algorithm (PRS Proposition4.4 / BRST Lemma3.8). Let T_H(2,kappa) be any fixed valid polynomial bound for that algorithm at confidence kappa+log4, including calls, time, logscales and query representations. The primary theorem supplies a polynomial bound; this packet does not claim an independently verified numerical exponent.

Define h0=delta*w/(32nk),

    a0=D^(1/n) w^(1-2/n) h0^(2/n)/(nq),
    S=max(0,(n/2) log(1/a0)).

Take kappa at least

    max(4S+4n+4log(k+1)+20, 2k, 2/delta, 20log3, log(8n/zeta)),

and sufficiently large that 3w exp(-kappa)<q/(8D). Choose, in order,

    Q_*=n ceil(T_H(2,kappa)),
    epsilon0=min(1/16,zeta/(64kQ_*)),
    a=ceil(sqrt(log(8n/epsilon0)/pi))+1,
    v0>=2sqrt(n)a,
    d0=delta*w/(32nkv0),

enlarging v0 if needed so d0<q/(4D^(1/n)). All bounds can be conservatively rounded by certified arithmetic. The construction has no circular parameter choice because h0=v0d0 is independent of v0.

There is a classical finite reduction which, given rational T=lambda+e with lambda in L and canonical infinity norm ||e||infinity<=d0, recovers lambda with probability at least

    1-(n/2) exp(-kappa)-zeta.

It makes at most Q_* calls to A and has polynomial bit complexity in the input, n,k,log P,1/delta,log(1/zeta),T_H, and A's runtime. The primary polynomial degree is left as published, not invented. There is no quantum step in this BDD reduction.

For each conjugate pair j the hidden center is z*=2+e_j/d0, of norm in[1,3], with scale3. Query using exact integral r in R whose elliptical Gaussian widths are v0 exp(t) on pair j and v0 elsewhere:

    Q_h(r(T-g(z))+G_w) mod L,
    g_j(z)=d0(z-2),  g_i=0 elsewhere.

Exact cancellation gives r(e-g(z))+G_w modulo L. Both Gaussian normalizers are retained in the completion calculation. Uniform posterior smoothing holds for |h_j|<=8d0 and every t>=0. A local comparison-oracle extension makes the error bound valid for arbitrary query positions; it does not assume unknown query confinement. The selected width tends to FULL Haar because every nonzero ideal-dual character has a nonzero selected embedding, with quantitative algebraic-norm smoothing. Fixed nuisance widths preserve the starting gap. The known shift handles zero and tiny coordinates.

Run all coordinate pairs under each of the two global orientations A and 1-A, reconstruct at most two candidates, and verify exact lattice membership and certified distance. No sign-calibration calls are needed. For every generated sample use a single global counter j and numerical error budget zeta/[16(j+1)^2]. The fixed posterior and multiplier normalization errors cost at most 2kQ_*epsilon0/(1-epsilon0)<zeta/16. The summable numerical errors are charged conditionally on each adaptive transcript; the stated conservative total is zeta. The proof specifies scalar samplers, CDF grid sampling, and mean/embedding precision as functions of actual t and j.

Compatibility: B's finite Gaussian-periodic bridge uses coefficient width w_B=w/sqrt(n), with the same h=1/(DP). If gcd(D,q)=1, its fractional output law is D_(J^-1,s) mod qJ^-1, s²=w_B²+r_B², identified with R/qR; its comparator is exactly uniform. A's pointwise fractional-composition theorem is a separate dependency. The present BDD theorem itself does not need gcd(D,q)=1.

A standard quantum BDD-to-DGS import would preserve the same J family, yielding a Gaussian on J at canonical absolute width nq sqrt(n)/(sqrt(2)d0). It does not prove that bounded-index ideals contain the standard arbitrary-ideal worst-case family. That normalization/family edge remains OPEN.

Primary references: [PRS, Pseudorandomness of Ring-LWE for Any Ring and Modulus](https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf), Definition4.3 and Proposition4.4; [BRST, Continuous LWE](https://arxiv.org/pdf/2005.09595), Definition3.7 and Lemma3.8. The new multiplicative query, exact finite interface, and restricted-family interpretation remain provisional pending fresh independent review.
