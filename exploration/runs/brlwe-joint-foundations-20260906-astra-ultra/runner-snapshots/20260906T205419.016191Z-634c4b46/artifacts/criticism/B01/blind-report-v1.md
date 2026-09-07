# B01-v1 blind mathematical report

Reviewed packet: **B01-M1**, `model-v1.md`, SHA-256
`df279e6d964d0ca6051232aa6b086e80582ce241e9000bb8e5d215139a3142af`.

Reviewer canonical agent: `/root/b01_blind`.
Observed nonsecret environment metadata: `CODEX_THREAD_ID=01a07863-0c67-75f1-8d4e-b893c7cd87db`; `CODEX_SESSION_ID=01a07849-2b26-7ac1-96c2-c15903ac2341`.
These are observed values, not UUIDs inferred from names. The assigned model was gpt-6-astra with ultra reasoning.

This report was derived from the frozen packet, its supplied hash manifest, `inputs/RESEARCH_SCOPE.md`, and the mathematical-proof-audit skill and its two permitted methodology references. No proposed proof, earlier verdict, coordinator scientific assessment, other criticism, worker output, or other project scientific file was read. No public literature result is imported: the algebraic estimate needed below is proved here. The complete assignment is preserved in `assignment.md`, and input hashes are in `your-input-hashes.json`. No external worker, agent, package installation, service, goal tool, or network experiment was used. No content-policy interruption occurred during this assignment.

## 1. Claim-addressed disposition

| Exact statement | Blind disposition | Dependency footprint |
|---|---|---|
| A1, literal B01-M1 independence premises | **Refuted:** the premises do not explicitly impose joint independence of the source tuple, S and E. An exact F3 witness has all three stated error terms zero and TV(P,Q)=2/9. | Literal finite law only; Section 2 and `counterexample-data.json`. |
| A2, same literal premises | **Refuted by the same witness:** the source challenge is exactly uniform, while a public target test has advantage 2/9. | Same witness; no computational assumption. |
| A1 and A2 with explicit independent secret/noise generation | Complete independent proof and explicit tests are supplied below. This is a sufficient repair, not an assumption silently added to B01-M1. Under the audit protocol it remains a repair requiring fresh review. | Joint independence repair; two stated TV premises; finite-group pushforwards; Sections 3–4. |
| B1 as stated | **Proved:** an explicit finite deterministic public test witnesses at least eta_iso−2 delta_E. Its supplied implementation is exponential, and no polynomial-time conclusion follows from this proof. | Cyclotomic norm estimate and the two strict gates; explicit independence in statement B; Section 5. B1 does not depend on A1/A2. |
| Shared asymptotic parameter substitution | For fixed c>1/2, the lower bound on q certifies the finite gates eventually; c=1,K=16 qualifies along the stated qualifying primes. The including-zero eta_iso is nonnegligible for every fixed K, whereas delta_E is negligible. | Section 6; no unproved extraction or convolution theorem is assumed. |

There is a possible intended reading of the phrase “fixed public laws”: if it was meant to specify fresh independent draws of S and E, the repaired A proofs below apply directly to that intended reading. The literal probability premises, however, only state independence of E from earlier source variables and independence of S,G from each other and the source tuple. Those conditions do not imply the needed joint law. The distinction changes the truth value, so the frozen statement needs to make the intended independence explicit.

## 2. Exact literal counterexample to A1 and A2

Take R=F3, J=0, I=R, and U=1. Draw F,V,S,G,H independently uniformly in F3, and set E=−S. Draw S0,E0 as the required fresh independent uniform copies, independent of every source variable.

Every literal independence premise is satisfied:

* E is uniform and independent of J,U,F,V, the variables preceding E in the packet.
* S and G are mutually independent, and their pair is independent of J,U,F.
* H is a valid fixed kernel given J,U,F: it is fresh uniform noise with coins independent of S,G.
* V has its required conditional uniform law and independence from U,F.

Conditional on F=f, fG+H is uniform. Consequently the first stated TV is exactly zero. Because G is uniform, Y=S+G is uniform and independent of S. It is also independent of F,H. Thus the second stated TV is exactly zero. Multiplication by U=1 is a bijection R/J→I, so eta_iso=0.

