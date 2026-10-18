# H-ALIGN v1: complete author proof

Status PROVISIONAL. Frozen statement: theorem-only-v1.md. No independent gate has yet accepted these bytes. Every Gaussian below has its original infinite normalizer.

## 1. Coefficient duality and algebraic minimum lengths

For field elements u,v, coefficient inner product is Tr(u conjugate(v))/n. This follows by evaluating the power basis at all n primitive 2n-th roots: the normalized Fourier matrix is unitary. In particular,

    sum_sigma |sigma(u)|^2 = n ||u||^2,
    |N_(K/Q)(u)|^(1/n) <= ||u||.                       (P1)

The second formula is arithmetic-geometric mean applied to the nonnegative squared absolute values. It also holds for nonintegral field elements.

For every nonzero integral ideal L, its coefficient dual is exactly conjugate(L)^-1. Here is a direct check that avoids an unrecorded trace normalization. If y belongs to conjugate(L)^-1, then x conjugate(y) is integral for every x in L, so its constant coefficient, which equals <x,y>, is integral. Conversely, if all <x,y> are integers, apply this to every negacyclic rotation of x, which also belongs to L. All coefficients of x conjugate(y) are then integers. Thus conjugate(y)L is contained in R, proving y belongs to conjugate(L)^-1. The rationality of y follows from the integral ordinary basis defining the dual.

If 0!=x in L, the integral ideal (x)L^-1 has positive integer norm |N(x)|/N(L), whence |N(x)|>=N(L). If 0!=y in L*=conjugate(L)^-1, the integral ideal (y)conjugate(L) has positive integer norm |N(y)|N(L), whence |N(y)|>=1/N(L). By (P1), with r=N(L)^(1/n),

    lambda_1(L)>=r,       lambda_1(L*)>=1/r.           (P2)

All norms in (P2) are coefficient norms. A factor n belonging to the canonical trace dual must NOT be imported into this formula.

## 2. An elementary all-width packing estimate

Let L be any real lattice of dimension n and minimum distance lambda>0. For t>=0, the open balls of radius lambda/2 centered at lattice points of the closed ball of radius t are disjoint and lie in the ball of radius t+lambda/2. Volume comparison therefore yields

    N_L(t) := #{x in L: ||x||<=t} <= (1+2t/lambda)^n.  (P3)

Tonelli's theorem applied to nonnegative terms and the identity exp(-pi r^2/s^2)=integral_(r)^infinity (2pi t/s^2)exp(-pi t^2/s^2)dt gives

    rho_s(L)=integral_0^infinity N_L(t)(2pi t/s^2)
                                     exp(-pi t^2/s^2)dt.

For n>=2, (a+b)^n<=2^(n-1)(a^n+b^n). In our even dimensions, Gamma(n/2+1)=(n/2)!<=(n/2)^(n/2). Hence

    rho_s(L)
      <=2^(n-1)[1+(2s/(sqrt(pi)lambda))^n Gamma(n/2+1)]
      <=2^(n-1)[1+(sqrt(2n/pi)s/lambda)^n]
      <=[4sqrt(n) max(1,s/lambda)]^n.                  (P4)

The last inequality is deliberately loose: replace the sum by twice its larger term and use sqrt(2/pi)<2. The zero point contributes one throughout; it is not silently deleted from the Gaussian numerator.

## 3. A sufficient smoothing threshold with explicit shells

Suppose lambda_1(L*)>=1/r and s>=4sqrt(n)r. For each integer k>=1, the number of nonzero dual points in k lambda<=||y||<(k+1)lambda, with lambda=lambda_1(L*), is at most (2k+3)^n by (P3). Therefore

    rho_(1/s)(L*)-1
      <=sum_(k>=1)(2k+3)^n exp(-pi s^2 k^2 lambda^2)
      <=sum_(k>=1)(2k+3)^n exp(-16pi n k^2)<1.         (P5)

For the strict final inequality, 2k+3<=5^k follows by induction from equality at k=1. Since k^2>=k, the last sum is at most a/(1-a), where a=(5exp(-16pi))^n<1/2 for n>=2. Thus (P5) is valid without an unstated asymptotic condition.

Centered Poisson summation has only positive dual terms:

    rho_s(L)=s^n/det(L) rho_(1/s)(L*).

It follows that rho_s(L)<2s^n/det(L) at the preceding sufficient threshold, and rho_s(F)>=s^n/D_F for EVERY s>0. No shifted coset is identified with its centered normalizer.

## 4. The dichotomy, exact event, and descent

Set L=FI and r=(D_F M)^(1/n). The exact Gaussian event excluding zero has probability [rho_s(L)-1]/rho_s(F), since L is a sublattice of F and rho_s(0)=1.

If s>=4sqrt(n)r, (P2),(P5) and Poisson give

    [rho_s(L)-1]/rho_s(F) <=2/M.

