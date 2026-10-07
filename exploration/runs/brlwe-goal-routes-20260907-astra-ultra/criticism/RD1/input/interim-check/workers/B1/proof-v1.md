# B1 proof attempts and source comparison v1

Frozen statement: [statement-v1.md](statement-v1.md). Status: PROVISIONAL, pending nonauthor review. Imported X1/NC1 and the observable bridge remain version-specific mathematical dependencies; source hardness is an explicit assumption.

## 1. Actual factor degrees and the binomial family

For any odd prime q and n=2^m, the derivative nX^(n-1) is coprime to X^n+1 over F_q. Every root alpha of X^n+1 has exact multiplicative order 2n: its order divides 2n but does not divide n, and 2n is a power of two. Frobenius acts by alpha->alpha^q, so every orbit has length ord_(2n)(q). Every irreducible factor therefore has exactly that degree. For m>=2, this degree is a power of two dividing n/2, because the exponent of (Z/2^(m+1)Z)^* is 2^(m-1). In particular neither a generic degree nor an extension coefficient field may be substituted.

If q=1 modulo 4 and s=v2(q-1), repeated squaring gives v2(q^(2^r)-1)=s+r. Multiplication of the exponent by an odd number leaves this valuation unchanged, by the factorization (z^u-1)/(z-1)=1+...+z^(u-1), an odd sum of odd terms. Therefore ord_(2^(m+1))(q)=2^max(0,m+1-s). For completeness, q=3 modulo 4 instead gives order 2^max(1,m+1-v2(q+1)) when m>=2. The construction uses only the first case, with s=m+1-j>=2, so f=2^j exactly.

Since 2N=2n/f divides q-1, T^N+1 splits into N distinct linear factors T-a over F_q, all a of order 2N. Substitution T=X^f gives the identity

X^n+1=product_(a in A)(X^f-a).

Each root of each displayed binomial is a root of X^n+1 and thus has Frobenius orbit length f. A degree-f binomial having such a root is consequently its minimal polynomial. The N binomials are irreducible and distinct. This proves B1-ALG-v1 without a separate binomial irreducibility theorem.

Selecting k binomials gives R/J_K isomorphic to product_(a in K) F_q[X]/(X^f-a). Each component has q^f elements. Therefore |R/J_K|=q^(kf), not q^k, and D=kf is the total quotient degree. The full ring has N factors; k counts selected factors; f counts the degree of each selected factor.

## 2. Exact coefficient decomposition and source packing

Every polynomial S of degree<n has a unique expression

S(X)=sum_(r=0)^(f-1) X^r S_r(X^f),
S_r(T)=sum_(t=0)^(N-1) S_(r+ft) T^t.

This is a permutation of n coefficients. Modulo X^f-a, its image is sum_(r<f) X^r S_r(a), whose coefficients in the basis 1,X,...,X^(f-1) are precisely (S_r(a))_r. These are an F_q basis because the binomial is irreducible. Thus the quotient coordinate for a vanishes if and only if every S_r(a) vanishes.

