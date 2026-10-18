# H-ALIGN companion v2: exact congruence laws and a max-atom extension

Status PROVISIONAL, separate from frozen theorem/proofv1. V2 changes only the forward reference to the scope-repaired relation companion; the coset statements and proofs are unchanged. No prior acceptance is inherited by this companion.

Let the ideals, widths and coefficient norms be as in H-ALIGNv1. Set K=FI and V=R/I. Since I is prime of norm M>N(F), I does not divide F. Thus F+I=R, F intersect I=FI, and reduction identifies F/FI with V, a field of M=p^f elements. This is an additive quotient as well as an R-module. For each a in V, choose any t_a in F reducing to a; ordinary ideal arithmetic gives the quotient and representatives. For an original fresh X~D_(F,s), put A=X mod I. Its EXACT probability vector is

    pi(a)=rho_s(K+t_a)/rho_s(F),        sum_a pi(a)=1.  (C1)

Every coset has strictly positive Gaussian mass. At a=0 this includes X=0: pi(0) differs from the nonzero alignment probability by 1/rho_s(F).

## Uniform upper bound for every atom

The disjoint-ball bound in the H-ALIGN proof applies equally to a translate K+t_a: its point separation is lambda_1(K), even though it need not contain zero. Its layer-cake integral and (P4) therefore remain valid. At s>=4sqrt(n)N(K)^(1/n), shifted Poisson summation and the triangle inequality give

    rho_s(K+t_a) <=rho_s(K)<2s^n/N(K).

Below that threshold, the same layer-cake bound gives rho_s(K+t_a)<=(16n)^n. Dividing by rho_s(F)>=s^n/N(F) proves

    max_a pi(a) <= b :=min(1,2/M+(32n/s)^n).           (C2)

No coset is assigned mass exactly1/M. In particular the historical A-CLASS-ASSERTION-1 failure, where a broad centered zero coset has mass slightly ABOVE1/13, is compatible with (C1)-(C2).

## Full source and comparator, including retained samples

For m fresh iid samples, the ORIGINAL complete source law on (X_1,...,X_m,A_1,...,A_m) is

    P_src(x,a)= product_j [rho_s(x_j)/rho_s(F)
                                      1_{x_j mod I=a_j}].        (C3)

Its congruence-data marginal is pi^m. A uniform congruence comparator has the same public I,F,s,m and independent uniform A_j in V. If the algorithm also retains the X_j, its compatible FULL comparator must specify a lift. The natural analytic comparator used here draws the uniform A_j first, then independently draws

    X_j | A_j=a_j ~ D_(K+t_(a_j),s).

Thus

    P_cmp(x,a)=M^(-m) product_j [rho_s(x_j)
                       1_{x_j mod I=a_j}/rho_s(K+t_(a_j))].      (C4)

Conditional on the full A tuple, (C3) and (C4) have the SAME product lift kernel. Their likelihood ratio and exact distance are

    P_src/P_cmp = M^m product_j pi(a_j),
    TV(P_src,P_cmp)=TV(pi^m,Uniform(V)^m).              (C5)

This comparator is an analysis experiment, not an efficient simulator promised by a centered restricted DGS oracle. It cannot be replaced by independent uniform residues adjoined to the original X_j: that replacement would break the exact constraint A_j=X_j mod I. Likewise, conditioning on a relation-selection/rank/nonzero event uses the actual mass of that event in EACH experiment.

The selected relation and output law are the pushforward of (C3), retaining FAIL. If c=c(a) is a deterministic relation rule and rank screening is used, then the exact output mass at y is the sum of (C3) over all tuples with rank screening passed and sum_j c_j(a)x_j=y; FAIL gets its literal remaining mass. The comparator output is the same sum with (C4). Neither output is asserted to be a centered or spherical Gaussian. Conditional lift normalizers depend on the actual residues and remain present even after c is selected.

## When a uniform comparison is justified

Define epsilon_K=sum_(0!=u in K*) exp(-pi s^2||u||^2). Shifted Poisson gives

    rho_s(K+t_a)=[s^n/N(K)](1+e_a),  |e_a|<=epsilon_K.

The average e_bar=(1/M)sum_a e_a equals rho_s(F)/(s^n/N(F))-1 and is nonnegative, by centered Poisson. Hence pi(a)=(1+e_a)/[M(1+e_bar)]. The triangle bound gives

    TV(pi,Uniform(V)) <=min(1,epsilon_K),
    TV(P_src,P_cmp) <=min(1,m epsilon_K).              (C6)

The shell estimate in H-ALIGNv1 bounds epsilon_K by a/(1-a), with a=(5exp(-16pi))^n, at s>=4sqrt(n)N(K)^(1/n). This comparison is optional and has a clear threshold. The all-width max-atom bound (C2) alone DOES NOT imply closeness to uniform.

For example, for any B>0 let T_B consist of residues of coefficient vectors in [-B,B]^n. Under the original Gaussian, the elementary coordinate tail bound gives pi(T_B)>=1-2n exp(-pi B^2/s^2), while uniform(T_B)<= (2floor(B)+1)^n/M. For M much larger than that finite box size, the two laws are far apart. A tiny maximum atom and a tiny probability of the zero coset cannot be substituted for the full-law comparison (C6).

## One limited consequence, not the selected constructive route

For two independent original residues, collision probability is sum_a pi(a)^2<=b. A nonzero difference X_j-X_i in FI is a subevent of residue collision; X_i=X_j must be removed. For m iid samples, any selected pair difference succeeds with probability at most binom(m,2)b. This follows by a union bound over all pairs, so later selection is paid in full. General coefficient search is a different event and is analyzed in short-relation-v2.md.

If samples have per-call conditional TV errors epsilon_j, their complete original transcript and any postprocessing differ by at most the charged sum under the same full-kernel contract as H-ALIGNv1. Such errors do not disappear upon conditioning on a successful relation or on nonzero output.
