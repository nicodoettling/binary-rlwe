# B-IDEN-GP-P v3 — full proof of the finite Gaussian-periodic bridge

Status: REPAIRED-PENDING-RECHECK author proof. Statement: gaussian-periodic-theorem-v3.md. The preserved BT4 defect concerns literal bit complexity and optional joint challenge generation, not the statistical endpoint argument. Full numerator/denominator input lengths are counted throughout this version. The BT5 trial-cap qualification is preserved in gaussian-periodic-bt5-literalization-v1.md; this proof uses the new integer L=40K ceil(log_2(16/nu)). Every claim below is conditional on the stated ideal family and challenge laws, not a standard-hardness import.

## 1. Algebra and representation

For an integral ideal J of index D, DR is contained in J because multiplication by D annihilates the finite additive group R/J. Thus a in J^-1 implies Da in R. Also R subset J^-1. Consequently Z^n subset Lambda subset D^-1 Z^n, det(Lambda)=1/D, and qLambda is an integer sublattice of h_J Z^n for h_J=1/(DP).

Multiplication by q is invertible on the group Lambda/R of order D. Therefore R/qR -> Lambda/qLambda is an isomorphism: its kernel is trivial because qlambda in R implies lambda in R; its image is all because q acts surjectively on Lambda/R. Writing a=v/D gives the inverse map v D^-1 modulo q. This also proves that the source comparator is uniform on the intended ring, not merely on an unidentified quotient.

Ordinary rational linear algebra, HNF and SNF compute Lambda, Lambda/R and DPqLambda from an ordinary basis of J. Their bit complexity is polynomial in the full binary input representation, counting both numerator and denominator lengths of every rational parameter and coordinate, the ideal basis, all integers, and all metadata that is read or copied. Magnitude logarithms alone are not a bound on the encoding size. A derived rational center and its fractional part have polynomial encoding length under these operations. Sampling invariant factors uses logarithmic rather than enumerative dependence on D. The grid quotient has order det(qLambda)/h_J^n=q^n D^(n-1)P^n.

Coordinatewise grid rounding commutes with qLambda. Uniform Haar measure on R^n/qLambda gives equal mass to every cell of the grid quotient because translation by its grid points permutes the cells. Thus its rounded image is exactly uniform on F_J. Fixed tie behavior changes no continuous probabilities.

## 2. Scalar finite sampler and uniform center bound

Put rho_r(x)=exp(-pi x^2/r^2). For r>=1, Poisson summation gives

    rho_r(Z-c)/r >= 1-2 exp(-pi r^2)/(1-exp(-3pi r^2)) > 0.9

uniformly in c. Here k^2>=1+3(k-1) for k>=1 bounds the nonzero dual sum. In particular every one-dimensional normalizer is bounded below without any assumption on the center.

Reduce c=m+f as in the statement. With N=ceil(rK)+1, the mass omitted by j outside [-N,N] is at most

    2r integral_K^infinity exp(-pi t^2) dt
      <= r exp(-pi K^2)/(pi K).

Dividing by the normalizer gives a truncation distance less than nu/16 for the declared K. There are 2N+1<=r(2K+5)<=3rK choices because K>=8. Approximating each weight with absolute error 2^-p changes total unnormalized mass by at most 3rK 2^-p. The true truncated normalizer is at least 0.8r. The elementary normalized-weight bound

    TV(a/sum a, b/sum b) <= (sum |a-b|)/(sum a)

therefore bounds the change by at most 4K 2^-p<nu/16. The approximated normalizer is still at least 0.7r, so one proposal accepts with probability at least 0.7/(3K)>1/(20K). The integer cap L=40K ceil(log_2(16/nu)) is at least ceil(40K ln(16/nu)), since log_2 x>=ln x for x>=1. Therefore the probability of L failures is at most exp(-L/(20K))<nu/16. Conditioning on any acceptance gives exactly the normalized dyadic weights. The deterministic fallback changes the distribution by at most the failure probability. The sum is less than nu, with ample slack.

