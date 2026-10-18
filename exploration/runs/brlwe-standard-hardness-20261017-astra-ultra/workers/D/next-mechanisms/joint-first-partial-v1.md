# D joint quotient-preimage first partial

PROVISIONAL; no acceptance authority. Exact source mechanism: B ideal-ring-sis theorem/proof v1 and binary-filter-correction-v1. Root follow-up clarifies that a private hint ignored by binary Rec need not match the published canonical hint law. The public-law comparison below is required only when invoking an external solver promised that law. No new hardness assumption is accepted.

## 1. Exact simultaneous lattice

Let N=n(m+k). Write E=[A|W], and define the R-linear map Gamma:R^k -> R/J by Gamma(v)=sum_l g_l v_l mod J. The quotient bit-generators generate R/J even as an additive group. A generates R_q. Consequently

    F:R^(m+k) -> R_q x R/J,
    F(u,v)=(Au+Wv mod q, Gamma(v))

is surjective: choose v for the second target, then solve for u using A. Its integer kernel L_joint has rank N, determinant q^n D, and index D inside L_q=ker(E mod q). The affine target for correction of r is F^-1(r,0). All bases and membership tests are computable by ordinary integer HNF/SNF. Their shortness does not follow from bit complexity.

The available private corrected lift is

    Lcorr=[Q | VS+B'-g]
         =V[I|R1|R2|S]+[0|E1/q|E2/q|B'-g].

For z=(u,v) in L_joint, Qaug z belongs to J and Gamma(v)=0, so Lcorr z=Qaug z-gv belongs to J. A simultaneous norm bound on B's V-tail event is

    H_joint = sigma n sqrt(h) ell sqrt(1+n^2 h(t+k))
              +(sqrt(n)/q)||[BK|BG]||_F
              + n sqrt(k)||B||_op/(2q).

Indeed each b'_l-g_l has coefficient norm at most sqrt(n)||B||/(2q); negacyclic multiplication contributes another sqrt(n). Thus ||Lcorr z||<=H_joint ||z||, simultaneously for every adaptively selected z.

## 2. A constructive nuance: the quotient constraint alone is easy

It is FALSE that Gamma(v)=0 alone requires a short basis of J. Write R/J as a product of cyclic factors Z/d_i with generators t_i. Let k_i be the binary length of d_i and g_(i,j)=2^j t_i, j=0,...,k_i-1. For constants in the i-th block, the vectors

    2 e_j-e_(j+1) (j<k_i-1),
    binary_digits(d_i)

form a basis of the scalar gadget kernel modulo d_i. The determinant has magnitude d_i: the first relations identify e_j=2^j e_0, and the last imposes d_i e_0=0. Entries are at most 2, and the block Frobenius norm is at most sqrt(6k_i). Taking the block diagonal gives a k-dimensional basis B_g of determinant D and operator norm at most sqrt(6k). Multiplication by each X^a preserves J, so coefficient copies of this basis give an explicit full-rank sublattice of ker Gamma in dimension nk, with determinant D^n and operator norm at most sqrt(6k). This is a sublattice, not generally the entire kernel, whose determinant is D.

One can also obtain a short basis of the ENTIRE ker Gamma in polynomial bit complexity. Compute an ordinary basis H of ker Gamma. For the known short sublattice basis B0, the rational lattice B0^-1 H Z^(nk) contains Z^(nk). Its column HNF can be chosen with diagonal entries <=1 and reduced off-diagonal entries of magnitude <=1: containment of each e_i implies that each reciprocal diagonal is an integer, and the HNF remainder convention bounds the other entries. Multiplying back gives a full basis with operator norm at most nk sqrt(6k). This argument charges complete rational encodings. It is ordinary arithmetic, not a short-vector search in J.

The unresolved step is the INTERSECTION with the mod-q equation. Parameterizing v by the above short quotient-kernel basis produces a new q-ary matrix; the old augmented trapdoor is not a trapdoor for this restricted domain. Its preimages can have nonzero Gamma, which is exactly the missing condition.

## 3. Routine simultaneous sampling and its width cost

Let L0=Z^(nm) x ker Gamma, with the explicit polynomial-norm basis just constructed. Since gcd(D,q)=1, qL0 is contained in L_joint. The same rational-overlattice HNF argument therefore gives a polynomial-time basis of L_joint with norm at most N q times a polynomial in n,k. It supplies a Gaussian sampler at width tau of order q times a polynomial, using an ordinary-basis Gaussian method. This is an algorithmic upper bound; it is not a claim that every simultaneous sampler needs a q factor.

With B's stated ordinary-basis initial Gaussian implementation, sigma>=sqrt(2)a0||B||/q. Combining that floor with the routine tau proportional to q makes the certified output bound H_joint tau sqrt(N) at least a polynomial multiple of ||B||. For a q0-ary ideal in standard HNF, a nontrivial pivot is q0, so ||B||>=q0. This routine guarantee cannot establish an output below the trivial vector q0 in the restricted family. A better simultaneous trapdoor or better initial sampler is a separate algorithmic obligation; sufficient width conditions are not universal lower bounds.

There is a direct check on overly strong proposed repairs. A full short basis Z of L_joint gives ideal vectors Lcorr Z_j. If Lcorr is nonzero, at least one is nonzero because Z is full rank. Their norms are at most H_joint times the basis-column bound. Thus a sufficiently short basis already solves the ideal task without any binary recovery oracle. For an individual preimage sampler, such a conclusion needs a nonzero/output-law argument: a sampler could deliberately return relations in ker Lcorr. Canonical Gaussian joint-kernel sampling admits the same posterior/nonzero analysis as B, because its law depends on private state only through E and fixed J,g.

## 4. Both public response endpoints after changing hints

Fix J,g and a public key E. The original hint column has law D_(F_q^-1(r),tau), where only E z=r mod q is imposed. The proposed new canonical column conditions this law further on Gamma(v)=0. If the original conditional event probability is p_r(E,J), their TV distance is EXACTLY 1-p_r. For conditionally independent gadget columns, it is 1-product_r p_r. Keeping the same E law and then averaging yields the exact full-key distance. Appending either fresh binary S and independent target noise, or an independent uniform response, is the same conditional kernel in the two compared experiments. Therefore EACH full response endpoint has exactly this key-law TV distance. This is not a one-sided planted error.

If tau>=eta_epsilon(L_joint), all joint affine theta masses are within factors 1±epsilon of tau^N/det(L_joint), so

    (1-epsilon)/(D(1+epsilon)) <= p_r <= (1+epsilon)/(D(1-epsilon)).

Naive canonical rejection therefore costs approximately D per column in that regime and strongly changes the published canonical law. Below joint smoothing that probability must be analyzed directly; no 1/D assertion is automatic. If J is hidden and mixed, a pointwise event depending on J does not automatically give the same marginal lower bound after forgetting J. If the new hint remains private and Rec ignores hints, this comparison is unnecessary; only the actual response/secret/noise law supplied to Rec matters.

## 5. Authorized exact control, and preserved reporting defect

D-JOINT-1 used n=2, q=5, J=(1+X), D=2, A=W=1, g=1. This is a valid split-q, low-index, coprime-D example. For one gadget target r=1, use exact Gaussian weights 2^(-||z||^2), corresponding to tau^2=pi/log 2. A four-coordinate residue DP over (u+v mod 5, v(1) mod 2), with truncation [-6,6], took 1053 transitions and 12 MiB peak RSS. Its exact rational tail bound uses

    sum_(|j|>=7) 2^(-j^2) <= 2*2^(-49)/(1-2^(-15)).

The four-variable omitted raw mass is bounded by (rho_trunc+tail)^4-rho_trunc^4. The q-fiber denominator is at least 1/2. Exact rational interval arithmetic gives

    p_1 in [0.5003121541345827,0.5003121541347103],
    TV(single target-1 hint) in [0.49968784586528964,0.49968784586541726].

Displayed decimals are only summaries; exact rational outputs are retained. This already lower-bounds the actual full gadget-key TV by projection to its target-1 column. The code additionally printed a THREE-REPEATED-TARGET-1 number. That is not the law of the published targets 1,2,4 and is rejected as a full gadget-key claim. The original code/input/output are preserved. A separately reserved correction would compute all actual target probabilities; no unreserved second run occurred. This small-width example is an endpoint control, not a claim about B's large published hint width or security.

Current next step: complete the canonical joint-kernel nonzero/width comparison and audit elementary algorithms for the q0-ary restricted family. The extra sampler remains unconstructed at a useful guaranteed radius; no impossibility or security conclusion follows.