Writing a=1+F gives

\[
P=(a,aS+E)=(a,(a-1)S).
\]

Here a is uniform and independent of the pair (S,E), exactly as required of the target's a. For a≠1, the second coordinate is uniform; for a=1, it is identically zero. In contrast, Q is uniform in R² because its independent V summand is uniform.

The deterministic public test

\[
D(a,c)=\mathbf 1\{a=1\text{ and }c=0\}
\]

accepts P and the target with probability 1/3 and a uniform pair with probability 1/9. Therefore TV(P,Q)=Adv_target(D)=2/9. The source challenge (1+F,V+E0) is exactly a uniform pair. **Every** public source test has advantage zero, regardless of its resources or access to public samplers. This contradicts both A1 and A2 with zero right-hand error.

An additional control shows that merely adding unconditional S⊥E is insufficient for A1. Take F,S independent uniform F3 and E=S+F, leaving U=1 and V,G,H fresh uniform. Each of (F,S), (F,E), and (S,E) is uniform on F3², but the triple is not mutually independent. Both stated TV premises are again zero, yet

\[
(U+F)S+E=(F+2)S+F
\]

is deterministic when F=1, and TV(P,Q)=2/9. The sufficient repair must specify the joint law with the source tuple, not just pairwise independence. This second control concerns A1; its target law with a fresh independent a is uniform, so it is not claimed as a second counterexample to A2.

## 3. A1 under the precise independence repair

Let K=(J,U,F). Add the explicit requirement

\[
\mathcal L(K,S,E)=\mu_K\otimes P_S\otimes P_E.
\tag{A-Ind}
\]

Continue to read the packet's S,G independence as joint independence of K from the mutually independent pair S,G, and retain the stated conditional kernel law for H. No independence between the original V and S,G,H is needed for the proof: a fresh V′ with law uniform I conditional J can be introduced, and its joint law with K agrees with the V used by Q. In Q the copies S0,E0 are already independent of source variables.

### 3.1 Conditional laws and projection

For a positive-mass value K=k=(j,u,f), H is independent of the pair S,G and is sampled from its specified kernel H_k. For any h,y with positive conditioning probability,

\[
\Pr[S=s\mid K=k,H=h,Y=y]
=\frac{P_S(s)P_G(y-s)}{P_Y(y)}.
\]

The posterior of pi_j(S) is obtained by summing this expression over s in the relevant coset. The extraction premise compares that entire retained joint law with one in which Z is uniform in Q_j and independent of K,H,Y conditional J. It does not state that original S remains an additional observation.

The map

\[
m_u:R/j\longrightarrow I,\qquad m_u(r+j)=ur
\]

is well defined because uj=0. Its image is uR. A uniform input Z pushes forward to the uniform law on uR: all fibers of this homomorphism have the same cardinality. Therefore

\[
\operatorname{TV}(m_u(Z),\operatorname{Unif}(I))
=1-\frac{|uR|}{|I|}.
\]

This needs neither injectivity nor |R/j|=|I|. Surjectivity uR=I suffices for zero loss. A bijection is one sufficient special case. Zero-probability conditioning branches are not assigned posteriors and contribute nothing to any expectation.

### 3.2 The four comparison steps

Set A=U+F and introduce V′ uniform I conditional J, independent of K,S,G,H beyond that dependence on J. Consider the following public output laws, with hidden variables used only in the proof:

