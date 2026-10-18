# Multiplicative Gaussian oracle to bounded-index ideal decoding, v2

PROVISIONAL — repaired theorem candidate, requiring fresh independent review. See ohcp-v1-gap-and-repair-record.md; no v1 review is inherited. This is an analytic reduction with finite implementation obligations stated explicitly. It does not establish standard hardness of the restricted ideal family.

Let n>=2 be a power of two, R=Z[X]/(X^n+1), and H its full canonical Euclidean embedding (both members of each conjugate pair included). Let J be any nonzero integral ideal, D=N(J), q>=2, and L=qJ^-1. No distribution on J is assumed. Write GP_(J,q,w) for a spherical continuous Gaussian of canonical width w reduced modulo L, and U_L for Haar on H/L. Gaussian width s means density proportional to exp(-pi||x||²/s²).

Suppose an algorithm A on k iid quotient samples has signed gap at least delta>0 between GP_(J,q,w)^k and U_L^k. The sign can be calibrated from efficiently generated samples and reversed. A may be arbitrary; no monotonicity, Lipschitzness, or Fourier concentration is assumed. All evaluations must use a common specified finite observation kernel, or else the following first constitutes an ideal-real-oracle theorem.

Choose a confidence parameter kappa polynomially large in n,k,1/delta and the bit lengths of J,q,w and the rational target T. Let epsilon=exp(-kappa²), let v0>=2 eta_epsilon(R) be a computable Gaussian-sampling bound (v0=O(sqrt(n)(kappa+sqrt(log n))) suffices), and set

    d0 = delta*w/(32*n*k*v0).

Also require d0<q/(4 D^(1/n)). Given T=lambda+e with lambda in L and ||e||_infinity<=d0, the proposed classical reduction recovers lambda with probability 1-exp(-Omega(kappa)), using polynomially many calls to A and polynomial-bit Gaussian arithmetic. A basis of J is the only ideal-specific input; no short-basis advice, trapdoor, random ideal law, or quantum computation is used in this BDD step.

For a selected conjugate pair j, a candidate z in C, and logscale t>=0, set g(z) in H to have coordinate d0*(z-2) in pair j and zero elsewhere. The hidden center is z*=2+e_j/d0, whose norm lies in [1,3]; use OHCP scale3. Sample r from the elliptical discrete Gaussian on R with width v0*exp(t) in pair j and width v0 in every other embedding. Independently sample G_w, and supply k iid copies of

    Y = r*(T-g(z))+G_w mod L

to A. Because rL is contained in L, the exact residual law is r*(e-g(z))+G_w mod L. Uniform posterior smoothing makes this epsilon-close to an elliptical continuous Gaussian. Its other widths remain fixed, while pair j has width sqrt(w²+(v0*d0*exp(t)*|z-(2+e_j/d0)|)²). Thus it is a two-dimensional oracle-hidden-center instance.

The centered Gaussian gap survives the small fixed nuisance widths. Increasing only pair j's width tends to FULL Haar on H/L, with polynomial logscale: for widths at least w except pair j of width W, PRS17 Lemma6.9 gives smoothing once

    c = [D*w^(n-2)*W²]^(1/n)/(n*q) >= 1,

with smoothing error exp(-n*c²). Every nonzero ideal-dual character is a nonzero field element and has nonzero value in every embedding. Consequently there is no proper-subtorus obstruction here. This resolves an earlier coordinator concern; it does not apply to a product algebra with zero divisors.

The known center shift handles zero and tiny coordinates without an algebraic lower-bound promise. Repeated hidden-center recovery for each pair gives all coordinates of e; rational-grid rounding then recovers lambda exactly. An average-over-J gap would only yield decoding on the corresponding good ideals. The stronger pointwise gap furnished by the proposed binary-recovery composition is necessary to obtain this result uniformly for all admissible J.

Finite implementation obligations: (i) a common finite observation kernel for A and its two benchmark laws; (ii) elliptical discrete Gaussian sampling from R by the explicit continuous-convolution and coordinate-rounding construction; (iii) polynomial precision through exp(poly(kappa)) multiplier widths, with negligible translation error after adding G_w; (iv) accounting for all adaptive oracle calls. The proof packet gives proposed bounds; these operational statements require review before upgrading this to a fully implemented reduction.

Primary imported results: Peikert–Regev–Stephens-Davidowitz, [Pseudorandomness of Ring-LWE for Any Ring and Modulus](https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf), Proposition4.4 (OHCP) and Lemma6.9 (elliptical ideal smoothing). BRST [Continuous LWE](https://arxiv.org/pdf/2005.09595), Lemma3.8, independently states the OHCP version used here. The multiplier query and its application to this known-ideal periodic oracle are new provisional work.
