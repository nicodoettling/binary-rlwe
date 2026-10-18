# D primary SuperSVP first-pass audit

2026-10-17. PROVISIONAL independent primary-source audit; no experiment, no acceptance authority. This supplements first-partial-v1.md and exact-controls-v1.md. Primary supplied PDF literature/2026-2443.pdf SHA256 cce6dc039dcecc0eaad5a17768f4cba81b8a6360100eb3a8c878896fc2d770e3; extracted text SHA256 a3cb8c7908d3db070f3d97cb49c3914adef4a13eadb4bcb13aef597f8ebe11e6. Ambiguous formulas on pages32,58,64 were checked against rendered primary pages. No theorem acceptance is inferred from author prose or an abstract.

## Main disposition

The paper supplies useful public-hint and quotient bookkeeping and several explicit dense-matrix reductions. No reviewed theorem directly yields the original uniform-multiplier, binary rank-one ring-LWE target. Two concrete obstacles are the off-promise uniform-secret queries of6.1 and the exact full-field Fourier identity of7.1. The arbitrary secret sampler in5.1 and8.8 preserves a secret law already assumed at the starting endpoint; choosing it binary would assume the missing binary premise. The small-secret result8.6 reaches a Gaussian, not the cube.

The restricted ideal-SuperSVP interpretation is meaningful as a separately stated nonstandard consequence if A/B/C and the quantum import pass review. General SuperSVP hardness does not establish hardness on those special ideal pairs. Its nontrivial absolute-output regime is not ruled out merely by the exponent-q0 vector; one must calculate the radius before drawing that conclusion.

## Distinct source and target interfaces

Write N for a rank-one ring degree and n for the paper's matrix-secret dimension; these need not be equal. The original target has one shared S in{0,1}^N, k independent uniform multipliers in R_q=F_q[X]/(X^N+1), and k independent coefficient-Gaussian errors of the prescribed width. The comparator has the same multiplier law and independent uniform responses. A ring-linear expansion into coefficient matrices has N rows and kN columns but only kN freely chosen multiplier coefficients, rather than kN^2 independent matrix entries.

The paper's succinct source instead has uniform dense A in F_Q^(n by m), independent uniform W in F_Q^(rn by k_aux), and public canonical Gaussian preimages T satisfying[I_r tensor A | W]T=I_r tensor G. The secret is uniform in F_Q^n unless another sampler is explicitly supplied; errors have independent D_Z,chi coordinates. Search uses full-row-rank conditioning on A. Hints are part of the joint law and cannot be replaced by arbitrary short vectors satisfying the same equation.

The decomposed law publishes W in F_Q^(n by r k_aux) and Gaussian R in Z^(k_aux by r n ceil(log2 Q)); its response has r^2 n ceil(log2 Q) coordinates under the same secret. Its comparator keeps exactly these W,R and replaces the whole response by independent uniform. These laws are neither ordinary RLWE pairs nor ring multiplication matrices.

For a fixed coefficient basis, a uniform dense N by kN matrix lies in the negacyclic block-multiplication subspace with probability Q^(-kN(N-1)). Conditioning dense A to full row rank only divides this by its full-rank probability. This is a simple exact law check, not an impossibility result for arbitrary adaptive transformations or changes of dimension. B's new ring-specific extraction avoids this syntax substitution but needs its own ring-structured starting law and hardness edge.

## SuperSVP hint, exponent and complete parameter map

Definition4.1 provides a rational basis B of Lambda and a public short basis P of Lambda' containing Lambda^r. It promises max column norm(P)<=beta and index<=2^kappa_index. The required nonzero output has absolute norm at most gamma_prime. No hidden shortest-vector normalization is part of that definition.

If the quotient exponent is E, E times a nonzero hint column belongs to Lambda^r; a nonzero block gives a vector in Lambda of norm<=E beta. For K_T=q0 preimage(I_T)^{*coef} subset Z^n, the rank-one hint I_n has beta1, indexq0^d and exponentq0 (d>0). Thus output radius>=q0 is elementary. At d0 the lattice is Z^n. For r copies with the natural hint, index becomesq0^(rd), exact quotient gadget width becomes r d ceil(log2 q0), while exponent staysq0. Block amplification cannot retain the rank-one index ledger.

