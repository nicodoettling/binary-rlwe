# Nonauthor full-proof review: planted information, frozen v1

Reviewer role: G, full/source referee, not blind. The same-model lineage is correlated with the other project reviewers; this is an independently worked audit, not independent statistical confirmation. No theorem or proof file was edited. No goal, spawned agent, external session, service, install or Git operation was used. Writes are confined to the assigned directory.

Verdict: **PASS of this full-proof review for the exact frozen v1 statement and proof.** No counterexample or load-bearing gap was found. This is a referee recommendation, not final project acceptance. Fresh blind review, structural reconciliation, source-scope reconciliation and the final artifact gate remain coordinator obligations. The standard computational foundation remains OPEN.

## Exact target and material read

- `coordinator/planted-information/theorem-v1.md`, SHA256 `536bb0235e7ccd11563d6f731a4935822a664ae393eb5ae301dbdad89a1ac5e1`.
- `coordinator/planted-information/proof-v1.md`, SHA256 `57a314f1f9c4671194b4943b20873b5ad1e8f8c5043cb6308ae89b8605177eb4`.
- Assigned instructions, SHA256 `48af4dd551be1f073dfca5115786d8eee2a0c0a8ccbde5cd7a62b10bf567c46a`.

Both frozen target files were read completely before mathematical work. Comparison inputs were the complete A-FRAC v1 theorem/proof and explicit definitions, the prior integer-error residue test and its original JSON control, the mathematical-proof-audit skill and its two mandatory references, and the allowed administrative resume/launcher/cap records. No other worker's review of this new theorem was read. No primary external theorem was needed: the imported geometry was checked in the supplied A-FRAC proof, and the present ideal/Poisson arguments were reconstructed below. Full law and complexity scope are separately reviewed in `source-parameter-review-v1.md`.

The actual cap sidecar was read before the experiment. Discovery cutoff is 2026-10-18 01:36:14.695009 UTC, worker stop 01:56:14.695009 UTC, graceful shutdown 02:05:09.695009 UTC and hard cap 02:06:14.695009 UTC. The run was well before these limits.

## Frozen model and quantifier order

Fix n a power of two, n>=2; R=Z[X]/(X^n+1), with coefficient Euclidean norm. Let J be a nonzero integral ideal of norm D>=2, with an injective coefficient-binary map into R/J. Assume a Z-basis of J exists whose row matrix has operator norm at most tau. Choose an odd split prime q with gcd(D,q)=1, k>=1, s,sigma,L>0 and

    q > 2 tau sqrt(n) L (n s+sigma).

Conditional on J, sample iid a_i from the centered discrete Gaussian on J^-1 with coefficient width s, reduce naturally to public A_i, then independently sample uniform binary S and iid coefficient discrete Gaussian errors of width sigma. The response is B_i=A_i S+E_i modulo q. The decoder may depend on J and need not be efficient. For the hidden-J extension, J is selected first, from a countable family with common bounds, before the independent S and errors. The success notion is guessing the actual sampled secret, averaged over the full joint experiment, not existence of a compatible secret or success on a selected source branch.

## Dependency and step audit

| ID | Claim | Dependencies and review result |
|---|---|---|
| G-PI-Q | Natural quotient is R/qR and products by J reduce correctly | Ideal inverse, finite index D, q coprime D; checked |
| G-PI-D | J_a differs from J exactly on the stated prime-divisor union | Prime valuations in the Dedekind ring; checked, including zero samples and repeated prime powers |
| G-PI-C | Source coset law is eps_s-close to uniform | Poisson on Z^n with numerator and denominator retained; checked |
| G-PI-G | Generator loss <=chi_J(k)+k eps_s | G-PI-D/C, iid labels conditional on J before selection; checked |
| G-PI-P | Explicit prime-norm upper bound for chi_J(k) | Cyclotomic residue order and norm factorization; checked |
| G-PI-T | Full-law bad tail <=min(1,8kn exp(-pi L^2)) | Shifted-theta maximum, exact MGF, coefficient/canonical normalization; checked |
| G-PI-U | Both integer products are recovered by centered public lifts | G-PI-Q/T and strict displayed q inequality; checked |
| G-PI-S | Decoder returns the unique actual S on good tail and J_a=J | G-PI-U, invertibility of J, binary injectivity; checked |
| G-PI-H | Full posterior and optimal success unchanged by hiding J | Exact common response likelihood and prior; checked without postselection |
| G-PI-R | Final success bound and family average | Union bound on original law and G-PI-G/T/S/H; checked |

### 1. Quotients and effective denominator ideal

R is the ring of integers in the power-of-two cyclotomic field; every nonzero ideal is invertible. Put Lambda=J^-1. Then R is contained in Lambda and the finite quotient Lambda/R has order D. Multiplication by q is a bijection on that quotient. Consequently every a in Lambda can be written a=r+q ell with r in R, ell in Lambda. The kernel of R -> Lambda/qLambda is exactly qR: if r=q ell is integral, then q[ell]=0 in Lambda/R, so ell lies in R. This establishes the claimed natural isomorphism without coefficient rounding. For j in J, ja-jr=qj ell lies in qR, proving the public product identity.

