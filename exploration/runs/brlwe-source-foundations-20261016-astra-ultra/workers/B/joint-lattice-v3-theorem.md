# B-JL-v3 — frozen short joint-relation obstruction

Frozen 2026-10-16 21:26 UTC. Status **PROVISIONAL**, author claim only. This narrows the v2 domain to b>=1, because its displayed tail formula was undefined at b=0. All earlier versions are preserved. No certification is inherited.

## Source, public witness and resources

Use SC-v1 exactly, including uniform ideal values with zeros, one uniform d-subset T, coefficient-iid D_ell errors, and one public pair A_1,A_2. Let O=Z[X]/(X^n+1), K=Q[X]/(X^n+1). G=Gal(K/Q) has order n. All quantities below are fixed before the challenge.

Let integers C,b>=1 and B>=0, 1<=r<=n, 1<=d<n, and impose the strict gates

  sqrt(n)*C < sqrt(q),
  sqrt(n)*(B+2nCb) < q^(1-d/n),
  2B+1 < q.

A public witness is a subgroup H<=G of index at most r and a nonzero pair (h_1,h_2) of H-fixed elements of O, each with coefficient infinity norm <=C, for which every centered coefficient of h_1 A_1+h_2 A_2 mod q has magnitude <=B. Multipliers and the subgroup can be selected after seeing the entire pair, with arbitrary computation. Acceptance event W is existence of such a witness. A witness-search distinguisher accepts only upon producing and verifying such a witness; it may fail to find an existing witness. This is a precise restricted method class, not a restriction on arbitrary source distinguishers.

Let N_G be the number of subgroups of index <=r. The elementary bound N_G<=n^ell is permitted, ell=log2 n. Set

  a = 2 / 3^(3/4) < 1,
  L = floor(d/4)+1,
  eta_rel = min(1, N_G * 2^r * (a^d + (q+1)^r q^(-L))),
  eta_F = min(1, 2n exp(-pi*b^2/ell^2) ell/(pi*b))   [b>0],
  rho = (2B+1)/q,
  eta_unif = min(1, N_G (2C+1)^(2r) rho^(n/2)).

Candidate conclusions:

1. Under Base2, Pr[W] <= eta_rel+eta_F (capped by 1).
2. Under independent uniform ring A_1,A_2, Pr[W] <= eta_unif.
3. Consequently any witness-search test in the class has absolute distinguishing advantage at most eta_rel+eta_F+eta_unif. This includes its complement, but does not bound algorithms that use additional input-dependent acceptance rules after a failed search.
4. For the two SC-v1 concrete d families, q least 1 mod 2n^3, any r=o(d), C=n, b=ell^2, B=2n^2 ell^2, all gates hold eventually and both bounds are negligible. The same conclusion holds for any d/log^2 n -> infinity with d<=n/(64ell), and the same polynomial-q bounds. Thus using short multipliers from all fixed fields of degree o(d), even chosen jointly/adaptively, cannot yield a useful short-output cancellation witness.

No efficient algorithm is claimed. Verification of a provided H,h_1,h_2 is polynomial in n,log q and the witness bits; the existence bounds are information theoretic and impose no memory assumption. A coordinate enumeration of the admissible multiplier sets can be exponential in r log C, but neither such enumeration nor any exact-SVP solver is needed to prove the obstruction. This does not show a lower bound on general lattice reduction or exclude approximate cancellation outside the strict output/norm gates, multipliers outside fixed fields, large multipliers, arbitrary nonlinear statistics, or a different source model.

## Separate low-degree supplement to be checked

For coefficient polynomials h_i of degree <k, with no coefficient bound for this algebraic supplement, the exact source hidden amplitudes satisfy

  Pr[exists nonzero (h_1,h_2) mod q with h_1 U_1+h_2 U_2=0]
      <= min(1, k q^(2k-d)/(q-1)).

This holds for every fixed d-subset T, including every zero amplitude pattern. A monic-gcd/projective-pair count supplies the proposed proof; no adaptive stage product is permitted. For public witnesses with |h_i,j|<=C and output coefficient bound B, replace 2nCb by 2kCb in the strict norm gate. This supplement covers a different multiplier family from fixed fields and is not a claim that every degree-k polynomial lies in a degree-k number subfield.
