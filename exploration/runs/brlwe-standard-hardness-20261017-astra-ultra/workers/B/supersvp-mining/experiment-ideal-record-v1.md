# B-SUP-2 exact ideal/ring encoder control

Authorized by root, after its live cap read21:17:22 UTC, as sole active team job, <=30 seconds and <=256MiB address space. Start notification sent; completed and reservation released21:18:48 UTC. No computation remains active.

Input/code: control-ideal-v1.py, seed20261017, n2,q5,J=(17,X-4), column basis[[17,-4],[0,1]], h9,p4,r12,k5. Every correctness calculation uses Python Fraction or integers. No Gaussian distributions or hardness claims are tested. The script enforces RLIMIT_AS268435456 and RLIMIT_CPU30; the command adds timeout30 with1-second kill grace.

All25 natural targets and25 X-rotated trapdoor targets passed. All630 constructed SIS relations lifted to J,627 nonzero. Quotient-only encoding fails20/25 targets, retaining the need for residual blocks. A characteristic-zero multiplication control has16 distinct images; the corresponding modulo-q multiplication collapses to one, so modular injectivity would be false.

Script monotonic elapsed0.1740502530010417 seconds; maxRSS12288KiB. Exec-reported wall_time_seconds0.089118193 is preserved separately and is not used as the script timer. Exit0; stderr empty. The complete command, stdout and stderr are adjacent immutable files.

SHA256:
- code ba3684bc4b4eadbf67c294dfdcd41a4d21d6db9e5eb15b731d972d83833ae178
- command 9458c5f4a0643b4cf0b5702aea490626148e874a8c31a6f2c95517d55fc21de1
- stdout 9ac0af3c2818d0dae36e1ce1967fc753b65e7ad8ae89f5f6742ce43cb2690c51
- stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

This finite algebraic control does not certify the new theorem, Gaussian sampling laws, rank-posterior estimates, or any asymptotic hardness premise.
