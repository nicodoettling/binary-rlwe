from pathlib import Path
import json,datetime,hashlib,re,sys
sys.dont_write_bytecode=True
from exploration.runner.resilience import snapshot,write_json
r=Path('/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-goal-routes-20260907-astra-ultra')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
cap=json.loads(Path(json.loads((r/'launcher-run.json').read_text())['cap']['status_file']).read_text())
refs=[('RB1','criticism/RB1/blind-report-v1.md'),('RF1','criticism/RF1/report-v1.md'),('RS1','criticism/RS1/report-v1.md')]
reviews=[{'reviewer':id,'path':p,'sha256':hashlib.sha256((r/p).read_bytes()).hexdigest(),'disposition':'PASS in expressly stated scope'} for id,p in refs]
scientific='''A new conditional search-hardness implication has passed full mathematical, blind, and source review: assuming pseudorandomness of the exact two-point nonbinary hidden-ideal source below, coefficient-binary rank-one RLWE recovery from **one or two samples** is hard for uniform probabilistic polynomial-time algorithms, at polynomial modulus and with negligible reduction loss. Final acceptance is pending the ledger-scope repair recheck and delivery audit. This does **not** resolve the original polynomially-many-samples recovery question.

## Exact source, target and computational premise

Let n grow through powers of two, ell=ceil(log2 n), and R_q=F_q[X]/(X^n+1). Write D_t(k)=exp(-pi k²/t²)/Z_t on the integers. The source **Base2(n,q,d)** chooses a uniform d-subset T of the n CRT roots once; conditional on T, it chooses U_1,U_2 independently and uniformly in the ideal I_T supported on T, including zero coordinates. It independently chooses all 2n integer coefficients of F_1,F_2 from D_ell and publishes (U_1+F_1,U_2+F_2) modulo q. The comparator consists of two independent uniform R_q elements. The challenger supplies one pair and no oracle, support, witnesses, binary secret, correlated completion or target responses.

The explicit computational hypothesis is that these two source worlds are indistinguishable by every uniform randomized polynomial-time test, for the separately selected parameter family below. It is **assumed, not proved**. The source specializes the same-hidden-ideal noisy-point problem motivated by Order-LWE Section 7; its exact comparator and shared-ideal law are made explicit using that paper's final hybrid. Its polynomial modulus and small noise are additional parameter choices for the assumption, not a worst-case or standard-RLWE consequence proved by the cited paper. Coefficient D_ell agrees exactly with canonical spherical width sqrt(n)ell by Parseval. See the [source review](criticism/RS1/report-v1.md) and [source comparison](source-comparison.md).

For each fixed m in {1,2}, the target chooses independent uniform a_1,...,a_m in R_q, one common uniform coefficient-binary S in {0,1}^n, and **fully independent** coefficient D_sigma_m errors E_i, jointly independent of S and the multipliers, where sigma_m=2sqrt(m)n ell³. It publishes ((a_i,a_iS+E_i))_i. Success means returning the actual sampled S, not merely any residual-consistent secret. The solver gets no additional samples.

## Finite implication and costs

For every target solver Q with exact success epsilon_m, the source test B_m uses its single supplied source pair as the first m multipliers, samples its own independent S and target errors, invokes Q once, and accepts exactly when Q returns that S. For m=1 it ignores the entire second source component. With absolute source distinguishing advantage,

    epsilon_m <= Adv_Base2(B_m)
                 + q^d ((1+D_ell(0))/2)^n + eta_N + delta_F,m.

All constants are explicit. Put

    kappa(t) = 2 sum_(j>=1) exp(-pi t j²),
    Delta_N = (1+kappa(3ell²/4))^n - 1,
    eta_N = min(1, Delta_N/(1-Delta_N)) if Delta_N<1,
            1 otherwise,
    delta_F,m = min(1, mn exp(-pi ell²)/(pi ell)).

For a finite implementation, add xi_source+2xi_alg+xi_target. These are total-variation errors for the full planted pair, the entire challenge-independent local (S,E) sampler, and the target witness/transcript law respectively; the source comparator is exact uniform. An approximate comparator requires its own additional error. One can choose xi_alg<2^-n with bounded polynomial runtime. The exact theorem is [theorem-only-v2.md](candidates/search/theorem-only-v2.md); complete derivations are the [proof](candidates/search/proof-v1.md) and [sampling/dimension supplement](candidates/search/supplement-v1.md).

Beyond the one Q call, B_m uses n fair secret bits, mn independent Gaussian coefficient draws, m ring multiplications and additions, and a canonical equality check. At these parameters, a shared table with O(n²ell³) entries and O(n+log n) probability bits gives the stated Gaussian approximation; naive ring multiplication uses O(n²) modular operations per sample. The total bit complexity is polynomial in the security parameter n. No source sampling, hidden-ideal recovery, matrix-Gaussian sampler, G sampler or completion oracle is executed by B_m.

## Fixed asymptotic parameter families

Choose **q(n) as the least prime congruent to 1 modulo 2n³**. The checked Xylouris least-prime theorem gives

    2n³+1 <= q <= C(2n³)^5.18 <= n^16 eventually,
    q/sigma_m >= n eventually.

This is one specified polynomial-modulus sequence, not a conclusion for every polynomial q. Deterministic progression enumeration with trial-division primality testing, and even exhaustive public root enumeration, run in polynomial time in unary n under this bound. Input length is O(n log n); no practical parameter threshold or benchmark is asserted.

Either of the following concrete, polynomial-time computable choices supports the consequence, **under its own Base2 hypothesis**:

- d(n)=floor(sqrt(n)/ell^4), eventually positive;
- d(n)=floor(n/(64ell)), eventually positive.

Both eventually satisfy d<=n/(64ell). Since D_ell(0)<=1/ell,

    q^d ((1+D_ell(0))/2)^n
       <= 2^(-3n/4+n/(ell ln 2)) <= 2^(-n/2) for ell>=6.

The completion and mask-tail losses are exp(-Omega(log² n)), hence negligible against every fixed inverse polynomial. Widths, modulus sequence, d and sampler precision are fixed before the adversary. Therefore every uniform PPT target solver has negligible exact recovery under the chosen source premise. The implication has a full asymptotic negligible-success conclusion; it is not limited to a promised advantage exponent. See the [parameter table](parameter-table.md).

The general entropy interval in the frozen theorem is purely conditional. It does not assert plausible source hardness at every d, and merely computable d does not imply efficient setup. In particular d=1 has a polynomial distinguisher: enumerate n*q ideal points using the first source component and test a coefficient residual box. Its planted acceptance is 1-negl(n), while uniform acceptance is at most nq(2ell²+1)^n/q^n. The reviewed existing ATT method also gives a polynomial source attack at d=O(log n); for the two displayed growing choices its exp(O(d)) bound is superpolynomial. This bounded attack comparison supplies no proof of the remaining source hypotheses.

## Why the argument closes its analytic obligations

On the event |F_i,j|<=ell², stack the integer negacyclic multiplication matrices into M of shape mn by n. Then ||M||²<=mn²ell^4. For proof-only G~D_ell^n, choose H conditional on F as the exact integer Gaussian with positive exponent matrix B=sigma_m² I-ell²MM^t, independently of S,G. Completing squares and using a normalized Poisson sum gives the full retained-source comparison MG+H versus the iid mn-dimensional target error, with exactly eta_N. The normalizer and the piecewise guard are retained. For two samples the off-diagonal blocks of B are essential; Gaussian marginals alone are insufficient.

After retaining S in that comparison, reveal source coins and H only in the completed world. They are independent of (S,S+G). The completed transcript is determined by these variables, S+G and one quotient of S with at most q^d values. Revealing this quotient multiplies average guessing probability by at most q^d. The exact unwrapped noisy-bit probability is ((1+D_ell(0))/2)^n; wrapping can only reduce it. This argument needs no uniform quotient, invertible ideal point or extractor. The Gaussian completion is proved directly in the [rectangular note](coordinator/rectangular-completion-v1.md) and frozen proof, so no historical analytic certification or unimplemented conditional source sampler is assumed.

The lossiness/projection idea has ancestry in ordinary entropic LWE. The new implication here is its explicitly stated ring-source specialization, exact-witness recovery test, discrete joint completion, and one/two-sample parameter consequence. The [source referee](criticism/RS1/report-v1.md) compares the checked primary papers and repository outcomes; this is a claim of a new implication in that checked record, not an exhaustive literature-priority claim.

## Review, retained evidence and remaining scope

The [blind report](criticism/RB1/blind-report-v1.md) was frozen and hashed before any proposed proof or prior objection was disclosed, and independently reconstructs the finite and asymptotic argument. The [full mathematical report](criticism/RF1/report-v1.md) checks the exact proof/supplement, probability laws, constants, finite sampler, primary prime import and all historical regression IDs. The [source report](criticism/RS1/report-v1.md) checks the primary HLBDD interpretation, concrete parameter effectiveness, source attacks and scientific scope. These are complementary same-model reviews, not independent statistical confirmation or formal verification. Frozen author status headers are preserved; the current [ledger](claims.json) and [reconciliation](reconciliation.md) control disposition.

The delivery review found an imprecise modulus clause in A-PPT ledger v1. That exact version and its [failure of the broader bound substitution](coordinator/A-PPT-ledger-v1-scope-defect.md) were saved before repair. Ledger v2 names the exact least-prime family; the theorem and proof bytes did not change. Fresh parameter recheck and final delivery disposition are tracked in reconciliation.

Exact controls include 1,560 rational rectangular identities, 11,664 full-product probability models, 64,152 arbitrary-leakage models, 712 small ideal tuples, rare/posterior branches, actual-witness interfaces, dyadic rounding and the cached-prefix counterexample. Qualified Gaussian numerical sums remain diagnostics, with tails and floating-point limitations recorded. All code and original results are retained in the [experiment registry](experiments/registry.json). Historical records, including rejected probability claims, are preserved by [complete provenance hashes](imports/historical-file-index.json) and [regression dispositions](regressions.json). Finite tests do not establish asymptotic hardness.

Only A was selected for detailed development before the 50-minute boundary. [B partial splitting](workers/B1/final.md) preserves an exact packing/algebra candidate with an explicit 2f-source-point budget; [C computational transfer](workers/C1/final.md) preserves a larger-modulus decision candidate and scoped obstructions. Both remain provisional and deferred under [selection.md](selection.md). They are not dependencies of the search result.

The original polynomially-many-samples problem remains open. No target decision hardness, standard-RLWE or worst-case source reduction, quantum/nonuniform security, practical bit-security estimate or efficient hidden completion sampler is established. A useful future test is a rigorously budgeted extension to more independent source points, or a source-hardness justification at the concrete growing d. Future work requires a new user decision after this capped service ends; no automatic restart is authorized.
'''
identity='\n## Service, goal and preservation record\n\nSession/goal thread: `01a07dcb-40ad-7231-8540-1675639ae41b`. The exact native objective and creation receipt are in [goal-created.json](goal-created.json). No token budget was requested. The goal is still active at this delivery-preparation checkpoint.\n\n'
identity+='\n'.join('- '+k+': '+str(cap[k]) for k in ['service','started_at','wrapup_at','graceful_shutdown_at','scheduled_kill_at','hard_deadline_at'])+'\n'
identity+='''
Initial Git revision was `174e0a2ca47dcb1e09ba8c5ae48117b698e2f2ed` on main, with an existing HANDOFF modification and untracked plan/run directories; exact intake worktree evidence is in [intake-verification.json](intake-verification.json). No research, literature, historical run, runner code or Git history was edited. All 1,902 indexed historical files passed the interim preservation check. HANDOFF and run-config received external launch-state updates after intake, matching a 21:37:37 startup receipt; both observed states, unchanged approval/cap identity and the initially failed preservation checks are retained in [metadata-change-observation-v1.json](coordinator/metadata-change-observation-v1.json). The coordinator did not overwrite them.

[Operational notes](coordinator/operational-notes.md) disclose late checkpoint intervals, two imperfect local assignment archives and restricted host-service visibility. A1's locally paraphrased scope and C1's altered heading are preserved, with later clearly dated exact-scope addenda; no missing original plaintext archive is reconstructed. The cap sidecar, fresh worker heartbeat and populated cgroup are available, while host service inspection is restricted. Actual launcher exit and descendant cleanup remain unobserved by this coordinator. File consistency checks certify saved-artifact consistency only; mathematical disposition comes from the claim-specific reconciliation.
'''
for name,body in [('final.md',scientific+identity),('resume.md','# Self-contained resume checkpoint\n\n'+scientific+identity+'\nCurrent frontier: RP1 fresh ledger repair recheck and RD1 delivery audit. Do not create another goal or resume after the cap. Read native goal state, exact cap sidecar, claims.json and this checkpoint before scheduling. Authorization covers only this still-live service.\n')]:
 p=r/name;t=p.with_name(p.name+'.tmp');t.write_text(body+'\nPrepared '+now+'\n');t.replace(p)
