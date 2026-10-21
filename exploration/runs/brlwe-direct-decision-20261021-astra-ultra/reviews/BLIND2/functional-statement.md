# SFUNC-v2: optimal selected-functional guessing

Let J be any full-rank subgroup of Z^n, t>0, S uniform on {0,1}^n, G independent with law D_(J,t), and Y=S+G as an unwrapped integer vector. Fix a nonempty finite family of deterministic finite-valued functions F_1,...,F_m on the cube. A predictor observing Y outputs one index j and one value v, and succeeds when F_j(S)=v. Define p_selected to be the supremum of this success probability over ALL randomized predictors; it is the optimal Bayes success, not the success of an arbitrary chosen predictor.

For each occupied residue c modulo J define

    N(c,j,v)=#{b in {0,1}^n : b modJ=c and F_j(b)=v},
    K_F=2^-n sum_(occupied c) max_(j,v) N(c,j,v).

For every real r0>0,

    K_F <= p_selected
        <= min(1,K_F*exp(pi*n/(4r0))*(1+r0/t^2)^(n/2)).

The lower bound is the exact optimal success using only Y modJ. The upper bound consequently holds for every predictor, including one whose index depends on the full Y. For t=2n^2 ell with ell>=1 and r0=t, the multiplicative overhead is at most exp((pi/8+1/4)/(n ell)).

J and all functions are fixed before sampling. Additional metadata can be revealed only if, conditional on it and J, S remains uniform on the cube and G retains its stated independent Gaussian law. The claim does not provide an algorithm computing K_F, sampling G, or solving a decision problem.
