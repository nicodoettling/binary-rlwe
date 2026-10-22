# BLIND-RESOURCE4: statement-only referee report

## Frozen scope and verdict

This is a fresh statement-only, correlated same-model review, not a formal proof-assistant certificate or independent statistical confirmation. The complete assignment is preserved in `assignment-verbatim.txt`. The original six mathematical inputs, their exact SHA256 digests, and exposure times are preserved in `allowed-read-manifest-v1.json` and `reviewer-input-hashes-v1.json`. The only additional mathematical input is the requested statement-only TWOEVENT dependency, authorized by `allowed-read-addendum-v1.json`. The reading chronology and methodology digests are in `exposure-chronology-v1.json`. No author proof, author status, prior referee report, project claim summary, existing experiment checker, or other mathematical file was read.

The targets are exactly:

* `compact-selector-statement-v3.md`, SHA256 `eecebca3d1d23bb1cd88c577d90b66cc42e8f14254098356aedd9cdf285e26e1`.
* `energy-rank-kernel-statement-v2.md`, SHA256 `a8c7daf894df5d0d5ac8ac5fa8132fcbad884ab5020baac7500d820169c95556`.

**Local verdict: the exact finite claims and the stated conditional mathematical conclusions pass this review.** The computational conclusions pass with their stated expected-time and numerical-size qualifications. Neither target establishes a scalable family of full binary-secret modulus-transfer kernels. No general asymptotic existence claim is accepted here. The additional TWOEVENT Gaussian-instantiation paragraph is not needed for the two conditional targets and is not imported or certified by this report.

The following conventions are used explicitly: n is a positive integer; moduli/alphabet sizes are positive integers; each stated Markov kernel is a probability kernel; all randomized draws called independent, and successive rejection proposals, use fresh random tapes. The input-dependent class and weights may depend on the complete observed input, but not on the hidden secret except through that input. The pair version of ENERGY inherits the hypothesis of uniform conditional rank inside each joint shell from the words “the same statement.” Mapping class masses without that hypothesis is insufficient.

The review certifies distributions of the stated output sample pairs, jointly with their one shared secret. It does not append arbitrary internal rejection traces or random-bit consumption to the output theorem. Retry counts themselves are ancillary in the exact selector sampler, as proved below.

## Dependency graph

Statuses below are local to this frozen packet and this review. They do not replace the coordinator's reconciliation with project regressions or certification of a later edited artifact.

| ID | Claim and hypotheses | Dependencies | Local status | Evidence |
|---|---|---|---|---|
| C1 | Target two-residual coordinate map is bijective for every oriented cube edge | Ring relation and unit edge difference | ACCEPTED | Section 1 |
| C2 | Formula K is row normalized under nonnegative g and pointwise N | C1 | ACCEPTED | Section 1; 81 exact finite rows |
| C3 | Rejection implementation has kernel K and geometric mean M, on every input and posterior history | C2; fresh trials; M bounds G | ACCEPTED | Section 2; 500 finite posterior cases |
| C4 | All secret endpoints imply the full shared-secret batch law | C2; conditional iid input samples; fresh implementation tapes | ACCEPTED | Section 3 |
| C5 | Outer cap has pointwise TV at most exp(-L/M), batch error at most k times this plus charged sampler errors | C3; coupling | ACCEPTED | Sections 2–3 |
| C6 | The supplied n=2 H and selector satisfy all stated finite equations and max G | Exact supplied rational tables | ACCEPTED | Section 4; independent exact reconstruction |
| C7 | Stated sampler costs and cube-edge fair-bit bounds | Numerical M and explicit efficiency assumptions | ACCEPTED WITH STATED SCOPE | Section 5 |
| E1 | Rank formula maps uniform source-shell rank to uniform target-shell rank | Uniform source rank; independent uniform T | ACCEPTED | Section 6; 512 exact rank cases |
| E2 | ENERGY uniform and noise endpoints; rank permutation invariance | E1; h maps both shell laws; shell-constant input laws | ACCEPTED | Section 6 |
| E3 | Pair rank extension | E1–E2 with joint shell-constant laws and product shell sizes | ACCEPTED | Section 7 |
| E4 | Polynomial DP/bit/expected rational-sampling claims | Polynomial numerical alphabet widths and magnitudes; polynomial rational table encoding | ACCEPTED WITH STATED SCOPE | Section 8 |
| E5 | Wrapped versus finite Gaussian errors and their negligibility in the stated regime | TV contraction, scalar tail bound | ACCEPTED | Section 9 |
| E6 | Conditional construction from TWOEVENT | Its two likelihood inequalities; union of source shells | ACCEPTED | Section 10; 179 rational finite cases |
| X1 | A scalable full binary-secret family follows from the finite witness or ENERGY alone | No such premises supplied | NOT ASSERTED / NOT CERTIFIED | Scope of both targets |

