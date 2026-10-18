# B-SUP-IR-P v1 — proof and operational scope

Status: PROVISIONAL author proof of ideal-ring-sis-theorem-v1.md. Primary mechanism adapted with new ring arguments from 2026/2443 Sections4.4–4.5. It is not an invocation of that paper's general hardness theorem.

## 1. Natural inclusion and exact lifted relation

Because gcd(D,q)=1, multiplication by q on R/J is invertible. Hence J intersect qR=qJ. The natural inclusion J/qJ -> R/qR is injective and both groups have q^n elements, so it is an isomorphism. In particular, A0=qV mod qR has uniform target Rq^h when V mod J is uniform in (J/q)/J.

Every E1/E2 column is in J and every C column is in J. Every Q component is in J/q: this fractional ideal is closed under multiplication by ring masks. Moreover qQ=A in Rq. If Ax=0, then qQx is in J intersect qR=qJ, so Qx is in J. This argument uses the ideal property essentially and does not replace arbitrary lattice columns by multiplication matrices without justification.

## 2. Full residual encoder, in natural ring coordinates

For target u in Rq choose an integer coordinate representative of B^-1 u mod q, denoted ztilde. Put x=B ztilde/q in J/q. Coordinatewise nearest-integer rounding gives u' in R with ||x-u'||<=sqrt(n)/2. The quotient encoder gives z3 in {0,1}^k with u'-sum_l g_l z3_l in J. Put

  rcorr=x-u'+sum_l(g_l-b'_l)z3_l.

Then rcorr lies in J/q and has norm at most R0. Furthermore

  q rcorr + C z3 = u mod qR.

Set z1=round(p rcorr) in Z^n, so ||z1||<=Z1 and its rounding error ez=z1-p rcorr has norm at most sqrt(n)/2. Write K=(q/p)B^-1+DeltaK with ||DeltaK||op<=||DeltaK||F<=n/2. The integer vector

  zrem=qB^-1 rcorr-Kz1
      =-(q/p)B^-1 ez-DeltaK z1

has norm at most Zrem. Signed binary expansion gives z2 in {-1,0,1}^b with Gz2=zrem. Therefore

  E1 z1+E2 z2+C z3=u mod qR.

The components of z1,z2,z3 are integer constants interpreted as ring elements. They are not claimed to be independent uniform bits. The quotient part alone is not an additive homomorphism into Rq; the displayed residual terms retain the necessary carry information.

For each ring gadget target 2^j, choose this encoding and set z0=-R1z1-R2z2-Sz3. Then [A|W](z0,z1,z2,z3)=2^j. A coefficient of z0 is bounded by ||z1||1+b+k<=sqrt(n)Z1+b+k. The remaining preimage coefficients obey the same Btrap bound. Multiplication of these preimages by X^a, 0<=a<n, gives a coefficient-expanded integer trapdoor for all targets 2^j X^a, with the same entry bound. Thus Dpub's n by N coefficient expansion has a standard n-row gadget trapdoor. This justifies use of the general preimage SAMPLER at this matrix; it does not invoke a general matrix HARDNESS theorem.

## 3. Entire public law and rank selection

By smoothing at sigma>=2eta_epsilon(J), every coset theta rho_sigma(c+J), divided by sigma^n/D, lies between 1-epsilon and 1+epsilon. The V mod J law is the uniform law on q^n cosets reweighted by these values and divided by their actual mean. Its distance is at most epsilon/(1-epsilon). A product hybrid for h initial columns costs h times this bound. No exact Gaussian convolution equality is assumed.

Now replace A0 by uniform U0 while retaining the independently sampled sign masks. The ring extraction theorem ring-extraction-theorem-v1.md applies with coefficient maximum atom 1/2. Conditional on U0, the t+k independent mask columns give a PRODUCT of their conditional output laws. A hybrid that retains U0 gives total distance at most (t+k)gamma_hash. It does not replace that law by a product of averaged collision probabilities. Fixed ring offsets E1,E2,C do not affect the bound. Thus (A,W) is delta_pub-close to independent uniform ring rows.

For a uniform ring row A, failure to generate Rq occurs if all m values vanish at some CRT root, of probability at most nq^-m. The real rank event therefore has probability at least alpha. Conditioning both joint laws on the SAME rank event changes their distance to at most 2delta_pub/alpha. In the ideal law, W stays independent uniform because the event depends only on A. In the real law, ALL retained latents follow the rank-posterior; no fresh independence is claimed for them.

For each retained state the bounded trapdoor is valid, so SamplePre's per-state canonical comparison, averaged and hybridized over gq targets, costs delta_hint while retaining V,R1,R2,S,Q. The exact canonical hint conditional law depends only on A,W, not on the private construction trapdoor. Adding that common conditional kernel preserves the public distance. Independent capped rejection contributes at most (1-alpha)^a and initial sampler error delta_init. This proves the public Delta bound and, by appending the same independent response kernel, BOTH response endpoints in the statement.

## 4. A nonzero ring relation yields a nonzero ideal vector

Work first with exact initial Gaussians, one attempt conditioned on rank success, and exact canonical T. Let the solver use independent coins; invalid outputs are set to zero. Partition x=(x0,x1,x2) and set c=x0+R1x1+R2x2 in R^h.

