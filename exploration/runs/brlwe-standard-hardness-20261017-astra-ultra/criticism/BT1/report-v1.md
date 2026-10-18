# BT1 complete referee report v1

## Identity, frozen input, and procedural qualification

Reviewer: BT1, assigned theorem-only referee. The mathematical input was

    criticism/BT1/input/theorem-only-v1.md
    SHA256 6eda9e0b34f25f54372b19bfcdbd2cdbb30b92a9643039d063b45de8d685eb54

under the run directory

    /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra

The input hash was checked directly. The input was never altered.

**This report must be recorded as NON-BLIND.** I began with only the frozen theorem, the operational assignment and cap file, and the expressly permitted generic audit skill references. No project proof, summary, status ledger, package plan, other worker directory, or worker result was read. I did not call list_agents, spawn agents, initiate model sessions, run experiments, or change any service or goal. During primary-source retrieval, search unexpectedly returned mathematical excerpts from unpermitted external papers. The incident and exact tool-transcript locators are preserved in exposure-20261017T2024Z.md. I notified the coordinator without disclosing mathematical audit results. The coordinator instructed me to finish and freeze this non-blind report, and to stop source searching. I complied.

The coefficient-dual/Fourier/theta proof route was independently written in my first private checkpoint before the relevant external smoothing excerpts arrived. This chronology does not restore strict blind status. This report supplies an independently developed derivation, not a certification of the project's theorem or its blind-review gate.

No content-policy interruption occurred. Ordinary source-access failures were HTTP/access/cache failures, one unavailable local executable, and a local DNS failure.

## Assessment

The finite statistical-uniformity statement, its retained-latent product bound, both finite mask bounds, and the stated asymptotic conclusions follow under the natural interpretation of the frozen assumptions. I found no counterexample to these statements. The derivation below proves each claim without importing a smoothing theorem.

One notation clarification is necessary for the BBPS attribution: the norm in its denominator must be

\[
 M=\|u\|_{\infty,\mathrm{can}}=\max_i|\sigma_i(u)|.
\]

The mask norm is instead the maximum absolute coefficient. If the frozen theorem's unqualified \(\|u\|_\infty\) were intended to mean the coefficient maximum, its assertion about the primary family's exact width floor would be false. Section 10 gives a finite example. No extra algebraic assumption beyond the frozen power-of-two setting is needed for the main estimate.

This is a referee derivation and a scope/notation assessment, not a self-issued final ACCEPT. The coordinator must reconcile it with the current proof and the replacement blind review.

## 1. Definitions and exact laws used

Write \(C:K_{\mathbb R}\to\mathbb R^n\) for the coefficient map in the basis \(1,X,\ldots,X^{n-1}\). Identify \(R\) with \(\mathbb Z^n\) through \(C\), but distinguish this Euclidean space from canonical \(H\). Complex conjugation on \(K\) is denoted \(x\mapsto\bar x\); it sends \(X\) to \(X^{-1}=-X^{n-1}\). It is an orthogonal signed permutation in coefficient coordinates.

The real inner product on \(H\) is

\[
 \langle z,w\rangle_H=\sum_{i=1}^n z_i\overline{w_i};
\]

the sum is real on the conjugate-paired subspace. All \(n\) embeddings are included. For real coefficient vectors \(x,y\),

\[
 \langle \sigma(x),\sigma(y)\rangle_H
 =n\langle C(x),C(y)\rangle.
 \tag{1}
\]

Thus the coefficient-to-canonical Jacobian is \(n^{n/2}\).

For each latent value \(\lambda\), the centered canonical Gaussian has normalized density, with respect to Euclidean volume on \(H\),

\[
 \phi_\lambda(z)=
 \frac{1}{\prod_{i=1}^n r_i(\lambda)}
 \exp\!\left(-\pi\sum_{i=1}^n\frac{|z_i|^2}{r_i(\lambda)^2}\right).
 \tag{2}
\]

