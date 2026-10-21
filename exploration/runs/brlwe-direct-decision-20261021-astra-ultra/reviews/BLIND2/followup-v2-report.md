# BLIND2 exact-v2 statement-only recheck

This separate report does not alter the original independent report or seal. The complete follow-up assignment, verified input hashes, independently generated statement comparison, and exposure log are preserved with the followup-v2 prefix. No current author proof, repair note, other review, or current scientific status was read.

## Verdict

**FIXED-MAIN-v2 is ACCEPTED in the same explicit conditional scope as the quantitative reduction in my original sealed report.** The changed scope wording resolves the only textual gate I identified in v1. It makes no change to the assumptions, parameters, distributions used in the distinguishing promise, algorithm, success estimate, finite costs, source family, or inherited dependencies.

The two optional claims in nonvacuity-statement.md are independently ACCEPTED. They are not dependencies of the main reduction and do not establish efficient distinguishing algorithms, source hardness, or a quantum composition.

Exact reviewed statement hashes:

    fixed-main-statement-v2.md
    3358158fb5f138b584de4dc726c63b21af58b2f669fc0f291bcef62826a80359

    nonvacuity-statement.md
    0e4642921bb9e6a63c2c087357bd1a216b57bdc1f126e0486f06a12e0d9144bf

The coordinator's unsanitized source hash is supplied in the input manifest, but that file was not read; this recheck certifies the exact supplied statement bytes above. The manifest says only its status paragraph was removed. The mathematical statement, not an unseen status banner, is the reviewed object.

## Exact changes and their meaning

My own byte comparison of the permitted v1 and v2 files finds only the version title and final paragraph changed. In particular no numerical or resource claim was silently repaired. The comparison is preserved in followup-v2-independent-diff.txt.

The new paragraph correctly separates three facts:

1. Every actual D0 execution receives pairs represented modulo the same prescribed q0.
2. D0's assumed distinguishing gap refers to the exact binary-secret, independent coefficient discrete-Gaussian target law.
3. Actual executions include transformed and hybrid inputs. The all-input bound makes those executions legal; MR supplies the statistical comparison needed to transfer the distinguishing gap to the auxiliary target experiments.

MR need not assert that every individual hybrid or C8-induced call is statistically close to D0's promised planted experiment. In the composition it establishes the auxiliary distinguisher's fixed input-distribution gap once. The extractor then analyzes exact hybrid expectations of the supplied Boolean code, and the source information bound handles arbitrary behavior on the fractional-source transcripts. This is precisely the interpretation supported by the new wording and by my original derivation.

The original public-law counterexample remains a useful regression: if q0 is even and an auxiliary q is odd, no deterministic map from one uniform Z/qZ coefficient can give an exactly uniform Z/q0Z coefficient. V2 makes no such assertion. It retains the all-input code access needed when exact target-law simulation is unavailable. Thus this counterexample no longer rejects any sentence in the revised scope paragraph.

The added quantifier clarification is also correct. In the displayed family b and c are fixed before target parameters are chosen, and sigma0=n^(b+c+4) depends on those constants. A single fixed exponent d cannot cover all polynomial sample/advantage exponents through sigma0=n^d: taking k0=n^b and epsilon_*=n^(-c), the explicit lower guard already requires sigma0 to be at least a constant times n^(b+c+2). Choosing b+c+2>d defeats that guard for sufficiently large n. This exact targeted boundary check validates the clarification without changing the general finite theorem, which accepts any supplied parameters satisfying its displayed guards.

Every inherited-scope restriction from the original report remains: the norm-restricted ideal family, pointwise ideal metadata, true supplied numerical guards, all-input finite code, actual sample and call counts, charged scalar evaluation costs, and exact B-GP/C8/A-FRAC interfaces. This recheck is not a new proof of the inherited C8 theorem or a global acceptance of unreviewed artifacts.

## Optional finite bounded oracle premise

Let L=log2(8n). It is an integer because n is a power of two. With n>=128 we have L>=10. Let B=ceil(sigma0*L), and let H be the image of the integers [-B,B] modulo q0.

