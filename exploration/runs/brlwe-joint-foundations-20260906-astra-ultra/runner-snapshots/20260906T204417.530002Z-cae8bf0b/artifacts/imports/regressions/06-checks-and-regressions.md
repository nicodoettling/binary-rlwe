# C02 critic: local checks and adversarial controls

Review scope: C02 as read at 2026-09-06 10:30 UTC. This is a bounded nonauthor review, not a blind review or a full source-proof audit. The coordinator's and author's proposed dispositions were not used as evidence. All probability statements below distinguish the reference product error law from controls that intentionally violate it.

## 1. The source public-tuple hybrid is valid at its stated assumptions

The supplied primary BD2020 text independently confirms the source experiments and sampler: Definition 2.6 at lines 568–577; DSPR Definition 6.1 at lines 1278–1285; sampler and Lemma 6.6 at lines 1335–1381 of `sources/2020-1185.txt`. These are statements at specified source parameters, not guarantees of hardness for every q, Gaussian width, or law chi.

Let H_0 output all A_i=h r_i+r'_i with the shared DSPR challenge h. Replacing h by uniform gives H_1 under DSPR. For j=0,...,m define J_j by a uniform shared h, independent uniform outputs for i<=j, and h r_i+r'_i for i>j. A single HNF challenge (h,b) places b at position j; sample all other outputs as described. The structured challenge gives J_{j-1}; a uniform challenge gives J_j. The secret r_j from this challenge is not reused in another position. Other source samples are generated publicly using the common h and independently chosen r_i,r'_i. Thus the construction does not require m HNF samples sharing r_j, and it does not require knowledge of the hidden f,g. The whole tuple has distinguishing advantage at most one DSPR advantage plus m single-sample HNF advantages. Discarding h is valid postprocessing.

Regression J1: marginal pseudorandomness alone fails. If A_1=A_2 is a uniform element of R_q, each coordinate marginal is exactly uniform, whereas the equality test succeeds with probability 1 compared with q^{-n} on two independent uniform samples. C02 requires the joint tuple and passes this regression. No source hardness for a new Boolean-lossy denominator family is supplied.

## 2. Sampler-coin conditioning passes only with the joint kernel

For a fixed public a and sampler tape t, both the prior P(S=s|a,t)=P(S=s|a) and the likelihood P(Y=y|S=s,a,t)=K_a(y|s) are needed. Under these hypotheses, the Bayes numerator and normalization are both independent of t, so the posterior is unchanged. A tape-only event can select a different law of a, but it cannot change the posterior at a fixed a. No stagewise product or adaptive cached-prefix argument occurs here; the factorization is explicitly part of the reference joint error law.