\[
\begin{aligned}
L_0&=(A,AS+E),\\
L_1&=(A,AS+FG+H)=(A,US+FY+H),\\
L_2&=(A,m_U(Z)+FY+H),\\
L_3&=(A,V'+FY+H),\\
L_4&=(A,V'+FS+E'),
\end{aligned}
\]

where E′ is a fresh P_E draw independent of the displayed source variables.

1. The first noise comparison can be extended by the independent S under (A-Ind), then pushed forward to (A,AS+noise). Thus TV(L0,L1)≤eta_N. H is integrated out at this step. This is exactly the step invalidated by Section 2 without (A-Ind).
2. Apply the stated extraction comparison and the map (K,H,Y,z)↦(A,m_U(z)+FY+H). It follows that TV(L1,L2)≤eta_X. At this step original S has been projected to pi_J(S) and is then discarded. H,Y remain in the proof filtration throughout this comparison.
3. Conditional on each positive-mass K,H,Y, replace uniform UR by independent uniform I. The exact conditional distance is 1−|UR|/|I|. Averaging gives TV(L2,L3)≤eta_iso.
4. Rewrite the second coordinate of L3 as V′+FS+(FG+H). The pair S,V′ can be attached to the noise comparison by a common conditional kernel: S is independent of K,G,H, while V′ is fresh conditional J. Pushing forward gives TV(L3,L4)≤eta_N. Only after this comparison are H and the auxiliary G discarded. L4 is Q by the fresh-copy definitions.

Triangle inequality and TV≤1 prove exactly

\[
\operatorname{TV}(P,Q)\le\min\{1,2\eta_N+\eta_X+\eta_{\rm iso}\}
\]

under (A-Ind). No efficient sampling of H is used in the argument.

### 3.3 Required boundary controls

* **U=0:** UR={0}; the correct conditional loss is 1−1/|I|. It is zero when I={0}. There is no division by U and no omitted zero-rank branch.
* **A bijection Q_J→I:** the image is all I, so the loss is zero. The proof also handles a surjection with a nontrivial kernel.
* **J=R in a unital ring:** I={0}, Q_J is a singleton, U=V=0, and the repaired P,Q are identical fresh secret/noise laws conditional the source tuple.
* **Original S retained:** take F3, J=0,U=1,F=H=E=0, S uniform {0,1}, and G uniform F3. Then Y is independent of S and
  TV((Y,S),(Y,Z))=1/3. But
  TV((S,Y,S),(S,Y,Z))=2/3. Equivalently, adding original S to the public P,Q observations changes their distance from 1/3 to 2/3 while eta_N=eta_iso=0. The stronger retained-S conclusion is false under the stated eta_X premise. Discarding S is essential to this comparison.

## 4. Repaired A2: explicit public tests and finite implementation errors

Use names T1,T2 here to avoid confusing the first test with ring statement B1. Given a source challenge pair (a,c), define

\[
\begin{aligned}
T_1(a,c):&\quad s\leftarrow P_S,\ e\leftarrow P_E
\text{ independently};\quad\text{return }D(a,as+e),\\
T_2(a,c):&\quad s\leftarrow P_S;\quad\text{return }D(a,c+as).
\end{aligned}
\]

All these draws are fresh and independent of the challenge. Each test invokes D exactly once. Neither test receives J,U,F,V,H, takes a secret as an input, nor samples H.

In source world 0, T1 feeds D the repaired P law. T2 feeds D

\[
(U+F,V+E0+(U+F)s).
\]

Conditional on J,U,F,s,E0, the term Us belongs to I and V+Us is uniform I, with the same law for every such conditioning value. Therefore this is exactly Q. This verifies the joint law: it is not merely a marginal assertion about V+Us.

In source world 1, T1 feeds D the independently sampled target law. T2 feeds D a uniform pair, since adding as to an independent uniform c preserves uniformity even after conditioning on a,s. Consequently, writing epsilon_A=2eta_N+eta_X+eta_iso,

\[
\begin{aligned}
\operatorname{Adv}_{\rm target}(D)
&\le |\mathbb E D(\mathrm{target})-\mathbb E D(P)|
 +|\mathbb E D(P)-\mathbb E D(Q)|
 +|\mathbb E D(Q)-\mathbb E D(\mathrm{uniform})|\\
&\le \operatorname{Adv}_{\rm source}(T_1)
 +\operatorname{Adv}_{\rm source}(T_2)+\epsilon_A.
\end{aligned}
\]

If one invocation of D costs T_D, a P_S draw costs T_S, a P_E draw costs T_E, and one multiplication/addition costs T_mul/T_add, then T1 costs at most T_D+T_S+T_E+T_mul+T_add plus ordinary input/coin handling; T2 costs at most T_D+T_S+T_mul+T_add. The tests are polynomial if these component operations are polynomial. A fixed mathematical law alone need not have an effective exact sampler; this is an oracle construction unless an implementation and cost are specified.

For finite sampler implementations, suppose T1 uses independent approximations with TV errors epsilon_S,1 and epsilon_E,1, and T2's secret approximation has error epsilon_S,2. Put delta_1=min(1,epsilon_S,1+epsilon_E,1) and delta_2=epsilon_S,2. Under exact ring arithmetic and the exact challenge laws, the implemented tests satisfy

\[
\operatorname{Adv}_{\rm target}(D)
\le\operatorname{Adv}_{\rm source}(\widetilde T_1)
 +\operatorname{Adv}_{\rm source}(\widetilde T_2)
 +\epsilon_A+2\delta_1+\delta_2.
\]

T1 can move both challenge-world acceptance probabilities by at most delta_1. T2's source-world probability moves by at most delta_2, while its uniform-world output remains **exactly** uniform for every approximate secret law. With a common secret error epsilon_S and noise error epsilon_E this gives the simple extra loss 3epsilon_S+2epsilon_E. A generic bound 2(delta_1+delta_2) is valid if one does not use that sharper uniform-world observation. Further approximations to the two challenge laws must be charged separately; there is no H-sampling implementation loss in either test.

## 5. Proof of finite statement B1

Statement B explicitly makes E independent of all other variables, so the literal A objection does not affect this section. Its F distribution may be arbitrary within the specified coefficient cube.

### 5.1 Elementary norm estimate

For an integer coefficient vector w of degree less than n, define supp_q(w) to be the CRT coordinates at which its reduction modulo q is nonzero. If w is nonzero as an integer vector and |supp_q(w)|≤k, then

\[
\|w\|_2\ge q^{1-k/n}.
\tag{N}
\]

To prove this, X^n+1 is irreducible over Q for n a power of two: after replacing X by X+1, Eisenstein at 2 applies. The intermediate binomial coefficients are even, the constant coefficient is 2 and not divisible by 4, and the leading coefficient is 1. Thus multiplication by any nonzero w in Q[X]/(X^n+1) has a nonzero integer determinant N(w).

Modulo q, CRT diagonalizes multiplication by w, so its rank is at most k. A rank deficiency n−k over F_q implies q^(n−k) divides the integer determinant: integer row operations invertible modulo q can put n−k rows into multiples of q, and expanding the determinant gives the divisibility. Hence |N(w)|≥q^(n−k).

Let zeta_i be the n complex roots of X^n+1. Orthogonality gives

\[
\sum_i|w(\zeta_i)|^2=n\|w\|_2^2.
\]

The determinant is the product of w(zeta_i). Applying arithmetic–geometric mean to their squared magnitudes yields |N(w)|≤||w||_2^n. Combining the two inequalities proves (N). This also covers a nonzero integer vector that reduces to zero modulo q, for which k=0.

### 5.2 Deterministic public test

The test receives only the public pair (a,c) and the public n,q,d,b,R0 and CRT roots.

1. Enumerate integer coefficient vectors f in [-b,b]^n. Keep those for which a−f has at most d nonzero CRT coordinates. If none exists, reject. Under the strict first norm gate there is at most one; call it f* and put u*=a−f*, W=supp_q(u*).
2. Accept if and only if there exists an integer coefficient vector h in [-B0,B0]^n such that supp_q(c−h) is a subset of W.

Both P and Q have a stage-one candidate, namely their actual F. If f,f′ were distinct candidates, w=f−f′ would be a nonzero integer vector with CRT support at most 2d and ||w||_2≤2b sqrt(n). Estimate (N) and the strict first gate contradict this. Thus f*=F and u*=U on both laws. This recovers U and its actual nonzero support W; it does **not** purport to recover hidden T when U has zero coordinates.

### 5.3 Exact good-noise conditional behavior

Let Good be the event that the integer E (or E0 in Q) lies in [-R0,R0]^n. Its probability is 1−delta_E. Every coefficient of the integer negacyclic product FS or FS0 has absolute value at most nb, because each output coefficient is a signed sum of n terms of magnitude at most b. Thus on Good, h0=FS+E or h0=FS0+E0 lies in [-B0,B0]^n before reduction modulo q.

For P, c−h0=US has support contained in W, so the test accepts on every Good outcome.

For Q, c=V+h0. If the test accepts using some h, put v′=c−h, whose support is contained in W⊆T. The integer vector w=h−h0 satisfies w modulo q=V−v′, with CRT support at most d. If w were nonzero, then

\[
q^{1-d/n}\le\|w\|_2\le 2B0\sqrt n,
\]

contradicting the strict second gate. Therefore h=h0 and V=v′ is supported on W. Conversely, if V is supported on W, h0 is an accepting witness. Hence on every positive-mass Good branch of J,U,F,S0,E0,

\[
\text{Q accepts}\quad\Longleftrightarrow\quad V\in I_W=UR.
\tag{B-good}
\]

If |W|=k, conditional T,U the probability is exactly q^(k−d). This includes U=0,k=0, where the probability is q^(−d), and full support k=d, where the probability is one. No rank branch is conditioned away.

### 5.4 Averaging and statistical gap

Conditional on T, the d pairs of CRT coordinates (U_i,V_i) are mutually independent uniform F_q² pairs. A coordinate causes no obstruction if U_i≠0 or V_i=0. Its probability is

\[
(1-1/q)+(1/q)(1/q)=1-1/q+1/q^2.
\]

This is a product of explicitly independent coordinates conditional on T, not an inferred product of marginal bounds after adaptive conditioning. Therefore

\[
r:=\Pr[V\in UR]=(1-1/q+1/q^2)^d,
\qquad 1-r=\eta_{\rm iso}.
\]

The acceptance probabilities obey Pr_P[accept]≥1−delta_E and Pr_Q[accept]≤r+delta_E. Their signed difference is at least eta_iso−2delta_E. TV is at least that difference and at least zero, proving precisely B1.

The independence of Good from T,U,V gives a slightly stronger optional bound: on Good the Q acceptance probability is exactly (1−delta_E)r, so Pr_Q[accept]≤(1−delta_E)r+delta_E. Thus the signed gap is at least eta_iso−delta_E(1+eta_iso). The claimed weaker bound does not need this improvement.

### 5.5 Resource class and boundaries

Straight enumeration takes

\[
O\!\left(((2b+1)^n+(2B0+1)^n)\,
\operatorname{poly}(n,\log q,\log(B0+1))\right)
\]

bit operations using naive CRT evaluation and exact integer/modular arithmetic. Candidates can be streamed, so polynomial working space suffices. In the shared asymptotic parameters, the second enumeration is exp(O(n log n)); this supplied test is not polynomial time. The report does not prove that every possible witness needs exponential time or that a different polynomial algorithm cannot exist. Its conclusion is finite deterministic statistical distinguishability.

For n=4,q=97,d=1,b=1,R0=0,F=0 and the deliberately modified E=0 law, the first gate is sqrt(97)>4 and the second is 97^(3/4)>16. Exact enumeration gives

\[
\Pr_P[\mathrm{accept}]=1,\quad
\Pr_Q[\mathrm{accept}]=9313/9409,\quad
\eta_{\rm iso}=96/9409.
\]

The full TV is 7872/9409, much larger than the guaranteed witness gap; B1 is a lower bound, not an asserted equality for binary S. The computation explicitly includes U=0,V=0 and U=0,V≠0 branches.

**Strictness and equality.** The proof invokes strict inequalities to contradict (N). In the packet's exact integer regime, however, equality in either displayed norm gate is impossible. Equality in the first would imply

\[
q^{n-2d}=(2b)^n n^{n/2}.
\]

The equality would force n−2d>0, and then its left side is odd while its right side is even. Equality in the second would imply

\[
q^{n-d}=(2B0)^n n^{n/2},
\]

again impossible by parity, since B0≥nb>0. Thus replacing `>` by `>=` does not actually add an equality case under these integer assumptions. If the norm envelopes are generalized so equality becomes attainable, (N) need not be strict: for n=2,q=5,w=1+2X, the CRT support has size one and ||w||_2=sqrt(5)=q^(1−1/2). No claim about such generalized equality cases is inherited automatically.

A negative control for omitting the first gate uses n=4,q=17,d=1,b=2: w=1+4X² has CRT support two and can be the difference of two allowed small f vectors. Splitting its two nonzero CRT coordinates between two rank-one U candidates gives a genuine first-stage decomposition ambiguity. This control violates the gate and is not a counterexample to B1 with its gates.

## 6. Shared asymptotic model

Write ell=log2 n, since n is a power of two, and let L_q=2n^(1+c)ell³ denote the stated lower bound on q. Eventually d=floor(sqrt(n)/ell⁴) is positive and d/n tends to zero. Also b=ell², sigma=2n ell³ and

\[
R0=\sigma\ell=2n\ell^4,\qquad
B0=n\ell^2+2n\ell^4.
\]

For fixed c, L_q^(−d/n)=1−o(1). Substitution of the lower endpoint gives

\[
\frac{L_q^{1-2d/n}}{2b\sqrt n}
=(1-o(1))n^{c+1/2}\ell,
\]

and

\[
\frac{L_q^{1-d/n}}{2B0\sqrt n}
=(1-o(1))\frac{n^{c-1/2}\ell}{1+2\ell^2}
\sim\frac{n^{c-1/2}}{2\ell}.
\]

Both relevant exponents of q are positive eventually, so the inequalities are monotone in q. For the packet's c>0 the first gate and 2b<q follow eventually. The second follows from the stated lower bound alone for **c>1/2**. At c=1/2 the lower endpoint misses a factor of order ell, and for 0<c<1/2 it misses a polynomial factor as well. Larger qualifying primes can still satisfy the gate in those ranges; the assertion is about what direct substitution of the given lower bound certifies, not an unproved assertion about primes in short arithmetic-progression intervals.

The explicit c=1,K=16 regime therefore satisfies all finite gates eventually along its qualifying primes. Existence of an eventual nonempty interval sigma n^c≤q≤n^K requires K>1+c; no prime-existence theorem is proved or needed beyond the packet's qualifying-prime condition.

For completeness, the stated Gaussian tail is elementary here. For sigma≥2, the normalization of the one-dimensional D_sigma law is at least sigma−1≥sigma/2 by comparison with the integral of the decreasing positive half-Gaussian. Since R0≥sigma ell,

\[
2\sum_{k>R0}e^{-\pi k^2/\sigma^2}
\le 2\int_{R0}^{\infty}e^{-\pi x^2/\sigma^2}dx
\le\frac{\sigma}{\pi\ell}e^{-\pi\ell^2}.
\]

Dividing and taking a union bound over coordinates gives delta_E≤2n exp(−pi ell²), as asserted, for the sufficiently large parameters here. This is negligible in n.

Set p=(q−1)/q². Then

\[
\eta_{\rm iso}=1-(1-p)^d=\Theta(d/q).
\]

For example, for all sufficiently large parameters, dp≤1 and

\[
\frac{d}{4q}\le\eta_{\rm iso}\le\frac d q.
\]

Using the lower and upper bounds on q and the floor in d gives

\[
\frac{n^{1/2-K}}{8\ell^4}
\le\eta_{\rm iso}
\le\frac{n^{-c-1/2}}{2\ell^7}.
\]

Thus eta_iso is small but **not negligible** for fixed K. Eventually 2delta_E≤eta_iso/2, so the B1 lower bound remains inverse polynomial; one explicit consequence is eta_iso−2delta_E≥n^(1/2−K)/(16ell⁴). An additive A budget containing this eta_iso cannot be declared negligible even if eta_N and eta_X are negligible. Choosing K after seeing an adversary's advantage exponent would change the frozen quantifier order and does not establish a fixed-parameter negligible-error reduction.

If instead U has independent nonzero coordinates on every element of T, then W=T and UR=I_T always. The corresponding eta_iso is exactly zero, and the B1 witness above provides only the trivial zero lower bound. This convention is different from conditioning merely on U≠0 as a whole vector when d>1. The full latent-law distance between uniform including-zero U and U conditioned to have no zero T-coordinate is 1−(1−1/q)^d=Theta(d/q), so exchanging the conventions is not justified by a negligible latent statistical error under fixed K. No equality for the projected public-law distance is claimed.

Finally, the H_seq kernel is well defined in the displayed regime: ||M_F||_op≤||F||_1≤nb, hence

\[
\tau^2||M_F||_{\rm op}^2\le n^2\ell^6=\sigma^2/4,
\qquad B_F\succeq(3/4)\sigma^2\operatorname{Id}.
\]

Its rational LDL decomposition therefore has positive pivots. If y=L^(−1)h, its mass is exactly

\[
\frac{\exp(-\pi h^TB_F^{-1}h)}
 {\prod_i Z(v_i,c_i(h_{<i}))},\qquad
Z(v,c)=\sum_{z\in\mathbb Z}\exp(-\pi(z-c)^2/v).
\]

The factors in the denominator generally depend on the prefix. They cannot be replaced silently by one global normalizer to identify H_seq with multivariate D_B. This report proves neither the quantitative eta_N/eta_X bounds for this kernel nor a general extraction theorem. The asymptotic packet does not itself give numerical eta_N/eta_X estimates or an explicit asymptotic law for G. Under the nonzero-coordinate U convention, whether the remaining A budget is negligible is therefore unresolved here. No multiple-sample or tensorized conclusion is made; m=1 throughout.

## 7. Reproducible finite checks and their limits

Source: `finite_checks.py`. Each mode was run separately with `timeout 120s`, one experiment at a time, using installed Python 3 only. Arithmetic was exact integers and `fractions.Fraction`; there was no seed, stochastic sampling, numerical precision choice, Gaussian truncation, or approximation tail in these finite tests.

| Mode and data file | Exact scope | Result | Recorded wall time |
|---|---|---|---|
| `counterexample`, `counterexample-data.json` | Full F3 literal-law witness and retained-S boundary | eta_N=eta_X=eta_iso=0, TV(P,Q)=2/9, source TV=0; retained-S distances 1/3 versus 2/3 | 0.000486 s |
| `repaired_a`, `repaired-a-data.json` | 46,798 listed independent uniform-support models over Z/2,Z/3,Z/4; every ideal and allowable deterministic U,F branch in those models | No A1 violation; maximum TV minus budget is 0 | 2.396912 s |
| `a2`, `a2-data.json` | All 512 deterministic bit tests on F3² for a mixed-ideal source; both public-test pushforwards; pairwise-independence negative control | Both mapping TVs zero; all A2 inequalities pass; pairwise control has TV 2/9 | 0.012085 s |
| `ring_b`, `ring-b-data.json` | Full modified-noise n=4,q=97 P/Q laws; 625 first-stage difference vectors, 6,561 second-stage vectors and all 83,521 second-stage difference vectors; nine public-test rank representatives; norm/gate negative controls | Witness gap 96/9409; full TV 7872/9409; no prohibited short nonzero vectors in the checked gated cubes | 0.378706 s |

From the run directory, commands have the form:

```sh
timeout 120s python3 criticism/B01/finite_checks.py counterexample
timeout 120s python3 criticism/B01/finite_checks.py repaired_a
timeout 120s python3 criticism/B01/finite_checks.py a2
timeout 120s python3 criticism/B01/finite_checks.py ring_b
```

The independent A search exhausts its documented finite family, not all finite rings, all real probability laws, or all conditional source kernels. The A2 enumeration is one mixed source with all deterministic tests on its nine public points. The ring test uses the explicitly modified zero-noise boundary, not an approximation to D_sigma. These negative searches support the proofs; they are not substitutes for the unrestricted arguments. All found counterexamples are exact complete finite laws, not failed random searches.

## 8. Strongest limitations and remaining obligations

The decisive statement-level issue is the missing explicit joint independence in A. If the author intended independent sampler generation, the exact condition must be frozen and the supplied repaired proof freshly checked; a reviewer should not repair it silently. Even under that repair, this report treats eta_N and eta_X as the stated hypotheses and does not certify an asymptotic instantiation of them.

B1 is a statistical lower bound with an explicit exponential public witness. It supplies no polynomial distinguisher, no computational hardness theorem, no information about m>1, and no tensorization. The nonnegligible including-zero eta_iso is a real limitation of that convention and of a fixed-polynomial-modulus additive error budget. Independent nonzero CRT coordinates remove that particular term but do not establish the remaining extraction or noise comparison estimates.

This is a blind same-model review, complementary to other reviews rather than statistically independent confirmation. The report is to be frozen and hashed before any additional author material is read; the exact frozen-output hash is recorded outside this file in `your-input-hashes.json` and `partial.md`.
