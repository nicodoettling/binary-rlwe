# Same-class bounded-index normalization: asymptotic counting obstruction

PROVISIONAL new theorem, not accepted. This only concerns preserving an ideal class in the same power-two cyclotomic field. It is not a barrier to class-changing reductions, field changes, dimension lifting, oracle-assisted transformations, or the original computational goal.

Let n tend to infinity through powers of two, K_n=Q(zeta_(2n)), and R_n its ring of integers. Fix a constant c>0. Let C_n(c) be the set of ordinary ideal classes containing an integral ideal J with N(J)<=exp(c n). Then

    |C_n(c)|/h(K_n) <= exp(-(1/4+o(1)) n log n).

In particular, for all sufficiently large n some ideal classes have no integral representative of norm at most 2^(rho n), for any fixed rho>0. No algorithm can normalize every ideal to this bound by multiplication by a nonzero field element. The threshold is asymptotic and no effective starting n is claimed.

Imported analytic premise: the unconditional normal-field Brauer-Siegel theorem: along normal number fields F with [F:Q]/log|Delta_F| tending to zero, log(h_F Reg_F) is asymptotic to one half log|Delta_F|. This exact version is stated as Theorem 1 in Timo Lepistö, Two remarks concerning Dirichlet's L-functions, Ann. Acad. Sci. Fenn. A I 433, printed July 1968, page 3, citing Brauer 1950, pages 739-746. The original Brauer proof is not re-proved here. The primary research PDF was independently opened at https://www.acadsci.fi/mathematica/1969/no433pp01-08.pdf . No GRH premise is used for this theorem.

Proof is in same-class-count-proof-v1.md. Full nonauthor, source and blind review remain open. This result would only redirect a named normalization attempt; it would not complete or block the computational-foundation goal.
