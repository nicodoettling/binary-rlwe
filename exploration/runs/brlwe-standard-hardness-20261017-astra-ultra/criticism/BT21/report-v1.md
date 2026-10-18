# BT21 independent blind report — specification v1

## Scope and status

I reviewed only `assignment-v1.md` and `input/theorem-only-v1.md` in BT21's assigned directory. I independently reconstructed the four claims below. No other report, proof, status record, ledger, external source, experiment, or computational search was consulted. This is correlated same-model scrutiny, not formal verification. It records a referee assessment; it does not accept a claim or complete a goal.

The algebraic statements and the fixed-multiplier probability bounds admit complete reconstructions from the allowed background. The Gaussian normalizer, its atom at zero, and the off-ideal failure branch are essential. The stated ideal norm cap supplies the short direction needed for the zero-probability bound; Gaussian width alone would not do so for an arbitrary sparse lattice.

Two logical qualifications should be made explicit in the wording. A randomized multiplier's moment inequality is conditional on the multiplier, with an expectation on its squared norm in the unconditional version. Also, polynomial numerical parameters do not by themselves imply a nonvacuous success budget. Claim 4 is valid when “with nonvacuous success budget” is an additional condition inherited from Claim 3. If it is intended as an automatic consequence of polynomial parameters, it is false; an exact admissible example appears below. Neither qualification supplies an algorithm that is absent from the hypotheses.

## 1. Normalized trace duality

Write every element of L uniquely as

    b = sum_{j=0}^{t-1} z^j b_j,     b_j in K.

The relative embeddings send z to the t roots of U^t-w, so their averaged sum selects the coefficient b_0. Thus Pi(b)=b_0. On the ordinary S power basis this is exactly selection of exponents divisible by t, without an extra t factor. The decomposition S = direct sum_{j=0}^{t-1} z^j R also gives Pi(S)=R and Pi(IS)=I.

The crucial stronger identity is

    {b in L : Pi(bS) subset I} = IS.                 (1.1)

Indeed, testing against 1 gives b_0 in I. For 1 <= j < t, testing against z^{t-j} gives w b_j in I: among the relative exponents only j+(t-j)=t contributes. Since w is a unit of R, b_j belongs to I. Conversely, coefficients in I remain in I after multiplying by S and applying Pi. Equivalently, the relative trace-pairing matrix has its (0,0) entry 1 and its remaining anti-diagonal entries w; its determinant is a unit. This explicitly resolves the possible different/codifferent normalization issue.

Suppose Pi(aF) is contained in I. For each f in F and s in S, fs is in F, so Pi((af)s) is in I. Equation (1.1) implies af in IS. The condition therefore equals aF subset IS. All nonzero ideals in this cyclotomic integer ring are invertible, so

    (IS : F) = IS F^{-1}.

The reverse implication follows immediately as well. Claim 1 follows. The proof includes t=1. Although I is not expressly declared nonzero in Claim 1, I=0 also causes no problem: aF=0 and F nonzero force a=0, and the right side is the zero ideal. Integrality of F is more than the duality proof needs, but is consistent with it.

## 2. Complementary ideal, norms, and actual family

By J dividing IS, the quotient ideal C=IS J^{-1} is integral and CJ=IS. Since S is free of rank t over R with the displayed relative basis,

    [S:IS] = [R:I]^t = M^t.

Multiplicativity of ideal norm gives N(C)=M^t/D. For a in C, aJ is contained in CJ=IS, and applying Pi gives Pi(aJ) subset I. This also follows from Claim 1 with F=J.

If N(C) and D both satisfy the cap 2^{rho m}, then

    M^t = N(C)D <= 2^{2 rho m}.

Taking the 1/m power, and using m=tn, gives A=M^{1/n} <= 2^{2rho}. This is a necessary condition, not a sufficient condition for both caps or for the required primes to exist.

Oddness ensures that the relevant primes avoid the cyclotomic ramification at 2. If r is the residue degree of J over I, then D=M^r, r divides t, and N(C)=M^{t-r}. Thus the actual two cap conditions are

    A^{r/t} <= 2^rho,      A^{1-r/t} <= 2^rho.

Their product proves the stated weaker necessary bound. In the inert case r=t, C=S; in general C need not be prime. For example, when the extension splits I into several primes, C is the product of the other prime factors. Consequently an oracle restricted to prime ideals, or to some other specified class, is not automatically applicable to C. No universal existence of an admissible J is proved by the specification. At rho=0 its assumptions on a nonzero odd prime J are impossible, since D>1; that case is simply vacuous.

## 3. Exact Gaussian: full normalizer and covariance

Identify J with its full coefficient lattice Lambda in R^m. Its covolume is D. Put

    Z_Lambda(W) = sum_{x in Lambda} exp(-pi ||x||^2/W^2),

