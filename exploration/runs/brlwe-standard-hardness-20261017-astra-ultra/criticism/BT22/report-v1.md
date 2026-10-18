# BT22 complete blind referee report, v1

Review date: 2026-10-18 UTC.
Packet: "Normalized trace and complementary multipliers: specification v2."
Reviewer scope: independent reconstruction of the claims in the supplied theorem-only packet. The only substantive input was that packet. No proof, earlier referee report, ledger, project status, external source, experiment, or other agent's scientific finding was inspected.

This is a mathematical referee report within the assigned frozen scope. It does not change an acceptance record, promote a computational result, or complete a parent goal. This is correlated same-model scrutiny, not independent-model confirmation.

## Result and limits

I independently reconstructed Claims 1–4. I found no false algebraic or probabilistic assertion under their stated hypotheses. The moment estimate, the zero-probability bound, the complete-law total-variation transfer, and the conditional formulation for a random multiplier all have direct proofs with the stated constants.

The conclusion remains conditional on the supplied multiplier and sample-law premises. The packet does not establish an efficient way to obtain a short multiplier, an exact or sufficiently accurate sampler, an inverse-polynomial success margin, an amplified solver, or a standard hardness reduction. I did not infer any of those conclusions.

The final arithmetic sentence is justified for the ordinary explicit coefficient and rational ideal-basis encodings stipulated in the packet, with all represented inputs included in the size measure. It is not an algorithm for exact operations on unspecified real-number encodings. Neither computing an exact value involving pi nor testing an exact comparison with such a real threshold is necessary for the stated event theorem.

## 1. Ring, trace, and coefficient conventions

Write t = m/n. Both fields are power-two cyclotomic fields, with the full integer rings R and S as stated. The inclusion satisfies w = z^t. As an R-module,

S = direct sum, for j = 0,...,t-1, of R z^j.

For an arbitrary element b in L, use this same basis with coefficients b_j in K. The K-conjugates of z are z times the t-th roots of unity. Their sum on a power gives

Pi(z^k) = 0 if t does not divide k,
Pi(z^k) = w^(k/t) if t divides k.

Thus Pi selects precisely the ordinary power-coefficient positions divisible by t. This verifies the normalization by t; using the unnormalized trace would change the dual-ideal calculation.

Multiplication by z is a signed cyclic permutation in the ordinary m-dimensional coefficient basis, since z^m = -1. It preserves the stated Euclidean norm and every S-ideal. Each row of the coefficient multiplication matrix of a has squared Euclidean norm ||a||^2. These facts are specific to the given power basis and are not an arbitrary-basis assertion.

## 2. Claim 1: normalized trace duality

First determine the relative dual of S with target I. Write

b = sum_{j=0}^{t-1} b_j z^j,  b_j in K.

Testing against 1 gives Pi(b) = b_0. For 1 <= k <= t-1, testing against z^k gives

Pi(b z^k) = w b_(t-k).

No other term contributes because 0 <= j+k <= 2t-2. Since w is a unit of R, these tests show

Pi(bS) subset I  if and only if  every b_j belongs to I
               if and only if  b belongs to IS.

The converse also follows directly by multiplying R-basis expansions. This includes t = 1.

Now assume Pi(aF) subset I. For every f in F and s in S, fs belongs to F, so Pi((af)s) belongs to I. The preceding duality gives af in IS. Therefore aF subset IS. Conversely, aF subset IS implies Pi(aF) subset I.

Consequently the desired set is the ideal quotient (IS:F). For nonzero F, invertibility of ideals in the integer ring S yields

(IS:F) = IS F^(-1).

For completeness, the equality can be seen without treating an ideal quotient as a black box. If aF subset IS, write 1 as a finite sum of products f_i g_i with f_i in F and g_i in F^(-1). Then a = sum_i (af_i)g_i belongs to IS F^(-1). The converse follows from F^(-1)F = S.

