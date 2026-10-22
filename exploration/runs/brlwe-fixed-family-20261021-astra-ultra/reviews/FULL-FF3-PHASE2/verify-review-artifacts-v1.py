from pathlib import Path
import hashlib,json,datetime
p=Path(__file__).resolve().parent;out=p.parents[1]
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
freeze=p/'inputs/workers/FF3/author-phase2-seal-v1.json';expected='4d0dfe1336c115e8cde9870585aa3b8e7893d2d7f012fe0a708159ae980258e5';assert sha(freeze)==expected
seal=json.loads(freeze.read_text());assert len(seal['files'])==177
for f in seal['files']:
 assert sha(p/'inputs/FF3'/f['path'])==f['sha256']
 assert sha(out/'workers/FF3'/f['path'])==f['sha256']
inputs=0;changed_context=[]
for name in ['input-manifest-v1.json','input-manifest-addendum-v1.json','input-manifest-addendum-v2.json','input-manifest-addendum-v3.json']:
 for f in json.loads((p/name).read_text())['files']:
  assert sha(p/f['snapshot'])==f['sha256'];inputs+=1
  if sha(Path(f['source']))!=f['sha256']:changed_context.append(f['source'])
assert not changed_context,changed_context
jobs=[]
for stem,expected_exit in [('independent-certificate-check-v1',1),('independent-certificate-check-v2',0),('independent-probability-controls-v1',0),('independent-enum-repair-controls-v1',0)]:
 end=json.loads((p/(stem+'-end.json')).read_text());assert end['exit']==expected_exit
 if expected_exit==0:
  start=json.loads((p/(stem+'-start.json')).read_text())
  for f in start['code_and_registration']:assert sha(p/f['file'])==f['sha256']
  assert 'Exit status: 0' in (p/(stem+'.stderr.txt')).read_text()
 jobs.append({'stem':stem,'exit':expected_exit,'cleanup':end['cleanup']})
reg=json.loads((p/'regression-dispositions-v1.json').read_text());assert reg['historical_count']==203 and all(e['reference_integrity_match'] for e in reg['entries'])
old=out/'reviews/FULL-SOURCE3/phase1-final-seal-v1.json';assert sha(old)=='46f2aefbe140f2b7868834ce6a405b8619e34a0e31aad5e8e4e3b7edd5bf7215'
result={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','author_files_reverified':177,'snapshot_records_reverified':inputs,'all_source_versions_unchanged':True,'jobs':jobs,'active_jobs':0,'inherited_references':203,'old_source_phase1_seal_unchanged':True,'scope':'file integrity, exact recorded outputs and cleanup only; no extra experiment or blanket historical recertification'}
(p/'artifact-verification-v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