with x=0 included. Let Lambda* be the Euclidean dual lattice. Poisson summation gives the exact identity

    Z_Lambda(W) = (W^m/D) sum_{u in Lambda*} exp(-pi W^2 ||u||^2).       (3.1)

All these sums converge absolutely. Symmetry gives E[X]=0. Applying two derivatives at v=0 to

    sum_{x in Lambda} exp(-pi ||x||^2/W^2) exp(2 pi i <x,v>)
      = (W^m/D) sum_{u in Lambda*} exp(-pi W^2 ||u-v||^2)

and dividing by the normalizer yields

    E[XX^T] = W^2/(2pi) Id
       - W^4 (sum_{u in Lambda*} uu^T exp(-pi W^2 ||u||^2))
               /(sum_{u in Lambda*} exp(-pi W^2 ||u||^2)).             (3.2)

The subtracted matrix is positive semidefinite. Hence E[XX^T] <= W^2/(2pi) Id in the positive-semidefinite order. This does not require a smoothing assumption or an approximation of the normalizer by its zero-frequency term.

Fix an allowed nonzero a. Let T_a be the real matrix of x -> Pi(ax). Multiplication by a in the ordinary power basis is negacyclic convolution. Every row of its m-by-m matrix contains the coefficients of a once, with possible sign changes. Pi selects n rows, so

    ||T_a||_F^2 = n ||a||^2.                                          (3.3)

Consequently

    E[||Pi(aX)||^2] = tr(T_a E[XX^T] T_a^T)
                    <= n W^2 ||a||^2/(2pi).

This proves the moment bound for the full exact lattice law. No assertion about the moment of an arbitrary TV perturbation follows from it.

## 4. Exact Gaussian: zero atom and its bound

The map T_a has real rank n: multiplication by nonzero a is invertible on L and Pi is surjective onto K. Let H=J intersect ker(T_a). For each y in T_a(J), choose x_y in J with T_a x_y=y. The entire exact pushforward law is

    Pr[Y=y] = (sum_{x in x_y+H} exp(-pi ||x||^2/W^2))/Z_J(W).          (4.1)

For y outside T_a(J) this probability is zero. In particular,

    Pr[Y=0] = Z_H(W)/Z_J(W),                                         (4.2)

where H has rank m-n and the numerator includes zero. For t=1, H={0}, so that numerator is 1. These formulae are not, in general, an ordinary discrete Gaussian on I; the fibers retain their own Gaussian weights.

Here is an independent proof of the claimed upper bound. Minkowski's theorem applied to coefficient cubes gives a nonzero v in J with

    ||v|| <= sqrt(m) D^{1/m} <= sqrt(m) 2^rho < 2 sqrt(m).             (4.3)

For completeness, a cube of radius r>D^{1/m} has volume greater than 2^m D and therefore contains a nonzero J vector. Letting r decrease to D^{1/m}, and using discreteness, gives the weak inequality in (4.3).

At least one of v,zv,...,z^{t-1}v has nonzero image under T_a. Otherwise the normalized pairing computation in Section 1, applied to av, would imply av=0, contrary to a and v being nonzero field elements. Choose such a vector b. Multiplication by a power of z is a signed permutation in coefficient coordinates, so

    b in J,    T_a b != 0,    ell:=||b|| < 2 sqrt(m).

Partition J into cosets modulo Zb. Each coset contains at most one point of H, since two such points would differ by a nonzero integer multiple of b in ker(T_a).

In any coset c+Zb, write c=c_perp+u b with c_perp perpendicular to b. Put s=W/ell. Its full Gaussian mass is

    exp(-pi ||c_perp||^2/W^2) Theta_s(u),
    Theta_s(u)=sum_{k in Z} exp(-pi (k+u)^2/s^2).

The Gaussian mass of any one point of that coset is at most the first exponential factor. Since W>=4 sqrt(m), we have s>2. One-dimensional Poisson summation gives

    Theta_s(u) = s sum_{j in Z} exp(-pi s^2 j^2) exp(2 pi i j u)
               >= s (1 - 2 sum_{j>=1} exp(-pi s^2 j^2))
               >= s/2.

The last inequality follows, for example, by setting q=exp(-4pi)<1/5 and bounding the positive-frequency sum by q/(1-q)<1/4. Thus the fraction of any coset's mass at its possible H point is at most 2/s. Summing over all cosets preserves this bound and gives

    Pr[Y=0] <= 2 ell/W < 4 sqrt(m)/W.

In particular the stated non-strict bound is valid. This derivation neither drops the zero vector nor conditions the sampler on nonzero output. It uses the ideal's root-of-unity symmetries and the supplied norm cap. Without a cap controlling a nonkernel lattice direction, an arbitrary very sparse lattice would invalidate such a width-only bound.

