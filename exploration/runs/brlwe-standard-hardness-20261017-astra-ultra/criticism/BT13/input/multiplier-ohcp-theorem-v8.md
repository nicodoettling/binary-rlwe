# Finite periodic-Gaussian decision to ideal BDD, v8

PROVISIONAL. The exact v7/spec1/proof8 packet was rejected at C8-FV1: its final residual test compared a rational bound to a potentially nonrational threshold without a bounded rule. That gap is preserved in C8-FV1-before-repair.md. This revision changes only the final test to an explicitly computed rational threshold, with no change to the BDD promise, success bound, oracle counts or source laws. Fresh exact-byte review is required. This standalone theorem binds multiplier-ohcp-algorithm-v2.md as its complete algorithm definitions and multiplier-ohcp-proof-v9.md as its full proof. BT7 and the v6 causal gap are preserved in v6-gap-record-before-v7-v8.md; no previous certification is inherited. A blind referee must receive this theorem AND the algorithm definitions, without the author proof. V1's exact gap record and all earlier immutable versions remain available. This theorem does not assert standard hardness of a restricted ideal family.

Let n>=2 be a power of two, R=Z[X]/(X^n+1), and use the full canonical Euclidean embedding. Let J be a nonzero integral ideal given by an ordinary basis, D=N(J), q>=2 and P>=1 integers, k>=1 an integer, and L=qJ^-1. Let w>0 and 0<delta<=1. All scalar inputs are rational or efficiently computable with certified polynomial-bit precision; the rational BDD target is encoded in coefficient coordinates. Put h=1/(DP) in coefficient coordinates and F=hZ^n/L. Its order is q^n D^(n-1)P^n. Let Q_h be nearest-grid rounding with a fixed tie convention. Gaussian canonical width w means density proportional to exp(-pi||x||²/w²); coefficient width is w/sqrt(n).

Suppose A distinguishes the following EXACT finite experiments with absolute advantage at least delta>0:

    GP: (J,Y_1,...,Y_k), Y_i=Q_h(G_w) mod L independently;
    U:  same J, Y_i independently uniform in F.

All metadata is the same in both worlds. No ideal distribution, short basis, trapdoor, or advice is supplied. The statement is pointwise for every such J. An average-family advantage only yields the corresponding good-ideal conclusion.

Let 0<zeta<=1/8. The algorithm below is an explicit finite implementation of the PRS comparison/guided-walk method, using the actual author-version pages12–16 and independently checked conservative parameters. No generic exact-real OHCP bit-complexity contract is assumed. Take kappa to be an integer. For the OHCP dimension d_H=2 define, after choosing kappa,

    K=kappa+200,
    T_walk=10^6 K^3 d_H^4,
    Lambda_walk=10 K d_H^2 ceil(log2(2T_walk)),
    C=K+Lambda_walk,
    Lambda_cmp=10000 C^4,
    M=100 C ceil(log2(C Lambda_cmp)),
    Delta=1/(100 C Lambda_cmp M),
    G=100 C Lambda_cmp M^2,
    N=10000 Lambda_cmp^2 M^2 [C+ceil(log2(8(G+1)))],
    Q_H=2(T_walk+1)(G+1)N,
    Q_*=n Q_H.

All loop bounds and grid points are exact integers or rationals. Each comparison estimates both suffix profiles at i Delta, 0<=i<=G, using N calls per point; it compares their weighted empirical maxima with threshold4/Lambda_cmp. The walk has T_walk+1 steps. These formulas bound all calls even when the orientation is incorrect. Maximum logscale is M. Their large polynomial degree is an explicit conservative implementation bound, not a numerical degree attributed to the published theorem.

Define h0=delta*w/(32nk),

    a0=D^(1/n) w^(1-2/n) h0^(2/n)/(nq),
    S=max(0,(n/2) log(1/a0)).

Take kappa at least

    max(4S+4n+4log(k+1)+20, 2k, 2/delta, 20log3, log(8n/zeta)),

and sufficiently large that 3w exp(-kappa)<q/(8D). Choose, in order,

    epsilon0=min(1/16,zeta/(64kQ_*)),
    a=Up(sqrt(log(8n/epsilon0)/pi))+1,
    v0>=2sqrt(n)a,
    d0=delta*w/(32nkv0),

enlarging v0 if needed so d0<q/(4D^(1/n)). The algorithm companion defines Up(x) by certified evaluation to error1/8 followed by a rational upper ceiling; ceil(x)<=Up(x)<=ceil(x)+1. It is used for nonrational precision/cutoff expressions, so no exact equality test against a computable-real integer boundary is needed. All integer-log loop counts defining Q_* are exact and unchanged. The possible one-unit increase of a and numerical precision/cutoffs is the explicitly specified conservative rounding already permitted by v6. The construction has no circular parameter choice because h0=v0d0 is independent of v0. The displayed Q_* is calculated before epsilon0 and v0.