For a prime P, write e_P=v_P(J). Each source point has valuation at least -e_P. The ideal

    J_a={z in R: a_i z in R for every i}

has valuation max(0,max_i(-v_P(a_i))). At primes not dividing J the source points are already integral, hence this exponent is zero. At P dividing J, the exponent equals e_P precisely when some sample has valuation -e_P. It is smaller precisely when every sample belongs to P Lambda. For a zero source point use v_P(0)=+infinity; the formula and event characterization still hold. Repeated powers of P do not introduce a new probability factor: detecting the top allowed denominator valuation is enough.

An equivalent invariant is J_a=(R+sum_i a_i R)^-1. The explicit R term explains why the samples need not generate the whole fractional ideal at primes outside J. The proof does not substitute the stronger and unnecessary event that the a_i generate Lambda globally.

### 2. Coset normalizers and the single TV charge

For a coset label c in Lambda/R, the exact probability is

    p_c = rho_s(R+c) / sum_d rho_s(R+d).

Poisson summation gives rho_s(R+c)/s^n as a Fourier series with constant term 1. The sum of the absolute values of all nonconstant coefficients is exactly

    Delta_s = (1+2 sum_(m>=1) exp(-pi s^2 m^2))^n-1.

Thus r_c=rho_s(R+c)/s^n lies in [1-Delta_s,1+Delta_s]. The exact denominator is D times the actual average r_bar. For Delta_s<1,

    TV(p,uniform) = (1/(2D)) sum_c |r_c-r_bar|/r_bar
                  <= Delta_s/(1-Delta_s).

Taking the minimum with one and using the trivial bound when Delta_s>=1 reproduces eps_s. This does not replace rho_s(Lambda) by D s^n without charging its deviation.

The k coset labels are genuinely independent conditional on the fixed J. A product hybrid bounds their joint TV distance by k eps_s; this is performed on the original source law before the tail event. Under independent uniform labels, P Lambda/R has index N(P) in Lambda/R, because R is contained in P Lambda for P dividing J and [Lambda:P Lambda]=N(P). Its probability is 1/N(P), and all k labels lie there with probability N(P)^(-k). One union bound over primes plus one joint TV charge gives the exact claimed loss. There is no unjustified independence among prime-divisor events, and no multiplication after conditioning on the good tail or a denominator event.

### 3. Explicit prime-divisor bound

Modulo 2, X^n+1=(X+1)^n. Thus there is exactly one prime ideal above 2 and its residue field is F_2, so its norm is 2. It divides J exactly when 2 divides D.

For any odd residue characteristic, the image x of X satisfies x^n=-1 !=1 and x^(2n)=1. Because 2n is a power of two, its multiplicative order is exactly 2n. Hence 2n divides N(P)-1 and N(P)>=2n+1. If m distinct odd primes divide J, norm factorization gives D>=product_P N(P)>=(2n+1)^m. Therefore m<=log D/log(2n+1), and summing N(P)^(-k) proves the displayed explicit bound. No integer or ideal factorization algorithm is required for this numerical upper bound.

### 4. Full-law Gaussian tail with all factors

For any full-rank real lattice M and u>0, Poisson summation makes rho_u(M-v)<=rho_u(M) for every real shift v: the centered dual series has positive coefficients, and a shifted series cannot have larger absolute value. Completing the square in the exact discrete Gaussian mass gives

    E exp(<h,X>) = exp(u^2||h||^2/(4pi))
                  rho_u(M-u^2 h/(2pi))/rho_u(M)
                <= exp(u^2||h||^2/(4pi)).

No shifted-theta factor is silently removed. Chernoff optimization at 2pi t/(u^2||v||^2) gives the two-sided tail 2 exp(-pi L^2) at t=u||v||L. This is valid at every positive width; it does not need smoothing or an approximately continuous source.

For a primitive 2n-th root zeta, the real and imaginary evaluation vectors each have squared norm n/2. The geometric sum sum_(j=0)^(n-1) zeta^(2j)=0 proves this, including n=2. If the complex evaluation exceeds u sqrt(n)L in modulus, one component exceeds u sqrt(n/2)L. The resulting factor is 4 exp(-pi L^2) per sample and embedding. Applying this separately to a_i and E_i, then union bounding over k samples and n embeddings, gives 8kn exp(-pi L^2), capped by one. Conjugate embeddings are redundantly counted but never undercounted. Dependence between embeddings is harmless.

The full source/error tail event is defined before S and before denominator conditioning. It is uniform conditional on every J. It is independent of S, but the deterministic bound for all binary S is enough and no later use requires a conditional iid claim.

### 5. Fourier normalization and exact public unwrapping

For coefficient vectors, the normalized negacyclic Fourier transform is unitary, and multiplication by a has operator norm max_zeta |a(zeta)|. Equivalently, the unnormalized embedding norm is sqrt(n) times the coefficient norm. This is the place where a missing sqrt(n) would matter; the stated proof has the correct factor.

