# A-FRAC -> bounded B-GP -> C-BDD: explicit parameters

Status: PROVISIONAL composition, conditional on the exact A-FRAC theorem/proof, B GP-v2 plus bounded-wrapper, and C multiplier-OHCP-v5 and its finite primary contract. No low-index worst-case hardness theorem is inferred. This packet changes no other worker's artifacts.

Fix rho<1, polynomial sample count k, and

  ell=ceil(log2(2nk)),
  tau2=2n², t=2n²ell,
  r_B=w_B=ell², s=sqrt(2)ell²,
  sigma=8n² ceil(sqrt(kn))ell^4,
  epsilon_B=nu=2^(-ell²), P=2^(2ell²), eta=2^(-ell²).

Let J be supplied with D<=2^(rho n) and gcd(D,q)=1. The target meaningful-noise condition is q>=n^c sigma for a fixed c>0; q may be any supplied split prime satisfying it. All scalar encodings here have polynomial length. A's existence-only short-basis geometry is used solely in its proof; no such basis is supplied or sampled by the reduction.

Define

  beta=min(1,exp(-(1-rho)n ln2+1/(2n ell))),
  delta_tail=4kn exp(-pi ell²),
  Delta_B=2k epsilon_B/(1-epsilon_B)
             +2pi kn/(P r_B)+kn nu.

Let eta_A be A-FRAC's explicit completion error from its theorem (the parameter packet proves it negligible). Let Rec be a bounded-time binary recovery algorithm with success epsilon_rec on the exact target, and let its runtime be bounded on every valid input.

One GP challenge call is mapped by B-v2 to ring multipliers. Then sample n fresh uniform bits S and kn target coefficient Gaussians, each approximated by the same scalar sampler to error nu. Invoke Rec and test its result against S. The exact unbounded rejection implementation has GP distinguishing advantage at least

  epsilon_rec-delta_tail-beta-eta_A-Delta_B-2kn nu.

This is A's displayed W4 with the target-sampler charge written separately. To make the WHOLE call bounded, use

  K=ell²+6,
  Lplus=40(ell²+6)(ell²+4),
  Uall=kn(1+2Lplus),
  Bcap=ell²+ceil(log2 Uall).

There are at most kn coset uniform draws, kn Lplus B scalar proposals and kn Lplus target scalar proposals. Capping EACH elementary uniform draw at Bcap attempts gives a coupling discrepancy at most eta on every complete call/input. The bits S and dyadic Bernoulli coins already have fixed lengths. Thus the fixed bounded GP distinguisher has absolute advantage at least

  delta_C := epsilon_rec-delta_tail-beta-eta_A
              -2k epsilon_B/(1-epsilon_B)
              -2pi kn/(P r_B)-3kn nu-2eta.

Choose any explicit positive lower bound delta<=delta_C as C's declared advantage parameter. If epsilon_rec is inverse polynomial and the preceding negligible terms are smaller than epsilon_rec/2, delta=epsilon_rec/2 is permissible. The pointwise advantage is the same for every admissible J when Rec discards J; an average-family guarantee alone does not imply this pointwise statement.

For C's canonical embedding set

  w_C=sqrt(n) w_B=sqrt(n)ell²,
  Lattice=qJ^-1,  grid=1/(DP).

Apply C-v5 with this w_C, the SAME grid, k and supplied J, and the bounded distinguisher above. Its parameter procedure chooses v0 and yields canonical BDD radius

  d0=delta w_C/(32nkv0).

For v0>=2sqrt(n)a, this is at most delta ell²/(64nka); the actual chosen v0 and all uniqueness conditions are retained from C. Its success is at least1-(n/2)exp(-kappa)-zeta and it makes at most Q_* calls. Each call now has a strict polynomial bound on every input, including queries from the incorrect orientation. The two-sided cap loss2eta is already part of delta; it is not multiplied again by Q_* because this bounded algorithm is the actual oracle used throughout. C's own physical/comparison/numerical query errors remain separately budgeted as in its theorem.

The final conclusion is a conditional BDD algorithm for the SAME supplied low-index ideal family. It is not a proof that this family contains arbitrary worst-case ideal lattices, not a standard source-hardness import, and not a completed computational foundation. The primary OHCP finite implementation contract and every provisional theorem dependency retain their review status.
