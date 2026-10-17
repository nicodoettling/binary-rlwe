# A-H3 author derivation v1

**PROVISIONAL**, no referee or finite control has yet checked this file. Frozen statement: entropy-budget-theorem-only-v1.md. No ordinary RLWE hardness theorem is assumed or imported; the source is only a specified distribution.

All logarithms are natural. Entropy and KL divergence concern finite distributions after coefficient reduction modulo q.

## 1. Source information budget, including zero multipliers

Fix the complete k-tuple a. In CRT coordinate j, the map

    s_j -> (a_1j*s_j,...,a_kj*s_j)

has F_q-rank one unless all k multipliers vanish, when it has rank zero. Therefore the full linear map `s -> (a_i*s)_i` has rank

    r(a) = #{j: (a_1j,...,a_kj) != (0,...,0)}.

Uniform s maps to the uniform distribution on this image, with entropy `r(a) log q`. Independent additive noise cannot decrease entropy on a finite additive group: its convolution is a mixture of translations of that uniform distribution and entropy is concave. The argument conditions on the actual tuple a and requires only independence of the complete source error vector from a,s; it does not require separate error coordinates.

Since the a_i are independent uniform ring elements, the k multiplier coordinates at each fixed j are independent uniform F_q. Thus

    E r(a)=n(1-q^(-k)),
    H(P_k)=H(a)+H(b|a)
          >= k n log q+n(1-q^(-k))log q.

The exact full-uniform input comparator Q_k has alphabet size q^(2kn), so

    D(P_k || Q_k) <= (k-1+q^(-k)) n log q.             (1)

This includes the all-zero multiplier branches without conditioning them away. The input's k ring samples are the entire challenge budget.

## 2. Comparator preservation and output entropy

For any randomized channel K, the log-sum inequality gives KL contraction:

    D(KP_k || KQ_k) <= D(P_k || Q_k).

The exact hypothesis `KQ_k=U(R^m)` turns the left side into `mn log q-H(KP_k)`. Consequently

    H(KP_k) >= (m-k+1-q^(-k)) n log q.                (2)

This step requires exact uniform preservation. Total-variation closeness of KQ_k to uniform alone is not silently substituted; rare comparator outputs can change likelihood ratios.

## 3. Base_m entropy upper bound

The published tuple is a deterministic function of `(T,U_1,...,U_m,F_1,...,F_m)`. Hence

    H(B_m) <= log binom(n,d)+m d log q+m H_F.          (3)

This is an upper bound; overlapping hidden-support representations or modular wrap may reduce output entropy further. All uniform ideal points include zero active coordinates. Independence of the masks gives the sum m H_F, while each conditional ideal-point entropy is exactly d log q. The one common T is charged once.

Equations (2) and (3) imply `H(KP_k)-H(B_m)>=g` with g in the frozen statement.

## 4. TV comparison

On an alphabet of size M=q^(mn), a maximal coupling (X,Y) of KP_k and B_m satisfies `Pr[X!=Y]=epsilon`. Let J be its mismatch indicator. The chain rule bounds

    H(X|Y) <= H(J)+Pr[J=1] log(M-1)
             <= h2(epsilon)+epsilon log M.

Since `H(X)-H(Y)<=H(X|Y)`, the candidate finite inequality follows:

    g <= h2(epsilon)+epsilon mn log q.

The coupling is proof-only and does not assert the public algorithm can see J. No sequential product or posterior-resampling argument appears.

## 5. Explicit Gaussian entropy and asymptotic scope

Let `Z_t=sum_z exp(-pi z^2/t^2)`. Monotonicity on the positive half-line gives `Z_t<=1+t`. Poisson summation gives

    Z_t=t theta(t),  theta(t)=sum_z exp(-pi t^2 z^2).

Termwise differentiation is justified by absolute convergence for t>0. Since theta'(t)<=0,

    (2pi/t^3) E[D_t^2] = (log Z_t)' <=1/t,
    E[D_t^2]<=t^2/(2pi).

Thus the integer Gaussian entropy obeys

    H(D_t)=log Z_t+pi E[D_t^2]/t^2 <=log(1+t)+1/2.

Reduction modulo q is deterministic, and the n coefficient errors are independent, giving

    H_F <= n(log(1+ell)+1/2).                         (4)

For q>=2n^3+1, ell=log2 n and either baseline d family, `d/n=o(1)`, `log binom(n,d)<=n log2=o(n log q)`, and (4) is `o(n log q)`. Dividing the finite inequality by mn log q and using `h2<=log2` proves

    epsilon >= (m-k+1)/m-o(1)

for fixed k,m with k<=m. In particular, two ordinary RLWE samples cannot be converted to Base2 with negligible planted TV while preserving the uniform comparator exactly. An additional ordinary RLWE sample is a necessary budget condition within this precise map class, not a sufficient construction.

## 6. Limits and open gates

The argument does not imply hardness, does not rule out a reduction using three or more ordinary samples to Base2, and does not rule out computational-only endpoint comparisons. The independent local coins of K may be unbounded and its runtime unrestricted, so the impossibility is information-theoretic inside its class. It is valid even for arbitrary source noise independent of a,s. Finite controls and nonauthor review remain required. Historical broad-source entropy obstructions inspired the channel argument; this is a different source/target comparison and its claimed novelty is the explicit ordinary-RLWE sample-budget bound.
