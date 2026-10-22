# BLIND-FF2 probability and conditioning audit

This audit accompanies `independent-report-v1.md` and uses the same frozen inputs. Its purpose is to specify the actual joint laws and conditioning, including the branches where a sequential argument could fail.

## Ambient law and filtration

Draw S once, uniformly from coefficient-binary vectors. Conditional on S=s, all K raw pairs have A_i uniform in R_q and E_i independent from the exact product coefficient Gaussian, with B_i=A_i s+E_i. All A_i, error coefficient variables, transformation tapes, and D execution tapes are mutually independent conditional on s. D's tapes are fresh at every call. S is not redrawn for any block, candidate, prefix, or stage.

Each stage has a calibration bank and a test bank of disjoint raw samples; stages have disjoint banks. For a fixed s, F_{l-1} exposes previous banks, their transformation and D coins, and the prior outputs. It does not expose future banks. This is a proof filtration justified by the specified algorithm's data dependencies, even if the raw input is physically stored as a whole. Every selected root set, stopping decision, and prefix is measurable in the past/calibration information specified below. No hidden cache-hit variable is added to the filtration.

For every positive-probability history h,

    Law(future banks | S=s,F_{l-1}=h)
      = product of their original conditional raw laws.

Indeed the Bayes numerator factors as Pr[F_{l-1}=h | s] times the product future-bank law, and dividing by the positive first factor restores that same law. Conditioning merely on F_{l-1}=h without fixing S may alter the secret posterior and need not leave unconditional banks independent. No such unconditional independence is used.

Zero-probability branches are excluded from conditional statements. If a branch has already stopped, it contributes zero to any event of a newly reached bad stage.

## Lemma-by-lemma audit

| Lemma | Random variables and exact conditional law | Selection/support issue | Valid bound and finite attack |
|---|---|---|---|
| Gaussian projection | E_i independent coefficient Gaussians; E_T is their deterministic linear image | T fixed first, or fixed after independent-history conditioning at fixed s | Characteristic function factors over coefficients, never CRT coordinates. Analytic theta/dual-norm proof plus 29 finite rational approximants. |
| Shift jointly with A | A uniform independent of E; B_T=A_Ts_T+E_T | Conditional on fixed A and s the shift is a bijection | TV equals projection TV; averaging over A does not increase it. Partial-endpoint finite enumeration includes the full joint pair. |
| Product-batch TV | Conditional on s, k independent pairs | Shared S makes unconditional pairs dependent; fix s first | Hybrid/telescoping replacement gives k tau. Fifteen exact tensor cases. No product of event probabilities. |
| Adaptive root-set projection | H is F_{l-1}-measurable; new errors independent of F_{l-1} at fixed s | Selection from the same error bank would change support | Pointwise fresh-bank law at every positive history. 130 exact independent-history cases and a deliberate same-bank bias 3/4 versus 1/2. |
| Partial endpoint | W_C independent uniform; endpoint error is (E_H,E_C+W_C) | E_H and E_C can be arbitrarily correlated | Conditional on full E, W_C kills all dependence in the C output. TV equals TV(E_H,U_H), including full A. Enumerated all 35 two-bit rational error laws, 560 secret/subset cases. |
| Candidate test | A uniform, p independent uniform, E arbitrary joint law; A'=A+pe_j | Replacing A must preserve dependence with all B coordinates | (A',p) remains independent uniform and independent of E. Correct t gives previous prefix, wrong t gives next prefix. 972 exact atom cases; mixtures follow by linearity. |
| Calibration concentration | For each fixed prefix, Ncal independent raw blocks and fresh tapes | Means across different prefixes can be correlated by shared raw blocks | Hoeffding for each mean, union over at most n+1 means. No independence across prefixes is asserted. Exact Bernoulli tails and 30,330 threshold perturbations. |
| Test concentration | Reveal all calibration values/tapes, then j and prefix are fixed; test bank remains fresh | Candidate selection is adaptive; means across q candidates share their test bank | Conditional Hoeffding for each candidate, union over q. Calibration success is not used as a substitute for conditioning on the full calibration history. |
| Stage union | Bad_l is measurable after stage l; H may depend on incorrect old results | Conditioning on old success can change old support; future-bank factorization persists at fixed s | At every reached history Pr[Bad_l | past,s]<=delta/(2r). E[1_reached Pr(Bad_l|past,s)] and sum over l gives delta/2. No sequential product is taken. |
| Bounded field sampler | Independent fair-bit chunks per draw; each draw accepts with probability >1/2 | Number and addresses of later draws may depend on earlier coins | Predraw enough tapes for Tfield draws, couple each to ideal rejection. Union of failures <=Tfield 2^-B<=delta/2 pointwise in every raw input. 72 exact finite samplers. |
| Good-secret measure | d(S) in [-1,1], one uniform S | Good-set measure must not be amplified by fresh secrets across banks | E|d|>=epsilon implies Pr[|d|>=epsilon/2]>=epsilon/(2-epsilon). 1,090 exact finite cases. Pointwise good-secret success then averages to >=epsilon/2-delta. |

