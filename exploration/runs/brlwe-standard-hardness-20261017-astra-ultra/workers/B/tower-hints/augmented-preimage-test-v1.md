# B-TOWER-HINT v1: exact missing rows and augmented-preimage washout

Status: PROVISIONAL new endpoint calculation. This is a scoped failure of the fresh canonical augmented-preimage mechanism, not an impossibility theorem for module-to-ring reduction. No source hardness or binary-oracle query is silently assumed. The prior A-tower algebraic and affine-law obstructions remain in force.

## 1. Actual tower, row convention and source law

Let R=Z[X]/(X^n+1), S=Z[Y]/(Y^(nr)+1), n,r powers of two, n>=2,r>=2, N=nr, with X=Y^r. Let q be a prime splitting S, hence R. Write A=sum_(j=0)^(r-1)Y^j A_j and the uniform binary secret Z=sum_jY^j Z_j. Each Z_j has n independent coefficient bits, jointly independent of all public source data.

Define the r-by-r R-matrix C(A), with SECRET block index j on rows and OUTPUT block index k on columns, by

  C(A)_(j,k)=A_(k-j) if k>=j,
             X A_(r+k-j) if k<j.

Then the block row of AZ equals (Z_0,...,Z_(r-1)) C(A). For r2,

  C(A)=[[A0,A1],[X A1,A0]].

This is the transpose of the convention with equations indexed by rows. Multiplication by X in the wrapped entries is essential. The set C(Sq) is an Rq-linear subspace of r-by-r matrices of Fq dimension nr, inside ambient dimension nr².

Grant an ordinary binary MODULE input with h samples: M uniform Rq^(r by h), b=zM+e, z=(Z_0,...,Z_(r-1)), e with independent coefficient D_tau. The comparator has b independently uniform Rq^h. This is a temporary exact source contract; any published module hardness theorem must separately be matched to its rank, secret/error law and parameters. A standard ring secret being a hash of these bits does not itself provide these module samples.

The desired extension target is A uniform Sq, B=AZ+G with all N error coefficients independently D_chi, versus the same A and independent uniform B. The target recovery oracle receives only valid samples of this exact full-ring law. All r correlated block responses are required.

## 2. What a direct successful short-preimage map would supply

Sample A uniformly independently of M,z. If a public response-independent algorithm returned a short V in R^(h by r) satisfying

  M V=C(A),                                                   (T-H1)

then bV=zC(A)+eV. Rectangular Gaussian completion from the frozen preimage-transport proof, at chi>=2tau max(1,||V_c||) and tau above the coefficient smoothing threshold, yields the required independent D_chi output errors, retaining the actual binary witness z and A. This is a genuine sufficient algorithmic interface.

If A is a unit in Sq, C(A) is invertible over Rq; consequently V has full column rank at every base CRT root. The comparator bV is then EXACT uniform Rq^r conditional on M,V,A and completion coins. A nonunit abort costs at most N/q for uniform A. A non-surjective input M has its separate public rank failure. Thus the obstruction is not an inability to state both endpoints: it is computing suitably short V with (T-H1), full law, and polynomial runtime without unavailable advice.

An unrestricted short-preimage sampler for M alone would be much stronger than the supplied canonical augmented hint. It must not be inserted as an assumed primitive. The sufficient interface only needs uniform structured targets C(A), but no efficient implementation from the available hint is established here.

## 3. Actual augmented canonical-hint map

Give the proposed mechanism its favorable public setup: independent uniform W in Rq^(r by k) and a valid canonical gadget hint for [M|W], with the exact same public law in both source worlds. The source provides responses b for M ONLY. It provides no responses zW. Such hints can be discussed only with their full standard-input simulator and width losses; their presence is granted here to test whether even the ideal sampling endpoint fixes the tower rows.

Using that hint, sample short canonical preimages of the r columns of C(A):

  T'=(V;U), M V+W U=C(A), V in R^(h by r), U in R^(k by r).

The executable response formed from available data is bV+f. Its exact planted identity is

  bV+f=zC(A)-zWU+(eV+f).                                  (T-H2)

The term -zWU is secret-dependent. A covariance calculation about eV+f cannot remove it. Adding the missing zWU would require the unknown z or appropriate extra secret-dependent responses.

At the smoothed canonical endpoint, U is iid coefficient D_sigma, independent of M,W,A,z. Conditional on U, V has its actual M-coset Gaussian law. The proof is the same exact normalizer calculation as B-SUP-PT, now with r module equations: the U marginal is its Gaussian prior reweighted by product_j Pr_M[Mv_j=C(A)_j-WU_j], divided by the ACTUAL expectation. One needs pointwise flatness for the r-ring-row M and the augmented(r+1)-row matrix[M;b-e0]. The ring character identity extends with coefficient(q^d-1)^|T| for d retained rows; the q^(nd) Markov amplification must be paid. This packet does not assert that merely calling the rank-one theorem supplies those extra dimensions for free.

