# Nonauthor full review of B-CUBE-THETA-v1

Frozen review draft, 2026-10-21. This is a full nonauthor mathematical review of the exact `input-v1/theorem-only-v1.md` and `input-v1/proof-v1.md`, with separate dispositions for the concrete family and downstream audit. It is not an acceptance decision or a blind report. Exact input bytes are recorded in `input-hashes-v1.sha256`. No blind materials were consulted.

## Main theorem: no mathematical defect found

For fixed full-rank J subset Z^n, the exact joint mass is 2^-n 1_(y-b in J) rho_t(y-b)/rho_t(J). Maximizing separately for each observation y gives the displayed guessing formula. Randomized decoders cannot improve it because success is affine in their decision distribution. All lattice sums are positive and absolutely convergent, and zero is retained.

The residue lower bound is exact. The residue Y mod J equals S mod J. A fiber of size s has probability s/2^n and posterior maximum 1/s, hence contributes exactly 2^-n. Summing the C_J occupied fibers gives C_J/2^n. The statement correctly avoids saying that the full observation has a uniform posterior on each fiber.

I independently expanded the square in proof equation (2). The difference between its left and right sides is

    r||z||^2/[t^2(t^2+r)] - 2<z,d>/t^2
       + (t^2+r)||d||^2/(t^2 r),

which is exactly the stated nonnegative square. Every binary vertex is at squared distance n/4 from the common center c. The resulting envelope therefore holds pointwise before taking a maximum or summing.

The numerator is supported on precisely the occupied cosets. Within each occupied coset the envelope is summed over the entire coset; no actual Gaussian coset weight is asserted uniform. Poisson summation and the triangle inequality bound rho_u(J+v) by rho_u(J). The separate ratio rho_u(J)/rho_t(J) is bounded by (u/t)^n because the positive dual theta sum decreases term by term as u increases. The denominator includes its zero vector and is never divided by zero. These two steps establish T1 with all normalizers intact. Taking r=t and log(1+1/t)<=1/t proves T2 for every positive numerical t. No unit or dimensional asymptotic assumption is hidden in that substitution.

The collision geometry also checks. C_J<2^n supplies two distinct binary vertices whose difference f is a nonzero ternary member of J. In the power-two cyclotomic field, multiplication by nonzero f is invertible, so its n rotations are independent and have norm <=sqrt(n). The primitive-flag construction from the exact A-FRAC proof applies to these rotations. Its coefficient alpha_i is a positive generator of the projected rank-one lattice and is <=1 because the i-th rotation lies in J. Subtracting earlier integral rotations preserves the primitive quotient class. The resulting basis has column/row lengths <=n sqrt(n) and operator norm <=n^2. This is explicitly existential and supplies neither f nor that basis to an algorithm. The norm bound N(J)<=|N(f)|<=||f||^n<=n^(n/2) follows from ideal containment and Parseval/AM-GM in the stated coefficient normalization.

At t=2n^2 ell, the T2 exponent becomes exactly (pi/8+1/4)/(n ell). The main theorem makes no computational claim based on evaluating C_J, and no accessible Gaussian sampler is assumed. Its metadata qualification is necessary and sufficient for the stated conditional application: conditional on each exposed value, S and G must retain the exact product law. Arbitrary secret-dependent revelation would violate that premise.

## Probability regressions and finite evidence

No sequential event product occurs. The only n-dimensional product factor in the new proof is the exact Poisson scaling (u/t)^n. The block-family product is separately justified by an orthogonal direct-sum lattice, product secret, and product joint observation. It is not a product of selected marginal success probabilities. CP-1's 21/2000>1/100 counterexample remains rejected by the stated model.

I read the complete author's test code and its input-in-code, stdout, resource manifest and preserved exact output structure. The Gaussian check covers 40 rank-two HNF lattices using exact rational weights (15/16)^(x^2+y^2). Its choice t^2=pi/log(16/15), r=t^2/2 makes the T1 upper bound exactly 2C_J/5. The code computes optimal guessing for the finite truncated source, retaining the true finite normalizer. Its raw omitted mass is bounded by

    124(15/16)^1089 / [1-(15/16)^67].

This bound is valid: theta_Z<=1+2 sum_(j>=1)(15/16)^j=31; each one-coordinate tail is bounded by twice the geometric series starting at j=33; a two-coordinate union supplies factor124. Since rho_t(J)>=1, the raw mass also bounds the full normalized truncation probability. Guessing probability is a bounded-event optimum and changes by at most joint TV. Thus the check `finite_guess+tail<=bound` rigorously implies the asserted finite-parameter infinite-Gaussian inequality in each nontrivial tested case. Float output fields are display-only; assertions use exact rationals.

As a separate hand boundary, for n=1,J=2Z the residue reveals the bit and both sides cap at one. For n=2,J=Z^2 the exact guessing probability is ((theta+1)/(2theta))^2; at the test's rational weight theta>1+2(15/16)+2(15/16)^4>4, giving probability<25/64<2/5. This independently checks a nontrivial instance without reusing the envelope proof. Revealing S itself would make guessing one, but fails the theorem's conditional-law premise.

