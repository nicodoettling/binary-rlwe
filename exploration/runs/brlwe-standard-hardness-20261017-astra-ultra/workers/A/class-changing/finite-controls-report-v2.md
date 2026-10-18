# A-class finite controls, with the v1 failure preserved

2026-10-17. A-class-finite-1 failed at an overstrong control assertion and was released. Its exact source, empty stdout, stderr and resource record remain unchanged. finite-v1-failure-record.md records the issue before repair. A separately authorized A-class-finite-2 completed in 0.19 seconds, peak RSS12,288KiB, exit0, empty stderr. All repaired assertions use exact integers or Fractions. No experiment remains active.

The exact replacement control confirmed that F=(1+i), I=(3+2i), x=2 gives I''=(1+5i), an associate of the manuscript's (5-i), with norm26 rather than13. Choosing x=1+5i instead gives I''=R and a valid transfer into I. Unit associates do not change the ideal.

For Gaussian weights (1/2)^||x||² on F, the nonzero FI-alignment probability is about2.62168818327523e-8, whereas including zero gives about0.439846309017223. Repeating until the first nonzero sample changes the alignment probability to about4.68030132225431e-8. These are DIFFERENT experiments. The omitted two-dimensional mass is bounded above by1.139e-50.

For weights (63/64)^||x||², the full alignment probability lies between0.0769230769332 and0.0769230769361; this is slightly ABOVE1/13. That explicitly explains the v1 control failure. The nonzero probability lies between0.0668973615050 and0.0668973615079. The total omitted two-dimensional mass is at most2.466e-10. Exact rational bounds are computed in the code before decimal display. The tail bound is the geometric one-dimensional series 2b^((R+1)²)/(1-b^(2R+3)), then 2theta_inside*tail+tail² in two dimensions.

Along the exact chain (1+i)^j, j=0,...,6, the finite conditional probabilities telescope exactly to the total finite acceptance. In the narrow case the total acceptance is about0.220635, almost entirely zero: nonzero acceptance is only4.785e-20. Thus cheap eventual zero acceptance is not a nonzero ideal-SVP algorithm.

The CP-1 cloning control starts with two iid uniform points in Z/8, successively keeps residues divisible by2,4,8, and resamples surviving points with replacement. Exact survival probabilities are3/4,13/32,53/256. The naive selected-stage independent prediction gives27/64, which is false. Even the support-only upper bound15/64 is larger than the actual final survival. Cloning does not manufacture fresh conditional samples.

Finally a finite skew-basis scalar-Gaussian control with basis ((13,0),(-5,1)) has adaptive first-coordinate theta normalizers about1 and2.9802322388e-8 at second coordinates0 and1. Ignoring these normalizers gives total variation about0.52979389 from the intended finite Gaussian law. This validates the need for the UNIFORM center-dependent bounds in small-index-simulation-v1.md; it is not a counterexample under that statement's smoothing condition.

Artifacts are finite-controls-v1.py/v2.py, inputs, commands, original stdout/stderr, resource records, finite-hashes-v1.sha256 and finite-hashes-v2.sha256. The controls do not certify arbitrary-ideal geometry or a standard hardness edge.
