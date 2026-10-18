# D-R1-H: a useful homogeneous output map already distinguishes ordinary RLWE

Frozen 2026-10-17. Status PROVISIONAL, pending nonauthor review. The decisive observation was supplied by A after reading the D-R1 interface. This note does not claim existence or efficient discovery of the required map. It shows why that missing construction cannot simply be assumed in a reduction from the same ordinary-RLWE hypothesis.

## Frozen statement

Let N ordinary RLWE samples over R_q=F_q[X]/(X^n+1) have common uniform secret s and independent coefficient errors D_a, versus independent uniform pairs. A public polynomial-time procedure, depending only on multipliers and local coins, may select a unit pivot a_0, m distinct designated multipliers a'_1,...,a'_m and their ratios r_j=a'_j/a_0. Write R for the stacked coefficient multiplication matrices M_rj. Suppose on a public event E, of probability pi, it outputs a p-by-m matrix K over Z[X]/(X^n+1) satisfying:

1. K R=0 as an integer coefficient matrix (the weaker congruence K R=0 modulo q also suffices for this lemma).
2. K modulo q is surjective from R_q^m to R_q^p, equivalently it has rank p at every CRT coordinate.
3. Its coefficient operator norm is at most kappa.

Let j0=np and choose an integer b with0<=b<q/2. Then the public test accepting exactly when E occurs and every centered coefficient of K b' lies in[−b,b] has advantage at least

    pi [1−2j0 exp(−pi_math b²/(a² kappa²))−((2b+1)/q)^j0],

where pi_math denotes the usual circle constant and pi denotes Pr[E]. A negative lower bound is vacuous. For kappa=0 no surjective map with p>=1 exists, so only kappa>0 is relevant. The comparison uses the actual full uniform sample endpoint and does not require an ideal source, Gaussian leakage, or source masks.

## Proof, including the selected-public-data conditioning

Condition on all multipliers, public coins, the selected indices and K on a positive-probability E branch. The designated errors remain independent D_a because the entire selection is response/error independent. Ring-linearity and the definition of the ratios give

    K (a'_j s)_j = K (r_j a_0 s)_j =0 modulo q.

Thus the planted processed response is exactly K e' modulo q. Under the comparator, designated responses remain independent uniform after the same conditioning; surjectivity of K makes K b' exactly uniform in R_q^p. If the public procedure selects indices adaptively using only the multipliers, the same conclusion holds because all responses are independent uniform conditional on the complete multiplier tuple. The event E has the same probability in both worlds.

For X~D_a on Z, completing the square and using maximality of the centered shifted theta mass gives

    E exp(t X) <= exp(a² t²/(4pi_math)).

Independence gives the same inequality with a²||v||² for a linear form v e'. Optimizing the Chernoff parameter yields

    Pr[|v e'|>b] <=2exp(−pi_math b²/(a²||v||²))
                  <=2exp(−pi_math b²/(a² kappa²)).

Every row of K has norm at most kappa. Union bound over j0 rows shows the unreduced planted vector lies in the box with probability at least1−2j0 exp(−pi_math b²/(a²kappa²)). On that event, because b<q/2, centered reduction retains the same vector. This is only a lower bound on planted acceptance; additional wrapped values can also be accepted. The uniform acceptance conditional on every successful public branch is exactly((2b+1)/q)^j0. Average over E to obtain the stated advantage. No success-conditioned error law or independent marginal product is substituted.

## Consequence for the anisotropic escape

For any delta in(0,1), choosing

    b=ceil(a kappa sqrt(log(2j0/delta)/pi_math))

gives planted box failure at most delta. If this b is much smaller than q and the public success probability is nonnegligible, the above test is a nonnegligible ordinary-RLWE distinguisher. In particular an efficient K with the small a kappa scale needed by D-R1's prospective subgaussian output masks would generally distinguish the input assumption directly. This is a concrete circularity check, not merely a statement that finding relations resembles SIS.

The required useful-width comparison must be made for each claimed downstream parameter family; no universal threshold is asserted beyond the displayed finite bound. Extremely rare public success, a wide map, a map chosen using responses, nonsurjective outputs, or changed input distributions are outside this statement and require their own endpoints. Nothing here rules out a mechanism that avoids these hypotheses. No failed relation search proves source or target security.

No new experiment was run. The proof is an analytic consequence of exact Gaussian moment bounds and the public-selection law. Source hardness remains OPEN.
