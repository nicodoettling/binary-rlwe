# A-BIN v1: exact binary-image obstruction for the large-ideal escape

Status: **PROVISIONAL**. This is a scoped algebraic/composition obstruction, not an attack, a hardness impossibility, or an exclusion of all proof methods.

Let n>=2 be a power of two, q a split prime, and U_1,...,U_k in R_q. Let T_* be the union of their nonzero CRT supports, with r=|T_*|. If

    q^r > n^(n/2),

then s -> (U_1 s,...,U_k s) is injective on coefficient-binary s in {0,1}^n. In particular its exact binary-image cardinality D is 2^n. The generalized completion proof's revelation of this image determines S completely, so using the exact D instead of q^r gives no residual guessing entropy on this branch.

Proof. A collision yields a nonzero integer polynomial v=s-s' with coefficients in {-1,0,1}, vanishing at all r roots of T_*. Multiplication by v has rank at most n-r modulo q, so q^r divides its nonzero integer determinant. It is nonzero because X^n+1 is irreducible over Q. The determinant/norm bound from EX-v2 §2 gives

    q^r <= |det M_v| <= ||v||_2^n <= n^(n/2),

a contradiction. The strict inequality is essential; no converse is asserted. This argument requires no random ideal or ideal-point distribution.

If conditional on a d-subset T the k ideal points are independent uniform I_T including zeros, then

    Pr[T_*=T | T]=(1-q^-k)^d >=1-d q^-k.

This is the original CRT product law, before any observed transcript or selection; it does not condition away zeros. Thus if q^d>n^(n/2), the completion revelation is fully informative with at least this probability. This exact failure probability need not be negligible at fixed polynomial q and constant k. The statement is an obstruction to that upper-bound proof; it does not show efficient binary recovery from the public noisy source.

## Conditional application to C's proposed Order-LWE width

Worker C provisionally identifies coefficient width

    tau >= sqrt(n) q^(1-d/n) w(n),  w(n)->infinity,

for a known-ideal-modulus reduction after dual/canonical conversion. The primary theorem/normalization check belongs to C and is NOT certified here. Conditional on this floor:

* If q^(d/n)<=sqrt(n), then tau>=q w(n), so any method requiring target sigma>=tau cannot yield q/sigma>=1 eventually.
* If target sigma>=tau and q/sigma>=n^c for c>=0, then q^(d/n)>=sqrt(n) n^c w(n)>sqrt(n) eventually. On full-support branches, the binary ideal-image revelation is therefore injective.

Consequently replacing the crude q^d entropy charge by the exact binary-image cardinality does not rescue this same completion proof in the claimed width-compatible range. This conditional dichotomy concerns this width floor, sigma>=tau, and revelation of the full ideal image. A different source reduction, smaller actual mask representation, or a proof avoiding that revelation is not ruled out. In the current stacked completion, sigma>=2t||M||; a large width cannot simply be ignored, but a rigorous high-probability norm lower bound for the exact rounded elliptical law remains a separate check.

## Exact finite control

For n=8,q=17, all 256 binary vectors and every subset of the eight roots were enumerated in A-finite-1. Here n^(n/2)=4096 and 17^3=4913. Every subset with d>=3 has binary image cardinality 256, as predicted. At d=1 the image is 17; at d=2 image sizes range from 176 to 256, showing that injection can already occur below the sufficient threshold. Source: finite_controls_v1.stdout.json. This finite result is diagnostic, not a proof of hardness or necessity of the threshold.