If the phrase "integral R-ideal I" permits I = 0, both sides are zero: the dual-basis tests force af = 0 for every f in F, and F contains a nonzero element. Thus this edge case does not require an unstated nonzero-I premise.

Claim 1 is established with the complete normalized pairing, not merely an inclusion.

## 3. Claim 2: complement, norm, trace, and simultaneous cap

Since J divides IS in the ideal factorization, removing one J factor leaves the integral ideal

C = IS J^(-1).

Oddness of I is compatible with the setting, but this integrality argument itself only needs the stated divisibility.

The R-module decomposition gives

S/IS = direct sum of t copies of R/I

as finite additive groups. Hence N_S(IS) = M^t. Multiplicativity of ideal norms then gives

N_S(C) = M^t / D.

Applying Claim 1 with F = J proves Pi(aJ) subset I for every a in C.

If N_S(C) <= 2^(rho m) and D <= 2^(rho m), then

M^t = N_S(C)D <= 2^(2 rho m).

Taking an m-th root and using t/m = 1/n gives

A = M^(1/n) <= 2^(2rho).

There is no converse claimed, and the inequality is only a necessary condition for the two norm caps. The case rho = 0 has no proper nonzero prime J satisfying D <= 1; this is an empty parameter case rather than a problem with the implication.

## 4. Claim 3: the exact Gaussian moment

Let Lambda be the coefficient lattice of J. Its covolume is D. Define the complete normalizers

Z_Lambda(W) = sum_{x in Lambda} exp(-pi ||x||^2/W^2),

Z_dual(W) = sum_{y in Lambda^*} exp(-pi W^2 ||y||^2).

Every sum here includes zero. Poisson summation gives

Z_Lambda(W) = (W^m / D) Z_dual(W).

All the Gaussian sums and their polynomially weighted versions converge absolutely, so the moment transform and termwise summations below are justified.

For every real coefficient vector u, applying Poisson summation to
<u,x>^2 exp(-pi ||x||^2/W^2) gives

sum_{x in Lambda} <u,x>^2 exp(-pi ||x||^2/W^2)
 = (W^m / D) [
     (W^2/(2pi)) ||u||^2 Z_dual(W)
     - W^4 sum_{y in Lambda^*} <u,y>^2 exp(-pi W^2 ||y||^2)
   ].

Dividing by the entire primal normalizer yields the exact identity

E[<u,X>^2]
 = (W^2/(2pi)) ||u||^2
   - W^4 [
       sum_{y in Lambda^*} <u,y>^2 exp(-pi W^2 ||y||^2)
       / Z_dual(W)
     ]
 <= (W^2/(2pi)) ||u||^2.

In particular, the coefficient second-moment matrix is bounded above by
(W^2/(2pi)) times the identity in positive-semidefinite order. This bound does not assume spherical geometry of J, a smoothing parameter, or a continuous-Gaussian replacement. It holds for every positive W. Centering on the entire lattice, with zero retained, is essential to this derivation.

Let T_a be the coefficient matrix of x -> Pi(ax). It consists of the n rows, at indices 0,t,...,(n-1)t, of the negacyclic multiplication matrix of a. Therefore

||T_a||_F^2 = n ||a||^2.

Apply the preceding directional estimate to each of those rows and sum:

E ||Pi(aX)||^2 <= (n W^2 ||a||^2)/(2pi).

This verifies the exact moment constant and the coefficient-norm convention. The short-multiplier bound is not needed for this step; it is used later to obtain the stated certificate.

## 5. Claim 3: zero mass, with full conditional normalizers

Minkowski applied to the coefficient lattice of J gives a nonzero v in J with

||v|| <= sqrt(m) D^(1/m).

One way to obtain precisely this constant is the coefficient cube with side length 2D^(1/m), first enlarged strictly and then passed to a limit using lattice discreteness. Since D <= 2^(rho m) and rho < 1,

||v|| < 2 sqrt(m).

