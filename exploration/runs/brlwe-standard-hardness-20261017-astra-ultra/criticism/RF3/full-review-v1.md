# RF3 nonauthor full-proof review v1

Verdict: **favorable on the complete exact frozen theorem and proof; no repair required**. I found no counterexample, missing hypothesis, incorrect finite factor, or invalid asymptotic substitution within the stated integral, same-field, same-class scope. This is a completed nonauthor recommendation. Separate blind, regression-reconciliation, and final artifact gates remain the coordinator's responsibility; this report does not by itself certify the project or solve the computational-hardness goal.

Theorem SHA256: f090c6c128eb2d0fd52a9cadb2a2b67b8bdd731d84ef932aabbbdc3c74eb180a.

Proof SHA256: 012d77de4765194b8b22943d81773c42c59739f00e91012df8afd676ef210bfc.

The exact assignment hash matches 183628aee11a85d9692de53914bb897b8c2db7379920ae50dce6177f25f9e4d1. All permitted local mathematical inputs and controls are hashed in reviewed-inputs-sha256-v1.json. I read the whole current theorem and proof, the whole cited class-number proof, its permitted prior reviews and source gate, and the same-class regression-gate entries. I am not a blind reviewer and do not characterize same-model agreement as statistical independence or formal verification.

## 1. Frozen meaning and initial falsification

For n>=2 a power of two, R=Z[zeta_(2n)] is the full ring of integers in the degree-n field K. The class group is the ordinary fractional-ideal class group. C_n consists of those classes admitting at least one nonzero integral representative J whose quotient identifies two distinct coefficient-binary vectors. The existential quantifier ranges over all such integral representatives without a preassigned norm cutoff. The later decoding conclusion quantifies over every integral representative of every excluded class.

My first checks were the exact ideal-divisor count and attempts to break it at the ramified prime, by increasing index, and by same-class fractional scaling. Their complete exact witnesses appear in counterexample-attempts-v1.md, before any repair. The fractional variant fails in every class: a^(-1)I contains R whenever 0!=a is in I. Its corresponding guessing conclusion can fail, with exact success (3/4)^n for independent uniform binary S and G. The frozen text explicitly excludes fractional representatives, so this is a scope regression and not a counterexample to the actual theorem.

The degree-2 witness z=1+i proves that the factor v_n+1 cannot simply be dropped from the ideal count. It is present. A degree-4 witness proves that an individual embedding can exceed sqrt(n); the proof uses the full canonical norm identity instead of that false shortcut. A degree-4 odd-prime witness attains N(P)=2n+1; the proof correctly uses a non-strict lower bound.

## 2. Collision equivalence and the complete embedding bound

The coefficient vectors are interpreted in the fixed basis 1,zeta,...,zeta^(n-1), with no basis change. Two binary vectors s and s' collide modulo J exactly when their difference z=s-s' belongs to J. Their difference is a nonzero ternary vector. Conversely, a ternary vector is the difference of binary vectors by placing its positive coefficients in one vector and negative coefficients in the other. Nonzero degree-less-than-n polynomials cannot vanish at zeta because its minimal polynomial is X^n+1. Hence there are exactly 3^n-1 nonzero eligible elements z, before harmless identification of opposite signs or equal principal ideals.

Index the n complex embeddings by zeta -> exp((2j+1)pi i/n), j=0,...,n-1, including both members of each conjugate pair. For coefficient indices k,l between 0 and n-1,

    (E*E)_(k,l)
      = sum_j exp((2j+1)(l-k)pi i/n)
      = n if k=l, and 0 otherwise.

The last equality is the full finite geometric sum, so E*E=nI without an omitted factor of 2. Therefore sum_sigma |sigma(z)|^2=n sum_k |z_k|^2. AM-GM gives

    |N_K/Q(z)|^2
      = product_sigma |sigma(z)|^2
      <= ((sum_sigma |sigma(z)|^2)/n)^n,

and consequently

    1<=|N_K/Q(z)|<=||z||_2^n<=n^(n/2)=B_n.

The lower inequality uses a nonzero algebraic integer norm. This is an absolute field norm; the norm of the principal integral ideal (z) is its absolute value. No individual-embedding upper bound is assumed.

## 3. Every prime-ideal norm, including ramification

Let P lie above an odd rational prime p, with residue degree f. The image of zeta in R/P is a unit satisfying zeta^n=-1!=1. Its order divides 2n but does not divide n. As 2n is a power of two, this order must be exactly 2n. The finite multiplicative group of R/P has size p^f-1, so

    2n divides p^f-1,
    N(P)=p^f>=2n+1.

