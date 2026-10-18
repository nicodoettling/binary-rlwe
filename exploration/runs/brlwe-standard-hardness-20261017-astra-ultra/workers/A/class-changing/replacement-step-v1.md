# A-CLASS replacement step: a controlled transfer with a descent-density gate

Status PROVISIONAL. This is a concrete oracle-assisted algorithm and a scoped analysis of its geometry and success mass. It is not a standard-hardness reduction or a theorem against every class-changing method. No experiment has yet been run for this file; the exact hand countercontrol below precedes the general statement.

## 1. Exact small control

In Z[i], let F=(1+i), I=(3+2i), with norms 2 and 13. If an F-oracle returns x=2, then C=(x)F^-1=(1-i), and

    I'=I C^-1=((5-i)/2).

The least positive integer clearing its denominator is d=2. Consequently I''=dI'=(5-i) has norm 26, larger than N(I)=13. The output multiplier x/d=1 is harmless, but there was no descent. This shows why clearing the denominator cannot be ignored.

If instead x=(1+i)(3+2i)=1+5i, then C=I, I'=I''=R and d=1. Transferring y=1 gives x in I with norm ratio ||x||/N(I)^(1/2)=sqrt(2). This is a geometrically good one-step descent. It required x in FI, not an arbitrary short sample in F. The Gaussian mass of this event, with zero excluded, is the issue analyzed below. The Gaussian integer example is algebraic and easy; it is a falsification control, not a hard family.

## 2. The actual algorithm and full output law

Let R=Z[X]/(X^n+1) with n a power of two, and let I be any nonzero integral input ideal. Choose an eligible nonzero integral F, meaning N(F)<=2^(rho n) and gcd(N(F),q)=1. Its ordinary basis may depend on I and previous classical history. Invoke only the promised centered oracle for F, obtaining x approximately distributed as coefficient D_(F,s_F). If x=0, return FAIL. For nonzero x compute exactly

    C=(x)F^-1,       I'=I C^-1=IF/(x).

C is integral. Let d be the smallest positive rational integer with dI' integral, computed from the denominator ideal by integer linear algebra. Put I''=dI'. If I'' is not eligible, return FAIL rather than make an off-promise oracle call. Otherwise obtain y from the promised centered DGS oracle on I'', and output

    z=(x/d)y.

Membership is exact: (x/d)I''=IF subset I. If nonzero output is required, y=0 is another explicit failure. This algorithm is well-defined regardless of whether it ever reaches an eligible I''.

For exact first-oracle law, each x has mass rho_(s_F)(x)/rho_(s_F)(F). Retain all failures in the output experiment. Conditional on each successful x, the second draw has its stated D_(I'',s_(I'')) law. The output law is the pushforward of this joint experiment through z=(x/d)y. It is generally an ELLIPTICAL Gaussian on the subideal IF conditional on x, not a spherical Gaussian on I. Its covariance parameter is s_(I'')² M_(x/d)M_(x/d)^T. It does not have full support I unless F=R. No new DGS-on-I theorem is claimed.

If the two oracle calls have conditional total-variation errors at most epsilon_1 and epsilon_2 uniformly for every eligible input, the complete experiment including FAIL differs by at most epsilon_1+epsilon_2. Conditioning on a rare success event would require division by its probability; it is not done for free. No decisional endpoint is used here: the only imported interface is the restricted centered DGS oracle from the coordinator's current contract.

## 3. Exact index and norm transfer

Let B=gcd(I,C), with prime-ideal valuations min(v_P(I),v_P(C)). The denominator ideal of I C^-1 has valuations max(v_P(C)-v_P(I),0), hence equals C B^-1. Since dR is contained in this denominator ideal,

    d^n >= N(C)/N(B).

The cleared ideal satisfies

    N(I'') = d^n N(I)/N(C) >= N(I)/N(B).                 (A1)

In particular, if I and C are coprime, then N(I'')>=N(I). A sample from an unrelated small ideal does not decrease the index after honest clearing.