For the given nonzero a, choose a power z^r such that Pi(a z^r v) is nonzero. Such an r always exists. Indeed, av is a nonzero field element. Choose a nonzero coefficient at position j. If j = 0 take r = 0; if j > 0 take r = m-j. The constant coefficient of z^r av is respectively that coefficient or its negative, and no other coefficient contributes to the constant position. Pi retains this coefficient.

Put f = z^r v. Then f is in J, ||f|| = ||v||, and T_a f is nonzero. The choice uses a and J before the fresh sample; it is an existence proof for the anti-concentration direction, not a claimed efficient subroutine.

Partition J into all cosets of the subgroup Zf. No primitivity assumption on f is required. In a coset b + Zf, write

b = b_perp + tau f,  with b_perp perpendicular to f.

Under the exact Gaussian, the conditional probability of b + kf, given that entire coset, is

 exp(-pi (k+tau)^2/alpha^2)
 ---------------------------------------------------,
 sum_{ell in Z} exp(-pi (ell+tau)^2/alpha^2)

where alpha = W/||f||. The transverse factor has canceled from both numerator and denominator. In particular, this is the complete shifted one-dimensional normalizer, not a sum over nonzero points or over a finite range.

The condition W >= 4sqrt(m) ensures alpha > 2. One-dimensional Poisson summation gives

sum_{ell in Z} exp(-pi (ell+tau)^2/alpha^2)
 = alpha sum_{q in Z} exp(-pi alpha^2 q^2) exp(2pi i q tau)
 >= alpha [1 - 2 sum_{q>=1} exp(-pi alpha^2 q^2)].

Set r_0 = exp(-pi alpha^2). Since alpha >= 2, r_0 <= exp(-4pi) < 1/5, and

sum_{q>=1} exp(-pi alpha^2 q^2)
 <= sum_{q>=1} r_0^q
 = r_0/(1-r_0).

Thus the conditional normalizer exceeds alpha/2. The numerator is at most one, so every conditional point mass is at most 2/alpha.

The equation T_a(b+kf) = 0 has at most one integer solution k, because T_a f is nonzero. Consequently

Pr[T_a X = 0 | X in b+Zf] <= 2||f||/W.

Averaging over the countable partition of J gives

Pr[Pi(aX)=0]
 <= 2||f||/W
 <= 2sqrt(m) D^(1/m)/W
 <= 4sqrt(m)/W.

This includes X = 0 and every other point in the trace kernel. It is not a bound on Pr[X=0] alone. No conditional nonzero-Gaussian distribution or renormalization has been substituted for the stated full law.

## 6. Claim 3: success event, TV transfer, and failures

Let

B_a = sqrt(n/(2pi h)) W||a||,  0 < h < 1.

It is positive. Markov's inequality applied to the exact second moment gives

Pr[||Pi(aX)|| > B_a] <= h.

On J, ideal membership of the output follows exactly from Claim 2. Combining the large-output event with the zero event gives exact-reference failure probability at most

4sqrt(m)/W + h.

For a full implemented law, take the sample space to include its off-ideal representations and any sampler-failure symbols. Define the deterministic output map to tag failure on every such off-ideal or failed input. On an ideal input, use Pi(ax), and define success to require a nonzero output of norm at most B_a. The reference law assigns zero mass to off-ideal inputs and failures.

The total variation inequality applies directly to this single full failure event. If its distance from the complete reference law is at most eta, then

Pr_implemented[failure]
 <= min(1, eta + 4sqrt(m)/W + h).

No conditioning on successful sampling, no deletion of the zero sample, and no separate renormalization are legitimate or needed. Applying an arbitrary rejection or restart step would require analyzing its full resulting law again.

An arbitrary TV-approximate law need not satisfy the moment estimate. For example, replace an eta fraction of an exact Gaussian by a point mass at a very long vector kf in J with T_a f nonzero. Its TV distance is at most eta, but its output second moment can grow without bound as k grows. The packet correctly transfers an event bound, not an unbounded expectation.

