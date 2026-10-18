# Preserved literal null-branch counterexample, before any repair

Frozen input: pair-theorem-v1.md, SHA256 8bce599bcf65ce6dc980b2859e2f89e9b07f0a0f3642f7557359292e2966c0b7.

This concerns the literal **atomwise** meaning of “every positive-probability prior branch.” No extra restriction to countable retained histories is stated. It does not claim to falsify an almost-sure regular-conditional interpretation.

Take n=2, R=Z[i], I=H=R, c=1, J=L=R, and G trivial. Take gamma=1, W=10, and m=2. The displayed parameter is exactly b=9/100. Let U be uniform on [0,1], retain U as classical private state, and set X_1=0. At the second attempted stage return X_2=1 when U<1/2 and X_2=i otherwise. Both trials are attempted; no rejection or abortion occurs. Retained U is relevant to the next sample choice and belongs to the complete preceding transcript. Its every exact value has probability zero, so the complete preceding transcript has no positive-probability atoms. Under the atomwise reading the claimed conditional requirement for eta_2=0 is therefore vacuous.

Nevertheless X_2-X_1 is always a nonzero element of I of norm one. The pair event and useful-selector success both have probability one, contradicting the displayed upper bound 9/100.

This construction uses X_1 in J, hence does not rely on the ambiguity of the ambient space of arbitrary X_1. It uses uncountable retained private state; if the intended model permits only countably many finite classical transcripts, that is an additional restriction and this particular construction is excluded. The conditional law given the retained history in the regular-conditional sense is a point mass, so the construction does not satisfy an almost-sure conditional Gaussian premise.

The counterexample has now been preserved before presenting a repair. It requires no numerical experiment.