## 5. Failure event, TV transfer, and random multipliers

For fixed valid a, exact samples always give Y in I. Let

    B_a = sqrt(n/(2pi h)) W ||a||,       p0 = 4 sqrt(m)/W.

Markov's inequality applied to the nonnegative variable ||Y||^2 gives Pr[||Y||>B_a] <= h. Therefore the exact failure event, consisting of Y=0 or ||Y||>B_a, has probability at most min(1,p0+h).

For an implemented sample law Q, compare its full output law with the exact reference on a common measurable output space. This space must include any sampler failure tags; off-ideal values are part of Q's law, not silently discarded. Define the recovery map to return a failure tag on x not in J and otherwise to compute Pi(ax). Declare failure also for zero or over-bound outputs when defining the event of interest. Under the exact reference, the off-ideal branch has mass zero. If TV(Q,D_{J,W})<=eta, the probability of this entire failure event can increase by at most eta. Hence

    Pr[nonzero output in I of norm <= B_a]
      >= 1-min(1,eta+p0+h).

It is enough that zero and norm overflow define failure events mathematically; the theorem does not require exact runtime evaluation of its transcendental threshold. Exact membership is needed to protect the ideal-membership conclusion on Q's off-ideal mass. Conditioning Q on membership, resampling until success, omitting timeout mass, or truncating and renormalizing a law requires a new law and a new TV calculation. No such operation is implicit here.

TV closeness alone permits arbitrarily large second moments: put eta mass at an arbitrarily large lattice point and the remaining mass according to the reference. Thus retaining the exact-law moment statement separately from the implemented-law failure statement is necessary and correct.

For a randomized multiplier A, the rigorous moment statement is

    E[||Pi(AX)||^2 | A=a] <= n W^2 ||a||^2/(2pi)

for each allowed a, when X is independent of A and has the exact reference law. Unconditionally its right side is n W^2 E[||A||^2]/(2pi). Writing an unconditional expectation bounded by the random number ||A||^2 is not the correct general formulation. Fixing a returned multiplier before drawing X, as the specification requires, supplies the intended conditional reading.

For TV transfer with a random multiplier, one may assume independent X with the stated approximate marginal law; more generally it suffices that Q_{X|A=a} is within eta of the exact law for every allowed a, or that the complete joint law is within eta of mu_A times D_{J,W}. An approximate marginal for X alone would not suffice in the absence of the specified independence. Independence of random seeds alone is not a substitute if the sampler's chosen distribution depends on A.

The distinction has a concrete algebraic obstruction: when t>1, choose nonzero gamma in ker(Pi). For each nonzero x in a finite subset of J, a sufficiently divisible integer multiple of gamma/x belongs to C and maps that x to zero under Pi. Assign that multiplier after seeing x. Outside that finite set choose a fixed nonzero element of C, and at x=0 choose any one of these valid multipliers. On any finite set carrying reference probability near one, the resulting finite set of possible multipliers has some finite uniform norm constant C0 satisfying the prescribed bound. Thus a sample with the exact marginal reference law can be made to produce zero with probability near one by correlating the multiplier with it. This construction violates the independence premise, so is not a counterexample to the stated fixed/independent experiment; it shows why that premise must be retained.

If the multiplier routine itself has invalid-output probability delta, charge that branch before sampling. Conditional on its valid outputs, the previous calculation applies. A safe total failure bound is min(1,delta+eta+p0+h); under separate conditional assumptions one may retain the sharper delta+(1-delta)(eta+p0+h), clipped at one. An uncharged failure branch is not covered by the theorem.

## 6. Shortest-vector comparison and Minkowski existence

For nonzero y in I, the principal ideal (y) is contained in I, so the nonzero integer |N_{K/Q}(y)| is at least M. Orthogonality of the power-two cyclotomic coefficient embeddings gives

    sum_sigma |sigma(y)|^2 = n ||y||^2.

Applying arithmetic-geometric mean to the n squared absolute values yields

    |N_{K/Q}(y)| <= ||y||^n.

Hence ||y|| >= M^{1/n}=A and lambda_1(I)>=A. The genuine approximation factor on the successful event obeys

    ||Y||/lambda_1(I) <= B_a/lambda_1(I) <= B_a/A
      <= C0 sqrt(nm/(2pi h)) W/D^{1/m}.

The last step substitutes the supplied pointwise bound on ||a||. It uses coefficient norms throughout; no missing canonical-embedding scale occurs.

The coefficient covolume of C is N(C)=M^t/D. Repeating the Minkowski cube argument gives a nonzero a in C with

    ||a|| <= sqrt(m) N(C)^{1/m}
           = sqrt(m) A/D^{1/m}.

