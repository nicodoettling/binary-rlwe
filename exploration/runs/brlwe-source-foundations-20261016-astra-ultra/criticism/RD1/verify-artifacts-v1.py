from pathlib import Path
import hashlib, json, difflib
from datetime import datetime, timezone
base=Path('exploration/runs/brlwe-source-foundations-20261016-astra-ultra')
out=base/'criticism/RD1'; inp=out/'input'
manifest=json.loads((inp/'manifest.json').read_text())
checks=[]
for e in manifest['files']:
 p=inp/e['file'];data=p.read_bytes();got=hashlib.sha256(data).hexdigest()
 checks.append({'file':e['file'],'expected':e['sha256'],'actual':got,'match':got==e['sha256'],'bytes':len(data)})
 assert got==e['sha256']
a=(inp/'expansion-proof-v1.md').read_text();b=(inp/'expansion-proof-v2.md').read_text()
la=a.splitlines(keepends=True);lb=b.splitlines(keepends=True)
changes=[]
for tag,i,j,k,l in difflib.SequenceMatcher(None,la,lb,autojunk=False).get_opcodes():
 if tag!='equal':changes.append({'operation':tag,'old_start_line':i+1,'old_end_line':j,'new_start_line':k+1,'new_end_line':l,'old_exact_text':''.join(la[i:j]),'new_exact_text':''.join(lb[k:l])})
assert len(changes)==3
assert [x['old_start_line'] for x in changes]==[1,3,175]
assert a[a.index('## 1.'):a.index('## 10.')]==b[b.index('## 1.'):b.index('## 10.')]
exactdiff=''.join(difflib.unified_diff(la,lb,fromfile='expansion-proof-v1.md',tofile='expansion-proof-v2.md'))
assert exactdiff==(inp/'proof-v2-metadata-diff.txt').read_text()
(out/'verified-diff-v1.txt').write_text(exactdiff)
evidence=out/'evidence';evidence.mkdir(exist_ok=True)
files=[('claims.json','claims-snapshot.json'),('regressions.json','regressions-snapshot.json'),('coordinator/source-contract-v1.md','source-contract-v1.md'),('criticism/RS1/report-v1.md','RS1-report-v1.md'),('criticism/RS1/sampler-budget-v1.md','RS1-sampler-budget-v1.md'),('criticism/RS1/primary-access-v1.json','RS1-primary-access-v1.json'),('criticism/RS1/input/source-comparison.md','RS1-source-comparison.md'),('criticism/RS1/input/parameter-table.md','RS1-parameter-table.md')]
evidence_hashes=[]
for src,dst in files:
 data=(base/src).read_bytes();(evidence/dst).write_bytes(data)
 evidence_hashes.append({'source':src,'snapshot':'evidence/'+dst,'sha256':hashlib.sha256(data).hexdigest()})
claims=json.loads((evidence/'claims-snapshot.json').read_text()); cs={x['id']:x for x in claims['claims']};ex=[x for x in cs if x.startswith('EX-')]
for cid in ex:
 for dep in cs[cid].get('dependencies',[]):assert dep in cs
stack=set();done=set()
def visit(cid):
 assert cid not in stack
 if cid in done:return
 stack.add(cid)
 for dep in cs[cid].get('dependencies',[]):visit(dep)
 stack.remove(cid);done.add(cid)
visit('EX-PPT')
regs=json.loads((evidence/'regressions-snapshot.json').read_text())['entries'];ids=[x['id'] for x in regs]
assert len(ids)==43 and len(set(ids))==43
receipt={'scope':'Administrative identity and graph checks only; not mathematical certification','time_utc':datetime.now(timezone.utc).isoformat(),'frozen_input_checks':checks,'exact_changed_regions':changes,'mathematical_sections_1_through_9_byte_identical':True,'diff_matches_supplied_file_exactly':True,'additional_evidence_hashes':evidence_hashes,'load_bearing_EX_nodes':ex,'EX_dependency_graph_acyclic':True,'EX_PPT_dependency_closure':sorted(done),'regression_unique_ids':ids,'current_claim_graph_proof':claims['proof'],'current_claim_graph_proof_hash':claims['proof_sha256'],'canonical_proof_v2_hash':hashlib.sha256((inp/'expansion-proof-v2.md').read_bytes()).hexdigest(),'numerical_experiments_in_RD1':0,'blind_material_accessed':False,'author_files_modified':False}
(out/'artifact-verification-v1.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'input_hashes_match':True,'changed_regions':len(changes),'mathematical_sections_unchanged':True,'EX_nodes':len(ex),'regression_ids':len(ids),'graph_proof':claims['proof'],'receipt':'artifact-verification-v1.json'}))
