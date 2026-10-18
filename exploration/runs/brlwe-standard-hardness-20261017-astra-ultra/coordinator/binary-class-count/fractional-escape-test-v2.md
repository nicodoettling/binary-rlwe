# Fractional-ideal escape and its scale, first test v2

PROVISIONAL revised R2 endpoint test. The standalone v1 scale gap is preserved in fractional-scale-gap-before-v2.md; v2 adds explicit parameters and a specified radius, without changing the source law. The frozen integral binary-collision theorem intentionally does not cover fractional ideals. This file tests one genuine escape; it does not extend that theorem by assertion and does not import the integral-only A/C theorems onto changed lattices.

For any integral ideal I and known nonzero a in I, the fractional representative J=a^-1 I contains1. It therefore has binary collisions and the same ordinary ideal class as I. Thus the integral-class conclusion would be FALSE if its word integral were deleted. But J^-1=a I^-1 is integral: a belongs to I, so every a b with b in I^-1 is in R. A narrow Gaussian on this multiplier lattice has short ordinary integer representatives and no hidden denominator. This is an explicit endpoint issue, not a proof that all fractional representatives fail.

A less trivial padding candidate retains denominators from an independent integral ideal H. Let P be a degree-one prime ideal of norm p in a power-two cyclotomic ring of degree n, let H be integral with norm D_H and gcd(p,D_H)=1, and put

    J=P H/p,        Lambda=J^-1=p P^-1 H^-1.

Since pR is contained in P, H is contained in J. Consequently any binary collision in H survives in J, while the ordinary class of J is[P][H]. This can change the large class component without an integral representative and is not excluded by the class-count theorem. The multiplier lattice satisfies Lambda contained in H^-1. The exact formal source is k iid D_(Lambda,s) modulo qLambda, mapped by natural rational reduction to R/qR, versus k iid uniform R/qR, for q prime to pD_H. These are different planted points from D_(H^-1,s); the distinction cannot be dropped. Natural reduction is a bijection Lambda/qLambda -> R/qR because all rational invariant factors are q-units. All ordinary lattice/ideal metadata must be identical in the two worlds. No short basis or conditional sampler is supplied.

Its covolume is p^(n-1)/D_H. For every nonzero x in Lambda, the integral ideal xJ has norm at least one, so

    |N(x)| >= p^(n-1)/D_H,
    ||x||_coeff >= R0 := p^(1-1/n)/D_H^(1/n).

The second inequality is AM-GM in the canonical embedding. Hence a narrow centered Gaussian on Lambda collapses near zero. An explicit bound follows by packing shells of radius R0: the number of lattice vectors in the shell[jR0,(j+1)R0) is at most(2j+3)^n. If pi(R0/s)^2>=2n log5, then

    rho_s(Lambda minus{0}) <= 2 exp(-pi R0^2/(2s^2)).

Indeed log(2j+3)<=j^2 log5 for j>=1, and the remaining Gaussian series is bounded by twice its first term. The centered zero weight is1, so planted Pr[A=0] is at least1 minus this bound; additional nonzero lattice points reducing to0 only increase it. The uniform comparator has Pr[A=0]=q^-n. Thus a one-sample zero test has gap at least

    1-2 exp(-pi R0^2/(2s^2))-q^-n.

This is a provisional elementary estimate, not a hardness claim. It uses the full discrete source and its centered normalizer. A large index in Lambda is not silently assumed to yield a rich Gaussian.

Exact finite falsification control: n=2, R=Z[i], P=(2+i), p=5, H=R gives Lambda=(2-i)R and R0=sqrt5. Choose s^2=pi/(2log2). On the finite nine-point subset(2-i)(a+bi), a,b in{-1,0,1}, the Gaussian weights are exactly1024^(-a^2-b^2), with normalizer(1+2/1024)^2. Its nonzero mass is exactly1-(512/513)^2, less than the proposed full-law bound1/16. This finite conditional control does not prove the infinite tail bound. The full estimate above follows from the explicit shell series, not extrapolation from nine points.

Finally grant, only for a favorable scale diagnostic, an extension of the current pointwise GP->BDD->DGS chain to this fractional J at coefficient Gaussian width

    W_J=n q/(sqrt2 d0),   d0=delta sqrt(n) w_B/(32 n k v0),   w_B<=s.

This extension is not accepted here. For this favorable scale diagnostic impose explicitly n>=2, k>=1,0<delta<=1,a>=1,v0>=2sqrt(n)*a, and q/s>=1. These are the relevant lower-bound conditions from the current chain, now stated rather than imported silently. The formulas give W_J>= (32/sqrt2)n^(3/2)k v0 q/(delta s)>=32sqrt2 n^2>1.

Use the specific coordinate-tail radius B_J=W_J sqrt(n) L_tail for a chosen L_tail>=1. For an exact centered discrete Gaussian on J at coefficient width W_J, the translated Gaussian-sum maximum implies E exp(t X_i)<=exp(t^2 W_J^2/(4pi)); Chernoff and a union bound give Pr[||X||_2>B_J]<=2n exp(-pi L_tail^2). Any sampler TV error is additionally subtracted. This is the actual certified radius being discussed, not a universal claim about all possible radius bounds. Nonzero-output success is a separate obligation; zero collapse is not waived.

To turn an output x in J into a vector of P by the available direct integral map, output p x in P H contained in P. The specified radius becomes p B_J>p. The public integer p itself lies in P and has coefficient norm p. Thus the search guarantee certified by this tail bound and direct clearing map is already met by a public vector. This does not prove that the sampler never outputs a much shorter vector or that a sharper extraction/radius analysis is impossible. The limited diagnosis is that these particular certified bounds do not establish a nontrivial worst-case application.

If H is principal with a supplied short generator f, the relation f in H contained in J also supplies a short known source test via fA in R. Choosing a hard-looking H without such advice is not a hardness foundation by itself. The candidate has exposed two separate requirements: avoid Gaussian zero collapse and extract a useful vector of the original P without paying the full rational clearing factor. Neither is solved by its exact class/containment identities.

No external algorithm, new service or experiment was run for this note. The original source-family foundation remains unresolved. Next useful discriminator is a class-changing or fractional extraction map with a submultiplicative clearing cost, not another unqualified change of ideal notation.
