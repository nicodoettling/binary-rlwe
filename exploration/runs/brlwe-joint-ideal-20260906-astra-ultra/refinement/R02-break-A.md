# R02 — bounded attack audit of A2's exact correlated source

Completed bounded audit on 2026-09-06, before the 15:40 UTC deadline. No experiments or child workers. New deductions are provisional pending nonauthor review. This audit tests the specified A2 parameter refinement, not another source family.

**Disposition:** no polynomial attack was obtained by the two bounded attempts. The grouped-orbit method supplies a material exp(O_c(sqrt(n)/ell^4)) attack with the imported solver's success probability explicitly retained. The exact correlated source suppresses fixed additive-character tests, but is statistically far from uniform and has no matching independently justified computational reduction. Defer its source-hardness assertion; absence of a successful attack supplies no hardness evidence.

## Exact experiment and inputs read

Let n be a sufficiently large power of two, ell=ceil(log2 n), d=floor(sqrt(n)/ell^4)>=ceil((ln n)^2), b=ell^2, tau=ell, and sigma=2n ell^3. Let q be a fully split prime with sigma n^c<=q<=n^K for fixed c,K>0. The coordinator's [prime-regime note](../development/coordinator-prime-regime.md) supplies a conservative nonempty family by choosing q=1 mod 2n^h, fixed integer h>1+c; no narrow-interval prime claim is needed here.

Draw T uniformly among ALL d-subsets of the n roots of X^n+1 over F_q. Put J={r:r vanishes on T} and I=Ann(J), supported on T. Draw U with independent uniform nonzero active coordinates and V independently uniform I conditional on T. Draw F with independent D_ell coefficients each conditioned on [-b,b], independently of T,U,V. For its negacyclic multiplication matrix M_F, put B_F=sigma^2 I_n-ell^2 M_F M_F^T. In fixed coefficient order, compute B_F=L diag(v_i)L^T with unit-lower-triangular L. Sequentially set c_i=sum_(j<i)L_ij y_j, draw h_i in Z with probability proportional to exp(-pi(h_i-c_i)^2/v_i), and put y_i=h_i-c_i. Return H_seq=(h_i) and publish

    (A,C)=(U+F,V+H_seq) modulo q.

There is no binary secret input. G~D_ell^n is a separate later independent bridge draw. The exact comparison is with two independent uniform ring elements. Every PPT approximation is a separately charged distance from this canonical sequential law. In particular the present audit does not silently replace H_seq by D_(B_F).

Read: [known-counterexamples.md](../known-counterexamples.md), [D01 theorem v1](../development/D01-theorem-v1.md), [F02's exact sampler](../foundations/F02-completion.md), [D02 correlation audit](../development/D02-A-correlation.md), and [F03's attack inventory](../foundations/F03-attacks.md). D01's extraction assertion applies to this smaller d if its proof passes review; it is not a source-hardness theorem. The active-unit law is exact, without a hidden conditioning reduction from uniform U.

## Attempt 1 — exploit the unique first-mask decomposition

The exact norm criterion from D02, q^(1-2d/n)>2b sqrt(n), holds eventually here. Thus F and then T are information-theoretically determined by A among the allowed decompositions. This is not a polynomial decoder. The concrete algorithm is the frozen subgroup-orbit super-support enumeration, using known-support ideal BDD only AFTER each public orbit choice. No claim that the support was initially public is permitted.

