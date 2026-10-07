# Probability Audit and Regression Cases

Read this reference for proofs involving adaptive observations, conditioning,
transcripts, posterior resampling, caches, stopped processes, or sequential
events.

## 1. Sequential bounds require sequential evidence

Marginal estimates

\[
  \Pr[E_i] \le p_i
\]

do not imply

\[
  \Pr\!\left[\bigcap_{i=1}^r E_i\right] \le \prod_{i=1}^r p_i.
\]

To use the product bound, prove for a declared filtration
\((\mathcal F_i)_{i=0}^r\) that, on every positive-mass surviving history,

\[
  \Pr[E_i\mid \mathcal F_{i-1},E_1,\ldots,E_{i-1}]\le p_i,
\]

or supply a different explicit invariant whose iterated expectation gives the
claimed result. The proof must survive adaptive event selection, posterior
renormalization, disappearing support, repeated observations, and zero-mass
branches.

Local independence of a fresh oracle value is not enough. Conditioning may
remove sibling cylinders that supplied compensating mass even when the newly
read value remains independent under each surviving component.

## 2. Conditioning and cache checklist

For each stage, write down:

- the ambient sample space and current density or component weights;
- the sigma-algebra exposed before selecting the next event;
- whether the event address, value, incidence, and cache-hit status are known;
- the exact Bayes numerator and normalization denominator;
- which support components disappear after the observation;
- whether an address is adaptive and which prefix determines it;
- whether a cached value is physically present but latent to the proof;
- whether replay/resampling changes the joint law or only its representation;
- how a trace can split, merge, or be counted across adaptive branches; and
- the pointwise inequality used before taking expectation.

Never let a proof branch on cache-hit status unless the actual algorithm can
observe it. Conversely, do not treat a physically cached value as newly
independent merely because the proof delays revealing it.

## 3. Finite-support falsification protocol

Apply this protocol to every probabilistic lemma before acceptance:

1. Reduce to the smallest finite state spaces consistent with the assumptions.
2. Represent probabilities as exact rationals where feasible.
3. Enumerate deterministic algorithms first; randomized algorithms are
   distributions over deterministic tapes.
4. Encode all premises, including strict versus non-strict thresholds,
   measurability, correctness, query caps, and positive-mass conditioning.
5. Search for a model satisfying the premises and violating the conclusion.
6. Concentrate probability near thresholds and include rare branches, repeated
   queries, adaptive addresses, and cached observations.
7. Cross-check any found model by an independent exact calculation.
8. Store the model, expected result, search bounds, and command in the
   regression registry.

Use exhaustive enumeration, SAT/SMT, LP/MILP, symbolic algebra, or a custom
exact checker as appropriate. A solver result needs a human-readable witness.
`UNSAT` only proves the encoded finite instance, not the unrestricted lemma.

## 4. Canonical regression CP-1: cached-prefix branch inflation

### Purpose

This finite random-oracle model falsifies the tempting rule that repeated raw
lightness or locally restored independence yields a product bound after
sequential conditioning. It must reject any proof that silently multiplies
marginal residual-hit bounds or claims that transferring a cached prefix value
cannot increase the relevant dominating mass.

### Model

Let a binary random oracle have independent uniform values on

\[
  x,e_0,e_1,f_0,f_1,
\]

and set \(\gamma=1/10\). Before conditioning on \(vk=1\), KeyGen has traces

\[
  A_b=\{e_b,f_b\} \quad\text{with mass }21/2200,
\]

\[
  C_b=\{e_b,x\} \quad\text{with mass }1/11
\]

for \(b\in\{0,1\}\), and an empty trace \(D\) with mass \(879/1100\).
Trace \(C_b\) outputs \(vk=1\) exactly when \(H(x)=b\); traces \(A_b\) and
\(D\) always output \(vk=1\).

Since \(\Pr[vk=1]=10/11\), conditioning on \(vk=1\) gives

\[
  \Pr[A_b]=21/2000,\qquad
  \Pr[C_b]=1/20,\qquad
  \Pr[D]=879/1000.
\]

Each \(C_b\) records the trace answer \(H(x)=b\). Let Sign return one fixed
signature. Verify queries \(x\), sets \(b=H(x)\), queries \(e_b\), then
queries \(f_b\), and accepts. This verifier has three queries, KeyGen traces
have at most two, and correctness is pointwise for every oracle.

### Calculation

At the initially closed posterior, query incidences are

\[
  p(x)=0.1,\qquad p(e_b)=0.0605,\qquad p(f_b)=0.0105.
\]

None is heavy under the strict rule \(p>\gamma\). Fix the matching of verifier
positions \((2,3)\) to KeyGen ordinals \((1,2)\). It occurs for \(A_b\) when
the independent base has \(H(x)=b\), so its total probability is

\[
  \sum_{b\in\{0,1\}} \frac{21/2000}{2}
  =0.0105
  >\gamma^2=0.01.
\]

After the first selected hit at \(e_b\), transferring the cached value
\(H(x)=b\) and applying Bayes' rule leaves \(f_b\) at incidence

\[
  21/221\approx0.095<\gamma.
\]

Thus the second hit is still residual even though the two-stage event exceeds
the claimed \(\gamma^2\) bound. In the failed envelope, first-stage mass rises
from \(0.0605\) to \(0.1105\) when the cached value is transferred.

### Failure mechanism

The first selected event removes sibling base cylinders that previously
compensated the matching-trace term. A later cached-prefix transfer then changes
relative branch mass. Neither restarting the verifier at each selected stage
nor asserting local independence of the transferred value repairs this. The
missing object is a filtration- or change-of-measure invariant that pays for
support removed along the adaptive prefix.

### Required regression outcome

A candidate proof passes CP-1 only if it does all of the following:

1. Reproduces the posterior masses and the strict-lightness calculation.
2. Computes \(0.0105>\gamma^2\) and therefore rejects the old product claim.
3. Identifies support restriction and renormalization, not oracle-value
   correlation alone, as the failure.
4. Keeps latent cache-hit status out of the branch filtration unless the
   algorithm observes it.
5. Shows explicitly why its replacement statement is not falsified by this
   model, including all threshold losses or prefix charges.

Any proof that concludes the old \(\gamma^2\) bound on this model fails the
audit, regardless of how many marginal or local-independence checks it passes.

## 5. Adding new regressions

Assign stable IDs (`CP-2`, `CP-3`, and so on) rather than replacing CP-1. Keep
each exact enough for another reviewer to reproduce without access to the
original discussion. When a later repair changes assumptions, record whether
the case now violates a premise or remains a live test; do not silently remove
it.

