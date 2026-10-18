# BT14-FV1 reserved exact finite control

Reservation: coordinator approved one foreground job, at most 120 seconds, at most 512 MiB, no more than one million branches; Python standard library only. This file records estimates before execution.

Inputs will be the finite alphabets {0,...,7} and {0,1,10,11,20,21,30,31}, the uniform reference law of eight atoms, and all laws obtained by moving one mass 1/8 from one reference atom to a different atom, together with the unmodified reference law. There are 57 candidate laws, each with TV at most 1/8. All probabilities are exact fractions. No random sampling is used; seed is inapplicable.

The conditional union control will enumerate histories of lengths one and two, then all 57 candidate next-step laws. At most (8+64)*57=4,104 conditional configurations are inspected, with eight possible next atoms each, giving 32,832 atom checks. A dynamic programme for at most four stages uses subsets of an eight-point alphabet, fewer than 1,024 stage/state entries, with at most 57*8 transitions each. Even a crude sum is below 500,000 transitions and below one million branches. The additional geometry and normalization checks are smaller than these bounds.

The largest exact dynamic-programme denominator is at most 8^4=4096; conservative fraction-integer bit allowance is 64 bits. Python object overhead dominates. Expected memory is below 32 MiB; a process address-space limit of 512 MiB will be imposed. The exact arithmetic script will reject a branch counter above one million. CPU and elapsed-time bounds will be 120 seconds. All code, command, stdout, stderr, and resource output will be retained in this directory.

Purpose: falsification controls for causal union bounds, the one-TV-charge-per-later-sample accounting, predictable stopping, zero-probability outcomes, arbitrary output-selected pairs, and the insufficiency of marginal laws. These finite laws are NOT exact discrete Gaussians; successful controls cannot certify the infinite-support Gaussian theorem or the Poisson identity. The actual truncated-Gaussian normalization issue will also be handled by a symbolic exact finite-support calculation in the report.
