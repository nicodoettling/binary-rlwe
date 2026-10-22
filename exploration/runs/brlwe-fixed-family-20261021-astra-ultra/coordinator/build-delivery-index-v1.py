from pathlib import Path
import json,hashlib,datetime,re
O=Path(__file__).resolve().parents[1];now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def atom(rel,x):
 p=O/rel;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(x,indent=2)+'\n');t.replace(p)
x=json.loads((O/'claims.json').read_text());by={c['id']:c for c in x['claims']}
for ident in ['SV-GAP-DECODE-v1','SV-LIST-DECODE-v1']:
 c=by[ident];c['dependencies']=['SV-RS-DECODE-v2' if d=='SV-RS-DECODE-v1' else d for d in c.get('dependencies',[])];c['dependency_gate']='CLOSED_EXACT_GENERIC_R_EQUIVALENCE_BY_FULL_REPAIR4_AND_ACCEPTANCE_V5'
by['SV-RS-ACTUAL-v3']['dependencies']=['SV-DENSE-SPLIT-v1','SV-RS-DECODE-v2 generic-r decoder','inherited FIXED-MAIN-v2 radius and charged chi freedom']
x['updated_at']=now;atom('claims.json',x)
local={
'CRT-PROJ-v1':[], 'CERT-EXTRACT-v2':['CRT-PROJ-v1'],
'SV-BDD-CLASS-v1':[], 'SV-FROB-PRIME-v1':['SV-BDD-CLASS-v1'],
'SV-SYMDESC-v2':['SV-BDD-CLASS-v1'], 'SV-SUBFIELD-v2':['SV-BDD-CLASS-v1','SV-SYMDESC-v2'],
'SV-PRIME-SUPPORT-v2':['SV-SUBFIELD-v2'], 'SV-ALL-SUBFIELDS-v1':['SV-SYMDESC-v2','SV-SUBFIELD-v2'],
'SV-DENSE-SPLIT-v1':['SV-ALL-SUBFIELDS-v1'], 'SV-RS-DECODE-v2':[],
'SV-GAP-DECODE-v1':['SV-RS-DECODE-v2'], 'SV-LIST-DECODE-v1':['SV-RS-DECODE-v2'],
'SV-RS-ACTUAL-v3':['SV-DENSE-SPLIT-v1','SV-RS-DECODE-v2'],
'SV-RS-BIT-v2':['SV-RS-DECODE-v2','SV-GAP-DECODE-v1'], 'SV-SPARSE-ACQ-v1':['SV-BDD-CLASS-v1'],
'GAUSS-AVG-v1':[], 'FRAC-INFO-v1':[], 'WEIGHT-COV-v1':[], 'WEIGHT-GAUSS-v1':['WEIGHT-COV-v1','GAUSS-AVG-v1'],
'FF3-TWOSECRET-v1':[], 'FF3-TWOEVENT-v1':[], 'FF3-ENUM-v1':[],
'FF3-COMPRESSED-SELECTOR-INFORMATION-v2':['FF3-ENUM-v1'], 'FF3-SELECTOR-PUBLIC-v3':['FF3-COMPRESSED-SELECTOR-INFORMATION-v2'],
'FF3-ENERGY-RANK-v2':['FF3-TWOEVENT-v1'], 'FF3-JOINT-RANK-FINITE-v1':[], 'FF3-COMPACT-SELECTOR-v3':[], 'BOUNDED-AFFINE-TV-v1':[]}
nodes=[];edges=[]
for ident,deps in local.items():
 c=by[ident];nodes.append({'id':ident,'status':c['status'],'statement':c['statement'],'statement_sha256':sha(O/c['statement']),'proof':c['proof'],'proof_sha256':sha(O/c['proof']),'acceptance':c.get('review'),'scope':c.get('scope'),'external_or_historical_dependencies':c.get('dependencies',[])})
 for d in deps:edges.append({'from':ident,'requires':d,'status':by[d]['status'],'kind':'local exact theorem or explicitly conditional instantiation'})
bad=[e for e in edges if by[e['from']]['status'].startswith('ACCEPTED') and not by[e['requires']]['status'].startswith('ACCEPTED')];assert not bad,bad
atom('claim-dependencies.json',{'at':now,'scope':'Exact local dependency index, not a proof certificate. DENSE optional arbitrary-subfield conclusion uses ALL-SUBFIELDS; generic RS has its own direct proof. ENUM dependency for selector is only its Gaussian lower-bound corollary. ENERGY TWOEVENT dependency is conditional instantiation, not bare rank transport.','nodes':nodes,'edges':edges,'accepted_dependency_gaps':bad,'historical_policy':'Inherited exact DD acceptance read-only, not recertified. Radius comparison separately requires actual DD parameter interface.','open_objectives':{'FF':'No proved edge from auxiliary claims to full fixed-family decision reduction. Target quantifiers/source comparison or scalable kernel remain open.','SV':'Substantive algorithms at inherited source radius; no new FF-delivered radius.','hardness':'No compatible independently established premise/effective map.'}})
atom('coordinator/acceptance-v5-dependency-label-addendum-v1.json',{'at':now,'base':'coordinator/acceptance-v5.json','base_sha256':sha(O/'coordinator/acceptance-v5.json'),'reason':'Frozen accepted-claim copies retained earlier pending labels/dependency names. Their dependency_resolution and top qualifications already closed exact generic-r equivalence. Mutable claims and graph now use RS-v2 explicitly. No theorem bytes or acceptance scope changed.','corrected':['SV-GAP-DECODE-v1','SV-LIST-DECODE-v1','SV-RS-ACTUAL-v3'],'graph':'claim-dependencies.json'})
art=[]
for base in ['experiments','workers','reviews']:
 for p in (O/base).rglob('*'):
  if not p.is_file():continue
  rel=p.relative_to(O);parts=rel.parts
  if any(v in parts for v in ['inputs','allowed-input','frozen-inputs','frozen']):continue
  name=p.name.lower()
  if any(t in name for t in ['registration','prereg','receipt','resource','stdout','stderr','output','exit','seal','disposition','report','verdict']):
   art.append({'path':str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
atom('experiments/evidence-index-v1.json',{'at':now,'scope':'Inventory of original experiment/review records, excluding copied review inputs; raw failures and unknown solver outcomes remain. An artifact count is not an experiment count. Full bounded test results do not prove infinite distributions.','artifacts':art,'root_registry':'experiments/registry.json','limits':'Per registered job only; no aggregate memory containment claim. At most2simultaneous/1heavy by coordinator slot grants.','newest_review_gate':'Resource review in progress; final refresh required.'})
print({'at':now,'nodes':len(nodes),'edges':len(edges),'evidence_artifacts':len(art)})
