# B ideal-denominator checkpoint report, v1

Status PROVISIONAL. No standard foundation is established, and no acceptance or completion gate has been passed.

The ideal-denominator algebra works. With the correct row convention, every a in J^-1 has an integral B_J M_a, and coprimality of N(J) with q gives the requested modular factorization. An actual finite source and both full endpoints are frozen in first-test-v1.md. Revealing a useful short denominator basis makes that source easy by an exact box test. D independently checked the relevant proof and added a nonuniform polynomial-catalog obstruction; neither result forbids a hidden exponential ideal family with ordinary public HNF data.

The published ideal-to-NTRU construction also has a concrete fractional interpretation: h=round(qy) has natural lift round(qy)-qy with denominator ideal exactly I. Its known vector-search reduction does not become a decision theorem. Applying the checked decision-to-module transform recovers a direction the ideal reduction already knows and leaves short-vector recovery in I unresolved. The displayed established ideal family also has too large a norm for the simple binary coset bound. These are precise failures of the attempted composition, preserved in ps21-actual-map-v1.md.

A constructive conditional bridge is now frozen as a theorem-only statement and a separate proof. From k quantized periodic-Gaussian samples on R^n/qJ^-1, a public finite sampler produces k inverse-ideal Gaussian residues. Its actual uniform comparator is exactly iid uniform on R_q, even with finite dyadic Gaussian rejection and fallback. Its planted loss is

    2k epsilon/(1-epsilon) + 2pi kn/(Pr) + kn nu.

The sampler uses ordinary ideal arithmetic and scalar Gaussian routines in expected polynomial bit complexity. It never needs a short basis of J. See gaussian-periodic-theorem-v1.md and gaussian-periodic-proof-v1.md; root and D have been asked to audit them.

For the next search edge, the exact query r(T-g)+G modulo qJ^-1 removes the unknown lattice point because r belongs to R. C developed this into a shifted coordinate hidden-center theorem using one-embedding smoothing to full Haar. B checked the two completion normalizers, identified the original logcenter/decay gap, and reviewed C's shifted-center v2 repair. C owns that theorem and its remaining finite oracle-query obligations. B supplied a separate finite elliptical multiplier sampler with explicit theta, mean-precision, and adaptive-call losses in elliptical-multiplier-sampler-v1.md. No correlated Gaussian trapdoor is assumed.

A independently completed a provisional binary-composition packet with proof-only denominator geometry and an explicit polynomial q/target-noise window. Its source matches the exact Gaussian law in B's bridge. This improves the conditional chain, but the checked literature still lacks a standard reduction from arbitrary worst-case ideals to the required low-index ideal family. Renaming that restricted BDD/periodic source would not fill the gap.

The authorized B-IDEN-1 finite control completed and released its reservation. All 160 fractional identities, 12960 denominator probes, and 334084 uniform-output enumerations passed; runtime was about1.254 seconds and peak RSS25036KiB. The control did not test computational hardness. Exact artifacts and resource boundaries are preserved in experiment-record-v1.md. No B experiment is active or reserved.

The claim ledger and primary-source scope are in claims-v1.md and references-v1.md. Earlier B packets remain immutable. The cap and discovery/stop deadlines remain unchanged.
