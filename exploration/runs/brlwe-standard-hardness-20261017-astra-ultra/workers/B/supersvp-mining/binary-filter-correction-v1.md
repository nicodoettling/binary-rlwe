# B-SUP-BIN v1 — two concrete binary Fourier follow-ons

Status: PROVISIONAL negative/conditional analysis, not a general impossibility theorem. Requested by root after the uniform-secret ring quantum repair. The current source-hardness goal remains open.

## 1. Canonical hint correction preserves an augmented equation only

Use the exact public law from ideal-ring-sis-theorem-v1: A in Rq^m, W in Rq^k and canonical T with [A|W]T=G. For a measured Fourier vector x, let r=Ax. Bit-decompose r using the coefficient-expanded gadget. Applying the corresponding expanded T gives a correction (u,v) satisfying

  A u+W v=r.

The actual corrected vectors obey

  A(x-u)=Wv,
  [A|W](x-u,-v)=0.

Thus the public hint corrects into the AUGMENTED kernel. It does not give an A-only relation. Conditioning v=0 has not been shown efficient; ignoring v changes the equation. This is true in both the planted and uniform response worlds because it is an identity of the full public tuple.

The ideal construction has a private augmented lift

  Qaug=[Q | V S+C/q] in (J/q)^(m+k),
  q Qaug=[A|W] mod q.

Therefore the augmented relation DOES lift into J. But its W contribution includes C/q=B', which approximates the quotient bit-generators g_l. These generators can have size comparable to D, and the one-vector norm theorem deliberately bounded only Q. A canonical hint of polynomial width does not control the magnitude of B'v. Declaring the augmented lift short would drop an explicit exponential-in-logD term.

There is a precise possible repair condition: if sum_l g_l v_l belongs to J, then subtracting this known ideal vector from the augmented lift leaves only the rounding errors B'-g and the Gaussian/mask part. Enforcing this extra quotient constraint on the W-coordinates amounts to sampling short preimages in the simultaneous kernel of the public gadget equation and a map into R/J. No short trapdoor or efficient sampler for that extra lattice has been supplied. The ordinary basis of J permits dense corrections, whose size must be charged. This is the missing algorithm, not an assertion that the algebraic repair is impossible.

A useful control is that the augmented public hint already yields short augmented kernel vectors without any binary oracle: for example, correct a coordinate vector's residual. If its private augmented lift were automatically short, the same construction would solve the restricted ideal problem without the recovery oracle. The unbounded quotient-generator contribution is therefore load-bearing.

## 2. Repeating the binary Fourier filter: exact state and success

For y in Fq^n define

  K(y)=2^-n sum_(b in {0,1}^n) exp(2pi i<b,y>/q)
      =product_j (1+exp(2pi i y_j/q))/2.

Given a normalized state sum_x psi_x |x>, prepare a fresh uniform binary ancilla, apply the controlled phase with y=L_A^T x, Hadamard the ancilla, and postselect its all-zero outcome. This implements the contraction

  |x> -> K(L_A^T x)|x>.

After t successful filters the UNNORMALIZED state is

  sum_x psi_x K(L_A^T x)^t |x>,

with exact success probability

  P_t=sum_x |psi_x|^2 |K(L_A^T x)|^(2t).

Let w_A=sum_(L_A^T x=0)|psi_x|^2. Every desired kernel amplitude is unchanged before normalization. For nonzero y, some coordinate satisfies

  |K(y)|^2<=cos^2(pi/q)<=exp(-4/q^2),

using sin(pi/q)>=2/q. Consequently

  w_A <= P_t <= w_A+exp(-4t/q^2),
  Pr[kernel | all filters accept] = w_A/P_t.

With polynomial-value q, t=O(q^2(n logq+log(1/eta))) can make the conditional state almost a kernel state. The UNCONDITIONAL kernel probability remains exactly w_A. If the starting state is the independent Gaussian Fourier state, the shared-key moment theorem gives E_A w_A<=K1/(alpha0 q^n). Making the filter narrow does not raise this mass. Even coherent amplitude amplification costs on the order of 1/sqrt(P_t), which is exponential when P_t is on the q^-n scale. This is a normalization/postselection obstruction to this concrete implementation, not a ban on other binary algorithms.

If the starting state is the binary recovery circuit's postselected state v, the oracle hypothesis gives overlap with the broad binary comparison state, not a lower bound on w_A. The frozen quantum proof bounds the comparison state's kernel energy by (2/q)^n K1/alpha0. A diagonal repetition filter cannot create missing kernel amplitude: it preserves those amplitudes and discards others. No polynomial success bound follows from recovery advantage alone.

## 3. Summing binary secrets does not reverse the oracle direction

The sum modulo q of t independent binary secrets approaches uniform after a random-walk mixing time. Likewise, summing their genuinely planted responses produces the corresponding sum-secret law with enlarged/correlated discrete error convolution. These are FORWARD distribution statements. A solver for individual binary instances does not supply a solver for an aggregate challenge: decomposing a supplied aggregate response into independently planted component responses requires the hidden secret/error posterior. Choosing arbitrary component responses makes the binary recovery queries off-promise.

Coherent preparation of a sum distribution does not remove that missing challenge decomposition. A construction that retains component response registers must either keep their full entanglement or prove a valid uncomputation/postselection bound. No such bound is established here. In particular, the t binary-recovery successes may not be multiplied without conditional evidence on every selected history.

## Current next edge

Two concrete open obligations remain: an efficient short joint preimage sampler enforcing the extra R/J quotient constraint, or a binary-recovery quantum construction that transfers inverse-polynomial success to the exact ring kernel without q^-n postselection. The present canonical hint and repeated diagonal filter do not by themselves furnish either obligation.
