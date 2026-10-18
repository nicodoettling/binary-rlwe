# D SuperSVP first partial, v1

2026-10-17. PROVISIONAL primary-source audit, not acceptance of the preprint or a new hardness premise. No experiment run. Source local literature/2026-2443.pdf SHA256 cce6dc039dcecc0eaad5a17768f4cba81b8a6360100eb3a8c878896fc2d770e3; extracted text SHA256 a3cb8c7908d3db070f3d97cb49c3914adef4a13eadb4bcb13aef597f8ebe11e6. Primary pages32,58,64 were rendered locally and visually checked to disambiguate extracted formulas. External ePrint retrieval failed normally; local PDF is the authoritative supplied input.

Use q0 for the original CRT-ideal modulus, Q for the paper's SIS/LWE modulus, and r for its block-copy parameter (called ell in the paper). These are not automatically equal to each other or to the source noise ell.

## Exact initial endpoint ledger

The paper's succinct source has public A uniform in F_Q^(n by m), W uniform in F_Q^(rn by k_aux), and T whose independent columns have the ACTUAL lattice-Gaussian law conditioned on [I_r tensor A | W]T=I_r tensor G. The search variant additionally conditions A to full row rank. The response is s^T A+e^T versus independent uniform, with s uniform in F_Q^n and e iid integer D_chi. T is public and correlated with A,W; it is not free short-basis advice or an unconditioned Gaussian.

The decomposed source publishes W uniform in F_Q^(n by r k_aux), R iid integer D_sigma of size k_aux by r n ceil(log2 Q), and response s^T[W(I_r tensor R)+vec(I_r)^T tensor G]+e^T. It contains m=r^2 n ceil(log2 Q) scalar response coordinates. Comparator response is independent uniform with the SAME joint W,R law. Neither matrix is a uniformly sampled rank-one ring multiplication tuple.

## SuperSVP geometry and elementary solutions

Definition4.1 supplies a basis L of Lambda and a PUBLIC basis P of a superlattice Lambda' containing Lambda^r, with column lengths<=beta and index<=2^k. Output is a nonzero vector in Lambda of ABSOLUTE length<=gamma_prime. This is not an approximation factor unless lambda1 is separately related.

If the quotient has exponent E, multiply any nonzero column of P by E and take a nonzero n-block. This gives a target vector of norm<=E beta. For K_T=q0 J_T* subset Z^n with public hint P=I and r=1, the index is q0^d and exponent q0 when d>0; q0 e_i is an explicit solution. Thus gamma_prime>=q0 is an elementary-easy regime. For d=0 the lattice is Z^n and a unit vector already solves it at bound1. An asserted hardness premise must exclude these regimes and preserve the restricted ideal family, not merely invoke worst-case general SuperSVP.

The exact quotient gadget width is k_Gamma=d ceil(log2 q0). If the number of copies becomes r>1 with natural hint I_(rn), its index becomes q0^(rd), exponent stays q0, and width becomes r d ceil(log2 q0). The r=1 correspondence cannot silently be used after a theorem increases the block degree.

## Parameter compatibility that must be charged

Theorem4.2 supplies sigma0>=2 eta_(2^-(lambda+2))(Lambda) and obtains gamma_prime=4 gamma gamma_det sigma0, where gamma_det=2 m0 n sqrt(r_M). It also requires Q>=4 gamma gamma_det lambda. The target hint width can be the exact k_Gamma or a padded2k; the public trapdoor width s obeys the large bound on page32. Q, p, m and s depend on the ORIGINAL input basis and geometry, not just on n and the quotient entropy.

Theorem7.1 uses m>=max(n log2 Q,4lambda+4), 4sqrt(lambda+ceil(log2(m+1)))<=chi<=Q/[8sqrt(lambda+ceil(log2(m+1)))], and returns SIS bound gamma>=Q sqrt(m)/(2chi), with success at least delta^2-negligible. Combining its gamma bound with Theorem4.2 necessarily gives

    chi>=2 gamma_det lambda sqrt(m),
    gamma_prime>=2 Q gamma_det sigma0 sqrt(m)/chi.

For the restricted q0-exponent family, a nontrivial use additionally requires gamma_prime<q0. Q need not equal q0. These conditions do not by themselves prove the intersection empty; they rule out treating the parameters as independent.

Theorem6.1 is NOT a parameter-preserving same-block search-to-decision theorem. An epsilon-advantage r-block decision solver gives a search solver at block count L=r ceil(32(lambda+2)ln2/epsilon^2). It requires k_aux>=6n ceil(log Q)^2, sigma=Omega(sqrt(n)ceil(log Q)), Q polynomially bounded (not merely log Q), and an ADDITIONAL ordinary decisional-LWE assumption of dimension n ceil(log Q), sample count n L ceil(log Q), error chi and modulus Q. Its wrong-guess comparison is computational under that assumption; it is not an exact uniform simulation. The unpadded small-quotient width O(n) does not meet this k_aux condition when log Q grows. Padding is possible only with its resulting changed parameters explicitly tracked.

## Concrete binary-secret obstruction to the cited chain

Theorem5.1 and Lemma8.8 preserve a supplied secret sampler. Setting that sampler to binary transports an ALREADY ASSUMED binary-secret problem; it does not connect uniform-secret hardness to binary-secret hardness. Lemma8.6 changes the secret to an integer discrete Gaussian, not to bits.

Theorem6.1 randomizes secrets by adding uniform z in F_Q^n. Even if its input secret were binary, the queries are uniform-secret, not binary-secret. A binary-only recovery/decision oracle has no promise on these queries. A new cube-preserving random self-reduction would be needed; none is proved by this theorem.

Theorem7.1 has an even more explicit dependence on uniform secrets. Its proof sums the character over ALL s in F_Q^n, obtaining an exact indicator Ax=0. With a binary secret superposition the same Fourier term is instead

    2^(-n/2) product_j [1+exp(2pi i(Ax)_j/Q)].

For odd Q this product is nonzero for EVERY Ax, since -1 is not a Qth root of unity. Already n=1,Q=3,A=[1],x=1 gives a nonzero factor although Ax!=0. Thus replacing its uniform secret by bits destroys the exact Fourier kernel support used to produce SIS. This is a concrete gap in importing the published proof for binary secrets, not a proof that no other quantum reduction can exist.

The quantum reduction requires coherent access to the solver circuit and its inverse and yields a QUANTUM worst-case solver after composition. A classical-only SuperSVP hardness assumption is not enough for that contrapositive. The pointwise hint law, full-rank conditioning and original uniform-secret law must all remain in the instance distribution.

## Next checks

Continue the actual retained-hint and Gaussian-rerandomization proofs, page32 rounding parameters and the conditional dependence in6.1/8.8. In particular Matrix(W,M) in8.8 cannot depend on the fresh R: choosing it to cancel W(I_r tensor R) into a ring matrix violates the published hypothesis. Coordinate with B on ring-compatible extraction and C on the restricted K_T geometry. No broad impossibility or source hardness is claimed.
