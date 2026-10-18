# A-FRAC v1 complete author proof

Status PROVISIONAL; frozen statement theorem-only-v1.md. Norms are coefficient Euclidean. All arguments below concern actual joint laws, not posterior product assumptions.

## 1. Quotients, integrality and the exact wrapper

Since R is the maximal order of the power-of-two cyclotomic field, every nonzero integral ideal is invertible, Lambda=J^-1 contains R and [Lambda:R]=D. The finite group Lambda/R has order D. Multiplication by q is a bijection on this finite group when gcd(D,q)=1. Therefore R -> Lambda/qLambda is surjective and its kernel is qR: if r=q lambda lies in R, the class of lambda in Lambda/R is q-torsion and hence zero. This gives the stated canonical isomorphism R/qR -> Lambda/qLambda. Rational reduction of a is the corresponding inverse map, not coefficient rounding. In particular a g lies in R for every a in J^-1 and g in J.

Fix an unwrapped source state z=(J,a_1,...,a_k). Use column coordinates for this proof. Let M be the kn-by-n vertical stack of column-action multiplication matrices M_ai; these are transposes of B's row-action matrices. Then M g is an integer vector whenever g belongs to J. The transpose convention does not change operator norms. Completing with fresh binary S and independent integer target E gives responses M S+E reduced through the quotient isomorphism, block by block. Under the uniform source comparator, these are exactly the original uniform-multiplier target samples. There is no Gaussian conversion at either wrapper endpoint.

## 2. A tail bound for the actual fractional-lattice Gaussian

For any full-rank real lattice L and width s>0, Poisson summation writes its shifted theta as

    rho_s(L-v) = s^n/det(L) sum_(u in L*) exp(-pi s²||u||²)
                                          exp(2pi i<u,v>).

Consequently rho_s(L-v)<=rho_s(L) for every v; both sides are real and the upper bound follows from the triangle inequality. Completing the square in the ACTUAL mass of a~D_(L,s) gives, for all real h,

    E exp(<h,a>)
      = exp(s²||h||²/(4pi))
          rho_s(L-s²h/(2pi))/rho_s(L)
      <= exp(s²||h||²/(4pi)).

Chernoff optimization therefore gives, for every nonzero real vector v and L0>0,

    Pr[|<a,v>|>=s||v||L0] <= 2 exp(-pi L0²).             (P1)

This does not require a smoothing assumption, uniform coset weights, or a basis of L.

For a primitive 2n-th root zeta, the real and imaginary coefficient vectors of evaluation a(zeta) each have squared norm n/2. Indeed sum_(j=0)^(n-1) zeta^(2j)=0 for n>=2. If |a(zeta)|>s sqrt(n)L, one of its real and imaginary parts has absolute value greater than s sqrt(n/2)L. Applying (P1) twice gives probability at most 4exp(-piL²). A union bound over all k samples and n roots gives, except with probability delta_tail,

    |a_i(zeta)|<=s sqrt(n)L for all i,zeta.

The normalized complex Fourier matrix unitarily diagonalizes all negacyclic multiplication matrices. Hence

    ||M||_op = max_zeta (sum_i |a_i(zeta)|²)^(1/2)
             <= s sqrt(kn)L.                            (P2)

This tail bound holds conditionally on EVERY J, even though the a_i share J. Good is the source-only event in (P2), independent of fresh S and all proof Gaussian randomness.

## 3. Discrete rectangular completion over J, with every normalizer

Fix any good state z. Sample proof-only G~D_(J,t). Independently conditional on z sample the integer vector H on Z^(kn) with mass proportional to exp(-pi h^T C^-1 h), where

    C=sigma² I_(kn)-t²MM^T >=3sigma² I_(kn)/4.

Neither G nor H is sampled by the public reduction. Both are well-defined mathematical random variables. Set

    Theta=t² I_n-(t^4/sigma²)M^TM >=3t² I_n/4,
    mu_e=(t²/sigma²)M^T e.

The exact rectangular square-completion identity is

    ||g||²/t² + (e-Mg)^T C^-1(e-Mg)
       = ||e||²/sigma² + (g-mu_e)^T Theta^-1(g-mu_e).    (P3)

Because M maps J into Z^(kn), the sum over all g in J is precisely the probability mass of MG+H at each integer e; no fractional or missing support is dropped. Thus its mass is

    rho_sigma(e) rho_Theta(J-mu_e)
                 / [rho_t(J) rho_C(Z^(kn))].             (P4)

Let a row basis B_J of norm at most tau2 exist. Its coefficient lattice is B_J^T Z^n and its Euclidean dual is B_J^-1 Z^n. For each dual vector B_J^-1 z,

    (B_J^-1 z)^T Theta(B_J^-1 z)
       >= 3t² ||z||²/(4tau2²).

Poisson summation, now for the elliptical Gaussian, gives uniformly in every center mu,

    rho_Theta(J-mu) / (sqrt(det Theta)/D) in [1-Delta,1+Delta].

For Delta<1, write that ratio as r_e at center mu_e. Normalizing (P4) gives the EXACT expression

    Pr[MG+H=e] = D_sigma^(kn)(e) r_e
                         / E_(D_sigma^(kn))[r].          (P5)