(r/'coordinator/delivery-scientific-v1.md').write_text(scientific)
c=json.loads((r/'claims.json').read_text());c['updated_at']=now;c['mathematical_reviews']=reviews;c['delivery_gate']='RP1 repair recheck and RD1 delivery review pending'
for x in c['claims']:
 x['proof_sha256']=hashlib.sha256((r/x['proof']).read_bytes()).hexdigest()
 if x['id'] not in ['B-SPLIT','C-LARGE-Q','C-SPAN']:
  x['reviews']=[v for v in reviews if v['reviewer'] in (['RF1','RS1'] if x['id'] in ['SOURCE-2','PRIME-POLY'] else ['RB1','RF1'])]
  x['mathematical_review_disposition']='PASS for stated scope; final acceptance pending remaining gates'
write_json(r/'claims.json',c)
a=json.loads((r/'agents.json').read_text());a['updated_at']=now
if not any(x['id']=='RP1' for x in a['workers']):a['workers'].append({'id':'RP1','task':'/root/r_parameter_recheck','status':'running','role':'fresh repaired-ledger/parameter recheck','ownership':'criticism/RP1','deadline':'2026-09-07T22:42:00Z','model':'gpt-6-astra','reasoning_effort':'ultra','fork_turns':'none'})
write_json(r/'agents.json',a)
historical=json.loads((r/'imports/latest-regressions.json').read_text());rows=[x for x in (r/'criticism/RF1/report-v1.md').read_text().splitlines() if x.startswith('|')]
application=[]
for x in historical['controls']:
 matches=[v for v in rows if re.search(r'(?<![A-Za-z0-9_-])'+re.escape(x['id'])+r'(?![A-Za-z0-9_-])',v)]
 application.append({'id':x['id'],'historical_entry':x,'current_evidence':'criticism/RF1/report-v1.md section8','current_application_rows':matches,'status':'RECONCILED_APPLICABILITY' if matches else 'MAPPING_PENDING'})
