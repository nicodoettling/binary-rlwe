# S08 dynamics / public exact sampling — independent development

Run brlwe-explore-20260906-astra-ultra. Started 2026-09-06 09:52:36 UTC. Only context/formal-only.md read initially; barrier/literature release 10:03:00 UTC. Task deadline 10:22:00 UTC. No experiments run.

Question: public transcript Markov kernels that change the hidden secret prior in a controlled way. Ledger remains power-of-two degree n, odd q, rank 1, coefficient basis, m independent uniform ring A_i, independent coefficient D_sigma errors, unless explicitly stated.

## Initial algebra (deduction in progress)

Public translation T_t: retain A_i and replace B_i by B_i+A_i t. Its coupled latent secret is S+t and its error remains E_i. The full input/coin joint law matters; a uniform t makes S+t uniform, but t retained gives a public coupling back to S, while forgetting t loses that recovery relation. This points in the easy binary-to-uniform search reduction direction, not uniform-to-binary hardness.

For a ring automorphism phi and signed monomial u=±X^j, the coefficient map L=u phi is a signed permutation. Define H=sum_j X^j and t=(H-L(H))/2 over the integers. Then s'=L(s)+t preserves the binary cube, with a complemented bit on every negative signed-permutation row. Set A_i'=u^{-1}phi(A_i), B_i'=phi(B_i)+A_i't. Then B_i'=A_i's'+phi(E_i). Coefficient Gaussian noise is invariant under phi. This is a nontrivial public affine cube action, but its orbit is likely polynomially small and cannot resample n independent bits.

Need verify group size, invariant orbit laws, exact global mixing obstruction, and distinguish public transformations from posterior-dependent hidden-secret bit flips.

09:54 UTC: Additional candidates / cautions.

- A fresh uniform public translation is an exact one-step sampler of the uniform secret marginal, even conditional on the incoming secret; fresh translation coins cannot be omitted in reductions that must recover the source. This is an exact coupling, not a hardness implication.
- Normal form from an invertible first A_0: output A_i'=-A_i A_0^{-1}, B_i'=B_i-A_i A_0^{-1}B_0, with S'=E_0 and E_i'=E_i for i>0. Retain A_0,B_0 to recover S from E_0. This consumes a sample and produces a Gaussian secret, not a binary secret. Candidate likely baseline, so do not present as new.
- A multiplicative unit walk makes S uniform over its unit orbit while keeping noise unchanged; zero CRT coordinates / generated ideal remain invariant. Again this is a public easy-direction distribution change, with no known inverse distribution reduction.
- Potential structural contribution: classify all deterministic coordinate signed-permutation isometries that preserve coefficient noise, ring rank one, and the binary cube. The ring multiplication algebra and noise isometry constrain such actions to affine negacyclic index permutations, yielding only polynomial-size orbits. This would be a precise obstruction to public binary heat-bath proposals within this restricted class; it does not rule out general public kernels.

## Mechanism A: affine normalizer walk (fully written small calculation)

Let C={0,1}^n, H=1+X+...+X^{n-1}. For k odd modulo 2n let phi_k(f)=f(X^k) in Z[X]/(X^n+1); choose j modulo 2n and write u=X^j. L_{j,k}=u phi_k is a signed coordinate permutation. Let t_{j,k}=(H-L_{j,k}(H))/2, whose integer coefficients are 0 or 1. Define

S'=u phi_k(S)+t, A_i'=u^{-1}phi_k(A_i), B_i'=phi_k(B_i)+A_i't, E_i'=phi_k(E_i).

The public rule only requires A_i,B_i,j,k. Expanding A_i'S' yields phi_k(A_i S)+A_i't, so the equation is exact modulo q. Conditional on j,k, all A_i' are independent uniform ring elements, all E_i' have independent D_sigma coefficients, and they are independent of S'. Thus arbitrary source prior mu is pushed to L mu+t with the complete standard sample law; n,q,rank,basis,sigma,m unchanged. Averaging over j,k preserves those conditional sample facts.

