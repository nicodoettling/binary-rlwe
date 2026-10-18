# Exact map from arbitrary I to prime-padded fractional J

Status: ENDPOINT/PARAMETER TEST; the standard worst-case reduction is OPEN. This follows only the specified map I -> I H/c with prime-ideal padding. It introduces no second extraction mechanism. The existing pair extractor and the classical known-witness simulator are used only in their audited scopes.

## Executable metadata map

Input: a rational/integer basis of a nonzero INTEGRAL ideal I in the fixed power-of-two ring R, together with the ring dimension n. Compute D_I=[R:I] and set c=D_I. Every element of the finite group R/I is annihilated by its order D_I, so cR subset I. A smaller known annihilator could be used, but c=D_I is an explicit uniform choice requiring no short vector.

Public padding parameters: an odd prime p with p=1 mod2n and p<2^(rho n), rho<1, and a primitive2n-th root r modulo p. Given such p, root generation/checks are as in `known-witness-scope-review-v1.md`; no unproved prime-generation runtime is hidden. Let

    H=(p,X-r),
    J=I H/c,
    Lambda=J^-1=c I^-1 H^-1.

Ordinary exact ideal multiplication, inversion and rational basis normalization compute these metadata in polynomial bit complexity. One can see the inverse representation without a trapdoor: constraints x*I subset R are rational linear congruences in the coefficient basis. All integer/rational representation lengths are part of the input cost. The algebraic output is exact, with

    N(H)=p,       det(J)=D_I p/c^n,
    det(Lambda)=c^n/(D_I p),
    H subset J,  [J]=[I][H].

Because p<2^n, evaluation of binary coefficient polynomials modulo p has a collision. Its nonzero ternary difference lies in H, hence in J. This is an existence statement; the algorithm above never computes or receives the difference. The map does not provide a short basis or any full-rank short set. Conversely, no hardness of finding such a set is asserted.

The ordinary ideal class of I is not erased. In fact I=cJH^-1 is recoverable from the public output metadata. With p fixed and r uniform among its n primitive2n-th roots, H ranges over only n prime ideals above p; consequently [J] ranges over at most n translates of their classes. This does not establish class-group mixing or a standard ideal-family distribution. For any uniform target on a class group of size h, a law supported on at most n classes has TV at least max(0,1-n/h), simply by testing the complement of its support. No class-number asymptotic is required for this conditional statement, and no such uniform comparator is substituted for the actual source.

## Complete challenge endpoints

Choose q with gcd(q,c D_I p)=1, a positive source width s, and sample count k. Let P denote the complete retained metadata (I,c,p,r,H,J,q,s,k, bases and declared parameter-generation law). Condition on P first. Then the two proposed challenges are

    P;  A_1,...,A_k iid with
        Pr[A_i=a] = rho_s(z_a+qLambda)/rho_s(Lambda),

and

    the SAME P;  A_1,...,A_k iid uniform in R/qR.

Here z_a is any Lambda lift under the natural rational isomorphism Lambda/qLambda -> R/qR. If p,r or other data are random, the same law is used in both worlds. There is no public f and no automatically supplied sampler. Any later binary secret S is fresh, uniform coefficient-binary and independent of the entire challenge and metadata.

The map from arbitrary I computes P. It does not, by itself, map samples from a standard RLWE/Order-LWE experiment to either endpoint or produce an oracle for the endpoint decision problem. The conditional wrapper from binary recovery, the finite GP/BDD interface, and decision-to-DGS machinery must be proved for this fractional J and its exact retained metadata. The inspected accepted A-FRAC theorem assumes integral J; this construction cannot cite it as already providing that extension.

A standard worst-case reduction would need a distinguisher with the required advantage for every generated J (or a proved average-case-to-pointwise conversion with accounted success loss). Averaged hardness for some unrelated ideal distribution is insufficient. Picking an independent random ideal after receiving a standard challenge would not preserve the joint law above. No source of such an oracle is established by the metadata identities.

