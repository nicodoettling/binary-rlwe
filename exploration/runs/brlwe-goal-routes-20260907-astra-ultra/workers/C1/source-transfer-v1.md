# C1-COMP v1 — what one challenge can and cannot amplify

Frozen author proof and exact controls. Status PROVISIONAL pending nonauthor review. This is a scoped obstruction to named transformation/accounting classes, not a proof that every polynomial-q computational reduction fails.

## Exact source and target

Throughout this note R is the fully split product ring F_q[X]/(X^n+1), T is a uniform d-subset of roots and I_T has CRT support T. The supplied planted pair is P=law(U+F,V+H), with U,V independent uniform I_T given T and F,H independent iid coefficient D_ell, independent jointly of the ideal points and T. The comparator is Omega=Unif(R^2). Only the public pair and parameters are supplied. Any public algorithm gets this one pair, fresh internal coins, and public code; it cannot request new points from the challenge's hidden T. The target is the independent-error one-sample binary-RLWE distribution stated in larger-q-theorem-v1.md, with the polynomial-q baseline also admitted for the negative controls here.

## C1-MIX — exact cancellation defeats conditioning-only inheritance

For any rational 0<delta<1/2 let Q=Bernoulli(1/2), P_bad=delta_0 and P_good=Bernoulli(1/[2(1-delta)]). Then

    P=(1-delta)P_good+delta P_bad=Q,
    Pr_good[D=1]-Pr_Q[D=1]=delta/[2(1-delta)]

for the deterministic test D(x)=x. Thus even an inverse-polynomial advantage on a 1-delta good branch need not give any decision advantage on the full source. If delta=n^-K, the good advantage is inverse polynomial with a fixed exponent. Its signed gap is cancelled exactly by the bad branch. This model refutes every universal active-source hardness inheritance argument whose only premise is this mixture decomposition. It does not exhibit actual HLBDD distributions with P=Q, and it does not rule out an argument exploiting their additional specific algebra.

A more directly concentrated example is Q=delta_0 and P=(1-delta)delta_0+delta delta_1: all distinguishing advantage delta lies on the rare branch. Removing the deficient branch erases the advantage entirely. Together the two models reject both informal claims that a high-mass branch retains most signed advantage and that repeatedly evaluating a test can necessarily move the advantage to that branch.

Any adaptive computation on one supplied X, with arbitrarily many fresh independent tapes, is a Markov kernel K from X to its complete transcript. For P=Q, KP=KQ exactly. This statement covers evaluating D repeatedly, estimating a conditional acceptance probability, adaptively choosing source symmetries, and randomized stopping based only on the observable transcript. It does not depend on a query bound. Fresh tapes make evaluations conditionally independent given X when the chosen calls are independent; they do not make the inputs independent marginal draws.

For delta=1/3, P_good=Bernoulli(3/4). One good draw gives advantage 1/4; the majority of three independent good draws gives 11/32, and of nine gives 59123/131072. Repeating deterministic D on one X returns the same bit and does not amplify that one-input advantage. Independent draws of the ACTUAL mixture P still equal independent Q, so even they give zero decision advantage in this cancellation model. A sampler for P_good or for fresh points conditional on the same hidden T is an additional resource, not a consequence of one source challenge.

## C1-SPAN — both components improve but do not eliminate fixed-budget deficiency

Condition on T,U,V as proof variables and set J0=RU+RV. Every output of the form alpha U+beta V lies in J0, even if alpha,beta depend adaptively on all previously generated combinations or on the full latent tuple. Giving the coefficients this excessive information only strengthens the following impossibility. For a fixed coordinate i in T, J0 vanishes there iff U_i=V_i=0. These events are independent with probability q^-2. Thus M=dim(I_T/J0) is Binomial(d,q^-2).

Conditional on U,V, independent uniform ring coefficients alpha,beta make alpha U+beta V exactly uniform in J0. Any distribution supported in J0 has distance at least 1-|J0|/|I_T| from uniform I_T; the uniform-on-J0 law attains it. Therefore the optimal averaged conditional defect is

    eta_span=E[1-q^-M]=1-(1-q^-2+q^-3)^d.                (SPAN.1)

For d>=1, eta_span>=q^-2-q^-3, so for any fixed q<=n^K it is at least (2/3)n^(-2K) when q>=3. This is nonnegligible. For t truly independent source ideal points with the SAME hidden T the corresponding formula is 1-(1-q^-t+q^(-t-1))^d. A growing t can make it negligible, but ordinary HLBDD supplies t=2; polynomially many fresh coefficients applied to those two points leave their original J0 unchanged.