This normalization uses the paired-width condition. In each conjugate pair, the real orthonormal coordinates are \((z_i+\bar z_i)/\sqrt2\) and \((z_i-\bar z_i)/(i\sqrt2)\); both have width \(r_i\). Accordingly, a pair contributes \(r_i^2\) to the normalizing product.

Let \(X_\lambda=nq\,C(e)\), and let \(g_\lambda\) denote its density on coefficient space. Then

\[
 g_\lambda(x)=
 \frac{1}{n^{n/2}q^n\prod_i r_i(\lambda)}
 \exp\!\left(
 -\frac{\pi}{n^2q^2}
 \sum_i\frac{|\sigma_i(C^{-1}x)|^2}{r_i(\lambda)^2}
 \right).
 \tag{3}
\]

Let \(G=R/qR\), \(J=P/qR\), \(h=|J|\), and \(B=[-1/2,1/2)^n\). Choose arbitrary integral representatives of \(G,J\). With \(\nu\) the law of \(\Lambda\), define

\[
 p_\lambda(a)=\frac1h\sum_{v\in J}\sum_{z\in\mathbb Z^n}
 \int_B g_\lambda(C(a-v)+qz+t)\,dt.
 \tag{4}
\]

The fixed rounding tie convention does not change (4): all Gaussian and Haar laws involved assign zero probability to rounding hyperplanes. The **full joint law**, including its shared latent variable, is exactly

\[
 \Pr[\Lambda\in D,\ A_1=a_1,\ldots,A_k=a_k]
 =\int_D\prod_{j=1}^k p_\lambda(a_j)\,\nu(d\lambda).
 \tag{5}
\]

The comparison law replaces every \(p_\lambda(a_j)\) by \(q^{-n}\), leaving \(\nu\) unchanged. Conditional independence in (5) comes from the stated conditional independence of the errors and the independently sampled uniform ideal points. No factorization after integrating \(\lambda\) is used.

As customary for a prescription by conditional distributions, the widths and the resulting probability kernels are assumed measurable. Since the outputs \(A_j\) lie in finite sets, the subsequent retained-latent total-variation calculations do not require any additional regular-conditional-probability theorem for an arbitrary latent state space.

## 2. Coefficient, trace, and canonical duals

The norm and inner-product identity (1) follows directly by summing powers of the \(n\) distinct roots of \(X^n+1\). For exponents \(a,b\in\{0,\ldots,n-1\}\), the embedding sum of \(X^a\overline{X^b}\) is \(n\) if \(a=b\) and zero otherwise.

For \(x,y\in K\), constant-coefficient extraction gives

\[
 [1](x\bar y)=\langle C(x),C(y)\rangle,
 \qquad
 \operatorname{Tr}_{K/\mathbb Q}(xy)=n[1](xy).
 \tag{6}
\]

I use \(P^{-1}=\{y\in K:yP\subseteq R\}\). The coefficient dual is exactly

\[
 P^*=\overline{P^{-1}}.
 \tag{7}
\]

Here is a direct proof which also fixes the conjugation. Since \(qR\subseteq P\), every vector in the coefficient dual has coefficients in \(q^{-1}\mathbb Z\), so it represents an element \(v\in K\). If \(\bar vP\subseteq R\), (6) shows \(\langle C(x),C(v)\rangle\in\mathbb Z\) for all \(x\in P\).

Conversely, suppose this integrality holds. For each \(x\in P\), all \(X^t x\) lie in \(P\). If \(x\bar v=\sum_{j=0}^{n-1}b_jX^j\), the \(t=0\) test yields \(b_0\in\mathbb Z\), and the \(t=n-j\) test yields \(-b_j\in\mathbb Z\) for each \(1\le j<n\). Thus \(x\bar v\in R\), proving (7).

The same proof applies to fractional full-rank \(R\)-ideals after clearing denominators. Euclidean lattice duality and the orthogonality of conjugation therefore imply

\[
 (P^{-1})^{-1}=P.
 \tag{8}
\]

Indeed (7) writes inversion as conjugation composed with coefficient duality; these operations commute and their squares are the identity.

The trace dual and canonical Euclidean dual are, respectively,

