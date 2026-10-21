# Effective LLL complementary multiplier: first test v1

Frozen 2026-10-21. PROVISIONAL author calculation. This is a scoped test of a named effective construction, not a new LLL theorem, a lower bound on actual LLL output, or a standard-hardness reduction. The complete accepted same-J and conditional weighted-trace interfaces are imported only in their accepted scopes. The primary computational foundation remains OPEN.

## Frozen model and algorithm

Let n>=2 and m=tn be powers of two. Put R=Z[w], S=Z[z], w=z^t, w^n=z^m=-1. All norms below are ordinary coefficient Euclidean norms. Let I be an odd prime R-ideal of norm M, J a supplied prime S-ideal above I, D=N(J), and A=M^(1/n). The explicit input consists of ordinary integral bases of I,J and their tower embedding. Require D<=2^(rho m), 0<rho<1, and gcd(D,q)=1 for the actual same-J recovery modulus q. Form the integral ideal

    C=IS J^-1,       N(C)=M^t/D,       N(C)^(1/m)=A/D^(1/m).

Compute an ordinary integral basis of C by exact ideal arithmetic and reduce it by the usual size-reduced Lovasz-delta=3/4 LLL algorithm. Fix every tie convention. Let a be its first basis vector. Then a is a nonzero element of C, deterministically chosen before all fresh DGS/Rec coins. Invoke the same-J sampler once on J in dimension m, retaining its full output X and all metadata. Return the tagged failure symbol if the implementation gives an off-ideal point, if Pi(aX)=0, or if the stated output norm bound fails; otherwise return Y=Pi(aX). The accepted same-J sampler itself always outputs in J and uses zero fallbacks, so the off-ideal check is defensive and has zero probability under that exact implementation.

There is no eligible-family call on C. C need not be eligible. No short basis, exact Gaussian implementation, or sampler on C is supplied as advice. Supplying J is still a separate input requirement; this algorithm does not choose a suitably split eligible J for every target I.

## Exact norm certificate

For a size-reduced delta=3/4 LLL basis b_1,...,b_m with Gram-Schmidt vectors b_i^*, the Lovasz and size-reduction inequalities give ||b_(i+1)^*||^2 >= (1/2)||b_i^*||^2. Consequently

    det(C)^2 = product_i ||b_i^*||^2
             >= ||b_1||^(2m) 2^(-m(m-1)/2).

Taking the 2m-th root gives

    ||a|| <= L_m A/D^(1/m),       L_m=2^((m-1)/4).                 (1)

This uses the standard LLL algorithm at its actual ordinary input dimension m. The old primary-source record `workers/H/prime-alignment/lll-source-check-v1.md` identifies the 1982 LLL preprint Proposition 1.6/equation 1.9 and Proposition 1.26 for precisely the determinant and polynomial-bit-complexity claims. No stronger typical-case or ideal-specific estimate is imported. Equation (1) is independently derived above from the reduced-basis conditions.

The weighted theorem's supplied-multiplier form can be met with C0=max(1,L_m/sqrt(m)). More directly its accepted event statement applies with the actual certified norm (1).

## Delivered width, radius, success and queries

All RF4-SAMEJ-v1 parameters are evaluated with dimension m, the exact supplied recovery code, its all-input runtime bound, and its actual positive gap delta. In particular

    ell=ceil(log2(2mk)),
    d0=delta ell^2/(64mk chi),
    W_m=mq/(sqrt(2)d0)=32sqrt(2) m^2 k chi q/(delta ell^2),
    eta=min(1,epsilon+2sqrt(p_fail)+E_m),
    p_fail=(m/2) exp(-kappa)+zeta.

The full frozen theorem specifies chi,kappa,Q_*,E_m and every precision/cap term; none is dropped here. Its feasibility/gap inequalities remain prerequisites. Fix 0<h<1 before sampling. Provided W_m>=4sqrt(m), the accepted weighted result gives one-trial success at least

    1 - eta - 4sqrt(m)/W_m - h,                                  (2)

whenever this is positive, for a nonzero Y in I satisfying

    ||Y|| <= B_LLL=sqrt(n/(2pi h)) W_m L_m A/D^(1/m).             (3)

Thus B_LLL/A = sqrt(n/(2pi h)) W_m L_m/D^(1/m) is a valid approximation certificate relative to lambda_1(I)>=A. This is an event bound transferred under full-law TV, not a moment claim for arbitrary approximate output. All unsuccessful attempts remain in the law. One attempt uses one fresh J-sampler and at most 2Q_* coherent executions of the supplied Rec code. A classical answer oracle is insufficient. Actual setup, decoder compilation, and quantum execution cost is exactly the charged same-J amount, plus the charged classical ideal arithmetic, LLL, multiplication and trace costs.

No amplification is asserted. If repetition is later used, each trial must use fresh coins and have a conditional success margin bounded below by an inverse polynomial; its total calls and every failure must be charged.

## Both complete mapped endpoint laws