There is a classical finite reduction which, given rational T=lambda+e with lambda in L and canonical infinity norm ||e||infinity<=d0, recovers lambda with probability at least

    1-(n/2) exp(-kappa)-zeta.

It makes at most Q_* calls to A and has polynomial bit complexity in the input, n,k,log P,1/delta,log(1/zeta),kappa, and A's runtime. In particular every loop bound above is polynomial in kappa. Runtime includes the full binary encoding lengths of EVERY supplied scalar (including numerator and denominator lengths), ideal basis, target, and parameter-evaluation routine, plus the actual certified evaluation cost at each requested precision. Polynomial-time scalar representations are part of the declared input model; no bound polynomial only in log of a scalar magnitude is asserted. Rational or explicitly algebraic scalars with polynomial-time certified evaluation suffice. There is no quantum step in this BDD reduction.

For each conjugate pair j the hidden center is z*=2+e_j/d0, of norm in[1,3], with scale3. Query using exact integral r in R whose elliptical Gaussian widths are v0 exp(t) on pair j and v0 elsewhere:

    Q_h(r(T-g(z))+G_w) mod L,
    g_j(z)=d0(z-2),  g_i=0 elsewhere.

This display is the ideal physical analysis kernel. The companion implements it approximately while keeping r an exact integral ring element on every branch and charging its two normalizer/numerical errors. Exact algebraic cancellation gives r(e-g(z))+G_w modulo L. Both Gaussian normalizers are retained in the completion calculation. Uniform posterior smoothing holds for |h_j|<=8d0 and every t>=0. A local comparison-oracle extension makes the error bound valid for arbitrary query positions; it does not assume unknown query confinement. The selected width of the CONTINUOUS GAUSSIAN PROXY tends to full Haar, with quantitative algebraic-norm smoothing. This is not an exact endpoint assertion for the physical discrete-multiplier query. Rational displacements can retain persistent characters and a nonuniform rounded limit; the physical-to-proxy approximation is uniformly bounded by the fixed epsilon0 error instead. BT7's exact counterexample is preserved unchanged. Fixed nuisance widths preserve the starting gap. The known shift handles zero and tiny coordinates.

Run all coordinate pairs under each of the two global orientations A and 1-A, reconstruct at most two candidates, and verify exact lattice membership and certified distance. Both orientations use the same fixed finite loops above. Normalize the scale3 to1 inside the walk; sample each step using B random bits and approximate its exponential to absolute error2^(-B), where B=2M+2K+Up(log2(256Q_*(T_walk+2)/zeta))+10. All empirical comparisons use exact rational arithmetic. The proof couples this walk to the primary real walk through the globally Lipschitz physical query kernel, with total extra loss below zeta/16; it does not require continuity of the analytic patch. No sign-calibration calls are needed. For every generated sample use a single global counter j and numerical error budget zeta/[16(j+1)^2]. The fixed posterior and multiplier normalization errors cost at most 2kQ_*epsilon0/(1-epsilon0)<zeta/16. The summable numerical errors are charged conditionally on each adaptive transcript; the stated conservative total is zeta. The definition-only companion specifies every scalar sampler, finite CDF search, bounded integer-rejection fallback, mean/embedding precision, global sample counter, fresh-coin convention, comparison score and strict decision threshold, walk initialization/update/output, and complete-candidate verification, including an exact rational final threshold computed from a fixed certified relative approximation to d0. Its fixed loops hold on all answer sequences and all target inputs. A must itself have a supplied bounded polynomial runtime on every valid finite input.

Compatibility: B's finite Gaussian-periodic bridge uses coefficient width w_B=w/sqrt(n), with the same h=1/(DP). If gcd(D,q)=1, its fractional output law is D_(J^-1,s) mod qJ^-1, s²=w_B²+r_B², identified with R/qR; its comparator is exactly uniform. A's pointwise fractional-composition theorem is a separate dependency. The present BDD theorem itself does not need gcd(D,q)=1.

A standard quantum BDD-to-DGS import would preserve the same J family, yielding an APPROXIMATE Gaussian sampler on J at canonical absolute width nq sqrt(n)/(sqrt(2)d0), with primary state/gate approximation and coherent BDD error charged separately. It does not prove that bounded-index ideals contain the standard arbitrary-ideal worst-case family. That normalization/family edge remains OPEN.

Primary references: [PRS, Pseudorandomness of Ring-LWE for Any Ring and Modulus](https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf), Definition4.3 and Proposition4.4; [BRST, Continuous LWE](https://arxiv.org/pdf/2005.09595), Definition3.7 and Lemma3.8. The new multiplicative query, exact finite interface, and restricted-family interpretation remain provisional pending fresh independent review.
