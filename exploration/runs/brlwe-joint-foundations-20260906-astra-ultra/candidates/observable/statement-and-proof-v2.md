# W3-v2: an independent-noise observable bridge and its public rank obstruction

Status: **REPAIRED-PENDING-RECHECK** for W3-OBS v2; W3-RANK v1 remains PROVISIONAL. This is one alternative source/hybrid to A2, with two explicit first-ideal-point conventions. It is not a proof of P0-A2 or an unconditional binary-secret RLWE hardness theorem.

The correlated completion kernel can be removed from the computational source. A complete public hybrid instead uses `(U+F,V+E_sigma)` and the public map `(a,c) -> (a,aS0+c)`. Its statistical cost is `2 eta_N+eta_X` for active U, where the completion kernel exists only inside the proof. For uniform-in-I U, the same hybrid pays the averaged image defect `eta_iso`. In the subregime `c>1/2`, that last cost is essentially sharp for these actual public pair laws: an explicit unbounded public test gives distance at least `eta_iso-negl`. Thus this route removes the correlated-source obligation but does not complete a negligible-error reduction from ordinary uniform-point HLBDD at c=1.

Canonical agent ID: `/root/w3_observable`. A final administrative environment check exposed `CODEX_THREAD_ID=01a0784e-b2cb-7612-b5cf-d2da1b99b6ea` and `CODEX_SESSION_ID=01a07849-2b26-7ac1-96c2-c15903ac2341`; these are reported exactly as environment metadata, without asserting that they identify distinct worker infrastructure. Assignment W3-v1 fixes deadline 2026-09-06T21:19:15Z and the unchanged run deadline. All output is confined to this directory. No CPU experiment, worker, package installation, or source-sampler implementation was run. This is an author derivation with exact hand controls, not statistical independence from the other same-model agents. No new content-policy interruption occurred; two primary-PDF screenshot attempts returned ordinary cache-miss errors, recorded in source notes.

## W3-OBS v2 — full finite public comparison

**Explicit joint law added in v2.** The general theorem is defined on the product-kernel space

    mu(dJ,dU,dF) K(dHhat | J,U,F) Unif_I(dV)
      * P_S(dS) * P_G(dG) * P_E(dE) * P_S(dS0) * P_E(dE0).

All factors after the conditional source kernels are independent draws. In particular the FULL joint law of (J,U,F,S,E) is mu x P_S x P_E, so E is independent of S jointly with the latent source tuple, not merely marginally independent of each coordinate. The computational source uses (J,U,F,V,E0); Hhat remains proof-only. On the extracted comparison side Z is appended by the uniform Q_J kernel independently of every other variable conditional on J. The target uses a fresh uniform a independently of the product-law pair (S,E). The source and public tests retain these exact independence conventions.

The original coordinator blind packet B01-M1 omitted the S/E joint condition. Its literal A1/A2 statement is refuted by the exact F3 control with E=-S and zero stated errors. This v2 premise excludes that control. The original packet, counterexample and author v1 note remain preserved. The entire edited proof below requires a fresh nonauthor recheck; no earlier disposition is inherited. This is a clarification/strengthening of the general probability model, not a change to the intended independent-error binary-RLWE target or W3-RANK's already independent-error ring model.

**Frozen general law.** Let R be a finite effectively represented commutative ring. Draw `(J,U,F)` from a specified law `mu`, with `I=Ann(J)`, `Q_J=R/J`, and `U in I`. Conditional on J, V is uniform in I and independent of `(U,F)`. Draw `E0` independently from a fixed public target-noise law `P_E`. The computational source worlds are exactly

```
Src_ind(mu): (A,C)=(U+F,V+E0),
Unif_2:     (a,c) with a,c independent uniform in R.
```

Neither source world takes a binary-secret input. Its hidden variables are `J,U,F,V,E0`; only the pair and public ring/parameter description are released. In particular its actual second noise is E0, independent of F. No completion kernel occurs in the source experiment.

