# RF4 separate exact finite parameter-witness recheck

Verdict: **SUPPORTED for finite conditional compatibility, after the two preserved corrections.** This is a narrow addendum to the main RF4 review. It neither changes the frozen F-QFINITE v2 inputs nor supplies standard-family hardness, security at dimension16, or a complete gate count independent of the supplied Rec implementation.

Reviewed exact source: `coordinator/quantum-integration/effective-parameter-v3`.

| File | SHA256 |
|---|---|
| certificate.md | bdc9ea7aa9ba63f59a2ed52a16ee1cdbe31334cee469364c74a1cf39fd98611d |
| control.py | 6f09e6c5218075cb41fef696906b0a30cd73d5fb913228588ba5bd39a648f947 |
| stdout.json | 464c6a248dcc27479d37a7c379e628ea727ff12a16a8bf1a7cf72506cdf9c487 |

Every file listed in the v3 freeze receipt was hash-verified before the independent exact check. The earlier certificate, code, input, output and resources were copied into RF4 as `parameter-witness-read-v1-*`, with hashes in `parameter-witness-read-hashes-v1.json`.

## 1. Preserved objections and their resolution

[RF4-PARAM-T-1](parameter-witness-gap-before-recheck-v1.md) records that v1 stated t=288 while using the losses for t=4608. The original byte sequence is preserved. V3 now fixes tau2=512, t=tau2*ell=4608, n/t=1/288 and 3t²/(4tau2²)=243/4 in both the certificate and code. It also explicitly checks the squared A completion inequality. This resolves the parameter inconsistency; merely changing the prose while leaving a mismatched loss would not have sufficed.

[RF4-PARAM-ENC-1](parameter-witness-encoding-observation-v1.md) records that the old integer length bit_length+3 did not specify the required binary framing. V3 gives a typed self-delimiting format: two-bit tag, sign, unary magnitude length and terminator, then magnitude; rationals and lists have their own tags and recursively encoded components/counts. I independently materialized and decoded this format. The old numerical G0 is superseded. New B_len=859028, A_eval=863357 and G0 bit length1627 match exactly. Neither repair changes a frozen F/C8 theorem premise or error constant.

## 2. Independent algebra and prime certificate

For q=2^64-2^32+1, the independently recomputed residues are7^(q-1)=1 and7^((q-1)/2)=q-1 moduloq, and the latter minus1 is coprimeq. Hence for every prime divisor p ofq, ord_p(7) divides q-1 but not(q-1)/2. Since q-1=2^32(2^32-1), its2-adic valuation is exactly32. Thus2^32 divides p-1 and p>=2^32+1>sqrt(q). Every composite positive integer has a prime divisor at most its square root, so q is prime. This is a deterministic order certificate, not a probable-prime test or unproved factoring step. Also q=1 modulo32 and gcd(q,97)=1.

The residues19²,19⁴,19⁸,19¹⁶ modulo97 are70,50,75,96. Consequently evaluation X->19 induces a surjection R=Z[X]/(X^16+1)->F97 whose kernel is(97,X-19). Its norm is97<=256=2^(rho n). The ordinary column basis97e0 and e_j-(19^j mod97)e0 is exact. It is ordinary public ideal data, not a supplied short-basis witness.

I reconstructed B=q*(conjugate(J) basis)^(-T) in closed form. Let r_j=19^j mod97. Then B[0,0]=q/97; for1<=i<=15, B[i,0]=-q r_(16-i)/97 and B[i,16-i]=-q; other entries vanish. This independently realizes qJ^-1. Its denominator product is b=97^16. With A=bB, the inverse/adjugate formulas were checked entrywise against A using exact rationals, avoiding the author's Gaussian-elimination routine. They reproduce U,V and the full finite schedule.

## 3. Gap, confidence and radius

The parameters n=k=16, ell=9, w_B=r_B=81, s²=2*81², tau2=512, t=4608 and sigma=214990848 satisfy the squared completion inequality sigma²>=4t²s²kn ell². The supplied q exceeds n sigma.

