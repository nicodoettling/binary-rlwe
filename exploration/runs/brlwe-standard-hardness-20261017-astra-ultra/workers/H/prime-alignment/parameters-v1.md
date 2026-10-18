# H-ALIGN: actual A/B/C width substitution

Status PROVISIONAL author parameter check. This companion does not edit the frozen H-ALIGN v1 theorem/proof or change any source, secret, noise, or family premise.

## Exact convention and lower bound

C's `workers/C/periodic-hardness/multiplier-ohcp-theorem-v6.md` explicitly chooses

    v0 >= 2 sqrt(n) a,
    a=ceil(sqrt(log(8n/epsilon0)/pi))+1 >=1,
    d0=delta w_C/(32 n k v0),       0<delta<=1.

It identifies the B coefficient width as w_B=w_C/sqrt(n). The assignment's conditional delivered DGS interface has COEFFICIENT width

    s_J=nq/(sqrt(2)d0).

Therefore, before any asymptotic assumption,

    s_J =16 sqrt(2) n^(3/2) k v0 q/(delta w_B)
        >=32 sqrt(2) n^2 k a q/(delta w_B).             (W1)

The coefficient width is the canonical output width divided by sqrt(n). The displayed v0 floor comes from C's actual finite parameter choice; it is not inferred from a generic smoothing slogan. Increasing v0 to satisfy C's uniqueness gate only increases s_J.

For abstract positive parameters, (W1) proves s_J>=512n^2 whenever

    k a q/(delta w_B) >=8sqrt(2).                      (W2)

This condition must be checked; it is not automatic from merely saying the width is polynomial. An arbitrarily large w_B/q would invalidate such an unconditional inference.

## A's concrete family passes the threshold

Read `workers/A/fractional-composition/parameter-and-finite-bridge-v1.md`. Its complete choice uses

    ell=ceil(log_2(2nk))>=2,
    w_B=ell^2,
    sigma=8n^2 ceil(sqrt(kn)) ell^4,
    q>=8 n^(c+2) ceil(sqrt(kn)) ell^4,     c>0.

Here the symbol w in A's companion is the COEFFICIENT width w_B; it is not C's canonical width. Combining this with (W1) yields

    s_J >=256 sqrt(2) (k a/delta)
               n^(c+4) ceil(sqrt(kn)) ell^2.           (W3)

In particular,

    s_J/(512n^2)
       >= (k a/(sqrt(2)delta))
               n^(c+2) ceil(sqrt(kn)) ell^2 >1

for every stated n>=2,k>=1,c>0,delta<=1,a>=1. Even the weaker substitutions n^(c+2)>=4, ceil(sqrt(kn))>=2 and ell^2>=4 give a right side at least16sqrt(2). Thus the requested threshold follows with substantial slack from the actual A/B/C parameter packet, without an extra v0 or t floor.

The resulting one-step probability bound is

    Pr[0!=X in FI] <=2^(1-rho n)+(16n)^(-n),

with original zero mass retained. A polynomial attempt cap T and total conditional oracle error E_tot give at most T times the displayed expression plus E_tot. This is negligible for fixed0<rho<1 and negligible E_tot. It is not a contradiction to a conditional restricted DGS oracle: it says this particular fresh-sample replacement mechanism almost never descends on these prime inputs.

## Size and premise qualifications

The explicit polynomial-VALUE q choice, polynomial k, inverse-polynomial delta and polynomial-time finite scalar parameters give the intended polynomial absolute width. A's separate polynomial-BIT modulus existence argument permits q with exponentially large value; that alone does not certify polynomial absolute s_J. The lower bound (W3) remains valid there, but claims of polynomial output-vector norm or polynomial approximation must retain the stronger actual magnitude assumptions.

The finite quantum DGS implementation is being checked separately. The algebraic width conversion above is conditional on the assignment's interface and cannot certify the coherent sampler, standard arbitrary-ideal hardness, or the missing family-transfer edge. Every source/comparator law in A and B remains unchanged.
