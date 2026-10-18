# RF2 exact review: B bounded wrapper and fractional bounded composition v1

PROVISIONAL nonblind review. Exact author hashes freshly matched:

- gaussian-periodic-bounded-wrapper-v1.md: 335f4a176331df262eda5c775a7d565e3c47fee6413d714957741c81b6087521.
- fractional-bounded-composition-v1.md: 6ff55f5926ae639deb30985f009a3898a2da05e1accab4682e022c258122f225.

Verdict: both packets survive the full endpoint, finite-cap, fresh-secret, and adaptive-composition audit. B's accepted expected-time bridge is used only in that accepted scope. C's actual primary finite T_H contract remains OPEN and is an explicit dependency of the final conditional BDD conclusion. No source hardness is inferred.

## 1. B wrapper: counts and both endpoints

Each coset choice has at most n nontrivial invariant-factor draws. Each of kn scalar samplers makes at most L uniform interval proposals. Since ln x<log_2 x for x>1 and Lplus is an integer, L=ceil(40K ln(16/nu))<=40K ceil(log_2(16/nu))=Lplus. Thus Umax=kn(1+Lplus) is a deterministic bound, including every reached scalar trial.

For an interval of cardinality M>=2, a b=ceil(log_2 M)-bit proposal is accepted with probability M/2^b>1/2 (or exactly 1 for a power of two). Conditional on every earlier history, the probability that Bcap proposals all reject is at most 2^(-Bcap). Couple capped and uncapped implementations using the same random tapes. They agree until the first exhausted elementary loop. The union bound over at most Umax opportunities gives an input-uniform disagreement probability at most eta, without assuming a product law for any selected histories. Returning a fixed valid value preserves the domain but need not preserve uniformity.

Apply the same coupling pointwise and then average over each complete input experiment. Planted distance to FG is at most Delta_B+eta; comparator distance to uniform FG is at most eta. Appending an arbitrary common randomized FG distinguisher cannot increase either distance. Therefore the advantage loss is Delta_B+2eta. Exact comparator equality is correctly reserved for the uncapped map. No unconditional finite-fair-bit exact uniform sampler on an odd-order quotient is assumed.

All random loops in this wrapper are now capped. The unchanged exact logarithmic ceiling has the independently checked BT4 integral implementation (RF2 b-v2-log-ceiling-recheck-v1.md). Full scalar input encodings and sample-representative bit lengths remain charged. A bounded downstream algorithm is still needed for a bounded composite.

## 2. A-to-B complete target wrapper

For every fixed J and every supplied GP tuple, the implementation samples fresh S uniformly in {0,1}^n and target-noise coins independently of J, source samples, B's coins, and Rec's coins. The target errors are scalar D_sigma approximations with total product distance at most kn nu. S is retained only for testing the returned answer against the actual sampled secret. A's proof-only G,H and short-basis witness are never supplied to the algorithm. This preserves CP1 and the actual conditional guessing argument.

Before elementary-loop capping, the comparator multipliers are exactly uniform and independent conditional on J. Its completed law is within kn nu of the exact binary recovery target. The planted law is within Delta_B+kn nu of A's exact fractional-Gaussian completion. Thus the endpoint sums cost Delta_B+2kn nu, in addition to A's delta_tail+beta+eta_A. This accounts for exactly THREE copies of kn nu after expanding Delta_B: one for B's planted scalar approximation and one in each completed endpoint. There is no omitted comparator charge.

The simultaneous cap covers both B's and the target sampler's uniform interval proposals. The common nu gives K=ell^2+6 and Lplus=40(ell^2+6)(ell^2+4), so Uall=kn(1+2Lplus) covers all required uniform draws. With Bcap=ell^2+ceil(log_2 Uall), Uall 2^(-Bcap)<=2^(-ell^2)=eta. Its whole-call coupling error is at most eta separately in BOTH worlds. The resulting displayed delta_C therefore subtracts exactly 2eta, not two independent full-wrapper charges in each world.

The geometric window also checks: tau2=2n^2 covers n^2 D^(1/n); sigma>=2ts sqrt(kn)ell follows from 8ceil(sqrt(kn))>=4sqrt(2)sqrt(kn). The stated beta is an upper bound on D_max p_t^n using rho_t(Z)>=t and (1+1/t)^n<=exp(n/t). The uncapped tail bound used in the packet is a valid upper bound even where a minimum with 1 would be tighter. The chosen r_B satisfies B's smoothing sufficient condition, as detailed in A's parameter packet. All these losses are negligible for fixed rho<1 and polynomial k.

If Rec discards J, its exact comparator recovery success is the same epsilon_rec for every J. The ideal fractional-completion upper bound is also pointwise in J. Consequently a positive numerical delta<=delta_C gives the required same-J gap. An averaged recovery or ideal-family advantage would not imply this statement, and the packet correctly excludes that inference.

## 3. Why the advantage loss is not multiplied by Q_*

Fix the complete capped circuit just analyzed. It is ONE actual GP distinguisher; its exact acceptance function supplies C's oracle. The inequality establishing its initial gap is an inequality about that circuit's two source acceptance probabilities. C calls that same circuit, with fresh independent coins on each invocation, so the circuit has not been replaced by an idealized version at every query. Therefore Delta_B+2kn nu+2eta enters the numerical gap once. Multiplying this source-gap loss by Q_* would analyze a different, unnecessary hybrid.

In contrast, C's comparisons between its physically generated query distributions and its analysis oracle must retain the conditional-on-history per-query bounds and the stated global Q_* / summable precision budget. Those are separate losses. The composition packet keeps them separate. Both global orientations and malformed/off-promise queries remain bounded because the capped inner algorithm and Rec have declared worst-case bounds on all valid inputs.

## Disposition

B-BND v1: endpoint/running-time corollary survives. Fractional bounded composition v1: survives conditionally on A and the declared C primary finite implementation contract. Imported regressions retain their prior scope dispositions; this adds controls for odd-order finite-bit fallback, both-endpoint cap loss, fresh S/noise independence, and the distinction between establishing a fixed oracle's gap and approximating its adaptive queries. Standard low-index source hardness and the original computational foundation remain OPEN.
