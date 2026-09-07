# F03 primary-source ledger and exact mismatches

Checked on 2026-09-06. Equations below use the authors' parameter names only within their own entries. Elsewhere n is ring degree, d is active-support size, gamma is coefficient perturbation width, tau is auxiliary width, and sigma is target coefficient width. Source facts, mathematical deductions, and unproved matching claims are distinguished. This is a bounded comparison, not an audit of every theorem in these papers.

## S1. Order-LWE / HLBDD

Bolboceanu–Brakerski–Perlman–Sharma, [2018/494](https://eprint.iacr.org/2018/494), full version last revised 2019-09-04; original received 2018-05-23; ASIACRYPT 2019. Primary [46-page PDF](https://eprint.iacr.org/2018/494.pdf), printed pp.37–41, Sections 7.1–7.2, Definitions 7.1, 7.3, 7.4, Lemmas 7.2, 7.6, 7.7, Theorem 7.5; swallowing definition on printed p.11. The conference [primary version](https://www.iacr.org/archive/asiacrypt2019/119210284/119210284.pdf) retains the definitions but leaves the formal theorem/proof to the full version.

**Exact source and endpoint.** In the intended shared-lattice interpretation of Definitions 7.3–7.4, choose a uniform ideal Q in P_(n-k), then independent x_1,x_2 uniform in Q/qR and independent e_1,e_2~D_(R,r'). Publish (x_1+e_1,x_2+e_2), compared with a uniform pair in R_q. Here P_j contains all products of j distinct prime factors of qR. Thus Q/qR has k active CRT coordinates. The source contains no binary secret and makes no covariance-completion correlation. Definition 7.4 is terse: read literally, drawing twice from Definition 7.3 could resample the lattice, and its comparator is printed L2/L. The introduction's initialized oracle and Lemma 7.7's common Q make the intended same-lattice, ambient-mod-q experiment clear. This interpretation must be stated, not silently replaced by two independent supports.

**Imported parameter record.** Theorem 7.5 assumes a fully split prime q, k-wise ϕ as in Definition 7.1, B-bounded ϕ, a smoothing parameter κ>=eta_epsilon(R), and Gaussian vectors r,r',t,tilde-r,r-star. Put r_(κ,i)=sqrt(r_i^2-κ^2). The printed equation is (r-star_(κ,i))^2=r_(κ,i). Required swallowing relations are r-star swallowing t and tilde-r, r swallowing t, and tilde-r swallowing r'. Definition 2.13 means n||t||_infinity/min_i r_(κ,i)=negl(n). The theorem reduces HLBDD at r' to entropic decisional R-LWE at r, assuming ordinary R-LWE at t separately. Lemma 7.7 handles one sample; Lemma 7.6 provides sample rerandomization using the additional RLWE assumption and swallowing.

**What is actually matched.** The basic pair, full random support family, and a uniform comparator are independently motivated prior assumptions. Their computational hardness is not derived from the paper's worst-case Order-LWE result. Lemma 7.2 explicitly conditions x_1 to be invertible on the active support, while Lemma 7.7 samples x_1 uniformly and its H3 justification uses superpolynomial q to discard failures. That superpolynomial premise is load-bearing in the proof even though it is not repeated in the displayed Theorem 7.5 statement. SC0 resolves invertibility by changing the first-point law; importing the old hardness then costs delta_unit or needs a separate reduction.

**Normalization deduction.** For the power-of-two ring, the canonical embedding satisfies ||can(x)||_2=sqrt(n)||coeff(x)||_2. A *spherical* D_(R,r') therefore has iid coefficient width r'/sqrt(n). Elliptical canonical widths generally do not produce iid coefficient errors. This fixed polynomial conversion cannot turn an inverse-polynomial separation into negligible swallowing.

**Polynomial-baseline obstruction to this import.** The target coefficient sigma is polynomial because q is polynomial and q/sigma>=n^c. Therefore its canonical r is polynomial. If the old swallowing requirement n||r'||_infinity/min_i tilde-r_(κ,i)=negl(n) holds with polynomial tilde-r, then r' itself is negligible. The discrete perturbation is zero with overwhelming probability. For a proper ideal, x_1+e_1 is then a nonunit with overwhelming probability, whereas a uniform ring element is a unit with probability (1-1/q)^n>=1-n/q>1/2. A public gcd/unit test gives constant advantage. Thus shrinking source noise to make this particular swallowing proof fit polynomial target widths destroys HLBDD hardness. This is a restriction of that import, not an impossibility for covariance completion or other channels.

The paper's B-bounded wording only asks for nonnegligible probability of a bounded norm, although subsequent hybrids reason in statistical-distance terms. No blanket certification of that issue is made here. For the proposed binary secret one can instead impose the deterministic bound ||can(S)||<=n, so a clean source import need not rely on the weaker wording. Definition 7.1's display averages over P while the surrounding prose asks for every k-set; SC0 should retain a joint extraction statement with its actual support, avoiding both ambiguities.

## S2. General entropic LWE is a matrix theorem

Brakerski–Döttling, [2020/119](https://eprint.iacr.org/2020/119), received 2020-02-06, revised 2020-06-23, EUROCRYPT 2020. The supplied local primary PDF and prior text copy were read. Relevant locations: Proposition 3.2 (continuous Gaussian decomposition), Theorem 4.1 (printed p.16), Definition 2.6 (entropic LWE).

Theorem 4.1 fixes n,m=poly(lambda), m>=n, an r-bounded secret S (r=q allowed), e_1~D_sigma1 mod q, and demands

    Htilde_infinity(S|S+e_1)
      >= k log(min{2 C gamma sqrt(n) r,q}) + omega(log lambda),
    sigma > C sqrt(m) gamma sigma1.

It derives entropic *search* LWE from dLWE(q,k,D_(Z,gamma)). Its additional decision statement uses the stronger entropy threshold k log q+omega(log lambda), requires prime q or binary S, and additionally assumes dLWE(q,k,m,D_sigma). Its public lossy matrix is BC+F with independent rectangular random matrices and Gaussian F. Proposition 3.2 uses an exact continuous covariance complement sigma^2 I-sigma1^2 F^T F, under the operator inequality sigma>sigma1||F||_op.

**Mismatch.** A ring multiplication matrix is not an independently sampled rectangular matrix. The theorem supplies neither a distribution of hidden CRT ideals nor a two-point correlated source. The scalar factor sqrt(m) belongs to its matrix dimensions; replacing those dimensions by a ring rank or rotations is not an import. Its continuous Gaussian machinery motivates the completion calculation, but the finite wrapped-discrete law and SC0 source hardness remain separate.

## S3. DSPR/NTRU and the lossy ring sampler

Brakerski–Döttling, [2020/1185](https://eprint.iacr.org/2020/1185), received 2020-09-30, TCC 2020 major-revision full version. Supplied local primary PDF read through its prior text copy. Relevant locations: Definition 6.1 p.19; Theorem 6.2, Lemmas 6.3–6.6 pp.20–21; Lemma 6.8 and Theorem 6.9 pp.21–22; Definition 5.1, Proposition 2.2, Lemma 5.4, Theorems 5.7–5.8; Definitions 3.1–3.3 and Lemmas 3.4–3.5.

**Source definitions.** DSPR takes independent f,g~D_(R,gamma), conditioning f mod q to be a unit, and publishes h=g/f mod q versus uniform R_q. Only f is conditioned in Definition 6.1. It is an independently studied ratio assumption, with efficient conditioning needing its own lower bound. The paper's DSR generalization (Definition 5.1) publishes Z_0^(-1) Z mod q versus the desired matrix law. Its ring instantiation takes independent e_i,e'_i~chi and z_i=g e_i+f e'_i; the public tuple is

    A_i=z_i/f=(g/f)e_i+e'_i mod q,  1<=i<=k.

Lemma 6.6 justifies this tuple jointly from DSPR and Hermite-form RLWE for chi. The public DSPR reduction samples e_i,e'_i itself from a challenge h; a k-step Hermite-RLWE hybrid then replaces the outputs. This source transfer is real, but it has a common short denominator, not two independent ideal points in a random CRT support.

**Widths and endpoint.** Definition 2.3 uses continuous Gaussian noise lossiness nu_sigma(S)=Htilde_infinity(S|S+e). Theorem 6.9 requires

    nu_sigma(S) >= n log(gamma log(n) sqrt(n)) + omega(log lambda),
    sigma_0 >= O(sigma n log(n) B sqrt(k)),

where chi is B-bounded and both DSPR_gamma and RLWE_chi are assumptions. Its conclusion is *mild search hardness* for k ring samples. Theorem 5.8 additionally has sigma>tau_2 eta_epsilon(Lambda(Basis^(-1))) and sigma_0>2^(3/2) tau_1 sigma, with the two singular-value bounds holding on a delta-fraction of sampler coins. Lemma 6.8 obtains the bounds under

    gamma > max{sqrt(n ln(2n(1+n^2))/pi) q^(1/n), 8n eta_epsilon(R)}.

The underlying probability estimates and coefficient/canonical inverse-norm conversions are not recertified here; the prior C02 ledger already isolates that normalization issue. No use of a disputed probability import is needed for the mismatch conclusions.

**Why this does not solve the baseline.** For dense binary S, nu_sigma(S)<=n bits. Already any gamma bounded below by a positive constant makes n log(gamma log(n) sqrt(n)) exceed n asymptotically. The stated sufficient entropy budget therefore does not cover this source secret. Setting gamma to a tiny value to evade the inequality abandons the verified sampler regime and its unit-conditioning analysis. Mild hardness also differs from negligible average recovery at a fixed sample budget; Lemma 3.4 invokes an unrestricted sample oracle, and Lemma 3.5 changes the error experiment through finite-input rerandomization. None is an unchanged iid wrapped-D_sigma decisional conclusion.

**NTRU normalization boundary.** Theorem 6.2 restates Stehle–Steinfeld for fully split prime q>=5, n>=8 power of two, 0<alpha<1/3, and gamma>=n sqrt(ln(8nq)) q^(1/2+alpha). It conditions *both* f and g to be units and compares g/f to uniform units, with its stated exponential statistical bound. That is a different conditioning/comparator from Definition 6.1; the surrounding argument uses additional RLWE and conditioning reasoning. The larger gamma regime permits dropping the DSPR assumption in the paper, but demands more than roughly (1/2+alpha)n log q input entropy, which binary S cannot provide at polynomial growing q. No claim that all small NTRU/DSPR widths enjoy worst-case hardness is made.

The continuous covariance complement is already Proposition 2.2 and its stacked form is Lemma 5.4. The latter controls the whole concatenated Gaussian vector, with operator norm of the full block matrix. The discrete convolution intermediates in Theorem 5.7 are not an independently justified paired noisy-ideal source with an F-conditioned anisotropic H.

## S4. Partial Vandermonde/ideal decoding

Boudgoust–Gachon–Pellet-Mary, [2022/709](https://eprint.iacr.org/2022/709), received 2022-06-03, revised 2022-09-01; CRYPTO 2022, DOI 10.1007/978-3-031-15979-4_17. Primary [35-page PDF](https://eprint.iacr.org/2022/709.pdf) checked directly. Definition 2.14 (p.14), Theorems 3.1–3.2 (pp.15–16), Lemma 4.1 and Corollary 4.2 (pp.20–21), Section 4.3, Section 5, Appendix B.

PV-Knap publishes a *known* set Omega of t roots and the residue of a bounded a modulo I_Omega, and asks to recover a; its defining bound is 2B<sqrt(n) q^(t/n), with B in canonical norm. The natural decision version compares the residue to uniform. Theorem 3.1, for an unramified ideal and gamma>=2sqrt(n), gives Hermite-SVP runtime

    exp(O(n log(n)/(|H_I| log(gamma/sqrt(|H_I|))))) * poly(input size),

where H_I is the ideal stabilizer in the Galois group. Corollary 4.2 reduces power-of-two ideal-HBDD to Hermite-SVP in the inverse ideal when gamma_1>2gamma_4. Section 4.3 combines these into attacks for suitable stable supports and q^(t/n)>=8B. Section 5 also tests random *public* supports after discarding coordinates to obtain a stable subset; those are concrete attack results, not a theorem of generic random-support hardness.

**Precise mapping.** If SC0's T were known, A reduced modulo the ideal vanishing on T^c is a PV-Knap noisy coset of F with t=n-d. Hidden T must first be learned, guessed, or bypassed. In [F03-attacks.md](F03-attacks.md), A2 accounts for that cost using subgroup-orbit super-supports and derives an exp(O(d)) attack under an explicit polynomial noise gap. This is an actual algorithmic connection; there is no converse hardness import for hidden paired samples or an F/H completion law.

Targeted follow-up: Boudgoust–Sakzad–Steinfeld, [2022/679](https://eprint.iacr.org/2022/679), revised 2023-06-15, DOI 10.1007/s10623-022-01083-7, introduces PV-LWE and states computational equivalence with PV-Knap. The exact PDF was denied by the browser and the DOI fetch failed, so no theorem-numbered reduction from that source is imported here. BGP22 Appendix B independently records the known-support equivalence in power-of-two cyclotomics. This is a search lead and conceptual comparison only.

## S5. Ring leftover hashing under leakage

Boudgoust–Lapiha, [2025/1080](https://eprint.iacr.org/2025/1080), latest ePrint revision 2026-02-12. The supplied `literature/related/2025-1080.pdf` is HAL lirmm-05396888v2, deposited 2026-06-03, manuscript dated 2026-02-12, EUROCRYPT 2026 full revision (DOI 10.1007/978-3-032-25327-9_3). These are two version dates for the same supplied text, not a 2025 theorem frozen before later revisions.

Theorems 4–5, printed pp.17–19, consider independent uniform ring matrices A and a distribution P on ring vectors x. They express the order-two likelihood moment exactly by summing N(I)^(number of rows) times the probability that the coordinate differences x_i-x'_i generate I. Theorem 5 replaces this probability by its average under the leakage-conditioned pair law. Corollary 6 adds low-splitting and a strict norm bound; Corollary 7 uses well-spreadness but does not include a general leakage version.

**Mismatch.** The identities are available machinery, not a bound for this particular random CRT quotient given Y=S+G. A support-specific collision/Fourier estimate is still required. The high-splitting polynomial-q baseline does not meet Corollary 6's small-difference universality condition for dense binary inputs; Corollary 7 cannot simply be conditioned on Y. This paper supplies no computational noisy-ideal assumption or completion-kernel hardness. Counting collisions by generated ideals and the general leakage organization are prior work, so no novelty is claimed for those steps.

## S6. Paired/correlated-source search result and its limit

Targeted searches included combinations of HLBDD, hidden ideal, correlated Gaussian noise, paired RLWE, noise completion, PV-LWE and correlated-noise attacks. They identified the actual preceding Gaussian-complement lemmas, HLBDD, DSPR's common-denominator tuple, and [Agrawal–Pellet-Mary 2020/415](https://eprint.iacr.org/2020/415), received 2020-04-13, EUROCRYPT 2020. In that paper Definition 4.1 and Lemma 4.3 treat a different four-pair correlated source with reciprocal small denominators; their determinant-product attack works under the stated q>>(n sigma)^8 gap. See A5 in F03-attacks.md for scope.

No checked source theorem gives an exact public reduction from an independently studied distribution to SC0 with H drawn from the prospective F-dependent anisotropic discrete-Gaussian covariance complement. This is a bounded-search outcome, not a novelty claim or evidence of hardness. The public-shear transfer in F03.md is an explicit limited source reduction and should be used to distinguish justified correlations from arbitrary tailored ones.
