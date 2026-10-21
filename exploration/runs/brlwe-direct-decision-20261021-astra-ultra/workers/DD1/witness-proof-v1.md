# DD1-WITNESS-v1 candidate proof

Status PROVISIONAL; exact statement in witness-theorem-v1.md.

For X~D_Z,r, shifted-theta maximality and square completion give E exp(hX)<=exp(r²h²/(4pi)). This is the one-dimensional specialization of OLD A-FRAC proof section 2, which proves the fact from Poisson summation. In particular EX=0 and EX²<=r²/(2pi).

For J=R the unwrapped constant coefficient of a_1 S+E_1 is

    T=a_(1,0) S_0-sum_(j=1)^(n-1) a_(1,j) S_(n-j)+E_(1,0).

Conditional on S, the independent Gaussian coefficient variables yield the MGF bound exp((sigma²+wt(S)s²)h²/(4pi)), hence the unconditional upper bound exp(Vh²/(4pi)). Chernoff gives Pr[|T|>=q/4]<=2exp(-pi q²/(16V)). Every integer T with |T|<q/4 is accepted after reduction modulo q; the centered interval has c_q residues. Thus the planted acceptance is at least one minus the displayed tail, while the uniform-response acceptance is exactly c_q/q. This proves W1 without conditioning on a Gaussian tail event or changing the source law.

For uniform A, fix any nonzero binary S. In the displayed coefficient sum at least one uniform coefficient of A has coefficient +1 or -1. Conditioning on all other coefficients makes T modulo q uniform. Adding E preserves uniformity. The sole exceptional S=0 occurs with probability 2^-n and leaves T=E. This proves W2, including the exact normalization and independence statement. Only the first sample is used, so arbitrary shared-secret grouping of the remaining k-1 samples is retained.

For the cosine score, conditional characteristic functions multiply because the a coefficients and error are independent given S. Symmetry makes the sign of each active a coefficient irrelevant. Averaging each independent binary bit gives the factor (1+phi_s(1/q))/2. The uniform-response cosine has mean zero, proving W3. Alternatively E T²=E E_0²+(n/2)E a_0²<=(sigma²+n s²/2)/(2pi), and cos x>=1-x²/2 gives W4 directly. This avoids assuming an unproved pointwise bound for phi_r.

The inherited parameter ratio is

    n s²/sigma² = 1/[32n³ ceil(sqrt(kn))² ell⁴] <= 1/(32n⁴ell⁴).

As q>=n sigma, the tail in W1 vanishes at least as exp(-Omega(n²)); c_q/q=1/2+O(1/q). The mixture identities are linearity of expectation and Delta_D0(P_FG)>=-1. No relationship between D0's behavior on the two multiplier laws is presumed.

Finite-support audit planned: exact rational enumeration of a symmetric three-point coefficient law at n=2 with common binary S and q=5,13, checking W2 exactly and separating planted/uniform response comparators. This finite control checks identities and grouping, not the discrete-Gaussian tail theorem. No sequential product bound is used; CP-1's warning applies only as a prohibition against replacing the conditional coefficient independence given the fixed S with an unsupported posterior assertion.
