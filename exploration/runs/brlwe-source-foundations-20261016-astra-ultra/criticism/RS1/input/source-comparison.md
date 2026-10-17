# Source comparison at intake

| Experiment | Input | Comparator | Status |
| --- | --- | --- | --- |
| Base2 | Two noisy uniform ideal points, one hidden uniform T; coefficient D_ell | Two independent uniform ring elements | Explicit unproved computational premise |
| Base_m, m>2 | m independent points and errors conditional on one T | m independent uniform ring elements | Stronger premise unless separately justified |
| Target m=1,2 | Independent uniform multipliers and Gaussian errors, common binary secret | Exact recovery task | Historical conditional A-PPT v2 |
| Known-ideal HLBDD | Must verify primary-source interface | Must verify | Track A pending |

No new reduction, expansion or attack yet. Same-T recovery and public decisional tests are distinct.

| EX-v2 expansion | One original Base2 pair; fresh box mixtures and coefficient D_L additive noise | Full m-output law statistically close to iid uniform, even retaining uniform seed | PROVISIONAL direct proof, fresh blind review in progress |

EX-v2 changes q to least prime 1 mod2n^(h+10) for fixed sample exponent h, with d separately selected. It does not inherit the September source hypothesis or assert the expanded planted law is Base_m. Generic normal-form ring regularity has primary ancestry in LPR 2013 Theorem7.4/Corollary7.5; the proposed contribution is the explicit Base2-to-many-sample recovery composition and parameters, not priority for regularity.
