# S12 supporting calculations

Run `brlwe-explore-20260906-astra-ultra`; baseline/control scout. These are finite analytical checks, not a proof audit or a binary-RLWE hardness claim. No experiments were run.

## 1. The continuous precursor already exposes the integer-lattice quotient

**Evidence: fully written small calculation.** Use row vectors. Let $F\in\mathbb Z^{n\times n}$ be nonsingular over the rationals and invertible modulo an odd $q$. Choose an integer representative $H$ of its modular inverse and write

\[
HF=I+qK,\qquad \Lambda=\mathbb Z^nF.
\]

For an independent real error vector $E$, the first precursor in the 2020 proof is

\[
U=(SH+EF^{-1})\bmod q.
\]

Here modulo $q$ for a real vector means reduction into a fundamental box of $q\mathbb Z^n$. The analyst knows $F,H$; the public adversary generally does not. Let $u$ be the representative supplied by $U$. There is an integer vector $k$ such that

\[
uF=S+E+q(SK-kF).
\]

Compute $v=uF$, $w=\operatorname{center}_q(v)$, and $J=(v-w)/q\in\mathbb Z^n$. On the explicitly required event

\[
\mathcal N=\{\|S+E\|_\infty<q/2\},
\]

we have $w=S+E$, hence $J=SK-kF$. Consequently

\[
qJ=qSK-qkF=SHF-S-qkF\equiv-S\pmod\Lambda.
\]

Thus $(F,U)$ determines $S\bmod\Lambda$ on $\mathcal N$. This does not use discretization of $E$, a bound on the number of cosets, or a singular-value upper bound. It also does not say that the public transcript determines $U$ or the quotient.

For independent coefficient continuous Gaussians of width $t_1$, with density $t_1^{-1}\exp(-\pi x^2/t_1^2)$, binary $S$ gives

\[
\Pr[\neg\mathcal N]\le 2n\exp\left(-\pi(q/2-1)^2/t_1^2\right).
\]

In Theorem 5.7, $t_1=\sigma_{0,\mathrm{coeff}}/\tau_1$ if $\tau_1$ denotes the actual ratio operator norm. The precise sufficient condition is $q\tau_1/\sigma_{0,\mathrm{coeff}}\gg\sqrt{\log n}$. More generally the Gaussian decomposition permits any upper bound $L\ge\tau_1$, setting $t_1=\sigma_{0,\mathrm{coeff}}/L$. Taking the published polynomial bound enlarged to $L\ge1$, a target gap $q/\sigma_{0,\mathrm{coeff}}\ge n^c$ implies negligible no-wrap failure. This is a statement about the chosen precursor in the existing proof, not an assertion that every possible decomposition is nonlossy.

If the binary cube maps injectively into $\mathbb Z^n/\Lambda$, an information-theoretic decoder enumerates its $2^n$ points and recovers $S$ from the quotient, with probability at least $1-\Pr[\neg\mathcal N]$. Hence

\[
\widetilde H_\infty(S\mid F,U)\le-\log_2(1-\Pr[\neg\mathcal N]).
\]

The correct data-processing step is

\[
\widetilde H_\infty(S\mid Y,F,Z)\ge
\widetilde H_\infty(S\mid U,F,Z),
\]

where $Y=UZ+E'_1\bmod q$, and the independent residual can be included and then discarded in the conditioning. The displayed equality in the source proof can be read as this sufficient inequality; no theorem refutation is claimed.

## 2. Standard 2020 denominator: exact quotient is injective on its usual good event

**Evidence: source-verified result plus fully written small calculation.** Let $R=\mathbb Z[X]/(X^n+1)$, $n\ge2$ a power of two, and $F=M_f$. The coefficient multiplication matrix is normal, with singular values $|f(\zeta_j)|$. The embedding matrix obeys $V^*V=nI$, so canonical norm is $\sqrt n$ times coefficient Euclidean norm. In particular a canonical Gaussian width $\gamma$ corresponds to coefficient width $\gamma/\sqrt n$.