The q=3,d=1 and d=2 exact values are 2/27 and 104/729; q=5 gives 4/125 and 984/15625. Exhaustive exact enumeration verifies these in exact-controls-v1.py/json. At q=3, all three scalar shears U+tV vanish simultaneously with probability 1/9, whereas treating them as three independent uniform ideal coordinates would falsely give 1/27. The shared all-zero branch persists after any finite number of shears.

This is an exact retained-variable/support obstruction. It does NOT establish the same lower bound after adding noise and projecting to a public pair; such projection may erase it. Nor is the optimal latent span sampler a public small-noise source map: alpha(A)+beta(C0) has error alpha F+beta H, and arbitrary ring coefficients can greatly broaden/correlate that error. Arbitrary public nonlinear maps, additive fresh uniform masks, map-dependent changes of ideal support, and changed source budgets lie outside SPAN.1. These exclusions are material, not loopholes silently closed by the formula.

## C1-SYM — explicit public symmetries and their limits

A simultaneous cyclotomic automorphism X->X^k for odd k, multiplication of either component by a signed monomial unit, component swaps, and sign changes preserve the equal-small-noise source law (with its uniform support law) and preserve Omega. Signed coefficient permutations preserve the iid symmetric coefficient Gaussian. These symmetries permute CRT support coordinates or scale them by nonzero values; the common-zero count of U,V is invariant. Uniform first-point activity is not created by randomly traversing such an orbit.

More generally any public fixed M in GL_2(R) preserves Omega, and at the latent level preserves the joint ideal-point law Unif(I_T)^2. At each CRT coordinate an invertible 2x2 matrix preserves whether (U_i,V_i)=(0,0). But M(F,H) generally has a changed correlated error law. Equal Gaussian widths give exact signed-swap invariance; they do not give invariance under arbitrary modular shears. Applying different Galois permutations to the two components generally changes their shared-ideal relation. None of these observations asserts that the changed law equals the desired target or A2 source.

If M itself is selected from the observed pair, fixed-M bijectivity does not by itself prove that the adaptive map preserves Omega. That endpoint requires its own full joint calculation. Likewise a selector that tries many transformations and keeps one satisfying an observable event conditions the source and comparator with their actual, potentially different normalizers.

## C1-REJECT — observable rejection pays both normalization and resources

Let E be an observable acceptance event in a randomized kernel. For laws P,Q, let a=P(E), b=Q(E), and let r=P(B=1|E), s=Q(B=1|E), for positive a,b. A public one-challenge test that runs the kernel and returns 1 iff E and B has signed gap ar-bs, not a(r-s). The extra (a-b)s term can cancel. A rejection sampler supplied fresh independent challenges from each respective world has conditional outputs P(.|E),Q(.|E), expected challenge costs 1/a,1/b, and r-round failure probabilities (1-a)^r,(1-b)^r. These formulas require actual fresh input draws. A one-challenge algorithm can instead rerun its internal E-tape, but its posterior law is reweighted by a function of its original X and cannot be identified with independent challenge rejection without a separate joint-law proof.

The exact control P=(3/4,1/4), Q=(1/2,1/2), with acceptance probabilities (1/3,1) on inputs 0,1, gives a=1/2 and b=2/3. Conditioned P is uniform but conditioned Q is (1/4,3/4), at TV 1/4. Correct planted conditioning alone therefore does not match the original uniform comparator. Hidden activity is not an observable E unless an explicit public procedure decides it with its errors/runtime paid.

For finite K output laws, the universally valid transfer inequality is

    Adv_target(D)<=Adv_source(D composed K)
                    +TV(KP,target)+TV(KOmega,Omega).

Both approximation terms must be negligible for full negligible-advantage inheritance by this route. The prior exact-uniform-preserving entropy obstruction does not extend merely by adding a small comparator error. Its rare-support collapse counterexample remains applicable. On the other hand, a special efficient K that is literally the identity outside an event rare under Omega but often modifies P gives an observable change-event distinguisher; no such rare-modification implementation is supplied by a statistical support argument. General PPT maps with negligible comparator TV remain an open class here.

## Outcome and next test

No new full polynomial-q decision implication was obtained. C1-MIX and C1-SPAN are scoped finite obstructions; they prevent a claimed universal amplification/conditioning repair from bypassing the missing signed-advantage argument or source budget. Equal-small-noise joint nonlinear maps with controlled approximate comparator preservation remain open. The next concrete test for such a proposed map is its exact planted/uniform pair law, not its noise covariance or planted posterior alone.

The constructive escape developed in larger-q-theorem-v1.md changes q,d so the existing observable hybrid's actual image loss becomes negligible. Its new extraction and bit-complexity calculations have not yet received a fresh review, and its inherited finite analytic premises remain explicit.
