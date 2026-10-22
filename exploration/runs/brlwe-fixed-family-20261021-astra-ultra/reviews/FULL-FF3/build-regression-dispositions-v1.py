from pathlib import Path
import json,hashlib,datetime
root=Path('exploration/runs/brlwe-fixed-family-20261021-astra-ultra');out=root/'reviews/FULL-FF3'
raw=(root/'regressions.json').read_bytes();reg=json.loads(raw);(out/'regression-source-snapshot-v1.json').write_bytes(raw)
dd=Path('exploration/runs/brlwe-direct-decision-20261021-astra-ultra/regressions.json');ddraw=dd.read_bytes();ddreg=json.loads(ddraw)
def ids(s):return set(s.split())
groups={
'FULL_CONDITIONAL_LAW':{
'ids':ids('R03 R04 R05 R08 R12 R15 C03-HC5 C03-HC7 C02-LATENT-PUBLIC PUBLIC-ENCODED-F SE-CORRELATION-F3 PAIRWISE-SE-F3 EX-PUBLIC-TAPE EX-RETAINED-M3 B-JL-REDRAW-T B-SUP-RETAINED-COINS-1 DD1-SHARED-SECRET DD1-EXTRACT-FULL-LAW DD2-CRT-ERROR-CORRELATION DD2-UNKNOWN-CUBE-TRANSLATE MR-FULL-SHARED-LAW RT2-NC3 BT16-POSTERIOR-1 B-REVEAL-S-1 MR-ROUNDED-PUBLIC-BIAS BLIND2-QUERY-LAW-1'),
'reason':'DIRECT_APPLICABILITY: every fixed-S endpoint and the uniform comparator are proved/checked as complete laws; S retained across samples, fresh coins only conditionally iid; no actual-S advice or reverse projection. See probability-audit-v1.md.'},
'NORMALIZATION_AND_POSITIVITY':{
'ids':ids('R02 C03-HC1 C03-HC2 C03-HC3 C03-HC4 NC1-v1 UNIFORM-APPROX-COLLAPSE N03-PV-CONDITIONING N03-SCAL-POSTERIOR RECT-ALG-1 EX-APPENDED-H EX-M3-CROSSBLOCK D-THETA-RETAIN-U-v1 D-LSW-THETA-1 B-TWO-ROW-NORMALIZER-1 B-BINARY-FOURIER-1 ROOT-COSET-NORMALIZER-1 E-PAIR-TRUNCATION-1 M1-FV1-NORMALIZERS B-THETA-FV1 MR-DISCRETE-GAUSSIAN-NORMALIZER FQ-NORM-1 RF4-RETRY-NEG1'),
'reason':'DIRECT_GUARD: H rows, event denominator p-u, DG rho, finite Z(x), and both endpoint measures retained. FV5 rejects row-only normalization repair. No signed inverse, discarded theta mass or source/G conditioning used.'},
'ADAPTIVE_CP1_AND_UNIONS':{
'ids':ids('R11 R18 C03-HC6 CP-1 A-CLASS-CP1-1 C-CAUSAL-WALK-1 BT14-HISTORY-ATOM-1 BT14-FV1 M1-FV1-CP1 HC1-FV1 RF4-FV1 FQ-RETRY-1 BT19-SELECTION-1'),
'reason':'DIRECT_GUARD: CP1 posterior normalizer10/11 and21/2000>1/100 explicitly reject marginal sequential products; ENUM uses unions, rejection cap has fresh pointwise conditional proposals. No unobservable history branch.'},
'RANK_NONUNITS_AND_ACTUAL_SECRET':{
'ids':ids('R06 R07 R09 R10 R14 N02-DUAL-NUMBER D-HIGHINDEX-GUESS-1 BT12-FV1 B-FV1-CUBE289 A-BFAM-FV1 BT16-ZERO-1 DD2-NORM-ROOT-MULTIPLICITY FULL2-NONVACUITY-1'),
'reason':'DIRECT_GUARD: rank/Smith divisibility counts actual image support, includes all nonunits and allzero A. ENUM enumerates actual binary candidates; residual acceptance is not silently whole-secret correctness. Cost2^n and error of competitors explicitly charged; degree8 nonunit control included.'},
'EFFECTIVENESS_AND_QUANTIFIERS':{
'ids':ids('S0-dependency A-PPT-LEDGER-SCOPE B-GP-RATIONAL-ENCODING-1 C-OHCP-BOUNDED-RUNTIME-1 C8-FV1 FQ-MODULUS-1 ROOT-PARAM-T-1 ROOT-PARAM-ENC-1 H-LLL-BITLENGTH-1 H-V0-BITLENGTH-1 BT19-RETRY-1 BT20-VACUITY-1 BT20-RETRY-MARGIN-1 BT20-WIDTHVALUE-1 BT21-VACUITY-1 BT22-MARGIN-WIDTH-1 DD1-MAIN-GAUSSIAN-NOTATION DD1-MAIN-RATIONAL-EXPONENT MR-VARIABLE-WIDTH-CAPS MR-ADVANTAGE-WINDOW MR-FV1-LOGGING-FAILURE FULL2-WORDING-1 FULL2-SCOPE-1 BLIND2-SMALL-N-1'),
'reason':'DIRECT_GUARD: exact finite encodings versus real mathematical kernels distinguished;2^n search and ideal transcendental sampling not PPT. Polynomial numeric value distinguished from bits; target quantifier order retained; asymptotic conditions do not certify a finite instance; failures preserved.'},
'COVARIANCE_OR_EVENT_SCOPE':{
'ids':ids('R13 C02-CHAR MR-SIGNED-SECRET-COVARIANCE RT2-WEIGHTED-FV1 RT2-NC1 RT2-NC2 BT21-ADAPTIVE-MULTIPLIER-1 BT22-TV-MOMENT-1 BT22-JOINT-MULTIPLIER-1 ROOT-MASK-RESIDUE-1 ROOT-SELECTED-FIBER-BOUNDARY'),
'reason':'SCOPE_GUARD: full law equalities and bounded retained-S events are used, not moment-to-TV, marginal-covariance or one-character sufficiency. No correlated source-multiplier conditioning or secret invariant is supplied.'}
}
refs=reg['inherited_entries'];assert len(refs)==203 and len({e['id'] for e in refs})==203
known={e['id'] for e in refs}
assert all(g['ids']<=known for g in groups.values())
entries=[]
for e in refs:
 parts=e['json_pointer'].strip('/').split('/');src=ddreg[parts[0]][int(parts[1])]
 assert src['id']==e['id'] and hashlib.sha256(ddraw).hexdigest()==e['source_registry_sha256']
 assert hashlib.sha256(json.dumps(src,sort_keys=True,separators=(',',':')).encode()).hexdigest()==e['entry_sha256']
 hit=[name for name,g in groups.items() if e['id'] in g['ids']]
 entries.append({'id':e['id'],'source_reference':e,'description':src.get('description_hint',src.get('scope',src.get('reason','See exact source pointer'))),'groups':hit or ['HISTORICAL_SCOPE_RETAINED'],'current_disposition':'REVIEWED_GUARD_CURRENT_MECHANISM' if hit else 'RETAINED_OUTSIDE_PHASE1_DEPENDENCY','reason':[groups[h]['reason'] for h in hit] or ['No binomial/subset source sampler, fractional-ideal BDD decoder, quantum adapter, tower descent, selected-root extraction or inherited AM implementation is claimed or modified here. Exact historical failure remains valid in its source scope; no hardness or acceptance inference.'],'evidence':['full-report-v1.md','probability-audit-v1.md','source-complexity-report-v1.md']})