Consequently S is supported only on K in the original CRT if and only if each S_r belongs to I'_K. The coefficient permutation is an F_q-linear bijection (I'_K)^f -> I_K. Independent uniforms on I'_K map to uniform I_K. Two disjoint groups of f points give independent uniforms conditional K. Independent coefficient D_tau errors retain exactly their n-coordinate product law under the permutation. Uniform (R')^(2f) likewise maps to uniform R^2. This proves B1-PACK-v1 and the exact source equivalence. Packing is not asserted to preserve multiplication from the direct-product ring (R')^f.

The source budget is therefore exactly 2f smaller-ring points. This is not statistical amplification of a two-point challenge. One original-ring pair is a public encoding of those 2f points, with their common hidden support. The scalar integer prime q remains unchanged throughout, and the target multiplication occurs in the original R.

## 3. Product-ring defect

Fix K and U. Multiplication by U maps a uniform quotient point uniformly onto UR. The total variation distance between uniform UR and uniform I_K is 1-|UR|/|I_K|. This holds also when U=0. For one selected field coordinate of size Q=q^f, a uniform U coordinate is zero with probability 1/Q. Its contribution to |UR|/|I_K| is 1 when nonzero and 1/Q when zero. Independence across the k selected coordinates therefore gives

E[|UR|/|I_K|]=(1-Q^-1+Q^-2)^k.

The joint retained distance averages the exact conditional distances because both laws have the same (K,U) marginal. It equals 1-(1-Q^-1+Q^-2)^k, at most k(Q^-1-Q^-2)<=k/Q. The probability of at least one zero U coordinate is instead 1-(1-Q^-1)^k; these two quantities remain distinct. Both become negligible in the proposed family.

The product is justified by the original independent field-coordinate law, with no adaptive events or posterior conditioning. The cached-prefix regression therefore forbids no step here: no sequential marginal bound is multiplied after restriction. Exact controls also check the retained law, without inferring an equality after hidden variables are deleted.

## 4. Conditional extraction under the exact decomposition

Fix K. The pairs (S_r,G_r), r<f, are independent, identically distributed length-N coefficient blocks. Let Y_r=S_r+G_r modulo q. Since these observations depend separately on their own independent blocks, the full joint law of ((Y_r,ev_K(S_r)))_(r<f) is the product of f copies of the smaller-ring joint law in the premise. Equivalently, for every positive-mass y=(y_r)_r the posterior factorizes as

Pr[(S_r)_r=(s_r)_r | (Y_r)_r=(y_r)_r]
 =product_r Pr[S_r=s_r | Y_r=y_r].

This identity follows directly from the product numerator and product observation probability. Every posterior replica used within a block must condition on the same Y_r. Independently redrawing observations for two replicas would be a different distribution and is not used.

The comparison distribution is also a product: retain each Y_r marginal and replace its k evaluations by independent uniform F_q^k. A sequence of f ordinary product-measure hybrids bounds the distance by f epsilon_X. In these hybrids the factor being replaced is independent of all other factors in BOTH adjacent laws; this is not a product of success bounds under an adaptive filtration. The coefficient permutation then identifies this comparison with (Y,Z_K) for uniform quotient Z_K. Its output has fk independent F_q coordinates, as required. Averaging over arbitrary K and appending any fixed kernel C conditional K independent of S,G proves B1-X-v1, capped at 1.

This is the necessary new argument connecting X1 to the actual non-split quotient. X1 is applied solely in the fully split dimension N. There is no invocation of an arbitrary-quotient leftover-hash lemma or of scalar marginal character bounds as joint extraction.

## 5. Finite decision inequality and full independence

Write the packed mathematical base source as (U+F_infty,V+H_infty). Truncate F_infty to the full coefficient box, costing delta_F. Add independent coefficient D_rho noise to the second point; by the broadening premise its distance from the auxiliary independent-noise source

(U+F,V+E0), with E0 independent coefficient D_sigma,

is at most delta_F+eta_br. Every uniform comparator is preserved exactly by packing and by adding fixed noise to a uniform second component.

For the independent-noise source, the full observable hybrid is reproduced here to make all source/target variables explicit. The mathematical H_F is drawn by the fixed kernel conditional (K,U,F), independently of independent S,G. The target E is fully independent of S and of source variables; pairwise independence alone is insufficient. Use these public output pairs:

H0: (a,aS+E), with uniform a.

H1: (U+F,US+FS+E).

H2: (U+F,US+F(S+G)+H_F).

H3: (U+F,UZ+FY+H_F).

H3r: (U+F,UZ+F(S0+G0)+H_F), with fresh independent S0,G0.

H4: (U+F,UZ+FS0+E0).

H5: (U+F,V+FS0+E0).

H6: (A,A S0+C) for the independent-noise source challenge (A,C).

H7: uniform R^2.

H0/H1 costs the first source-test advantage. H1/H2 appends independent S to the retained noise comparison and applies (K,U,F,S,N0)->(U+F,US+FS+N0), costing eta_N. H2/H3 applies B1-X with the entire independent source kernel retained, costing min(1,f epsilon_X).

The extracted joint law at H3 is P_(K,U,F,H_F) P_Y Unif_quotient, with the quotient law depending only on K. It is therefore legitimate to redraw a fresh independent S0,G0 with Y0=S0+G0 for H3r. The old S,G are no longer retained. H3r/H4 appends independent S0 and a quotient uniform conditional K to the same retained noise comparison, costing a SECOND eta_N. H4/H5 costs the exact averaged image defect, followed by contraction to the public pair.

For H5/H6, condition on K,U,F,S0,E0. Translation V->V-US0 preserves uniform I_K and leaves its conditional law constant, so V+FS0+E0 has precisely the law of (U+F)S0+(V'+E0) with V' independent uniform I_K. For each fixed S0, (A,C)->(A,A S0+C) is a permutation of R^2; no unit hypothesis is needed. The last edge costs the second source-test advantage.

Compose the two tests with source packing and actual base-source broadening. T1 ignores the second point and only incurs delta_F; T2 incurs delta_F+eta_br. Triangle inequality gives exactly B1-DEC-v1. This derivation retains every target/source independence required by the historical E=-S and E=-F-S counterexamples. It neither implements nor conditions on a completion kernel publicly. Implementation errors follow by ordinary TV contraction; the uniform T2 endpoint is exact for every fixed s,w, so its w sampler is paid only at the planted endpoint.

## 6. Nonempty polynomial-modulus asymptotics and bit costs

Let j=ceil(log2 m), f=2^j, N=n/f, ell=m-j. Thus m<=f<2m, N is a power of two, ell/log2 n tends to 1, and N tends to infinity. For sufficiently large m, s=ell+1>=2 and mh=3m>s. The progression representative A0=n^3+1+2N is odd, lies between n^3 and 2n^3, and is coprime to M0=2n^3. Every positive prime q congruent A0 modulo M0 is at least A0>n^3, since A0 is the least positive residue. Also

q-1=2N+n^3(2t+1)

has exact 2-adic valuation s: after division by 2N the first term is 1 and the second is even. This proves the required factor degree for every member of the progression.

Xylouris's primary Theorem 1.1 gives q<=C(2n^3)^5.18=O(n^15.54). Hence q<=n^16 eventually. Since log N/log n tends to 1, q<=N^17 eventually. This is unconditional nonemptiness; no prime-density heuristic or GRH assumption is used. The paper was checked at [publisher PDF, Theorem 1.1](https://www.impan.pl/shop/publication/transaction/download/product/83078). Its displayed exponent is 5.18, with an effective constant.

Prime generation is polynomial in the growing dimension n, not claimed polynomial in log n alone. Enumerate A0+tM0 until prime, using trial division if desired. The effective polynomial upper bound on the returned prime makes even this elementary deterministic algorithm polynomial in n; a coarse runtime bound is O(q^(3/2) poly(log q))=n^O(1). It need not know the numerical constant C in advance. This is an asymptotic complexity assertion without practical thresholds.

Root setup requires only a primitive 2N-th root in F_q, not an extension-field root of order 2n. For a nonzero g, put w=g^((q-1)/(2N)); check w^N=-1 to certify order 2N. Enumerating g is deterministic polynomial in q and hence n, or uniform g succeeds with probability 1/2 because 2N is a power of two. The N odd powers of w enumerate A. The explicit binomials, ordinary polynomial arithmetic and CRT inverses have polynomial size and construction cost in n,log q. No exhaustive search over q^f field elements is needed. Field elements in each factor are length-f F_q coefficient vectors. Source ideal sampling is polynomial via the smaller-ring CRT; selecting a uniform k-subset is polynomial by standard exact finite sampling.

Set k=floor(sqrt(N)/ell^4). Eventually k>=ceil((ln N)^2), and k<=floor(sqrt(N)/(ln N)^4). Imported X1 thus applies with fixed exponent 17 and tau=ell, giving

epsilon_X<=(1/2)exp(-c_17 N/(k(ln N)^6)).

Because k=Theta(sqrt(N)/(ln N)^4), the exponent is Omega(sqrt(N)/(ln N)^2). Multiplication by f=Theta(log n) leaves a negligible error in n, since N=Theta(n/log n). The finite X1 gates in the imported proof can also be used directly with n replaced by N, d by k, Lambda=k ln q, and kappa_X=(ln N)^-3. In particular its strongest length gate has right side O(N/ln N), eventually below N-1. No old dimension-n X1 theorem is applied to a degree-D quotient here.

The quotient information cost is

D log q=fk log q=O(sqrt(n)/(log n)^(5/2))=o(n).

Meanwhile q^f>=n^(3f), so k/q^f<=n exp(-3f ln n)=exp(-Omega((ln n)^2)), negligible. The rank defect is therefore negligible at an integer prime modulus polynomial in n.

For truncated F, ||M_F||<=n b and sigma=2tau n b, hence B_F>=3sigma^2 I_n/4. The guarded NC1 bound may be instantiated as follows. Put kappa(t)=2 sum_(r>=1) exp(-pi t r^2), delta_N=(1+kappa(3ell^2/4))^n-1, and kappa_H=kappa(3sigma^2/4). Its convolution term is min(1,delta_N/(1-delta_N)) if delta_N<1 and 1 otherwise; its sequential term is min(1,(((1+kappa_H)/(1-kappa_H))^n-1)/2) if kappa_H<1 and 1 otherwise. Their sum capped at 1 bounds eta_N. At ell=Theta(log n), both terms are negligible. This is the n-dimensional coefficient completion, with no splitting premise.

Truncation has delta_F<=n exp(-pi ell^2)/(pi ell), negligible. Broadening has theta_br=ell^2(1-ell^2/sigma^2), delta_br=(1+kappa(theta_br))^n-1 and the same guarded convolution ratio eta_br, negligible. Since q>n^3 and sigma=2n ell^3, q/sigma>=n eventually. All coefficient, root and quotient representations have polynomial bit length. The public tests need only independent one-dimensional Gaussian samplers at polynomial widths, admitting polynomial-time negligible-TV truncation and approximation; no sequential completion sampler is executed by them.

## 7. Source motivation, exposed structure and decoding scope

The independently specified source is the noisy hidden-ideal-point family used in the same-ideal interpretation of HLBDD, with one explicitly stated number of points. The latest repository source comparison identifies Order-LWE Section 7 / Lemma 7.7 as using one common ideal and uniform ideal points, while warning that Definitions 7.3–7.4 are terse about repeated ideal sampling and comparator notation. This proof does not turn that literature assumption into a worst-case theorem, remove those interpretation qualifications, or show its hardness at the present parameters.

The relevant source premise here is the exact split degree-N, support-k, width-ell, **2f-point** family in statement-v1.md. It is stronger than an assumption giving only two points. Original-ring degree-n source syntax hides no free sample expansion: the public coefficient permutation exposes all 2f smaller-ring noisy points. Conversely, a source challenge with exactly that tuple budget packs without statistical loss. An arbitrary polynomial-point same-ideal HLBDD premise would cover the stated logarithmic budget if its other ring, support and width hypotheses match. This literature/interface check remains a coordinator dependency, separate from the algebraic packing theorem.

The source is not claimed hard merely because no binary secret appears. A known structural decoder in the imported ATT v3 family can be applied to one unpacked point in dimension N, taking a subfield dimension r=Theta(k), and under the present large-q/small-noise gates costs exp(O(k)) poly(n,log q). This is superpolynomial here because k=Theta(sqrt(N)/(log N)^4), but supplies an explicit subexponential upper bound on source security. It is an inherited algorithmic statement, not newly implemented or certified. Choosing k=O(log n) would admit polynomial cost for that route and is avoided.

The exact packing exposes 2f=Theta(log n) repeated noisy points sharing K. Nothing here proves that they do not enable a faster source attack. There are fewer than k such points eventually, but that comparison alone proves no hardness or lower bound. The small Gaussian errors, support symmetries, and repeated-sample algebra must remain visible in the source premise. First-mask statistical support is sparse at these parameters; negligible character bias or high representation dimension cannot certify computational pseudorandomness.

For comparison with direct search, revealing pi_K(S) costs at most |R/J_K|=q^D in guessing probability: for each y, sum_z max_(s:pi(s)=z) Pr[S=s|Y=y] <=q^D max_s Pr[S=s|Y=y], then average over y. This is a finite general inequality independent of extraction or units. Since D log q=o(n), an exponentially small noisy-bit guessing bound can survive this cost. Any claimed transcript-to-this-observation reduction and exact wrapped Gaussian guessing probability remain separate obligations assigned to A1.

## 8. Why the new ring LHL is not automatically an extractor here

The allowed 2025/1080 PDF matches the pre-existing /tmp PDF byte-for-byte (SHA256 fdae6acc8113c310d13b3948953d657b0e260608d0c8ae8dea7cdaa5a96d3437); its corresponding text extraction was used. The local pdftotext executable was unavailable, the IACR web PDF fetch was robots-denied, and the HAL document fetch returned a source-access error. No installation or policy interruption occurred.

Boudgoust–Lapiha Theorems 4–5 concern a uniformly random, independent ring matrix A and the joint output (Ax,A), with ideal-sensitive difference probabilities. The conditional version averages the difference ideal over two replicas drawn given the same leakage value; the paper's definition explicitly matches sum_y P_Y(y) sum_x P(x|y)^2. A deterministic selected-quotient evaluation map is not a uniform ring multiplication matrix, so this does not establish pi_K(S)|Y uniform by itself. Treating the projected S as an already uniform/high-entropy input would move the missing extraction statement into a premise.

Corollary 6's low-splitting short-unit sufficient condition uses the number of irreducible factors, denoted f in that paper but N here. For the power-of-two coefficient embedding its displayed gate specializes to 2eta<q^(1/N). At any fixed coefficient bound eta>=1 this fails eventually, since log q=O(log n) and N=Theta(n/log n), so q^(1/N)->1. Thus slowly growing residue degree does not place this construction in that corollary's effective low-splitting regime. Corollary 7 explicitly does not supply a leakage variant; it asks for an additional well-spreadness property. The Gaussian smoothing Theorems 6–7 take Gaussian hash inputs and additional kernel/surjectivity hypotheses, while S is coefficient-binary. None can silently replace those hypotheses.

These observations only reject a direct invocation of those sufficient theorems. They do not refute conditional extraction, which here has the separate explicit block proof in Section 4. The original integer coefficient field and the complete same-observation law are preserved throughout.

## 9. Finite controls and residual review obligations

The exact standard-library experiment [exact-controls-v1.py](exact-controls-v1.py) completed in 0.923 seconds under the coordinator's <=120s slot. [exact-controls-v1.json](exact-controls-v1.json) preserves all outputs. It checks 27 actual prime/order combinations and 2,592 binary coefficient-decomposition instances. Retained product-field TV equals 24/625 and 29424/390625 for F25 with k=1,2, and 8/81 and 1232/6561 for F9 with k=1,2. Both fields occur as factors of X^4+1 over their original integer primes.

A finite S_i,G_i fair-bit example with n=8,q=5,f=4,k=1 confirms the joint conditional map and product inequality, with block distance 11/20 and full distance 153439/160000. Its capped product upper bound is 1, so it supplies no quantitative extractor evidence; it is a structural regression only. The Gaussian asymptotics rely on X1, not this toy. All experiments use locally generated formal ring elements. No source-hardness benchmark was run.

The packet is ready for fresh nonauthor review of factor degrees, ideal conventions, product conditional law, sample budget, finite bridge, parameter effectiveness and imported theorem hypotheses. No claim has been promoted to ACCEPTED. The result remains scoped to one target sample and the explicitly logarithmic source tuple budget.
