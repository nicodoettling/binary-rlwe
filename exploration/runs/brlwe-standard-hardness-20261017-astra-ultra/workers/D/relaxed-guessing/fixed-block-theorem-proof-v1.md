# A concrete high-index actual-secret guessing family

D; after tool clock2026-10-17T21:48:15Z. PROVISIONAL new theorem/proof, pending independent review. This shows that the D p_t^n upper bound can be vacuous while actual guessing is exponentially small. The same family has an easy public source, so it does NOT widen the verified standard-hardness intersection.

## Exact family and index

Let n>=8 be a power of two, m=n/8, R=Z[X]/(X^n+1), and

    f(Y)=1+Y+Y²-Y³+Y⁴+Y⁵-Y⁶+Y⁷,
    F(X)=f(X^m), J=F R.

Permute coefficient coordinates into the m blocks (X^j,X^(j+m),...,X^(j+7m)), j=0,...,m-1. Multiplication by F is a direct sum of m copies of multiplication by f in R8=Z[Y]/(Y^8+1). Consequently J is the orthogonal direct sum of m coefficient lattices J0=fR8, and

    [R:J]=2176^m > 256^m=2^n.

Here is an exact hand determinant calculation. Write f(Y)=a(Y²)+Y b(Y²), where a(Z)=1+Z+Z²-Z³ and b(Z)=1-Z+Z²+Z³. Modulo Z⁴+1,

    a²-Zb²=2(1+Z+3Z²-Z³)=2c(Z).

Write c(Z)=(1+3W)+Z(1-W), W=Z², W²=-1. Its relative norm is -10+6W, of absolute norm136. Thus N_R8(f)=2⁴*136=2176=128*17. All factors are nonzero. The multiplication columns form a public basis of J with operator norm at most||f||_1=8; no shortest-vector algorithm is needed.

## Actual joint guessing law

Let S be uniformly coefficient-binary and let G~D_(J,t), independent, t>0. Observe the FULL unwrapped Y=S+G. Under the above coordinate permutation, the pairs (S_block,G_block) are independent across all m blocks, and G_block~D_(J0,t). This follows from the exact Cartesian lattice decomposition and the factorization of the squared coefficient norm, not an assumption about marginal covariances. Therefore the optimal actual-secret guessing probability factors EXACTLY:

    p_guess(S|Y)=p0(t)^m.

For j=0,...,7 let v_j=Y^j f in R8. Each has eight coefficients in{+1,-1}, lies in J0 and has squared coefficient norm8. Its positive and negative indicator vectors b_j^+,b_j^- are two binary vertices whose difference is v_j. These eight antipodal pairs are disjoint. Indeed equality up to sign between two rotations of f would imply Y^(i-j)=+1 or -1 in the characteristic-zero field, impossible for0<|i-j|<8.

For any probability mass P and eight disjoint label pairs, pointwise maximum over all labels is at most the sum over all labels minus the sum of the paired minima. Applying this to P(y-b), then summing y, gives

    p0(t) <= 1-(8/256)(1-TV(D_(J0,t),D_(J0,t)+v_0)).

All eight TV terms agree by the signed-rotation isometry of J0; agreement is not needed for the common upper bound below. Since v belongs to J0, translation preserves the support and normalization. The centered Gaussian mean is zero, and the KL divergence to its translate is EXACTLY

    KL(D_(J0,t) || D_(J0,t)+v)=pi||v||²/t²=8pi/t².

Pinsker thus gives TV<=min(1,2sqrt(pi)/t), and hence

    p_guess(S|S+G)
      <= [1-(1/32)(1-min(1,2sqrt(pi)/t))]^(n/8).       (B1)

In particular t>=4sqrt(pi) gives (63/64)^(n/8). This is an actual-secret guessing bound after revealing all Y, not merely a quotient image entropy statement. It can replace beta in the proof of A-FRAC for this fixed family, with all its independent completion/tail errors still charged. The proof-only G and H remain independent of fresh S conditional on the source state exactly as in A-FRAC; no auxiliary tape is made public in the original experiment.

By contrast, D p_t^n is at least D/2^n=(2176/256)^(n/8)>1 for every t, so the original bound is identically vacuous. One full-support relation in n coordinates would affect only two binary vertices; here the independent repeated8-coordinate blocks supply linearly many bounded-support ambiguities. This distinction is essential.

## Exact finite control

Reserved D-ENTROPY-1 completed with one fixed r8 candidate,256 binary vectors,17,548 counted arithmetic cells,0.0267s and13MiB, exit0. Hard limits20s wall/256MiB/18s CPU, one process. Bareiss integer determinant and exact Fraction inverse/coset arithmetic give determinant2176 and EXACTLY248 binary quotient classes:240 singleton fibers and8 double fibers. The double fibers are exactly the eight rotation pairs used above. No Gaussian mass or asymptotic conclusion is inferred from the finite test.

All code/input/estimate/command/full output/stdout/stderr/resources/exit records are in entropy-control-v1-manifest.json. Code SHA dfcba5323b73db8ba68f95272cfe8e6180d05aa58b4f0cbaa07cee6d4f4af720; full exact output SHA3d75e5f9beb2a45058aaaa6c5363c869ba80b9b0097fd121b02ce4f6cc015a16. There is no numerical Gaussian truncation or omitted tail in this experiment. The infinite Gaussian comparison is the analytic KL argument above.

## Why this does not give a harder source

Take an odd split prime q coprime to2176 (q!=17). The A-FRAC source is a~D_(J^-1,s), A=a mod qJ^-1 identified with Rq, versus uniform A. Since F belongs to J, Fa belongs to R and

    F A modq = F a modq.

The public F is a unit moduloq because its norm is coprime toq. Therefore F A is exactly uniform in Rq at the comparator. At the planted source, each coefficient of Fa is an inner product of a with a vector of norm sqrt(8). The actual lattice-Gaussian MGF bound, which needs no smoothing, gives

    Pr[||Fa||_infinity > s sqrt(8) U] <= 2n exp(-pi U²).

Thus test whether every centered coefficient of F A lies in[-K,K], K=s sqrt(8) U. Its planted acceptance is at least1-2n exp(-pi U²), whereas its comparator acceptance is at most

    min(1,(2floor(K)+1)/q)^n.

For U=Theta(sqrt(log n)) and s sqrt(log n)<<q this is an efficient high-advantage distinguisher using one source sample. The original useful target-noise constraint sigma>=2ts sqrt(kn)L together with sigma<<q lies inside this easy regime for normal polynomial parameters. The known basis also allows direct efficient Gaussian sampling above its ordinary smoothing scale. The family is principal and publicly generated; it does not represent arbitrary ideal classes.

The result is therefore a genuine counterexample to necessity of the coarse index cutoff for LOSSINESS, while failing the separate source-hardness gate. It supplies no standard foundation and no security inference from a failed attack.
