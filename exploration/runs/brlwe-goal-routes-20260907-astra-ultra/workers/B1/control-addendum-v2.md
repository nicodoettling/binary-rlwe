# B1 additional exact controls, v2

The separate frozen [v2 script](exact-controls-v2.py) and [output](exact-controls-v2.json) supplement, and do not replace, v1. The coordinator allocated one <=30s slot; the script completed in 0.061 seconds with standard-library exact rationals. The prelaunch cap snapshot is [cap-before-exact-v2.json](cap-before-exact-v2.json).

For n=4,q=5,f=2,N=2,k=1, the exact packing enumerated every one of the 25 original ideal points, all 25 active quotient coordinates, 400 source point/noise combinations, and the 625-element full coefficient-space bijection. Independently assembled packed and direct original-ring noisy source count tables agree exactly. Noise in this finite control has independent coefficient fair bits; the algebraic proof covers any iid coefficient noise law, including the stated Gaussians.

The new conditional control uses independent G mod5 coordinates with probability vector (2,1,1,1,1)/6, so Y=S+G has nontrivial secret-dependent posteriors. The length-2 block distance is 23/90. For n=4,f=2 the full distance is 431/1080, below the nonvacuous product bound 2*(23/90)=23/45<1. Exact posterior factorization was checked for all 10,000 positive joint entries, always using the SAME retained Y coordinates. This adds a targeted check beyond the v1 structural toy whose bound was vacuous. Neither toy certifies the Gaussian asymptotics.
