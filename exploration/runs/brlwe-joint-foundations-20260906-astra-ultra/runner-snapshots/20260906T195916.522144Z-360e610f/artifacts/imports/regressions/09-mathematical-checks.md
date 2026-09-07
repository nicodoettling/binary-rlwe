# C03 mathematical criticism and hand regressions

Review date: 2026-09-06. Input version: `candidates/C03.md` and its
`transport.md`, read at 10:30 UTC. No numerical or exhaustive experiment was
run. The finite checks below are exact hand calculations. This report checks
the existing transport only; the proposed variance-matching lemma is excluded.

## Frozen statement and probability space

Let n be a positive power of two, q>1 odd, and
R=(Z/qZ)[X]/(X^n+1). Independently sample uniform a_1,a_2 in R and uniform
x,y in {0,1}^n. The source gives (a_1,a_2,t=a_1x+a_2y). The source task in the
finite lemma is recovery of the actual sampled pair (x,y), not merely a valid
pair. Let T have success epsilon in recovering uniform binary x from exactly
one pair (A,Ax+E), with A uniform in R and iid coefficient E distributed as
D_sigma modulo q. All solver coins are independent of these choices.

Put tau=pi/sigma^2, H=sum_(j=0)^(n-1) X^j, and
k_c=1+exp(tau)(cosh(2tau)-1). The claimed reduction aborts when a_2 is nonunit;
otherwise it sets A=a_2^(-1)a_1, C=a_2^(-1)t, gives
(A'=2A,B'=2C-H+G_sigma) to T, and reconstructs y_hat=C-Ax_hat.
The exact finite bound being checked is

    Pr[(x_hat,y_hat)=(x,y)] >= rho_q epsilon^2 / k_c^n.

For a polynomial-time interpretation, use polynomially bounded q and sigma,
an effective polynomial-bit representation of sigma^2, and charge total
variation error eta of the whole Gaussian sample by
rho_q max(0,epsilon^2/k_c^n-eta). The finite probability inequality itself
requires only sigma>0 and exact Gaussian sampling. It gives neither a source
hardness theorem nor a decision or multiple-independent-sample reduction.

## C03-R1: likelihood direction cannot be interchanged

Write P for the target law and Q for the simulated law. Cauchy--Schwarz gives

    P(F) = sum_z 1_F(z) [P(z)/Q(z)] Q(z)
         <= sqrt(Q(F) M_2(P||Q)),

so the required denominator is M_2(P||Q). It is not M_2(Q||P).

An exact full-support regression makes this distinction substantive. Take
P=(1/2,1/2), Q=(1/16,15/16), F={first point}. Then

    M_2(Q||P)=113/64,
    P(F)^2/M_2(Q||P)=16/113 > 1/16=Q(F).

Thus the reversed-direction success inequality is false. In the correct
direction M_2(P||Q)=64/15 and the lower bound is 15/256 <= 1/16.
The candidate passes: it uses a separate pointwise comparison to reverse the
Gaussian moment, rather than putting the exact forward identity into the
success bound.

## C03-R2: exact scalar calculation and the reverse bound

For P(z)=exp(-tau z^2)/Z_sigma and Q(z)=(P(z-1)+P(z+1))/2,

    Q(z)/P(z)=exp(-tau) cosh(2tau z) >= exp(-tau).

For integer k,

    E_P exp(2k tau Z)
      = exp(k^2 tau) [sum_z exp(-tau(z-k)^2)]/Z_sigma
      = exp(k^2 tau).

This equality depends on k being an integer. The proof uses only k=2 in the
cosh-square expectation, so no fractional-shift normalizer is being omitted.
Consequently,

    M_2(Q||P)
      = exp(-2tau) E_P[(1+cosh(4tau Z))/2]
      = exp(-2tau)(1+exp(4tau))/2
      = cosh(2tau).

The pointwise lower bound on Q then gives, term by term,

    chi^2(P||Q) = sum_z (P(z)-Q(z))^2/Q(z)
      <= exp(tau) sum_z (P(z)-Q(z))^2/P(z)
      = exp(tau)(cosh(2tau)-1).

Thus the claimed k_c is a valid upper bound for M_2(P||Q). It is not an
asserted exact reverse moment. The exact reverse moment is
exp(tau) E_P sech(2tau Z), also as stated by the candidate.

The original uncentered comparison is likewise sound: for integer u,
M_2(P||P+u)=exp(2tau u^2). Convexity in the second argument gives the
one-coefficient bound (1+exp(2tau))/2 after averaging u in {0,1}.

## C03-R3: products, wrapping, and what is actually exposed

The residual coordinates 2y_j-1 are independent signs. Since the G_j are
independent and independent of y, the unwrapped simulated error has the
product law Q^n. The target error has the product law P^n. Therefore
M_2(P^n||Q^n)=M_2(P||Q)^n by nonnegative summation. There is no multiplication
of success probabilities on adaptively selected histories.

For any map f, the fiberwise inequality

    (sum_(f(z)=r) P(z))^2/(sum_(f(z)=r) Q(z))
      <= sum_(f(z)=r) P(z)^2/Q(z)

proves contraction after summing r. This applies to wrapping modulo q,
including arbitrarily many wraps. No truncation or no-wrap event is used.

