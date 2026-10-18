# D-SREL-NTRU-1: exact principal-source and NTRU endpoint audit

Status: provisional nonauthor-discovery packet, no acceptance or foundation claim. Written 2026-10-17. Owned assignment short-relation-source/assignment-v1.md. This mathematical control uses no local experiment.

## 1. Frozen public and latent law

Let n be a power of two, R=Z[X]/(X^n+1), q an odd split prime, and nu a specified distribution on nonzero ternary f of weight at most w, conditioned on gcd(|N(f)|,q)=1. The conditioning is part of nu; its sampling cost is not assumed negligible. Set J=fR, publish its canonical integer HNF, and erase f from the oracle interface. The reduction/key generator knows f only when it sampled nu itself. A received NTRU challenge does not supply f or J.

Let pi_q be reduction of rational coefficients with denominators prime to q. It identifies J^-1/qJ^-1 with R_q. For k samples the desired two complete laws, with latent values displayed, are

P=(f,J,(a_i,A_i)_{i<=k}), f~nu, a_i|f iid D_(J^-1,s), A_i=pi_q(a_i);
Q=(f,J,(A_i)_{i<=k}), f~nu, A_i|f iid U(R_q).

Only (J,A_1,...,A_k) is public. In P, a_i are independent conditional J, and their conditional distribution depends on f only through J. The scalar s and sample count k are fixed public parameters. Fresh binary S and response errors, if used downstream, must be independently sampled conditional all this source state; none are present in P or Q above.

For x in J^-1/qJ^-1,
P[A_i=x|f]=rho_s(x+qJ^-1)/rho_s(J^-1).
The full product uses this SAME J. One cannot replace it by a product of marginal laws in which denominators are resampled.

## 2. Exact numerator change of variables

Multiplication M_f bijects J^-1 onto Z^n. Therefore g_i=f a_i has probability
  exp(-pi ||M_f^-1 g_i||²/s²) / sum_(g in Z^n) exp(-pi ||M_f^-1 g||²/s²).
This is an elliptical integer Gaussian with width-square matrix s² M_f M_f^T. Here width-square specifies the exponent; it is NOT asserted equal to the actual moment covariance of a discrete Gaussian.

Conversely, if ordinary NTRU samples g_i iid D_(Z^n,sigma) independently of f and publishes h_i=pi_q(f^-1 g_i), then before reduction a_i=f^-1g_i has density proportional to exp(-pi ||M_f a_i||²/sigma²). Its width-square matrix is sigma² M_f^-1 M_f^-T, in general anisotropic. The numerator law needed for spherical FG depends on f. Conditioning g_i to be a q-unit adds another restriction absent from FG.

The uniform endpoint itself is exact: for every allowed f, g_i iid uniform R_q implies f^-1 g_i iid uniform R_q, independent of f and J. It does not repair the planted law.

Even a theorem for marginal h_i does not justify retaining J. Appending J=fR from an unknown-denominator challenge requires its correct posterior joint law. Sampling an independent J' is a different law. Moreover, ordinary NTRU with one h does not automatically give k independent numerators under the SAME f. Reusing an h or multiplying it by public randomness needs a separate joint-law proof.

## 3. Finite hand falsification, including the modular endpoint

Take n=4, f=1+X, q=17, s=1. Then N(f)=2 and f is a unit modulo17. The two integer numerators g_+=1+X and g_-=1-X have identical probability under D_(Z^4,sigma), for every sigma, including after reduction mod17: coefficient reflection bijects all their lifts and preserves the spherical density.

Their preimages are
  f^-1 g_+=1,
  f^-1 g_-=-X+X²-X³,
with squared coefficient norms1 and3. Thus their unperiodized spherical-FG weights are e^-pi and e^(-3pi), unequal.

This difference survives modulo17. For either a in these two preimages and z in Z^4 nonzero,
  ||a+17 f^-1z|| >= (17/2)||z||-sqrt(3) >= 6||z||,
because ||M_f||op<=2. Consequently the total extra weight over nonzero lifts is at most
  sum_(z!=0) exp(-36pi||z||²)
  = (sum_(r in Z)exp(-36pi r²))^4-1 < 1/1000.
For the last elementary bound, pi>3 and e>2 imply the scalar nonzero tail <=2 sum_(r>=1)2^(-108r)<2^-106; expanding the fourth power gives the displayed coarse bound. Meanwhile pi<4, e<3 imply e^-pi>1/81, and pi>3,e>2 imply e^(-3pi)<1/512. Hence
  e^-pi > e^(-3pi)+1/1000.
After division by the same positive rho_1(J^-1), the two target residue probabilities differ. Ordinary spherical-numerator NTRU gives them equal probability. This is an exact finite counterexample for ALL scalar sigma, not a Monte Carlo discrepancy or a claim about useful asymptotic widths.

## 4. Knowledge and shortness

If f is public, or efficiently recovered from J, then for one desired source sample the centered coefficients of fA are small with high probability. For any U>0, the Gaussian shifted-mass bound gives
  Pr[||f a||infty > s sqrt(w) U] <= 2n exp(-pi U²).
Under Q, fA is exactly uniform since f is a q-unit, and the box has mass at most min(1,((2 floor(s sqrt(w)U)+1)/q)^n). This provides a distinguisher in a useful narrow-width regime. The bound uses that each row of M_f has norm sqrt(w). It does not claim f can always be recovered efficiently from HNF(J).

The short relation is hidden from the distinguisher but known to a reduction that generated it. Such private knowledge is permitted. It does not create a standard hardness reduction: a simulator that independently generates (f,J) and FG samples has not used its incoming challenge to program the planted/uniform choice.

## 5. Exact source-interface failures

(a) Independent spherical NTRU numerator: rejected by Section3.
(b) Retain J without a conditional simulator: unresolved extra information, not justified by marginal ratio pseudorandomness.
(c) Publish f to fix the simulator: source becomes distinguishable under Section4's parameters.
(d) Replace f by a broad Gaussian to use provable NTRU key generation: removes the required sparse ternary relation; the provisional sparse guessing lemma no longer applies.
(e) Use an arbitrary NTRU short-vector oracle as a decision oracle: different computational task. Published source edges are recorded separately in the primary ledger.

No general impossibility is asserted for f-dependent numerator programming, class-changing maps, or a different hidden-relation family. No source hardness is established here.
