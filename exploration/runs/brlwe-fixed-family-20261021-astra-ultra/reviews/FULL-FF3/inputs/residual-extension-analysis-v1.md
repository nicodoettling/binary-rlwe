# Residual-coordinate extension: exact restriction and remaining coupled escape

Author analysis, PROVISIONAL. This restricts the independent residual-channel design, not all normalized channels. The exact finite LP certificates already show that some coupled channels exist.

For the four candidate secrets0,1,X,1+X, every residual tuple from a pair(a,b) satisfies

    u0-u1-uX+u1X=0.

Suppose a design applies the SAME scalar/ring kernel H separately and independently to these four residuals and insists that the four outputs are residuals of one target pair(c,d) with probability1. Take input a=0,b=u. Then all four inputs equal u, so the four outputs are independent draws from H(u,·). If H(u,·) has two distinct support points v,w, choose any fixed positive-mass values for the last three outputs. At most one of v,w for the first output can satisfy the displayed affine equation. Therefore the forbidden output has positive probability. H(u,·) must be a point mass for every u. This argument uses support and exact normalization, not covariance.

If H must also map a uniform ring of cardinalityQ^n to a uniform ring of cardinalityq^n, its deterministic fibers all have cardinalityQ^n/q^n. In particular distinct prime Q,q exclude such a deterministic kernel. Thus the independent four-residual extension cannot simultaneously satisfy the affine relation and uniform endpoint in that setting. The FV4 control gives an explicit rational failure at source(a,b)=(0,0), with output tuple0,0,0,(1,0) of probability9005442705/208827064576.

This does NOT reject correlated residual sampling. A candidate joint law is

    W_x(c,d) = product_(t in T) H(b-a*t, d-c*t),
    K_x(c,d)=W_x(c,d)/Z(x),
    Z(x)=sum_(c,d) W_x(c,d),

for a chosen collection T of candidate secrets, provided Z(x)>0. This is normalized and always has compatible residuals. However normalizing each source row changes the source-weighted output measure. Neither

    sum_x U(x)K_x(c,d)=V(c,d)

nor the fixed-secret planted identities follows from the separate uniform/noise identities for H. Every Z(x) is load-bearing. Conditioning an independent residual product onto the affine subspace without these checks repeats the forbidden posterior normalization shortcut.

For T={0,1,X,1+X} and coefficient-product H, local negacyclic adjacency might permit a polynomial transfer-matrix computation of Z and conditional samples (after fixing boundary states). This only addresses computation for four secrets; it does not establish the endpoint identities for those four or for all2^n binary secrets. With all cube residuals, direct evaluation has2^n factors and q^(2n) output states. An efficient factorization remains unidentified.

FV2/FV3 unrestricted kernels preserve both endpoints with fully coupled randomness and need not have this product form. Their finite tables therefore show that the independent-residual restriction is substantive. They supply no efficient asymptotic representation.

Invariant-assisted Gaussian correction is a separate route. A ring covariance complement depends on M_S C M_S^T (and cross terms), so a Hamming-weight-only invariant is insufficient in n>=4. If a supplied invariant permits correction, the source comparison must condition the actual binary secret distribution on that invariant and must retain the posterior law of the common latent mask G. An invariant that leaves only polynomial-size secret fibers does not preserve an exponential guessing bound. No outer wrapper knowledge becomes free advice to the recovery algorithm.
