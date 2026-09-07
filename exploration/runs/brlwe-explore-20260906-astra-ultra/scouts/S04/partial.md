# S04 partial discovery notes

Started 2026-09-06 09:31 UTC. Scope: harmonic analysis of coefficient-binary sources projected modulo ideals; at most two candidate mechanisms. No experiments yet. Baseline files read.

Ledger: target degree n power of two; rank 1; coefficient basis; q odd polynomially bounded; iid coefficient-uniform {0,1} secret; iid coefficient D_sigma errors, modular law W_sigma,q; m polynomial ring samples. All ideal-projection calculations below concern the secret marginal only unless explicitly extended. Rotations are deterministic correlated views, not extra samples.

Initial direction: derive exact Fourier/collision formulas for binary projection and compare to ideal-index upper bounds. Investigate weighted exceptional-ideal mass as distinct from worst-case elimination of nonunits. Need first inspect the 2025 ring LHL primary statement. Feasibility warning: for n>=4 no odd prime makes X^n+1 irreducible (unit group modulo 2n has exponent n/2); maximal possible factor degree n/2 gives two prime factors.

## Primary source checks, 09:35 UTC

- Source-verified result: Boudgoust–Lapiha 2025/1080, Theorems 4–5 (printed pp.17–20), already organize extraction by exact generated difference ideal, with exact order-2 Renyi quantity sum_I N(I)^r Pr[<S-S'>=I]. Corollary 3 upper bounds by collision modulo ideals. Thus merely rewriting a weighted ideal-collision sum is not novelty.
- Source-verified result: their Corollary 6 handles low splitting by making all short nonzero differences units; Corollary 7 supplies a coarser well-spreadness bound and explicitly leaves well-spreadness under leakage to future work (printed p.23). Lemma 30 bounds symmetric bounded-uniform projection collisions by alphabet-size^{-degree}; its proof gives the binary analog 2^{-degree}.
- Source-verified result: Brakerski–Dottling 2020/1185 Theorem 6.9 requires noise lossiness at least n log_2(gamma log n sqrt(n))+omega(log lambda). Its proof pays log determinant of the short-basis lattice (printed pp.18–19). Theorem 4.1 of 2020/119 instead pays the chosen scalar projection dimension k times log q (decision case). The product binary source cannot pay more than n bits.
- Source-verified result: Bourgain–Konyagin, C.R. Math. 337 (2003), Section 2 Theorem 2.1, gives max_{t!=0}|sum_{h in H}e_p(th)| <= |H|p^{-gamma} for multiplicative subgroup |H|>=p^delta, gamma>0 depending only on delta. Primary PDF inspected at https://www.numdam.org/item/10.1016/S1631-073X(03)00281-4.pdf . It suffices for single fully split coordinates for polynomial q(n).
- Access failures: 2006 BGK Wiley epdf rejected as unsafe by web tool; IAS Bourgain–Glibichuk PDF timed out. No claim relies on these inaccessible files. Tao–Vu arXiv math/0511215 primary PDF accessed; its stated initial setting is integer coefficients, so no finite-field inverse statement imported without checking conditions.

## Candidate A: conditional Fourier extraction (fully written small calculation)

Restrict to odd prime q. Let J be an ideal of R_q, quotient V=R_q/J of F_q dimension d, v_j=X^j mod J. Let Y=S+G mod q coefficientwise with independent G_j~D_tau. Conditional on Y=y, bits remain independent with p_y=W_tau,q(y-1)/(W_tau,q(y)+W_tau,q(y-1)). Define beta_tau,q=4 E[p_Y(1-p_Y)] = 2 sum_y W(y)W(y-1)/(W(y)+W(y-1)) in (0,1]. For additive character ell in V^*,

E_Y |E[exp(2 pi i ell(S)/q)|Y]|^2 = product_j (1-beta_tau,q sin^2(pi ell(v_j)/q)).

Consequently E_Y Coll(S mod J | Y)=q^{-d} sum_{ell in V^*} product_j(1-beta sin^2(pi ell(v_j)/q)). No independent samples or transformed error law are presumed. This is exact for wrapped Gaussian leakage, as opposed to the transcript itself.

If d=1 and J=(X-r), ord_q(r)=2n, H=<r> has size 2n. Pairing +/- gives sum_{j<n}sin^2(pi t r^j/q)=n/2-(1/4)sum_{h in H}e_q(th). BK Theorem 2.1 then bounds each nontrivial expected squared Fourier coefficient by exp[-beta n(1-q^{-gamma})/2]. Thus joint statistical distance of (S(r),Y) from (U(F_q),Y) <= (1/2)sqrt(q-1) exp[-beta n(1-q^{-gamma})/4]. For fixed positive tau and q growing polynomially, beta is bounded below by a positive tau-dependent constant; wider tau is also viable. This proves conditional extraction for a single CRT coordinate, not arbitrary ideals or a rank-one RLWE hardness bridge.

## E02 exact experiment completed, 09:36 UTC

Coordinator allocated one CPU slot until 09:38 with timeout 30 s. Code: experiment_e02.py; output: experiment_e02.json; seed=none. First invocation `timeout 30s python ...` failed (exit 127; python alias absent); rerun with python3 passed in 0.177 s. No other experiments run. Direct n=8,q=17 Fourier sum equals exact projection collision 241/4096 with floating difference 0.

Exact binary enumeration examples (error absent; secret marginal only):
- n=4,q=3, J=(X^2+X-1), feasible two-splitting: collision 1/8, support 8 of 9, TV 1/9. Nonzero difference X^2+X-1 lies in J: choose S=X^2+X and S'=1. Factorization (X^2+X-1)(X^2-X-1)=X^4-3X^2+1.
- n=8,q=3, J=(X^4+X^2-1): collision 1/64, support64 of81, TV17/81.
- n=8,q=5, J=(X^4-2), feasible two-splitting: injective on 256 binary secrets, TV369/625. This shows q>n is sufficient, not necessary, for unit differences.
- n=8,q=13, J=(X^4-5), feasible two-splitting: injective, TV28305/28561.
- n=8,q=17, J=(X-3), full splitting: collision241/4096, TV1/272. Explicit difference X^4+X+1 vanishes at3 (81+3+1=85).
- Same n,q, J=(X^2-9), two selected full-split slots +/-3: injective, TV33/289.
- Same n,q, J=(X^4-4), four selected full-split slots: injective, TV83265/83521. Reduction yields independent pairs S_j+4S_{j+4}, each supported on {0,1,4,5}.
- n=16,q=97, r=19 of order32: singleton CRT TV9/24832, collision1383689/134217728.

Hand checks: 3^8=-1 mod17; 19^16=-1 mod97; 2^2=-1 mod5; 5^2=-1 mod13. All quoted quotient polynomials divide X^n+1. Constant-q cases illustrate geometry only and do not meet the growing q/sigma noise separation target.

## Low-splitting feasibility and limits (fully written small calculation)

For n>=4 power of two, the exponent of (Z/2nZ)^* is n/2, so odd-prime irreducible factor degrees cannot exceed n/2. Prime q=3 or5 mod8 attains n/2 for sufficiently large n (including displayed n=8 examples). There are at least two CRT fields. If D in {-1,0,1}^n is nonzero, Parseval and arithmetic-geometric mean give |Norm(D)| <= ||D||_2^n <= n^{n/2}. If D vanishes in a degree-d prime quotient, q^d divides its nonzero integer norm; hence q>n^{n/(2d)} guarantees all nonzero binary differences are units. At feasible two splitting d=n/2, q>n suffices. This is the elementary content behind existing short-invertibility bounds, not a new mechanism.

Under that unit-difference condition, each prime-ideal projection is injective on the binary cube. Thus it retains all n bits and has TV at least 1-2^n/q^{n/2}; it cannot be a low-information compression. Low splitting helps universality for multi-input ring hashes but does not supply a single-binary-input entropy surplus.

## Entropy-budget refinement and explicit obstruction, 09:40 UTC

Coordinator correctly flagged that n=8,q=17 degree2 and degree4 examples have q^d>2^n. They are boundary sanity checks, not counterexamples to extraction inside d log2 q<n. Likewise two-splitting q=13 lies beyond the binary entropy budget. The unknown statement must stay inside the conditional entropy budget.

However, the q=3 example yields a fully written within-budget counterexample to any unrestricted total-entropy-only criterion. Let n>=4 be a power of two and h=n/4. Over F_3,

X^n+1=(X^{2h}+X^h-1)(X^{2h}-X^h-1).

These are the two irreducible factors (ord_{2n}(3)=n/2). Set J=(X^{2h}+X^h-1). In each residue class modulo h, put T=X^h so T^2=1-T and T^3=-1-T. Four binary bits (a,b,c,d) reduce to (a+c-d)+(b-c-d)T mod3. Their images occupy exactly 8 of the9 coefficient pairs, twice each; the missing pair is (2,1). One can verify the list by separating (c,d)=(0,0),(1,0),(0,1),(1,1), which gives four shifted {0,1}^2 squares. Consequently S modJ is uniform on8^h residues, collision8^{-h}, and TV=1-(8/9)^h. Yet log2|R_q/J|=(log2 3)n/2 <0.793n, leaving >0.207n bits of unconditional entropy slack. This refutes an unrestricted criterion based only on degree and total binary entropy. It is not a counterexample in the target small-noise asymptotic regime: q=3 is fixed, so q/sigma cannot grow like n^c when sigma is bounded below.

## Candidate B: structured-ideal spectrum and block factorization

For J=(X^d-a) dividing X^n+1, put L=n/d so a^L=-1. Reducing S separates d independent binary blocks T_j=sum_{k<L}a^k S_{j+kd}. Under the same surrogate Y=S+G modq leakage, the exact Fourier identity tensorizes:

q^d E Coll(S modJ | Y)=[sum_{t in F_q} product_{k<L}(1-beta sin^2(pi t a^k/q))]^d.

This converts a growing-degree ideal problem to a scalar geometric-progression collision problem at effective length L, and exposes what a candidate inverse theorem must measure. Source comparison: this block decomposition is already in Lyubashevsky–Seiler (2018), Section3.2 equations(12)–(13), used there for worst-case invertibility; the prospective difference is quantitative conditional collision / Fourier-energy enumeration of the binary block distribution.

For general J, define E_J(ell)=sum_j sin^2(pi ell(X^j modJ)/q) and N_J(t)=#{ell !=0:E_J(ell)<=t}. Then K_J(beta)=sum_{ell!=0} product_j(1-beta sin^2(...)) <= integral exp(-beta t) dN_J(t), and TV((S modJ,Y),(U,Y)) <=sqrt(K_J(beta))/2. The scalar sequence ell(X^j) satisfies the recurrence of the quotient polynomial; classify low-energy recurrence sequences rather than discard every exceptional ideal. In a binomial quotient, characters supported on one output coefficient have energy at most L=n/d, so a uniform Omega(n) energy claim is false even when d logq<n. The needed statement concerns the aggregate weighted spectrum. No such general theorem is proved here.

Multiplier clarification (fully written small calculation): multiplying the quotient output by any unit b is a bijection, so conditional collision and distance to uniform are unchanged. Exceptional multipliers for this object are controlled by their kernel ideals, not the numerical size of an invertible multiplier. This does not hold automatically if one also changes the leakage or coefficient error law.

Inverse-theorem warning: Tao–Vu (arXiv math/0511215), Theorem2.5 and Corollary2.7 are stated for integer/torsion-free coefficients and polynomially large concentration. They cannot be directly transplanted to modular near-uniformity at scale1/q. In the binomial threshold L~logq, 1/q is exponentially small in L. A suitable finite-field quantitative statement, including the modular uniform baseline, is still missing.

## Source-verified upgrade: actual joint extraction for structured ideals, 09:42 UTC

New primary source accessed: Breuillard–Varju, *Cut-off phenomenon for the ax+b Markov chain over a finite field*, arXiv:1909.09053v2 (24 August 2022), https://arxiv.org/pdf/1909.09053 . Section2 Theorem5 states, with absolute C, for any two-point-or-more step distribution mu on F_q and multiplier a of order at least C log q logloglog q,

T_2(delta) <= C/(1-||mu||_2^2) * log(q/delta) log q (loglog q)^5,

where T_2(delta) is the first walk length L with q||mu_a^{(L)}-U||_2^2<=delta^2. Lemma6 identifies low multiplicative order as the exceptional case for a quantitative orbit-energy lower bound; its derivation uses a low-degree, small-Mahler-measure polynomial vanishing at a. Their sharper Theorems1–3 average over most multipliers (and in stronger forms primes/GRH); those cannot simply be restricted to cyclotomic roots. Only the uniform Section2 result is used here.

Fully written small calculation applying it: choose p_beta=(1-sqrt(1-beta))/2, and mu_beta=Bernoulli(p_beta). Then |hat(mu_beta)(t)|^2=1-beta sin^2(pi t/q), and 1-||mu_beta||_2^2=beta/2. Therefore the exact averaged conditional Fourier energy from CandidateA equals ordinary Fourier energy for this effective biased-Bernoulli walk. This is an identity of collision quantities; it does NOT replace the actual uniform-binary secret distribution by biased bits.

For full splitting q=1 mod2n, let L|n be a power of two, d=n/L, r have order2n, and a=r^d have order2L. Then X^d-a divides X^n+1. Define

k_L=sum_{t!=0} product_{k<L}(1-beta sin^2(pi t a^k/q)).

Theorem5 gives k_L<=delta^2 once L is at least its displayed bound with beta/2 substituted. Exact independence of the d coefficient blocks gives K_J=(1+k_L)^d-1, whence conditional TV<=1/2 sqrt((1+delta^2)^d-1).

Consequently, for polynomial q(n), beta>=beta0>0, and L a power of two of size Theta((log n)^3), the above distance is negligible in n: for every fixed A, the required time for delta=n^{-A} is O_A((log n)^2(loglog n)^5)=o((log n)^3), and d<=n. The order condition 2L>=C log q logloglog q also holds. This establishes a joint selected-CRT projection result, of degree d=Theta(n/(log n)^3), strictly within the entropy budget. It does not classify all ideals; the binomial ideal is specifically chosen. It uses only a surrogate Y=S+G_tau modq with independent coefficient G, not the mixed RLWE transcript. The target secret, rank, original sigma and number of samples are unchanged; tau is an auxiliary leakage width with beta>=beta0.

This is the strongest surviving mechanism: the first substantive difference from the old scalar-rank / lattice-index arguments is a source-specific conditional extraction bound for an explicit structured quotient of one binary ring element. What remains missing is a computationally pseudorandom rank-one public-mask construction that spends only this quotient information and allows the source-side Gaussian decomposition at target noise. A bare nonunit multiplier exposes its annihilator, while unit multiplication cannot reduce information. The Fourier lemma alone provides neither public-mask pseudorandomness nor a search/decision reduction.

Cheap next test (future, not run): select feasible full-splitting prime q around a polynomial in n and measure k_L by O(qL) exact-modular orbit / floating-Fourier computation for powers-of-two L around logq, log^2q, and log^3q; tensorize analytically for d=n/L. Test beta=1 and beta=1/2, and compare the worst a of order2L, not random a from all F_q. This tests whether the log^3 n block size can be materially reduced before any hardness construction is attempted.

Auxiliary-width witness: tau=2 already ensures a uniform positive beta lower bound for every odd q. Indeed W(0)>=D_2(0), W(1)>=D_2(1), W(0)+W(1)<=2, and the y=1 summand in beta=2 sum_y W(y)W(y-1)/(W(y)+W(y-1)) is at least D_2(0)D_2(1)>0. This chooses only the auxiliary leakage width, not the target error width sigma.

Tooling note: local `pdftotext` was absent (exit127). The supplied text extracts were readable; load-bearing short-invertibility conditions were checked in the authors' primary PDF at crypto.ethz.ch instead. No source-access gap affects the stated conditional extraction calculation.

Discovery completed 2026-09-06 09:43 UTC; final scouting note written 09:44 UTC, 560 words before minor link correction. No further computation or research planned.
