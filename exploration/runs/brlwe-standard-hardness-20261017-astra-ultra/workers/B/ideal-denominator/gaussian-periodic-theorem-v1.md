# B-IDEN-GP-T v1 — finite public Gaussian-periodic bridge

Status: PROVISIONAL theorem statement, not accepted or certified. The separate proof is gaussian-periodic-proof-v1.md. This is a conditional public reduction. No standard hardness theorem for the required low-index ideal distribution is asserted.

## Ring, public information, and finite representation

Let n be a power of two, R=Z[X]/(X^n+1), and use the coefficient Euclidean norm. Let Gen be any fixed, explicitly specified distribution of integral ideals J of R, represented by an ordinary integer basis, with D=[R:J] and gcd(D,q)=1. The integer q>=2 need not be prime for this bridge. Put Lambda=J^-1. Both experiments retain the SAME public J and any explicitly specified additional Gen metadata. They do not retain a short basis or a sampling trapdoor unless that is explicitly part of Gen. The theorem holds pointwise for every J and therefore under any common Gen distribution.

Fix an integer P>=1 and put h_J=1/(DP). Input torus elements are elements of the finite group

    F_J = h_J Z^n / qLambda.

This is well-defined because Z^n subset Lambda subset D^-1 Z^n. A sample is encoded by an integer vector modulo the integer lattice DPqLambda; an ordinary HNF/SNF representation is sufficient. Its order is q^n D^(n-1) P^n. Choose any canonical representative of polynomial bit length in the supplied ideal basis, log q, log D, and log P. No closest-vector computation is used.

Let Q_h denote coordinatewise nearest-grid rounding with a fixed tie convention. It commutes with translation by hZ^n, and hence with qLambda. For positive w, define the exact mathematical input experiments with k samples:

    GP_P planted:
      (J, Y_1,...,Y_k), Y_i=Q_(h_J)(G_i) mod qLambda,
      G_i independently continuous D_w conditional on J;

    GP_P comparator:
      same J, Y_i independently uniform on F_J conditional on J.

Continuous D_w has density w^-n exp(-pi ||x||^2/w^2). If one starts instead with continuous Gaussian versus Haar samples on R^n/qLambda, applying Q_(h_J) gives exactly the above two mathematical laws. The finite experiment is the operational oracle interface; no infinite-precision real input is required by the reduction.

Choose rational parameters 0<epsilon<=1/4, 0<nu<=1/4, w>0 and r satisfying

    r >= max(1, sqrt(log(8n/epsilon)/pi)),    s=sqrt(w^2+r^2).

The exact mathematical output source is

    FG planted:
      (J, A_1,...,A_k), a_i independently D_(Lambda,s),
      A_i=a_i mod qLambda, identified with R/qR;

    FG comparator:
      same J, A_i independently uniform on R/qR.

The isomorphism Lambda/qLambda -> R/qR sends a=v/D to v D^-1 modulo q. This formula is independent of the chosen numerator representation. The source uses the actual lattice Gaussian, including its coset normalizers; it is not a uniform-coset Gaussian mixture.

## Reduction and finite guarantee

For each input y, independently:

1. Sample u uniformly from Lambda/Z^n, using invariant factors, and choose its coefficient representative in [-1/2,1/2)^n.
2. In each coordinate sample an approximate integer Gaussian with center y_i-u_i and width r using the finite, integer-translation-equivariant sampler specified below. Each coordinate distribution is within nu of D_(Z,r,y_i-u_i).
3. Set a=u+E and output its class in Lambda/qLambda, with J retained or discarded as required by the downstream distinguisher.

This single public map has the following full-joint guarantees:

    comparator: EXACTLY FG comparator;

    planted: distance from FG planted at most
      Delta = 2k epsilon/(1-epsilon) + 2pi kn/(Pr) + kn nu.

The exact comparator includes the finite-precision scalar sampler below, its truncation, and its fallback. It relies on exact uniform finite-group sampling, implemented in expected polynomial time by rejection of binary integers. Approximate uniform quotient sampling would require an additional error charge.

Consequently an FG distinguisher of advantage delta gives a GP_P distinguisher of advantage at least delta-Delta, with k input samples. This holds also for a distinguisher that receives only the A_i and discards J. All conditional correlations caused by the common ideal are retained. For a total desired loss zeta<=1/4, it suffices to take epsilon<=zeta/(16k), nu<=zeta/(4kn), and P>=8pi kn/(r zeta).

Runtime is expected polynomial in n,k, the bit lengths of the input ideal basis and samples, log q, log P, log D, log r, log w, and log(1/nu), plus the distinguisher runtime. The operation count does not depend polynomially on D or on r themselves. The reduction uses ordinary ideal arithmetic and scalar samplers only; it does not sample from a Gaussian over J or require a short basis of J.

## Explicit finite scalar sampler

For rational center c, write c=m+f with m=floor(c), 0<=f<1. Set

    K=ceil(log_2(64/nu)),  N=ceil(rK)+1,
    p=ceil(log_2(1024(K+1)/nu)),
    L=ceil(40K log(16/nu)).

At each of at most L trials, sample j uniformly from the integers [-N,N]. Compute a dyadic v_j in [0,1] with denominator 2^p and

    |v_j-exp(-pi(j-f)^2/r^2)| <= 2^-p.

Use exact p-bit Bernoulli sampling with probability v_j. On acceptance output m+j; after L failures output m. Elementary exponential evaluation to this absolute precision takes polynomial bit complexity because the normalized exponent has magnitude O(K^2), and all rational inputs have the declared bit lengths. The choice of approximation must be a fixed deterministic function of (r,f,j,p), so translating c by an integer translates the output exactly. The stated conservative constants give total variation at most nu; proof and bounds are in the proof packet.

Both finite input laws themselves admit sampling to arbitrarily prescribed additional statistical error in polynomial time using ordinary basis/SNF arithmetic and scalar Gaussian CDF approximation. Such an additional approximation error, if present in an external challenge implementation, is charged separately. The theorem compares the exact mathematical input laws above and the specified finite reduction, so it does not silently absorb an unbounded numerical error into the source assumption.

## Scales and scope

The normalized continuous periodic law has coefficient width w/q modulo Lambda. In the usual full canonical embedding its width is sqrt(n) w/q. The output coefficient width is s; its canonical width is sqrt(n)s.

The denominator index D may be below 2^(rho n), but this bridge does not establish hardness for that family. It also does not prove a binary-completion theorem. The existence of a short denominator basis can be used only in a separate proof; supplying that basis as metadata invokes the public-basis distinguisher in first-test-v1.md. No short-basis advice is hidden in this reduction.

This version supersedes no immutable earlier packet. It refines gaussian-periodic-bridge-v1.md by specifying a finite input interface and an equivariant finite sampler.