The displayed success lower bound is positive precisely when the untruncated error expression is strictly below one. At W = 4sqrt(m), that expression already exceeds one because h > 0, so this stated guarantee is vacuous at the allowed endpoint. This does not contradict the stronger intermediate estimates or the validity of the bound.

### Random multipliers

Let mu be the law of U on allowed nonzero multipliers. Under the independent reference law mu times D_(J,W), conditioning on U = a leaves exactly D_(J,W) for X. The fixed-a proof therefore gives

E[||Pi(UX)||^2 | U=a] <= nW^2||a||^2/(2pi).

The tower property gives

E||Pi(UX)||^2 <= (nW^2/(2pi)) E||U||^2.

The norm and membership hypotheses must hold pointwise for every allowed output. The common stated norm bound in particular makes this second moment finite when the parameters are fixed.

For the implemented pair, either of the packet's two sufficient TV premises works:

1. If each conditional implemented sample law given U=a has TV distance at most eta from D_(J,W), integrate the conditional failure bounds over the actual multiplier law.
2. If the implemented joint law has TV distance at most eta from mu times D_(J,W), transfer the single joint failure event, whose threshold is B_a on the fiber U=a.

This argument also covers a stated joint reference multiplier law when the implemented multiplier marginal differs slightly: that difference is already charged in the joint TV distance.

Marginal control of X alone supplies neither argument. The insufficiency is real even with pointwise valid, bounded multipliers. When t > 1, for each nonzero x in J the rational map a -> Pi(ax) has kernel dimension m-n > 0. The full lattice C therefore contains a nonzero element a_x in that kernel. On any finite set H of Gaussian inputs one can choose one such multiplier per input; at x=0 choose any nonzero multiplier. These choices constitute a finite set, so some finite C0 makes every chosen multiplier satisfy the prescribed norm cap. Outside H choose one fixed allowed multiplier. Sample X from the exact marginal law and set U to the corresponding multiplier. Then X has zero marginal TV error while Pi(UX)=0 throughout H. H can have reference probability arbitrarily close to one, independently of choosing W large enough that the claimed independent-law error bound is small. The joint law can equally be sampled by first drawing U and then drawing X from its conditional law; this does not restore the missing conditional TV or reference independence.

Admissible t > 1 instances exist. For example, n=2, m=4, I=(3) in Z[i] has norm 9. Modulo 3, X^4+1 factors as
(X^2+X+2)(X^2+2X+2), both irreducible. Either corresponding prime J has norm 9. A rho sufficiently close to one meets D <= 2^(rho m). Thus the preceding example of marginal insufficiency is not restricted to an empty parameter regime.

If a multiplier algorithm itself fails with probability delta, the event bound is applied only on branches satisfying the full nonzero, membership, norm, and sample-law premises. Charging those invalid branches yields, for example, the safe upper bound

min(1, delta + eta + 4sqrt(m)/W + h),

when eta is the bound on the valid branches. This is a separate failure budget; a pointwise multiplier hypothesis cannot be replaced silently by an average norm claim.

## 7. Claim 4: shortest-vector comparison and Minkowski existence

For every coefficient vector x in K, the cyclotomic embeddings obey the power-basis Parseval identity

sum_sigma |sigma(x)|^2 = n ||x||^2.

For x nonzero in I, the principal ideal (x) lies in I, so

|N_(K/Q)(x)| >= N_R(I) = M.

The arithmetic-geometric mean inequality applied to the embedding magnitudes gives

|N_(K/Q)(x)|
 = product_sigma |sigma(x)|
 <= [ (1/n) sum_sigma |sigma(x)|^2 ]^(n/2)
 = ||x||^n.

Consequently every nonzero x in I has ||x|| >= M^(1/n) = A, and

lambda_1(I) >= A.

Whenever the success event holds,

||Y||/lambda_1(I) <= B_a/A.

The supplied multiplier bound gives exactly

B_a/A
 <= C0 sqrt(nm/(2pi h)) W / D^(1/m).

