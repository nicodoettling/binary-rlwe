# RF3 exact recheck of fractional endpoint v2

Reviewed input: fractional-escape-test-v2.md, SHA256 9eac55c5c0e824d56dead42f31a6e273cf670d5a943220263f00e455d18520ec. I read the complete v2 note, its exact v1-to-v2 diff, the preserved gap record, and its freeze record. This is a narrow recheck requested by the coordinator, after the main binary-collision theorem review was complete.

Verdict: **the repaired explicit scale implication and specified Gaussian radius pass**. The exact endpoint algebra, zero-test estimate, and finite hand control are unchanged and retain the favorable mathematical assessment in fractional-endpoint-review-v1.md. The hypothetical GP-to-BDD-to-DGS extension itself remains unproved, as v2 says. This report does not certify a hardness reduction or every informal remark in the note. V1's standalone scale guarantee remains rejected, and its counterexample is preserved.

The only mathematical change relevant to the repaired width conclusion is the now explicit set of bounds

    n>=2, k>=1, 0<delta<=1, a>=1,
    v0>=2 sqrt(n) a, q/s>=1, 0<w_B<=s.

The old tuple v0=1/1024 at n=2 now violates v0>=2sqrt(2), so it cannot enter the new claim. Direct substitution yields

    W_J=(32/sqrt(2)) n^(3/2) k v0 q/(delta w_B)
        >=(32/sqrt(2)) n^(3/2) * 2sqrt(n)
        =32sqrt(2)n^2>1.

The chosen radius is B_J=W_J sqrt(n) L_tail for L_tail>=1. This is one explicit certificate, not a claim about every possible radius bound or the actual shortest sample.

I independently checked the new tail statement for an arbitrary full-rank coefficient lattice J, including fractional J. With rho_W(J-c) the translated Gaussian sum, Poisson summation gives

    rho_W(J-c)
      = (W^n/det J) sum_(y in J*) exp(-pi W^2||y||^2)
                         exp(2pi i <y,c>)
      <=rho_W(J).

The final inequality follows by the triangle inequality because the unshifted dual coefficients are nonnegative; the sum itself is real and nonnegative. Completing the square therefore gives, for every real t,

    E exp(t X_i)
      = exp(t^2 W^2/(4pi))
        rho_W(J-(tW^2/(2pi))e_i)/rho_W(J)
      <=exp(t^2 W^2/(4pi)).

No smoothing hypothesis or coordinate independence is needed. Chernoff with t=2pi L_tail/W bounds either coordinate tail by exp(-pi L_tail^2). If ||X||_2>W sqrt(n) L_tail, at least one coordinate exceeds W L_tail in absolute value. A union bound gives exactly

    Pr[||X||_2>B_J]<=2n exp(-pi L_tail^2).

For a sampler at total variation distance eta from the exact centered law, this failure upper bound increases by eta, equivalently subtracting eta from the success lower bound. At L_tail=1 the displayed bound may be vacuous for large n; a desired failure epsilon is obtained by choosing L_tail>=max(1,sqrt(log(2n/epsilon)/pi)). This only increases the certified radius. A nonzero output is still a separate condition, so the zero-collapse regression is respected.

Finally x in J implies p x in PH subset P, and ||p x||_coeff=p||x||_coeff. Thus the chosen radius becomes pB_J>p. The nonzero public vector p belongs to P and has coefficient norm p. The specific radius guarantee after this direct clearing map is therefore already satisfied by a public vector. This verifies precisely the limited scale diagnosis in v2. It does not prohibit shorter actual outputs, a sharper radius certificate, or a different extraction map.

FEP-3 from fractional-endpoint-objections-v1.md remains a boundary on this review: the unchanged final phrase about a supplied short generator is not quantitatively certified as a distinguishing claim without a stated concentration/separation parameter. It is not used in the endpoint algebra, Gaussian-zero bound, or repaired direct-clearing diagnosis reviewed here. I do not broaden the assignment to establish such a test.

No new experiment, external source, subagent, session, or service was used. The main theorem/proof hashes remain unchanged. The assignment is complete; final project integration and acceptance remain with the coordinator.
