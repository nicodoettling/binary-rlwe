# H-ALIGN v1: all-width prime alignment and honest attempt accounting

Frozen author statement. Status PROVISIONAL; no nonauthor, source, fresh-blind, or clean-artifact gate is inherited. This is a scoped obstruction for the specified replacement mechanism, not an arbitrary-ideal hardness theorem or a general impossibility result.

Fix a power of two n>=2, R=Z[X]/(X^n+1), its number field K, and coefficient Euclidean norm in the basis 1,X,...,X^(n-1). Put rho_s(x)=exp(-pi||x||^2/s^2), rho_s(L)=sum_(x in L)rho_s(x), and D_(L,s)(x)=rho_s(x)/rho_s(L). Ideal norm means coefficient-lattice determinant. The full canonical Euclidean norm is sqrt(n) times the coefficient norm. Widths in this theorem are coefficient widths.

Let 0<=rho<1, let I be a nonzero prime ideal of norm M>2^(rho n), and let F be any nonzero integral ideal of norm D_F<=2^(rho n). For compatibility with the restricted oracle one may additionally require gcd(D_F,q)=1 for a fixed public modulus q; this arithmetic restriction is not used in the probability proof. For every s>0 and an ORIGINAL fresh draw X~D_(F,s), including X=0,

    p(F,I,s) := Pr[0!=X in FI]
              = [rho_s(FI)-1]/rho_s(F)
              <= min(1, 2/M+(32n/s)^n)
              <= min(1, 2/M+(256n/s)^n).                 (T1)

The same probability estimate, without its descent interpretation, holds for every nonzero integral I of norm M, whether prime or not. No basis-quality, smoothing, average-ideal, or randomized-ideal assumption is required. The estimate concerns the full infinite Gaussian law.

For X!=0, define C=(X)F^-1, let d be the least positive integer such that I''=dIC^-1 is integral, and retain every failure and zero in the original experiment. Strict norm descent N(I'')<M requires 0!=X in FI. Thus (T1) also bounds strict descent in this exact one-step procedure. Reaching the eligible family, obtaining a nonzero second sample, or imposing a norm threshold can only decrease its original success probability.

The coefficient Gaussian oracle is conditional: for each eligible ordinary-basis input F and declared width s it returns the stated centered law, or a law at explicitly declared total-variation distance epsilon from it. Availability of this oracle is a premise. The conditional A/B/C/quantum chain motivating that premise, and its finite coherent implementation, are separate dependencies. This theorem neither calls an oracle outside its family nor supplies a short basis as advice.

For an adaptive version, fix a deterministic cap T on the number of draws. Let H_(j-1) contain the complete generated history before draw j, including all earlier returned values, stopping decisions and algorithm coins already sampled. A predictable activity indicator A_j and the parameters (F_j,I_j,s_j) are measurable in H_(j-1). The ideals obey the preceding conditions on every active history. Conditional on H_(j-1), the next unused fresh draw has law D_(F_j,s_j), or a kernel Q_j at TV distance at most a predictable epsilon_j from that law. This conditional contract holds almost surely in the actual experiment. It is a full-kernel premise, not a marginal promise after averaging hidden states.

Write B_j=min(1,2/N(I_j)+(32n/s_j)^n). Then, almost surely,

    Pr[A_j=1 and 0!=X_j in F_j I_j | H_(j-1)]
       <= A_j min(1,B_j+epsilon_j).                     (T2)

For any selection rule that, after observing any or all of these draws, retains an arbitrary subset S of the active indices, including randomized rules and stopped rules,

    Pr[at least one retained alignment]
       <= min(1,E sum_(j=1)^T A_j min(1,B_j+epsilon_j)). (T3)

The expected number of retained alignments is bounded by the same expectation before taking min(1,...). The right side pays for ALL active draws, not merely the number selected afterwards. In particular, if N(I_j)>=M_min, s_j>=s_min, and sum_j A_j epsilon_j<=E_tot almost surely, it is at most

    min(1,T[2/M_min+(32n/s_min)^n]+E_tot).              (T4)

No product bound for selected events is asserted. If a complete ideal-experiment/implemented-experiment TV comparison is desired, assume the corresponding kernel contracts also on every history reached by either experiment and deterministic per-stage bounds epsilon_j; then ordinary sequential coupling gives full transcript TV <=sum_j epsilon_j. All public postprocessing, including failure labels, obeys the same bound.

For a single fixed input, rejection of zero CHANGES the exact law: conditional on X!=0 the alignment probability is

    [rho_s(FI)-1]/[rho_s(F)-1].                         (T5)

Repeating the exact original oracle to obtain one nonzero draw has expected cost rho_s(F)/(rho_s(F)-1); a bounded implementation must count all attempts and failure mass. Conditioning on an arbitrary success/selection event of probability a>0 uses its actual normalizer and can inflate any original event bound by as much as 1/a. No version of (T1) is claimed unchanged after such conditioning.

For fixed 0<rho<1, M>2^(rho n), and s>=512n^2, (T1) is at most 2^(1-rho n)+(16n)^(-n). Polynomially many attempts and negligible total oracle error therefore have negligible total one-step descent probability. The abstract oracle assumptions alone do not force s>=512n^2. The separate parameter companion checks it for the actual concrete A/B/C parameter choice and keeps every width conversion explicit.

Resource claim: this is an analytic estimate, not an exact finite-machine Gaussian sampler. Given a returned finite-bit X, ideal arithmetic and membership/clearing checks use ordinary polynomial-bit lattice arithmetic. The bound does not make a rare-event retry procedure run in polynomial time. The constructive short-combination test is a separate statement and cannot be substituted into (T1) as if its selected combination were a fresh Gaussian.