Regression C1 (the dossier's finite pairwise example): S,T are independent fair bits, E=S xor T, A=0 and Y=E modulo 3. All four (S,T) outcomes have mass 1/4; each pair among S,T,E is independent. Guessing from Y is 1/2 and from (Y,T) is 1. The conditional kernel fails, so this is not a counterexample to C02's repaired claim.

Regression C2 (new, exact Gaussian marginals): take independent fair scalar bits S,T, an independent Z~D_sigma on Z, odd q, and fixed public A_1=A_2=0. Put E_1=Z and E_2=(-1)^{S xor T}Z. For every fixed S,T, each error separately has exactly the symmetric coefficient law D_sigma. The two errors are correlated, so the reference joint product law is deliberately violated. The pair Y=(E_1,E_2) modulo q is independent of S because T randomizes the sign. Therefore p_guess(S|Y)=1/2. Given T, if Z modulo q is nonzero, the observed pair distinguishes its plus and minus signs: q is odd, so r=-r implies r=0. On the zero residue the secret remains fair. Consequently

    p_guess(S|Y,T) = 1-W_{sigma,q}(0)/2 > 1/2.

This is a scalar two-observation diagnostic, not a reference ring instance. It directly tests the tempting repair that checks exact Gaussian marginals but ignores covariance or the complete conditional law across samples. C02's whole-kernel condition excludes it.

The TV approximation bound in the dossier is also valid: optimal guessing is the supremum of success probabilities of deterministic decision rules, each a bounded event functional, so TV epsilon changes guessing by at most epsilon. Apply this to the observation with and without T, and use equality in the ideal law, obtaining an additive 2epsilon gap. Negligible guessing requires a correspondingly negligible additive approximation.

## 3. The real precursor decoder and entropy direction check out

Write u=SH+GF^{-1}-qk and HF=I+qK. Then

    uF=S+G+q(SK-kF).

On ||S+G||_infinity<q/2, centered reduction of uF equals S+G. The computed integer J=(uF-center_q(uF))/q therefore satisfies

    qJ=SHF-S-qkF=-S modulo Z^n F.

Changing the representative u changes J by a vector in Z^n F and leaves the output coset unchanged. The argument neither assumes integral G nor identifies multiplication by F as invertible on the real torus. F invertible over Z_q is not enough for that latter assertion; multiplication by the scalar 2 already has a two-element kernel on a real circle.

The stated continuous tail follows from |S_j|<=1 and the two-sided Gaussian Chernoff bound, followed by a union over n coordinates. It covers S+G, not merely S. With masking width t=sigma_0/L and L>=1, q/sigma_0>=n^c gives q/t>=n^c and negligible failure. If L is the actual norm rather than an enlarged upper bound, the qL/sigma_0 condition must still be checked.

Given sampler coins, Y is obtained from U by the recorded independent residual Gaussian. Its combined error has joint parameter matrix sigma_0^2 I; individual residual coordinates need not be independent. Guessing can only decrease under this postprocessing. Thus precursor recovery is not a public transcript attack. E04 and C02's symbolic F=Z=2I example correctly exhibit a strict gap; their discrete error and fixed A=1 are explicitly different from the continuous source decomposition and uniform public law.

The E04 source code implements K=(q+1)S+E modulo 2q followed by Y=K modulo q, using independent coordinates in its defined diagonal model. The supplied output's zero entropies are floating-point/truncation artifacts, as recorded. Full-support exact wrapped Gaussian likelihoods overlap at every precursor output, so exact recovery probability is strictly less than one at finite widths.

## 4. Occupancy and injection checks

For a fixed integer lattice Lambda and uniform Boolean S, every occupied quotient fiber contributes exactly 2^{-n} to average guessing. Hence p_guess=N_occ/2^n and the retained average min-entropy is n-log2 N_occ, regardless of unequal fiber sizes. This is not Shannon conditional entropy or worst-case conditional min-entropy.

The augmentation inequality in C02 is valid for unwrapped integer V=S+G and C=G mod Lambda: for fixed V=v there are at most N_occ possible C values. It does not transfer by support counting to V modulo q. If F is invertible modulo q, qZ^n+Lambda=Z^n, so full-support integer Gaussian lifts of even a fixed modular V can realize every integer quotient class.

Both deterministic injection certificates are correct. A nonzero ternary difference has norm at most sqrt(n), whereas sigma_min(F)>sqrt(n) excludes it from Lambda. Alternatively, a nonzero divisibility relation d=fz implies the nonzero integer Norm(f) divides Norm(d); irreducibility of X^n+1 for power-of-two n and Hadamard bound |Norm(d)|<=||d||_2^n give the contradiction when |Norm(f)|>n^{n/2}.

Regression I1: strict thresholds matter. For n=2, f=1+X, q=3, the matrix has sigma_min=sqrt(2)=sqrt(n) and norm 2=n^{n/2}. The distinct Boolean secrets 0 and 1+X lie in the same ideal coset. Neither strict certificate applies, exactly as required.

The deterministic BD-event implication is valid as written: ||sigma(f^{-1})||_2<=24sqrt(n)/gamma implies sigma_min(M_f)>=gamma/(24sqrt(n)), giving injection at gamma>24n. No probability transfer follows from that algebra. The separate SS projection estimate was checked in [the primary PDF, Lemma 2.7](https://eprint.iacr.org/2013/004.pdf), printed p.7. With coefficient width kappa, real evaluation vector norm sqrt(n/2), v=16n and delta=1/4, the dossier's union bound and constants follow. The resulting probability is unconditioned; modular-unit conditioning still needs its own failure probability. The BD/SS normalization issue remains unresolved and was not audited further.

## 5. Denominator tests and Lucas control

For a known positive kappa in (f), kappa z/f is integral. Its coefficient norm is at most kappa times the rational multiplication operator norm. At kappa L<q/2, the centered modular test accepts every sample satisfying that bound. If gcd(kappa,q)=1, scalar multiplication preserves uniformity, so the exact uniform acceptance probability is ((2 floor(kappa L)+1)/q)^n. Enumerating polynomially many possible exponents is a valid union-bound test under the stated common K L<q/2 restriction. This does not say that every denominator with entropy has polynomial exponent.

Regression D1 (advantage boundary): no-wrap alone does not give a useful distinguisher. If (q-1)/2<=kappa L<q/2, every centered residue passes, and the exact uniform acceptance is one. Therefore a statement that the test "distinguishes" still requires its displayed false-positive bound to be meaningfully below the structured acceptance probability p. C02 gives the correct quantitative expression; its intended polynomial q/L gap for the fixed constant-exponent example satisfies this additional requirement. The same qualification applies to the fixed-f short-numerator test and any enumeration union bound.

For f=1-X-X^2, the exact matrix relation X^2=1-X gives T=[[0,1],[1,-1]]. For n=2^r>=4 and k=n/2, k is even, det(T^k)=1 and trace(T^k)=L_k. Cayley–Hamilton gives T^n+I=L_k T^k. Thus the quotient is (Z/L_k Z)^2, and both its index L_k^2 and exponent L_k are correct. The lower entropy bound based on N_occ<=L_k^2 is correct even when some classes are absent. The identity |1-z-z^2|^2=1+4sin^2(theta) on |z|=1 verifies the operator bound sqrt(5) and the asymptotic failure of the larger singular-value charge.

The fixed public denominator still permits multiplication by f followed by a short-numerator test. Its rotations and automorphisms form only a polynomial-size enumerable family. The exponential quotient exponent therefore evades one scalar test but does not establish public pseudorandomness.

E05, authorized by the coordinator, is the only new computational experiment in this criticism. `boolean_fibers.py` checks T^n+I=L T^{n/2}, computes a dynamic quotient count, and exhaustively reduces every Boolean polynomial directly by X^2+X-1. The two methods agree, including every residue and total mass. At n=4,8,16 the counts are respectively 8,48,2208; the sole absent residue in basis (1,X) is (2,1). Full occupancy is already false at n=4 and also at both proposed next-test degrees. An all-degree formula N_occ=L_{n/2}^2-1 with this sole omission is only a future conjecture supported by these three cases, not a theorem proved here.

## 6. Sometimes lossiness cannot be silently upgraded

BD2020 Definition 3.3, Definition 4.1 and Theorem 4.2 in the supplied primary text confirm the mild-hardness quantifiers used by C02. A fixed m is retained throughout the proposed public-tuple test. The paper's unbounded-sample amplification and subset-sum rerandomization are different interfaces; the latter changes the error law. No automatic finite-m unchanged-discrete-Gaussian conclusion follows.

Regression H1 (new, abstract noiseless family): let S be uniform Boolean of length n, let the public matrix A be uniformly either 0 or I, and set Y=AS with E=0. This departs from the reference in the public law and error law. Take X equal to that same public law, so public pseudorandomness relative to it is exact. Half the matrices are lossy with guessing 2^{-n}. Nevertheless a solver recovers perfectly on A=I and guesses 0 on A=0, for average success 1/2+2^{-n-1}. Mild hardness can still hold information-theoretically: near-perfect success over A for a fixed S requires guessing S with probability >1-2nu on the zero branch. For negligible nu this can hold for at most one S, whose prior mass is 2^{-n}. Thus the sometimes-lossy-to-negligible-average implication is false even in this elementary family.

By contrast, C02's stronger sufficient condition E_X g<=negl is valid: a public distinguisher samples its own S and exact target E, invokes the proposed solver, and compares its output with S. Its success under X is bounded by E_X g, and under uniform public tuples is the target solver's ordinary average success. Sampling errors and Gaussian-approximation losses must be explicitly negligible if an implemented sampler approximates the ideal law.

The unresolved step is consequently concrete: at supported source parameters, prove Pr_{a~X}[g_{sigma,q}(a)<=2^{-h}]>=delta under the exact target joint error law, with h=omega(log n), delta>=1/poly(n), and negligible smoothing if used. The exact coset calculation, informative precursor, marginal Gaussian checks, source public-tuple hybrid, and finite Lucas controls do not supply this statement.