The actual expectation in the denominator is retained. Since r_e and its expectation lie in [1-Delta,1+Delta], the total variation is at most Delta/(1-Delta), capped by one. When Delta>=1 the trivial distance bound one is used. Therefore the full laws of (z,S,MS+E) and (z,S,M(S+G)+H), with H integrated out, differ by at most eta on each good z. We do NOT retain H alongside the independent-noise endpoint, since that would be a different joint-law comparison.

## 4. Exact finite-index guessing bound

For each fixed J, let Y=S+G as an UNWRAPPED integer vector, with uniform binary S independent of G~D_(J,t). Its optimal actual-secret guessing probability is

    p_guess(S|Y)
      = 1/(2^n rho_t(J)) sum_(y in Z^n)
            max_(b in {0,1}^n) [1_(y-b in J) rho_t(y-b)].

Dropping the displayed membership indicator can only increase this sum. Write theta=rho_t(Z). Product factorization is used only for this unconditioned upper bound. In one coordinate, symmetry and unimodality give

    sum_(y in Z) max(rho_t(y),rho_t(y-1)) = theta+1.

Consequently

    p_guess(S|Y) <= (theta+1)^n/(2^n rho_t(J))
                  = [rho_t(Z^n)/rho_t(J)] p_t^n.         (P6)

Partition Z^n into its D cosets modulo J. By the centered-theta maximum already proved,

    rho_t(Z^n)=sum_(c in Z^n/J) rho_t(J+c)
                       <=D rho_t(J).                    (P7)

Equations (P6)-(P7) give the EXACT bound min(1,D p_t^n), for every t>0, including below smoothing. No coset is assumed uniform and no center-dependent normalizer is discarded.

The completed transcript is a deterministic function of (z,H,Y): compute M Y+H and reduce modulo q. Revealing these variables therefore only increases the recovery power. Conditional on z,H, S and G retain exactly their original independent laws because H was sampled independently of S,G conditional on z. Hence the bound applies to recovery from the completed transcript. There is no leakage term for the number of possible ideals or bases: J is fixed first, and the estimate is uniform before averaging. Bad source states contribute at most delta_tail and the good comparison contributes at most eta. This proves planted wrapper acceptance at most delta_tail+beta+eta.

The comparator acceptance is exactly epsilon. Taking the difference proves (F1). If each executable wrapper world is within delta_wrap of its ideal law, each acceptance changes by at most delta_wrap, giving the stated 2delta_wrap loss. Appending the separate GP bridge and data processing gives (F3), with its total two-endpoint implementation loss kept explicit.

## 5. Existence of a short ideal basis, without an algorithm

Minkowski's convex body theorem applied to the coefficient cube gives a nonzero f in J with ||f||_coef<=sqrt(n)D^(1/n): enlarge the closed cube by an arbitrarily small amount to get volume greater than 2^nD, then use discreteness to pass to the endpoint. The n rotations v_i=X^(i-1)f belong to J, have the same norm L0<=sqrt(n)D^(1/n), and are linearly independent over Q. Independence follows because multiplication by nonzero f is invertible in the number field.

Define V_i=span_R(v_1,...,v_i) and J_i=J intersect V_i. The flag is rational, so each J_i has rank i. Projection to the v_i coordinate maps J_i onto a discrete rank-one subgroup alpha_i Z with 0<alpha_i<=1, since v_i belongs to J_i. Choose b_i in J_i with v_i coefficient alpha_i. Subtract integer multiples of v_j, j<i, so its other v_j coefficients lie in [-1/2,1/2]. These subtractions remain in J_(i-1) and do not change its primitive image in J_i/J_(i-1). Inductively b_1,...,b_i are therefore a Z-basis of J_i. Their norms satisfy

    ||b_i|| <= alpha_i||v_i|| + (1/2) sum_(j<i)||v_j||
             <= (i+1)L0/2 <= nL0.

The resulting row basis satisfies

    ||B_J||_op <= ||B_J||_F <= sqrt(n)nL0
                                  <=n²D^(1/n).

This is an existence proof. It neither computes the Minkowski vector nor solves any lattice basis problem. The public reduction never evaluates B_J, G, H, Theta or the source event Good. Those objects only establish the information bound. The original source multipliers and fresh target errors are all the reduction needs.

## 6. Computational and scope gates

The wrapper uses one call to Rec, n independent bits, kn scalar integer-Gaussian draws, k ordinary ring products and equality testing. With explicit finite-precision samplers and polynomial-bit parameters this is polynomial-time up to the charged sampling distance. An exact unbounded discrete Gaussian is a mathematical law, not a claim of a bounded-time exact finite-machine implementation. There is no need for an efficient sampler for D_(J,t) or the covariance-C proof variable. Likewise the mathematical FG challenge can be reached approximately through B's public GP bridge without implementing a standalone arbitrary-lattice Gaussian sampler.

Every target error in this proof is a coefficient DISCRETE Gaussian. GP is a continuous torus source only inside B's separately audited bridge. We never replace rounded continuous errors by exact discrete errors. A small target-noise implementation error is charged by delta_wrap; a bridge numerical error is charged by delta_num. The analytic theorem uses no selected-stage coordinate independence, no uncharged conditioning on a good source event, and no off-promise recovery-oracle query.
