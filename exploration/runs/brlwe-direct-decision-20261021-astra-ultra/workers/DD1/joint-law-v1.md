# DD1 joint law, version 1

Frozen 2026-10-21 at startup. Status: reconstructed inherited interface, not a new accepted theorem.

Let n>=2 be a power of two, R=Z[X]/(X^n+1), and q an odd prime congruent 1 modulo 2n. The supplied fixed integral ideal J has D=N(J)<=2^(rho n), rho<1, gcd(D,q)=1. Put Lambda=J^-1. The same ordinary basis of J, or the same decision to omit it, occurs in both worlds. Grouping is one batch of k samples with one shared secret.

The public source P_FG samples unwrapped a_i independently from the exact coefficient discrete Gaussian D_(Lambda,s), then exposes only A_i=a_i mod qLambda under the inclusion isomorphism R/qR -> Lambda/qLambda. It does not expose the unwrapped a_i. The comparator P_U samples independent uniform A_i in R/qR. For either P, independently sample one S uniform in {0,1}^n and kn independent E coefficients from D_(Z,sigma). The planted completion is (J,A,B), B_i=A_i S+E_i. The uniform-response completion is (J,A,U), U uniform in R_q^k independently of everything else. Define

    Delta_D(P)=E[D(J,A,A S+E)]-E[D(J,A,U)].

No law comparison may replace P in only the second term.

For the inherited proof, fix the unwrapped source state z=(J,a_1,...,a_k), and stack coefficient multiplication matrices into M. Its source-only good event bounds ||M||op<=s sqrt(kn)L. On that event take the proof variables

    G~D_(J,t),
    H~D_(Z^(kn),C), C=sigma² I-t² M M^T,

independently conditional on z, with sigma>=2ts sqrt(kn)L. Here the elliptical Gaussian has mass proportional to exp(-pi h^T C^-1 h). The exact convolution mass is

    Pr[MG+H=e]=D_(Z^(kn),sigma)(e) r_e/E_Dsigma[r],

where r_e is the shifted theta ratio for covariance Theta=t² I-(t^4/sigma²)M^T M. The inherited theta bound gives TV<=eta_A, so

    (z,S,MS+E) approximately (z,S,M(S+G)+H).

H is integrated out on the independent-error side. Neither H nor G nor unwrapped a_i is an executable sampler input. Revealing (z,H,S+G) only for the guessing proof is legitimate because S and G retain their product law conditional on (z,H). This proves actual-secret guessing loss, not uniformity of B. No sequential multiplication or selected-stage independence is used.

Exact inherited sources:

- OLD/workers/A/fractional-composition/proof-v1.md, sections 1–4.
- OLD/workers/RF4/same-j-composition/interface-statements-v1.md, I–II.
- OLD/workers/RF4/same-j-composition/same-j-theorem-only-v1.md and OLD/coordinator/samej-acceptance-v1.md.
- RECENT/workers/B/theorem-only-v1.md, proof-v1.md and RECENT/coordinator/ab-acceptance-v1.md.

OLD and RECENT denote the October 17 standard-hardness and October 21 restricted-hardness run roots named in PLAN. The latter result sharpens guessing to the occupied cube-image size C_J; it does not alter the target decision comparator.