Define b(x)=||M_x||_op/|N(x)|^(1/n), equivalently the largest canonical absolute value divided by their geometric mean. For every nonzero y in I'',

    ||z||_coef/N(I)^(1/n)
      <= b(x) N(F)^(1/n) [||y||_coef/N(I'')^(1/n)].      (A2)

This follows by inserting N(I'')^(1/n)=d N(I)^(1/n)N(F)^(1/n)/|N(x)|^(1/n) into ||z||<=||M_x||||y||/d. The same relative inequality holds in full canonical Euclidean norm after the common sqrt(n) conversion. Thus ONE successful step need not multiply a long factor-base word's losses. Also |N(x)|>=N(F) gives b(x)N(F)^(1/n)<=||M_x||. Under x~D_(F,s_F), the accepted A-FRAC linear-tail argument yields

    Pr[||M_x||>s_F sqrt(n)L] <=4n exp(-piL²).

This supplies a polynomial one-step transfer loss at polynomial s_F. It does not establish that the successful branch has nonnegligible mass; its conditional probability must not be replaced by the unconditional Gaussian tail without a charge.

All ideal operations and the denominator computation are polynomial in the ordinary input basis lengths and the bit length of x. A polynomial-width Gaussian can be truncated to polynomial-bit x with a separately bounded failure probability. The arithmetic does not make the number of attempts polynomial when the successful branch is tiny.

## 4. Prime-input descent requires a rare congruence

Let I be a prime ideal with M=N(I)>2^(rho n), so it cannot divide any eligible F. For N(I'')<N(I), (A1) forces I to divide C. Therefore a necessary event for strict descent is

    0 != x in FI.

Under the exact centered first-oracle law, its probability is EXACTLY

    p_align = [rho_(s_F)(FI)-1]/rho_(s_F)(F).            (A3)

If the wrapper first repeats until x is nonzero, the corresponding probability is instead [rho_(s_F)(FI)-1]/[rho_(s_F)(F)-1], and the repeat cost is 1/(1-Pr[x=0]). Keeping these two laws distinct avoids a zero-mass or conditioning shortcut.

Every nonzero x in FI has |N(x)|>=N(F)M, so coefficient AM-GM gives ||x||_coef>=(N(F)M)^(1/n). The centered lattice-Gaussian moment bound from A-FRAC and a coordinate union bound therefore imply

    p_align <=min(1,2n exp(-pi (N(F)M)^(2/n)/(n s_F²))). (A4)

This is useful when the input root norm is much larger than the delivered width. In the opposite smoothed regime, if s_F>=eta_epsilon(FI), centered Poisson summation yields

    rho_(s_F)(FI)<= (1+epsilon)s_F^n/[N(F)M],
    rho_(s_F)(F)>=s_F^n/N(F),

and hence

    p_align <=(1+epsilon)/M.                             (A5)

This is a conditional sufficient bound for the smoothed regime, not a claim that every intermediate width has that mass. The exact expression (A3) covers all widths.

For adaptive attempts, each F and width must first be fixed conditional on the full prior transcript, then (A3)-(A5) apply to its fresh promised Gaussian draw. A uniform per-attempt bound can be summed over a bounded number of attempts; no independence of the selected successes is asserted. Approximate oracle error is added per attempt. This is the CP-1-safe accounting for this mechanism.

## 5. What this test changes

The one-step geometric transfer itself can be polynomial. The unprovided object is an efficient way to correlate an eligible F-Gaussian with a large prime factor of I, so that C shares that factor often enough to cause index descent. Algebraic class decomposition alone does not supply that correlation. Scalar denominator clearing defeats the naive hope that any short sample of F automatically moves I into a smaller eligible ideal.

The next constructive tests should use the full exponential index budget in correlated composite ideals or directly program simultaneous congruences. Independent small-prime sampling and an uncharged rare-event condition do not establish the desired standard family edge.
