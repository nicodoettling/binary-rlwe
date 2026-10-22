# FF3-TWOSECRET-v1: exact residual-coordinate modulus transfer

PROVISIONAL author candidate, finite-law identity. This theorem covers a secret set of size TWO in any finite ring when the secret difference is a unit. It is not the full binary-cube theorem.

Let R_Q,R_q be finite commutative rings of respective cardinalities N_Q,N_q. Pick two source secrets s0,s1 with s1-s0 a unit of R_Q, and two target secrets t0,t1 with t1-t0 a unit of R_q. Let nu_Q and nu_q be arbitrary probability distributions on the respective rings. Assume an explicitly given Markov kernel H:R_Q→R_q maps uniform to uniform and nu_Q to nu_q exactly. Neither H nor the algorithm receives the unknown secret label i in {0,1}.

For a source pair(a,b), form u=b-a*s0 and v=b-a*s1. Draw u' from H(u,·), v' independently from H(v,·). Solve

    c=(u'-v')/(t1-t0), d=u'+c*t0.

If a is uniform and b=a*s_i+e, with e~nu_Q independent, the output has EXACT law: c uniform, d=c*t_i+e', with e'~nu_q independent of c. If(a,b) is independent uniform, then(c,d) is independent uniform. Independent executions preserve arbitrary sample counts with one common label i. Any product structure in nu_q is preserved as its full joint law, not inferred from moments.

The computation uses two H calls and ring arithmetic per sample. Thus its cost is polynomial whenever those operations and H have polynomial implementation cost. This is a genuine normalized secret-independent kernel. For coefficient-binary ring secrets in dimension n>=2, restricting to only two possible secrets changes the original target experiment; no FF conclusion follows.
