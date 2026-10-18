# C-COS v1 — three explicit attempts at the known-ideal decision edge

Status: **PROVISIONAL**. These are attempted algorithms with computed endpoint laws and identified failures. They establish neither computational hardness nor a general impossibility. The original SC-v1 hardness remains OPEN.

## Frozen experiment and requested direction

Let n>=2 be a power of two, q>=n² a splitting odd prime, R_q=F_q[X]/(X^n+1), and T a fixed public d-subset of CRT coordinates. Put I=I_T and P={x∈R:x mod q∈I}. The public representation is T or an ordinary HNF of P, not a short basis, decoder, short-vector advice, or trapdoor. For k>=1, define G=R_q^k and J=I^k. The noisy law is X=U+F, with U uniform J including zeros and F having independent coefficient D_s entries. The comparator Z is exactly uniform G with the same public T. SC-v1 uses k=2,s=ell and subsequently hides T. A random-T version samples T from its stated law before the experiment; a guarantee averaged over T does not become a guarantee for every T.

A distinguisher D for the hidden experiment gives the public experiment the same advantage by ignoring T. The desired next arrow is a polynomial-time algorithm using D to solve a specified worst-case lattice problem. Merely calling the public experiment average-case BDD is not that arrow. In particular, P ranges only over divisors of qR. It is not an arbitrary worst-case ideal lattice L supplied by a basis. An efficient geometry-controlled map L to this P family is an additional missing obligation.

## Attempt 1: shift and smooth a worst-case target

Given a target t mod q and oracle D, sample U uniform I and E from D_s^n and query D(t+U+E). At t∈I the query law is exactly the planted noisy-point law. At t=v+e with v∈I it is the translate of that law by e, so its acceptance differs from the planted acceptance by at most TV(E,E+e), whenever the translate is defined on the chosen lattice/torus. A k-query version with independently sampled masks has the corresponding full product law, not fresh samples supplied by the original source experiment.

At a far target t, the query law is instead t+U+E. It is not the uniform comparator. The oracle's average advantage imposes no worst-case far rejection promise. Exact finite negative control: n=2,q=17,I={0}, E uniform B={-1,0,1}², t=(8,0), and D the indicator of B union (t+B), modulo17. These two boxes are disjoint. Planted acceptance is1, uniform acceptance18/289, advantage271/289. Both the t=0 query and the t=(8,0) query are accepted with probability1. Yet the latter has distance8 from17Z², whereas the masks have Euclidean norm at most sqrt2. This is a finite-support falsification of this query wrapper, not a claim about Gaussian hardness.

For genuine coefficient discrete Gaussians, replace B by [-b,b]^n with b<q/4 and choose a disjoint distant translate. Both query acceptance probabilities are at least Pr[E∈B], while comparator acceptance is at most2(2b+1)^n/q^n. Thus negligible Gaussian tails do not repair the missing promise. Symmetrization by translations in I changes neither conclusion. This counterexample needs no trapdoor and its I={0} predicate is efficiently computable; it only disproves a universal wrapper, not hardness at the intended positive d.

## Attempt 2: use coherent Fourier sampling to extract a dual vector

Even grant coherent access to a deterministic D:G→{0,1}; an ordinary distinguisher interface does not supply this automatically, though a known efficient classical circuit can be reversibly evaluated. Set f=1-2D and use normalized Fourier coefficients

    fhat(z)=E_{x uniform G}[f(x) conjugate(chi_z(x))],
    Phat(z)=E_{x~X}[conjugate(chi_z(x))].

Prepare a uniform superposition over G, apply phase f, and Fourier transform. The exact output probability at z is |fhat(z)|². Since X is invariant under J translations, Phat(z)=0 outside J^perp. If delta=|E_X D-E_Z D|, Fourier expansion and Cauchy–Schwarz give

    2delta = |sum_{z≠0} fhat(z) conjugate(Phat(z))|,
    p_nonzero_annihilator >= 4delta² / chi2(X||Z),
    chi2(X||Z)=sum_{z≠0}|Phat(z)|².

Conjugating the Fourier convention does not affect these real absolute-value relations. If chi2=0 then delta=0. For a selected short-frequency set W⊂J^perp\{0}, put C_W=sum_W|Phat|² and C_tail=sum_{J^perp\(W union{0})}|Phat|². Then

    Pr[z∈W] >= (max{0,2delta-sqrt(C_tail)})²/C_W

