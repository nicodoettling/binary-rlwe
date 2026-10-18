# RT1-authored weighted-trace complementary-multiplier bridge v1

Status: PROVISIONAL NEW RT1 AUTHOR LEMMA, requiring a fresh nonauthor check. This is an exact conditional ingredient with an explicitly missing algorithm, not a standard hardness proof or an available reduction. It is separate from the nonauthor review of root's frozen product lemma. The unweighted projection failure is retained in `preserved-failures-v1.md`.

## Exact multiplier module

Let R⊂S be the power-two cyclotomic tower, m=tn, z^t=ζ_(2n)=w, and Π=Tr_(L/K)/t. The pairing (a,b)↦Π(ab) makes S its own R-dual. To see this in the relative basis1,z,...,z^(t-1), the pairing matrix has entry1 in position(0,0), entryw when i+j=t, and zero otherwise. Its determinant is a signed power of the unit w, so the matrix is invertible over R. Equivalently the ordinary relative codifferent t^(-1)S becomes S after normalized trace pairing.

For any nonzero integral S-ideal F and nonzero integral R-ideal I, define

    C(F,I)={a∈L : Π(aF)⊂I}.

Then exactly

    C(F,I)=IS F^(-1).                                    (W1)

One inclusion follows from aF⊂IS and Π(IS)=I. Conversely, if Π(aF)⊂I then for every f∈F and s∈S, sf∈F and Π(afs)∈I. The unimodular pairing matrix forces every relative R-coordinate of af into I, i.e. af∈IS. Hence aF⊂IS and a∈(IS:F)=IS F^(-1), using invertibility of nonzero ideals in the Dedekind ring S. This reasoning handles fractional a and does not assume I principal.

For the relevant odd prime I and a chosen prime factor J|IS, the ideal

    C=IS J^(-1)

is integral: it is the product of all other primes above I in this unramified tower. In the inert r=1 case it is S. Its absolute norm is

    N_S(C)=M^t/D, D=N_S(J).                              (W2)

Thus weighted trace precisely requires a complementary ideal element, not arbitrary publicly chosen weights.

## Conditional algorithm and full probability law

Assume, in addition to an eligible supplied J and its finite same-J sampler, an algorithm supplies a nonzero a∈C with a fully charged finite representation and coefficient norm

    ||a|| ≤ C0 √m A/D^(1/m), A=M^(1/n),                 (W3)

where C0≥1 is polynomially bounded in n and a is chosen independently of the fresh sample and all fresh binary secrets. The basis of C and membership of a are exactly computable from I,J, but no efficient short-vector algorithm is presumed.

Take one fresh X∼D_(J,W), W≥4√m, and compute Y=Π(aX). Then Y∈I. For exact centered Gaussian X, the covariance and Frobenius arguments of RT1 moment v1 give

    E||Y||² ≤ nW²||a||²/(2π).                           (W4)

Since a≠0 and Π has rankn, ker(ΠM_a) is proper; root's subspace argument gives Pr[Y=0]≤4√m/W. With a full implemented sample law of TV≤eta, any h∈(0,1) gives a nonzero output of norm at most

    B_a=√(n/(2πh)) W||a||                              (W5)

except with probability at most min(1,eta+4√m/W+h). This is a single reference-law event transferred by TV; an actual approximate-source moment is not asserted. If a is randomized, require W3 and correctness on every allowed multiplier output, or charge its separate failure event and condition pointwise before fresh sampling. Do not hide a successful multiplier selection in the sample law.

The approximation certificate relative to λ1(I) is at most

    B_a/A ≤ C0 √(nm/(2πh)) W/D^(1/m).                  (W6)

For polynomial m,W,C0,h^(-1), this is polynomial even when A grows as n^alpha or faster. All coefficient sizes of a, its construction, and actual finite sampler costs must be charged. Membership computation alone does not produce the short a. The claim is deliberately conditional on W3 being effectively realized.

## What exists, what is missing, and why the same-J oracle does not supply it

Minkowski on the coefficient cube proves existence of a nonzero a∈C satisfying W3 with C0=1, because N(C)^(1/m)=A/D^(1/m). The algebraic norm/AMGM inequality also gives ||a||≥A/D^(1/m) for every nonzero a∈C. These are existence and scale statements. They provide neither short-vector advice nor a finite algorithm to compute that element from an ordinary basis.

In fact, if both J and C were eligible for the same norm cap, then

    M^t=N(J)N(C)≤2^(2rho m), so A≤2^(2rho).             (W7)

Thus a growing normalized target A=n^alpha rules out obtaining both sides from the unchanged eligible family. Explicitly, N(C)^(1/m)=A/D^(1/m)≥A/2^rho exceeds2^rho once A>2^(2rho). Applying the same-J sampler directly to C would violate its supplied-family promise. Factoring C again into eligible ideals and multiplying those fresh outputs returns the root product mechanism and its radius obligation.

The exact missing ingredient is therefore a polynomial-time procedure to find the complementary multiplier at the Minkowski scale up to a polynomial factor, or a richer source that supplies it. This is itself an ideal short-vector task in a generally ineligible complementary ideal. Its relationship to a standard arbitrary-ideal hardness problem has not been established here. The fact that its norm can be polynomial in n when A is polynomial does not make its discovery computationally easy.

For easy prime families over a small rational p, taking a=p or another obvious element may produce a polynomial norm bound, but p∈I already gives a short public target vector in those families. Such examples do not establish a hard family or solve the general complementary-multiplier computation.

This weighted-trace result identifies one concrete way to avoid multiplying r broad independent Gaussian samples: one short complementary multiplier absorbs the remaining ideal containment. It remains an extra algorithmic hypothesis, and no acceptance or standard hardness conclusion is asserted.
