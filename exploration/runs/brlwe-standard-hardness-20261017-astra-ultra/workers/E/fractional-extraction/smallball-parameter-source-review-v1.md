# E parameter, complexity and source-scope review

Status: FAVORABLE for the exact scoped fractional-smallball v1 statement. No standard-family foundation or executable fractional composition is certified. Exact theorem/proof hashes and full review are in `smallball-full-proof-review-v1.md`.

## Parameters and asymptotic meaning

All displayed theorem parameters have explicit domains: n>=2 a power of two; I,H nonzero integral ideals; positive integer c with cR contained in I; W>0; gamma>=0; fixed nonzero R-linear T:J->I. The coefficient norm is essential. N(I)<=c^n implies D_I^(1/n)/c<=1, with no requirement that I be principal or c minimal. Norm multiplicativity uses the maximal order R of a power-of-two cyclotomic field, so ideals are invertible.

The diagnostic chain has W=nq/(sqrt(2)d0), d0=delta sqrt(n) w_B/(32nk v0), 0<w_B<=s, v0>=2sqrt(n)a, a>=1, q/s>=1, k>=1 and 0<delta<=1. Direct substitution gives W=(32/sqrt(2)) n^(3/2)k v0 q/(delta w_B)>=32sqrt(2)n². The theorem itself does not require this diagnostic chain. Conditional on that lower bound and D_H<=2^(rho n), rho<1, polynomially many fixed-map outputs have negligible probability even of norm<=c, including zero. One can test this universal asymptotic conclusion with the explicit bound (6/(32sqrt(2)n²))^n; no unspecified tail parameter appears in the small-ball proof.

The theorem makes no runtime claim, does not compute t, y or any short basis, and does not supply a sampler. Ideal data may have arbitrary bit size; polynomial query statements are polynomial in n as stated and require polynomially bounded input descriptions for an ordinary polynomial-time application. The asymptotic probability obstruction even permits arbitrary advice in choosing each prior-measurable map. Allowing that advice here strengthens only this probability bound, not the feasibility of a reduction.

A TV bound is a bound on the complete fresh conditional law, not just moments or coordinate marginals. If the conditional errors vary with the transcript, a deterministic branchwise upper bound suffices; alternatively the proof can explicitly average the random bound, but the frozen theorem uses deterministic eta_j. No distributional independence among outputs is required. A coherent quantum procedure or a decision oracle with a source-averaged advantage would require separate interfaces.

## Exact source endpoints

Fix the SAME public metadata P=(n,R,I,H,c,J,basis descriptions,q,s,k and any declared latent law) in both experiments, with J=IH/c and Lambda=J^-1=cI^-1H^-1. If metadata are random, condition on the identical realized P first. Require gcd(q,cD_ID_H)=1. Then rational natural reduction r_q:Lambda/qLambda -> R/qR is an isomorphism, since at primes dividing q the factors c,I,H are units.

Planted endpoint: conditional on P, independently sample Z_i from exact centered D_(Lambda,s), return A_i=r_q(Z_i), for i=1,...,k. Equivalently, for a in R/qR,

    mu_P(a) = rho_s(z_a+qLambda)/rho_s(Lambda),

where z_a is any lift in Lambda. The full public law is P together with mu_P^k.

Comparator endpoint: the identical P and k independent uniform A_i in R/qR, probability q^(-nk) for each tuple. Any retained latent metadata must have the same original law; output-determining Gaussian samples, offsets or short-basis advice cannot be introduced on one side. A subsequent fresh binary S is independent of both the metadata and the entire tuple; the law must remain uniform coefficient-binary, not merely have the same covariance.

Neither endpoint is automatically hard. In particular, every nonzero lambda in Lambda has ||lambda||>=c/(D_ID_H)^(1/n), so narrow parameters can give a near-zero source and an explicit zero distinguisher. This follows from the exact full centered law, not from covolume alone.

## Scope gates

The small-ball theorem concerns a hypothetical subsequent X from D_(J,W), not the planted multipliers D_(Lambda,s) themselves. It proves no transform from either challenge endpoint to that sampler. The favorable W diagnostic expressly grants an unproved fractional extension. Decision-to-sampling, finite precision, nonzero success and coherent access are separate obligations.

Most concretely, the inspected accepted artifact `workers/A/fractional-composition/theorem-only-v1.md` begins with a nonzero INTEGRAL ideal J and D=[R:J]. Its source is called fractional because the Gaussian lies on J^-1. This is not a theorem for fractional public J=IH/c; D=[R:J] may not even be defined there. A-FRAC F1/F2 remain valid in their accepted scope and cannot be used here without a new statement/proof. The integral B/C interfaces likewise cannot be transferred by changing symbols. No result about ideal classes bridges this gap.

Even if all same-J Gaussian/periodic/BDD steps were independently supplied for fractional J, useful extraction to arbitrary I remains necessary before claiming a standard worst-case ideal problem. The pair mechanism in `pair-extraction-theorem-proof-v1.md` analyzes one such extraction separately and does not repair those source interfaces.

The theorem imports no result from the supplied SuperSVP/SIS paper, no analytic class-number estimate, no standard RLWE/Order-LWE hardness assumption, and no sampler/trapdoor algorithm. The proof uses explicit Fourier/AM-GM identities, ideal multiplicativity/invertibility, centered Poisson summation, packing, TV contraction and a union bound. These ingredients are fully exposed in the proof and require no literature theorem whose hidden parameter regime changes the conclusion.

Original computational objective: UNRESOLVED. This favorable probability audit is a scoped obstruction for fixed maps, not a foundation and not an impossibility result for general reductions.