when C_W>0. These are exact finite-group bounds. They do not promise inverse-polynomial success from inverse-polynomial delta alone. Nor does a nonzero annihilator frequency by itself meet an approximation guarantee for an arbitrary worst-case ideal lattice.

The density term is enormous in the narrow SC regime. Let b=ell², s=ell and S=I+[-b,b]^n mod q for one row. The elementary one-dimensional Gaussian tail bound gives Pr[F outside box]≤n exp(-pi ell²)/pi. Meanwhile

    mu=Pr_Z[S] <= q^d(2ell²+1)^n/q^n.

If q^d<=2^n and q>=n², this upper bound is [2(2ell²+1)/q]^n=exp(-Omega(n log n)). For the k-row product set, replace mu by at most the kth power and the tail by at most k times the one-row tail. Applying Cauchy–Schwarz to the centered indicator of S gives

    chi2(X||Z) >= (Pr_X[S]-mu)²/[mu(1-mu)]

for 0<mu<1. Thus the spectral advantage bound can pay an exponential density ratio precisely in the source's useful narrow-noise regime.

An exact success-cost control is D=1_S when X is uniform on a finite set S of uniform mass mu. Here delta=1-mu, chi2=1/mu-1, and the total nonzero Fourier mass is exactly4mu(1-mu). Constant distinguishing advantage can coexist with exponentially small nonzero-frequency probability. For I={0} and S a coefficient box this D is polynomial-time; for general I, membership in I+box is not asserted efficient. This is a limitation of the specified uniform-phase pipeline and of a guarantee based solely on delta, not a quantum lower bound for all reductions. Repetitions cost order1/mu for this example; ordinary amplitude amplification of this event still costs order1/sqrt(mu).

Preparing a Gaussian-localized state with an additional coherent error label does not automatically bypass the issue: tracing out that label loses the interference needed for a pure periodic Gaussian. Erasing it is a search/uncomputation requirement, not supplied by a decision bit. No theorem asserting impossibility of a different state preparation is claimed.

## Attempt 3: random ring multiplication of a target

For an integer target t∈R_q, sample a uniform in R_q, Z uniform I, and fresh E, and query D(a t+Z+E). Because multiplication by t maps uniform R_q onto the principal ideal R_q t, the exact query law is

    Unif(I+R_q t)+E.

At t∈I this is the planted law. If the CRT support of t together with T is all n coordinates, it is exactly the uniform comparator, even after adding E. But a worst-case far target may have only one nonzero CRT coordinate outside T, yielding a proper enlarged ideal and no comparator guarantee. Conditioning a on units changes the image to active-coordinate values and must also charge those zero branches; it does not fill missing coordinates.

For a noisy near target t=v+e, the law becomes a v+Z+a e+E. The unknown error is multiplied by a. Uniform a has no small multiplication norm guarantee, and choosing small a to preserve the error removes the exact uniform-image calculation. Therefore the wrapper is an exact ideal-membership test on its special branches, not a BDD reduction. Exact ideal membership is already polynomial-time from the public representation.

## Checked standard theorem interface

The primary version of Peikert, *Public-Key Cryptosystems from the Worst-Case Shortest Vector Problem*, Proposition3.2, gives a classical reduction for bounded-distance CVP radius alpha q/(sqrt2 r), using both a search-LWE solver and D_{L*,r} samples with r>=sqrt2 q eta_epsilon(L*). Its search output enables recovery of the nearby vector. Theorem3.1 subsequently derives GapSVP hardness under its parameter and basis-quality hypotheses. Replacing that search solver by the noisy-coset decision bit above is not a stated theorem. The public Gaussian-coset sample supplies neither the required dual DGS oracle nor the search output. These are concrete missing dependencies, not advice we silently grant. Primary source: https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol08491/DagSemProc.08491.4/DagSemProc.08491.4.pdf (Proposition3.2, PDF page12; Theorem3.1, page11).

## Outcome and scope

All three algorithms have an exact planted endpoint on a limited branch. None presently gives the required worst-case comparator, polynomial success, and arbitrary-ideal input coverage together. No new hardness assumption has been substituted for these missing edges. The Order-LWE route and noninvertible-order route are recorded separately; the direct route does not repair their noise/entropy mismatch. The next useful positive route would need a new randomization/sampling mechanism with explicit full endpoints and a quantified density or approximation guarantee, rather than another name for the known-ideal experiment.