\[
 P^\vee=\frac1nP^{-1},
 \qquad
 \sigma(P)^*=\frac1n\sigma(P^*)
 =\frac1n\sigma(\overline{P^{-1}}).
 \tag{9}
\]

In particular, the canonical Euclidean dual is not obtained by silently identifying coefficient and canonical lattices.

Finally, \(u\in(qP^{-1})^{-1}\) gives \(quP^{-1}\subseteq R\), so (8) gives

\[
 qu\in P.
 \tag{10}
\]

Consequently, for every \(v\in P^*\),

\[
 z(v)=qu\bar v\in R.
 \tag{11}
\]

Because \(u\ne0\) and \(K\) is a field, \(v\mapsto z(v)\) is injective and sends nonzero vectors to nonzero vectors. This is the complete algebraic input to the theta estimate.

## 3. Gaussian characteristic function and the continuous torus law

For completeness, the normalized one-dimensional Gaussian of width \(s\) has characteristic function

\[
 \int_{\mathbb R}s^{-1}e^{-\pi x^2/s^2}e^{2\pi itx}\,dx
 =e^{-\pi s^2t^2}.
 \tag{12}
\]

This follows without contour arguments: the integral at \(t=0\) is one by the real Gaussian integral; differentiating and integrating by parts gives \(F'(t)=-2\pi s^2tF(t)\). Solving this differential equation gives (12). The Gaussian integral itself follows by squaring the integral and using polar coordinates.

Applying (12) in the real orthonormal paired basis gives, for \(\xi\in H\),

\[
 \mathbb E[e^{2\pi i\langle \xi,\sigma(e)\rangle_H}\mid\lambda]
 =\exp\!\left(-\pi\sum_i r_i(\lambda)^2|\xi_i|^2\right).
 \tag{13}
\]

For a coefficient frequency \(v\in K_{\mathbb R}\), identity (1) gives

\[
 \langle C(v),nq\,C(e)\rangle
 =q\langle\sigma(v),\sigma(e)\rangle_H.
\]

Therefore the coefficient-space characteristic function is

\[
 \mathbb E[e^{2\pi i\langle C(v),X_\lambda\rangle}\mid\lambda]
 =\exp\!\left(-\pi q^2\sum_i r_i(\lambda)^2|\sigma_i(v)|^2\right).
 \tag{14}
\]

The factor is \(q^2\), not \(nq^2\), when the sum is in canonical coordinates. The factor \(n\) reappears only after converting the norm of an integral element to coefficient coordinates.

Consider the coefficient torus

\[
 \mathcal T_q=\mathbb R^n/q\mathbb Z^n,
\]

with Haar probability measure \(dt/q^n\). Let \(Y_\lambda=U+X_\lambda\bmod q\mathbb Z^n\), where \(U\) is uniform on \(J\). Its density relative to Haar probability is

\[
 f_\lambda(t)=\frac{q^n}{h}
 \sum_{v\in J}\sum_{z\in\mathbb Z^n}
 g_\lambda(t-C(v)+qz).
 \tag{15}
\]

The character lattice of \(\mathcal T_q\) is \(q^{-1}\mathbb Z^n\), identified with \(q^{-1}R\). Finite-group character orthogonality gives, for a character frequency \(v\in q^{-1}R\),

\[
 \frac1h\sum_{w\in J}e^{2\pi i\langle C(v),C(w)\rangle}
 =\mathbf1_{\{v\in P^*\}}.
 \tag{16}
\]

The frequency annihilates \(J\) precisely when it pairs integrally with every element of \(P\). All elements of \(J\), including zero, occur in this averaging.

Equations (14)--(16) give the exact Fourier coefficients

\[
 \widehat f_\lambda(v)
 =\mathbf1_{\{v\in P^*\}}\,
 \exp\!\left(-\pi q^2\sum_i r_i(\lambda)^2|\sigma_i(v)|^2\right).
 \tag{17}
\]

These Fourier series converge absolutely for every positive width vector, because the quadratic form is positive definite and the character lattice is full rank. Thus all subsequent integrals, expansions, and Parseval identities are legitimate.

One optional explicit version of the rounded law (4) is

\[
 p_\lambda(a)=q^{-n}\sum_{v\in P^*}
 e^{-\pi q^2\sum_i r_i(\lambda)^2|\sigma_i(v)|^2}
 e^{2\pi i\langle C(v),C(a)\rangle}
 \prod_{\ell=0}^{n-1}\operatorname{sinc}(C(v)_\ell),
 \tag{18}
\]

where \(\operatorname{sinc}(t)=\sin(\pi t)/(\pi t)\) and \(\operatorname{sinc}(0)=1\). This cell-integral law is not a coefficient discrete Gaussian.

## 4. Theta bound and rounding

Parseval on the probability Haar space gives the exact identity

\[
 \|f_\lambda-1\|_{L^2(\mathcal T_q)}^2
 =\sum_{v\in P^*\setminus\{0\}}
 \exp\!\left(-2\pi q^2\sum_i
 r_i(\lambda)^2|\sigma_i(v)|^2\right).
 \tag{19}
\]

The width floor and (11) imply

\[
 q^2\sum_i r_i(\lambda)^2|\sigma_i(v)|^2
 \ge c^2\sum_i|\sigma_i(qu\bar v)|^2
 =nc^2\|C(z(v))\|_2^2.
 \tag{20}
\]

We used \(|\sigma_i(\bar v)|=|\sigma_i(v)|\), valid for complex conjugation in this cyclotomic field.

The injectivity in (11) allows us to enlarge the sum from its image to all nonzero integral coefficient vectors:

\[
\begin{aligned}
 \|f_\lambda-1\|_2^2
 &\le\sum_{z\in R\setminus\{0\}}
      e^{-2\pi nc^2\|C(z)\|_2^2}\\
 &=\left(\sum_{a\in\mathbb Z}e^{-2\pi nc^2a^2}\right)^n-1
 =\Theta_n(c).
\end{aligned}
 \tag{21}
\]

Since Haar measure has mass one, Cauchy--Schwarz and the convention \(\mathrm{TV}=\frac12\|\cdot\|_1\) yield

\[
 \mathrm{TV}(Y_\lambda,\mathrm{Haar}(\mathcal T_q))
 \le\frac12\sqrt{\Theta_n(c)}.
 \tag{22}
\]

Taking the minimum with one gives the stated \(\delta_n(c)\).

Coefficient rounding modulo \(q\) is an almost-everywhere well-defined measurable map from \(\mathcal T_q\) to \(G\). Its \(q^n\) output cells each have Euclidean volume one and hence Haar mass \(q^{-n}\). Thus it sends Haar to uniform \(G\). Integer translation equivariance away from ties gives

\[
 \operatorname{Round}(U+X_\lambda)
 =U+\operatorname{Round}(X_\lambda)
 \quad\text{almost surely}.
\]

Data processing of total variation proves

\[
 \mathrm{TV}(p_\lambda,\mathrm{Unif}(G))\le\delta_n(c)
 \tag{23}
\]

pointwise for every latent value satisfying the assumptions. A null exceptional set of latent values does not affect any joint-law conclusion.

## 5. Retaining the latent variable and public parameters

For probability measures \(p,h_0\) on a finite set, the tensor telescoping identity

\[
 p^{\otimes k}-h_0^{\otimes k}
 =\sum_{j=1}^k
 p^{\otimes(j-1)}\otimes(p-h_0)\otimes h_0^{\otimes(k-j)}
 \tag{24}
\]

and the triangle inequality give

\[
 \mathrm{TV}(p^{\otimes k},h_0^{\otimes k})
 \le k\,\mathrm{TV}(p,h_0).
 \tag{25}
\]

This is a signed-measure identity, not a multiplication of marginal event bounds.

Because both joint laws retain the same \(\nu\), and the output space \(G^k\) is finite, their total variation is exactly

\[
 \frac12\int\sum_{a\in G^k}
 \left|\prod_jp_\lambda(a_j)-q^{-nk}\right|\,\nu(d\lambda)
 =\int \mathrm{TV}(p_\lambda^{\otimes k},
 \mathrm{Unif}(G)^{\otimes k})\,\nu(d\lambda).
 \tag{26}
\]

Combining (23)--(26), followed by the universal upper bound one, proves

\[
 \mathrm{TV}((\Lambda,A_1,\ldots,A_k),
             (\Lambda,Z_1,\ldots,Z_k))
 \le \min(1,k\delta_n(c)).
 \tag{27}
\]

For additional public parameters \(W\), use the combined latent parameter \((\Lambda,W)\). This step is valid exactly when the complete hypotheses hold under that conditioning: the prescribed Gaussian kernels, conditional independence, independent uniform ideal points, the algebraic relations, and the same deterministic \(c\). Merely preserving a width inequality after revealing a statistic of the samples would not be enough.

No factorization of \(\int p_\lambda^{\otimes k}\nu(d\lambda)\) into independent marginal mixtures is claimed or needed.

## 6. Primary BBPS family and the asymptotic theta estimate

Primary-source verification used the permitted [BBPS proceedings PDF](https://iacr.org/archive/asiacrypt2019/119210284/119210284.pdf), Definitions 3.2 and 3.6 and Theorem 3.7, and the permitted [full-version Gaussian definitions](https://eprint.iacr.org/2018/494.pdf), Section 2.2.1, as returned by source search. Direct full-PDF retrieval failed; the Gaussian-definition search excerpt was available. The proceedings PDF was accessible at the no-www archive URL. The following source-dependent description is specialized to the totally imaginary field in the frozen theorem.

For each of the \(n/2\) conjugate pairs, independently draw \(X_i,Y_i\) from the real width-\(1/\sqrt2\) Gaussian. One latent draw determines

\[
 r_i^2=r_{i+n/2}^2
 =\frac{\alpha^2}{2}
 \left(X_i^2+Y_i^2+
       \frac{f(n)^2|\sigma_i(u)|^2}{M^2}\right),
 \qquad M=\max_i|\sigma_i(u)|.
 \tag{28}
\]

The selected Gaussian distribution is shared across samples; conditioned on it, the samples use independent errors. The source's Gaussian convention uses real orthonormal coordinates of width \(r_i\), which agrees with (2). Theorem 3.7 imposes \(\alpha\in(0,1)\) for its hardness reduction; that upper restriction is unnecessary for the present statistical calculation.

Equation (28) gives the deterministic floor

\[
 r_i\ge \frac{\alpha f(n)}{\sqrt2M}|\sigma_i(u)|.
 \tag{29}
\]

Here \(f(n)>0\) is understood at the dimensions under consideration, as in the Gaussian-family convention; asymptotically this follows from \(f(n)=\omega(\sqrt{\log n})\). Thus \(c=\alpha f(n)/(\sqrt2M)\) is the correct substitution. The latent variable may retain all \(X_i,Y_i\), or only their resulting width vector. Either retains the complete mixture law required by (5).

Here is a finite bound avoiding unstated theta asymptotics. Put

\[
 t=e^{-2\pi nc^2}.
\]

Since \(a^2\ge a\) for integers \(a\ge1\),

\[
 \sum_{a\in\mathbb Z}t^{a^2}
 \le1+\frac{2t}{1-t},
 \qquad
 \Theta_n(c)\le
 \exp\!\left(\frac{2nt}{1-t}\right)-1.
 \tag{30}
\]

If \(t\le1/2\) and \(4nt\le1\), then

\[
 \Theta_n(c)\le 8nt,
 \qquad
 \delta_n(c)\le\sqrt{2n}\,e^{-\pi nc^2}.
 \tag{31}
\]

Indeed \(2nt/(1-t)\le4nt\le1\), and \(e^x-1\le2x\) for \(0\le x\le1\).

Under \(\alpha/M\ge2w(n)\),

\[
 c^2\ge2w(n)^2f(n)^2,\qquad
 \delta_n(c)\le
 \sqrt{2n}\exp(-2\pi n w(n)^2f(n)^2)
 \tag{32}
\]

for all sufficiently large dimensions. The conditions of (31) hold eventually. If \(k(n)\le Cn^D\), then for every fixed \(B>0\), the right side of \(k\) times (32) is at most \(n^{-B}\) eventually. This proves negligibility along the allowed powers of two. No upper bound on \(q\) and no replacement by coefficient discrete Gaussians enters this argument.

## 7. Finite short-mask bounds

Let \(m=2\lfloor b\rfloor+1\), and let \(E_b\subseteq G\) be the image of the integer coefficient cube \([-\lfloor b\rfloor,\lfloor b\rfloor]^n\). Then

\[
 |E_b|\le m^n,\qquad
 |I+E_b|\le |I|\,|E_b|\le q^d m^n.
 \tag{33}
\]

The first inequality allows coefficient collisions modulo \(q\); the second allows collisions among translated cubes. Neither requires unique representations.

For independent uniform \(Z_j\),

\[
 \Pr[\forall j,\ Z_j\in I+E_b]
 =\left(\frac{|I+E_b|}{q^n}\right)^k
 \le\min\!\left(1,\left(\frac{q^dm^n}{q^n}\right)^k\right).
 \tag{34}
\]

This is the only event product in the fixed-ideal argument. It is taken under a declared product reference law, not under the actual latent mixture.

Apply the joint TV estimate once to the full event to obtain exactly

\[
 \Pr[\forall j,\ A_j\in I_T+E_b]
 \le
 \min\!\left(1,\left(\frac{q^dm^n}{q^n}\right)^k\right)
 +\Delta_k.
 \tag{35}
\]

If \(I_T\) is random and public, condition the reference probability on it; (34) is uniform in every dimension-\(d\) ideal. Retaining the public parameter in (27) validates the same bound.

For a completely split prime, \(G\simeq\mathbb F_q^n\) as a ring. Every ideal is a product of coordinate ideals \(0\) or \(\mathbb F_q\). Hence the number of dimension-\(d\) ideals is precisely \(\binom nd\), for integers \(0\le d\le n\).

The union over common ideals is formed under the reference law first:

\[
 \Pr[\exists\ I,\ \dim I=d,\ \forall j,\ Z_j\in I+E_b]
 \le
 \min\!\left(1,
 \binom nd\frac{q^{kd}m^{kn}}{q^{kn}}\right).
 \tag{36}
\]

Transferring this single union event by TV adds \(\Delta_k\) only once. This gives the frozen arbitrary-common-ideal bound. There is no multiplication of \(\Delta_k\) by the number of ideals.

The event in (35) is equivalent to existence of \(V_j\in I_T\) and bounded integral coefficient masks \(F_j\) representing \(A_j\). Dependence among these witnesses is irrelevant to this set membership. The analogous assertion for (36) requires one common ideal for all samples, exactly as stated.

## 8. Asymptotics of both mask bounds, including the rounding term

Put \(L_n=\log_2 n\). The frozen bound on \(b\) gives

\[
 \frac{m}{q}
 \le\frac{1}{L_n n^a}+\frac1q
 \le\frac1{L_n}+\frac1{n^2}.
 \tag{37}
\]

Thus, under \(q^d\le2^{\rho n}\), define

\[
 \beta_n=2^\rho\left(\frac1{L_n}+\frac1{n^2}\right)
 \quad\text{so that}\quad
 \frac{q^dm^n}{q^n}\le\beta_n^n.
 \tag{38}
\]

This accounts for the \(+1\) in the cardinality of the integer mask cube. It works even if \(b<1\) or \(a\) is large.

Since \(\rho\) is fixed, \(\beta_n\to0\). For a concrete sufficient threshold, both \(L_n\ge2^{\rho+3}\) and \(n^2\ge2^{\rho+3}\) imply \(\beta_n\le1/4\). For every \(k\ge1\), beyond this threshold,

\[
 \beta_n^{nk}\le4^{-n},\qquad
 \binom nd\beta_n^{nk}
 \le2^n4^{-nk}\le2^{-n}.
 \tag{39}
\]

Therefore both reference-law event bounds are negligible. The polynomial upper bound on \(k\) is needed for \(\Delta_k\), already proved negligible in Section 6. Together (35)--(39) prove the final asymptotic assertion. They also show that no assumption \(a>0\), no polynomial upper bound on \(q\), and no independence of representation witnesses is needed.

## 9. Exact hand controls and probability regressions

No computational experiments were run. The following checks are exact finite-support or exact algebraic hand calculations; no resource reservation was necessary.

### F1. Shared latent law does not give independent marginal samples

Let \(\Lambda\in\{+,-\}\) be uniform. Conditional on \(\Lambda\), take two independent Bernoulli outputs, with probability of zero \(3/4\) on \(+\) and \(1/4\) on \(-\). Each unconditional output is exactly uniform.

The unconditional probabilities of \(00,01,10,11\) are

\[
 5/16,\quad3/16,\quad3/16,\quad5/16.
\]

Their TV distance from uniform independent bits is \(1/8\), not zero. Conditional single-output TV is \(1/4\), while the joint TV retaining \(\Lambda\) is \(5/16\le2(1/4)\). This exactly checks the logic of (5), (25), and (26), and rejects the tempting replacement of a shared-latent mixture by independently resampled latent widths.

This Bernoulli model is a probability-kernel regression, not a counterexample purporting to satisfy Gaussian hypotheses.

### F2. Revealing an output is not free public-parameter retention

Take an exactly uniform bit \(A\), and publish \(W=A\). The law of \((W,A)\) has TV distance \(1/2\) from \((W,Z)\), where \(Z\) is an independent uniform bit. Thus retaining arbitrary output-derived information cannot follow merely from uniformity of the unconditioned output. The frozen theorem's requirement that all hypotheses continue to hold conditionally is essential and excludes this invalid inference.

### F3. Exact common-ideal counting at \(n=2,q=5,b=0,d=1\)

Here \(X^2+1=(X-2)(X+2)\) modulo 5. There are two dimension-one ideals, each containing 5 elements, and they intersect only at zero.

For \(k=2\), one fixed ideal contains \(25\) of the \(625\) ordered output pairs, giving probability \(1/25\), exactly the fixed-ideal reference bound.

The union over the two common ideals contains \(25+25-1=49\) pairs. Its probability is \(49/625\), below the bound \(50/625\) in (36). Allowing each sample to choose its own ideal instead would give \(9^2/625=81/625\); this is a different event and confirms why the word common matters.

For \(d=0\), there is one ideal, the zero ideal. For \(d=n\), the ideal is all of \(G\) and the event has probability one. The minima with one correctly handle this endpoint and masks that cover all residues.

### F4. Fourier normalization and algebraic endpoints

If \(P=R\), then \(U\) is uniform on all of \(G\), so the published output is exactly uniform for every error law independent of \(U\). The rounding proof reflects this: \(P^*=R\), and every nonzero integral frequency in (18) has a zero sinc factor.

If \(P=qR\), then \(U=0\), \(Q=R\), and \(u=1\) is allowed. For an isotropic width \(r_i=c\), one has \(P^*=q^{-1}R\). The character associated with \(v=m/q\) has coefficient

\[
 e^{-\pi nc^2\|m\|_2^2}.
\]

Thus the continuous-torus sum in (19) is exactly \(\Theta_n(c)\). This checks the factor \(n\), the squared Fourier exponent \(2\pi\), and the scale \(nq\).

For a simple finite check of (16), take \(n=2,q=2,P=R\). Averaging any nontrivial character over all four elements gives zero. Averaging over the three nonzero elements instead gives \(-1/3\). The stated uniform law including zero is exactly the law used by the character cancellation.

### CP-1. Cached-prefix branch inflation

I reproduced the prescribed generic regression by hand. Before conditioning, the trace probabilities are \(21/2200\) for each \(A_b\), \(1/11\) for each \(C_b\), and \(879/1100\) for \(D\). The probability of the selected public key is

\[
 2(21/2200)+2(1/11)(1/2)+879/1100=10/11.
\]

After conditioning, the masses are \(21/2000\), \(1/20\), and \(879/1000\), respectively. Initial incidences are \(p(x)=1/10\), \(p(e_b)=121/2000=0.0605\), and \(p(f_b)=21/2000=0.0105\), so none exceeds the strict threshold \(\gamma=1/10\).

The two-position matching event has probability

\[
 2\cdot\frac{21}{2000}\cdot\frac12
 =\frac{21}{2000}
 >\frac1{100}.
\]

After exposing \(H(x)=b\), the relevant incidence of \(e_b\) becomes \(221/2000=0.1105\), rather than \(0.0605\). After the first selected hit, the surviving \(f_b\) incidence is \(21/221<1/10\). Support restriction and Bayes normalization, not merely lack of fresh-oracle independence, explain the failed marginal product.

The current proof does not make that inference. Its tensor estimate is the exact algebraic identity (24) under a fixed latent kernel. Its event powers occur only for fresh independent uniform reference variables, conditioned on any fixed public ideal. Under that reference filtration, for a fixed ideal \(I\), every history has

\[
 \Pr[Z_j\in I+E_b\mid Z_1,\ldots,Z_{j-1},I]
 =|I+E_b|/q^n.
\]

The common-ideal union is taken after these fixed-ideal products. There is no adaptive branch selection or cache-hit event entering the product argument. CP-1 therefore rejects the bad marginal-product rule while leaving the actual argument intact.

## 10. Precise qualifications, norm ambiguity, and scope

The substantive notation issue is the two uses of infinity norm. For example, in \(K=\mathbb Q(i)\), let \(u=(1+X)/q\), \(P=R\), and \(Q=qR\). Then

\[
 \|C(u)\|_\infty=1/q,\qquad
 \|\sigma(u)\|_\infty=\sqrt2/q.
\]

The actual family in (28) has limiting width floor \(\alpha f/\sqrt2\) as its pair of latent real coordinates tends to zero. Substituting the coefficient infinity norm into the frozen claimed BBPS floor would instead assert \(\alpha f\). That stronger floor fails on a positive-probability neighborhood of the latent origin. Explicitly defining the denominator as the canonical infinity norm removes this ambiguity. It does not change any part of the proof above.

The following natural conventions should be written explicitly if a completely formal standalone version is wanted:

- \(k\) is a finite nonnegative integer in the main bound, and \(k\ge1\) in the final asymptotic statement.
- The Gaussian widths are positive and measurable. The phrase independently draw \(U_j\) means independence from both the errors and the latent variable, as well as from each other.
- The term split prime is read as completely split in the CRT counting explanation; the given power-of-two cyclotomic setting then has \(n\) distinct linear factors modulo \(q\).
- The BBPS denominator uses canonical infinity norm; the mask norm uses coefficient infinity norm.
- Negligible means smaller than every inverse fixed polynomial in \(n\), along the prescribed powers of two. All asymptotic parameter inequalities hold eventually with fixed \(\rho,a\), and \(k\) has one fixed polynomial upper bound.

The bounds concern membership in the specified short-mask sumsets, with either the same fixed ideal or one common ideal. They do not establish an algorithm for the original RLWE problem and do not exclude transformations whose output distribution or representation condition lies outside these events.

## 11. Reproducibility and final procedural record

All mathematical finite controls in this report are exact hand calculations. The only executed local commands read authorized inputs, recorded owned checkpoints/exposure/report artifacts, attempted primary-source retrieval, or computed file metadata. No experimental process, package installation, external model session, detached job, or service mutation occurred.

The main source-specific assertions were checked against the permitted BBPS definitions. Search engines additionally exposed unpermitted snippets; these were reported and the blind gate is explicitly forfeited. No external snippet is needed as a premise for Sections 1--5 or 7--10.

The complete report is to be frozen and SHA256-hashed before its path/hash are sent to the coordinator. The freeze receipt records the actual UTC freeze time, this complete report's digest, the verified input digest, the exposure qualification, and the fact that no substantive audit result was disclosed before freezing.
