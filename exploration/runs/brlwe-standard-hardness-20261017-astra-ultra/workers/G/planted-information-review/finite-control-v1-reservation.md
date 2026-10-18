# G-PI-FV1 reservation and frozen design

The coordinator authorized one foreground run, at most 120 seconds, 512 MiB and one million joint atoms. The complete exact input and code were written before launch. Actual reserved design: 624,328 prior atoms, no sampling or floating-point probability calculation. Main mass totals are at most 20 bits; posterior cross-products at most 40 bits. Python arbitrary precision removes overflow risk. Expected memory is under 64 MiB, with an enforced 512 MiB address-space limit. The execution command has an enforced 120-second timeout. No installs, network, services or detached work.

The q=101 planted controls cover k=1 and k=2. The complete uniform comparator is enumerated at q=101,k=1 and q=5,k=2; the q=101,k=2 comparator would exceed the reservation and is deliberately not enumerated. Its exact wrapper formula is checked symbolically in the proof review. The q=5 planted case is a negative control that deliberately omits the large-q unwrapping premise. Any decoder failure there is preserved as a warning against deleting that premise, not as a counterexample to the frozen theorem.

The two-ideal mixture uses J=3R and J=6R with nontrivial overlapping public-A support, checks full posterior vectors by cross-multiplication on every positive-mass branch, and separately checks equality of optimal guessing success. Its complete source supports, priors and common target error law are in the input JSON. It is finite uniform-coset sampling, never asserted to be the unbounded lattice Gaussian.

CP1 enumerates its original five traces and all 32 oracle states. The expected outcome is rejection of the false gamma-squared product bound, while retaining its exact posterior normalizers.

Original output and resource report are preserved unchanged in adjacent files. A failure must be preserved before any repair; any repaired code or theorem requires a new version and a new reservation if re-execution is needed.
