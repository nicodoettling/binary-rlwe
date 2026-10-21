# DD1-EXTRACT-v1 complete candidate proof

Status PROVISIONAL. Exact theorem and finite algorithm in extraction-theorem-v1.md. This proof is for ordinary rank-one ring samples, without the old decomposed-input root-rank failure term.

## 1. Exact CRT transformation law

Condition on a fixed secret s. For one raw sample, A is uniform in R_q, E has the target law independently, and p is independent uniform in F_q. The map (A,p)->(A'=A+p e_j,p) is a bijection of R_q x F_q. Therefore A' is uniform and independent of p, E, and every fresh prefix mask W. Algebraically,

    B'=A s+E+t p e_j+W
      =A' s+E+(t-s(r_j))p e_j+W.

If t=s(r_j), the last added root-j term is0, giving exactly hybrid j-1. If t differs, multiplication by its nonzero difference permutes F_q, so the term is independent uniform at root j, giving exactly hybrid j. This is a statement about the FULL coefficient-error joint law: no CRT-coordinate independence of E is needed or asserted. Independence of the physical A,p,E,W variables across raw samples gives the k0-sample product law conditional on this fixed s. The secret is never shifted or resampled.

## 2. Calibration concentration despite bank reuse

Condition on s. For each fixed j, the Ncal block outputs are iid Bernoulli of mean p_j(q,s): the raw blocks are disjoint and their errors/public multipliers are independent conditional on s; transformation and D coins are fresh. Different j estimators share raw blocks and may be dependent. Hoeffding applies separately to each estimator, and a union bound gives

    Pr[C^c | s] <= 2(n+1) exp(-2Ncal a²) <= eta/2,

where C is the event that every p_hat_j differs from p_j by at most a. The displayed Ncal suffices because 2Ncal a² >= Lcal >= ln(4(n+1)/eta). No independence between the n+1 estimators is used.

If |p_0-p_n|>=epsilon/2, telescoping and the triangle inequality give max_j |p_(j-1)-p_j|>=epsilon/(2n). On C the maximal empirical gap is at least epsilon/(2n)-2a=15epsilon/(32n), so the threshold cannot cause FAIL. For any selected j that passes the threshold, C gives actual separation

    g=|p_(j-1)-p_j| >= epsilon/(4n)-2a=7epsilon/(32n)>4a.

This latter bound holds even for secrets outside the good set.

## 3. Fresh test bank and simultaneous correctness for all guesses

Now condition on s and the complete calibration transcript. The selected j and calibrated means are fixed. The raw test bank is independent of the calibration bank conditional on s. For each fixed t, its Ntest transformed block outputs are iid Bernoulli; section1 identifies their mean as p_(j-1) for the unique correct t and p_j for every wrong t. Across different t, the reused test bank causes dependence, which is allowed. A conditional union bound gives

    Pr[T^c | s, calibration] <= 2q exp(-2Ntest a²) <= eta/2,

where T means every query mean differs from its appropriate true endpoint by at most a. This inequality holds for every selected j and every positive-probability calibration transcript. If the calibration stage returns FAIL, the test stage can be skipped and the bound is trivial.

On C and T with the threshold passed, the correct t is at distance at most2a from its calibrated correct endpoint and at least g-2a>2a from the other endpoint. Every wrong t has the reverse strict comparison. Hence exactly the correct t is marked, and the output is correct. Consequently an incorrect pair requires C^c or T^c, proving E1. On every good fixed secret the threshold also passes, proving E2. The only product/conditioning argument used here is the explicit independence of the TWO physical raw banks conditional on s; reuse within a bank is handled by simultaneous events and additive union bounds.

## 4. Absolute and averaged decision advantages

Let random X=d(q,S), where q is fixed or chosen from the supplied list. In the averaged case,

    E_(q,S)|X| >= E_q |E_S X| >= epsilon.

Since |X|<=1, the event G={|X|>=epsilon/2} has probability at least epsilon/(2-epsilon)>=epsilon/2: E|X|<=Pr[G]+(1-Pr[G])epsilon/2. The same calculation applies to fixed q. Combining the pointwise good-secret success with the total error bound yields Pr[correct selected pair]>=Pr[G]-eta>=epsilon/2-eta. The sign of the decision advantage need not be known, and no two-output list or extra factor2 is used.

## 5. Source count, fair-bit caps, and scope

The calibration bank has k0 Ncal physical samples even though it is reused n+1 times; the test bank has k0 Ntest even though it is reused q times. Thus K=k0(Ncal+Ntest) while the actual D call count is N_D=(n+1)Ncal+qNtest. This distinction affects the inherited rectangular Gaussian completion norm and its noise width.

At calibration prefix j each sample needs j independent F_q mask values. Summing j=0,...,n gives k0 Ncal n(n+1)/2 field draws. Every test call needs one p and j-1 prefix values per sample, at most n, giving at most k0 n q Ntest. Each uncapped rejection draw has success probability q/2^ceil(log2q)>1/2, so its first B attempts all fail with probability at most2^-B. Couple capped and exact draws until the first cap failure. A union bound over at most Tfield attempts gives full output TV<=Tfield 2^-B<=nu, for every raw input and every adaptive history. This is a failure-event coupling, not a claim that capped draws remain exactly uniform.

Exact integer/rational arithmetic computes all displayed finite bounds. A fixed bounded D_q code makes every repeated call bounded, including calls that are not target-distributed. The theorem's success premise is used only for uniform-A raw inputs; its downstream fractional-source analysis is an information bound on the resulting complete output and must not reuse the uniform-A conditional-law proof there.

Dependencies: elementary CRT over the split prime; Hoeffding's bounded independent-trial inequality; the target decision premise. The old selected-root note supplies context but not a needed unverified rank hypothesis. Finite falsification and nonauthor/blind review are pending; no ACCEPT is claimed.
