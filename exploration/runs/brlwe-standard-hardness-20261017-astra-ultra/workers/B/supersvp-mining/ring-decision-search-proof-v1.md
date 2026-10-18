# Proof of B-SUP-DS-T v1

Status: PROVISIONAL. The coefficient convention is R=Z[X]/(X^n+1), ring rows multiply on the right. CRT ideals I_S have support in the designated root set S. Uniform I_S includes zero. All statements concern the full public tuple (W,R,b), retaining the original integer R until an explicitly specified Galois map is applied.

## 1. Publicly samplable calibration

Order the n CRT roots. For each prefix S_j, j=0,...,n, define H_j by drawing a fresh planted degree-ell tuple with uniform secret, then adding to EACH response coordinate an independent uniform I_(S_j) element. H_0 is planted and H_n is the comparator. Write p_j=Pr[D(H_j)=1]. Some adjacent difference has absolute value at least epsilon/n.

Estimate each p_j using Mcal independent fresh challenges and independent D coins. Hoeffding and the stated Mcal give simultaneous error at most a=epsilon/(16n) except probability zeta_cal. Select the adjacent pair with largest absolute estimated difference. Its true absolute gap is at least epsilon/n-4a=3epsilon/(4n)=3gamma/2. Orient the bit test, replacing D by1-D if necessary, so the first hybrid has higher acceptance. Set theta to the midpoint of the two oriented estimates. Its distance from the true midpoint is at most a=gamma/8. Therefore the first true mean is above theta by at least5gamma/8; the second is below theta by at least5gamma/8. Let S be the selected prefix and r* its next root. Calibration is independent of the search input.

## 2. Exact fixed-guess tuple

For a desired root r, choose the automorphism tau:X->X^a with a odd modulo2n such that r*^a=r. Apply tau to every ring entry of an input block, including its integer R and errors implicitly. Then s'=tau(s) satisfies s'(r*)=s(r). Because n is a power of two, tau is a signed coefficient permutation; iid symmetric coefficient Gaussians and the uniform W law are invariant. Integer-constant G is fixed. No assertion is made that arbitrary nonsymmetric coefficient laws are invariant.

For a proposed t in Fq, let e* be the CRT idempotent of r*. Independently draw p_i uniform Rq^h for i<=ell and z uniform Rq. Define

  Vi=Wi+e* p_i,
  c_ij=b_ij+t e* p_i Rj+z(Vi Rj+delta_ij G).

Finally add independent uniform I_S masks to every response coordinate, and call the oriented D on (V,R,c). Algebra gives

  c_ij=(s'+z)(ViRj+delta_ijG)+(t-s'(r*)) e* p_i Rj+e_ij+mask_ij.

The map (W,p)->(V,p) is a bijection on its finite product space. Thus V and p are independent uniform, independent of R,e,z. For this fixed original secret, s'+z is uniform and independent of all these variables.

If t=s(r), the residual vanishes and the FULL query is exactly H_S. If t differs, its scalar factor at r* is nonzero. On the event that concatenated R=[R1|...|Rell] has column rank ell g at r*, every p_i(r*)R(r*) is an independent uniform Fq^(ell g) row, even conditional on V,R,z,e. Hence the residual supplies independent uniform masks at r* to all ell²g outputs. The full conditional query is exactly H_(S union {r*}) conditioned on the same rank event. Conditional independence is proved for the full row, not individual blocks.

Each evaluation of a ring Gaussian coefficient vector has maximum atom at most mu: condition on every coefficient except its constant coefficient. For any nonzero v in Fq^(ell g), one entry v_j is nonzero; condition on all other entries of one R row to get Pr[Rrow*v=0]<=mu. Rows are independent, so Pr[Rv=0]<=mu^h. Union over nonzero v gives rank failure at most rho. The wrong-query law therefore has TV at most rho from H_(S union {r*}), without conditioning the actual algorithm. Its acceptance mean is below theta by at least5gamma/8-rho>=gamma/2. The correct mean is above theta by at least5gamma/8.

## 3. Amplification and all-coordinate recovery

Partition the L indices into N consecutive groups of ell. Keep only the N diagonal square response subarrays, their own W row groups and R column groups. Conditional on the fixed secret, these blocks are independent with the degree-ell planted law: the W groups, R groups and error coordinates are disjoint. Off-diagonal cross-group responses are discarded. Reusing an arbitrary single block would not have this independence guarantee.

For each pair (r,t), run the construction in Section2 on all N blocks with independent p,z,mask and D coins. The resulting bits are independent for this fixed pair and fixed secret. Accept t if their average exceeds theta. Hoeffding with mean margin at least gamma/2 gives per-pair error at most exp(-N gamma²/2)<=zeta_search/(2nq). A union bound over all nq pairs bounds the chance of any incorrect accept/reject by zeta_search. The guesses for different pairs may share the original input and need not be independent. On simultaneous correctness there is exactly one accepted t for each root; CRT interpolation returns s.

## 4. Implementation, source scope and hint bookkeeping

As q is polynomial IN VALUE, root enumeration, nq guesses and automorphism selection are polynomial. CRT interpolation and all other ring operations can also use polynomial-time finite-field linear algebra. Calibration is public: it samples known random secrets, prescribed W/R/errors, and ideal masks; it never asks for extra samples under the challenge secret. All rational width and accuracy encoding lengths count toward runtime. Capped elementary Gaussian/uniform samplers give complete computation error delta_impl; one couples the entire execution, charging its total failure/error once. The strict polynomial D runtime is part of the premise.

No public canonical trapdoor is present in the Decomp input. If D itself first performs the separately frozen triangular/canonical-hint map, its local hint coins are included in D's independent coins and its endpoint loss must first be subtracted from the usable epsilon. One must not append independent canonical hints to a selected (W,R) tuple without the proper map. The uniform secret shifts used here are not valid binary-secret-preserving shifts, so this proof provides no binary hardness conversion.
