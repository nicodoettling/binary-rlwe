# Initial SV report, 2026-10-21 18:05 UTC

Delivered before the 18:08:10 UTC initial gate. FF is not evaluated here. Source diagnostic has substantive PROVISIONAL family theorems; source hardness remains OPEN. No scientific termination is requested.

The exact accepted source radius is

    r=epsilon_*ell²/(1024 nKchi Qmax),
    K=k0(Ncal+Ntest), ell=ceil(log2(2nK)),
    Ncal=ceil(32768n² epsilon_*^-2 ceil(log2(1024(n+1)/epsilon_*))),
    Ntest=ceil(32768n² epsilon_*^-2 ceil(log2(1024Qmax/epsilon_*))).

All auxiliary/sample/advantage losses are retained. Its accepted width guard implies r<1/(2sqrt(n)) uniformly in the finite domain. See parameter-table-v1.md for the exact algorithm comparisons and asymptotic qualifications.

Two frozen candidates now provide new useful classification:

* SV-BDD-CLASS v1 (`source-classification-theorem-v1.md`, `source-classification-proof-v1.md`): direct exponent and effective-member rounding; HNF maximum equals quotient exponent for ideals; all polynomial NUMERIC index families are easy via an explicit ternary collision. It additionally proves e<=2D^(1/F) for supported families of odd residue degree at leastF. This is direct BDD, not an invalid reversal of wide DGS simulation.
* SV-FROB-PRIME v1 (`frobenius-prime-theorem-v1.md`, `frobenius-prime-proof-v1.md`): EVERY eligible prime ideal with polynomial NUMERIC characteristic p is easy from an ordinary basis, even when D=p^f is exponential or p exceeds the exponent-rounding threshold. Signed Frobenius invariants have rankg=n/f and residue image exactlyF_p; eligibility gives p<2^g. Enumerating p+1 invariant binary sums yields an effective nonzero ternary ideal member of norm<=sqrt(n), then direct rounding decodes.

The new prime theorem strictly strengthens the polynomial-index diagnosis: for n growing, p=3 and residue degree n/2 give D=3^(n/2), while the construction uses just four candidate fixed-lattice vectors. It is a broad characteristic family theorem, not evidence that one explicitly generated ideal is easy. Remaining prime candidates after this theorem require superpolynomial numeric p for the stated uniform polynomial-time guarantee. They still may be easy by other methods; no hardness premise or lower bound is claimed.

Finite evidence is registered and retained in experiments/. SV-FV1: exit0,0.94s,48128KiB; six ideals/eighteen basis presentations,8640 scalar/108 member decodes,twelve collisions,two strict-boundary rejections. SV-FV2: exit0,1.06s,50176KiB; nine prime cases n<=32,p<=97,42 sign-conflicted cycles, exact fixed-rank/residue-image/collision/decoding controls. Both had120s wall and512MiB address limits. No slot remains occupied. These are finite checks, not certifications.

Primary cyclotomic inputs were checked against Milne Proposition6.2 and Example8.18 and Weston PropositionIII.3.3; see primary-source-check-v1.md. Historical M1, complementary-multiplier and integral-map obstructions are retained. No new DGS composition or independent hardness transfer is asserted. All203 DD regressions remain centrally retained, with local relevance mapping to follow.

Next substantive work: extend the effective invariant-lattice collision method to prime powers and composite ideals via the computable Galois stabilizer and fixed-field contraction. Separately expose the remaining superpolynomial-characteristic split-prime source in exact ordinary coordinates, and test whether any known effective hardness map reaches it without recreating the complementary-short-object gap. Full and fresh blind reviews remain coordinator-owned gates.
