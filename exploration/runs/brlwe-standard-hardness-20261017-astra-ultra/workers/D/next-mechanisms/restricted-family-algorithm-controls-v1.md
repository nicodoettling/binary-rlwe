# Restricted q0-ary ideal family: elementary algorithm controls

PROVISIONAL audit, no security conclusion and no experiment. This concerns J=K_T(q0), q0 split and |T|=d, with D=q0^d<=2^(rho n). The inversion/conjugation in K_T only changes the known root subset. In coefficient coordinates there is a known d-by-n Vandermonde parity check H, H_(i,j)=alpha_i^j, whose roots alpha_i are distinct, and

    J={z in Z^n: H z=0 mod q0}.

No claim is made that this is a generic random dense matrix. Its first d columns form an invertible Vandermonde matrix.

## Polynomial elementary guarantees

For d=0, 1 is a solution. For d>0, q0 e_i is a public solution of norm q0. Thus any promised output radius >=q0 is trivial. Standard systematic elimination gives a basis with d diagonal q0 pivots and balanced off-diagonal entries; this computes J efficiently but does not give a basis below the desired radius.

The polynomial product f_T(X)=product_i(X-alpha_i) mod q0 gives a degree-d relation after centered coefficient lifting. Its guaranteed norm is at most sqrt(1+d(q0-1)^2/4), which is not uniformly below q0 when d grows. Linear elimination on any d+1 coefficient positions gives the same scale. These are upper bounds on these methods, not lower bounds on what their actual outputs can achieve.

Restricting to s<d initial coefficient positions gives full column rank, so the restricted lattice is exactly q0 Z^s; it contains no nonzero vector shorter than q0. For s>=d the determinant is q0^d. The standard LLL determinant guarantee on that s-dimensional lattice is 2^((s-1)/4) q0^(d/s). When d=Theta(n/log n) and q0 is polynomial, d is eventually much larger than sqrt(d log q0). The unconstrained minimizer s=2sqrt(d log2 q0) is below d. Hence this particular certified bound, optimized over permissible s>=d, does not improve the trivial q0 guarantee. This does not prove that LLL fails on a particular T.

The counting fact 2^n>D gives a nonzero {-1,0,1} vector of norm <=sqrt(n) by a collision among binary syndromes. Enumerating those syndromes is exponential; the existence claim is not an efficient syndrome algorithm.

## A rigorous exp(O(d)) control

Fix an integer c>=2 with s=cd<=n, and restrict to the first s coefficients. The lattice

    J_s={z in Z^s: H_[0:s] z=0 mod q0}

has determinant q0^d and an ordinary basis computable in polynomial time. Minkowski's cube argument gives a nonzero vector with Euclidean norm at most sqrt(s) q0^(d/s)=sqrt(cd) q0^(1/c). A slightly weaker bound sqrt(s) ceil(q0^(d/s)) also follows directly by pigeonholing integer box points.

Apply an exact s-dimensional shortest-vector algorithm to J_s and pad the output with n-s zeros. This yields a vector of J at that norm in 2^O(cd) times polynomial input complexity. The primary deterministic single-exponential algorithm is [Micciancio–Voulgaris, A Deterministic Single Exponential Time Algorithm for Most Lattice Problems](https://cseweb.ucsd.edu/~daniele/papers/Voronoi.pdf); only its 2^O(s) exact-SVP guarantee is imported here, not any hardness statement. The author-hosted primary paper was checked directly.

For fixed c and d=Theta(n/log q0)=Theta(n/log n), this is 2^O(n/log n), subexponential in n but not polynomial. If d=O(log n), the same method becomes polynomial and those smaller-codimension subfamilies are easy at the corresponding radius. For a proposed radius R=n^A with A>1/2 and q0<=n^B, choose a fixed c>B/(A-1/2). Then sqrt(cd) q0^(1/c)<R asymptotically, and cd<=n eventually. Thus this exponential-in-d control reaches the polynomial output radii under discussion. For q0 only moderately larger than the fractional chain's large polynomial R_out, c=2 can already suffice; the exact displayed inequality is the required test.

## Scope

These controls identify trivial radii and smaller easy subfamilies. They do not establish a uniform polynomial-time algorithm below q0 for the full d=Theta(n/log q0) family, and they do not prove that no such algorithm exists. Special root sets may admit much shorter explicit polynomials; the worst-case-over-T consequence must account for the full family. This audit provides no security evidence, source-hardness import, or class-changing descent. A stronger claimed restricted-SuperSVP assumption should be stated alongside the above 2^O(d) algorithm and its output bound.