Independently of the source variables, let S have the fixed public secret law `P_S`, let G have a fixed public law `P_G`, and let `Y=S+G`. Let `Hhat` be a **proof-only** random variable sampled from a fixed kernel given `(J,U,F)`, independently of `(S,G)` conditional on that tuple. Require the two precise mathematical comparisons

```
TV((J,U,F,F G+Hhat), (J,U,F,E)) <= eta_N,                 (Nhat)
TV((J,U,F,Hhat,Y,pi_J(S)),
   (J,U,F,Hhat,Y,Z)) <= eta_X,                           (Xhat)
```

where E is independent target noise and Z is uniform in Q_J conditionally independent of `(U,F,Hhat,Y)` given J. Hhat is integrated out in Nhat and retained in Xhat. This statement does not require the **actual source noise E0** to satisfy `F G+E0 ~= E`. That latter premise can fail while the theorem below succeeds.

For a randomized bit test D, all algorithmic coins are independent of its challenge. Define the two complete public source tests

```
B1(a,c): sample independent s~P_S, e~P_E;
         return D(a,a*s+e).       // c is unused

B2(a,c): sample s0~P_S independently of the challenge;
         return D(a,a*s0+c).
```

Neither algorithm samples Hhat or G, computes a quotient, uses hidden J/U/F, or invokes a source sampler. Each calls D once. With `T_mult,T_add` the public ring-operation costs, their runtimes are at most

```
T_B1 <= T_D+T_S+T_E+T_mult+T_add,
T_B2 <= T_D+T_S+T_mult+T_add.
```

An exact transcendental Gaussian law here is a mathematical distribution; executable approximate sampling is accounted below.

**Claim.** Put `eta_iso=E_mu[1-|UR|/|I|]`. Then

```
TV((U+F,(U+F)S+E), (U+F,V+F S0+E0))
  <= 2 eta_N+eta_X+eta_iso,                              (OBS.1)

Adv_target(D)
  <= Adv_ind(B1)+Adv_ind(B2)+2 eta_N+eta_X+eta_iso.        (OBS.2)
```

The target is `(a,aS+E)` with uniform a independent of S,E; advantages are absolute acceptance-probability differences against Unif_2. The two source advantages refer to different tests. If multiplication by U maps Q_J bijectively onto I, then `eta_iso=0`. No efficient sampler for the proof-only Hhat is necessary for this abstract implication; its exact law and comparisons must exist and be proved.

**Complete joint hybrid proof.** Every displayed output is only a public pair. At each statistical step the retained variables used to justify the map are separately named.

| World | Public pair | Edge from the preceding world |
|---|---|---|
| H0 | `(a,aS+E)` | Target; a uniform, S,E independent |
| H1 | `(U+F,US+FS+E)` | Source advantage of B1 |
| H2 | `(U+F,US+F(S+G)+Hhat)` | At most eta_N |
| H3 | `(U+F,UZ+FY+Hhat)` | At most eta_X |
| H3r | `(U+F,UZ+F(S0+G0)+Hhat)` | Exact equality of full retained law |
| H4 | `(U+F,UZ+F S0+E0)` | At most eta_N |
| H5 | `(U+F,V+F S0+E0)` | At most eta_iso |
| H6 | `(A,A S0+C)` for independent source challenge | Exact equality of full joint law |
| H7 | Unif_2 | Source advantage of B2 |

For H1 to H2 append independent S to the two retained tuples in Nhat and map `(J,U,F,S,N)` to `(U+F,US+FS+N)`. The algebraic identity `FS+FG=FY` is exact modulo q. No target noise is inferred from Gaussian marginals or covariance.

For H2 to H3 use Xhat and the map `(J,U,F,h,y,z) -> (U+F,Uz+Fy+h)`. Here `U pi_J(S)=US` is well defined because U annihilates J. The old S and G are **not retained** after this map.

