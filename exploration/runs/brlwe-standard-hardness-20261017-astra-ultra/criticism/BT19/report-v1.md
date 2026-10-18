# BT19 independent blind reconstruction: all-width ideal alignment

Date: 2026-10-18 UTC. This is a complete report, also satisfying the partial-checkpoint obligation before 01:03 UTC.

## Verdict and scope

**ACCEPT as a conditional analytic theorem.** I independently reconstruct all of (T1)–(T5), the prime-ideal strict-descent implication, the stated large-width constants, and the limited arithmetic resource claim. I found no counterexample or mathematical gap in those claims under their stated hypotheses. A short dual-lattice argument proves an error term smaller than the one stated, so neither the constant 32 nor the relaxed constant 256 needs a delicate geometric estimate.

This verdict does **not** establish an oracle implementation, a concrete width lower bound, any family-hardness implication, or a polynomial-time rejection procedure. Those are expressly outside the supplied theorem. No companion, prior proof, referee report, history, ledger, or motivating reduction was supplied or inspected. This is correlated same-model scrutiny, not formal verification.

The only mathematical input was `inputs/ideal-alignment-theorem-v1.md`, SHA256 `79faea39031aa47a5c5727191558d3b32c600437172415aa90232d9727f94f2b`. The separate exposure log records the complete access boundary.

## 1. Algebra and coefficient geometry

Let n be a power of two, n >= 2, let zeta denote the image of X in K, and write R = Z[zeta] = Z[X]/(X^n+1). Here X^n+1 is the cyclotomic polynomial of a primitive 2n-th root of unity. In particular K has degree n and R is its full ring of integers. I use the standard resulting Dedekind-domain facts: nonzero ideals are invertible, ideal norms multiply, and nonzero prime ideals are maximal. These are algebraic structural facts, not additional oracle or hardness assumptions.

For a = sum_i a_i zeta^i and b = sum_i b_i zeta^i, the coefficient inner product satisfies

    <a,b> = (1/n) Tr_(K/Q)(a conjugate(b)).

Indeed, Tr(zeta^(i-j)) is n for i=j and zero for the other differences occurring here. Consequently

    sum_sigma |sigma(a)|^2 = n ||a||^2.

Arithmetic-geometric mean applied to the n positive quantities |sigma(a)|^2 gives, for a != 0,

    |N_(K/Q)(a)| <= ||a||^n.                          (1)

The determinant of multiplication by a is N_(K/Q)(a), so principal-ideal determinant agrees with its absolute field norm. Conjugation is an orthogonal map of coefficient space and preserves ideal determinant.

For an integral ideal J, let J* denote its coefficient Euclidean dual. Its basis is the inverse transpose of an integral basis matrix, so its vectors belong to K. We have

    J* = (conjugate(J))^(-1).                         (2)

To check this directly, y is in J* exactly when Tr(j conjugate(y))/n is integral for all j in J. As J is an ideal, the same condition holds with j replaced by jr for every r in R. Since the coefficient basis makes R self-dual for the normalized trace pairing, this is equivalent to j conjugate(y) in R for every j in J. Conjugating gives y conjugate(J) contained in R, which is (2).

Set D_J = N(J). For nonzero y in J*, the ideal y conjugate(J) is a nonzero integral ideal. Thus

    1 <= N(y conjugate(J)) = |N_(K/Q)(y)| D_J.

Together with (1), this proves the crucial bound

    ||y|| >= D_J^(-1/n) for every nonzero y in J*.    (3)

This is independent of the quality of any displayed basis. No short basis is constructed, supplied as advice, or passed to an oracle.

## 2. A Gaussian dual-mass lemma with explicit constants

For a full rank lattice L in R^n whose nonzero vectors have length at least a>0, suppose t a >= sqrt(n). I claim

    rho_(1/t)(L) < 2.                                (4)

For integer k>=1, the number of lattice points satisfying

    k a <= ||y|| < (k+1)a

is at most (2k+3)^n. The open balls of radius a/2 around these points are disjoint and lie in the ball of radius (k+3/2)a; comparison of their volumes proves this count. Therefore

    rho_(1/t)(L)-1
      <= sum_(k>=1) (2k+3)^n exp(-pi t^2 a^2 k^2)
      <= sum_(k>=1) [(2k+3) exp(-pi k^2)]^n.