## 1. Selector coordinate map and normalization

Put m_E=|E|=n 2^(n-1). For an oriented edge e=(u,v), let delta=v-u=X^i. In R_m, X^n=-1, so X is a unit with inverse -X^(n-1); every X^i is therefore a unit. This holds in both source and target rings, without a primality assumption on the modulus.

For target residuals z_u=d-cu and z_v=d-cv, subtraction gives z_u-z_v=c delta. Thus

    c=(z_u-z_v) delta^(-1),   d=z_u+cu.

This is the unique inverse. Consequently the map (c,d) to (z_u,z_v) is a bijection of R_q squared. For each fixed input x, edge e, and variant (j,k),

    sum_y H_j(r_u,z_u(y)) H_k(r_v,z_v(y)) = 1.

The equality follows by summing independently over all two target residuals, not by assuming anything about source residual independence. It remains valid for arbitrary correlated coefficient laws inside each ring kernel. Nonnegativity of K follows from that of g and H. Summing the displayed K over y gives

    sum_y K(x,y) = (1/m_E) sum_e sum_(j,k) g(c_e(x),j,k)
                 = (1/m_E) sum_e G(c_e(x)) = 1.

The last equality is the pointwise condition N. In particular, max G over classes occurring at a given x is at least 1; hence a valid global upper bound M satisfies M>=1. Classes with G=0 are never accepted and need no definition of g/G on an executed branch.

## 2. Exact retry law, posterior conditioning, and the cap

Fix an arbitrary input x. One trial chooses e uniformly and accepts with probability G(c_e(x))/M. Its success probability is exactly

    a_x=(1/(m_E M)) sum_e G(c_e(x))=1/M=:a.

The accepted edge distribution is G(c_e(x))/m_E. Conditional on an accepted edge, choosing (j,k) with g/G cancels G, so the accepted edge/variant probability is g(c_e(x),j,k)/m_E. Applying the independent H rows and the inverse coordinate map gives exactly K(x,y).

Let tau be the accepted trial index. For all t>=1,

    Pr[tau=t,Y=y | X=x] = (1-a)^(t-1) a K(x,y).

This proves geometric mean E[tau|x]=1/a=M and, more strongly, independence of tau from (X,Y) under every input prior. The number of trials therefore does not update the secret posterior. This does not claim that the complete rejected-edge trace is independent of X.

Here is the conditional-law audit. Let F_(t-1) include any observed history of the first t-1 rejected trials and any earlier processed samples. On a positive-probability surviving branch, write mu_h(x)=Pr[X=x|F_(t-1)=h]. That posterior may have lost support. Fresh proposals nevertheless give

    Pr[success at t | F_(t-1)=h] = sum_x mu_h(x)/M = 1/M.

The same equality holds after also fixing a secret value with positive posterior mass. Conditional on X=x and any previous rejected history, the successful current-trial output is still K(x,.). Bayes' normalizer for conditioning on current success is the constant 1/M; it introduces no extra x-dependent factor. This is the needed invariant after support restriction. The proof does not multiply marginal success estimates.