This argument covers every odd prime ideal and does not require that the underlying rational prime be at least 2n+1. Small odd p can have larger residue degree. It also does not silently count rational primes in place of prime ideals.

At 2 one has

    R/(2) = F_2[X]/((X+1)^n).

This quotient has a unique prime ideal and its residue field is F_2. Hence precisely one prime P_2 lies above 2, with N(P_2)=2. The degree formula then gives total ramification, (2)=P_2^n, but the divisor formula has one exponent for P_2. It does not acquire n independent ramified factors. This is the crucial ramification check.

## 4. Exact finite divisor count and passage to classes

Unique factorization of nonzero integral ideals in the Dedekind domain R gives

    (z)=P_2^a product_(P!=P_2) P^e_P.

There are exactly

    (a+1) product_(P!=P_2)(e_P+1)

integral ideal divisors: each prime-ideal exponent may be chosen independently from 0 through its displayed exponent. The product ranges only over primes with positive exponent; absent primes contribute one. It includes R and (z).

Since N((z))<=B_n,

    a<=log_2 B_n=v_n.

For Omega=sum_(P!=P_2)e_P the odd-prime norm bound gives

    (2n+1)^Omega <= product_(P!=P_2)N(P)^e_P
                    <= N((z)) <= B_n,

so Omega<=u_n. Using e+1<=2^e for every positive integer e yields the exact claimed upper bound

    (a+1) product(e_P+1)
       <=(v_n+1)2^Omega
       <=(v_n+1)2^u_n=M_n.

The separate worst cases for a and Omega need not be simultaneously attainable; using them simultaneously only enlarges the upper bound. No factor counting rational primes, conjugate primes, or residue degrees is missing.

If z is in the integral ideal J, then (z) is contained in J, which is contained in R. This containment direction means that J divides (z) as an integral ideal. In valuation terms, every exponent of J lies between 0 and the corresponding exponent of (z). Equivalently, (z)J^(-1) is integral. Thus each relevant J lies in the union of the finite divisor sets of the 3^n-1 eligible principal ideals. Counting this union by the sum of its sizes and then forgetting the representative gives

    |C_n| <= number of colliding integral ideals
          <= (3^n-1)M_n.

Both operations can overcount and therefore have the right upper-bound direction. There is no injectivity assumption on the map from ideals to classes and no probability distribution on generators or divisors.

A collision itself forces N(J)<=N((z))<=B_n. Thus arbitrary initial index is covered rather than silently omitted. Nevertheless, this observation alone would not reduce the new theorem to the earlier bounded-index theorem: B_n=exp((n/2)log n) corresponds to c=(1/2)log n, whereas the earlier theorem fixes c independently of n. The new divisor argument is load-bearing and has been checked on its own.

## 5. Analytic dependency and exponent

The separate source-parameter-v1.md records direct primary-source access, independently reconstructs every analytic hypothesis and the regulator comparison, and verifies the same-class dependency's exact hash. In particular, both the full and real cyclotomic families are normal, their degree/log-discriminant ratios tend to zero, and the difference of their Brauer–Siegel formulas loses only O(n) through the regulator ratio. This gives log h_n>=(1/4+o(1))n log n without GRH or a real-class-number-one assumption.

For the numerator, u_n<=n/2 and log(v_n+1)=O(log n). Therefore

    log((3^n-1)M_n)
      <=n log 3+(n/2)log 2+O(log n)=O(n).

Subtracting the class-number lower bound gives the claimed logarithmic upper bound -n log n/4+o(n log n). This is an upper estimate for the uniformly counted fraction of ordinary classes, with no matching lower estimate, effective starting dimension, or efficient uniform sampler. The source access limitations are recorded accurately: screenshots failed to retrieve, while the arXiv text needed for the import was readable.

## 6. Exact posterior law and conditional scope

Fix an integral J with injective binary quotient map and any probability mass function mu supported on J. For independent uniform S on the coefficient cube and G with law mu, let Y=G+S. Then

    Pr[S=s,Y=y]=2^(-n) mu(y-s),

with mu interpreted as zero off J. If the right side is positive for two secrets s,s', then y-s and y-s' belong to J, so s-s' belongs to J; injectivity forces s=s'. Thus for every positive-mass y there is exactly one possible secret. In particular,

    P_guess(S|Y)
      = sum_y max_s Pr[S=s,Y=y]
      = sum_y Pr[Y=y]
      = 1.

The countable support allows these nonnegative sums, and the finite set of secrets gives a measurable decoder. Zero-mass observations may be assigned arbitrarily. The decoder is a mathematical function with fixed J as a parameter; efficiency is not asserted. The support argument is actually stronger than the independence/uniformity assumptions used in the frozen statement, but no stronger theorem is needed or substituted.

