# B-SUP-STD-P v1 — full block-fiber proof

Status: PROVISIONAL. The theorem specifies both actual joint endpoints and a standard-input direction.

## 1. Gaussian projection atom and simultaneous rank

For Z~D_(Z,sigma_R), its reduction modulo q has maximum atom at zero: Poisson summation gives nonnegative Fourier coefficients for the wrapped Gaussian, so the value at any residue is at most the zero value. Moreover

  max_r Pr[Z=r modq]
   <=rho_sigma_R(qZ)/rho_sigma_R(Z)
   <=(1+sigma_R/q)/sigma_R=1/sigma_R+1/q.

The numerator bound follows by comparing the decreasing positive half-line Gaussian sum with its integral; the denominator is at least sigma_R by Poisson summation.

A CRT evaluation of an R entry has this same maximum-atom bound: condition on all coefficients except the constant coefficient, whose multiplier is one. For a fixed root, rows of the evaluated h by ell g matrix are independent. If v is a fixed nonzero column vector in Fq^(ell g), condition in each row on all but one entry whose corresponding v coordinate is nonzero. The chance that the row annihilates v is at most mu. Thus

  Pr[R(root)v=0]<=mu^h.

Union over at most q^(ell g)-1 nonzero v and n roots gives the rank failure rho. This is an unconditional bound for the original iid R law. Conditioning R on full rank is not claimed to preserve its Gaussian product distribution.

## 2. Uniform affine fibers give the actual target law

Fix a full-rank R and let L_R(w)=wR. This is a surjective homomorphism of finite Rq-modules, with every fiber of size q^(n(h-ell g)). In the actual decomposed experiment Wi is uniform, so Yi=WiR is uniform in Rq^(ell g), and Wi conditioned on Yi=y is uniform in L_R^-1(y).

Conversely, first choose Yi uniform and then Wi uniformly from its fiber. Every w has probability

  q^(-n ell g) q^(-n(h-ell g))=q^(-nh),

so this gives precisely the same joint law (Wi,Yi). Adding the deterministic diagonal gadget offsets changes no probability. Repeat independently for i=1,...,ell. The supplied STD multiplier array has exactly the needed uniform law on these full rows, independent of R. This proves equality of (R,W,Adec) under the rank event, including every cross-block correlation.

The planted response is kept as S A+e. In STD, S,e are independent of A,R and of the fiber coins. Given the constructed W,R, A=Adec deterministically, and the preserved response therefore has precisely the target conditional law. We may retain S,e in this proof coupling; they are not revealed to the algorithm. In the uniform comparator, b is initially independent uniform conditional on A and remains so after the independent R/fiber channel. Thus both complete endpoint equalities hold.

The bad rank event depends only on R, whose law is identical in both worlds. The target experiment is the same good-event law mixed with its bad-event law. Replacing the bad branch by a failure symbol changes it by at most its probability rho. No hidden rare conditioning, unit-secret condition, or multiplier erasure occurs.

## 3. Implementation and loss

Coefficient expansion represents L_R as an Fq-linear map of dimensions n ell g by nh. Gaussian elimination tests full row rank, finds one solution for each supplied right-hand side and a kernel basis. Sampling a uniform kernel coefficient vector and adding the particular solution gives the exact uniform affine fiber. It works without explicitly finding CRT roots. The target R itself is retained as the sampled integer matrix; its reduction is used only in linear algebra.

Finite scalar Gaussian approximation and bounded exact-uniform rejection can be coupled to their ideal samplers uniformly over every supplied input. Set their combined error to delta_impl using the same fixed-cap method as gaussian-periodic-bounded-wrapper-v1.md. This adds delta_impl per endpoint. Triangle inequality for two acceptance probabilities gives advantage delta-2rho-2delta_impl. Runtime and space are polynomial in the dimensions and COMPLETE parameter/input encodings, including precision. One rank attempt suffices.

This proof establishes a standard-RLWE challenge simulation for the exact wide decomposed ring law. It does not establish that every narrower decomposed law is equivalent, and it does not transfer hardness between secret distributions.
