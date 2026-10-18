# A-BIN-FLOOR v1: full-support lower bound on the recovery-interface losses

Status **PROVISIONAL**. This is a corollary of binary-image-obstruction-v1.md and concerns the numerical upper bound supplied by A-ADM, not actual public recovery or all proof methods.

Suppose conditional on any size-d ideal support T, the k ideal points are iid uniform I_T, including zeros, and q^d>n^(n/2). Let Full denote that their union support equals T. Then Pr[Full]=(1-q^-k)^d. For every t>0 and every source-only good event, the A-ADM loss terms satisfy

    delta_bad + beta >= (1-q^-k)^d,

provided delta_bad>=Pr[not Good] and beta is the exact weighted binary-image charge in A-ADM. No independence of Good and Full is required.

Indeed on Full, the binary image is injective by A-BIN, so D_Z=2^n. Since p_t=(1+D_t(0))/2>=1/2, min(1,D_Z p_t^n)=1. Therefore

    delta_bad+beta
       >=Pr[not Good]+Pr[Good and Full]
       >=Pr[Full].

For q>=n² and k>=1 this is >=1-d/q^k>=1-1/n. Consequently the displayed completion/ideal-image recovery bound is intrinsically vacuous in this range, regardless of the chosen mask-norm good event or auxiliary Gaussian width. Conditioning on rare rank-deficient points cannot fix it without paying the complementary bad-event mass.

The companion low-d Gaussian small-ball argument discussed with C is narrower: it concerns C's canonical rounded mask F=Round(nq e). It does not by itself rule out replacing F with another representative modulo P_T and absorbing the difference into the ideal point. That potential representation change must be addressed separately. The present high-d statement is unaffected because uniform ideal points retain the same source law after any mask-dependent ideal translation.