The author's bounded experiment reports exit0, 0.49s wall and19,456KiB maximum RSS under120s/110sCPU/512MiB. Its exact output records the input-code hash. I found no uncharged selected-source or tail-normalizer issue. Finite checks support these explicit parameters and regressions only; they do not prove the general theta theorem or hardness.

## Norm289 family: favorable information and easy-source calculation

The algebraic calculation is consistent. For g=1+Y+Y^2-Y^3+Y^7, multiplication by Y gives the negative reciprocal quartic Y^4-Y^3-Y^2-Y+1. Dividing that quartic by Y^2 gives Q(z)=z^2-z-3, z=Y+Y^-1. Reducing P(z)=z^4-4z^2+2 modulo Q gives3z+2, so Res(P,Q)=9Q(-2/3)=-17. The full field norm is its square289. Modulo17, the quartic factors as the two stated quadratics, and10,12 are distinct roots of Y^2-5Y+1 and of Y^8+1. This proves containment in the index289 ideal and hence equality. Its additive exponent is17.

I inspected the author's independent exact matrix/inverse-residue enumeration record for the precise negative of g. It reports image176 and histogram112,48,16, which sum to176 fibers and256 vertices. The coefficient-block extension is an orthogonal direct sum, so both C_J=176^(n/8) and the full independent-block guessing law follow. This is a strict improvement over the old index-only estimate for this easy explicit family, with no claim of source hardness or novelty priority.

The source distinguisher is correct in both worlds. Since F belongs to J, multiplying the public class of a in J^-1/qJ^-1 by F gives the residue of the actual integral Fa. It is essential to multiply before centered lifting; the proof does so. Its coefficient rows are signed rotations of F of norm sqrt(5), so the exact lattice-Gaussian MGF tail applies without a smoothing premise. Under the comparator, multiplication by F is a bijection on R_q because q is coprime to N(F); all coefficients are exactly uniform, including zero and nonunits. The comparator acceptance count min(q,2floor(K)+1)^n/q^n is therefore exact. At the fixed schedule K=sqrt(10)ell^3, comparison to K can be implemented by the integer squared inequality z^2<=10ell^6; no arbitrary-real equality test is required. The actual q lower bound makes the threshold a small fraction of the centered range. The attack is one public multiplication and coefficient testing, with no hidden f or proof variable.

The multiplication basis of this explicit principal ideal is public, with norm bounds sqrt(5) per column and operator norm<=5. Hence the family is not evidence of hidden short-basis hardness. Its appeal to root's new M1 theorem remains conditional until that theorem's own gates close, but the public basis itself and the easy public-source test are already established independently.

## Changed-premise composition: favorable substitution, distinct certification scope

I checked the proposed substitutions against the exact A-FRAC proof, all four RF4 same-J interface statements, the accepted same-J theorem/acceptance record, and current C8 theorem-v8/acceptance. The obsolete C8 v7 final verifier is not used. A positive supplied delta in the changed gap forces beta_cube<1 and hence C_J<2^n. The collision basis then provides tau2=2n^2 with slack; all Delta_A/eta_A completion bounds keep their old values. The target noise inequality is exactly sigma>=4sqrt(2)n^2 sqrt(kn)ell^4, implied by the frozen sigma. H is integrated out for the noise comparison and exposed only in the completed-world guessing bound, where it is independent of S,G conditional on the source state. This avoids the historical appended-H defect.

The GP bridge is stated for any ordinary integral J coprime toq. Its quotient order and all cap/precision losses do not require the old norm cap. The two complete endpoint TV charges remain Delta_B+kn nu+eta_cap and kn nu+eta_cap, leading to exactly3kn nu+2eta_cap in the gap. That gap is a property of the fixed implemented test and is not charged per adaptive C8 call.

C_J<2^n gives D^(1/n)<=sqrt(n), and the existing q lower bound makes d0<q/(4sqrt(n))<=q/(4D^(1/n)). C8's finite hypotheses therefore remain available. Its kappa condition involving logD is still representable, since logD<=n log(n)/2. The weak coefficient separation lower bound q/(sqrt(n)D^(1/n)) suffices for the unchanged d=d0/sqrt(n) quantum interface. Final scaling, same-J output, zero fallbacks, full TV and the at-most2Q_* coherent Rec execution count consequently remain unchanged under these exact interface substitutions.

This is a favorable compatibility review, not a new complete composition acceptance. The extended theorem must remain a distinct frozen claim with the new cube bound as a new dependency; no acceptance can be inherited through that changed foundational lemma. I have not rerun or re-certified the full finite quantum compiler/setup artifact under a new theorem file. No arbitrary-ideal transfer, efficient C_J algorithm, standard hard family, or numerical polynomial-width conclusion for unrestricted q follows. The main B-CUBE-THETA-v1 gate can be considered separately from that larger certification task.

## Disposition

No blocking mathematical defect found in the main exact theta/cube theorem, its collision geometry, the explicit-family algebra/source distinguisher, or the displayed downstream parameter substitutions. The main theorem is recommended for root's remaining exact-version source, fresh-blind and regression reconciliation gates. The norm289 family and extended composition retain separate statuses and limitations as above. This review issues no final ACCEPT. Same-model scrutiny is correlated, not independent statistical evidence or formal verification.