The described algorithm has at most2^n candidate iterations. Each performs ordinary finite ring arithmetic and tests membership in H. H need not be explicitly enumerated: residue membership in an interval image is decidable by exact integer arithmetic. Thus the algorithm is deterministic and all-input bounded, with time at most2^n times a polynomial in the full input encodings. It ignores all other samples, which is valid for every k0>=1. No efficient-runtime conclusion is being made.

For E~D_(Z,sigma0), completing the square in its actual normalized mass gives

    E exp(tE)=exp(sigma0^2*t^2/(4pi))
        *rho_sigma0(Z-sigma0^2*t/(2pi))/rho_sigma0(Z).

The shifted theta is at most the centered theta by Poisson summation. Chernoff therefore yields P(|E|>=sigma0*L)<=2exp(-pi*L^2). In the planted world the actual binary S is one enumerated candidate; the algorithm accepts whenever all its first-sample error coefficients satisfy |E_i|<=B. Hence

    P_planted[accept]>=1-2n exp(-pi*L^2)>=3/4.

For the last inequality, 8n=2^L and pi*L^2>=L*ln2, so exp(-pi*L^2)<=1/(8n). No normalizer has been replaced by a continuous approximation, and the closed interval/ceiling at B only helps this tail estimate.

In the comparator, conditional on any A_1 and any candidate s, B_1-A_1*s is uniform in the ring. Its coefficients are independent uniform residues. Thus

    P_uniform[accept | A_1]
       <=2^n (|H|/q0)^n
       <=[2(2B+1)/q0]^n
       <=[(4L+6)/n]^n.

Here B<=sigma0*L+1, q0>=n*sigma0 and sigma0>=1. This is a union bound over guesses, not an independence assumption about those guesses. It remains valid if interval images overlap modulo q0.

At n=128,L=10 we have n>=8L+12. When n doubles, L increases by one and this inequality remains true. Consequently it holds for all stated powers of two, and (4L+6)/n<=1/2. This proves the uniform acceptance bound2^(-n). Subtracting gives gap>=3/4-2^(-n)>=1/2.

The code may ignore ideal metadata, so this is pointwise for every eligible supplied J. In particular the exact finite oracle premises can coexist with the main asymptotic guards for large n, using a distinguisher whose exponential runtime is explicitly charged. The optional claim makes no efficient-distinguisher or hardness assertion.

## Optional normalized separation

Let lambda_infinity be the shortest nonzero canonical-infinity length in J^-1. The full-rank lattice is discrete, so this positive minimum exists. For any nonzero x in J^-1, the ideal (x)J is integral. Its norm |N(x)|*D is a positive integer, hence |N(x)|>=1/D. The maximum over the n complex embeddings is at least their absolute-value geometric mean, giving

    ||x||_canonical,infinity >= |N(x)|^(1/n)
       >=D^(-1/n)>=2^(-rho)>1/2.

Conversely J is integral, so 1 belongs to J^-1 and has canonical-infinity length1. Thus lambda_infinity lies in(1/2,1], as claimed. For any absolute radius r>0,

    r <= r/lambda_infinity < 2r.

Therefore the radius as a fraction of this separation has exactly the same inverse-polynomial scale up to constants. No shortest-vector computation or source hardness premise enters this argument. The endpoint J=R gives separation1, and rho approaching1 from below preserves the strict lower endpoint without a uniform larger-than-one-half margin.

## Evidence and stopping scope

No new experiment was needed or run. The repair's new tests are the exact odd/even public-law regression and the fixed-noise-exponent quantifier check above; both classify the revised wording correctly. The optional claims have short uniform analytic proofs, with explicit threshold arithmetic at n=128 and induction over powers of two. The original sealed finite evidence and CP-1 audit remain unchanged and applicable to the unchanged dependencies.

All original21 sealed artifacts were verified unchanged before this recheck was written. This follow-up is sealed independently before any additional scientific exposure. Its acceptance is local and conditional on the exact declared historical interfaces; the coordinator still owns global dependency, historical-regression and final-artifact certification.
