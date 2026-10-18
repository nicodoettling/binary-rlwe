# Role A first discriminating result v1

Frozen 2026-10-17, before the 20:24:14.894509 UTC checkpoint. All new mathematics is **PROVISIONAL**. Source computational hardness is **OPEN**; the source interface does not complete the run's goal.

## 1. Finite generalized source experiment and reduction direction

The exact statement is admissible-theorem-only-v1.md, with author proof admissible-proof-v1.md. A public challenge X has planted law P and comparator Q; an executable map K outputs metadata V and m multipliers C_j. The full comparator K(Q) must be within delta_cmp of mu_V times m independent uniform ring elements. The planted image has latent decomposition C_j=U_j+F_j with every U_j in one common I_T. The entire latent variable Z (including metadata) is independent of the fresh binary secret and auxiliary D_t Gaussian.

Ideal points may be nonuniform, correlated, zero, or dependent on masks. The ideal prior may be arbitrary, deterministic, or public. Masks may have arbitrary joint law. On a source-only good event, require the complete stacked multiplication norm <=sigma/(2t). The exact weighted leakage charge is E[1_Good min(1,D_Z p_t^n)], where D_Z is the binary-image cardinality of s↦(U_j s)_j and p_t=(1+D_t(0))/2. With bad-event loss delta_bad and normalized completion error eta_t,

    target recovery <= source advantage + delta_cmp + delta_bad
                       + E[1_Good min(1,D_Z p_t^n)] + eta_t.

The wrapper samples its own actual S and target errors, invokes the target solver once, and tests equality to S. The algorithmic direction is target solver => source distinguisher. To reach the run's computational goal, a source distinguisher must additionally imply a solver for the specified standard problem. No such edge is supplied by this interface.

Metadata determined by source latents creates no new planted leakage about fresh S, but its own joint comparator must be checked and it must be publicly available to K. Proof-only H and expansion coins cannot silently be appended to the independent-noise/uniform-output comparator. The statement/proof need the usual regular conditional interpretation for general latent spaces; for all public finite-bit challenges, masks and ideal points may be retained as a countable latent state after integrating continuous sampling parameters out. No positive-mass-state assertion is intended to exclude that integration.

## 2. First exact finite nonuniform/correlated control

Reservation A-finite-1 was granted and completed under 30 seconds wall/256 MiB address-space limits. The exact model and every input are in finite_controls_v1.py and finite_controls_v1.stdout.json; raw stderr is retained. No seed was used because all cases were enumerated. Internal runtime was 0.5759381520329043 seconds and maximum RSS 31,744 KiB. Every exact assertion passed.

The structural finite model is the explicitly labelled coordinate-product ring F_3^4, not an instance of the cyclotomic Gaussian theorem. Choose z=0,1,2 with probabilities 1/2,1/3,1/6, one deterministic public first-coordinate ideal, U_1=z e_1, U_2=2z e_1, and perfectly correlated masks F_1=f(z)1,F_2=2f(z)1 with f(0)=f(1)=1,f(2)=2. Fresh S is uniform binary, G uniform F_3^4, and H=(0,H_2) with H_2 independent uniform F_3^4. For each z, (F_1G,F_2G+H_2) is exactly uniform on F_3^8; this full error law was enumerated.

The actual optimum recovery is exactly 1/16. Revealing the completed-world latent variables and ideal image raises guessing to exactly 3/32, which equals E[D_Z]/16 because D_Z=1,2,2 on the three source states. This is a discriminating nonuniform/correlated-source test: the average cardinality charge is tight, while no uniformity or source-mask independence is used. Replacing allowed metadata by V=S makes recovery one and rejects dropping fresh-secret independence. CP-1 still yields 21/2000>1/100 despite the later conditional factor 21/221<1/10; no forbidden product is used.

This finite-support control verifies the combinatorial/full-law structure, not the infinite Gaussian completion estimate, asymptotic hardness, or absence of attacks.

## 3. Simultaneous usable parameter envelope

parameter-range-v1.md gives the exact inequalities and losses. With auxiliary t=ell=log2 n, the sufficient entropy budget is d log2 q<=rho n for fixed rho<1. A direct m-point source whose coefficient masks have cutoff b0 uses sigma=2 sqrt(m)n b0 ell. For m<=n^h and source width tau<=n^a polylog(n), q>=n^K with K>h/2+1+a+c suffices for q/sigma>=n^c. This is a nonempty analytic parameter intersection at polynomial q, subject to an actual source-hardness theorem and m supplied common-ideal points.

For a two-point source expanded by accepted EX, b0=ceil(tau ell) yields sigma=2 sqrt(m)n ell[2n(L-1)b0+Lell], L=ceil(n sqrt(q)). A sufficient exponent condition is K>h+6+2a+2c. The entropy condition must use the actual q or a valid upper bound. Source errors, source points, standard-RLWE input sample count and target sample count are distinct budgets.

## 4. Concrete obstruction to C's first width-compatible escape

binary-image-obstruction-v1.md proves the following exact algebraic claim: if the union CRT support of U_1,...,U_k has size r and q^r>n^(n/2), their multiplication map is injective on coefficient-binary secrets. A nonzero binary difference v has ||v||_2<=sqrt(n), but vanishing on r roots forces q^r to divide its nonzero determinant, contradicting |det M_v|<=||v||_2^n. For iid uniform ideal points, full union support has probability (1-q^-k)^d; zero branches are retained.

The second exact finite control uses the actual split cyclotomic n=8,q=17. It enumerates all binary secrets and all root subsets. Every d>=3 subset is injective, matching 17^3>8^4. At d=2 the image ranges from 176 to 256, so injectivity can occur even below the sufficient gate.

C's provisional Order-LWE bridge has a largest coefficient principal noise width at least sqrt(2n)q^(1-d/n)w(n)f(n), with w→infinity and f=omega(sqrt(log n)), and rounded continuous elliptical masks sharing one latent parameter. This is NOT an iid coefficient-D_tau source. Under the earlier spherical shorthand tau>=sqrt(n)q^(1-d/n)omega(1), decreasing tau below q already crosses the binary injectivity gate. For the exact law, C is checking a canonical-coordinate small-ball bound: the good stacked-norm event implies a single wide Gaussian coordinate is anomalously small. This supplies a direct bridge from its real mask law to the same obstruction without a spherical replacement. The current artifact records the conditional result and explicitly leaves this norm/probability step pending.

Thus simply increasing d and replacing q^d by the exact binary-image size does not supply an evident repair to C's first route. This is scoped to the full ideal-image revelation used by this completion proof. It does not rule out other source transformations or lossiness methods.

## 5. Remaining obligations and next test

All new statements need nonauthor full/source/complexity and fresh blind reviews before acceptance. A-ADM is an auxiliary interface, not the computational foundation. C must finish its exact primary Gaussian and norm conversion; B must supply a direction-correct source endpoint. The next work is to test those concrete compositions, particularly whether any source can avoid both the small-ideal width obstruction and the large-ideal binary-image injection. No additional experiment is running and no new experiment is authorized without a fresh reservation.

The inherited EX-v2 theorem/proof were read at their accepted hashes; prior full/source/blind/recheck reports and historical regressions were consulted. No historical file was edited, no source-hardness assumption was upgraded, and no model/service/session changes were made.
