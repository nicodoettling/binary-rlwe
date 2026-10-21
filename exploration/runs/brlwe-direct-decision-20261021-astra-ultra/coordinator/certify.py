"""One-shot exact-version reconciliation; writes only this run's output."""
import hashlib, json, sys
from pathlib import Path
from checkpoint import OUT, ROOT, atomic, clock_check, checkpoint

def read(p): return json.loads((OUT / p).read_text())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

clock = clock_check()
assert clock['phase'] == 'discovery'
full = read('reviews/FULL2/verdict-v2.json')
assert full['verdict'] == 'PASS_WITH_STATED_SCOPE'
integrity = read('coordinator/second-wave-integrity-verification-v2.json')
assert all(x['matches'] for x in integrity['checks'])
assert integrity['blind_v2_statement_equals_author_with_only_status_line_removed']
oldcheck = read('coordinator/second-wave-integrity-verification-v1.json')
assert all(not x['mismatches'] for x in oldcheck['checks'])

# Freeze the actual mathematical dependency bytes, not their status banners.
inputs = read('reviews/FULL2/input-manifest-v1.json')['inputs']
files = {}
for item in inputs:
    p = Path(item['path'])
    assert sha(p) == item['sha256']
    if p.name not in ['fixed-main-statement-v1.md', 'fixed-main-proof-v1.md']:
        files[str(p.relative_to(OUT))] = item['sha256']
for item in read('reviews/FULL2/input-manifest-v2.json')['new_exact_inputs']:
    p = Path(item['path']); assert sha(p) == item['sha256']
    files[str(p.relative_to(OUT))] = item['sha256']
inherited = read('reviews/FULL2/dependency-hash-check-v1.json')
for item in inherited:
    assert sha(ROOT / item['path']) == item['sha256']

# Preserve inherited IDs, exact references, source hashes and verdict provenance.
reg = read('regressions.json')
source = ROOT / reg['baseline_source']
assert sha(source) == reg['baseline_sha256']
source_data = json.loads(source.read_text())
review_path = 'reviews/FULL2/regression-dispositions-v2.json'
review = read(review_path)
byid = {e['id']:(i,e) for i,e in enumerate(review['entries'])}
assert len(byid) == 200
for e in reg['inherited_entries']:
    x = source_data
    for component in e['json_pointer'].strip('/').split('/'):
        x = x[int(component)] if isinstance(x,list) else x[component]
    h = hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    assert h == e['entry_sha256'] and e['id'] == x['id']
for e in reg['inherited_entries'] + reg['new_entries']:
    i,v = byid[e['id']]
    e['scope_disposition'] = v['full2_disposition']
    e['reason'] = v.get('full2_reason', v.get('exact_v2_applicability'))
    e['current_review'] = {'registry':review_path, 'registry_sha256':sha(OUT/review_path),
                           'json_pointer':f'/entries/{i}', 'scope':'Exact FIXED-MAIN-v2 and its frozen dependency graph',
                           'v2_recheck':'reviews/FULL2/exact-v2-recheck.md',
                           'blind_crosscheck':'reviews/BLIND2/independent-report.md; followup-v2-report.md'}
for i,v in enumerate(review['entries'][193:], start=193):
    reg['new_entries'].append({'id':v['id'], 'scope_disposition':v['full2_disposition'],
        'reason':v.get('full2_reason',v.get('exact_v2_applicability')),
        'prior_exact_v1_disposition':v.get('prior_exact_v1_disposition'),
        'evidence':[{'registry':review_path,'json_pointer':f'/entries/{i}', 'registry_sha256':sha(OUT/review_path)}],
        'scope':'Exact FIXED-MAIN-v2; optional-note checks remain outside the main dependency graph'})
for id_,reason,evidence in [
    ('BLIND2-QUERY-LAW-1','Odd auxiliary and even target modulus cannot give exactly uniform deterministic rounded public output. FIXED-v1 sentence rejected; v2 pays both endpoint TV and distinguishes target promise from actual calls.','reviews/BLIND2/followup-v2-report.md'),
    ('BLIND2-PARTITION-1','A separately chosen evaluation partition for each q can give selected success one. The accepted fiber theorem fixes one common partition across the distinct-prime list.','reviews/BLIND2/independent-report.md Section8'),
    ('BLIND2-SMALL-N-1','At n=2,J=R the finite root quantities obey the lemmas but G-AM fails. The conditional theorem makes no decoding conclusion from failed guards.','reviews/BLIND2/independent-report.md Section8')]:
    reg['new_entries'].append({'id':id_,'scope_disposition':'CHECKED_EXACT_FIXED_V2_SCOPE','reason':reason,'evidence':[evidence]})