If x1=x2=0 on a valid output, c=x0 is nonzero. Otherwise fix a column j of R1 or R2 and consider valid outputs whose corresponding x_j is nonzero and for which c=0. Before rank conditioning, fix A0, S, all other mask columns, and the canonical hint and solver random tapes. The public input and rank decision depend on this remaining sign column only through its ring hash A0 R_col, with at most q^n possible values. For each such value the solver output is fixed. Multiplication by the nonzero x_j is injective in the characteristic-zero integral domain R. Therefore c=0 determines AT MOST ONE entire ring column R_col in R^h. Every such coefficient-sign column has probability 2^(-nh). Union over the t possible columns, then divide by rank-success probability, gives

  Pr[valid and c=0] <= t q^n 2^(-nh)/alpha.

This is a counting bound before selected-key conditioning. It does not claim uniformity or independence of a sign column after its hash has been exposed.

On valid outputs with c!=0 choose its first nonzero index i. Condition on A0, all masks, the canonical hint and solver coins/output, and all V columns except v_i. These quantities determine the index i and c. Because the canonical hint depends on the private state only through A,W, and rank depends on V only through A0, the remaining conditional law is EXACTLY D_(a_i+J,sigma), where a_i+J is the residue class fixed by A0_i. This also uses J intersect qR=qJ to identify the residue fiber.

The equation Qx=0 is an affine equation in v_i with coefficient c_i. In the number field Q[X]/(X^n+1), multiplication by nonzero c_i is invertible, so at most one v_i satisfies it. Smoothing at sigma/2>=eta_epsilon(J) gives every coset Gaussian atom at most 2^-n(1+epsilon)/(1-epsilon). One direct proof groups a_i+J into its 2^n cosets modulo 2J and bounds each coset mass by smoothing; each point mass is at most its coset mass. Adding the mask-zero bound proves beta_zero. Zero divisors modulo q do not invalidate this step: the injectivity is over the characteristic-zero field, before reduction modulo q.

## 5. Uniform norm bound and success probability

For a centered lattice Gaussian D_(L,sigma), its exponential moment is at most exp(sigma^2||t||^2/(4pi)). Completing the square leaves rho_sigma(L-c)/rho_sigma(L)<=1, since centered theta is maximal by Poisson summation. Thus each coefficient satisfies Pr[|v_j|>sigma ell]<=2exp(-pi ell^2). Union over hn coefficients and conditioning on rank costs at most beta_tail. On the resulting event ||V||F<=sigma sqrt(hn)ell.

For a ring element z, its negacyclic multiplication matrix M_z has Frobenius norm sqrt(n)||z||coef. The coefficient expansion of the ring row V therefore has operator norm at most sqrt(n)||V||F<=sigma n sqrt(h)ell. The combined h by t mask matrix has coefficient-expanded Frobenius norm n sqrt(ht), since every ring block has n^2 entries of magnitude one. Consequently the coefficient expansion of [I|R1|R2] has norm at most sqrt(1+n^2ht). The deterministic ring row [E1/q|E2/q] has operator norm at most (sqrt(n)/q)||[BK|BG]||F. Their sum is H. This bound is simultaneous for every x, including adaptively selected solver output.

On the exact accepted canonical experiment, validity has probability at least delta-2delta_pub/alpha. Subtracting beta_zero and beta_tail gives the desired good-output event. Passing to the implemented experiment changes this SINGLE event by at most delta_impl, rather than repeatedly charging the same implementation discrepancy. This yields delta-Delta-beta_zero-beta_tail. Every accepted output is independently checked for its exact ideal membership, nonzeroness and declared norm.

## 6. Initial Gaussian implementation and bit complexity

Let M=B/q, an ordinary rational basis of J/q. In integer coordinates the desired law has width-squared matrix Vcoord=sigma^2 M^-1 M^-T. Choose rational a0>=max(1,sqrt(log(8n/epsilon_g)/pi)) and impose sigma>=sqrt(2)a0||B||op/q, so Vcoord>=2a0^2 I. Apply elliptical-multiplier-sampler-v2.md to this rational matrix, then multiply its exact integer output by M. The total variation per draw is at most

  epsilon_g/(1-epsilon_g)+4pi xi/a0+zeta+n nu.

Taking a h times this bound at most delta_init covers every attempted initial draw, including adaptive rejection, by sequential coupling. This is an ordinary-basis Gaussian algorithm, with a width floor explicitly tied to B/q; it does not assume an efficient sampler at smoothing from an arbitrary basis. All rational numerator/denominator encodings and requested precision lengths count in runtime, per the repaired v2 operational dependency.

SNF quotient arithmetic, nearest plane, modular B inversion, coefficient-expanded trapdoor construction and checking use polynomial bit complexity. Initial draws and scalar rejection samplers take expected polynomial time. The preimage sampler is the imported primitive stated in the theorem, with numerical error delta_pre separately charged. No exponential enumeration of R/J is used.

## 7. What is and is not supplied

The map supplies a concrete ideal-to-ring-SIS one-vector reduction and a complete public hinted ring-LWE law comparison. It addresses the earlier basis-coordinate obstruction for INTEGRAL ideals coprime to q by using natural inclusion and explicitly retaining all residual encoders. It does not establish hardness of restricted low-index ideal inputs, does not supply a distribution-changing map from standard worst-case ideal lattices, does not implement the paper's search-to-decision step for rings, and does not change a uniform secret into binary bits. Those are separate missing edges. All new claims remain provisional pending full, primary-dependency, complexity and blind reviews.