For k>=1, 2k+3 <= 5^k and k^2>=k. Setting r=(5 exp(-pi))^n bounds the last sum by r/(1-r). Since exp(pi)>10 and n>=2, r<1/4 and r/(1-r)<1/3<1. This proves (4), including its boundary t a = sqrt(n).

The ordinary Gaussian Poisson identity in the coefficient Euclidean metric is

    rho_s(J) = (s^n/D_J) rho_(1/s)(J*).              (5)

It follows by periodizing the Gaussian, whose Fourier transform is s^n exp(-pi s^2 ||y||^2); both Gaussian sums converge absolutely. In particular

    rho_s(J) >= s^n/D_J for every s>0.               (6)

Combining (3)–(5), with

    t_J = sqrt(n) D_J^(1/n),

gives

    rho_s(J) <= 2s^n/D_J whenever s >= t_J,          (7)
    rho_(t_J)(J) <= 2 n^(n/2).                      (8)

The factor 2 is intentionally loose; the preceding packing estimate already gives a smaller factor.

## 3. Reconstruction of the entire all-width probability bound

Let F and I be nonzero integral ideals, with N(F)=D_F and N(I)=M. Primality of I is not needed in this section. Put J=FI, so D_J=D_F M. Since J is contained in F and the zero vector has Gaussian weight one,

    p = Pr_(X~D_(F,s))[X != 0 and X in FI]
      = (rho_s(J)-1)/rho_s(F).                       (9)

This is the original, unconditioned law, including its atom at zero.

If s >= t_J, (6) and (7) show

    p <= rho_s(J)/rho_s(F)
      <= [2s^n/(D_F M)]/[s^n/D_F]
      = 2/M.                                        (10)

If 0<s<t_J, Gaussian mass is monotone in its width. Equations (6) and (8) give

    p <= rho_(t_J)(J)/rho_s(F)
      <= 2 D_F n^(n/2)/s^n.

The promised D_F <= 2^(rho n), with 0<=rho<1, implies D_F<=2^n. Hence

    2 D_F n^(n/2)/s^n
      <= (4 sqrt(n)/s)^n
      <= (32n/s)^n.                                 (11)

The first inequality uses 2^(n+1)<=4^n, valid here. Combining the two width regimes, and also p<=1, proves

    p <= min(1, 2/M + (32n/s)^n).

Replacing 32 by 256 only enlarges this upper bound. In fact the same reasoning also proves the displayed sum with 4 sqrt(n) in place of 32n; this stronger auxiliary estimate is used only to verify the stated constants.

The probability proof did not need I to be prime or M>2^(rho n). Thus it applies, in particular, to every nonzero integral I under the source's stated conditions. It uses the full infinite Gaussian sums throughout. It needs neither smoothing as an oracle assumption nor average/random ideal behavior. The optional coprimality restriction gcd(D_F,q)=1 is irrelevant to this estimate.

The proof covers the equality boundary s=t_J by (10), every positive width, rho=0, and n=2. If the stated right side is at least one the bound is simply vacuous, not erroneous.

## 4. Prime-ideal strict descent

Now assume I is prime and X!=0. Since X belongs to F, the ideal

    C=(X)F^(-1)

is integral and nonzero. Let d be the least positive integer for which

    I''=d I C^(-1)

is integral. Such a d exists because the fractional ideal I C^(-1) has a rational coefficient basis. Invertibility gives

    I'' integral  <=>  dI contained in C,            (12)
    N(I'') = d^n M/N(C).                            (13)

Suppose X is not in FI. Equivalently, (X) is not contained in FI, hence C is not contained in I. Maximality of the prime ideal I then gives I+C=R. Multiplying by d and using (12),

    dR = dI+dC contained in C.

Taking integral-ideal indices yields N(C)<=N((d))=d^n. Equation (13) therefore gives N(I'')>=M. Its contrapositive is precisely

    N(I'')<M  =>  X!=0 and X in FI.                 (14)

Minimality of d is compatible with this argument but is not needed for the necessity implication: every positive integer d that clears this fractional ideal obeys the same obstruction.

If X=0, C^(-1) is undefined and this branch must remain a failure in the original experiment. The source explicitly does so. Adding eligibility, a nonzero second sample, or a norm cutoff intersects (14) with further events and can only lower the original unconditioned success probability.

Two exact algebraic controls distinguish the scope:

* **Primality matters for descent.** In R=Z[i], take n=2, rho=0, F=R, I=(4), and X=2. Then M=16, C=(2), d=1, and I''=(2) has norm 4<16, although 2 is not in (4). This is not a counterexample to the source: its nonprime extension explicitly excludes the descent interpretation.
* **Alignment is necessary, not sufficient.** In R=Z[i], take rho=0, F=R, I=(1+i), and X=2. Then X lies in FI, but C=(2), the minimal d is 2, and I''=I still has norm 2. Thus no equivalence or success guarantee may be inferred from (14).

## 5. Adaptive full-history and selection statements

On an active history h before draw j, define the measurable alignment event for the prescribed parameters as

    E_j(h) = {x : x!=0 and x in F_j(h) I_j(h)}.

Equation (T1) gives D_(F_j,s_j)(E_j)<=B_j. By the definition of total variation, the stipulated conditional kernel obeys

    Q_j(E_j) <= min(1,B_j+epsilon_j).

Since A_j is already measurable before this draw, multiplying by it proves (T2). On an inactive history both sides are zero; any arbitrary values for otherwise-unused parameters may be assigned there. The epsilon_j are understood to be nonnegative TV error bounds.

Only the conditional distribution given the actual complete pre-draw history is used. The source correctly assumes this contract almost surely in the actual experiment. A promise only about an unconditional marginal or a hidden-state average would not justify this step.

For any subsequently chosen random subset S of active indices, define

    Y = sum_(j=1)^T A_j 1_(E_j),
    Y_S = sum_(j in S) 1_(E_j).

The following inequalities are pointwise, regardless of how S uses the observed values, future draws, stopping rules, or extra randomness:

    0 <= Y_S <= Y,
    1_{Y_S>=1} <= Y.

Applying conditional expectation to each summand of Y and then the tower property proves

    E Y_S <= E sum_(j=1)^T A_j min(1,B_j+epsilon_j),

and, after also using that a probability is at most one, proves (T3). No independence between selected events, or between stages, was used.

Under the uniform active-history bounds M_j>=M_min and s_j>=s_min,

    A_j min(1,B_j+epsilon_j)
      <= A_j [2/M_min+(32n/s_min)^n+epsilon_j].

Summing, using sum_j A_j<=T and sum_j A_j epsilon_j<=E_tot almost surely, and taking expectation proves (T4). This pays for all active draws, as required.

For the separately stated full-transcript comparison, use the same initial law and algorithmic transition/postprocessing rules in the two experiments and change only the oracle kernels. On each still-matched prefix, maximal coupling makes the next oracle replies differ with probability at most the deterministic stage bound epsilon_j. A union bound over the first mismatch proves transcript TV at most sum_j epsilon_j (and, implicitly, at most one). The stated common-history kernel contracts suffice. Subsequent common public postprocessing, including labeling failures, cannot increase TV. This does not assert that the weaker actual-history T2 premise alone supplies all the separately requested transcript hypotheses.

## 6. Exact normalizers, endpoint controls, and selection stress test

For a fixed F and s>0, every nonzero point has positive weight and F contains a nonzero point, so rho_s(F)>1. Therefore

    a = Pr[X!=0] = (rho_s(F)-1)/rho_s(F) > 0,

and division of (9) by a proves exactly

    Pr[X in FI | X!=0]
      = (rho_s(FI)-1)/(rho_s(F)-1).                  (15)

Repeated independent calls to the exact same original oracle have a geometric waiting time with success probability a. Their expected number through the first nonzero response is 1/a = rho_s(F)/(rho_s(F)-1), as stated. A cap of K attempts also leaves failure mass (1-a)^K. Neither that mass nor the attempted draws can be discarded in an original-experiment probability or runtime statement.

For an arbitrary event G of probability a>0, the exact relation is

    Pr[E|G] = Pr[E intersect G]/a <= min(1,Pr[E]/a).

Taking G=E when Pr[E]>0 gives conditional probability one, demonstrating the possible inflation. There is no unchanged original-law bound under arbitrary selection conditioning.

The limits of the original Gaussian expression also check correctly:

* As s decreases to zero, rho_s(F) and rho_s(FI) both tend to one, so the original p tends to zero. The subtracted one in the numerator is essential. Absolute convergence and domination by any fixed larger-width Gaussian justify the limit.
* As s tends to infinity, (5) gives rho_s(F)~s^n/D_F and rho_s(FI)~s^n/(D_F M), so p tends to 1/M. Thus the 2/M large-width term is a valid upper envelope.
* At rho=0, the determinant condition forces F=R. The final negligible asymptotic statement appropriately imposes a fixed strictly positive rho instead.