assert len(reg['inherited_entries']) == 164 and len(reg['new_entries']) == 39
assert len({e['id'] for e in reg['inherited_entries']+reg['new_entries']}) == 203
reg['check_depth']='All 164 exact historical references/hashes verified; all 203 current entries reconciled by scope. Historical verdicts unchanged. Relevant finite controls and analytic joint-law audits rerun; no blanket rerun of historical jobs claimed.'
reg['updated_at']=clock['checked_at']
reg['current_accepted_graph']='FIXED-MAIN-v2 -> MR-v1 + AM-MAIN-v3, with exact imported interfaces'
atomic(OUT/'regressions.json',reg)

accept = {'id':'DD-ACCEPTANCE-v1','accepted_at':clock['checked_at'],'clock':clock,
    'status':'ACCEPTED_WITH_EXPLICIT_SCOPE','main':'FIXED-MAIN-v2',
    'accepted_new_components':['MR-v1','AM-MAIN-v3','SFUNC-v2','DD1-EXTRACT-v1','DD2-AM1-SNF-v1','DD2-PRIMES-v1'],
    'optional_accepted_note':'coordinator/nonvacuity-and-radius-note-v1.md (not a main dependency)',
    'files':files,'inherited_exact_files':inherited,
    'dependency_review':'reviews/FULL2/source-complexity-report-v1.md',
    'inherited_acceptance':['exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/coordinator/samej-acceptance-v1.md','exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/coordinator/ab-acceptance-v1.md'],
    'full_review':['reviews/FULL2/full-report-v1.md','reviews/FULL2/source-complexity-report-v1.md','reviews/FULL2/exact-v2-recheck.md'],
    'blind_review':['reviews/BLIND2/independent-report.md','reviews/BLIND2/followup-v2-report.md'],
    'seals':{p:sha(OUT/p) for p in ['reviews/FULL1/seal-v1.json','reviews/BLIND1/seal-v1.json','reviews/FULL2/seal-v1.json','reviews/FULL2/seal-v2.json','reviews/BLIND2/seal-manifest.json','reviews/BLIND2/followup-v2-seal-manifest.json']},
    'integrity':['coordinator/first-wave-integrity-verification.json','coordinator/second-wave-integrity-verification-v1.json','coordinator/second-wave-integrity-verification-v2.json'],
    'regression_coverage':{'baseline':164,'new':39,'total':203,'registry':'regressions.json','sha256':sha(OUT/'regressions.json')},
    'probability_gates':{'full_joint_law':'PASS: retain one S through K raw samples; condition on full calibration history before disjoint test bank; no CRT-error independence shortcut',
        'normalizers_support':'PASS: actual Gaussian normalizers, posterior denominator and occupied fibers retained; source-only bad event charged',
        'CP-1':'PASS: old product conclusion rejected; exact 160-atom control reproduced; current arguments use conditional bounds, union bounds, complete-law TV and inherited causal C8',
        'finite_falsification':'PASS at stated scopes; 12 preregistered jobs, 11 exit0, one preserved logging failure; finite and floating evidence do not replace analytic proofs'},
    'scope':['R=Z[X]/(X^n+1), n power of two; integral ordinary-basis J with N(J)<=2^(rho*n), fixed rho<1',
        'Classical BDD in J^-1; rational target within the explicit canonical-infinity radius; source-family hardness is not established',
        'Exact target uses one coefficient-binary shared secret, uniform public ring multipliers and independent coefficient discrete-Gaussian errors',
        'One prescribed target modulus q0; D0 all-input bounded code; actual calls may be transformed/hybrid',
        'Explicit finite guards and sample/advantage/noise window; fixed b,c before target family; full input/evaluator/oracle runtime charged',
        'No unrestricted worst-case hardness, quantum composition, practical efficiency or one fixed noise family for all PPT exponents'],
    'status_banner_policy':'Frozen theorem/proof bytes retain their original PROVISIONAL banners. This exact-hash acceptance record is authoritative for these versions only; later edits require new review.',
    'review_independence':'Full and fresh statement-only reviewers were separate fork-none Astra ultra agents; same-model agreement is correlated scrutiny, not formal verification.',
    'unresolved_main_gates':[]}
atomic(OUT/'coordinator/acceptance-v1.json',accept)