For H3r, sample entirely fresh independent `(S0,G0)` with laws `P_S,P_G` and put `Y0=S0+G0`. The joint law `(J,U,F,Hhat,Y,Z)` on the extracted side of Xhat is `mu(dJ,dU,dF) K(dh|J,U,F) P_Y(dy) Unif_QJ(dz)`. It therefore equals the law with Y replaced by S0+G0, with Z drawn independently of S0,G0,Hhat conditional on J. This is equality of the full factorized law. It is not permission to retain the original S or G while resampling them given Y.

For H3r to H4 append S0 independently to Nhat and append Z by the same kernel `Unif_QJ` depending only on retained J. Apply `(J,U,F,S0,Z,N) -> (U+F,UZ+FS0+N)`. Hhat and G0 are integrated out. This second use of Nhat is why the cost is **two** eta_N terms.

Given J,U, the variable UZ is uniform on UR. Its distance from uniform I is exactly `1-|UR|/|I|`. Append the independently sampled `(F,S0,E0)` with their actual conditional laws and average over `(J,U,F)` to get H4 to H5. Under bijective U this edge is equality. This is an upper bound after projection, not a public lower-bound argument.

Finally, given `(J,U,F,S0,E0)`, translation of V by `-US0` leaves a uniform ideal point `V'=V-US0`. Its conditional law is constant even when S0 is fixed. Therefore V' is independent of `(U,F,S0,E0)` conditional on J and

```
V+FS0+E0 = (U+F)S0+(V'+E0).
```

This proves H5=H6 as a full source/S0 joint law. For every fixed s0, `(a,c)->(a,a*s0+c)` is a permutation of R squared; it preserves Unif_2 regardless of zero divisors. Thus B2's uniform endpoint is exactly H7. Triangle inequality proves OBS.1 and OBS.2.

**Implementation terms.** If the actual source pair has TV at most xi_src from Src_ind, B1's actual independent `(s,e)` sampler has error xi_1, B2's independent s0 sampler has error xi_2, and the actual public target has error xi_tgt, a safe executable bound adds

```
2 xi_src+2 xi_1+xi_2+xi_tgt.                            (OBS.3)
```

B2's approximate s0 costs nothing at its uniform endpoint, since the permutation property holds for every s0. For coefficientwise fair binary S, both binary samplers use n exact fair bits; then xi_2=0 and xi_1 only contains target-Gaussian sampling error. No Hhat implementation term is required because no executable test samples it. If one uses an implemented Hhat as the mathematical proof kernel instead, its error must be included in eta_N twice.

## One fixed baseline instantiation and independent source support

Keep the assignment's exact parameters

```
ell=ceil(log2 n), d=floor(sqrt(n)/ell^4), b=ell^2,
tau=ell, sigma=2n ell^3, q=1 mod 2n prime,
sigma*n^c <= q <= n^K, m=1.
```

Fixed c>0 and K precede the choice of uniform randomized polynomial-time test. All eventual claims are along qualifying split-prime sequences with d>=1. No exponent is chosen after seeing the adversary's advantage. For a concrete nonempty asymptotic intersection, the previously checked c=1,K=16 sequence remains available; this note does not reprove its prime-existence import or claim practical thresholds.

Sample T uniformly among all d-subsets of CRT roots, put I=I_T and J=ker pi_T, and sample F with iid D_ell coefficients conditioned on `[-b,b]`. The sole source candidate is the independent-noise pair

```
IHS(u):  (U+F,V+E0), E0 iid wrapped D_sigma, V uniform I_T.
```

The explicit version flag `u=act` chooses U uniformly nonzero on every coordinate of T; `u=unif` chooses U uniformly in I_T. All U,V,F,E0 draws are independent given T except for their deterministic support constraints. These are different exact laws. In the active version eta_iso=0. In the uniform version

```
eta_iso=1-(1-1/q+1/q^2)^d,
delta_act=1-(1-1/q)^d.                                  (OBS.4)
```

