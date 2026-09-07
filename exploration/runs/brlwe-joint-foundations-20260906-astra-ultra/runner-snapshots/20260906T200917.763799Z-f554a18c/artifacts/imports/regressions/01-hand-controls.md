# C03 independent hand controls

No CPU experiment or sampler execution was allocated or performed. These are exact algebraic or analytic checks, including controls that intentionally violate a proposed shortcut's premises.

## HC1: the missing convolution guard

Take input/output dimensions n=p=1, M=0, sigma=1, tau=1/3. Then B=1, Theta=1/9, and MG+H_* has exactly law D_1. Its target TV is zero. Nevertheless

    delta(Theta) >= 2 exp(-pi/9) > 1,

because pi/9<1/2<ln 2. Thus delta/(1-delta)<0. Positive definiteness alone cannot justify the unguarded NC1 v1 ledger sentence. NC1 v2 returns the trivial bound 1 in this case and passes the control.

## HC2: adaptive H_seq is generally different from D_B

Take one input coordinate and two outputs, M=(1,1)^T, tau=1 and sigma^2=3. Then

    B = [[2,-1],[-1,2]],
    L = [[1,0],[-1/2,1]],    D=diag(2,3/2).

The sampler has c_1=0 and c_2=-h_1/2. For v=3/2 write Z_v(c)=sum_k exp(-pi(k-c)^2/v). Poisson summation gives

    Z_v(0)-Z_v(1/2) = 4 sqrt(v) sum_(k>=1 odd) exp(-pi v k^2) > 0.

Thus the second-stage normalizer differs for even versus odd h_1. In particular the exact H_seq probability is proportional to the target quadratic weight divided by a denominator that depends on h_1 parity. It cannot be identified with D_B. The pointwise denominator-ratio proof in F02 handles precisely this effect, and its eta_seq is a necessary separately identified comparison term.

The same matrix provides a cross-sample control. With M unchanged, B has eigenvalues sigma^2 and sigma^2-2tau^2. Setting sigma^2=3tau^2/2 would give positive marginal complements sigma^2-tau^2 but a negative full eigenvalue. This is a continuous Gaussian complement obstruction, not a theorem about arbitrary wrapped laws.

## HC3: actual discrete variance and the obstruction constant

For G~D_t, completing the square gives

    E exp(uG)=exp(t^2 u^2/(4pi)) rho_t(Z-a)/rho_t(Z),
    a=t^2 u/(2pi).

Every cosine term in the Poisson expansion of rho_t(Z-a) is at most its value at a=0. Hence the ratio is at most one. Differentiating at zero gives Var(G)<=t^2/(2pi), with no continuous approximation. Equality is not asserted; as t tends to zero, Var(D_t) is asymptotic to 2 exp(-pi/t^2), whereas t^2/(2pi) is much larger.

The normalized theta product follows by dividing NIST DLMF 20.5.3 at z=pi theta by its value at zero. With r=exp(-pi/t^2), each factor is

    1-[4r^(2j-1)/(1+r^(2j-1))^2] sin^2(pi theta).

The bracket coefficient increases with t; each factor remains positive. Taking limits of finite products proves monotonicity for every finite t>=t_0, without an upper bound on t. This use of the primary identity was checked directly at https://dlmf.nist.gov/20.5.E3.

For |x|<=1/2, the two atoms G=+1,-1 give

    1-phi_(t_0)(x) >= 4 D_(t_0)(1) sin^2(pi x)
                     >=16 D_(t_0)(1) x^2.

Together with 1-phi_sigma(1/q)<=pi sigma^2/q^2 and the 2epsilon bound for a modulus-one test under TV epsilon, this independently reproduces NO1's denominator 16 D_(t_0)(1).

## HC4: finite wrapped deconvolution and moment controls

On Z/5, let r=1/100 and s=1/50 parameterize scalar Gaussian masses r^(k^2) and s^(k^2). Their wrapped laws p=(p0,p1,p2,p2,p1) and t=(t0,t1,t2,t2,t1) satisfy

    p0>.98,  .009<p1<.011, p2<2e-8,
    t1>.019, t2<2e-7.

These follow directly from 1+2r<Z(r)<1+2r+3r^4 and the residue numerators r+r^16+... and r^4+r^9+.... If a completion exists, symmetrize it to (x,y,z,z,y). At residue 2,

    t2=p2 x+(p1+p2)y+(p0+p1)z,