Lemma 6.5 of [Brakerski–Döttling 2020](https://eprint.iacr.org/2020/1185.pdf), printed p.20, gives the good event

\[
\|\sigma(f^{-1})\|_2\le24\sqrt n/\gamma
\]

with probability at least $1/2$, assuming $\gamma\ge8n\eta_\epsilon(R)$. Its use inside Lemma 6.8 also conditions on modular invertibility and imports the stated ring/modulus conditions; this note does not extend those conditions to all odd $q$.

On this event,

\[
\sigma_{\min}(F)\ge\gamma/(24\sqrt n).
\]

If $\gamma>24n$, no nonzero binary difference $\Delta\in\{-1,0,1\}^n$ lies in $\mathbb Z^nF$: otherwise $\Delta=zF$ for nonzero integer $z$, and

\[
\sqrt n\ge\|\Delta\|_2\ge\sigma_{\min}(F)\|z\|_2>
\sqrt n.
\]

This establishes cube injectivity. Since $\eta_\epsilon(R)=\sqrt n\eta_\epsilon(\mathbb Z^n)$, the published lower bound $\gamma\ge8n\eta_\epsilon(R)$ implies $\gamma>24n$ asymptotically. Thus the same sufficient good event used to control the ratio norm already forces zero binary residual entropy in the precursor, up to no-wrap failure. Improving $\log|\det F|\le n\log\sigma_{\max}(F)$ alone cannot fix that event.

This is not a claim about all denominator draws, all alternative good events, or all possible lossiness proofs. The 2022 rank-preserving extension retains the same precursor step but uses a different denominator analysis; the present quantitative $24\sqrt n/\gamma$ deduction is only asserted for the 2020 instantiation and rank-one applications that explicitly reuse its lemma.

## 3. Strict data processing even with the reference discrete binary law

**Evidence: fully written small calculation.** Set $F=Z=2I$, $H=((q+1)/2)I$, and let $S$ be uniform coefficient binary and $E\sim D_\sigma^n$ exactly as in the reference ledger. Put

\[
U=(SH+E/2)\bmod q,\qquad Y=2U\bmod q=S+E\bmod q.
\]

The public matrix is $A=I$. The preceding quotient decoder recovers all bits from $U$ except on the no-wrap tail, since $\Lambda=2\mathbb Z^n$. But the *unwrapped* observation $S+E$ has exact guessing probability

\[
p_{\rm guess}(S\mid S+E)=\left(\frac{1+D_\sigma(0)}2\right)^n.
\]

For one bit, the likelihood comparison switches between outputs $0$ and $1$; each conditional success probability is $\Pr[E\le0]=(1+D_\sigma(0))/2$. Independent coordinates multiply these probabilities. Thus

\[
\widetilde H_\infty(S\mid S+E)=n-n\log_2(1+D_\sigma(0)).
\]

Taking $\sigma=n$ gives $n-O(1)$ bits. Reducing this observation modulo $q$ can only increase its conditional min-entropy. Taking, for example, odd polynomial $q\ge n^{1+c}$ simultaneously makes the precursor decoding failure negligible. This is an exact example where precursor conditioning destroys the useful lossiness of the transcript. It preserves coefficient binary secret, rank one, and the discrete-Gaussian coefficient law, but replaces uniform public $A$ by the fixed $I$; it is therefore an illustration of a proof step, not a pseudorandom construction or an attack on the reference target.

## 4. Exact index can save the entropy inequality, but quotient exponent gives a distinguisher

**Evidence: fully written small calculation; simple replacement refuted.** Let $f=1+X$ and $F=M_f$. Since $n$ is even,

\[
R/(f)\simeq\mathbb Z/2\mathbb Z,\quad |\det F|=2,
\quad\sigma_{\max}(F)=2\cos(\pi/(2n)).
\]

The quotient of a binary polynomial is the parity of its coefficient sum. Therefore

\[
\widetilde H_\infty(S\mid S\bmod(f))=n-1.
\]

The exact determinant charge is one bit, whereas $n\log_2\sigma_{\max}(F)=n-O(1/n)$. This conclusively shows that the singular-value charge can be much too coarse for specially chosen denominators.

However

\[
\frac2{1+X}=1-X+X^2-\cdots-X^{n-1}\in R.
\]

For any ratio $a=z/f\bmod q$, suppose its rational multiplication matrix satisfies $\|M_{z/f}\|_2\le L$. Then $2z/f\in R$, and each coefficient has absolute value at most $2L$: the coefficient Euclidean norm of a polynomial is at most its multiplication operator norm. If $2L<q/2$, the public test

\[
\|\operatorname{center}_q(2a)\|_\infty\le2L
\]

accepts. For uniform $a\in R_q$, multiplication by $2$ is a permutation, so its acceptance probability is

\[
\left(\frac{2\lfloor2L\rfloor+1}{q}\right)^n
\le\left(\frac{4L+1}{q}\right)^n.
\]

Even if the ratio bound occurs only with inverse-polynomial probability, this gives a nonnegligible distinguishing advantage when $q/L$ is polynomially growing. One ring sample suffices; no rotation is counted as an independent sample. The same check applies to any denominator ideal with a known small positive integer $\kappa\in(f)$, replacing $2$ by $\kappa$, provided $\gcd(\kappa,q)=1$.

The unresolved possibility is a denominator distribution whose binary quotient has large fibers, whose ratio norm permits small target noise, and whose quotient has no exploitable small integer exponent. A proposed distribution should first be checked symbolically for this exponent before any experiment or expensive hardness speculation.
