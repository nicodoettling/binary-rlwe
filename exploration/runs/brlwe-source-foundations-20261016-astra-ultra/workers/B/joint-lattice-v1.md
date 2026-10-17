# B-JL-v1 frozen joint cancellation/lattice candidate

Frozen 2026-10-16 21:22 UTC; timestamp approximate until next clock verification. Status PROVISIONAL.

SC-v1 is unchanged. Let public integer k>=1, and restrict potential cancellation multipliers h_1,h_2 to coefficient polynomials of degree <k. Their coefficient magnitudes are unrestricted modulo q for the first algebraic gate. Consider the hidden cancellation relation

  h_1 U_1 + h_2 U_2 = 0 in R_q.

This relation is not directly public; a candidate algorithm must find h_1,h_2 from A_1,A_2, making h_1 A_1+h_2 A_2=h_1 F_1+h_2 F_2 short. We first test whether a nonzero modular multiplier pair exists at all. Any successful short-noise lattice attack using exact cancellation from this multiplier space must pass this gate.

For fixed T, define the d-by-2k matrix M_T with rows
  (U_1(t),U_1(t)t,...,U_1(t)t^(k-1), U_2(t),U_2(t)t,...,U_2(t)t^(k-1)).
All U_i(t) remain independent uniform F_q, including zero. Exact-canceling pairs form ker M_T. Candidate finite obstruction: if d>=2k, a selected 2k-row determinant is a nonzero degree-2k polynomial in independent ideal amplitudes (witness specialization U_1(t)=1,U_2(t)=t^k gives Vandermonde). Hence rank deficiency <=2k/q by elementary polynomial root counting. Disjoint row blocks may sharpen this to (2k/q)^floor(d/(2k)) after writing the exact conditional product law; no posterior support restriction may be hidden.

Comparator and signal obligations: for independent-T source the union of supports imposes different one-sided constraints, never silently the same M_T law. For uniform A_1,A_2 and fixed nonzero h-pair, each root with at least one h_i(t) nonzero makes h_1(t)A_1(t)+h_2(t)A_2(t) independent uniform. Both h's vanish on at most k-1 roots. Any coefficient-short output test needs its actual modular rank and candidate enumeration count, not covariance.

Resource target: an improvement must have exp(o(d))*poly(n,log q) bit cost or another substantive gain over optimized ATT. A lattice whose sole exponential parameter is >=k with k>=d/2 cannot by this fact alone claim an improvement. Rank obstruction does not exclude approximate cancellation, full-degree sparse multipliers, adaptive unrestricted multiplier spaces, or nonlinear decoding.

Next discriminating test: exact tiny enumeration of the rank distribution with all ideal zeros; derive a sharper all-space kernel union bound that is negligible for k=o(d), ideally without an unsupported stage product. Request a reservation only after the exact test size is fixed.

Metadata correction: clock__curr_time immediately before this file write returned 2026-10-16 21:20:07 UTC. The 21:22 heading is an author transcription error. The actual freeze is at approximately 21:20 UTC; scientific statement unchanged.
