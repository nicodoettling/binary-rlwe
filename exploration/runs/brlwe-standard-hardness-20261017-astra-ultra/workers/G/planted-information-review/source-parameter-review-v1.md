# Nonauthor source, parameter and complexity-scope review

Target theorem SHA256 `536bb0235e7ccd11563d6f731a4935822a664ae393eb5ae301dbdad89a1ac5e1`; target proof SHA256 `57a314f1f9c4671194b4943b20873b5ad1e8f8c5043cb6308ae89b8605177eb4`. Both frozen files were read completely. This report is separate from the full-proof review and does not inherit a computational-hardness result from it.

Verdict: **PASS for the exact source law, finite parameter inequality and information-theoretic scope.** No source mismatch or missing normalizer was found. This is a nonblind, same-model referee recommendation; final acceptance remains with the coordinator after the remaining gates. The standard foundation remains OPEN.

## Exact two endpoints

All norms and Gaussian widths in the statement are in coefficient Euclidean coordinates. For fixed J, Lambda=J^-1 contains R. With the specified convention,

    D_(Lambda,s)(a) = exp(-pi ||a||_coeff^2/s^2)/rho_s(Lambda).

For a public residue A in R/qR, choose any integral lift r_A. Its exact planted probability is

    F_(J,s)(A) = rho_s(r_A+qLambda)/rho_s(Lambda).

Changing r_A by qR does not change the coset qLambda. The k-source law is the product of these probabilities conditional on J, because the original unwrapped source draws are iid. The comparator replaces this product by q^(-nk), retaining the same J prior and all optional metadata. Neither endpoint reveals an unwrapped a_i, a short basis or an auxiliary mask variable.

The target error is the coefficient discrete Gaussian on R=Z^n, not a continuous Gaussian and not a rounded continuous one. Its exact wrapped probability is

    W_sigma(e mod qR)=rho_sigma(e+qR)/rho_sigma(R).

Conditional on public A and binary S=s, the response likelihood is product_i W_sigma(B_i-A_i s). Thus the full planted mass, including the actual secret used for success evaluation, is

    pi_J [product_i F_(J,s)(A_i)] 2^(-n)
         [product_i W_sigma(B_i-A_i s)],

while the comparator mass is

    pi_J q^(-nk) 2^(-n)
         [product_i W_sigma(B_i-A_i s)].

Every denominator is retained. The comparator is precisely the uniform-multiplier binary-secret target wrapper with the same independent errors, not merely a matching response marginal. The theorem deliberately makes no assertion about its recovery success. The finite control inverted every mass in the fully enumerated comparator instances against this common response likelihood.

If J is discarded in both worlds, its sum changes only the public-A factor. On every positive-mass (A,B), the entire secret posterior is the common likelihood vector divided by its sum over all 2^n secrets. Equality with the J-conditioned posterior is exact. This survives arbitrary dependence between J and the generated A, countable mixtures, and different prior masses. It would fail if the secret prior or target error channel were allowed to depend on J after fixing A, or if the joint law were conditioned on a secret-dependent future event. Neither modification is permitted by the frozen statement. Conditioning on the proof's good event is not used to prove the posterior equality.

## Coefficient/canonical factors and imported geometry

The coefficient lattice R has determinant one, while the normalized complex embedding matrix is unitary. The unnormalized embedding norm is sqrt(n) times coefficient norm. Multiplication by a has coefficient operator norm max_zeta |a(zeta)|. Therefore the proof's sqrt(n) in each evaluation tail is necessary and present; no discriminant or canonical-volume factor belongs in the Z^n coset-theta calculation.

The hypothesis is an operator-norm bound tau for a row basis of J. It implies each row has norm at most tau. On the original full-law tail event, multiplication by a_i has norm at most s sqrt(n)L, multiplication by E_i has norm at most sigma sqrt(n)L, and multiplication by a coefficient-binary S has norm at most n. These yield exactly

    q > 2 tau sqrt(n)L(n s+sigma).

The strict inequality guarantees unique centered integer lifts. The q/2 threshold is per coefficient; bounding the whole coefficient norm by q/2 is stronger and valid. The phrase about q being larger than sigma must always be read through this actual inequality: the additive n s term cannot be dropped when sigma is small.

I independently checked the supplied A-FRAC geometry proof rather than treating its status as a substitute for proof. The coefficient-cube Minkowski argument gives a nonzero f in J with norm at most sqrt(n)D^(1/n). Its n negacyclic rotations have that norm and are linearly independent because the quotient polynomial defines a field. In the rational flag spanned by the rotations, each primitive projected lattice coordinate has step at most one. Centering earlier coordinates by integer rotations yields a basis row of norm at most n times ||f||. The Frobenius bound on its row matrix is at most sqrt(n) n ||f||, hence at most n^2 D^(1/n). Discreteness handles the Minkowski endpoint. This proves the stated existence substitution without constructing f or solving a basis problem.

With tau=n^2 D^(1/n), the displayed sufficient q condition becomes

    q > 2 n^(5/2) D^(1/n) L (n s+sigma).

