# WEIGHT-COV-v1 author proof

Let U be a binary vector supported outside coordinates0,1,2,3, of weight w-2; it exists because w<=n-2. Compare the four secrets U+e0+e1, U+e0+e3, U+e2+e1 and U+e2+e3. For arbitrary B=Cov(Z) and L=Cov(Z,Delta),

    V_s=Cov(W_s)=B-M_s L^T-L M_s^T+M_s C M_s^T.

The alternating sum V_01-V_03-V_21+V_23 cancels B, all terms linear in M_s, all baseline-U terms and the individual square terms. The remaining matrix is

    P C Q^T + Q C P^T,   P=I-T^2, Q=T-T^3=T P.

Under the equal-covariance premise this is zero. Diagonalize the real orthogonal negacyclic T by a complex unitary Fourier matrix. Its eigenvalues z_j=exp((2j+1)pi*i/n) satisfy |z_j|=1. In this basis let c_j be the diagonal entries of the Hermitian positive semidefinite C. The j-th diagonal entry of the displayed alternating sum is

    2*|1-z_j^2|^2*Re(z_j)*c_j.

For powers of two n>=4, z_j is never +/-1 and never +/-i: the latter would require2j+1=n/2 modulo n, impossible because n/2 is even. Thus every scalar factor is nonzero and all c_j=0. Positive semidefiniteness implies tr(C)=sum_j c_j=0, hence C=0.

Therefore Delta equals its deterministic mean d almost surely. If the full W_s laws are also equal, finite means imply M_s d is the same for every weight-w secret. Select two weight-w binary vectors differing by e0-e1; possible for1<=w<=n-1. Their mean equality gives(I-T)d=0. Since1 is not an eigenvalue of T, d=0. This proves the second claim.

For w=1 each M_s is an orthogonal power of T. Isotropic centered Gaussian Delta is invariant under these maps, so Z=0 makes all W_s identically distributed. For w=n-1, M_s=M_1-T^j for the omitted coordinate j, and Z=M_1 Delta gives W_s=T^j Delta, again with a common nondegenerate isotropic law. Boundary w=0,n is vacuous. No conclusion about approximate TV follows merely from covariance equality failure; rare large tails can carry variance at small TV cost. No posterior or independent-product assertion is used.