On a_2 being a unit, A=a_2^(-1)a_1 is exactly uniform and independent of
(a_2,x,y); conditioning has selected a_2 only. Since 2 is a unit, A'=2A has
the same property. Append shared independent (A',x) and the solver tape to
the two error laws and apply the common map
(A',x,e)->(A',x,A'x+e mod q). This is the correct joint experiment for
F={T(A',B')=x}.


## C03-R4: retaining the actual planted witness

The simulator does not need y to make its query, but its analyzed residual
is generated using the actual y. The event of outputting the planted pair is
pointwise exactly x_hat=x: if this occurs, y_hat=C-Ax_hat=y, and all checks
pass; if the planted pair is output, its first component necessarily equals
x. Thus y can be marginalized in the likelihood calculation without replacing
the planted witness by a fresh posterior sample.

Keeping C internally is legitimate. Passing C, y, or the source transcript
to T is a different oracle model. To see why revealing y matters, append the
same independent sign R under the target law and compare P against P+R
conditional on R. The one-coordinate joint moment is then exp(2tau), rather
than the mixture bound 1+O(tau^2). Across n coordinates it is exp(2n tau).
The candidate expressly excludes that strengthened transcript.

The existing ambiguity example survives: for n=1, q=3, a_1=a_2=1, t=1,
the valid binary pairs are (1,0) and (0,1). A validity check cannot say which
one was sampled. The current proof never relies on such recognition.

## C03-R5: units at composite odd moduli

For each prime p dividing q, p is odd and does not divide n. Hence X^n+1
is squarefree over F_p. Every root has multiplicative order exactly 2n,
because 2n is a power of two and its n-th power is -1. The Frobenius orbit
length is d_p=ord_(2n)(p), giving n/d_p irreducible factors of degree d_p.
The probability of a unit modulo p is (1-p^(-d_p))^(n/d_p).

Reduction modulo p detects units modulo p^e: the kernel is a nilpotent
ideal, so an inverse modulo p lifts. CRT across distinct prime powers then
gives the exact formula in the candidate,

    rho_q=product_(p|q) (1-p^(-d_p))^(n/d_p).

Since p^d_p >= 2n+1, Bernoulli's inequality gives each factor at least
1-n/(d_p p^d_p) >= 1-n/(2n+1) > 1/2. Thus
rho_q >= 2^(-omega(q)) >= q^(-log_3 2). This remains true at n=1, where
d_p=1 and it specializes to phi(q)/q. Prime powers have the same unit
fraction as their residue field, as the formula correctly records.

No factorization assumption enters the reduction algorithm. The public
multiplication matrix is invertible over Z/qZ exactly when its determinant
is coprime to q; its adjugate and a scalar modular inverse recover the
inverse ring element with polynomial bit complexity.

## C03-R6: polynomial success and a fixed-width counterexample

As sigma tends to infinity, tau tends to zero and

    log k_c = 2tau^2 + O(tau^3),
    log(k_c^n) = 2pi^2 n/sigma^4 + O(n/sigma^6).

Hence n/sigma^4=O(log n) suffices for polynomial likelihood loss.
If sigma^4=Omega(n), the likelihood factor is bounded by a constant. This
does not make rho_q a constant for every composite-q family. With
epsilon>=n^(-a), q<=n^C, and k_c^n<=n^b, the claimed source success is at
least n^(-2a-b-C log_3 2). The small-noise condition q/sigma>=n^c must still
be satisfied separately. The candidate states all these restrictions.

The centered displayed bound is not uniformly better at every finite width.
Set tau=log 2, equivalently sigma^2=pi/log 2. Then

    k_0=(1+exp(2tau))/2=5/2,
    k_c=1+2((4+1/4)/2-1)=13/4 > k_0.

This exact counterexample rejects an unrestricted improvement claim. It does
not refute the candidate, which limits the improvement to growing widths and
explicitly avoids a claim of improvement at every fixed small width.

## C03-R7: one sample is a genuine task boundary

Two direct repetitions of the source map with fresh Gaussians have
A'_1=A'_2 with probability one. Two independent target samples have this
equality with probability q^(-n). Thus even their public multipliers are
distinguished by an elementary equality test; the two-sample transcript
distributions have statistical distance at least 1-q^(-n).

They also reuse y. Neither repetitions nor ring rotations provide the
independent sample interface of an arbitrary polynomial-sample solver.
Independent source instances instead have different x's. The current
one-call lemma survives this regression because it does not claim any of
those conversions.

## C03-R8: inversion, collision search, and planted recovery

For n=1, q=5, a_1=1, a_2=2, the map (x,y)->x+2y sends the four binary
pairs injectively to 0,1,2,3. Binary inversion is trivial and yields the
original pair; there is no binary collision to extract. Even though a larger
ternary domain has collisions, returning the planted binary preimage does
not produce one. This refutes the generic shortcut from binary inversion to
collision search, without saying anything about hardness on uniform keys.

More generally, for fixed public weights let N(t) be the number of binary
pairs mapping to t. Since the planted pair is uniform on 4^n possibilities,
the best possible exact-witness success is

    sum_(t:N(t)>0) [N(t)/4^n] [1/N(t)]
      = |image|/4^n <= min(1,(q/4)^n).

For q=3 this is exponentially small without any computational assumption.
That constant-q example lies outside the simultaneous growing-width and
reference small-noise conditions used for polynomial transfer. Its role is
to demonstrate why exact-witness hardness, by itself, can reflect ambiguity
and must not be confused with any-preimage hardness.

## Mathematical disposition

No falsification of C03-L1 through C03-L7 was found. The exact finite transfer
survives this nonauthor review under its frozen one-sample model. This is a
checked conditional calculation, not formal proof certification: no blind
referee was commissioned in this bounded assignment, no experiment was
allocated, and the independent-hardness dependency remains open. None of the
hand boundary examples invalidates the carefully restricted present statement.