If D^(1/n), s, sigma and L have the claimed polynomial sizes, this is a polynomial numerical threshold. The theorem conditions on a supplied split prime satisfying it; it does not prove a particular prime-finding complexity bound or that a prescribed original problem window contains such a prime. The split assumption is stronger than needed for the elementary decoder but matches the stated source setting.

The regime is not empty as pure geometry. For J=mR with an integer m>=2, D=m^n and the binary quotient is injective; the basis mI has operator norm exactly m. Subject to the stated prime and coprimality requirements, sufficiently large q satisfies the inequality. This example provides no hardness for the induced source.

## Loss terms and asymptotic interpretation

The source coset loss eps_s uses full Gaussian theta sums over R, not a Gaussian conditioned to a finite box. The denominator loss is the finite sum over distinct prime ideals dividing J, with each contribution N(P)^(-k). Prime powers need no extra exponent factor, and primes outside J need no contribution. The explicit bound with the single norm-two prime and odd-prime threshold 2n+1 is valid.

For any desired tail tolerance delta in (0,1), L^2 >= log(8kn/delta)/pi suffices for the stated tail loss. For s>=1, the elementary estimate

    kappa_s <= 2 exp(-pi s^2)/(1-exp(-3pi s^2))

follows from m^2>=1+3(m-1), and Delta_s<=exp(n kappa_s)-1. Thus s can make eps_s as small as the desired finite target with explicit theta control. The contribution k eps_s must still be charged. Small individual eps_s is not a license to ignore a growing k. Similarly, fixed inverse-polynomial errors should not be called cryptographically negligible without the intended security-parameter quantifiers.

If 2 divides D, the explicit prime loss includes 2^(-k); for k=1 the general bound need not be close to one. High success requires the complete stated loss sum to be small. The theorem correctly retains this term rather than asserting universal high success for arbitrary k. Tail failure and denominator failure may be correlated; their sum is a union bound, not an assumed product.

## Relation to A-FRAC and the earlier failed mask route

The new theorem uses the same fractional-Gaussian multiplier source and the same fresh binary-secret/integer-error wrapper as the supplied A-FRAC theorem. It does not change either endpoint to make decoding easier.

Binary injectivity implies D>=2^n by counting. In A-FRAC, p_t=(1+D_t(0))/2>=1/2, so D p_t^n>=D/2^n>=1 and its beta=min(1,D p_t^n) is exactly one in this regime. Therefore the new lower bound does not conflict with the older finite-index guessing upper bound: that upper bound is trivial on binary-injective ideals. This observation also limits the new theorem's reach. It does not address the smaller-index collision regime in which that beta bound can be useful.

The prior continuous-mask test exposed (a,Y,H) and obtained residue leakage through an exact integer-support constraint. That prior result alone did not establish public recovery. The present proof supplies a different bridge: recover the relevant integral products from public residues under the large-q event, then use ideal membership to separate the actual secret. It does not assume a continuous mask or independent integer completion noise, and it does not inherit a claimed success probability from the exposed-variable model.

## Algorithmic and hardness boundaries

The recovery decoder may enumerate all 2^n binary secrets and use an existentially selected short basis of J. Finding that basis is not claimed efficient or included in a public reduction. In the hidden-J experiment, equality of the full posterior gives an information-theoretic maximum-likelihood rule independent of J; it does not give an efficient way to evaluate that likelihood or find the useful basis. Randomized decoding cannot improve over the posterior maximum, so the finite deterministic rule is enough for the information-theoretic statement.

Exact unbounded lattice Gaussian sampling is part of the mathematical source law. No polynomial-time exact sampler for arbitrary inverse ideals is constructed. No implementation distance, source-to-standard reduction, quantum procedure or average-case ideal-family hardness assumption is introduced by this theorem. The elementary Poisson and ideal arguments import no computational theorem.

The result can rule out a proposed information-theoretic planted-lossiness upper bound smaller than its explicit lower bound in this exact regime. It cannot by itself rule out computational planted lossiness, prove source distinguishability, separate planted and comparator optimal guessing, supply binary-RLWE hardness, or transfer a standard uniform-secret theorem by renaming its distributions. The finite comparator controls sometimes also have high optimal recovery; that is consistent with the theorem's deliberately one-sided scope.

## Finite-control scope and resource record

G-PI-FV1 is a finite uniform-coset source with product-weighted integer errors. It is not a truncated Gaussian claimed to approximate the full source, and no full-Gaussian eps_s or tail bound was applied to it. It checks actual public decoding, denominator-event accounting, both fully enumerated wrapper endpoints, the complete hidden-J posterior, and the mandatory CP1 rejection. Detailed original evidence is in the adjacent JSON and resource report.

The pre-execution input's phrase “per-atom masses <=5 bits” describes the wrapper-law weights. For clarity, CP1 has a separate largest unnormalized prior atom weight 1758, requiring 11 bits, and a prior total denominator 70400, requiring 17 bits. This bookkeeping clarification does not change any input, executed code, output, probability calculation or resource bound. All calculations used arbitrary-precision integers.

No mathematical repair or re-execution is requested. Remaining blind, structural and final-artifact gates are separate. The broad standard-hardness objective is unchanged and remains unresolved.
