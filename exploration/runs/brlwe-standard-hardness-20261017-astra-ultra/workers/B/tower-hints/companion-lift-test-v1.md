# Companion-action lift: a different correlated-row mechanism

Status: PROVISIONAL interface and explicit gap. This goes beyond rejecting fresh augmented preimages, but does not claim a useful short-lift sampler. Ring/secret conventions are exactly augmented-preimage-test-v1.md.

Let M be the r-by-h public binary-module multiplier matrix. Let J=C(Y)^-1, an r-by-r ring matrix whose coefficient action is a signed permutation. Thus J^r=X^-1 I. If c=C(A)e0 is the first column of C(A), its other columns are J^j c for j=1,...,r-1. The map c->A is a bijection of Rq^r and Sq.

## 1. A sufficient public lift, with both endpoints

Suppose an efficient public algorithm, depending on M and independent local coins only, produces integer ring matrices K_0,...,K_(r-1) of size h-by-h satisfying

  K_0=I, M K_j=J^j M modq, and
  C_K²=sum_(j=0)^(r-1)||K_(j,c)||op² <= a specified useful bound.

The matrices may be separately chosen lifts; if they are powers of one K, their ACTUAL integer powers must satisfy this bound. Reducing powers moduloq changes their noise action and must use the resulting actual integer lifts instead. A generic polynomial norm for K alone does not give a polynomial bound for K^r when r grows.

Draw v in R^h with iid coefficient D_s, independently AFTER choosing the K_j. Set c=Mv, recover A from c, and form

  V=[K_0 v | K_1 v | ... | K_(r-1)v].

Then M V=C(A) exactly moduloq, and the response bV has secret term zC(A)=AZ with the original uniform binary witness. On ||v||coef<=s sqrt(nh)a,

  ||V_c||op<=||V_c||F<=n s sqrt(h)a C_K.

This tail fails with probability at most2nh exp(-pi a²). Rectangular Gaussian completion at chi>=2tau max(1,n s sqrt(h)a C_K), with the original tau above its coefficient smoothing threshold, yields independent target coefficient D_chi errors. It preserves the full joint binary witness, rather than merely the error covariance.

For uniform M, the r-row ring hash bound gives

  TV((M,Mv),(M,U_(Rq^r)))
    <=eta=.5 sqrt((1+(q^r-1)mu_s^h)^n-1),
  mu_s<=min(1,1/s+1/q).

Because each K_j was chosen from M independently of v, this same bound retains the complete K tuple by a common conditional kernel. It does NOT apply if K or its selection event depends on Mv without further proof. Consequently A is eta-close to uniform, jointly with the public variables used in the noise completion. The target binary witness remains independent of A.

On A being a unit, C(A) and therefore the response map V have full column rank at every base CRT root. An independent-uniform source b then gives an EXACT uniform B=bV+f conditional on every public variable, including V and independent completion noise. A common nonunit abort costs at most N/q+eta for uniform-target comparison. Any lift-algorithm failure has its own declared charge. Thus a valid useful short-lift algorithm would supply both endpoints and a direction-correct binary-module-to-binary-ring reduction.

For several target samples, partition the input module samples into independent size-h blocks and apply this construction independently to each block. The module secret stays common, while all public variables and source errors are independent conditional on it. This avoids falsely inferring independence from multiple transformations of one error vector. Source cost is h module samples per extension sample, and the full target distance is bounded by the sum of the per-block losses.

## 2. What the canonical augmented hint really computes

Let D=[M|W] and let T be an actual supplied integer gadget trapdoor satisfying D T=I_r tensor G. For each j, compute the public binary gadget decomposition B_j of J^j D, so

  (I_r tensor G)B_j=J^j D.

Then the integer matrix Ktilde_j=T B_j satisfies

  D Ktilde_j=J^j D.

This is an EXECUTABLE short companion-action lift on the AUGMENTED sample space. Using separate gadget decompositions for each j avoids exponential norm growth through powers. A coefficient bound B_T on T gives, for example, a polynomial Frobenius product estimate ||Ktilde_(j,c)||<=n² B_T r g(h+k), where k is the number of W columns. This construction uses only the legitimate supplied trapdoor and public matrices; it does not assume a trapdoor for M.

However, the input responses cover the M coordinates only. Let E embed R^h into the first h augmented coordinates, and P_M,P_W be the two projections. For a seed v, define

  V_j=P_M Ktilde_j E v, H_j=P_W Ktilde_j E.

The actual equation is

  M V_j=J^j Mv-W H_j v.

Thus the desired lift on known-response coordinates is obtained only if

  H_j v=0 modq for EVERY j=1,...,r-1.                   (KRYLOV)

The j0 lift can be the identity, so H_0=0. This identifies a simultaneous short-kernel problem for an explicitly computable public stack H. The existing hint samples preimages under D, not under H. It supplies neither a short-kernel sampler for(KRYLOV) nor the needed extraction guarantee that Mv stays uniform AFTER sampling v in that M-dependent kernel.

Sampling v independently and ignoring the H_j terms gives precisely secret-dependent missing response corrections, the same type of endpoint defect exposed by the fresh-U washout. Imposing integer rather than modq zero constraints would suffice, but a generic exact integer nullspace basis can have large coefficients. A determinant/existence bound or generic lattice reduction is not a polynomial-size usable-norm guarantee. Even if h exceeds the number of constraints and the finite-field kernel is large, the obvious lifted basis has coefficient scaleq and does not meet the required completion-noise window.

## 3. Dense lifts and actual parameter cost

For a full-row-rank M, finite-field linear algebra can compute a right inverse P and separately set K_j=P J^j M for j>=1, with K_0=I. These satisfy the modular lifting equations. Centered coefficient representatives, however, have scaleq; the elementary operator certificate is O(n h q) for each K_j. Feeding that bound into the displayed chi requirement gives chi at leastq times polynomial factors. This is a failure of the available certified construction, not a lower bound on every possible short lift.

Using augmented Ktilde_j makes the raw norms polynomial in the hint width rather thanq, but transfers the unsolved task to(KRYLOV) and to conditional extraction. A successful next algorithm must solve BOTH tasks, retain full public metadata law, and preserve independent binary secrets and the comparator. No off-promise call to the ring recovery oracle is justified by the algebra alone.

This mechanism is distinct from simply conditioning independent module rows to be circulant: it would generate the whole multiplication block through a lifted ring action. The current canonical machinery supplies that action only in a space containing unavailable secret-dependent responses. The exact remaining computational obligation is therefore preserved, without adding it as a hardness premise or claiming a foundation.