## Width and useful output test

The exact inverse-lattice norm obstruction is

    ||lambda|| >= R0=c/(D_I p)^(1/n),   lambda in Lambda nonzero.

Thus widths satisfying pi(R0/s)²>=2n log5 enter the preserved zero-collapse regime, with planted zero probability at least1-2exp(-pi R0²/(2s²)). Uniform zero probability is q^-n. To avoid this immediate source defect one must select s consistently with the actual inverse-lattice scale; multiplying the ideal class symbol does not resolve it.

The diagnostic sampler width remains W>=32sqrt(2)n². This is a lower bound, not an upper bound. The obvious known witness p in H gives a classical sampler whenever the actual W>=p omega(sqrt(log n)); a large p avoids this particular witness only if the actual width ratio is too small. If W is polynomial in n while p is exponential below2^(rho n), the integer p does not supply that sampler. Other public vectors/sets may still do so; this is not a proved inability to sample.

Grant a fresh D_(J,W) oracle, solely for the next endpoint test. Direct clearing returns cX in IH subset I. Using the explicit Gaussian radius W sqrt(n)t, its certified output radius is

    B_I = c W sqrt(n)t,

with tail error at most2n exp(-pi t²), plus sampler TV error. In terms of an ideal-Hermite target ||v||<=Gamma D_I^(1/n), the supplied certificate is only

    Gamma = (c/D_I^(1/n)) W sqrt(n)t.

For c=D_I this contains D_I^(1-1/n), which is not bounded by a polynomial in n or in log D_I. Thus the map has not produced a standard polynomial-factor guarantee for arbitrary input ideals. The public integer c already has norm c, so the displayed radius offers no improvement over that public output.

This scale concern is concrete, not based only on a loose lower bound for lambda_1(I). Let M=floor(D_I^(1/n)). More than D_I coefficient vectors lie in {0,...,M}^n; two have the same I-coset. Their nonzero difference lies in I and has norm at most sqrt(n)M<=sqrt(n)D_I^(1/n). Therefore

    c/lambda_1(I) >= c/(sqrt(n)D_I^(1/n)).

For a degree-one prime input I of norm P and c=P, this lower bound is P^(1-1/n)/sqrt(n), which can be arbitrarily large as the input prime grows. A polynomial approximation target can require a vector far shorter than c on precisely such inputs. This existential bound is not an efficient algorithm for finding the difference.

The tested quotient-pair mechanism avoids literal clearing but does not repair the output endpoint. With m fresh samples its success of returning even a pair difference in I of norm<=c is at most binom(m,2)(6/W)^n, plus the causal TV losses. Thus polynomial m cannot supply the needed shorter output in the diagnostic regime, even though J was constructed without producing a binary witness. No claim is made about other short-combination algorithms.

## Frozen outcome and exact missing map

The arbitrary-I metadata construction is executable and preserves an existential binary collision in J. The challenge endpoint is fully specified. The construction neither supplies a standard-source distinguisher nor converts the granted broad Gaussian sampler into a polynomial approximation for arbitrary I. Randomizing the padding root does not supply a class-distribution theorem, and absence of a supplied witness is not computational hardness.

For this SPECIFIED map, the unresolved load-bearing step is an algorithm that uses the exact fractional-source decision interface (after its missing extensions are proved) to output a nonzero v in the original I with ||v||<=poly(n)lambda_1(I), or <=poly(n)D_I^(1/n), with polynomial sample/bit/runtime costs and success bounded below. If it reaches only the broad fresh DGS(J,W) interface, it needs extraction beyond the pair method analyzed here. Alternatively it must use additional explicitly specified behavior of the distinguisher; Gaussian marginals or source-name substitutions do not define such an interface.

This is the current boundary for the given I -> IH/c map. No further mechanism, new assumption, experiment or unrelated standard-family analogy is introduced in this test.