Each row j_l has coefficient norm at most the operator norm tau of the row matrix. Since |S(zeta)|<=n for every coefficient-binary S, the good event gives

    ||j_l a_i|| <= tau s sqrt(n)L,
    ||j_l(a_i S+E_i)|| <= tau sqrt(n)L(n s+sigma).

Both vectors have integer coefficients. The latter norm is strictly below q/2 by hypothesis; the former is smaller because n>=2 and sigma>0. Every coefficient is then strictly between -q/2 and q/2, so the centered lift of each public product is uniquely its actual integer value. The proof only needs an existentially selected basis, and uses the same deterministic choice for each fixed J. No unwrapped a_i or proof mask is supplied as public data.

### 6. Decoder correctness and actual-secret uniqueness

The decoder accepts binary s' when every v_il-u_il s' lies in J. The actual S passes because the residual is j_l E_i in J. If two candidates pass, their difference z satisfies a_i j_l z in J for every basis vector. Z-linearity extends this to a_i z J contained in J. Since J is invertible, (J:J)=R and hence a_i z lies in R for every i. Thus z lies in J_a. If J_a=J, binary injectivity modulo J forces z=0.

This argument remains valid even though candidate products u_il s' are computed as ordinary integer/rational ring expressions rather than reduced again modulo q: the true products u_il,v_il have already been unwrapped. Membership in J is exact. A tie or no-candidate rule outside the good event may be arbitrary, since the lower bound only uses correctness on the intersection of the two good events.

Combining the preceding points gives success at least 1-Pr[tail bad]-Pr[J_a!=J], with no asserted independence between these failures. This is exactly the theorem's lower bound after capping at zero.

### 7. Hiding J: complete Bayes calculation

Let pi_j be the prior on ideals. Define F_j(A) to be the exact conditional source probability of the public multiplier tuple, and let

    W_sigma(r) = rho_sigma(r+qR)/rho_sigma(R),
    H_s(A,B) = product_i W_sigma(B_i-A_i s).

Then the entire joint mass is

    Pr[J=j,A,B,S=s] = pi_j F_j(A) 2^(-n) H_s(A,B).

For a positive-mass (j,A,B), division by the actual normalizer gives

    Pr[S=s | j,A,B] = H_s(A,B) / sum_b H_b(A,B).

Summing the joint mass over j first produces exactly the same expression for Pr[S=s|A,B], because the common factor becomes sum_j pi_j F_j(A). No assumption that J is independent of A is made or needed. No use is made of a posterior restricted to the good tail event or J_a=J. In the full Gaussian model every wrapped error value has positive mass; for general finite analogues absent branches receive no asserted conditional value.

Equality of the complete finite secret posterior yields equality of its maximum and hence of optimal actual-secret guessing success. A fixed common maximum-likelihood rule with fixed tie-breaking already ignores J. Averaging the pointwise-in-J lower bound with the stated common constants proves the countable-family result. This is statistical equality of information, not an algorithm to recover J, simulate J conditional on A, or find a short basis efficiently.

## Finite falsification/control and regressions

The approved G-PI-FV1 job used 624,328 prior atoms, exact integers and rational reporting, 3.66 seconds wall time and 14,336 KiB maximum RSS. It exited 0. Full code/input/command/original output/resource report are adjacent. The planted q=101 controls achieved actual p_guess 11/12 for k=1 and 107/108 for k=2; denominator failure was 1/9 and 1/81 respectively, and every good-denominator atom had a unique correct decoder output. The full comparator endpoint was enumerated at q=101,k=1 and q=5,k=2, and its inverse likelihood formula matched every mass. q=101,k=2 comparator enumeration was not performed because it would exceed the atom reservation; the arbitrary-k endpoint formula is proved above and in the separate source review.

The hidden J=3R/6R mixture checked every positive posterior vector by exact cross-products. There were 576 positive J,A,B cells with overlapping nonzero A support, so the check was not limited to an uninformative zero multiplier. Both metadata choices gave guessing probability 103/108. All zero-mass posterior branches were excluded explicitly.

The deliberate small-q failure and its first witness were preserved in `counterexample-scope-v1.md`. The theorem's modulus premise prevents that failure; the finite distribution is never substituted for the Gaussian law. The prior continuous-mask support/leakage failure is also retained there and is not reused as a public-information argument.

The original CP1 enumeration reproduced 21/2000 > 1/100 and the still-residual second incidence 21/221. It rejects the old marginal-product inference. Here, products are used only for original iid source labels conditional on J and original independent target errors; all selected-event losses are union-bounded. Latent cache-hit information is absent from the model and never introduced as a branch variable.

## Residual gates and limitations

No repairs are requested for the frozen mathematical statement. The exact finite controls strengthen the check of its combinatorial and posterior mechanisms but do not certify the infinite Gaussian tail or an asymptotic hardness statement. The proof review supplies those elementary analytic arguments separately. Final acceptance still requires the coordinator's fresh blind/structural and artifact gates. The theorem gives an information-theoretic obstruction to a low planted-guessing claim only in its stated binary-injective, large-q regime; no standard source-hardness foundation follows.
