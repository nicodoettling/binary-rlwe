# Proof and conditional audit of FF3-SELECTOR-PUBLIC-v2

For each positive-mass atom z, condition on Z=z. Write pi_z(s)=Pr(S=s|z). The normalized accepted pair obeys Pr(E=e,C=c|S=s,z)<=M mu_z(e), by the base theorem's pointwise normalization at every x and averaging over the conditional input. Therefore

    sum_(e,c) max_s [pi_z(s) Pr(E=e,C=c|s,z)]
       <= sum_(e,c) M mu_z(e) max_s pi_z(s)
       <= ML max_s pi_z(s).

This is the optimal guessing probability from the accepted pair at that z. Postprocessing by the declared fresh output kernel cannot increase it. The joint observation includes Z, so its optimal guessing probability is exactly the countable sum of the conditional guessing probabilities weighted by Pr(Z=z). Countable summation is legitimate for nonnegative terms; zero-mass atoms contribute zero and no other points exist in the declared discrete model. This gives the claim. Independence and uniformity, when assumed, make max_s pi_z(s)=1/N. The transcript Z=S gives an upper bound ML and therefore no spurious secrecy. No product of conditional stage probabilities or unproved posterior independence is used.