Primary4.2 uses a supplied sigma0>=2 eta_(2^-(lambda+2))(Lambda), depending on geometry as well as security. Using spectral norms in that section, its fixed parameters are

    p>=max(1,6||B||||B^-1||sqrt(r n)/sigma0),
    Q>=17 max(1,kappa_index||B||,p beta sqrt(r)n^(3/2)||B||/sigma0),
    r_M=ceil log2(Q||B^-1||sqrt(r n)/p+2p beta sqrt(r)n^(3/2)),
    m0=ceil(3n ceil(log2 Q)+4lambda+2log2(2n r_M+2r kappa_index)),
    m=m0+n+n r_M,
    gamma_det=2m0 n sqrt(r_M),
    s_hint>=(r m+2kappa_index)(2p beta n sqrt(r)+n r_M+2kappa_index)log(r n).

It also requires Q>=4 gamma gamma_det lambda and returns radius gamma_prime=4 gamma gamma_det sigma0. The exact hint width is the sum of ceil(log2 invariant factor), bounded by2kappa_index; padding is an explicit option, not a free change of public distribution. All original-basis dependencies stay fixed through its basis-improvement rounds.

For the special q0-ary K_T, a coefficient permutation gives an ordinary systematic basis[[I,0],[B0,q0I]], with centered entries of B0 bounded byq0/2. Its norm is O(nq0), and its inverse has norm O(n). Thus these particular basis-size parameters can be polynomial for polynomialq0. This does not imply that arbitrary worst-case bases or ideals have the same bounds.

Combining4.2 with7.1's gamma>=Q sqrt(m)/(2chi) requires chi>=2gamma_det lambda sqrt(m) and gives gamma_prime>=2Q gamma_det sigma0 sqrt(m)/chi. Since7.1 also has chi<=Q/(8sqrt(H)), H=lambda+ceil(log2(m+1)), a nontrivial radius belowq0 needs q0>16gamma_det sigma0 sqrt(mH). These inequalities do not prove an empty intersection: a sufficiently large polynomialq0 and appropriately largerQ can preserve the window. Keeping Q,q0 and the original binary-target q distinct is essential. In particular, the fractional bridge with denominator indexq0^d requires gcd(q0,q)=1.

## Theorem6.1: full query laws, samples and extra premise

A decision solver on r blocks with advantage epsilon yields search only on L=r ceil(32(lambda+2)ln2/epsilon^2) blocks. It needs k_aux>=6n ceil(logQ)^2, sigma=Omega(sqrt(n)ceil(logQ)), and Q itself polynomially bounded. The additional assumed decisional-LWE problem has dimension n ceil(logQ), sample count nL ceil(logQ), modulusQ and errorchi. This extra premise must be listed; it is not an exact-uniform simulation fact.

For each coordinate i and guess t the map uses fresh z uniformF_Q^n and p uniformF_Q^(L k_aux), replaces W byV=W+e_i p^T, and produces the response under secret s+z plus residual(t-s_i)p^T(I_L tensor R). Conditional on a fixed query, the public pair(V,p) is jointly uniform by a bijection. At the correct guess the endpoint is EXACTLY planted with uniform secret. At a wrong guess the residual is computationally pseudorandom under the cited NLWE/ordinary-LWE premise, retaining R. The endpoint is not statistically uniform.

Amplification splits disjoint diagonal block groups of W,R and the response. Conditional on a fixed secret those groups have independent input coins. Independent uniform secret masks then make the transformed secrets independent uniform, justifying concentration. Different coordinate/guess queries reuse the original W,R,error and can remain correlated. The proof uses a union bound over polynomially many nQ queries, which is valid without asserting their independence. This is consistent with CP1; no product of selected-event marginals is needed.

For a binary-only oracle, the same secret shifts are off-promise. The theorem does not supply a cube-preserving random self-reduction. Its k_aux bound also exceeds the unpadded O(n) low-index quotient width when logQ grows; padding changes the actual hint and subsequent width ledger.