The second quantity is the full latent conditioning distance for replacing U by active U; it is not eta_iso and no equality for public-source TV is assumed.

Use the existing canonical coefficient-order H_seq(F) as **Hhat only**. Its matrix is `B_F=sigma^2 Id-tau^2 M_F M_F^t`, with `||M_F||<=nb`, so `B_F >=3sigma^2 Id/4`. The frozen guarded NC1 v2 and X1 v1 are inherited mathematical inputs, whose statuses remain those of the consolidated ledger. They prove Nhat and Xhat for either U law because U and the entire Hhat kernel are sampled independently of S,G conditional on T.

For clarity the guarded finite completion upper bounds are

```
kappa(t)=2 sum_{j>=1} exp(-pi*t*j^2),
delta_N=(1+kappa(3ell^2/4))^n-1,
e_conv=min(1,delta_N/(1-delta_N)) if delta_N<1; else 1,
kappa_H=kappa(3sigma^2/4),
e_seq=min(1,(((1+kappa_H)/(1-kappa_H))^n-1)/2)
       if kappa_H<1; else 1,
eta_N=min(1,e_conv+e_seq).
```

For extraction, let `L=ln n`, `Lambda=d ln q`, `kappa_X=L^-3`. The inherited finite gates are

```
ell>=3, kappa_X<min(1/100,ln 2,2/(ln(3n))^3),
3Lambda<n, Lambda>=max(kappa_X^-1,4),
n-1>=4 C_BV*kappa_X^-1*d*Lambda*(ln Lambda)^3.
```

With the primary constants imported in X1, put

```
E_X=c_BV*kappa_X*(n-1)/(4Lambda*(ln Lambda)^2),
eta_X=min(1, (1/2)exp((d ln q-E_X)/2)).
```

These gates hold eventually in the frozen A2 dimension range and both errors are negligible, using the existing X1/NC1 proofs with their exact qualifications. No new extraction theorem is claimed here. In particular the same-Y posterior replica law, rather than independent unconditional secret replicas, remains required. No larger quotient dimension or multiple-sample inference is imported.

**Independent computational support that is actually available.** Define the base challenge family precisely, with the same uniform T:

```
Base_unif: (a,c0)=(U+F_inf,V+H0),
U,V independent uniform I_T;
F_inf,H0 independent iid coefficient D_ell;
reference: independent uniform R_q pair.
```