Thus C0=1 is indeed an existence statement. It is not an efficient short-vector construction. It supplies neither a Gaussian sampler nor a family-preserving oracle call.

## 7. Nonvacuity, computational promises, and an exact boundary example

Because D>=1 and n<=m, polynomial numerical values of m,W,C0,h^{-1} make the displayed approximation factor polynomial. This is a statement about numerical values: a number W with polynomial bit length can have exponentially large value and produce an exponentially large bound.

A nonvacuous stated success guarantee additionally requires

    eta + 4 sqrt(m)/W + h < 1.                                      (7.1)

Polynomial parameters do not imply (7.1). Here is a fully admissible exact example, without an experiment:

* n=m=4, t=1, R=S=Z[z]/(z^4+1).
* I=J=(3,z^2+z+2). Modulo 3, z^4+1=(z^2+z+2)(z^2+2z+2); the first quadratic has no root in F_3. Therefore J is an odd prime of norm M=D=9.
* rho=7/8 satisfies D=9 <= 2^{rho m}=8 sqrt(2), since 81<=128, and rho<1.
* C=IS J^{-1}=S, A=9^{1/4}=sqrt(3), and choose a=1, C0=1. Its norm 1 is at most sqrt(m) A/D^{1/m}=2.
* W=8=4 sqrt(m), h=1/2, eta=0.

All displayed numerical parameters are bounded constants, yet eta+4 sqrt(m)/W+h=3/2. The theorem's clipped failure bound is 1 and its guaranteed success lower bound is 0. This does not show the actual success probability is zero; it shows that the advertised error budget is vacuous. It falsifies only an interpretation of Claim 4 that infers nonvacuity from polynomial size. If Claim 4's words “with nonvacuous success budget” impose (7.1) as a separate premise, the example is correctly excluded from that conclusion. The wording should explicitly say “and a nonvacuous success budget.”

Such a budget can be chosen with polynomial parameters; for example W=16 sqrt(m), h=1/4, eta<=1/4 makes the displayed failure bound at most 3/4. This is a parameter choice, not a claim that a required sampler is available at that eta and cost.

For a polynomial-time repeated-success algorithm, mere positivity of the success lower bound is also weaker than an inverse-polynomial lower bound. An exponentially small positive gap in (7.1) need not permit polynomial-cost amplification. The specification does not establish standard computational hardness and should not be read as asserting this amplification.

Given encoded ideal bases, encoded multipliers, and bounded represented samples, ideal membership, negacyclic products, coefficient selection, and squared norms reduce to rational/integer linear algebra and arithmetic polynomial in their represented sizes. This observation does not bound the size or running time of a sampler, compute arbitrary real parameters exactly, or create the supplied multiplier. Actual finite sampler/setup/recovery costs and failure probabilities remain separate premises. An exact Gaussian is an infinite-support mathematical reference; no finite-support implementation is exactly that law. A finite implementation can instead have a charged TV error as specified.

The independence from fresh binary secrets is a supplied hypothesis. The four claims do not identify any resulting binary-RLWE distribution, prove a reduction from a standard hardness problem, or supply an oracle on C or on an unintended ideal family.

## 8. Objection reconciliation and limits

The objections considered in this independent review were:

1. A missing relative different or factor t in Claim 1. Resolved by the explicit unit pairing matrix and coefficient tests in Section 1.
2. Integrality, ideal norm direction, or an implicit prime-family transfer for C. Integrality and norm are proved in Section 2; prime-family transfer remains unsupported and is not claimed.
3. A covariance bound that discards the discrete Gaussian normalizer. Resolved by the exact normalizer and dual-lattice covariance identities (3.1)-(3.2).
4. Excessive Gaussian mass at zero for sparse J, or an implicit conditioning away from zero. Resolved under the actual norm cap by the short nonkernel direction and coset normalizers in Section 4. Without that premise the objection would persist.
5. Transferring an unbounded moment under TV error. Such a transfer would be false; the specification correctly transfers only the complete failure event.
6. Confusing conditional and unconditional random-multiplier assertions. The conditional moment and joint-law requirements are recorded in Section 5. The independence premise is necessary; its removal has the algebraic counterconstruction given there.
7. Inferring algorithmic computation from Minkowski existence, or obtaining standard hardness from the map. Neither inference is justified; the specification explicitly disclaims them.
8. Inferring nonvacuity from polynomial parameter sizes. The exact example in Section 7 preserves this objection against that literal reading. Under the separate-budget reading the polynomial certificate calculation is sound.

No experiment was needed to reconstruct these claims or exhibit the boundary example. The assessment is limited to the frozen theorem and its supplied assumptions. It makes no claim about an unseen proof, implementation, oracle, upstream reduction, or project status.