For example, with two inputs, two proposed edges, M=2, and weight vectors G_0=(2,0), G_1=(0,2), rejecting a publicly exposed proposal of edge 0 identifies X=1. Thus a proof treating rejected traces as harmless would be wrong. The next trial still succeeds with probability 1/2, because this is pointwise true for both inputs. This is exactly the distinction used above.

Couple the uncapped and L-trial algorithms using the same random tape until trial L. They agree unless tau>L. Thus, for every x,

    TV(K_L(x,.),K(x,.)) <= Pr[tau>L|x]
                         = (1-1/M)^L <= exp(-L/M).

Any fixed fallback is allowed. The formula also covers L=0 by the direct event interpretation. When M=1, every first trial succeeds. This is a bound on outer trials and output variation, not automatically a worst-case bound on all bit-level subroutines.

## 3. Full shared-secret law and approximate batch error

Let S have any prior pi on binary secrets, and conditionally on S=s let X_1,...,X_k be independent with law P_s. Apply K with independent fresh random tapes. For every s and output tuple (y_1,...,y_k),

    Pr[S=s,Y_1=y_1,...,Y_k=y_k]
      = pi(s) product_i [sum_(x_i) P_s(x_i) K(x_i,y_i)]
      = pi(s) product_i T_s(y_i).

This is the full joint law, including the single secret shared across all samples. Taking pi uniform gives the requested experiment. It is stronger than matching each sample after averaging the secret. The product factorization is justified by conditional independence given S, not by separate marginal endpoint identities.