Otherwise lambda_1(L)>=r, so max(1,s/lambda_1(L))<=4sqrt(n). Consequently (P4) gives rho_s(L)<=(16n)^n. As D_F<=2^(rho n)<2^n,

    [rho_s(L)-1]/rho_s(F)
      <= D_F (16n/s)^n <=(32n/s)^n.

Both cases imply (T1), and probability is additionally at most one. The use of rho_s(L) rather than rho_s(L)-1 is an upper bound, so the small-width/zero-dominated regime cannot invalidate it. The argument did not need I to be prime.

For the descent corollary, C=(X)F^-1 is integral. Put B=gcd(I,C), with prime-ideal valuations min(v_P(I),v_P(C)). The denominator ideal of IC^-1 is CB^-1. Since dR is contained in this denominator ideal, d^n>=N(C)/N(B), and hence

    N(dIC^-1)=d^n M/N(C)>=M/N(B).

When I is prime, strict descent forces B=I, or equivalently I divides C. This is exactly X in FI. The algorithm has already excluded X=0. Nothing asserts that this necessary event is sufficient for eligibility or for a short nonzero second output.

## 5. Complete histories, postselection, and errors

Fix an active positive-probability history H_(j-1). Its F_j,I_j,s_j and activity indicator are already fixed. Under the exact next kernel, Section4 gives its ORIGINAL event mass with the original theta denominator. Total variation changes that event mass by at most epsilon_j, proving (T2) almost surely, including countable or general-history versions through conditional kernels.

For any later selection S, pointwise the number of selected alignment events is at most sum_j A_j 1_{0!=X_j in F_j I_j}. The indicator of at least one selected alignment is at most the same sum. Take expectation, apply the tower rule at each stage, and insert (T2). This proves (T3); uniform lower bounds and the deterministic attempt cap give (T4). No multiplication of marginal or selected probabilities occurs. A cached value reused without a fresh oracle draw does not satisfy the fresh-kernel premise and must not be counted as another fresh attempt.

For the optional full transcript comparison, couple the two stage kernels whenever their past transcripts coincide. Conditional disagreement probability is at most the declared deterministic epsilon_j. Once they diverge no further coupling property is needed. A union bound on the first disagreement gives transcript TV at most sum_j epsilon_j. Appending deterministic/randomized public output maps contracts TV. This uses the declared complete-kernel contract, including the actually possible selected inputs; a promise only for unconditional one-call marginals would not suffice.

For any original one-draw event E and event V of mass a>0, Bayes' formula is Pr[E|V]=Pr[E intersect V]/a. Taking V={X!=0} gives (T5), with denominator rho_s(F)-1. Independent original attempts until V have geometric waiting time with mean 1/Pr[V]=rho_s(F)/(rho_s(F)-1). This exact statement does not authorize a bounded-runtime exact Gaussian implementation. For any other retained branch, its ACTUAL numerator and normalizer are required. Selection on alignment itself makes conditional alignment probability one.

## 6. CP-1 and finite-scope controls

The mandatory cached-prefix counterexample has original masses A_b=21/2200, C_b=1/11 and D=879/1100, with Pr[vk=1]=10/11. Its conditioned masses are A_b=21/2000, C_b=1/20 and D=879/1000. Initial incidences are p(x)=1/10, p(e_b)=121/2000=0.0605 and p(f_b)=21/2000=0.0105; none exceeds gamma=1/10. The specified two-hit matching has probability 21/2000>1/100=gamma^2, while the later incidence 21/221<1/10. Conditioning removes sibling support, and transferring the cached prefix changes the first incidence from121/2000 to221/2000. The old product rule is false.

Our proof neither asserts that CP-1's selected hits obey the fresh conditional Gaussian premise nor multiplies their marginal lightness bounds. It would bound any selected success by the sum of the full applicable per-attempt probabilities; it never uses a latent cache-hit status as a physically observed branch. The exact finite control reproduces all these fractions and explicitly rejects gamma^2. It also checks original/zero-conditioned/postselected normalizers and packing counts in finite Gaussian-weight laws. Those finite laws are distinct truncated distributions and cannot establish Sections1–4 for the infinite Gaussian. Independent nonauthor and blind checks remain required.

## 7. Asymptotic substitution and scope

For s>=512n^2, (32n/s)^n<=(16n)^(-n). For M>2^(rho n), 2/M<2^(1-rho n). These are negligible together for fixed rho>0, and remain negligible after a polynomial number of attempts plus negligible cumulative TV error. When rho=0 this exponential-in-index conclusion is not asserted. A broader class-changing algorithm, correlated relation search, or a polynomially bounded combination of samples has a different output kernel and is not covered by this one-draw obstruction. Such a combination must be analyzed under its own full law.
