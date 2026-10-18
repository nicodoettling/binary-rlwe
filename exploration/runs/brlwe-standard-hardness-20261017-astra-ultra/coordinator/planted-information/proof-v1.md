# Proof of planted information retention, v1

PROVISIONAL complete author proof of theorem-v1.md. No standard computational foundation is claimed.

## 1. Natural reductions and a source-only denominator ideal

For integralJ, RsubsetLambda=J^-1 andLambda/R has orderD. Sincegcd(q,D)=1, the natural mapR/qR->Lambda/qLambda is an isomorphism. Ifj inJ anda inLambda, thenja inR and j times the natural residue ofa equalsja modqR. This follows by writinga=r+qell withr inR,ell inLambda; thenja-jr=qjell inqR.

Define the integral ideal J_a={z inR: a_i z inR for everyi}. It containsJ. Writev_P(J)=e_P. Sincea_i inJ^-1, at P dividingJ its allowed minimum valuation is-e_P; J_a has valuationmax(0,max_i[-v_P(a_i)]). At P not dividingJ all a_i are integral and J_a has valuation0. Hence J_a differs fromJ only if, for someP dividingJ, everya_i has valuation at least-e_P+1; equivalently all a_i belong toP Lambda. This includeszero samples. Conversely that event makes the exponent of J_a atP smaller thane_P. Thus

    {J_a!=J}=union_(P|J){all a_i inP Lambda}.

This condition needs only generation of the quotientLambda/R, not generation of the entire fractional ideal by the a_i. No asymptotic primitive-Gaussian theorem is imported.

## 2. Exact coset probabilities and generator loss

For every cosetc+R inLambda/R, its Gaussian probability isrho_s(R+c)/rho_s(Lambda). Poisson summation overR=Z^n gives, uniformly in realc,

    rho_s(R+c)/s^n in[1-Delta_s,1+Delta_s].

Both the shifted numerator and the sum over theD cosets are retained. IfDelta_s<1, dividing by the actual sum gives TV at mostDelta_s/(1-Delta_s) from uniformLambda/R. ForDelta_s>=1 use the trivial bound1. Consequently the joint k coset labels are withink eps_s of independent uniforms, by a product hybrid (the source points actually are independent conditionalonJ).

ForP|J, RsubsetP Lambda. The quotient homomorphismLambda/R->Lambda/P Lambda is surjective, and the latter group hasorderN(P), by the ideal-index identity for an invertible fractional ideal. Therefore a uniform coset label lies inP Lambda/R with probability1/N(P). For k iid uniforms the all-in probability isN(P)^(-k). Union overP and the one joint-TV charge show

    Pr[J_a!=J] <= chi_J(k)+k eps_s.

There is only one prime above2, of norm2. Everyoddprimeideal hasnorm>=2n+1, since the image ofX hasorder2n in its residue field. The numberofdistinctoddprimefactors ofJ isatmostlogD/log(2n+1). This gives the displayed explicitbound. Neither statistical bound conditions on a future tail event or assumes independence afterselection.

## 3. Full-law tail bound and exact integer unwrapping

For centered latticeGaussianX~D_(M,u), the shifted-theta maximum gives Eexp(<h,X>)<=exp(u²||h||²/(4pi)). The shift-dependent theta factor isbounded by its centeredvalue, not deleted. Chernoff givesPr[|<v,X>|>=u||v||L]<=2exp(-piL²). For a primitive2n-th root, the realandimaginary evaluation vectors eachhavesquarednormn/2. Therefore

    Pr[|a_i(zeta)|>s sqrt(n)L]<=4exp(-piL²),
    Pr[|E_i(zeta)|>sigma sqrt(n)L]<=4exp(-piL²).

Union overallk samplesandn embeddings bounds failurebydelta_tail. This event isdefined ontheactualjointsource/errorlaw beforeanypostselection and isuniforminJ. It isindependent ofS, although the proofonlyneeds deterministic bounds forallbinaryS.

The coefficient Fourier transform diagonalizes multiplication. Each rowbasisvector has||j_l||_coeff<=tau, while |S(zeta)|<=n for everybinaryS. On the good event,

    ||j_l a_i||_coeff <= tau s sqrt(n)L,
    ||j_l a_i S+j_l E_i||_coeff
       <=tau sqrt(n)L(n s+sigma)<q/2.

Each coefficient absolutevalue isatmostitsEuclidean norm. Both productsareintegercoefficient vectors. The public residues j_l A_i andj_l B_i therefore have unique centeredintegerlifts

    u_il=j_l a_i,
    v_il=j_l a_i S+j_l E_i.

The first norm isalso belowq/2 under the statedstrongerinequality. Strictq avoidscenteredboundaryambiguity. No scalar clearingbyD isused; a shortbasis isusedonlyby the information-theoretic decoder. Allproductsarecommutative ringproducts.

## 4. Unique actual secret on the good event

Fix an arbitrary deterministic choice ofa suitablebasis asafunctionofJ. Thedecodercomputesallcentered u_il,v_il fromthepublictupleand enumeratesbinary s'. It accepts candidates satisfying

    v_il-u_il s' inJ  for all i,l.

ThetrueS passesbecausej_l E_i inJ. If two candidatespass, theirdifferencez satisfies a_i j_l z inJ forallbasisvectorsj_l, hencea_i J zsubsetJ. InvertibilityofJ impliesa_i z inR. Thusz inJ_a. IfJ_a=J, binaryinjectivity moduloJ forcesz=0. ThecandidateisuniqueandthedecoderoutputsS.

This establishes successatleast1-Pr[tailbad]-Pr[J_a!=J], withtheunionbound andcappingat0. Noindependence betweenthesetwoevents isasserted. Basisfindingandbinaryenumerationneednotbeefficient; thesuccesslowerboundsoptimalinformation-theoretic guessing. TheordinaryintegerbasisofJ isenough todefinemembership; theadditionalshortbasismaybeselectedbyfinitesearch becauseexistenceisassumed. It isnotprovidedasshortadvice toan allegedlyefficientreduction.

## 5. Discarding metadata and exact comparator scope

Let J nowberandomwiththe statedcommonbounds. GivenpublicA, thejointsecret/errorlaw isP(S)P(E), independentofJ. Therefore foranypositive-mass(A,B,J),

    P(S=s|A,B,J) is proportional to 2^-n P(E=B-A s modq),

andthisexpressiondoesnotdependonJ. Theentireposterior, henceoptimalguessingsuccess, agreeswiththatgivenonly(A,B), almostsurely. Averagingthepointwiseguarantee proves the hidden-metadata statement. Nullversionsarearbitrary. This isastatisticalconditionalindependencestatementaboutthewrapper's fulljointlaw; itdoesnot giveanefficientway tosimulateJ orfindashortbasis.

Theuniformmultipliercomparator retains exactlytheoriginaltargetsecretanderrorlaw. No claimaboutitsoptimalguessingsuccessisnecessaryorproved. A computationalRec maystillbehavedifferentlybetweenplantedandcomparator. Thus thetheorem onlyrulesoutan information-theoretic planted-lossiness claim belowthislowerbound inthisspecificparameterregime. Itdoesnotruleoutcomputationalreductions,different sources,orotherparameters.