A uniform integer proposal needs O(log(rK)) random bits in expectation, but the computation of K, N, p, L and exact rational comparisons also charges the COMPLETE numerator/denominator encodings of r and nu. For example, r=2±1/(2^H+1) requires this charge even though log r is bounded: with nu=1/4 and K=8, the two values give N=17 and N=18 for sufficiently large H. Therefore the expected running time is polynomial in the full declared input length, not solely in the parameters' magnitude logarithms. K, p and the inner ceiling in L are computed by exact comparisons of rational numerators/denominators with powers of two; N is a rational ceiling. No exact natural-log ceiling is computed. Evaluating exp on the normalized bounded interval to p-bit absolute accuracy is polynomial in p and the rational input lengths; dyadic Bernoulli sampling is exact. The number of trials is bounded by L. Since f is unchanged under c -> c+z for integer z, the entire finite sampler, including fallback, is exactly integer-translation equivariant.

For later comparison of nearby centers, let Z_c have the exact D_(Z,r,c) law. The sum of f_c(x)=|x-c|rho_r(x-c) over Z is at most its real integral plus its total variation. Those quantities are r^2/pi and 4r/sqrt(2pi e), respectively. Since r>=1 and the denominator is at least 0.9r, E|Z_c-c|<=2r. Differentiating the normalized probabilities along the center gives

    sum_j |d p_c(j)/dc| <= (4pi/r^2) E|Z_c-c|,