## Constant ledger

With a=epsilon/(128n), 2a^2=epsilon^2/(8192n^2). The factor 8192 in each sample count is therefore sufficient for 2Na^2>=the displayed log2 ceiling. For L>=log2(8r(n+1)/delta), the total calibration failure is at most 2(n+1)e^-L<=delta/(4r); replacing n+1 by q gives the test-bank bound. Across r stages their sum is delta/2. Bounded field coins cost at most the other delta/2.

An empirical selected gap of 16a implies true gap >=14a. Candidate and own calibrated endpoint differ by at most 2a, while candidate and other calibrated endpoint differ by at least 12a. Thus marking is strict and unique. A good secret has endpoint difference >=epsilon/4 and some true adjacent gap >=32a; the observed maximum is >=30a and cannot trigger the 16a failure threshold.

All counts and inequalities remain valid as epsilon approaches zero; costs increase as the displayed inverse powers. They also remain valid for arbitrarily large fixed polynomial k, provided the explicit k tau condition eventually holds. There is no exponent-independent finite cutoff.

## Mandatory CP-1 rejection

The exact regression computes Pr[vk=1]=10/11, then posterior masses A_b=21/2000, C_b=1/20, D=879/1000. Initial query incidences are p(x)=1/10, p(e_b)=121/2000, and p(f_b)=21/2000. Strict heaviness means p>1/10, so none is heavy.

The designated two-hit event has probability sum_b (21/2000)/2=21/2000=0.0105, strictly larger than (1/10)^2=0.01. The later residual incidence 21/221 is below 1/10. The invalid inference is multiplying marginal or locally re-established lightness bounds after support restriction and Bayes renormalization. The same cached-prefix value can change component weights after sibling cylinders are removed.

Numerically, the problematic transferred first-stage mass rises from A+C=121/2000=0.0605 to A+2C=221/2000=0.1105. Its normalization yields A/(A+2C)=21/221 for the later incidence. Local lightness at that later point does not pay for the earlier increase.

The present extractor proof does not assert the forbidden product. It proves a pointwise bound under the actual fixed-s filtration, then uses an additive union bound. Its fresh-bank property is an explicit independence hypothesis, not an inference from local residual lightness. The deliberate same-bank regression exhibits precisely why weakening that hypothesis would fail.

## Evidence limitations

Finite negative searches supplement the analytic arguments; they do not prove unrestricted lemmas. Tests of Bernoulli exponential bounds use 80-digit arithmetic for exp. The Gaussian checks use exact rational truncated/rounded input laws and 80-digit evaluations of the proposed bound; they are not a substitute for the exact infinite-law theta proof. All primary analytic bounds used for certification are proved in the report. No statistical independence is claimed between model-based reviewers.