## Theorem7.1: uniform secret and quantum access

The search theorem uses m>=max(nlog2Q,4lambda+4),

    4sqrt(lambda+ceil(log2(m+1)))<=chi<=Q/[8sqrt(lambda+ceil(log2(m+1)))].

A solver successdelta yields quantum SIS success at leastdelta^2-negligible, using the solver circuit coherently and in reverse. A classical-only worst-case hardness premise is insufficient for the resulting quantum contrapositive. Full-row-rank A is used to erase the secret register reversibly.

The proof's reference Fourier vector has support only on Ax=0 because it sums over every secret inF_Q^n. Binary substitution gives a product of(1+Qth root of unity), with no zero factor whenQ is odd. More quantitatively, exact-controls-v1.md proves that the expected mass of this reference vector on ANY nonzero-kernel solution set is at most(2/Q)^n. This is a failure of that proof template, not a refutation of the published uniform-secret theorem or a universal quantum impossibility claim.

## Theorems5.1,8.6,8.8: law preservation and hint erasure

Theorem5.1 maps a decomposed instance to a succinct instance, preserving any supplied secret sampler. Its proof correctly first resamples the hint canonically conditional on the complete retained(W,R,secret,error,X,rerandomization coins) state, then rerandomizes the response, and only then compares public matrices through a channel that generates a fresh canonical hint from those new matrices. Keeping the original R,X and private short preimage in the final public endpoint would invalidate that last channel argument. The response rerandomization is statistical and its noise growth is explicit; it is not an exact Gaussian identity.

Lemma8.6 uses extra fresh public columns M and chooses an invertible pivot C using M only. The new secret is the corresponding independent error vector, distributedD_Z^n,chi', with chi'>=4chi sqrt(m(n+lambda)); its output error has the same Gaussian width. It canonically resamples the public hint for the transformed target. The comparator response remains uniform through the independent original response. It does not reach binary secrets.

For its wrapped Gaussian secret, each coefficient atom is at most1/chi'+1/Q by shifted Gaussian mass maximality and rho_chi'(Z)>=chi'. Hence any fixed global bijection followed by restriction to a2^n-point cube has probability at most[2/chi'+2/Q]^n. For the stated growingchi' and oddQ>=3 this is exponentially small. This proves a loss for that restriction strategy; it does not rule out adaptive reductions.

Lemma8.8 permits a deterministic offsetF=Matrix(W,M), explicitly independent of the subsequently sampledR. ChoosingF to cancel W(I tensor R) into a ring matrix violates the hypothesis. Its actual proof keeps the sampled R marginal independent only after a charged smoothing comparison of conditional preimage cosets; the uniform comparator uses an augmented random matrix[A;h] and must retain the public(W,R,M) law. Merely obtaining the same marginal response does not reproduce it.

## Current constructive fragments and boundaries

B's separate ring collision identity and triangular endpoint map have been read. The exact CRT-support sum and conditional-column extraction address the failure of treating the ring hash as two-universal; the triangular map preserves a supplied secret law. No immediate algebraic defect was found in that read. This is not a complete independent audit of its Gaussian-preimage implementation and does not import standard ring-source hardness.

C's restricted-ideal consequence has a nontrivial absolute-radius window. Its exact v1 example zeta=e^-kappa contradicted kappa>=log(8n/zeta); this control is preserved. Fresh v2 SHA59ed430839b218c0bc915228251b0b5b59038d86a16787e6774b89ba38aaf75b changes to zeta=e^(-kappa/2), kappa>=2log(8n), repairing the contradiction without changing the radius order. Its analytic dependencies should now be labeled B-GP-v2 and C-OHCP-v5. The primary quantum BDD-to-DGS import and same-family premise remain separate from the present paper's dense endpoint theorems.

No compatible published standard-hardness-to-original-binary-rank-one-ring chain has emerged from this first pass. The useful next constructive object is a fully specified ring-hinted source with its exact lift and nonzero proof, not a syntax replacement inside a dense-matrix theorem. B has supplied such a new ideal-ring-SIS packet for further adversarial review; all new claims remain provisional.