reg=json.loads((r/'regressions.json').read_text());reg['updated_at']=now;reg['historical_application']=application;reg['source_qualification_evidence']='criticism/RS1/report-v1.md section5';reg['new_records'].append({'id':'A-PPT-LEDGER-SCOPE','rejected_version':1,'repair_version':2,'status':'FRESH_RECHECK_PENDING','evidence':'coordinator/A-PPT-ledger-v1-scope-defect.md','repair':'coordinator/A-PPT-ledger-v2.json'})
for x in reg['new_records']:
 if x['id']=='SOURCE-SMALL-D':x['evidence']='criticism/RS1/report-v1.md';x['status']='EXACT_HAND_COUNTEREXAMPLE_REVIEWED';x['independent_evidence']='criticism/RF1/source-d1-limitation-v1.md'
write_json(r/'regressions.json',reg)
rec='''# Reconciliation of exact current claims

All three initial mathematical/source review gates pass the unchanged theorem-only-v2, proof-v1 and supplement-v1. Final acceptance remains pending RD1 delivery and RP1 fresh recheck of A-PPT ledger v2. Computational Base2 hardness is an explicit hypothesis, never an accepted source-hardness theorem.

| Current dependency | Exact evidence | Review disposition |
|---|---|---|
| SOURCE-2 v1 | source-and-parameters-v1; exact Base2 definition | RS1 source interpretation/motivation PASS; hardness ASSUMED |
| PRIME-POLY v1 | source-and-parameters-v1; primary Xylouris Thm1.1 | RF1 and RS1 primary statement/substitution/effectiveness PASS |
| NC-RECT v1 | rectangular-completion-v1; proof-v1 sections5–6 | RF1 exact proof and RB1 reconstruction PASS, full joint normalizer and guard |
| A-GUESS v1 | proof-v1 sections1–4 | RF1 and RB1 PASS, source independence, witness TV and single quotient charge |
| MASK-TAIL v1 | rectangular note and proof-v1 section7 | RF1 and RB1 PASS, explicit conditioning and union bound |
| SAMP-E v1 | supplement-v1; proof-v1 section8 | RF1 exact constants and RB1 independent bounded sampler PASS |
| A-FINITE v1 | proof-v1 section7; theorem-only-v2 F/I | RF1 and RB1 PASS, source pair and iid target endpoints |
| A-PPT v2 | exact repaired ledger and unchanged theorem-only-v2 A | Underlying asymptotic theorem PASS; precise ledger repair awaiting RP1 |
| B-SPLIT, C-LARGE-Q, C-SPAN v1 | initial worker notes | PROVISIONAL, deferred and outside accepted dependency chain |

RB1 received only the clean theorem packet and allowed explicit primary theorem, no proposed proof or coordinator verdict. Its complete report froze at22:15:09 UTC, hash c95e83a3a53cd589d2f2bf731ead33b35857af33edea28f1f3a0f8b722061b2d, before any proof disclosure. It reconstructed the same normalized rectangular convolution and guessing argument; it did not independently fetch the least-prime source. RF1 and RS1 performed that primary statement check. The reports are complementary same-model scrutiny, not independent statistical confirmations.

RS1's qualifications are adopted: each concrete growing d is a separate assumed source; generic d includes a d=1 attack; mere computability does not establish setup efficiency. No frozen theorem edit was necessary. RD1 then found overbroad mutable A-PPT ledger wording about polynomial q. Exact v1 was rejected and its failure of proof-bound substitution saved before v2 narrowed the wording to the already-frozen prime sequence. No downstream claim depends on A-PPT; no theorem/proof bytes changed. RP1 receives the exact repair and old failure for a fresh recheck plus targeted exact exponent search.

All40 historical regression IDs are retained in regressions.json, with RF1's exact reproduction or explicit nonuse/applicability explanation. Applicable probabilistic controls include shared-error and pairwise-law failure, witness versus residual success, latent/public projection, guarded normalizers, signed deconvolution and CP1 posterior normalization. The current proof uses no adaptive stage-product, extractor, active-point replacement or source expansion. Old imports remain provisional outside these explicit uses. In particular W3-OBS coordinatorv3/authorv2 retains precedence over its historical header; none of its unclosed analytic dependencies is promoted by this run.

Complete reports and exact input hashes: [RB1](criticism/RB1/blind-report-v1.md), [RF1](criticism/RF1/report-v1.md), [RS1](criticism/RS1/report-v1.md). The [ledger](claims.json), [regressions](regressions.json), [experiment registry](experiments/registry.json) and [frozen evidence manifest](coordinator/frozen-evidence.json) carry exact versions. File checks are administrative, not mathematical certification. Initial artifact-check-interim-v1 failed two external-metadata preservation comparisons honestly; the read-only observation and unchanged launch authority are preserved separately. Historical scientific input hashes all match.

Pending final gates: RP1 exact repaired-ledger report, RD1 delivered-scope report, current accepted graph and fresh artifact check. Goal remains active.\n'''
p=r/'reconciliation.md';t=p.with_name(p.name+'.tmp');t.write_text(rec+'\nUpdated '+now+'\n');t.replace(p)
p=r/'progress.md';t=p.with_name(p.name+'.tmp');t.write_text(p.read_text()+'\n\nUpdate '+now+'\n\nPrepared self-contained final/resume with full source/target law, constants, exact prime sequence, costs and scope. RF1 full review passes; all40 historical controls mapped. A-PPT ledger v1 rejected before scope repair; v2 awaits fresh RP1, while RD1 checks delivery. Session and goal remain active within the original cap; see final.md for exact mirrored identity/deadlines. External startup metadata changes are preserved honestly.\n');t.replace(p)
e=json.loads((r/'experiments/registry.json').read_text());e['updated_at']=now;e['experiments'].append({'id':'RP1-ALLOC','worker':'RP1','status':'allocated','slot':1,'maximum_seconds':120,'description':'fresh exact exponent/parameter regression for repaired ledger'})
for code,result in [('criticism/RB1/finite-controls-v1.py','criticism/RB1/finite-controls-v1.results.json'),('criticism/RB1/finite-controls-v2.py','criticism/RB1/finite-controls-v2.results.json'),('criticism/RF1/exact-search-v1.py','criticism/RF1/exact-search-v1.json'),('criticism/RF1/rectangular-control-v1.py','criticism/RF1/rectangular-control-v1.json'),('criticism/RF1/interface-controls-v1.py','criticism/RF1/interface-controls-v1.json')]:
 e['evidence_paths'].extend([code,result])
write_json(r/'experiments/registry.json',e)
cap2=snapshot(r,kind='capped-goal-coordinator',reason='Prepared full reviewed scientific delivery and40 historical regression dispositions; precise ledger repair and delivery audit still pending',core_only=True)
if cap2['missing_core_artifacts']:raise RuntimeError(cap2['missing_core_artifacts'])
write_json(r/'coordinator-checkpoint.json',{'created_at':cap2['created_at'],'snapshot_directory':cap2['directory'],'reason':cap2['reason'],'scientific_progress_verified':False})
print(json.dumps({'at':now,'snapshot':cap2['directory'],'unmapped_regressions':[x['id'] for x in application if not x['current_application_rows']]}))