Let T_a:J->I be the integer linear map x -> Pi(ax), and L_a=T_a(J). For exact X~D_(J,W_m), its untagged planted law is

    Pr[Y=y] = (1/rho_(W_m)(J))
              sum_{x in J:T_a(x)=y} exp(-pi||x||^2/W_m^2),       (4)

for y in L_a, and zero otherwise. It retains zero with its actual mass. The tagged output pushes (4) through the deterministic zero/norm checks above, sending rejected mass to FAIL. There is no conditioning or discarded normalizer. For the full approximate implemented input law, applying the same fixed map/checks changes this complete output law by at most eta.

The distinct uniform quotient comparator is Xbar uniform in J/qJ. Its exact map to L_a/qL_a is uniform there, because T_a induces a surjective homomorphism from J/qJ to L_a/qL_a. Its further image in I/qI is uniform on (L_a+qI)/qI. It need not be uniform on I/qI. Public I,J,a,t,q and all tower data are identical at the endpoints. If a comparator is subjected to an additional zero/size test, its exact chosen representative convention and the pushed FAIL mass must be retained; equation (4) gives no bound for that distinct event. This test is an ideal-vector extraction construction and asserts no fresh decisional reduction. Its actual same-J implementation continues to use the two exact RF4 internal GP/uniform completion laws, whose TV charges are unchanged.

## Degree, bit size, effectiveness and the stopped certificate

Since J lies above I, D=M^f for a positive integer residue degree f. Hence eligibility requires

    m >= f log2(M)/rho = fn log2(A)/rho.                          (5)

Even before imposing (5), m>=n. The denominator D^(1/m)<=2^rho<2 can cancel at most a constant in (3), whereas L_m=2^((m-1)/4). In particular the certified factor obeys

    B_LLL/A >= sqrt(n/(2pi h)) W_m 2^((m-1)/4-rho).             (6)

Equation (6) is a lower bound on this particular declared upper-bound expression, NOT on ||Y|| or on the actual LLL multiplier. For polynomial numerical m,W_m,h^-1, that expression is exponential in m, so this certificate supplies no polynomial approximation family as n grows. For the inspected hard-prime source window A>=poly(n), (5) further forces m=Omega(n log n) when f>=1. This last comparison is a substitution into the historical inspected source condition, not a new audit of that paper or a global impossibility result.

Let p be the rational residue characteristic of I. Both J and C contain pS. A canonical integral HNF basis of C therefore has diagonal entries at most p and entries bounded in magnitude by p; each basis column has norm at most p sqrt(m), and its encoding length is at most m^2(ceil(log2(p))+O(1)) bits. The necessary ideal quotient/HNF calculations are exact polynomial-time integer linear algebra in the supplied input lengths, m and log p. LLL has polynomial bit cost in that represented basis (the actual cost is denoted T_LLL and charged); this says nothing polynomial in a numerical p bound. Multiplication by a and Pi are exact arithmetic on encoded output coordinates. From (1), each coordinate of a has bit length at most

    2 + ceil((m-1)/4 + log2(A)),                                 (7)

using D>=1; these lengths are polynomial in m+log M. The finite same-J output representation and all its setup costs remain charged independently. A numeric exponential W_m cannot be treated as polynomial merely because log W_m is small.

Prime J has additive annihilator exactly p: J cap Z=pZ. Thus a classical sampler whose certified regime depends on small annihilator can already cover the J call whenever its width inequality at e=p is satisfied. Whether this holds at the actual W_m is assigned to root M1. High numerical p is a necessary way for this specific prime-query construction to leave that sufficient simulation regime; it is not evidence of hardness.

## Exact short-vector enumeration alternative and residual gap

For completeness a fully effective but non-polynomial alternative is explicit integer-box enumeration in C. Put R_C=N(C)^(1/m)>=1 and B=floor(R_C)+1. Minkowski applied to a slightly smaller cube inside [-B,B]^m yields a nonzero a in C with ||a||<=sqrt(m)B<=2sqrt(m)R_C. Exact enumeration of all (2B+1)^m integer vectors with the HNF membership test finds one and has a bounded search space

    (2B+1)^m <= (2A+3)^m.                                      (8)

Its bit sizes are finite and polynomial in log A,m,log p per candidate; its guaranteed enumeration count is exponential in m. Equation (8) is an upper bound on this stated exhaustive algorithm, not a lower bound on every algorithm or on its possible early exit. It supplies the required polynomial-quality multiplier with an unavailable polynomial runtime bound.

The remaining obligation for this named route is therefore an effective algorithm producing a nonzero a in C at norm poly(m) A/D^(1/m), with polynomial represented-input cost, or a concrete alternative map whose full output norm/cost bypasses that obligation. Minkowski existence, LLL's exponential certificate, and exhaustive enumeration do not close it. Existing eligible-block products and full-basis saturation already supply other effective constructions with multiplicative certified losses and are not reintroduced as new ingredients here.
