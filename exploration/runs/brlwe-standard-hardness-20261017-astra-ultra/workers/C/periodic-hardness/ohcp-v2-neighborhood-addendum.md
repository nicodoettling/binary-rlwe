# Required neighborhood addendum to OHCP v2

PROVISIONAL. This addendum is part of the v2 packet and must be included in fresh review. The frozen theorem/proof bytes remain unchanged.

B's review agrees that the shifted-center construction repairs v1's decay mismatch. It requests a stronger posterior domain to cover both formulations of the OHCP oracle conditions. The center-neighborhood bound in v2 is |z-z*|<=3(1+1/kappa)<=6. The BRST Lipschitz condition also refers to an origin-centered ball |z|<=3(1+1/kappa); because |z*|<=3 this permits |z-z*|<=6+3/kappa. Therefore certify the posterior comparison on the union by using the conservative residual bound |h_j|<=8d0 throughout.

This stronger bound holds with the same parameters:

    8d0 = delta*w/(4nk v0) <= w/(2 eta_epsilon(R)),

using delta<=1,n>=2,k>=1,v0>=2eta. All unselected residuals remain bounded by d0. No change is needed to the central excursion (selected residual<=3d0), radial profile, decay, or reconstruction. The addendum closes a domain-accounting omission; it does not change the theorem's decoding radius or introduce a new hardness premise.