**Primary theorem recheck.** Boudgoust–Gachon–Pellet-Mary, *Some Easy Instances of Ideal-SVP and Implications on the Partial Vandermonde Knapsack Problem*, ePrint 2022/709, revision 2022-09-01, [primary PDF](https://eprint.iacr.org/2022/709.pdf): Definition 2.14 requires a known root set and canonical bound 2B_can<sqrt(n)q^(t/n). Theorem 3.1 applies to an integral ideal with no ramified prime factors, supplied ideal/field bases and automorphisms, and gamma>=2sqrt(n); its runtime is exp(O(n log(n)/(s log(gamma/sqrt(s)))))*poly(input), where s is the full stabilizer size. Corollary 4.2 reduces power-of-two ideal-HBDD to inverse-ideal Hermite-SVP when gamma_1>2gamma_4. Lemma 2.11's underlying lattice algorithm is probabilistic. These hypotheses and its success probability must survive the import.

Fix epsilon=c/4 and a constant C0>=max(2,4(1+c)/c). Choose r to be the least power of two >=C0 d. Eventually r<=n, so r divides n. A known subgroup of order h=n/r partitions the roots into r orbits. Enumerate their at-most-d-element subcollections B; at least one union contains T. Let Omega_B be the complement, t=|Omega_B|>=n(1-d/r), and let L_B be the known full integer ideal vanishing modulo q on Omega_B. On a correct branch, A mod L_B=F mod L_B.

The public integer ideal q L_B^(-1) is exactly the product of the complementary prime ideals above q. Thus it is integral, unramified, and stable under the subgroup. Its basis and the full cyclotomic automorphism list have polynomial-size descriptions. Scaling by q preserves the Hermite approximation factor. Canonical orthogonality gives ||can(F)||_2<=nb=:B_can. Therefore take

    gamma_1=sqrt(n)q^(t/n)/(nb),   gamma_4=gamma_1/4.

The frozen sufficient gap is

    q^(1-d/r)>=8 n^(1+epsilon)b.                             (R02.2)

It holds eventually at A2: (1+c)(1-1/C0)>=1+3c/4 leaves a positive n^(c/2) margin over the required exponent 1+c/4, with the remaining powers of ell harmless. In particular gamma_4>=2 n^epsilon sqrt(n), so all stated approximation and uniqueness requirements hold. Since the full stabilizer has size s>=h, the runtime exponent is at most O(r/epsilon): the function s log(gamma_4/sqrt(s)) increases for 1<=s<=n when gamma_4>=2sqrt(n). Enumerating the branches gives total runtime

    exp(O_c(d))*poly(n,log q)
       =exp(O_c(sqrt(n)/ell^4))*poly(n,log q).              (R02.3)

Run the promised decoder and verify a proposed F' by |F'_j|<=b and A=F' mod L_B. A uniform A passes any branch with probability at most (2b+1)^n/q^t, hence total false acceptance is at most

    p_false=2^r(2b+1)^n/q^(n(1-d/r))=exp(-Omega(n log n)).  (R02.4)

Let p_alg be the success probability of the imported solver on a correct promised branch under the chosen algorithm/repetition policy. Then the finite distinguishing advantage is at least p_alg-p_false. **Scope repair to F03:** the frozen statement's literal planted acceptance one holds conditional on successful ideal solving; a probabilistic implementation must retain p_alg or charge its failure. Standard amplification may be applied once its base success guarantee is fixed. This audit does not invent an exact success probability absent from the cited theorem statement.

The exponent and congruence verification survive the primary-source check. The algorithm is a concrete subexponential upper bound on A2's source security, using only A and unaffected by F/H correlation. It is not polynomial at d=floor(sqrt(n)/ell^4). Uniqueness does not remove the branch search: it says the correct solution is determined, not how to identify it. A direct noiseless sparse-Fourier recurrence would likewise be invalid here: coefficients of the unknown recurrence lie in F_q and can amplify the dense integer noise; a decoder for those noisy modular recurrences is an additional missing algorithm.

## Attempt 2 — additive characters of the actual correlated pair

For CRT characters chi_alpha(x)=exp(2pi i sum_i alpha_i x(r_i)/q), the exact public expectation is

    E[chi_alpha(A)chi_beta(C)]
      = E_T[1_(beta|T=0) product_(i in T)c(alpha_i)]
           * E_F[chi_alpha(F) E(chi_beta(H_seq)|F)],
    c(0)=1, c(t)=-1/(q-1) for t!=0.

The factorization is valid because F,H_seq are independent of T,U,V, while H_seq depends on F. Its inner conditional expectation must not be replaced by an independent H marginal. The proposed bounded test family is one fixed additive character, or a polynomial-l1 linear combination of fixed characters. Data-dependent character selection and arbitrary nonlinear functions of many characters are outside the proposed exclusion.

For a nonzero CRT character alpha with support size s, its coefficient-frequency vector w_j=sum_i alpha_i r_i^j has at least n-s zero CRT evaluations after inverse-root permutation. Indeed W(r_l^(-1))=n alpha_l modulo q, by summing the geometric progression of (r_i/r_l)^j. Taking centered integer representatives, the nonzero integer cyclotomic norm is divisible by q^(n-s), while its absolute value is at most ||w||_2^n. Thus

    ||w||_2>=q^(1-s/n),   dist(w/q,Z^n)>=q^(-s/n).          (R02.1)

Here the distance uses that w has already been centered coordinatewise. If s<=n/ln(q), the distance is at least exp(-1).

**Uniform Gaussian character estimate.** For a positive parameter matrix B>=lambda I, the integer Gaussian has the positive Poisson expression

    E_(H~D_B) exp(2pi i <v,H>)
      = sum_(k in Z^n) exp(-pi(k-v)^T B(k-v))
          / sum_(k in Z^n) exp(-pi k^T B k).

Let kappa(t)=2 sum_(j>=1)exp(-pi t j^2). Splitting the exponent in half and using that the scalar periodized Gaussian is maximized at integer centers gives

    |E exp(2pi i <v,H>)|
       <= exp(-pi lambda dist(v,Z^n)^2/2)
             (1+kappa(lambda/2))^n.                         (R02.5)

For completeness, the denominator is at least 1; every summand is bounded by exp(-pi lambda dist(v,Z^n)^2/2) times exp(-pi lambda||k-v||^2/2). The latter sum factors by coordinates, and its maximum at zero follows from its Poisson Fourier series with nonnegative coefficients. No unwrapped covariance identity is used.

For every admitted F, B_F>=3sigma^2 I/4. Let eta_seq be F02's UNIFORM TV upper bound between H_seq|F and D_(B_F), retaining all adaptive normalizers. Equation R02.5 and the character/TV inequality imply that any nonzero beta with support at most n/ln(q) satisfies, for every F,

    |E(chi_beta(H_seq)|F)|
      <= exp(-3pi sigma^2/(8e^2))
              (1+kappa(3sigma^2/8))^n+2eta_seq=:xi_H.        (R02.6)

Consequently |E_F[chi_alpha(F) E(chi_beta(H_seq)|F)]|<=xi_H for every alpha. This step retains the entire dependence on F; it does not factor the joint noise into independent marginals.

When beta=0 and alpha has nonzero support at most n/ln(q), apply R02.5 to B=ell^2 I. If eta_F denotes the TV between ideal iid D_ell and the exact truncated F law, then

    |E chi_alpha(F)|
      <= exp(-pi ell^2/(2e^2))(1+kappa(ell^2/2))^n
              +2eta_F=:xi_F,
    eta_F<=n exp(-pi ell^2)/(pi ell).                        (R02.7)

This comparison charges truncation and is not a source substitution.

**Large support.** If beta has support s>n/ln(q), its V-character vanishes unless T avoids that support. Hence the absolute public character is at most

    binom(n-s,d)/binom(n,d)<=exp(-ds/n)<=exp(-d/ln(q)).

If beta=0 and alpha has support s>n/ln(q), the active-unit factor has absolute expectation at most

    E_T[(q-1)^(-|T intersect supp(alpha)|)]
      <=(1-(1-1/(q-1))s/n)^d<=exp(-d/(2ln(q))).             (R02.8)

The middle inequality is the elementary symmetric mean bound for sampling d weights without replacement, with s weights 1/(q-1) and the rest 1. It follows by pairwise averaging the weights: for fixed sum x+y, each elementary symmetric sum increases when the product xy increases. This is a fixed uniform-subset calculation, with no selected-stage independence assumption.

Combining all cases gives, for EVERY nontrivial fixed pair character,

    |E chi_alpha(A)chi_beta(C)|
      <=xi:=max(xi_F,xi_H,exp(-d/(2ln(q)))).                 (R02.9)

At A2's exact d and polynomial q, xi is negligible: the last exponent has order at least sqrt(n)/(ln n)^5, xi_F is exp(-Omega((ln n)^2)), and xi_H is still smaller up to F02's negligible eta_seq. A source implementation at joint distance eta_impl changes the bound by at most 2eta_impl. Against the independent uniform pair, a normalized real-part character test has advantage at most xi/2, and a fixed linear combination with coefficient l1 norm P has expectation gap at most P xi. This closes this explicit attack attempt, pending review of R02.1–R02.9.

It does NOT bound every efficient test, data-dependent character selection, or arbitrary nonlinear combinations of character values. Indeed the first marginal is statistically far from uniform: its support has size at most binom(n,d)(q-1)^d(2b+1)^n, whose ratio to q^n is negligible. Many individually small Fourier coefficients can encode that statistical distinction. The character calculation is therefore not hardness evidence.

The exact sequential order is also retained in this conclusion. Its deviation from the ideal centered D_(B_F) kernel is uniformly at most eta_seq, hence any public test of an ordering artifact attributable solely to that deviation has acceptance change at most eta_seq after the source projection. A negligible implementation distance cannot create an inverse-polynomial public attack by itself. This comparison is only with the same F-conditioned anisotropic Gaussian, not with an independent isotropic second noise.

## Source-map boundary and final recommendation

The source generator can compute B_F and every adaptive center because it knows F. A source adversary or a reduction given only A=U+F does not receive F. The uniqueness statement does not supply that missing computation, and the successful decoder currently recorded still pays R02.3. Thus efficient evaluation of the hidden-coin source kernel is not an independently justified public source reduction.

The nearest independent-noise HLBDD source, its active-unit conditioning cost, the DSPR common-denominator correlations, and the exact public shear comparison were checked in [F03's primary-source ledger](../foundations/F03-source-ledger.md). None supplies this exact sequential F-conditioned law at these widths. [D02](../development/D02.md) proves a wrapped retained-variable obstruction for the tested independent iid public shears; its latent-distance consequence also applies to A2, because its bound is independent of d. That consequence does not distinguish the public pair and does not retire A2's completion.

**Retain:** the exact A2 source specification, its separately checked completion/extraction obligations pending their reviews, and the conditional one-sample bridge. **Defer:** computational hardness of this same source against two independent uniform ring elements. Record the subexponential attack as a security ceiling without converting its asymptotic O-constant into a concrete bit estimate. No stronger claim follows from the failed character test or from the lack of a polynomial decoder.

Review priorities for this note are the normalization in R02.1/R02.5, the uniform retained-F passage to H_seq in R02.6, the active-unit hypergeometric factor in R02.8, and the probabilistic-success correction to the grouped-orbit import. The two attempts are exhausted; no continuation is requested.