This is the same-ideal reading of the pre-existing HLBDD source in Order-LWE, Section 7. Definitions 7.3–7.4 are terse about repeated lattice sampling and print an ambiguous comparator; Lemma 7.7 explicitly uses one common ideal and uniform ideal points. The present base experiment states that reading rather than silently treating the ambiguity as a theorem. Canonical spherical width is `sqrt(n)*ell`, since canonical norm is sqrt(n) times coefficient norm. The paper does not prove this computational assumption from worst-case Order-LWE at these parameters. Its own entropic bridge uses swallowing and a super-polynomial-q unit step, neither imported here. See [primary full version, Section 7](https://eprint.iacr.org/2018/494.pdf#page=38).

There is an explicit public broadening map from this independently specified base source to IHS(unif). Let `rho^2=sigma^2-ell^2`, sample W with iid coefficient D_rho independently of the challenge, and map

```
M(a,c0)=(a,c0+W).
```

For each W it preserves the uniform comparator. Let

```
delta_F=Pr[F_inf not in [-b,b]^n]
       <= n exp(-pi ell^2)/(pi ell),
theta_br=ell^2(1-ell^2/sigma^2),
delta_br=(1+kappa(theta_br))^n-1,
eta_br=min(1,delta_br/(1-delta_br)) if delta_br<1; else 1.
```

The diagonal specialization of the guarded discrete convolution proof gives `TV(H0+W,E0)<=eta_br`; there is no sequential-normalizer error for the diagonal complement. Conditioning F_inf on the full box gives exactly the product truncated F law and costs delta_F. Thus the complete source-pair distance is at most delta_F+eta_br. The map uses no hidden ideal or F. This overlaps W1's independently assigned broadening check; no unreviewed W1 formula is assumed in the derivation above.

The source tests composed directly with Base_unif are

```
T1(a,c0): sample independent binary s and e~D_sigma^n;
           return D(a,a*s+e).
T2(a,c0): sample independent binary s0 and W~D_rho^n;
           return D(a,a*s0+c0+W).
```

Since T1 ignores c0, its source-law comparison costs delta_F alone. T2 costs delta_F+eta_br. Hence the sharper finite base-source consequence is

```
Adv_target(D) <= Adv_Base_unif(T1)+Adv_Base_unif(T2)
              +2 eta_N+eta_X+eta_iso+2 delta_F+eta_br.   (OBS.5)
```

T2's runtime is `T_D+T_S+T_W+T_mult+2T_add`; T1 has B1's runtime. Approximate public Gaussian samplers add `2 xi_E+xi_W`, in addition to any actual target error, because the uniform endpoint of T2 is exact for every W. If Base_unif itself is implemented within xi_base of its mathematical law, add `2 xi_base`. All these samplers admit polynomial-time negligible-error approximations at the polynomial widths; no executed implementation is claimed.

OBS.5 is a supported **conditional finite reduction to a pre-existing independently specified source assumption**. Its eta_iso is not negligible at fixed polynomial q. Defining Base_act by active U would remove this term and give the active analogue of OBS.5, but **Base_act hardness remains unsupported** by this note. It is not justified by absence of a syntactically binary input, by the public broadening map, or by target-tailored nomenclature. P0-A2 also remains open; the argument does not prove a public map producing its H_seq source law.

## W3-RANK v1 — the remaining rank loss is publicly observable in a strict subregime

This claim is about the **two actual public laws** in OBS.1 for IHS(unif), not a retained-variable lower bound. Set

```
P=(U+F,US+FS+E),
Q=(U+F,V+FS0+E0),
R0=ceil(sigma*ell), B0=nb+R0,
delta_E=Pr[an iid integer D_sigma vector leaves [-R0,R0]^n]
       <=2n exp(-pi ell^2).
```

F has the fixed bounded law, S and S0 are independent fair binary vectors, and all errors have their independent target laws. Assume the finite strict gates

```
2b<q,
q^(1-2d/n)>2b sqrt(n),
q^(1-d/n)>2B0 sqrt(n).                                 (RANK.1)
```

**Claim.** Under these gates,

```
max(0,eta_iso-2delta_E) <= TV(P,Q)
                       <= min(1,eta_iso+2eta_N+eta_X).  (RANK.2)
```

The lower bound does not use extraction, Hhat, or any computational assumption. For any fixed `c>1/2`, all gates hold eventually at the frozen baseline; the lower bound is inverse polynomial. For `0<c<=1/2`, this sufficient lower-bound gate is not established from the frozen lower bound on q, and no conclusion is asserted for that subregime. The finite gate can of course hold for a particular qualifying q even if its stated lower exponent c is smaller.

**Norm fact used twice.** If a nonzero integer polynomial w of degree below n is supported modulo q on at most k CRT roots, it vanishes modulo at least n-k distinct prime ideals above q. Since q splits and X^n+1 is irreducible over Q, its nonzero integer cyclotomic norm is divisible by `q^(n-k)`. Parseval in the 2n-th cyclotomic embedding and AM-GM give

```
q^(n-k) <= |Norm(w)| <= ||coeff(w)||_2^n.
```

Consequently no such nonzero w can have coefficient norm below `q^(1-k/n)`. This is a strict statement, with no rounding equality included.

**A genuinely public test.** On input `(a,beta)` perform the following finite, potentially exponential computation:

1. Enumerate F* in `[-b,b]^n` and keep those for which `U*=a-F*` has CRT support of size at most d. If none exist, reject. The middle gate in RANK.1 implies that there is at most one F*: the difference of two would have coefficient norm at most `2b sqrt(n)` and CRT support at most 2d, contradicting the norm fact. Thus this step finds the actual F and U on both P and Q.
2. Put `W=supp_CRT(U*)` and `k=|W|`. Reject unless k<d.
3. Accept exactly when `beta belongs to I_W+Box(B0)`, where Box(B0) is the set of coefficient residues with representatives in `[-B0,B0]^n`. This can be tested by enumerating those representatives h and checking whether `beta-h` is supported on W.

Every quantity used is a deterministic function of the **public pair**. Hidden T, V and S are never provided to the test. This explicitly establishes measurability instead of promoting a latent test to a public one. A simple runtime upper bound is

```
((2b+1)^n+(2B0+1)^n)*poly(n,log q,log B0),
```

plus public-root preprocessing. Enumerating the polynomially bounded field to obtain CRT roots has polynomial-in-n cost. This is an unbounded-TV witness, **not a polynomial-time attack**.

Let `M=d-k` be the number of zero active coordinates of U. It has the exact binomial law `Binomial(d,1/q)` even though the test need not know the original T. Define `p_bad=Pr[M>0]` and `r_bad=E[1_(M>0) q^-M]`.

Under P, on `M>0` and the bounded-error event, the test accepts: US belongs to I_W and `FS+E` has coefficient norm infinity at most `nb+R0=B0`. Therefore `Pr_P[accept]>=p_bad-delta_E`.

Under Q, consider the bounded-error event and an accepting h in Box(B0). The integer difference `w=h-(FS0+E0)` has every coefficient bounded by 2B0. Modulo q it equals `V-v_W` for some `v_W in I_W`, hence it is supported on T, of size d. The last strict gate in RANK.1 and the norm fact force w=0. In particular `V=v_W in I_W`. Conditional on the full original `(T,U,F)`, V is uniform in I_T and independent of S0,E0, so this happens with probability exactly `q^(k-d)=q^-M`. Thus `Pr_Q[accept]<=r_bad+delta_E`.

Their acceptance gap is at least `p_bad-r_bad-2delta_E`. Direct binomial averaging gives

```
p_bad-r_bad=E[1-q^-M]
           =1-(1-1/q+1/q^2)^d=eta_iso.
```

This proves the lower bound. OBS.1 gives the upper bound. Neither calculation multiplies probabilities after a selected history; the only factor is the pointwise conditional uniform law of fresh V given the **full** tuple T,U,F.

For the asymptotics, `q^(d/n)=exp(O(d ln(n)/n))=1+o(1)`, since q<=n^K. Also `B0=O(sigma ell)`. Therefore the last gate follows from `n^(c-1/2)/ell -> infinity` when c>1/2; the first two gates already hold eventually. For d>=1 and q>=2,

```
eta_iso >= 1/q-1/q^2 >= 1/(2n^K).
```

Subtracting the negligible tail preserves an inverse-polynomial lower bound. In particular the concrete previous c=1,K=16 regime cannot close OBS.5 by asserting negligible TV between P and Q.

## Mandatory historical controls and new exact hand checks

The full imported registry remains authoritative. The following scopes identify the load-bearing controls for this candidate; others are explicitly not imported as positive claims.

| Control | What the present proof does |
|---|---|
| R02, vacuous source coins C=G | Hhat is drawn before and independently of G conditional J,U,F. The computational source contains independent E0. No public test accesses G hidden in a challenge. |
| R03, uniform marginals/correlated pair | Both computational assumptions and every hybrid compare complete public pairs. |
| R04/R05, Gaussian marginals and pairwise independence | Nhat is a full retained joint law; Xhat retains the actual Hhat kernel. No covariance-only inference occurs. |
| R06/R07 and same-Y posterior replicas | The precise frozen X1 is used with Y=S+G; no entropy-only extractor or independently sampled posterior observations are substituted. |
| R08 and C02 F5 latent/public erasure | OBS only uses TV contraction for upper bounds. RANK supplies a separate, explicit public test with information-theoretic recovery of F under strict gates. It does not infer a public lower bound from BNG. |
| C03-HC1/HC2 | NC1's delta<1 and kappa<1 guards remain explicit. H_seq is never equated to D_B. |
| C03-HC4 deconvolution | Gaussian broadening and Nhat use guarded full integer convolution, not positivity of Fourier ratios. The rational signed inverse and wrapped Z/5 counterexamples remain valid outside the required smoothing regime. |
| R13, Renyi transfer | No signed distinguishing advantage is moved via an event-only Renyi bound. |
| R14, active zeros | Both source laws are versioned; eta_iso and delta_act are distinct. RANK tests the public effect directly in its narrower regime. |
| R18/CP-1 cached-prefix | The old event is .0105>.01 despite marginal residual bounds. No selected-stage product occurs. H_seq's inherited comparison bounds full-path normalizers; the new binomial expectation is under explicitly independent original CRT coordinates. |
| R09/R10/R12 | Every norm gate is strict; the response box is eventually smaller than q; membership verifies an ideal coset and never identifies a planted binary witness. |
| R01 and R16/R17 | No binomial support, matrix surrogate, posterior sampler, statistical target-to-uniform planting, or renamed discarded mechanism is imported. The support law is the fixed full uniform d-family. |
| R11, R15, common-K and separate-Y controls | No mild-to-average amplification, repeated samples, common-K tensorization, rotations, or separate-Y extension is claimed. |

Two new hand controls expose the principal failure modes without a CPU search:

**HC-W3-1: a genuinely observable rank branch.** Take n=4,q=97,d=1,b=1, with F deterministically zero and E deterministically zero. This deliberately simplified control is not the asymptotic Gaussian instance. Put R0=0 and B0=nb=4. The strict gates hold: `sqrt(97)>4` and `97^(3/4)>16`. Roots are `33,47,64,50`; for example `33^2=22` and `33^4=-1 mod 97`. On the unique deficient branch U=0 the test checks beta in Box(4). P has beta=0, while Q has beta=V and the norm fact excludes every nonzero V from Box(4). The acceptance probabilities are exactly `1/97` and `1/97^2`; their gap is `96/9409=eta_iso`. This checks event probabilities and the q^-M factor directly.

**HC-W3-2: retaining the old secret would change the proof.** Over F3, take S uniform on `{0,1}`, G uniform F3, Y=S+G. Then Y is independent of S and `TV((Y,S),(Y,Z))=1/3` for uniform Z. If the old S is additionally retained, the analogous comparison `(S,Y,S)` against `(S,Y,Z)` has distance `2/3`. H3r is valid because the old S is discarded and the extracted side factors; it is not a same-Y resampling claim that preserves old-secret correlations.

These exact controls and the algebraic proof are provisional. No finite search was allocated or run. A fresh critic should independently reconstruct H3r to H4, the V translation at H5, and RANK's two norm arguments; same-model agreement is complementary mathematical review, not statistical independence.

## Disposition and next obligation

New claims are **W3-OBS v2** (general finite hybrid, instantiated source transfer) and **W3-RANK v1** (strict-regime public TV obstruction). Neither is globally accepted. The first removes the need to assume hardness of an F-dependent H_seq public source; it still uses the already proved mathematical completion internally. The exact independent active-point assumption remains unsupported, and ordinary uniform-point HLBDD leaves a public inverse-polynomial statistical gap for this route when c>1/2. This is a scoped limitation of the specified source tests and observable comparison, not an impossibility for all public maps, a source distinguisher in polynomial time, or a refutation of binary-RLWE hardness.

The useful next step is fresh review of these exact claim versions, followed by independently justified active-point source inheritance or a different explicitly authorized replacement for this rank-defective endpoint. No further source candidate, sample extension, automatic continuation, or unallocated experiment is included in this assignment.