Center V=2S-H. Then V'=u phi_k(V). These transformations form G=C_{2n} semidirect (Z/2nZ)^* of order 2n^2 for n>=2. A uniform group element sends a fixed S exactly uniformly to its G orbit in one step. Uniform measure on every orbit is stationary; the uniform binary prior is stationary but the chain has at least 2^n/(2n^2) communicating classes. TV distance from uniform binary, starting at one secret, is at least 1-2n^2/2^n. This concerns a secret marginal; repeated transformed transcripts remain correlated and provide no fresh samples.

An optional observable of the centered secret: the multiset {|V(zeta^a)|^2: a odd mod 2n}, zeta=exp(pi i/n), is preserved, since u has unit modulus at every root and k permutes odd a. This is a hidden invariant, not publicly recovered information.

Within deterministic samplewise transforms B'=Q B+M(A')t, S'=P S+t, E'=Q E where P,Q are signed coordinate permutations independent of samples, ring compatibility for every A requires Q M(A)P^{-1}=M(A'). At A=1, QP^{-1} is a signed-permutation ring multiplication, hence a signed monomial. Therefore Q normalizes the negacyclic multiplication algebra. Q M(X)Q^{-1} is again signed-permutation ring multiplication, hence M(±X^k); conjugacy and X^n=-I force k odd (mod 2n). Q is determined by Qe_0 and this k, so Q=±X^h phi_k. Consequently P belongs to the same monomial-semilinear family and the attainable binary-secret moves are within G. This restricted classification does not cover nonlinear, transcript-dependent, multi-sample, or noise-changing kernels. Need check finite-q exceptional identifications and formulate integer-exact scope if necessary.

## Mechanism B: translation intertwining and the reverse-kernel obstruction (deduction)

For public T=(A,B), define K(t|A,B) and output (A,B+A t) with latent S'=S+t. The fresh increment may depend on the public transcript. Write L_s(A,B)=product over i,j of W_{sigma,q}((B_i-A_i s)_j), the positive wrapped likelihood (omitting the common uniform-A factor). For input prior mu, exact output prior pi with unchanged independent error requires, for all A,B',s',

sum_t mu(s'-t) K(t|A,B'-A t)=pi(s').

Derivation: the residual B'-A s' equals the old residual for every summand, so the common positive L_{s'}(A,B') cancels from the full joint law. This is stronger than checking only the output secret marginal. Fresh increments independent of T reduce it to pi=mu*nu.

For full-support mu and any pi with a zero (especially the binary prior when q>2), the equality is impossible: fix s' with pi(s')=0. Positivity forces every K(t|A,B'-A t)=0, and varying B' contradicts stochasticity. Hence no exact public translation kernel, including transcript-dependent ones, maps a full-support prior to the binary prior while preserving this fixed sample/noise law. This is an exact-support obstruction only: it does not exclude negligible statistical distance, altered errors, extra algebraic dimensions, or other reduction architectures.

A uniform fresh t is nevertheless an exact one-step sampler to the uniform secret marginal from any source prior, with unchanged samples/noise. Recoverability is public: S=S'-t. This proves only the easy binary-search-to-uniform-search reduction direction. Conditioning a reverse increment on the latent S would not be a public algorithm.

09:58 UTC refinement: if mu is uniform on all R_q, the translation identity has left side independent of s', so pi must be uniform; the obstruction is stronger than support alone. More generally:

**Public symmetry selection lemma (fully written small calculation).** Let a finite group G act bijectively on secrets and transcripts, with channel likelihood ell_{gs}(gT)=ell_s(T)>0 on the source support and a G-invariant source prior mu(s)>0. Choose g from any public K(g|T), and push (s,T) to (gs,gT). Then

p_out(s',T')=mu(s') ell_{s'}(T') h(T'), where h(T')=sum_g K(g|g^{-1}T').

This follows by substituting g^{-1}s',g^{-1}T' in each summand and invoking the two invariances. If the output has the same channel with another prior pi, cancellation gives pi(s')/mu(s')=h(T') for every source s',T'. Positivity forces this ratio constant, so pi=mu. Thus even transcript-adaptive selection among exact channel symmetries cannot bias an invariant prior while preserving the full joint channel. Uniform ring prior + translations, or uniform binary prior + the affine normalizer group, instantiate this. Rejection only adds a global normalization and has the same conclusion if successful outputs are required to retain the same channel jointly.

Caution: matching only the transcript marginal does not establish this latent coupling. The strict-positivity argument provides no useful approximate lower bound when Gaussian tail probabilities are tiny; it cannot rule out statistical reductions or non-symmetry transformations.

Boundary comparison to check at release: ordinary scalar LWE permits arbitrary coordinate signed permutations of S by transforming columns of its arbitrary A matrix, so independent binary bit flips are publicly executable there. Rank-one ring A matrices are constrained to the negacyclic multiplication algebra; arbitrary column signs leave that algebra. Selecting one coefficient equation from each ring sample yields m ordinary scalar LWE samples of dimension n, after which those moves are valid, but changes the sample structure and loses the other correlated equations. It gives no method for packing independent scalar rows back into uniform ring samples. This is the concrete rank/basis distinction behind the restricted orbit obstruction.

## Sharpening the restricted classification (fully written small calculation)

If an affine map s↦Ps+t is a bijection of {0,1}^n modulo odd q, evaluating it at s=0 and at each basis vector shows that a row with t_r=0 has nonzero entries only +1 and a row with t_r=1 has nonzero entries only -1. Two nonzero entries in the same row produce respectively 2 or -1 at a binary input, outside {0,1} for every odd q>=3. Thus each row has at most one nonzero entry; bijectivity forces P to be a signed permutation. (This derivation assumes the affine formula on the whole cube; no full-ring invertibility assumption is needed once cube bijectivity is imposed.)

Let C=M(X). From Q M(A)P^{-1} in the ring algebra for every A, A=1 gives QP^{-1}=M(c). Since QP^{-1} is signed permutation, its first column shows c=±X^r and M(c)=C^h. Consequently Q normalizes the algebra and Q C Q^{-1}=C^k. Conjugacy preserves order 2n, hence k is odd modulo 2n. Write Qe_0=C^r e_0. Then Qe_j=Q C^j e_0=C^{kj+r}e_0, so Q=C^r phi_k and P also lies in the same family. The argument works modulo every odd q, including composite q, because a signed-permutation ring multiplication has precisely a signed monomial first column and C retains order 2n.

The actual A mechanism chooses Q=phi_k and P=X^j phi_k; allowing another monomial in Q can change the error rotation but does not enlarge the secret action G. Full transcript chains might have further orbit constraints. The claimed exact one-step uniformity is explicitly for the hidden secret orbit under independently uniform G, not an assertion of fresh transcript generation from a fixed transcript.

Approximation caveat: strict positivity is supplied by wrapped W_{sigma,q}; replacing it by an unwrapped bounded-distance test would destroy the exact support proof. The overlap lower bounds obtained from min W can be negligibly small, so no approximate-hardness lower bound is asserted.

Falsifiable next target: exhibit a public recoverable binary-secret move outside G (for example a single coordinate flip for n>=4), retain m independent uniform rank-one ring samples and iid coefficient D_sigma errors in the full output joint law, and explain a polynomial mixing guarantee for the group/kernel it generates. Arbitrary column sign flips give this in scalar LWE but do not preserve the ring multiplication algebra. An exact transcript sampler that discards the source secret is easy and does not answer this target. No experiment is needed to check the group cardinality bound; a cheap future diagnostic is n=8 orbit enumeration and a symbolic expansion of the full likelihood for any proposed extra move.