This uses the ordinary coefficient norm; no unannounced canonical-norm scale has been introduced.

Because D is a positive integral ideal norm, D^(1/m) >= 1. Also n <= m. Thus polynomial numerical bounds on m, W, C0, and h^(-1), relative to an explicit input-size parameter, imply a polynomial numerical upper bound on this approximation certificate. Polynomial bit length of W is insufficient: a value W = 2^k has only O(k) bits but an exponentially large numerical effect on the certificate.

For existence of the multiplier, the coefficient covolume of C is its absolute norm,

det(C) = N(C) = M^t/D.

Minkowski applied to the coefficient cube gives a nonzero a in C with

||a|| <= sqrt(m) det(C)^(1/m)
       = sqrt(m) A/D^(1/m).

As in the preceding application, enlarging the cube slightly and passing to a limit justifies the non-strict endpoint constant. Hence C0 = 1 is a correct existence statement. Minkowski's theorem provides no polynomial-time method to find that vector.

## 8. Computational promises and omissions

The following distinctions in the packet are necessary and are respected by its conclusions.

- The numerical certificate is conditional on receiving the supplied multiplier and the prescribed sample law. It does not produce either object.
- Positive stated success need not be inverse polynomial. A margin can be positive and exponentially or still more rapidly small while the other listed numerical parameters remain polynomial. Thus positivity alone does not support a polynomial repetition bound.
- Repetition would require a quantitative lower bound on conditional success in fresh trials and the fully charged cost of those trials and their setup. No amplification theorem is present.
- The stated independence from fresh binary secrets is an external premise. Nothing in the algebra proves that an upstream application meets it, particularly if its ideals or multiplier-selection inputs depend on that secret.
- A sampler or oracle for one family of ideals cannot be transferred to another ideal by this theorem. Its availability on J is a premise.
- The exact Gaussian normalizer and its infinite support are used as a reference law. Neither the Poisson proof nor the event transfer supplies an exact finite-time sampler.
- A bounded finite-support implementation must account for truncation, failure, and all other law changes in the asserted full-law TV distance or a separately justified failure budget.
- No standard computational hardness statement follows from these deterministic and probabilistic bounds.

For explicitly supplied ordinary rational coefficient bases and finite rational/integer sample coordinates, the coefficient operations used here have polynomial bit complexity in the complete represented input sizes. Negacyclic multiplication uses finitely many additions and products; Pi selects coefficients; squared norms are rational sums of squares; exact membership in a supplied rational lattice can be decided by exact linear algebra and checking integral coordinates. Rational linear algebra has polynomial bit bounds in the matrix dimensions and input bit lengths. The same statement requires counting the ideal bases and multiplier representation, not just a bound on the sampler output.

These facts do not subsume the cost of finding the represented bases, recovering a multiplier from some other representation, obtaining a norm guarantee, evaluating an unspecified real-number oracle, computing a sample law or its TV certificate, or executing a supplied sampler. The packet expressly leaves actual sampler/setup/recovery-code costs charged separately. A real comparison with the displayed threshold involving pi is a mathematical event definition; it need not be implemented to output Pi(aX) and prove the event bound.

## 9. Boundary checks and final disposition

The reconstruction covers t=1, arbitrary nonzero integral F, the possible zero target ideal in Claim 1, the full Gaussian mass at zero, nonprimitive short directions, all trace-kernel points, arbitrary lattice shape, off-ideal implemented samples, randomized multipliers, and vacuous success parameters.

The nonzero-multiplier condition is essential: a=0 would make the output always zero. The norm cap D <= 2^(rho m), rho<1 is used in the short-direction argument; the moment statement alone does not require it. Neither the zero estimate nor the TV transfer assumes that the implemented distribution has a finite second moment.

Disposition: no mathematical counterexample or missing hypothesis was found within the stated scope, and direct proofs of the exact claims are given above. All solver, sampler, input-encoding, independence, and success-margin limitations remain as stated. This report makes no project-level acceptance or completion action.
