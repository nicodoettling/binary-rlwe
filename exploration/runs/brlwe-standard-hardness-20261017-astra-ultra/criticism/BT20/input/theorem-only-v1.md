# Normalized trace and complementary multipliers: specification v1

Let n and m=tn be powers of two with n>=2. Let R=Z[w]=Z[X]/(X^n+1), S=Z[z]=Z[X]/(X^m+1), w=z^t, with fields K subset L. All vector norms are Euclidean in the respective ordinary power coefficient bases. Pi=Tr_(L/K)/t selects coefficient exponents divisible by t; Pi:S->R. Absolute ideal norm means index in the integer ring; fractional ideals have their ordinary rational coefficient bases. For a full lattice F, D_(F,W)(x)=exp(-pi||x||^2/W^2)/sum_(u in F)exp(-pi||u||^2/W^2), on the ENTIRE lattice including zero.

Claim 1. For any nonzero integral S-ideal F and integral R-ideal I,
{a in L: Pi(aF) subset I}=IS F^(-1).

Claim 2. Let I be an odd nonzero prime R-ideal of norm M, J a prime S-ideal dividing IS, D=N_S(J), A=M^(1/n), 0<=rho<1, D<=2^(rho m). Then C=IS J^(-1) is integral, N(C)=M^t/D, and Pi(aJ) subset I for every a in C. If both C and J meet the same norm cap, necessarily A<=2^(2rho).

Claim 3. Suppose a supplied algorithm, at its fully charged cost, returns a nonzero a in C with ||a||<=C0 sqrt(m) A/D^(1/m), C0>=1, independently of all fresh sampling and fresh binary secrets in any upstream application. For exact X~D_(J,W), W>=4sqrt(m), Y=Pi(aX),
E||Y||^2<=n W^2||a||^2/(2pi), and Pr[Y=0]<=4sqrt(m)/W.
For ANY implemented full sample law of TV distance <=eta from this exact reference, use exact ideal membership and tagged failure on off-ideal inputs. For 0<h<1, the output is nonzero in I and of norm <= B_a=sqrt(n/(2pi h)) W||a|| except with probability <=min(1,eta+4sqrt(m)/W+h). This is a failure-event statement; no moment bound on an arbitrary TV-approximate law is asserted. A positive guarantee requires the error bound <1. A randomized multiplier needs the norm/membership premise pointwise on its allowed outputs, or a separately charged failure bound before fresh sampling.

Claim 4. The certificate relative to lambda_1(I) is B_a/A <= C0 sqrt(nm/(2pi h)) W/D^(1/m), since lambda_1(I)>=A. Polynomial m,W,C0,h^(-1), bit-lengths and supplied computation costs give a polynomial approximation certificate with nonvacuous success budget. Polynomial bit-length of W alone is insufficient. Minkowski establishes existence of such a with C0=1 but supplies no efficient short-vector algorithm. No ability to compute that multiplier, implement an exact Gaussian, provide a restricted-family oracle on another ideal, or establish standard computational hardness is asserted. Given bounded represented sampler outputs, all exact arithmetic is polynomial in their encoded sizes; actual finite sampler/setup/recovery-code costs must be added.

Allowed background: standard power-two cyclotomic arithmetic, Poisson summation for a Gaussian, Minkowski convex-body theorem, elementary probability. These may be reconstructed; no external retrieval is authorized for this review. No source assumption beyond this specification is supplied.
