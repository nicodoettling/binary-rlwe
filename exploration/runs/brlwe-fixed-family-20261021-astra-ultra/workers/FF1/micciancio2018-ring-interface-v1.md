# Micciancio 2018 sample-extension interface: exact ring obstruction

Primary source read: [On the Hardness of Learning With Errors with Binary Secrets](https://theoryofcomputing.org/articles/v014a013/v014a013.pdf), especially Lemmas 2.6–2.9, Figure 1, Theorem 3.1 and Corollary 3.4. This is an interface analysis, not a reproof or automatic import of the theorem.

## Primary-source facts (summary)

The construction treats ordinary LWE public matrices with independent entries and uses matrix-valued secrets. Its transformation contains X=[Y,G]Q^t diag(z), where z is a sign vector and Q is an integer gadget. Coordinate sign changes preserve independent coefficient Gaussian laws. The proof exchanges sample and parallel-secret dimensions; a column hybrid reduces multiple uniform secrets to one. Its leftover-hash step compresses a longer binary vector into a smaller unrestricted matrix image. Corollary 3.4 permits arbitrary polynomial output sample count with fixed target noise growth. These are ordinary vector-LWE assertions.

## Our exact algebraic obstruction to the direct port

Let T be the n-by-n negacyclic shift, so the coefficient action of rank-one ring public multipliers is the commutative algebra A={f(T):f in F_q[X]/(X^n+1)}. Let D_z=diag(z_0,...,z_(n-1)) for z_i in {+1,-1}, q odd.

Claim: right multiplication by D_z preserves A for every input M_a in A if and only if z is constant. Proof: setting a=1 shows D_z must belong to A, hence commute with T. Comparing each nonzero shift entry in D_z T=T D_z gives z_(i+1)=z_i, including the wrap edge. Thus z is constant. Conversely +/-I preserves A. A uniform sign vector satisfies this with probability2^(1-n).

Explicit n=4 witness: z=(1,1,1,-1). Entry(0,3) of T D_z equals+1, whereas that of D_z T equals-1. They differ modulo every odd q. Thus the independently chosen sign matrix in the ordinary-vector construction does not preserve rank-one ring public multiplication matrices. One cannot group independent output rows into ring samples without changing the promised public law and its within-sample structure.

The scalar +/-1 norm identity is also insufficient for a substitute ring gadget: multiplication by a coefficient sign polynomial has covariance M_z M_z^t, not ||z||^2 I. FF1-COV-v1 supplies the separate exact obstruction for additive Gaussian correction designs. A Gaussian projection theorem requiring orthogonal rows must check those rows at the actual ring block level.

## Our entropy obstruction to a full-ring leftover-hash substitution

For any fixed ring multiplier a, the image of uniform coefficient-binary z under z->az has support at most2^n. In R/qR of cardinalityq^n, its distance from uniform is therefore at least1-2^n/q^n. The same bound holds when a is retained and averaged, since the support test may depend on a. For units the image size is exactly2^n. Thus the full-ring map cannot substitute for the smaller output dimension in the vector leftover-hash step when q>2. This is a support/normalization statement, not a claim about computational hardness.

Partial CRT projections or a smaller subring could have enough entropy room, but they change the algebraic interface. A successful replacement must supply (i) an explicit rectangular ring/module map; (ii) a proof that the final target is rank-one with all n coefficient secret bits uniform; (iii) independent uniform target multipliers; (iv) the full conditional independent coefficient Gaussian law; and (v) effective source transfer with target dimension/modulus/noise fixed before the adversary. None is supplied by the direct matrix import. This escape remains OPEN, not refuted by the diagonal-sign calculation.

## Compatible ingredient and status

The conceptual source-sample/parallel-secret transposition is a useful alternative to the current K-row common-mask completion. It would remove the latter's covariance accumulation if a ring-compatible two-endpoint construction were proved. The existing unrestricted-matrix gadget cannot be called such a construction. This avenue is a substantive exact-interface failure of the direct port, with a specific new gadget interface still open; it is not programme exhaustion.