so z<3e-7. The residue-1 equation and x<=1 then imply y>.0079. But t2>=p1 y>.009*.0079=7.11e-5, a contradiction. The contradiction still holds when each target coordinate changes by at most 1e-5: then z<1.1e-5 and y>.0079, while t2<1.02e-5. Thus this is also a fixed-parameter approximate obstruction. It does not refute growing-width approximate completion.

An entirely rational finite-support control is

    mu=(2/5,3/20,3/20,3/20,3/20),
    h=(3/5,1/4,-1/20,-1/20,1/4),
    nu=mu*h=(3/10,17/80,11/80,11/80,17/80).

All nontrivial mu Fourier coefficients equal 1/4, so the inverse is unique. Its ratios are (10+3sqrt(5))/20 at frequencies +/-1 and (10-3sqrt(5))/20 at +/-2, both in (0,1), but h has negative entries. This rejects the positive-ratios-imply-probability shortcut.

For the Renyi control take Q=(1/2,1/2), P=(1/2+epsilon,1/2-epsilon), 0<epsilon<=1/2. Then M_2(P||Q)=1+4epsilon^2. P has decision advantage epsilon against Q; replacing it by Q erases that advantage entirely. Cauchy–Schwarz still gives the valid positive-event inequality Q(E)>=P(E)^2/M_2(P||Q). The useful general TV consequence is only TV(P,Q)<=sqrt(M_2-1)/2.

## HC5: common-K and Gaussian marginal controls

In F_3 take J=0, U_1=U_2=1 and K uniform. The common-K ideal tuple is uniform on three diagonal pairs. Independent ideal points are uniform on all nine pairs. The retained distance is

    (1/2)[3(1/3-1/9)+6(1/9)]=2/3.

This is the specialization of 1-|I|^(1-m). Forgetting U and adding correlated F,H can decrease the distance, so it is not automatically a public source distinguisher.

For independent fair bits S,T and independent Z~D_sigma, set E_1=Z, E_2=(-1)^(S xor T)Z modulo odd q. Every conditional error marginal is the correct wrapped Gaussian, but the pair is not the product target. Given T and a nonzero first residue the sign reveals S, while at zero it does not; guessing is 1-W_sigma,q(0)/2. Without T it is 1/2. MN's full output-law comparison excludes this control by its actual joint law, not by checking covariance alone.

## HC6: adaptive verification and the cached-prefix regression

On a two-atom space let solver success equal the bad-error event, each of probability 1/2. Success and good error never coincide. Multiplication epsilon_rec*(1-delta_T)=1/4 is false for the same input, whereas the subtraction epsilon_rec-delta_T=0 remains valid.

A verified residual property does not establish the planted witness: in F_3, a=b=1 and residual set {0,1} allow both binary candidates 0 and 1. REC uses exact planted success only to lower-bound acceptance and does not reverse this implication.

For the imported CP-1 model, conditioning on vk=1 has normalization 10/11 and gives masses P(A_b)=21/2000, P(C_b)=1/20, P(D)=879/1000. The incidences are .1 at x, .0605 at e_b and .0105 at f_b, with strict heavy threshold .1. The selected two-hit event has probability

    sum_b (21/2000)(1/2)=.0105>.1^2=.01.

The later cached-prefix transfer restricts support and renormalizes branch mass; local residual marginals cannot supply a product bound. F02/R03 instead use exact conditional kernel products and uniform pointwise transition errors on every complete preceding history. Held-out REC multiplies only after conditioning on the entire solver prefix, its tape and S, with freshly sampled errors on every such history. Self-verification uses subtraction. These replacements pass CP-1 for explicit structural reasons.

## HC7: A2 versus A1 leakage scales

Let a=pi C/4. At m=C tau^2 ln n, the per-bit error bound is n^(-a) plus negligible wrapping, and n h_2(error)=O(n^(1-a) ln n). A2 asks for Theta(sqrt(n)/(ln n)^3) quotient bits, so the entropy ratio is O(n^(1/2-a)(ln n)^4), which tends to zero exactly under the stated sufficient strict inequality C>2/pi. At equality this calculation does not tend to zero. Adding (4+epsilon)ln ln n inside the displayed refined threshold supplies the missing logarithmic factor.

For A1, output entropy is Theta(n/(ln n)^2). Taking m=C tau^2 ln ln n instead gives ratio O((ln n)^(2-pi C/4) ln ln n), tending to zero for C>8/pi. Applying that A1 threshold to A2 would be unjustified. Full-S recovery has its separate n exp(-pi m/(4tau^2)) bound; inverse-polynomial failure at fixed C>4/pi is not negligible failure.
