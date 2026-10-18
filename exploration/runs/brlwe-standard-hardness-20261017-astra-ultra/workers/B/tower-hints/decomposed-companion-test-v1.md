# Structured decomposed key: short conjugation and the missing inverse

Status: PROVISIONAL exact construction test. Parent asked whether M=aR+G already supplies an invariant known-response space, rather than an arbitrary-M trapdoor. This packet keeps both endpoints and the actual full-column-rank source simulation. It does not claim a useful short inverse exists.

Use the tower and row conventions of augmented-preimage-test-v1.md. Let the binary module secret have rank r. Choose h=r g, padded gadget G=I_r tensor(1,2,...,2^(g0-1),0,...,0), g0=ceil(log2q). Let a uniform Rq^(r by k), R in R^(k by h) with prescribed independent coefficient Gaussian entries, and

  M=aR+G, b=zM+e.

The comparator has b uniform Rq^h independent of a,R. The complete public source includes a,R, hence M. This module version of the full-fiber standard simulator samples R with FULL COLUMN RANK at every base root and, for ordinary uniform M, samples each row of a uniformly from aR=M-G. Conditional on that rank event it has exactly the displayed decomposed joint law; rank failure must be charged. It leaves the binary law and source noise unchanged but does not establish that binary source hardness from uniform-secret RLWE by itself.

## 1. Exact gadget conjugation

Compute the ordinary coefficientwise binary gadget decomposition D=D(a) in R^(h by k), with coefficients0 or1, satisfying G D=a modq. Then

  S=I_h+D R,   M=G S modq.                               (DC1)

Let J=C(Y)^-1 and P_j=J^j tensor I_g. These have signed-permutation coefficient actions, ||P_(j,c)||=1, and G P_j=J^j G. If a short integer lift U of S^-1 moduloq is available, set

  K_j=U P_j S for j>=1, K_0=I.

Then M K_j=J^j M modq and

  ||K_(j,c)||<=||U_c|| ||S_c||.

Separate P_j matrices avoid taking potentially large integer powers of one approximate lift. Thus a useful short U would supply the sufficient companion interface in companion-lift-test-v1.md. Its complete planted and comparator target laws would follow there, including fresh source blocks for independent extension outputs, hash extraction retaining all chosen public metadata, and actual operator-noise loss.

The literal decomposition gives S, not a short inverse U. S may even be singular moduloq; an executable scheme must test and pay that event before inversion. Finite-field Gaussian elimination only produces dense representatives of an inverse, with available coefficient bound(q-1)/2 and operator certificate O(nh q), which is too large for the desired noise window. Invertibility or small entries of S alone imply no usable small inverse.

## 2. The tempting nilpotent/triangular repair changes the source

If R D=0 as an integer matrix, then(DR)²=0 and S^-1=I-D R is explicitly short whenever D,R are short. However, in the standard-input simulation R has full column rank over Rq. Therefore RD=0 moduloq implies D=0 moduloq and hence a=G D=0. It cannot hold for the prescribed independent uniform a except on its negligible zero event. This failure uses the actual wide-R regime, not a generic heuristic.

One can force an apparent triangular example by reserving gadget-prefix columns: take G=[G0|0], choose D supported in that prefix and R zero on the prefix. Then RD=0 and M=[G0|aRrest]. But R is now column-rank deficient and the first multiplier block is the FIXED gadget G0. The source requires the associated secret-dependent responses zG0+e. They cannot be created from ordinary input multipliers/response samples by merely appending public gadget columns. Treating those responses as known or independent would change the planted endpoint. If they are actually supplied at low noise, they directly reveal the binary secret as in Section4.

A more general square-zero factorization would take N=H(M-G), with a short H satisfying

  G H=I_r,   (M-G)H=0 modq.                              (DC2)

Then M=G(I+N), N²=0 moduloq, and I-N is an inverse moduloq. But(DC2) is a simultaneous gadget preimage and random-syndrome kernel problem. Ordinary digit decomposition satisfies only the first equation. The canonical augmented hint does not by itself provide a short H satisfying the second. All conditions are public; their mere finite-field solvability does not supply the useful small integer norm.

## 3. Both response endpoints of the putative short inverse

If S is invertible moduloq and U is an actual integer inverse lift, the public map b->bU satisfies

  planted: bU=zG+eU;
  comparator: bU exactly uniform Rq^h conditional on a,R,U.

The uniform law follows from bijectivity moduloq; the planted error is the FULL correlated eU law. Independent Gaussian completion can be added with its stated operator cost, but cannot make a large inverse cheap. The above identities retain the entire public source, so there is no hidden conditioning or absent response block.

For the standard source simulated from uniform M, choosing D,U from the complete public decomposition before fresh hashing seeds is compatible with conditional-kernel extraction. It is the short-inverse algorithm and its success/norm law that are missing, not a license to replace M with a syntactically structured distribution.

## 4. Useful inverse already decodes the binary module source

This route has a stronger consequence than extension packing. Choose a gadget weight w=2^j with q/4<=w<=q/2. Such a weight occurs among the powers through2^(g0-1). In each module block, the corresponding response polynomial in bU is

  w Z_i+(eU)_(i,j).

If every centered coefficient error has magnitude belowq/8, nearest-center decoding between0 andw recovers every coefficient bit of every Z_i. The two centers are circularly separated by at leastq/4. No ring-recovery oracle is needed.

The source Gaussian tail gives ||e||2<=tau sqrt(nh)a except probability2nh exp(-pi a²). Hence the explicit sufficient condition

  tau sqrt(nh)a ||U_c||op < q/8

already yields direct high-probability binary-module recovery from the supplied decomposition. A short inverse suitable for the earlier companion completion certificate normally satisfies an even stronger bound after its additional S/hash factors. Thus importing such an inverse as an unexplained public primitive would insert essentially the computational work being sought. This is a conditional reduction consequence, not an unconditional impossibility claim about finding U.

The structured decomp key therefore does give a concrete algebraic conjugation, but its standard full-rank joint law does not supply the required short inverse or invariant known-response subspace. The remaining task is explicit(DC2), a useful inverse of(DC1), or another mechanism with a genuinely proved input simulation. Signed rotations of secret coordinates alone do not generate missing responses under the same binary witness and are not substituted here.