To isolate the response problem, GRANT exact independent-U law and exact Gaussian completion Eout=eV+f independent of M,W,U,A,z. Any finite/smoothing errors in a real implementation add their full joint distance Delta. Even this favorable endpoint has

  (A,z,Bblocks)=(A,z,zC(A)-zWU+Eout),                       (T-H3)

after M,W,U,V and all hints are discarded to form an ordinary extension-ring query.

## 4. Full planted washout

Let GoodZ mean that at every base CRT root omega, the module row z(omega) is nonzero. Since the constant coefficient of each independent binary Z_j has maximum atom1/2,

  Pr[not GoodZ]<=n 2^-r.

This is a union bound; no independent CRT evaluations are assumed. Let GoodU mean U(omega) has full column rank r at every base root. If coefficient D_sigma moduloq has maximum atom mu<=min(1,1/sigma+1/q), independent rows and a union over nonzero kernel vectors give

  Pr[not GoodU]<=n(q^r-1)mu^k.

Conditional on any fixed good z and good U, W is still uniform independent of A,z,U and the completed error. At each root, z(omega)W(omega) is uniform Fq^k. Multiplication by full-column-rank U(omega) makes z(omega)W(omega)U(omega) uniform Fq^r. All roots and all output coordinates are jointly uniform because W has the full independent uniform ring-matrix law. Therefore zWU is EXACT uniform Rq^r conditional on A,z,U,Eout. Translating by zC(A)+Eout preserves uniformity.

Consequently the full joint planted endpoint (A,z,B) in(T-H3) satisfies

  TV((A,z,B),(A,z,U_Sq))
    <=n2^-r+n(q^r-1)mu^k+Delta.                           (T-H4)

This is a washout result, not merely a loose norm estimate. In a parameter family where r has logarithmic surplus and k supplies negligible rank failure, the proposed planted target becomes nearly uniform even while retaining the latent binary witness. Its probability of an error coefficient K-box is at most ((2K+1)/q)^N plus the displayed loss; a true small-noise binary-ring sample lies in that box with high probability. Hence it cannot be the promised recovery-oracle input.

The comparator endpoint of the legitimate canonical preimage transport is independent uniform after its augmented coset-flatness/completion charges, retaining W,U. Alternatively one may test V's actual full column rank and preserve exact uniformity conditional on that event, paying and proving its changed joint law. One must not infer comparator surjectivity solely from M V+WU=C(A), because V itself may be rank deficient. This issue does not save the planted washout in the favorable full-joint endpoint above.

Keeping W in an oracle query does not fix(T-H2): the requested ordinary ring oracle has no guarantee on this extra-metadata, wrong-error experiment. We do not query it there or assume it behaves like a decoder.

## 5. Concrete attempted repairs and their exact missing obligation

1. Force WU=0. Then(T-H1) holds, but fresh canonical U does not provide that constraint. Conditional on good U and uniform W, WU is uniform in Rq^(r by r); acceptance probability is q^(-nr²). This is a conditioned joint-preimage task, not an event to omit.

2. Allow WU itself to be C(D) and replace A by A-D. This at least keeps the multiplication structure. Conditional on good U, its exact acceptance probability is q^(-nr(r-1)), because C(Sq) has dimension nr. A uniform A independent of W,U makes A-D uniform conditional on accepted D, so the algebraic and multiplier endpoints can be repaired, but polynomial rejection does not sample the required rare event. Error/comparator law and all selected metadata would still need their own charges.

3. Set the target F=C(A)+WU in advance. Canonical sampling's target may depend on W and chosen public data, but not on the very U coordinate whose fresh independent Gaussian marginal is being asserted. If U is first sampled and then a new preimage(V,U') of F is drawn, the residual becomes W(U-U'), not zero. If one instead insists on the prescribed U, the remaining conditional task is exactly MV=C(A), so the missing short-preimage computation has simply returned.

4. Correct zWU using a recovered or guessed secret. Recovery on these off-promise samples is unavailable; guessing the binary witness is exponential and is not a reduction. Source-dependent public metadata must remain independent of the fresh target binary secret under the actual endpoint law.

The precise surviving algorithmic obligation is therefore a polynomial-time, small-norm joint-preimage sampler that imposes MV in C(Sq), yields a uniform extension multiplier independent of the binary witness, preserves a full-rank comparator response map, and keeps completion noise below the desired q/chi. It may use the actual augmented hint, but must prove its conditional sampler law rather than replace it by fresh independent U. The new canonical machinery by itself supplies a different law, and(T-H4) shows that law fails the target.

## 6. Relation to the preserved radix obstruction

This test starts from a granted binary MODULE source, so it does not evade A's earlier radix obstruction. Starting directly from scalar base-secret responses still yields affine secret dependence C s; matching a tower digit vector forces A(Y-2)=0, or a secret-dependent carry correction. Those immutable equations and their exact comparator bookkeeping remain in A/tower-binary/tower-first-partial-v1.md and correlated-row-repair-v1.md. The successful ingredient required here is all r correlated module rows, not a single trace or algebra homomorphism projection. No standard foundation follows from merely renaming the source.
