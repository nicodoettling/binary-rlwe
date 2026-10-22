# SV-RS-ACTUAL-v1: separate independent reconstruction

This supplement concerns only the frozen v1 statement and the sanitized v4/v5
parameter definitions. The v1 file contained an author-status sentence, recorded
verbatim in `status-exposure-exception-v1.md`. Accordingly this is independent
statement reconstruction with a status-only exception, **not a strict blind
gate**. No author proof or outcome was read. The parent later mentioned the
existence of a separate revised statement; that statement and its proof were not
opened and are not assessed here.

The mathematical radius-tuning and source-family conclusions follow from the
supplied parameter convention. An effective exact constructor for the specified
floor involving rho additionally needs a representation convention for rho, as
explained below. This does not affect pointwise existence or ordinary-basis
decoding once the integer support size and basis are supplied.

## A. Uniform C8 parameters precede the ideal

Use exactly the supplied convention: fixed b,c, epsilon_*=n^(-c), fixed or
inverse-polynomial zeta, and polynomial numeric values for the supplied resource
parameters, with all routine and input encodings charged. In particular
epsilon_*^(-1) and zeta^(-1) are polynomial. This qualification matters: merely
giving a tiny epsilon_* a polynomial-length binary encoding would not suffice.

Put delta=epsilon_*/16, w=sqrt(n)ell^2, and h0=delta w/(32nK). The supplied
formula simplifies to

    a0,max = D^(1/n) w [delta/(32nK)]^(2/n)/(nQmax),
    Smax = max(0, (n/2)log(nQmax/w) - (1/2)log D
                  + log(32nK/delta)).                    (A.1)

Thus Smax is largest at D=1 and has a polynomial common upper bound. The strict
tail condition holds uniformly for D<=2^(rho n) if

    kappa > rho n log 2 + log(24w/Qmin).                  (A.2)

All other lower bounds on kappa are polynomial under the parameter convention.
No actual D or factorization of J is needed. One can even choose a crude exact
rational upper bound: because w>=1 and log x<=x for x>0,

    Smax <= A := n^2 Qmax/2 + 32nK/delta.

Since w<=n ell^2 and rho<1, an integer strictly larger than

    4A + 4n + 4(K+1) + 20 + 2K + 2/delta + 40
       + 8n/zeta + n + 24n ell^2/Qmin + 2

simultaneously satisfies the supplied bounds and the strict tail condition.
This explicit overshoot avoids any exact comparison of logarithms. It has
polynomial numeric value and can be fixed before choosing J.

The v5 definitions make every C8 loop quantity a function only of this common
kappa (and Q_*=nQ_H). Each is obtained by a fixed number of additions,
multiplications, powers of fixed degree, and logarithmic ceilings. Therefore
Q_* is common and polynomial in the numeric parameter values. In particular
epsilon_C=min(1/16,zeta/(64KQ_*)) is inverse polynomial. The corrected precise
Up definition in v5 is Up(x)=ceil(c_x+1/8), |c_x-x|<=1/8, so the common integer

    a=Up(sqrt(log(8n/epsilon_C)/pi))+1

has polynomial value, indeed O(sqrt(log n)) within a fixed polynomial family.
It is independent of J. None of this uses the unprovided historical author
proof; it follows from the copied formulas and the permitted parameter guards.

## B. A split prime above the threshold is effective and polynomial

The positive represented rational

    C=epsilon_*ell^2/(1024 n K Qmax)

has polynomially bounded reciprocal in this convention. Hence

    H=max(Qmax,n^4,(a+1)/C,2n)

is a polynomial-value threshold. Choose a power of two V>H. It is a multiple
of 2n. The progression V+1 modulo 2V is coprime to its modulus, and every
positive member exceeds H and is 1 modulo 2n. Effective Linnik with exponent
6 supplies a prime p in this progression with p<=C_0(2V)^6. Searching the
progression until the first prime, using exact primality checks, is therefore
polynomial in the numeric threshold; no unproved short-interval prime statement
is required. This proves simultaneously p>Qmax, p>=n^4, Cp>a+1, complete
splitting, and polynomial numeric p.

