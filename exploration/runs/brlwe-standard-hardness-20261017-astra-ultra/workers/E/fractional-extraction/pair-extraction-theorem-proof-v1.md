# Quotient collisions from multiple fractional Gaussian samples

Status: PROVISIONAL SCOPED OBSTRUCTION with a complete proposed proof. This is worker E's ONE tested extraction mechanism: choose two samples after seeing the whole list, then subtract them. It does not rule out general short combinations, output-dependent scalar division, lattice reduction, nonlinear processing of another kind, or a different source interface. No blind or independent review of this new statement has yet occurred.

## Frozen mechanism and finite claim E-PAIR-v1

Let n>=2 be a power of two, R=Z[zeta_(2n)] with its coefficient Euclidean norm, I,H nonzero integral ideals, D_I=N(I), D_H=N(H), and c>=1 an integer with cR contained in I. Put J=IH/c, L=I intersect J, and G=J/L. Fix W>0, gamma>=0, and a sample cap m>=2. Exact samples are iid X_1,...,X_m from D_(J,W), conditional on the identical fixed public ideal data. Any algorithm, even computationally unbounded and supplied arbitrary public advice, may inspect all samples, their quotient labels in G, and all norms. It either returns one signed pair difference X_j-X_i with i<j and equal labels, or fails. A useful output is nonzero, in I, and of norm at most gamma c. It may use its own independent coins.

Set

    b = min(1, D_H ((D_I^(1/n)/c+2gamma)/W)^n).

Then even the event that SOME pair, including a zero difference, is in I and has norm at most gamma c has probability at most

    min(1, binom(m,2) b).

Consequently every described selector's useful-output probability obeys that bound. This is not an application of the fixed-map theorem with identity J->I: that map generally does not exist.

More generally let the samples be drawn sequentially, possibly with adaptive stopping before the cap, and require on every actual prior branch that the next conditional law is within eta_j TV of D_(J,W), where eta_j is a deterministic bound. Any missing trial is no event. Then the upper bound is

    min(1, binom(m,2) b + sum_(j=2)^m eta_j).

There is only ONE TV charge for the entire union against earlier samples at each new stage, not one charge per earlier pair. The first sample may have any distribution for this bound: all subsequent pointwise counts condition on its actual value. If the extraction procedure insists on quotient labels, it can reject any sample not in J. The same upper bound also holds for any returned pair difference directly tested for membership in I, without quotient labels.

## Direct proof and filtration

For the exact law, each atom of X_j has probability at most p*=det(J)/W^n=D_I D_H/(c^n W^n), by the full centered Poisson normalizer. Ideal points of I within the radius-gamma c ball number at most N=(1+2gamma c/D_I^(1/n))^n, by packing. Neither claim depends on a previous sample.

Fix j and the entire ACTUAL transcript through X_(j-1), including the algorithm's previous coins and stop decisions. For each fixed prior x_i, the possible fresh x satisfying x-x_i in I and ||x-x_i||<=gamma c are contained in

    x_i + (I intersect Ball(gamma c)).

This set has at most N elements; restricting x to J cannot increase the count. Every exact fresh Gaussian atom is at most p*. Thus the event against this one anchor has exact conditional probability at most min(1,N p*)=b. Taking a union against all j-1 prior anchors gives exact conditional probability at most (j-1)b. The corresponding ACTUAL conditional probability differs by at most eta_j, because this whole stage event is one fixed event after the prior transcript is fixed. No future successful collision is in the conditioning sigma-algebra.

Take expectation over the actual prior transcript, and then union over j=2,...,m. This gives sum_(j=2)^m ((j-1)b+eta_j). The final selector's success is a subset of this existence event, regardless of how it chooses a pair after seeing the entire list. Zero differences were included throughout, and a nonzero requirement only decreases success. This proves the finite claim and its approximate-sampling variant. There is no multiplication of marginal probabilities and no conditioning on eventual success.

If samples lie in J, one may replace I by L in the candidate count, since all differences already lie in J. The stated bound intentionally uses the simpler universally valid packing count of I. The proof works even if a past approximate sample lies outside J; the larger translate-of-I count remains valid.

## Membership, law and norm before a hardness inference

The quotient is finite. Indeed cJ=IH is contained in both I and J, so cJ is contained in L, and the exponent of G divides c. Its size is [J:L]=det(L)/det(J), at most c^n. Exact rational bases suffice to compute L and quotient labels using ordinary integer lattice intersection and Smith/Hermite computations. On finite-bit sample coordinates, testing the integer threshold ||X_j-X_i||²<=c² and membership in I is exact and polynomial in the supplied bit lengths. This is ordinary arithmetic, not a Gaussian sampler or short-vector oracle. The m samples and the source-to-sampler transformation are still extra resources.

