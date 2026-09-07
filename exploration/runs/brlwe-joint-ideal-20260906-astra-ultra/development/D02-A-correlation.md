# D02 — attempt to expose candidate A1's completion correlation

Provisional bounded deductions on 2026-09-06. No experiment. This note uses only candidate A1 and the source-inherited B1 family; it does not introduce a third candidate.

## Exact source under investigation

For power-of-two n, fully split prime q, ell=ceil(log2 n), d=max(1,floor(n/ell^3)), gamma=tau=ell, b=ell^2 and sigma=2n ell^3, draw T uniformly among d-subsets of CRT roots. Put J={r:r vanishes on T} and I=Ann(J), supported on T. Draw U with independent uniform nonzero active coordinates, and V independently uniform in I conditional on T. Independently draw F coefficientwise from D_ell conditioned on |F_j|<=b (or its fixed finite-table implementation). Let

    B_F=sigma^2 I_n-tau^2 M_F M_F^T.

Sample H from the exact implemented adaptive LDL kernel H_impl(B_F) in F02-completion.md and publish (A,C)=(U+F,V+H) mod q. H is independent of the later G and binary S, conditional on F. This is the exact source being tested; it is not an independent Gaussian at width sigma. Replacing its F-dependent law changes the assumption.

## A-D02-1: the F/H dependence is not negligibly removable at the latent level

Let K_A be A1's joint law of (J,U,F,H), and let K_B use the same law of (J,U,F) but H=H00+LF+W from D02-B1, with the independent iid public shear law and fixed independent base/broadening laws specified there. Append an independent G~D_tau^n and map the resulting tuple to (J,U,F,FG+H mod q). If A1's completion error is eta_A and delta=TV(K_A,K_B), then data processing and the triangle inequality give

    eta_noise(B)<=eta_A+delta.

The two-fiber wrapped character bound therefore implies

    delta >= b0 exp(-2pi)/(96 n^2 ell^4(1+ell))-eta_A,          (A-D1)
    b0=1-pi/16,

whenever q>=8sigma. This is nonnegligible if eta_A is negligible. With implemented F,H and a comparison to ideal probabilities, subtract the explicitly budgeted negligible implementation distance as well. One may alternatively apply the general D02-B1 formula to the actual two coefficient masses of the finite F table; those masses remain inverse polynomial.

This rules out an uncharged *latent* negligible-TV replacement of A1 by any tested independent-noise/public-iid-shear family. It does not prove a source distinguisher: F and the noise H are hidden behind A and C, and the public projection can reduce statistical distance. Candidate A is outside D02-B1's hypothesis precisely because its H kernel varies between the F0 fibers. Its correction is the mechanism that prevents the common-x factorization.

## A-D02-2: first-mask uniqueness is information-theoretic, not an efficient decoder

A useful attempt is to ask whether hiding F as a source coin really loses information. Suppose two representations obey

    A=U+F=U'+F' mod q,

where U,U' have at most d active CRT coordinates and all centered F,F' coefficients are bounded by b. Assume 2b<q and

    q^(1-2d/n)>2b sqrt(n).                                  (A-D2)

Then F=F' as integer coefficient vectors. Indeed w=F-F' lies modulo q in the sum of two ideals with at most 2d active coordinates, so it vanishes at at least n-2d CRT roots. If w is nonzero in the cyclotomic field, its nonzero integer field norm is divisible by q^(n-2d). On the other hand AM-GM over its n embeddings and the orthogonality of the power-of-two canonical embedding give

    |Norm(w)| <= (||can(w)||_2/sqrt(n))^n
              = ||coeff(w)||_2^n <= (2b sqrt(n))^n,

contradicting (A-D2). Therefore w=0. With active-unit U, its support also determines T uniquely.

For A1, q>=2n ell^3 n^c, q<=n^K and d/n<=1/ell^3 imply q^(1-2d/n)=q exp(-O(log(n)/ell^3))=q(1-o(1)). This exceeds 2ell^2 sqrt(n) eventually, so (A-D2) holds along the qualifying parameter sequence. Thus A contains enough information to determine F uniquely among the permitted sparse-CRT/noise decompositions.

**Algorithmic limit.** This norm argument is not a polynomial algorithm for recovering F or T. Computing that unique decomposition is exactly an approximate ideal/support decoding task. Enumerating all F tables or all supports is not polynomial at A1's d. The frozen grouped-super-support algorithm in F03-attacks.md supplies an exp(O(d)) route under its additional explicit gap; that remains superpolynomial here. This uniqueness observation does not silently strengthen that algorithm's bound.

If an efficient algorithm did recover such an F on a nonnegligible fraction of A1 inputs, verification would be public: check the coefficient box and that A-F has at most d nonzero CRT coordinates. A uniform A passes existence of some such F with probability at most

    (2b+1)^n sum_(j=0)^d binom(n,j)(q-1)^j / q^n.              (A-D3)

At the candidate parameters this is negligible. Therefore a successful verified decoder would break the source marginal, and also the paired source. No such polynomial algorithm is supplied by the norm uniqueness proof.

## A-D02-3: correlations cannot be read as unwrapped public covariance

The matrix B_F corrects the whole conditional multiplication covariance. It generally changes off-diagonal noise correlations, not merely a scalar variance. A public norm/covariance test on centered representatives of A,C cannot directly inspect B_F: the independently uniform ideal parts U,V are added modulo q, and wrapping changes those moments. The source challenge provides one pair, not repeated H samples at a known fixed F. Revealing F and H in a diagnostic therefore over-observes the public source.

The most direct public ways to expose the perturbations remain:

* Recover the unique F/support decomposition of A and then decode C relative to that support.
* Find a short multiplier w annihilating the common ideal, yielding wA=wF and wC=wH.
* Find a short pair relation P U+Q V=0 and test P A+Q C=P F+Q H.
* Find an explicit pair character surviving the ideal averaging with nonnegligible completion-induced bias.

The first three are decoding or lattice tasks at the actual d and widths; neither existence of short annihilators nor a lower-dimensional field quotient is an algorithm by itself. The fourth needs the joint characteristic law. None of the simple source-free shears supplies a negative covariance complement, and no checked primary reduction supplies an F-conditioned complement kernel from a public challenge.

For example, conditional on T, F,H are independent of U,V in A1. For CRT-coordinate characters chi_a,chi_b, the exact pair average therefore has the factorization recorded in F03-attacks.md A6. The noise factor is E_F[chi_a(F) E(chi_b(H_impl)|F)]. It may not be replaced by E chi_a(F) times E chi_b(H): that would remove the dependence being investigated. Retaining this factor leaves a nontrivial analytic/algorithmic problem; no character with an established inverse-polynomial public bias was constructed in this bounded investigation.

## Source comparison and disposition

Existing independent-noise HLBDD motivates the hidden ideal but does not determine this H kernel. The exact public-shear reduction preserves source hardness for B1's kernel and actual U law, but (A-D1) prevents a negligible latent substitution of that tested family for A1. DSPR's source-inherited common-denominator tuples and the older continuous Gaussian decomposition lemmas likewise do not yield a public sampler for A1's conditional H from an external source challenge. Defining and efficiently sampling H using hidden F is not that source reduction.

**Recommendation:** defer A1's exact computational source-hardness claim, while keeping its separately proved completion statement and conditional bridge as mathematical results pending review. No polynomial source attack has been obtained for d~n/ell^3; no inference of hardness follows. The most material missing claim is either a public reduction producing this same F-dependent pair from an independently justified source, or a public test that exploits the correlation without first solving the hidden support/noise decomposition.