claims=read('claims.json')
for c in claims['claims']:
    if c['id'] in ['DD2-AM1-SNF','DD2-PRIMES','DD1-EXTRACT','AM-MAIN','SFUNC','MR','FIXED-MAIN']:
        c['status']='ACCEPTED_WITH_EXPLICIT_SCOPE'; c['acceptance']='coordinator/acceptance-v1.json'
        c['check_depth']='Nonauthor full proof/source/complexity plus fresh blind independent derivation, exact repaired-version rechecks, scoped old/new regressions and root seal/dependency checks'
        c['reviews']=accept['full_review']+accept['blind_review']
        if c['id']=='FIXED-MAIN':
            c['prior_versions']=[{'version':'v1','status':'LITERAL_EXECUTION_LAW_REJECTED_CORE_SUPPORTED','statement':c['statement'],'statement_sha256':c['statement_sha256']}]
            c['version']='v2';c['statement']='coordinator/fixed-main-statement-v2.md';c['statement_sha256']=files[c['statement']]
        c['canonical_id']=c['id']+'-'+c['version']
    elif c['id']=='DD-TARGET':
        c['status']='MATHEMATICAL_OBJECTIVE_ACHIEVED';c['dependencies']=['FIXED-MAIN-v2'];c['dependency_logic']='One complete reviewed bridge satisfies the stated objective in its explicit restricted scope.'
        c['current_candidate']='Accepted FIXED-MAIN-v2';c['check_depth']='coordinator/acceptance-v1.json; native status updated only after final delivery checks'
    elif c['id']=='DD3-INTERMEDIATE':
        c['status']='ACHIEVED_IN_EXPLICIT_MODEL';c['dependencies']=['AM-MAIN-v3','FIXED-MAIN-v2'];c['acceptance']='coordinator/acceptance-v1.json'
    elif c['id']=='DD1-BRIDGE':
        c['status']='NAIVE_SUFFICIENT_CLAIM_REFUTED_ALTERNATIVES_SCOPED';c['evidence']='workers/DD1/report.md';c['scope']='No blanket impossibility claim; selected-functional route is the accepted replacement.'
    elif c['id']=='DD2-BRIDGE':
        c['status']='EXAMINED_NO_USEFUL_DIRECT_SAMPLING_BRIDGE_ACCEPTED';c['evidence']='workers/DD2/final.md';c['scope']='Uniform-mask off-promise and cancellation overlap are mechanism-specific; no exhaustion claim.'
    elif c['status']=='ACCEPTED-INHERITED' and c['id']!='RF4-SAMEJ-v1':
        c['check_depth']='Exact inherited acceptance/hash retained; FULL1 and FULL2 reread relevant complete proof/specification and verify present interfaces. No broader scope inherited.'
claims['claims'].append({'id':'RECENT-B-CUBE-THETA-v1','canonical_id':'RECENT-B-CUBE-THETA-v1','version':'historical exact','status':'ACCEPTED-INHERITED','acceptance':'exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/coordinator/ab-acceptance-v1.md','scope':'Original full-observation cube theorem; selected-functional extension newly reviewed as SFUNC-v2','dependencies':[]})
claims['claims'].append({'id':'Xylouris-Theorem1.1','canonical_id':'Xylouris-Theorem1.1','version':'Acta Arithmetica 150.1 (2011), printed p66','status':'PRIMARY_SOURCE_IMPORTED','source':'https://www.impan.pl/shop/en/publication/transaction/download/product/83078','scope':'Effective least-prime exponent5.18, weakened to6; checked from primary text, not reproved','dependencies':[]})
claims['new_acceptances']=[{'record':'coordinator/acceptance-v1.json','sha256':sha(OUT/'coordinator/acceptance-v1.json'),'main':'FIXED-MAIN-v2','at':clock['checked_at']}]
claims['invalidations'].append({'at':clock['checked_at'],'claim':'FIXED-MAIN-v1 closing execution-law sentence','cause':'Exact target promise is not the law of every transformed/hybrid execution','replacement':'FIXED-MAIN-v2 separately rechecked by FULL2 and BLIND2; v1 rejection preserved'})
claims['updated_at']=clock['checked_at'];atomic(OUT/'claims.json',claims)

ledger=read('coordinator/audit-ledger.json')
ledger['events'] += [
    {'event':'AM-v2 polynomial-value sentence rejected; SFUNC optimum clarified','evidence':['reviews/FULL1/seal-v1.json','reviews/BLIND1/seal-v1.json'],'status':'PRESERVED_PRIOR_FINDINGS'},
    {'event':'New MR and variable-width AM-v3, FIXED-v1 independently reviewed','evidence':['reviews/FULL2/seal-v1.json','reviews/BLIND2/seal-manifest.json'],'status':'CORE_PASS_LITERAL_QUERY_LAW_REJECTED'},
    {'event':'Exact FIXED-v2 repair and optional note rechecked','evidence':['reviews/FULL2/seal-v2.json','reviews/BLIND2/followup-v2-seal-manifest.json'],'status':'PASS_WITH_EXPLICIT_SCOPE'},
    {'event':'Coordinator exact-version acceptance','at':clock['checked_at'],'evidence':['coordinator/acceptance-v1.json','regressions.json'],'status':'ACCEPTED_WITH_EXPLICIT_SCOPE'}]
atomic(OUT/'coordinator/audit-ledger.json',ledger)
print(json.dumps(checkpoint('Exact FIXED-MAIN-v2 accepted after full/blind repair checks and all 164 inherited regression dispositions', ['Final report and programme consistency review','Final native usage/completion receipt and process observation'], ['Mathematical objective achieved in the explicit restricted family and parameter window','No exhaustion or unrestricted-hardness claim']),indent=2))
