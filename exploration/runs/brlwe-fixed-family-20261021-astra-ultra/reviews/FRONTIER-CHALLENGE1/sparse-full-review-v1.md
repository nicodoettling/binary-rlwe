# Full proof, source and complexity review: SV-SPARSE-ACQ-v1

Recommendation: **PASS within the literal sufficient algorithmic scope**, subject to the coordinator's separate fresh statement-only review and exact-hash acceptance. This is a new full review of coordinator/sparse-acquisition-statement-v1.md and sparse-acquisition-proof-v1.md, frozen in input-manifest-v1.json. It neither certifies FF nor establishes source hardness. All reasoning here is correlated same-model scrutiny, not formal verification.

## Quantifiers, finite input and acquisition

The support bound h is fixed before inputs. The basis is an arbitrary nonsingular integer column basis A of an integral ideal J, in the power basis of R=Z[X]/(X^n+1), with n a power of two. B is an integer of numeric size B, encoded in binary. Enumeration of supports of size j<=min(h,n) and signed coefficients 1,...,B includes every promised vector. The ordered-slot encoding gives an immediate valid bound (1+2nB)^h, including duplicates; the displayed support-count inequality is also valid. The zero vector is excluded. The claim does not promise polynomial time for varying h or exponentially large numeric B.

Compute A^-1 once by exact rational linear algebra. Membership is A^-1 f in Z^n, so each test costs polynomially many bit operations in n, the complete A encoding and log B. Determinant/cofactor bounds bound inverse entries by polynomial bit lengths, and no integer factorization is needed. Enumeration is polynomial for fixed h and polynomial numeric B, even if the shortest displayed input basis is poor. It actually constructs a member; it does not use an existence theorem as algorithmic advice. A qualifying member need not generate J.

The algorithm can stop at its first member when the uniform guard 4r²hB²<1 holds. When using the sharper member-dependent guard, it must retain the qualification "test ... for each found candidate": a candidate failing that guard may be skipped while enumeration continues. No universal improvement to the finite enumeration bound is asserted.

## Rounding, quotient and norm

For lambda in J^-1 and f in J, f lambda lies in R. The Fourier evaluation matrix at the n roots of X^n+1 is unitary after division by sqrt(n). Thus

    ||fw||_coef,2² = (1/n) sum_tau |tau(f)|² |tau(w)|²
                  <= ||w||_canonical,infinity² ||f||_coef,2².

Consequently every coefficient of fw has absolute value strictly below 1/2 under the guard, so nearest-integer rounding of fT gives f lambda, with no tie case. This directly verifies the stronger Euclidean product inequality used in the proof; it is not a confusion between canonical and coefficient norms. Nonzero f is invertible in the cyclotomic field: X^n+1 is irreducible for power-of-two n. Exact inversion of the multiplication matrix and rational output arithmetic have polynomial bit cost in the entire input and found f. The output lambda is not assumed to have bounded numeric magnitude; its encoding cost is charged.

There is no new probabilistic or adaptive argument. Neither Gaussian sampling nor a short basis nor a supplied generator is part of the input. The algorithm is pointwise for every promised rational target.

## Explicit Lucas family

Put f=X²-X-1 and theta=X mod f. The ring Z[theta] is free with basis 1,theta. The identity theta(theta-1)=1 makes theta a unit; its conjugate is -theta^-1. For m=n/2 even, the Lucas recurrence gives theta^m+theta^-m=L_m. Multiplying by theta^m gives theta^n+1=L_m theta^m. Since theta^m is a unit, ideals (theta^n+1) and (L_m) in Z[theta] coincide. Commuting the two monic polynomial quotients gives

    R/fR ≅ Z[theta]/(L_m) ≅ (Z/L_m Z)² as additive groups.

This establishes BOTH the norm L_m² and quotient exponent L_m, without factoring L_m or assuming it prime. The exponent assertion is not inferred merely from the determinant. At n=4 it gives exponent 3, norm 9; n=8 gives exponent 7, norm 49; n=16 gives exponent 47, norm 2209. These were independently checked using full multiplication matrices and inverse denominators, alongside the quadratic-ring identity.

For even m, L_m=phi^m+phi^-m. Hence log2(N(J_n))/n tends to log2(phi), approximately 0.69424, and any fixed rho strictly between that limit and 1 gives eventual norm eligibility. The theorem intentionally does not claim this family is eligible for all rho<1 or all small n. Its ordinary multiplication basis has entries in {-1,0,1}, proving a polynomial-length available representation; the algorithm nevertheless accepts any supplied ordinary basis and charges its full encoding. The input is not required to reveal f as a named generator.

## Actual inherited radius and useful separation

The accepted DD substitution is epsilon0=epsilon_*/2, epsilon=epsilon_*/4, delta=epsilon_*/16, giving exactly

    r = epsilon_* ell²/(1024 n K chi Qmax).

Here K=k0(Ncal+Ntest), chi is the represented integer chosen by AM, and Qmax is the actual largest auxiliary prime. No quantity has been dropped or replaced by its bit length. The guards give

    Qmax >= 8n³ ceil(sqrt(Kn)) ell⁴,
    r < 1/(8192 n⁴ K chi ceil(sqrt(Kn)) ell²) < 1/(4sqrt(n)).

The slight strengthening from the earlier SV-BDD-CLASS statement's 1/(2sqrt(n)) is justified by these exact numbers; it is not an unproved import. With h=3,B=1, 12r²<3/(4n)<1 for every n>=4. Thus the sparse decoder succeeds at every inherited admissible radius on this family.

When "inverse-polynomial r" means the intended positive radius lower bounded by n^-C in a fixed admissible polynomial family, exponential L_(n/2) times r tends to infinity. Therefore 2e(J_n)r<1 eventually fails while sparse rounding succeeds. If one instead allowed an exponentially tiny r, that separation need not hold; the statement explicitly restricts the separation to inverse-polynomial inherited families.

This is a useful algorithmic diagnostic beyond the scalar quotient-exponent guard, with a uniform acquisition rule. It overlaps the accepted short-member decoder in its final step; the new part is bounded-support acquisition and this exact exponential-exponent family. It does not claim the family defeats all prior subfield/code decoders, that it is hard, that an arbitrary eligible ideal has a polynomially searchable sparse member, or that a fixed-family FF radius has been delivered. The older norm-289/exponent-17 block family is not this exponential-exponent family and lay above the present norm cap; its warnings that supplied short generators can make sources easy remain relevant.

## Independent finite evidence and limitations

Preregistered FC1 control-v1, executed with parent LIGHT permission, exited 0 at 2026-10-21T21:21:18.238560+00:00. Exact Fraction checks cover n=4,8,16,32 determinant/exponent identities; n=4,8 acquisition from A times a nontrivial determinant-one integer matrix; and exact decoding of rational targets after the acquired member is found. No optimizer or root script was imported. The control is finite evidence, not a proof of the Lucas asymptotic, bit complexity, or all input bases. Those conclusions follow from the arguments above.

No blocking defect was found in the frozen v1 statement or proof. All inherited regressions are retained by exact reference in inherited-203-references-v1.json, with applicability in regression-scope-v1.md. The source-hardness foundation and the efficient unrestricted fixed-family decision reduction remain open.
