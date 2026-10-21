# Proof of B-CUBE-THETA-v1

Status PROVISIONAL; exact statement in theorem-only-v1.md. All normalizers below are mathematical convergent lattice sums.

## 1. Joint law and residue lower bound

The joint mass is 2^(-n) 1_{y-b in J} rho_t(y-b)/rho_t(J). Thus

    p_guess(S|Y) = [2^n rho_t(J)]^(-1)
                    sum_{y in Z^n} max_{b in cube}
                        1_{y-b in J} rho_t(y-b).               (1)

The observation Y mod J equals S mod J exactly. On each nonempty binary fiber, S is uniform conditional on its residue, because S was uniform before the deterministic map. Each residue contributes exactly 2^(-n) to optimal success, giving C_J/2^n. Extra information Y cannot decrease optimum success. No claim that S remains uniform conditional on the full Y is made.

## 2. Gaussian envelope with the global cube center

Put c=(1/2,...,1/2), u=sqrt(t^2+r). For every real z,d, completing a square gives

    ||z-d||^2/t^2 >= ||z||^2/(t^2+r) - ||d||^2/r.              (2)

Indeed the difference equals || sqrt(r) z/sqrt(t^2+r) - sqrt(t^2+r) d/sqrt(r) ||^2/t^2. For any binary b, ||b-c||^2=n/4. Substitute z=y-c and d=b-c to obtain

    rho_t(y-b) <= exp(pi n/(4r)) rho_u(y-c).                    (3)

Only the C_J occupied cosets of J contribute to (1). Fix one binary representative b_a in each occupied coset a. Summing (3) separately on b_a+J bounds its numerator contribution by

    exp(pi n/(4r)) rho_u(J+b_a-c)
      <= exp(pi n/(4r)) rho_u(J).                              (4)

The last inequality is the centered-theta maximum: Poisson summation gives

    rho_u(J+v) = u^n/det(J) sum_{w in J*}
        exp(-pi u^2 ||w||^2) exp(2pi i <w,v>),

and the triangle inequality bounds this real nonnegative quantity by its centered value. This does not replace any actual Gaussian coset normalizer by a uniform approximation.

## 3. Exact normalizer ratio

Again by Poisson summation,

    rho_u(J)/rho_t(J)
      = (u/t)^n [sum_{w in J*} exp(-pi u^2||w||^2)]
                  / [sum_{w in J*} exp(-pi t^2||w||^2)]
      <= (u/t)^n,                                             (5)

because u>=t and every summand in the numerator is bounded by the corresponding summand in the denominator. Both sums are positive, since each includes w=0. Combining (1), (4), and (5) proves T1, including every normalization. Set r=t and use log(1+1/t)<=1/t to get T2. Here t and r are simply positive numerical parameters in the fixed coefficient normalization; equivalently one may state r=t times the unit coefficient length. No asymptotic dimensional convention enters the algebra.

## 4. Conditional-law audit

There is no sequential product argument. Formula (1) is the actual full joint guessing law. The Gaussian envelope is pointwise before summation. The only factorization is the scalar (u/t)^n from Poisson's exact dimension factor. If metadata Z and a proof-only H are revealed, application requires that for every positive-probability conditioning value (Z,H), the conditional law of (S,G) is the original product of uniform binary S and D_{J,t}. This holds in the existing A-FRAC proof because H is sampled independently of S,G conditional on its fixed source state. It does not hold for arbitrary secret-dependent revelations or H defined by subtracting MG from an independent target error. Zero-probability conditions are never used; zero source or output values are not discarded.

## 5. Cyclotomic geometry

If C_J<2^n, two distinct binary vertices b,b' have difference f=b-b' in J. Its coefficients lie in {-1,0,1}, it is nonzero, and its norm is at most sqrt(n). Since R is a number field, the n rotations f,Xf,...,X^(n-1)f are linearly independent over Q, belong to J, and have the same Euclidean norm L<=sqrt(n).

The elementary primitive-flag basis construction in A-FRAC proof section 5 now applies directly to these rotations. It chooses a basis whose i-th vector is alpha_i X^(i-1)f plus a combination of earlier rotations with coefficients in [-1/2,1/2], with 0<alpha_i<=1. Hence each basis vector has norm at most nL, and its basis matrix has operator norm at most Frobenius norm <=n^(3/2)L<=n^2. This construction is existential; the unknown f is not supplied to an algorithm.

Also (f) subset J gives N(J)<=|N(f)|. Parseval for the n complex embeddings gives sum_sigma |sigma(f)|^2=n||f||_2^2. AM-GM therefore gives |N(f)|<=||f||_2^n<=n^(n/2). This restricts eligible integral ideals themselves. It is not an obstruction to arbitrary class-changing, dimension-changing, or oracle-assisted reductions.

## 6. Scope

At t=2n^2 ell, T2 differs from residue guessing by at most exp((pi/8+1/4)/(n ell)). This is a uniform quantitative link, including ideals above the prior norm cutoff. Computing C_J can still require exponential enumeration. Exact image size, source hardness, accessible sampling, and effectiveness of a family transfer remain separate obligations. No finite test proves the infinite theorem; no failed source attack is hardness evidence.
