# B-SUP-STD-T v1 — ordinary RLWE to wide decomposed ring law

Status: PROVISIONAL new public simulation. This is a concrete standard-input edge, with NO source renaming. Its source has the same secret/noise law as its target; it supplies no binary-secret conversion. Proof: standard-rlwe-decomposed-proof-v1.md.

Let Rq=Fq[X]/(X^n+1), n>=2 a power of two, q>=5 an odd split prime. Fix integers ell,g,h>=1 and a deterministic public ring gadget row G in Rq^g. The gadget may be padded, and no entropy property of G is needed. Let sigma_R>=2, and put

  mu=min(1,1/sigma_R+1/q),
  rho=min(1,n(q^(ell g)-1)mu^h).

The useful regime requires rho<1. Ordinary input consists of m=ell²g standard ring samples with one common secret S from a fixed law Secret, independent coefficient error law E, and either

  STD planted: A uniform in Rq^m, b=S A+e, e~E;
  STD comparator: same A, b uniform in Rq^m independent of A.

All the A multipliers are supplied. For ordinary uniform-secret coefficient-discrete-Gaussian RLWE take Secret uniform in Rq and E with iid coefficient D_chi entries. Any imported standard hardness theorem must still match that exact source error/embedding/modulus regime; this theorem does not assert hardness for arbitrary chi.

The target decomposed law is

  R=[R1|...|Rell] in R^(h by ell g),
      every coefficient independently D_sigma_R;
  Wi uniform independent in Rq^(1 by h), i=1,...,ell;
  Aij=Wi Rj+delta_ij G, an ell by ell array of g-ring-element blocks;
  publish (W,R,b), with R retained as its integer coefficient matrix.

Its planted response is b=S Adec+e with the SAME Secret/E, independent of W,R. Its comparator is an independent uniform b in Rq^m. The optional explicit Adec is a deterministic public function of W,R and may be retained in both worlds.

## Simulator

1. Sample the complete concatenated R with the stated iid coefficient Gaussian law.
2. Test whether the Rq-linear map w -> wR from Rq^h onto Rq^(ell g) is surjective. Equivalently its coefficient expansion has full Fq row rank, or R has full column rank at EVERY CRT root. If it fails, output a declared failure symbol.
3. Arrange the supplied independent multipliers A as ell rows of ell g ring elements. For each i solve the FULL row equation

     Wi R = A_i - [delta_i1 G | ... | delta_iell G].

   Sample Wi uniformly from this affine fiber, independently across i conditional on R,A.
4. Output (W,R,b), preserving b verbatim. Do not publish the independent fiber coins.

Conditional on the rank event, the ENTIRE joint law (R,W,Adec,b,S,e) in the planted world equals the actual decomposed law conditioned on that event. In the comparator world, the ENTIRE public joint law equals its conditioned decomposed comparator. In particular, all shared-R and shared-W block correlations are retained; sampling separate blockwise fibers would not establish this theorem.

With one attempt and the failure symbol, each endpoint is within rho of the corresponding unconditioned decomposed endpoint. If the finite Gaussian/fiber implementation has total input-uniform error delta_impl, the endpoint bound is rho+delta_impl in EACH world. Consequently a decomposed distinguisher with advantage delta gives an ordinary RLWE distinguisher with advantage at least

  delta-2rho-2delta_impl.

The simulator uses exactly ell²g ordinary input samples, adds no response noise, preserves the full secret law, and uses no additional challenge samples or secret-dependent hints. Exact Gaussian draws and exact finite-field uniform sampling may be implemented in expected polynomial time; capping their elementary rejection loops gives a strict polynomial implementation with the explicit delta_impl charge. All rational input encoding lengths are counted. No rank rejection loop is required; alternatively independent rejection of R until success produces the conditioned law in expected1/(1-rho) attempts.

## Explicit polynomial window

For sigma_R=2, q>=5 gives mu<=7/10<2^-1/2. Therefore

  h >= 2[ell g ceil(log2 q)+lambda+ceil(log2 n)]

makes rho<=2^-lambda. For g=ceil(log2 q), polynomial ell and polynomial-bit q, h is polynomial in n,ell,log q,lambda. The value of q need NOT be polynomial for this simulator, since finite-field linear algebra is polynomial in log q. Source noise chi is unchanged, so every independently verified standard RLWE source regime survives this edge without an additional noise restriction. Composing a separate triangular rerandomization incurs that theorem's own noise and hint-width losses.

The target is wider than a minimal quotient gadget. Padding a quotient construction to this width changes its public hint law and sampling/norm bounds; it is not free notation. This standard edge alone does not turn a binary recovery oracle into a uniform-secret oracle and does not establish the required low-index fractional source hardness.
