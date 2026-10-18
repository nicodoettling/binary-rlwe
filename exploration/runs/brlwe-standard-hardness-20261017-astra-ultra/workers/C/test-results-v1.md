# C-ENDPOINT-1 exact results

PROVISIONAL supporting falsification evidence; no hardness certification.

Reservation was granted before execution and released after completion. The exact command is endpoint_control_v1.command.txt. The executable uses 30-second GNU timeout and sets RLIMIT_AS=268435456 bytes before enumeration. It terminated successfully after 0.085005 seconds of measured Python time, with maximum RSS 12,288 KiB and empty stderr. No random seed is needed: enumeration is exhaustive and all probabilities are fractions.Fraction.

At n=2,q=5, all four ideals (empty support, each singleton root, full support) satisfy exact zero TV for the fresh-offset planted pair, including retained finite correlated mask branch. The comparator pair has exact zero TV from uniform. Each secret value is checked separately before averaging, retaining the all-zero-secret branch.

Without the fresh ideal offsets, each singleton support gives pair TV 24/125. Its zero-pair probability is 29/125 instead of the uniform-ideal value 1/25. The full ideal gives TV 5184/15625 and zero-pair probability 841/15625 instead of 1/625. These equal the explicitly enumerated support-rank mixtures. Thus the test preserves the failure it is intended to repair.

The finite joint mask surrogate is sampled by one branch: probability 1/2 gives both masks zero; probability 1/3 gives masks (1,0),(0,1); probability 1/6 gives masks (-1,1),(1,-1), represented modulo 5. Exact equality holds while retaining this branch, so the check tests full dependence rather than independent mask marginals. It does not approximate the actual continuous Gaussian law.

An additional 660-case integer grid finds no simultaneous q^d≤2^n and q^d>2^n, the latter being the necessary primary Order-LWE condition at the weakest w=1. This is a finite arithmetic regression, not the proof of the asymptotic norm argument. CP-1 reproduces 21/2000>1/100 and the later conditional 21/221<1/10; the old selected-product inference remains rejected.

Files and hashes are bound in experiment-record-v1.json. The experiment establishes only the named finite algebraic controls. It does not test primary-source precision, Gaussian tails, worst-case reduction uniformity, quantum hardness or asymptotic security.