local=json.loads((out/'inputs/regressions.json').read_text())['new'];local_out=[]
for e in local:
 st='PRESERVED_SCOPED_NEGATIVE_OR_POSITIVE_CONTROL'
 if e['id']=='CP-1':st='OLD_PRODUCT_REJECTED_EXACTLY'
 if e['id']=='FF3-RADIAL-POSITIVE-1':st='POSITIVE_ALL_ENDPOINTS_INDEPENDENTLY_VERIFIED'
 if e['id']=='FF3-ADAPTIVE-FIXED-H-FAIL-1':st='EXCLUSION_INDEPENDENT_FARKAS_VERIFIED_EVENT_FORMULA_AUDITED'
 local_out.append({'source_entry':e,'current_disposition':st,'evidence':['full-report-v1.md','independent-controls-v1.stdout.jsonl','independent-secondary-v1.stdout.jsonl']})
new=[{'id':'FULL-FF3-ENUM-SIGN-1','disposition':'REJECTED_INTERMEDIATE_INCLUSION_v1_STATEMENT_BOUND_UNAFFECTED','evidence':'new-regressions-v1.md'}, {'id':'FULL-FF3-UNIT-GUARD-1','disposition':'SOURCE_NONUNIT_EXTENSION_REJECTED','model':'Z4 source0,2,identity H,zero noise,target0,1 gives C=2A,not uniform','evidence':'full-report-v1.md'}, {'id':'FULL-FF3-Q17-BOX-1','disposition':'BOUNDED_CONDITIONAL_LAW_CHECK_PASS','evidence':'independent-controls-v1.stdout.jsonl'}, {'id':'FULL-FF3-N8-NONUNIT-1','disposition':'BOUNDED_ALL6560_DIFFERENCES_CHECK_PASS','evidence':'independent-controls-v1.stdout.jsonl'}, {'id':'FULL-FF3-TWOEVENT-FINITE-1','disposition':'BOUNDED89_VALID76_INVALID_CASES_PASS','evidence':'independent-secondary-v1.stdout.jsonl'}]
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Frozen FF3 phase1 exact87file packet only; not DD recertification or later FF3v2','source_registry_sha256':hashlib.sha256(raw).hexdigest(),'inherited_count':len(entries),'all_ids_unique':True,'source_entries_all_hash_verified':True,'groups':{k:{'ids':sorted(v['ids']),'reason':v['reason']} for k,v in groups.items()},'entries':entries,'phase1_local_entries':local_out,'review_new_entries':new,'CP1':'REJECT21/2000>1/100;normalizer10/11;later21/221<1/10'}
(out/'regression-dispositions-v1.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'inherited':len(entries),'groups':{k:sum(k in x['groups'] for x in entries) for k in list(groups)+['HISTORICAL_SCOPE_RETAINED']},'local':len(local_out),'new':len(new)}))