For public information U, apply the same support partition on each conditional branch where J is fixed as specified and the conditional law has the stated support. Changing mask probabilities, allowing zero masses, or using a non-Gaussian shape does not change which coset contains y. There is no multiplication of per-stage success estimates, restoration of independence after selection, posterior resampling, or hidden normalizer estimate. Hence CP-1's sequential-product failure does not enter this reasoning. Exact finite rational controls and the excluded fractional posterior countercontrol are recorded in counterexample-attempts-v1.md.

The observed Y here is the proof's exact G+S. Nothing in this argument establishes that a public binary-RLWE adversary sees Y or can compute it. It must not be recast as a public attack, or as a computational hardness theorem. A mixture over unknown representatives without the stated fixed-support interpretation is not an extra conclusion of this theorem.

## 7. Independent audit of the existing finite control

I read control-v1.py, input-v1.json, command-v1.txt, the original stdout, and the empty stderr. I did not rerun the code or start a new experiment. Their hashes are preserved. The code's 60-second alarm and 256 MiB address-space limit are inside the assignment bounds; the documented command also has a 60-second foreground timeout.

The multiplication routine computes negacyclic products exactly with Python integers. Writing z=a(X^2)+Xb(X^2), its norm recursion uses the relative norm a(Y)^2-Yb(Y)^2 in Z[Y]/(Y^(n/2)+1). This is the correct quadratic tower norm down to degree one. The determinant routine builds the multiplication matrix and uses exact Bareiss elimination with row pivoting and divisibility assertions. It supplies a different norm calculation, but shares the multiplication routine; the two arithmetic implementations are not fully independent.

For odd p the code uses f=ord_(2n)(p). This equals the residue degree in this cyclotomic ring: Frobenius sends a primitive 2n-th root to its p-th power, so its orbit length is exactly that order. All prime ideals over p have this f. Therefore v_p(N(z))/f equals the sum of the ideal exponents above p, and the code's omega is the appropriate total odd multiplicity. At 2, the rational norm valuation is the single P_2 exponent. This validates the translation from integer norms to the divisor upper bound used by the control.

The exhaustive nonzero ternary state counts are 8, 80, and 6560 at n=2,4,8, totaling 6648. The reported per-polynomial bounds are respectively 2, 10, and 52. Determinants are checked on all 88 states of degrees 2 and 4 and on every 31st degree-8 nonzero state, giving 211 further checks and 299 total. These counts agree with the loops and input record.

The output reports PASS for the norm bounds, exact divisibility by residue degrees, odd multiplicity bounds, and norm-derived divisor upper bounds. It does not factor each principal ideal, enumerate its exact divisor set, compute ideal classes, or test the analytic asymptotic. Its reported maxima are maxima of norm-based upper estimates, not exact maximum ideal-divisor counts. I rely on the mathematical proof for the universal divisor formula and asymptotic conclusion; the existing finite record is corroborative falsification evidence only.

## 8. Regression disposition, exclusions, and completion record

I reviewed all 66 entries in the allowed same-class regression gate. Their prior dispositions are historical input, not automatic acceptance for this new theorem. The underlying reports outside the assignment's read scope were not opened. The current proof uses none of the catalogued simulator, tower-transfer, Gaussian normalizer, lattice-search runtime, oracle cache, or sequential-product arguments. Its posterior assertion was separately checked above rather than inheriting the earlier theorem's blanket observation that no posterior assertion was present. Root must perform its own final regression reconciliation against the complete project registry.

The additional targeted regressions are: ramification at 2; full versus half canonical embedding normalization; equality at the odd-prime norm bound; unrestricted integral index; every-class fractional scaling; a finite fractional posterior counterexample; small-n asymptotic non-effectiveness; and nonuniform-mask disjoint-coset decoding. All classify as required by the frozen theorem. No repair or version change was necessary.

Multiplication by a nonzero field element preserves ordinary ideal class. It therefore cannot normalize an excluded class to an integral representative with a coefficient-binary collision. A Gaussian shape change with the same ideal support cannot change this conclusion. Fractional representatives can escape, as proved explicitly; class changes, field or dimension changes, altered coefficient encodings, computational-only simulation, different exposures, and different source mechanisms remain outside the claim. The arbitrary-ideal to eligible source-family hardness bridge remains unresolved.

All review writes are inside criticism/RF3. No subagent, goal, external model session, service, installation, detached process, new mathematical experiment, external message, or Git operation was used. This review stops after delivering the scoped recommendation and its exact evidence; project acceptance remains with the coordinator.