Using pi>3 and e>2, the theta bound follows explicitly from

    theta_A < 2*2^(-182)/(1-2^(-546)) < 2^(-180).

The leakage bound is at most2^(-8)*288/287. Combining the stated source tail, eta_A, two bridge terms, THREE kn nu terms and TWO eta_cap terms gives exactly the rational loss reported by v3. Independent recomputation confirms1/16-loss>1/32. Thus delta=1/32 is compatible with the conditional pointwise recovery-success premise epsilon_rec>=1/16. The capped comparator remains approximate.

For h0=81/65536, w_C^7 h0>1 and16q<2^68 imply a0>2^(-68), hence S<544. Kappa4096 exceeds every declared C8 floor, including the separate confidence floor for zeta=2^(-74). The strong inequality3w_C<q/(8D) already makes the residual exponential condition hold.

The exact loop formulas yield the same600-bit Q_*. The rational ratio8n/epsilon0 is below2^691, so its natural logarithm is below691. This bounds the SPECIFIED a=Up(sqrt(log(8n/epsilon0)/pi))+1 by128 without redefining Up or executing an exact-real ceiling. Choosing v0=1024 satisfies the allowed inequality v0>=2sqrt(n)a. Therefore d0=81/2^26, d=d0/4=81/2^28 and d²=6561/2^56. Since97^(1/16)<2, lambda_1(qJ^-1)>q/8>d0=4d. Both C8 uniqueness and F's stronger separation hold.

## 4. Recomputed finite resources and error

The independent exact calculation reproduced:

| Quantity | Value |
|---|---:|
| W | 64 |
| log2 H | 179 |
| log2 N | 267 |
| signed coordinate bits b_u | 2823 |
| m | 45168 |
| p_g, p_ph | 100,123 |
| R_g, R_ph | 16777216,7872 |
| M_ph | 379503424 |
| B_len, A_eval | 859028,863357 |
| G0 bit length | 1627 |

The complete G0 integer equals v3's value, not just its bit length. Decoder code remains an input: total execution count is G0+4S_dec+m+2r_dec, with at most2Q_* executable coherent Rec traversals per output. No Rec runtime or source-hardness premise is inferred from these numbers.

At n=16, tau_n<2^(-40), c_n=2^(-256), so E_n<6*2^(-20)+2^(-40). The separately chosen C8 confidence gives p_BDD<=17zeta/16<4zeta and2sqrt(p_BDD)<4*2^(-37). With epsilon=2^(-40), the exact rational upper bound is

    3145745/549755813888 < 2^(-17).

This controls the proposed same-J DGS law only under the stated bounded executable Rec premise and main finite theorem. It does not assert security of this small explicit instance.

## 5. Reserved independent computation and final scope

Root authorized RF4-PARAM-FV2, one foreground job at most10s and64MiB, after the v3 freeze. The independent [script](RF4-PARAM-FV2.py) passed328 exact assertions, exited0 in0.03s wall/user, and used peak16,384KiB RSS; stderr is empty. [Input](RF4-PARAM-FV2-input.json), [command](RF4-PARAM-FV2-command.sh), [stdout](RF4-PARAM-FV2.stdout), [stderr](RF4-PARAM-FV2.stderr) and [resources](RF4-PARAM-FV2.resources) are preserved. Reservation was released immediately. There was no randomness, floating-point scientific calculation, Rec invocation, BDD walk, Gaussian sampling or quantum circuit execution.

The distinct purpose was to catch inconsistent parameter binding and encoding, and to check the basis/resource values with a different algebraic implementation. It was not a repeated execution of the author's control.py. Both recorded objections now pass their new regression checks.

This supplies one nonempty finite conditional compatibility witness. It does not change q as a function of an arbitrary input ideal, assume an average-over-ideals recovery promise, or fill the open standard-family edge. The main review remains favorable at its original supplied-J scope, and the project's computational-foundation goal remains unresolved.