After any positive-mass output history h=(y_1,...,y_t), the secret posterior is

    pi_h(s) = pi(s) product_(i<=t) T_s(y_i)
              / sum_(s') pi(s') product_(i<=t) T_(s')(y_i).

The next output has conditional law sum_s pi_h(s) T_s. Under the exact retry sampler, observing its trial counts adds independent geometric factors that cancel from this posterior. This equality reconstructs the adaptive posterior law rather than supposing that the secret remains uniform after observing samples.

The definition of T_s ensures that its public multiplier is uniform, its full error vector has law nu_q, and those are independent. The joint formula ensures independence across samples conditional on the same S. It does not impose coefficient independence on a general nu_q. For the comparator, iid U inputs map to iid V outputs by the same calculation.

A minimal hand-checked finite regression is S uniform on {0,1} and Y_1=Y_2=S. Each output marginal is uniform, but the joint law has mass 1/2 each on (0,0) and (1,1). Thus equality of secret-averaged one-sample laws would not justify the tensor conclusion. The proof above instead verifies the endpoint separately for each fixed s and factors only conditional on that same s.

For capped or approximate kernels, couple each row separately and apply a union bound, including S in the coupling. The resulting joint TV bound is at most k exp(-L/M), plus the sum of the explicitly charged implementation errors. No product of marginal failure probabilities is used. For example, if each of at most L acceptance coins differs by at most delta_a under a conditional coupling, the final variant choice differs by at most delta_v, and the two sampled H rows differ by at most delta_H1 and delta_H2, a valid additional per-sample charge is L delta_a+delta_v+delta_H1+delta_H2. Other approximate subroutines must be charged as well; no universal zero cost is inferred from the phrase “efficient.”

## 4. Exact finite n=2 certificate

The independent checker `exact-audit-v1.py` was written from the allowed statement and tables. It does not import an author checker. All arithmetic relevant to acceptance is `fractions.Fraction` arithmetic. It reconstructs multiplication as

    (a0,a1)*(s0,s1) = (a0*s0-a1*s1, a0*s1+a1*s0) modulo m.

Source vectors are all nine tuples in {0,1,2}^2; target vectors and secrets are all four tuples in {0,1}^2, in ascending lexicographic order. All 81 source pairs and 16 target pairs are enumerated. The four positively oriented edges are generated directly from the binary cube.

For a quick independent check of the radial data, let D=43680 and h_j(z,f) denote a table numerator. The target zero-count class sizes are (1,2,1); the source class sizes are (4,4,1). The four supplied tables obey, for every appropriate j,z,f,

    h_j(z,0)+2h_j(z,1)+h_j(z,2)=D,
    4h_j(0,f)+4h_j(1,f)+h_j(2,f)=9D/4,
    h_j(0,f)+14h_j(1,f)+49h_j(2,f)=D*(4,12,36)_f.

These are respectively row normalization, the uniform endpoint, and the noise endpoint. The source noise shell masses are (1,14,49)/64 and the target noise probabilities per atom of zero count f are (1,3,9)_f/16. No Gaussian law is substituted for these rational laws.

The exact reconstruction verified:

* 36 radial row sums, 16 radial uniform equations, and 16 radial noise equations;
* all 33 supplied selector weights strictly positive, with all unspecified weights zero;
* sum_e G(c_e(x))=4 for each of the 81 individual source inputs;
* nonnegativity and exact row sum 1 for all 81 rows of K;
* all 16 equations P_s K=T_s for each of the four binary secrets;
* all 16 equations UK=V, with target entries exactly 1/16;
* the exact stated maximum G, attained at class (0,0,0), and its strict inequality G<3.

The target secret endpoint entries are exactly the appropriate residual permutation of (9,3,3,1)/64 for every fixed public target multiplier. Full endpoint vectors are preserved in `exact-audit-results-v1.json`; the entire independently reconstructed rational matrix is preserved in `exact-kernel-v1.json`.

The maximum is

    31747846170836756094431065767102005668874369915000841877198843
    /11688058834193179864192788149647847121368047468795377899320297.

Consequently M=3 is valid and the uncapped finite sampler has mean exactly three edge trials. The supplied n=2 statements are finite exact facts, not numerical feasibility tolerances.

Individual H endpoints are insufficient for an input-dependent selector. A concrete regression has n=1,Q=q=2 and uniform source and target noise. Let H_0 be identity and H_1 bit flip; both preserve uniform. There is one edge (0,1). For input (a,b), set r_0=b,r_1=b-a, choose variant (r_0,r_1) with weight 1, and apply the corresponding H rows. Both residual outputs are zero, hence the final pair is always (0,0). N holds and M=1, but UK is a point mass rather than V. Thus the warning in COMPACT is necessary, and the separately checked four secret equations cannot be dropped.

## 5. Selector resource audit

A uniform oriented cube edge is generated by drawing i uniformly from {0,...,n-1}, setting u_i=0, and drawing the other n-1 bits uniformly. For n>=2, sample i by repeated ceil(log2 n)-bit proposals below n. Each proposal is accepted with probability greater than 1/2, so fewer than 2 ceil(log2 n) fair bits are needed in expectation for i. Total expected bits are O(n). For n a power of two, i uses exactly log2 n bits, giving a worst-case n-1+log2 n fair-bit bound. For n=1 the edge is deterministic.

There are (n+1)^3 nominal zero-count classes, although some may be unreachable. Computing a class from an explicit edge and input requires only polynomially many ring operations. Summing and sampling a supplied polynomial-sized rational table is polynomial in its total encoding length; exact uniform-integer rejection sampling uses expected polynomially many fair bits. Rational multiplication and comparison must charge numerator/denominator bit lengths, including those of M.

If the expected cost of a trial and all final subroutines is uniformly polynomial in the specified input sizes, multiplying the trial cost by the exact mean M gives the claimed polynomial dependence on the **numeric value** M as well as encoding lengths. This is not a polynomial-in-log M conclusion. A supplied M can be exponentially large, and a pointwise normalization alone does not guarantee a useful polynomial rejection bound. For example, for a general class that names the edge, assigning weight |E| to one distinguished edge and zero to all others satisfies N while max G=|E|.

To make the outer failure at most eta/k one may take L>=M log(k/eta), rounded up. Polynomial total runtime requires control of that numeric M and of the invoked samplers. An outer cap alone does not turn an unbounded fair-bit rational sampler, a non-power-of-two exact edge sampler, or an arbitrary expected-time H sampler into a worst-case bounded-time procedure. The target does not claim otherwise. Additional bit/runtime caps introduce additional approximation error that must be explicitly charged.

The finite rational tables have fixed finite encoding length. Their existence at n=2 does not supply uniform table generators, polynomial M, polynomial table size, endpoint error bounds, or any asymptotic Gaussian replacement.

## 6. Energy-rank theorem

Fix nonempty source and target shells of sizes m=M_e and t=N_f. Conditional on a source-shell-constant input law and on E=e, its rank r is uniform on {0,...,m-1}. The choice of f depends only on e, so conditioning additionally on f preserves uniform r. T is independent and uniform on {0,...,t-1}.

The map

    (r,T) -> t*r+T

is a bijection onto {0,...,m*t-1}. For each j in {0,...,t-1}, exactly the m consecutive integers jm,...,(j+1)m-1 satisfy floor((t*r+T)/m)=j. Therefore the rank formula gives a uniform target-shell rank. It is normalized on every fixed source input as well: 0<=t*r+T<=mt-1 implies 0<=j<t, and T is a probability distribution.

For a source law with shell masses w_e and uniform ranks inside its shells, the output probability of a target vector y in shell f is

    [sum_e w_e h(e,f)] / N_f.

Taking w=alpha and using alpha h=beta gives 1/q^n for every y. Taking w=p and using p h=n gives n_f/N_f=N(y). This proves both endpoints exactly. Zero-mass source shells cause no conditioning obligation, and all enumerated energy shells have positive cardinality.

A fixed permutation of source ranks preserves the uniform source rank in every shell. The same counting proof applies, including reversal. The construction uses the full rank of a fixed input in general: for m=t=2 it is j=r, so two inputs in the same energy shell can give different output laws. “Retains the full rank” should be read as dependence on that rank, not a universal assertion that the output reveals an invertible copy of it. Cases such as N_f=1 obviously discard rank information.

This argument does not survive arbitrary conditioning that destroys uniformity within a shell, nor does it claim to. For m=t=2 and deterministic h, conditioning the source to rank 0 makes the output rank 0. This elementary regression prevents replacing the shell-uniform premise by equality of shell probabilities alone.

If an approximate sampler changes h(e,.) by TV at most epsilon, then, for fixed x, the exact rank stage is a Markov postprocessing of the sampled f. TV contracts, so the resulting output row changes by at most epsilon. Indeed the target shells for different f are disjoint, so with the same conditional rank stage the two variations are equal. The ideal uniform endpoint remains exact; an approximate implemented h incurs its declared error at that endpoint as well.

## 7. Pair extension and its necessary inherited premise

For a fixed pair of source shells, the Cartesian shell has size M_e0*M_e1. Ascending lexicographic order on the ordered pair has rank

    r=r0*M_e1+r1.

The corresponding target pair shell has size N_f0*N_f1 and target rank j=j0*N_f1+j1. Apply the preceding counting argument with these two product sizes, then use integer quotient and remainder to recover j0,j1. Every endpoint law constant on each joint shell is uniform inside that joint shell, so the same proof applies with joint class masses. A table mapping those joint masses is sufficient under this inherited premise.

Separate uniformity of each component's rank is not enough. For two ranks in {0,1}, the law giving probability 1/2 each to (0,0) and (1,1) has uniform marginal ranks but is not uniform on the four-element joint shell. A rank map with equal source and target product sizes is the identity and preserves this correlation, rather than producing independent uniform target ranks. Thus a pair-residual application must establish the full joint-shell premise or directly verify its endpoints. The statement's final warning that one or two residual endpoints do not establish the full cube endpoint is correct.

## 8. Energy dynamic programming and sampling costs

Let A be the largest absolute alphabet entry. For a source alphabet I, define integer suffix counts

    D_0(0)=1;  D_0(t)=0 for t!=0;
    D_l(t)=sum_(a in I) D_(l-1)(t-a^2),

with out-of-range entries interpreted as zero. Only l<=n and 0<=t<=n A^2 are needed. With Q and A polynomial in n numerically, there are polynomially many states and summands. Every count is at most Q^n, so its binary length is at most n log2 Q+1. The same argument applies to target counts with q.

To rank x in its shell, scan positions in order. At position i, for each alphabet value smaller than x_i, add the corresponding remaining suffix count at the remaining energy. Then follow the actual prefix. To unrank, choose the first alphabet value whose count block contains the desired rank, subtract earlier blocks, and recurse. These procedures use polynomially many additions, comparisons, and table accesses on O(n log(max(Q,q))) bit integers. Squaring alphabet entries and evaluating the energies also have polynomial bit cost under the stated numeric bounds.

The pair shell product is at most max(Q,q)^(2n), hence at most 2n log2(max(Q,q))+1 bits; it is not covered by the single-shell n-factor bound. Intermediate numerators in the rank formula can be products of source and target shell sizes, but still have O(n log(max(Q,q))) bits, with the appropriate larger constant. No claim that every intermediate integer has the single-count bound is needed.

For a polynomial-sized rational h row with polynomial numerator/denominator encodings, place its entries over a common denominator, for example the product of the denominators. The common denominator's bit length is at most the sum of the entry denominator bit lengths and is polynomial. Draw an exact uniform integer below it by fair-bit rejection and use cumulative integer weights. Expected sampling time is polynomial; a fixed worst-case number of fair bits is generally impossible for a non-dyadic probability. Sampling T below a shell count works the same way, with O(n log(max(Q,q))) expected bits. Arbitrary real h values do not receive a finite exact sampling implementation from this argument.

For a finite centered independent coefficient Gaussian, the vector probability is a fixed normalizer times exp(-pi E(x)/sigma^2); therefore it is constant on each energy shell. This verifies the stated example directly. The theorem does not need coefficient independence for any other law that is already shell-constant.

## 9. Wrapped/truncated Gaussian comparison and tail estimate

Let Z have the integer discrete Gaussian and let I_m be the fixed centered representative interval. Write t=Pr[Z outside I_m]. The law of Z conditioned on I_m differs from the original integer law in TV exactly t. Reducing both modulo m is deterministic postprocessing, so the wrapped law differs from the centered truncated-and-renormalized residue law by at most t. Taking n independent copies gives at most 1-(1-t)^n<=nt. This argument respects normalization; it does not equate wrapped and conditioned probabilities.

Let P_w,P_f be wrapped and finite source noise laws and N_w,N_f the corresponding targets. If P_f H=N_f, Markov contraction and the triangle inequality give

    TV(P_w H,N_w) <= TV(P_w,P_f)+TV(N_f,N_w)
                    <= n*t_Q+n*t_q.

An implemented kernel with a uniform per-row error delta adds at most delta. The uniform endpoint remains exact for the ideal H because the representative intervals identify bijectively with residue classes. No comparison of moments is used.

A finite normalization regression takes masses (1-t,t) on two points and retains only the first point. Conditioning produces (1,0), at exact TV distance t; n independent coordinates give distance 1-(1-t)^n from the all-retained point. This verifies the normalization and product-loss formulas in their smallest finite setting. It is a hand calculation, not an additional computer invocation.

For completeness, an elementary tail bound avoids an imported unverified theorem. Every excluded integer has magnitude at least m/2. Since the Gaussian normalizer is at least 1,

    t <= 2 sum_(k>=0) exp(-pi*(m/2+k)^2/sigma^2)
      <= 2 exp(-pi*m^2/(4*sigma^2)) /(1-exp(-pi*m/sigma^2))
      <= 2*(1+sigma^2/(pi*m))*exp(-pi*m^2/(4*sigma^2)).

The last inequality follows from e^a-1>=a. This bound handles the asymmetric even-modulus interval as well as odd moduli; overcounting the two tails is harmless. If m/sigma>=c n for a fixed c>0 and the stated widths have polynomial numerical size, its prefactor times n is polynomial while its exponential is at most exp(-pi c^2 n^2/4). This is negligible in n. Applying it separately at Q,sigmaQ and q,sigma0 proves the displayed regime's assertion.

## 10. Requested TWOEVENT dependency

The original packet referred to FF3-TWOEVENT without defining its two inequalities. This was an intake dependency gap, not a discovered counterexample. The reviewer requested the exact statement before reading more, and the root supplied it through the manifest addendum. Its SHA256 is `ba5c8050af98cce9e7dec3d9c1b9a1806f606f9b59f1ca40e62917aa093e913b`.

Use only its general finite-set construction here. First consider 0<u<p<=1. Its two likelihood bounds make every numerator of g1 and g0 nonnegative. Their sums are respectively ((1-u)-(1-p))/(p-u)=1 and (p-u)/(p-u)=1. Direct algebra gives

    p*g1+(1-p)*g0=N,     u*g1+(1-u)*g0=V.

These are complete probability-law identities. If C is a union of source energy classes, each class is assigned one row type. Because N and V are constant on target shells, aggregate those rows over a target shell to obtain

    h1(f)=((1-u)*n_f-(1-p)*beta_f)/(p-u),
    h0(f)=(p*beta_f-u*n_f)/(p-u).

This is a Markov table mapping p to n and alpha to beta. Consequently the ENERGY theorem applies. The likelihood bounds are assumptions; this proof does not show that they hold in every parameter family. With real Gaussian probabilities the table is an exact mathematical object, not automatically an exactly computable finite sampler.

There is a small import-scope mismatch that must not be hidden: ENERGY's last paragraph mentions C and the two inequalities, whereas the supplied TWOEVENT theorem separately assumes u<p and strict positivity of N. The existence conclusion remains true under the literal weaker ENERGY wording. For the two displayed fractions to be defined, 0<u<1. Since the V-average of L is 1, their upper bound implies 1<=p/u, hence p>=u. If p=u, every L(y)<=1 and its mean is 1, so L is identically 1 and N=V. In that case take the constant Markov table h(e,f)=beta_f; it maps both normalized source shell laws to beta=n. This avoids the undefined denominator p-u. If p>u, the aggregate formulas above do not require strict positivity of N: their numerators remain nonnegative by the given inequalities. A zero target mass is compatible only with p=1, and the same algebra applies. Thus the broader conclusion is proved by a direct extension and a uniform-target boundary case; it is not licensed by blindly importing the narrower TWOEVENT theorem.

Two exact boundary witnesses make this explicit. With u=p=1/2 and N=V=(1/2,1/2), the constant h row (1/2,1/2) works although the displayed g formulas have a zero denominator. With u=1/2,p=1,N=(1,0),V=(1/2,1/2), the likelihood vector is (2,0), both inequalities hold, and g1=(1,0),g0=(0,1) give a valid table although N is not strictly positive. These are hand-checked finite rational cases, not additional unregistered computer experiments. Cases u=0 or u=1 do not satisfy a pair of defined rational inequalities as written; an application using such a C must specify its separate boundary convention.

The supplied dependency's finite rejection formulas also check directly. The g1 acceptance probability is (p-u)/(1-u), and the g0 acceptance probability is (p-u)/p. If p>=3/4 and u<=1/4, both are at least 2/3. Fresh attempts have geometric failure at most (1/3)^ell. These calculations are pointwise for each row type; proposal and numerical approximation costs remain separate. The optional subsequent Gaussian parameter-existence claim is outside the required dependency for these two targets and receives no verdict here.

## 11. Falsification protocol, CP-1, and preserved findings

The deterministic experiment was preregistered before execution in `experiment-preregistration-v1.json`, with script SHA256 `3cd527f76b36a71cc08e24ac82ccae076bb7f1d18ef2d6c3af714b48f4f5c8a0`. The root explicitly granted the LIGHT slot. The single invocation enforced a 120-second timeout and 512 MiB address-space limit; no retries occurred. It exited 0 in 0.152 seconds by the harness clock with peak RSS 17,408 KiB. Full stdout, stderr, external timing/RSS, and exact command/exit metadata are preserved as `experiment-v1.stdout`, `experiment-v1.stderr`, `experiment-v1.time`, and `experiment-v1.exit.json`.

Besides the complete finite table verification, it checked 512 rank cases (M,N from 1 through 16, each with identity and reversal), 500 exact retry/posterior cases (25 two-input weight models, five rational priors, four trial positions), and 179 feasible finite TWOEVENT models. All passed. These bounded searches are evidence, not substitutes for the general proofs above. The endpoint-warning counterexample and CP-1 deliberately reject tempting stronger claims.

For CP-1, before conditioning the trace masses sum to 1 and Pr[vk=1]=10/11. The posterior masses are A_b=21/2000, C_b=1/20, and D=879/1000. Thus p(x)=1/10, p(e_b)=121/2000, and p(f_b)=21/2000, all nonheavy under the strict threshold gamma=1/10. The two-hit event has probability 21/2000>1/100=gamma^2, while the later incidence is 21/221<gamma. The false marginal-product claim is rejected. Its failure arises from support restriction and posterior renormalization, not merely correlation of fresh oracle values.

The current selector proof survives this regression because its next-trial probability is exactly 1/M for every fixed x and remains so after an arbitrary posterior support restriction. The batch theorem factors only after conditioning on the one shared secret and establishing fresh independent tapes. ENERGY explicitly conditions on uniform ranks inside a shell and does not assert that arbitrary adaptive rank restrictions preserve uniformity. No latent cache-hit status is introduced in any filtration here.

Preserved finding log:

| Finding | Classification | Disposition |
|---|---|---|
| Original packet omitted the TWOEVENT definition | Missing dependency at intake | Resolved by requested authorized statement-only addendum; no earlier conclusion relied on a guessed definition |
| ENERGY mentions two likelihood inequalities, while the named TWOEVENT result also assumes u<p and N>0 | Nonblocking import-scope mismatch | Direct proof extends the formulas to zero target masses when p>u, and uses a constant table in the necessary uniform-target case p=u; exact boundary witnesses preserved |
| Individual H endpoints plus N do not imply selector endpoints | False stronger claim, already excluded by COMPACT | Explicit n=1 exact counterexample preserved; all actual finite endpoint equations checked |
| Marginal sequential bounds do not imply a product bound | False stronger claim | CP-1 reproduced and rejected; pointwise retry invariant used instead |
| Joint shell masses without joint-shell uniformity do not imply the pair endpoint | False stronger claim, excluded by inherited ENERGY premise | Explicit correlated-rank witness preserved; application must check inherited premise |
| Outer rejection cap does not itself bound all fair-bit runtime | Resource limitation, not a false stated conclusion | Expected-time and finite-output-error claims kept separate from worst-case runtime |
| Polynomial numeric-M cost is not polynomial bit-input cost | Resource limitation, expressly acknowledged by COMPACT | No scalability inferred |
| “Retains the full rank” can be mistaken for invertible information retention | Wording clarification | Interpreted as general rank dependence; degenerate target shells need not retain information |
| Finite n=2 witness or ENERGY table implies a scalable full-cube family | Unsupported stronger claim, explicitly disclaimed | Not certified |

No false literal main theorem conclusion was found under the stated and explicitly inherited hypotheses. No target was edited during this review. All defects of stronger statements and all scope qualifications above remain in the record rather than being erased by a repair.

## 12. Certification boundary and reproducibility

The mathematical proofs above establish the two frozen conditional targets, and the exact independently reconstructed finite matrix establishes the supplied n=2 instance. The first and only checker invocation started from the supplied immutable rational data and an independent implementation, without using a previously generated kernel or author output. Input hashes matched before computation.

The experiment's exact command is in `experiment-v1.exit.json`. Reproduction requires only Python's standard library and the six initial packet files; no network, installation, solver, service, detached process, or repository change is needed. Reproduction should retain the same resource limits. A final seal records the immutable report, script, inputs, and evidence hashes.

This review supplies local mathematical acceptance, not a new asymptotic theorem, not a formal proof-assistant certificate, and not a certificate for unspecified metadata leakage, arbitrary posterior-conditioned rank inputs, or worst-case bit runtime. Root-level certification still must compare the current artifacts with any broader project dependencies and historical regressions that were intentionally withheld to preserve this blind review.