so the total-variation derivative is at most 4pi/r. Integration yields

    TV(D_(Z,r,c),D_(Z,r,c')) <= 4pi |c-c'|/r.

For products, the sum of the coordinate bounds is valid by a product coupling. These estimates are uniform over all centers.

## 3. Exact full comparator for the actual finite kernel

Let Q_y^fin be the implemented kernel before reduction modulo qLambda. For lambda in Lambda, translation by lambda permutes Lambda/Z^n. If u is a chosen representative and u' represents u+lambda, then v=u+lambda-u' belongs to Z^n. The new Gaussian center is

    (y+lambda)-u' = (y-u)+v.

The finite scalar sampler translates by v exactly, so the new output is u'+(E+v)=u+E+lambda. Therefore Q_(y+lambda)^fin is the translate by lambda of Q_y^fin. In particular qLambda translations do not affect the output class, so the channel is well-defined on F_J.

For a uniform input on F_J, invariance under the Lambda/qLambda subgroup and the preceding covariance imply that the output law on Lambda/qLambda is invariant under every translation. The unique such law is uniform. This proves the exact comparator for the actual finite sampler, without replacing it by an ideal Gaussian. Conditional on J, independent inputs and fresh independent local coins give independent outputs. Averaging over the common Gen law preserves the whole joint distribution and any retained Gen metadata.

## 4. Explicit smoothing bounds

For r^2>=log(8n/epsilon)/pi, write t=exp(-pi r^2)<=epsilon/(8n)<=1/32. The one-dimensional dual sum is at most 2t/(1-t^3), hence

    rho_(1/r)(Z^n)-1
      <= exp(2nt/(1-t^3))-1 <= epsilon.

Thus r>=eta_epsilon(Z^n) with the usual Gaussian smoothing convention. Poisson summation gives, for every real c,

    rho_r(Z^n-c)/r^n in [1-epsilon,1+epsilon].

Because Lambda contains Z^n, its Euclidean dual is contained in Z^n. The same dual-tail bound gives

    rho_r(Lambda-c)/(r^n/det Lambda) in [1-epsilon,1+epsilon].

Both estimates are uniform in every center and in J. No sampled center is treated as fixed independently of its actual law.

## 5. The two planted normalizers

Let Q_y be the exact uniform-coset/product-Gaussian kernel, before numerical approximation, and let P_y=D_(Lambda,r,y) be the exact lattice-Gaussian kernel. In P_y, the probability of a coset u+Z^n is proportional to rho_r(Z^n+u-y). Conditional within that coset, P_y and Q_y agree. These coset weights, divided by r^n, are in [1-epsilon,1+epsilon]. Relative to uniform cosets, they are reweighted and divided by their ACTUAL mean. For any positive reweighting V in [1-epsilon,1+epsilon],

    TV(mu, V mu/E_mu V) <= epsilon/(1-epsilon).

Consequently TV(P_y,Q_y)<=epsilon/(1-epsilon), uniformly in y.

Now let G have continuous D_w density and sample a according to P_G. Its full joint density/mass is

    p(y,a)=rho_w(y)rho_r(a-y)/(w^n rho_r(Lambda-y)).

Define a different, explicitly normalized joint law

    q(y,a)=rho_w(y)rho_r(a-y)/Z,
    Z=integral rho_w(y)rho_r(Lambda-y)dy.

Completing the square and integrating y shows that the a marginal of q is exactly D_(Lambda,s), s^2=w^2+r^2. Its y marginal is continuous D_w reweighted by rho_r(Lambda-y), divided by its ACTUAL expectation under continuous D_w. This theta value divided by r^n/det Lambda is in [1-epsilon,1+epsilon]. Therefore the y marginal of q is within epsilon/(1-epsilon) of continuous D_w. Given y, both joints use exactly P_y. Their full-joint distance is consequently at most epsilon/(1-epsilon). Combined with the preceding comparison, using Q_G instead gives distance at most 2epsilon/(1-epsilon) from D_(Lambda,s) on the a marginal.

This argument retains both center-dependent theta normalizers. Neither exact equality of the convolved marginal nor independence after conditioning is asserted without the corresponding reweighting charge.

## 6. Grid rounding and finite-sampler charges

Couple the actual planted input with an unwrapped G by y=Q_(h_J)(G). Then ||y-G||_1<=n h_J/2. Couple the uniform coset u in both exact Q kernels and apply the scalar center bound coordinatewise. It gives

    TV(Q_y,Q_G) <= 2pi n h_J/r <= 2pi n/(Pr).

The finite scalar sampler changes each conditional product law by at most n nu. Averaging over u preserves this bound. Therefore the implemented planted output for one sample is within

    2epsilon/(1-epsilon) + 2pi n/(Pr) + n nu

of D_(Lambda,s) modulo qLambda. Product coupling conditional on J yields the factor k. The bounds hold pointwise in J, so the actual joint ideal law and metadata may be averaged without a hidden independence assumption. The exact comparator was proved separately and needs no such charge.

The distinguisher advantage loss is at most the planted distance Delta. Data processing permits discarding J. Sample count stays k. All reduction work has the declared expected polynomial bit complexity.

## 7. Challenge implementation and foundation boundary

Conditional on a supplied J and supplied metadata, the finite input law is mathematically defined by rounded scalar real Gaussians. For a supplied rational zeta>0, it can be generated to error zeta by truncating each real coordinate outside a Gaussian-tail radius and using inverse-CDF sampling on the finite grid. This optional sampler counts the complete binary encodings of J, metadata, q, P, w and zeta, including all rational numerators and denominators. The number of grid points may be exponential, but its logarithm is polynomial in log D, log P, log w and log(1/zeta); binary-search inverse CDF needs only that logarithm many CDF evaluations. Taking CDF absolute precision smaller than zeta divided by the finite number of grid bins controls the total error, while its bit precision remains polynomial. Uniform finite-group sampling is exact in expected polynomial time conditional on the supplied ideal. To generate the JOINT experiment including J and metadata, one must additionally run Gen; joint efficiency is asserted only when Gen is efficiently samplable and includes its runtime. An arbitrary Gen is permitted for the pointwise statistical theorem and common-mixture conclusion, without any claim that Gen can be implemented efficiently. Any supplied challenge implementation error is additional to Delta.

The continuous input experiment has coefficient width w/q modulo Lambda, whereas the conventional full canonical embedding scales lengths by sqrt(n). This conversion is the only scale change in the bridge.

Nothing in this proof randomizes arbitrary worst-case ideals into a low-index family, proves a search-to-decision theorem, or supplies a hard source. The public short-basis test remains applicable if such advice is revealed. All new proofs await independent and blind review.