The master auxiliary list was fixed before this choice. In particular p being
larger than every auxiliary modulus prevents any auxiliary modulus from having
a common factor with the later source norm p^t. This does not select or modify
the target list as a function of J.

## C. Exact delivered radius

Write x=Cp and choose chi=ceil x. Since x>a+1 and a>=1, chi>=a and x>1. Exact
rational arithmetic gives

    1/2 < x/(x+1) < x/ceil x <= 1,
    therefore 1/2 < pr <= 1 for r=C/chi.                  (C.1)

The first displayed strict inequality can be weakened as needed; the middle
strict inequality holds even if x is an integer, since ceil x<x+1. Chi has
polynomial numeric value and is explicitly charged. The interface expressly
permits any chi>=a. Its displayed d0=delta ell^2/(64nKchi) only decreases when
chi is increased, so its upper guard remains valid. This use of a larger chi
does not claim that the minimal choice chi=a has the same property.

For this corollary the supplied delivered-radius numerator is epsilon_*.
The internal interface parameter epsilon=epsilon_*/4 is a separate definition;
it must not be substituted into C a second time. Thus r=C/chi is exactly the
copied delivered-radius expression, not an illustrative replacement. The usual
Qmin and sigma_floor guards also give r<1/(4sqrt(n)) by the common radius
calculation in the main report.

## D. Source family and decoding comparison

For v1's precise support size, let t be the largest positive odd integer at
most floor(rho n/log2 p). Polynomial p>=n^4 gives log p=Theta(log n), so

    t=rho n/log2 p+O(1),  t tends to infinity,
    log2 N(J)=t log2 p=rho n-O(log n)=Theta(n).

Eligibility follows directly from the floor. Eventually 1<=t<n and n-t+1>8.
For the consecutive split-prime product, ordinary basis construction given
n,p,t is polynomial in numeric p and n. Its exponent is p, its support is odd
and therefore has trivial full Galois stabilizer, and the exact contraction
calculation remains d_g=p^min(t,g). Those properties do not depend on whether
the support-size definition uses log2 p or its ceiling; here I have checked
v1's definition directly instead of silently substituting the other one.

Every feasible standard contraction has index d_*=p^t=exp(Theta(n)), and the
arbitrary-subfield comparison gives d_all>=sqrt(d_*)=exp(Omega(n)). But (C.1)
implies

    2pr>1,
    8p^2r^2<=8<n-t+1.

The scalar sufficient guard fails and the exact RS guard succeeds at the actual
delivered r. The ordinary-basis RS decoder consequently runs in polynomial
time on this family. Failure of the collision criterion is still not hardness.

## E. Exact scope and the remaining representation qualification

The above is a pointwise mathematical construction and proves a nonempty
actual-radius regime under the supplied inherited-family assumptions. It does
not construct a new fixed-target theorem or assert that valid inherited
parameter families exist for every adversary; those are expressly supplied
assumptions. Polynomial reciprocal epsilon_* and zeta, the common loop formulas,
and permission to enlarge chi are load-bearing and were checked from the
sanitized definitions.

V1 allows an arbitrary fixed real rho, while its precise t uses an exact floor
involving rho. The pointwise existence argument is valid for every 0<rho<1.
An effective exact family generator for that specified t requires more. For a
fixed rational rho=A/B, one can determine t by exact integer comparisons
p^(Bt)<=2^(An) and choose the largest admissible odd integer; the bit lengths
are polynomial. For an arbitrary noncomputable real rho no algorithm can be
inferred for that floor. Alternatively a fixed rational rho0<rho gives an
effective eligible exponential-index family with the same radius conclusion,
or t can be supplied with a certified eligibility bound. This is a generation
qualification, not a defect in the decoder from a supplied ordinary basis.

No numerical experiment was needed for (A.1)-(C.1): these are exact elementary
inequalities and ceilings. The source contraction and RS mechanisms were
independently proved and registered finite checks were already preserved for
the original ten statements. The corollary's status remains **PROVISIONAL** for
programme certification and it does not satisfy a fresh strict blind gate.