Here is a concrete exact stress test against charging only selected draws. It does not require an experiment. Take n=2, F=Z[i], I=(2+i), rho=0, and s=128. The norm M is 5 and

    B = 2/5+(64/128)^2 = 13/20.

For the one-dimensional theta sum, comparison of a decreasing Gaussian sum to its integral gives rho_128(Z)<=129. Hence rho_128(F)<=129^2=16641. By (6), rho_128(I)>=128^2/5. Therefore the actual one-draw alignment probability satisfies

    p >= (128^2/5-1)/129^2 = 16379/83205 > 1/6.

Take six independent original draws and retain only the first aligned draw if any. At most one draw is retained, but the retained-alignment probability is

    1-(1-p)^6 > 1-(5/6)^6 > 13/20 = B.

The last inequality is exact since 20*15625 < 7*46656. Thus replacing the number of active draws by the number retained would be false even in this elementary instance. The source's (T3), which charges six active draws, remains valid.

## 7. Large-width constants, effective parameters, and finite resources

With fixed 0<rho<1, M>2^(rho n), and s>=512n^2,

    2/M < 2^(1-rho n),
    (32n/s)^n <= (1/(16n))^n.

Thus (T1) is at most the asserted 2^(1-rho n)+(16n)^(-n). For n tending to infinity through powers of two, both summands are negligible; multiplying by a polynomial number of attempts preserves negligibility. Adding a negligible total oracle error preserves it as well. The analogous adaptive conclusion uses (T4), or the corresponding expected active-history sum, with the stated uniform width and norm hypotheses.

This conclusion depends on the lower width bound. The conditional availability of D_(F,s) for declared widths does not impose s>=512n^2. Nor does a fixed-rho asymptotic statement automatically extend to rho=0 or to an arbitrary rho(n) tending to zero. No unspecified companion is used to supply any of these hypotheses here. Every width in this reconstruction is a coefficient width; the full canonical Euclidean norm is sqrt(n) times the coefficient norm, as stated.

The arithmetic resource sentence is valid when read, as written, in the bit size of the returned X and the ordinary ideal bases. Multiplication matrices, rational matrix inversion, lattice products, and normal-form computation construct C and I C^(-1). Formula (2) also supplies ideal inversion through coefficient duality and conjugation, without ideal factorization. For any rational basis matrix of I C^(-1), the least positive integer d that clears every reduced entry denominator is the lcm of those denominators. This is exactly the integrality condition for d I C^(-1), so the minimum d and a basis for I'' can be obtained by polynomial-bit integer/rational lattice arithmetic. Membership is another normal-form computation. These statements do not bound the oracle's sampling time or the bit length of its output by a polynomial in n alone.

In particular, the retry expectation can be enormous even for an ordinary input. For F=Z[i] and 0<s<=1, put u=exp(-pi/s^2). Since k^2>=k for k>=1,

    rho_s(Z) <= 1+2u/(1-u) = (1+u)/(1-u).

Consequently the nonzero probability satisfies

    Pr[X!=0] = 1-rho_s(Z)^(-2)
      <= 1-[(1-u)/(1+u)]^2
      = 4u/(1+u)^2 <= 4u.

The expected attempts to obtain a nonzero result are therefore at least exp(pi/s^2)/4. Taking the rational width s=2^(-b) gives at least exp(pi*4^b)/4 attempts despite a width description of O(b) bits. This confirms the importance of the source's finite-runtime limitation rather than contradicting any theorem assertion.

Finally, a selected short combination of previous oracle outputs has a different conditional distribution. None of the proofs above permits substituting such a combination for the next fresh conditional Gaussian draw. The source correctly keeps that separate.

## 8. Audit disposition

All advertised analytic, adaptive, descent-necessity, normalization, and limited arithmetic assertions survive this independent reconstruction. The nonprime descent example, alignment-without-descent example, exact selection example, and small-width retry lower bound identify the boundaries that must remain explicit. No authorized finite computation was needed; no experiment or external retrieval was performed. The report and exposure log were completed before any findings were disclosed and are frozen by the accompanying full-file SHA256 manifest.