Pair collision law is not assumed uniform. For g in G, set pi_g=rho_W(g+L)/rho_W(J). Then the probability that an independent pair has equal labels is sum_g pi_g². Conditional collision changes the distribution. For every v in L, the exact unconditional probability of difference v is

    Pr[X_2-X_1=v]
      = exp(-pi ||v||²/(2W²))
        rho_(W/sqrt(2))(J-v/2) / rho_W(J)².

This follows by completing ||x||²+||x+v||²=2||x+v/2||²+||v||²/2 in the exact sum over x in J; symmetry makes either sign of the translate equivalent. Conditional on a collision, divide this expression by sum_g pi_g². Thus the collision output is supported on L, not necessarily all of I, and is not automatically D_(I,sqrt(2)W) or even D_(L,sqrt(2)W): the shifted theta factor can depend on v. Claiming a new Gaussian source from collision alone would discard both this modulation and the collision normalizer.

The raw difference does avoid multiplication by c. A valid simple norm certificate is also explicit: for exact centered D_(J,W), each coordinate has tail at W t bounded by 2exp(-pi t²), by completing the square in the moment-generating sum and using the maximum of a shifted theta sum at its lattice center. A union over coordinates and m samples shows that, except with probability 2mn exp(-pi t²), every pair has norm at most

    2 W sqrt(n) t.

Conditional sampler TV errors add their sum. This radius need not exceed c: when c is large enough the norm certificate can be favorable, but then obtaining an I-membership collision remains subject to the same small-ball probability bound. When collisions are easy, their norm is not certified to improve on c. The proof above resolves the combined event, without inferring either alternative from heuristics.

At gamma=1, D_H<=2^(rho n) with rho<1 and W>=32sqrt(2)n², one has b<=(6/W)^n. Polynomially many samples and a negligible sum of errors therefore almost never yield a useful pair difference. For exact sampling, constant useful success epsilon requires

    binom(m,2) >= epsilon (W/6)^n,

and hence m >= sqrt(2epsilon) (W/6)^(n/2). This is a necessary sample count derived from an upper bound, not an algorithm achieving that count. It is superpolynomial at the diagnostic width.

## Exact source endpoints and unresolved bridge

The input challenge remains P together with k iid natural reductions of Z_i~D_(Lambda,s), Lambda=J^-1=cI^-1H^-1, versus the SAME P and k iid uniform elements of R/qR, with gcd(q,cD_ID_H)=1. The exact mass of a planted residue a is rho_s(z_a+qLambda)/rho_s(Lambda); the comparator has mass q^-n. Identical public bases and declared latent laws are retained. Any independent fresh binary secret remains uniform coefficient-binary. These are the source endpoints described in `smallball-parameter-source-review-v1.md`; neither has been replaced by D_(H^-1,s), a covariance surrogate, or a uniform quotient law.

The new mechanism is downstream of a HYPOTHETICAL sampler of m full vectors D_(J,W). A bare source challenge supplies residues on Lambda/qLambda, not vectors on J or their quotient labels in J/L. No lift, same-family decision-to-sampling reduction, independence of successive sampler outputs, success probability, or coherent implementation follows from the pair algorithm. In particular, one cannot declare the sampler outputs to be Gaussian in one source world and independently uniform in the other without proving that complete transformation. The accepted A-FRAC statement inspected here still assumes an integral public J; the fractional extension is a separate open gate.

The only proven output endpoint is the displayed pushforward of the granted Gaussian product law by this pair selector. There is no standard RLWE/Order-LWE endpoint or arbitrary-ideal worst-case reduction established here.

## Finite falsification, failed inference and missing input

`finite-pair-v1/` exhausts n=2, I=(2+i), H=(1+i), c=5, J=((1+3i)/5)Z[i], L=(1+3i)Z[i], quotient G=(Z/5Z)², on the 81-point coefficient box [-4,4]² with exact weights (1023/1024)^(a²+b²). All 6561 ordered pairs are checked with rational arithmetic. Every anchor has at most nine admissible differences of norm<=5, of which at most eight are nonzero. Exact probabilities satisfy the finite law's own max-atom count. The report splits zero and useful nonzero mass and verifies the quotient labels directly from division by 2+i.

The tempting finite inference is demonstrably false: using the full-law geometric b after conditioning to this small box. Its useful pair probability is approximately 0.0316345, greater than 5/341, whereas full b=18/W²<5/341. This failure is preserved as E-NORMALIZER-1. It does not attack the full theorem; it identifies exactly why conditioning/truncation cannot be substituted in its premises. No extrapolation from the conditional finite pair law is used in the analytic proof.

The tested mechanism fails in the favorable diagnostic regime because polynomial sample caps cannot overcome the combined membership-and-small-norm event. The missing algorithmic input for this route is a different way to obtain useful combinations without enumerating a superpolynomial candidate family, or a rigorously narrower same-source sampler with a nonnegligible combined event. General combinations, division or nonlinear processing need their own joint-law and norm analyses; this statement gives no impossibility result for them. The original computational foundation remains unresolved.
