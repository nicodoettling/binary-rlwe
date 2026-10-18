# A-ADM v1 author proof

Status: **PROVISIONAL**, pending full nonauthor/source/complexity and fresh blind reviews. Frozen statement: admissible-theorem-only-v1.md.

Fix any positive-mass good latent state z. Write M=M(z), p=mn and

    B=sigma² I_p-t²MM^T >=3sigma² I_p/4,
    Theta=t²I_n-(t^4/sigma²)M^TM >=3t²I_n/4.

Independently of fresh S,G, conditional on z draw the proof-only integer vector H with mass proportional to exp(-pi h^T B^-1 h). Completing the square gives

    ||g||²/t² +(e-Mg)^T B^-1(e-Mg)
      =||e||²/sigma² +(g-mu_e)^T Theta^-1(g-mu_e),
    mu_e=(t²/sigma²)M^T e.

Poisson summation bounds the shifted Theta lattice sum divided by sqrt(det Theta) between 1-Delta_t and 1+Delta_t. Hence the normalized law of MG+H is

    D_sigma^p(e) r_e / E_(D_sigma^p)[r],

and its full-vector TV from D_sigma^p is at most eta_t. The normalizer is retained and the Delta_t>=1 guard gives the universal bound. The calculation is pointwise in z; it therefore retains Z and independent S while integrating out H. No claim is made that H can remain attached to the independent-noise comparison.

The resulting completed transcript has responses

    U_j S+F_j(S+G)+H_j.

Reveal (Z,H,Y=S+G modulo q,L_Z(S)), where L_z(s)=(U_j(z)s)_j. These data determine V and the complete transcript. Conditional on any (Z=z,H=h), the original joint law of S,G is unchanged. This holds even when Good selected a rare source branch, since Good only depends on Z. For each fixed z and observation y, summing maxima of the UNNORMALIZED joint masses across leakage fibers yields

    P_guess(S | Y,L_z(S)) <= D_z P_guess(S | Y).

It is also at most one. For integer Y=S+G, product structure before leakage gives P_guess=p_t^n: in one coordinate the symmetric unimodal D_t law satisfies sum_y max(D_t(y),D_t(y-1))=1+D_t(0). Reducing Y modulo q can only reduce guessing power. Average the pointwise bound over good z to obtain beta. On bad source states success is at most one. The good-state comparison contributes at most Pr[Good] eta_t<=eta_t. This gives planted acceptance <=delta_bad+beta+eta_t.

At the comparator endpoint independently append S and the entire iid E vector, then compute responses. The displayed full comparator changes the actual-witness recovery probability by at most delta_cmp. Absolute source advantage bounds comparator acceptance by planted acceptance plus Adv_(P,Q)(B_Q). Combining gives the claimed inequality.

The common ideal implies |image(L_z on all R)|<=q^|T|, but only the binary-image cardinality is needed. There is no charge for the number of possible latent supports because the estimate holds separately at every z before averaging. Likewise metadata V is already determined by Z and creates no additional planted leakage about the fresh S. Its computational usefulness is limited by its separate comparator requirement.

No selected posterior product, latent rejection sampler or unit conditioning is used. The only bit-product calculation precedes leakage; the leakage inequality is pointwise in unnormalized masses. Thus CP-1's selected-stage product remains false and is not a proof step here. Full finite-support controls are recorded separately; they cannot certify the infinite Gaussian identity or source hardness.
