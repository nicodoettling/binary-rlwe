# Reserved pivot and fresh output scope

Status: clarification of the frozen B construction, not a new reduction.

The dense elimination map in ../first-test-v1.md selects a pivot only among reserved multipliers a_1,...,a_k. Its output rows use the disjoint designated multipliers a_(k+1),a_(k+2). No failed candidate from the pivot search is reused as an output row. Conditional on the pivot index and selected multiplier, those designated multipliers remain independent uniform; conditional on all multipliers and the auxiliary responses, their designated comparator responses also remain independent uniform. The semi-adaptive map in ../semiadaptive-hints-map-v1.md uses the same reservation with m fresh designated identity blocks.

D's counterexample to selecting a first successful pivot and then reusing failed pivot-search rows does not apply to this frozen map. It does forbid replacing the map by that different selection procedure while carrying over either its ratio law or its endpoint proof. All earlier planted approximation qualifications and the dense-noise obstruction remain in force.
