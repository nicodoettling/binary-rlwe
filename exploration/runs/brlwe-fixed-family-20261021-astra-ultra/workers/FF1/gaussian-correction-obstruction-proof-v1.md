# FF1-COV-v1 proof

Let C=Cov(Delta), B=Cov(Z), and H=Cov(Delta,Z). Direct expansion, retaining cross covariance, gives

    V(S)=B+M_S C M_S^T-M_S H-H^T M_S^T.

The discrete second difference V(1+X)-V(1)-V(X)+V(0) is TC+CT^T. The hypothesis therefore yields TC+CT^T=0. The negacyclic shift is unitarily diagonalizable over C, with eigenvalues zeta_j=exp((2j+1)pi i/n), j=0,...,n-1. In this eigenbasis C'=F C F* is positive semidefinite, and the j-th diagonal of the equation is

    2 Re(zeta_j) C'_(j,j)=0.

For n divisible by four no zeta_j equals +/-i: the equation 2j+1=n/2 modn has an even right side and an odd left side. Hence every Re(zeta_j) is nonzero, every diagonal C'_(j,j) vanishes, and trace(C)=0. A positive semidefinite covariance with zero trace is zero. No inference of coordinate independence is made.

For the explicit equal-weight example, T is orthogonal and T^2+(T^2)^T=0 at n=4. Expanding (I+T)(I+T)^T gives 2I+T+T^T, which is not 2I; expanding I+T^2 gives 2I. This invalidates scalar Hamming-weight variance matching in the ring.

At n=2, take C=cI, H=(c/2)(I-T), and B=cI, c>0. The joint block covariance [[C,H],[H^T,B]] is positive semidefinite because H^T H=(c^2/2)I<=c B. Direct substitution gives V(S)=cI for all binary S. This checks that the excluded degree is a genuine boundary, rather than an artifact of the proof.

Application gate: actual Gaussian rounding has center-dependent theta normalizers and an integer output operation. One may not apply this lemma to that kernel by silently replacing it with an independent Gaussian perturbation. A separate quantitative comparison would be required. This candidate supplies a falsifier for the naive correction design, not a completed lower bound for every normalized kernel.
