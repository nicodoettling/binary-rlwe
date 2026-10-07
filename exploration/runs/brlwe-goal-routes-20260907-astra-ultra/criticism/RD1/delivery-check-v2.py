"""Administrative audit of frozen delivery evidence; no mathematical experiment."""
from pathlib import Path
import datetime, hashlib, json, re, sys

OUT=Path(__file__).resolve().parent
RUN=OUT.parents[1]
REPO=RUN.parents[2]
label=sys.argv[1]
assert re.fullmatch(r'[a-zA-Z0-9_-]+', label)
DEST=OUT/'input'/label
DEST.mkdir(parents=True,exist_ok=False)
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
records={}; checks=[]
def digest(b):return hashlib.sha256(b).hexdigest()
def read(rel):
    if rel not in records:
        src=RUN/rel
        raw=src.read_bytes()
        copy=DEST/rel;copy.parent.mkdir(parents=True,exist_ok=True);copy.write_bytes(raw)
        records[rel]={'source':str(src),'archived':str(copy),'sha256':digest(raw),'bytes':len(raw),'read_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    return (DEST/rel).read_bytes()
def obj(rel):return json.loads(read(rel))
def check(name,passed,detail=None):checks.append({'name':name,'passed':bool(passed),'detail':detail})
launcher=obj('launcher-run.json');cap_path=Path(launcher['cap']['status_file'])
assert cap_path.is_relative_to(RUN)
cap=obj(str(cap_path.relative_to(RUN)))
check('inherited service hard cap',cap['hard_deadline_at']=='2026-09-08T00:34:27.111419+00:00',cap['hard_deadline_at'])
core=['final.md','resume.md','parameter-table.md','source-comparison.md','claims.json','reconciliation.md','regressions.json','experiments/registry.json','claim-history.jsonl']
for rel in core:read(rel)
cl=obj('claims.json'); cs=cl['claims'];by_id={c['id']:c for c in cs}
check('unique claim identifiers',len(by_id)==len(cs))
errors=[]
for c in cs:
    for d in c.get('dependencies',[]):
        dep=by_id.get(d['id'])
        if dep is None or dep['version']!=d['version']:errors.append([c['id'],'dependency/version',d])
        elif c['status']=='ACCEPTED' and dep['status']!='ACCEPTED':errors.append([c['id'],'nonaccepted dependency',d])
    if c.get('proof'):
        try:read(c['proof'])
        except FileNotFoundError:errors.append([c['id'],'missing proof',c['proof']])
    if c['status']=='ACCEPTED' and not c.get('reviews'):errors.append([c['id'],'no review receipt'])
check('graph versions, proof paths and accepted review receipts',not errors,errors)
seen=set();active=set();cycles=[]
def walk(i):
    if i in active:cycles.append(i);return
    if i in seen:return
    active.add(i)
    for d in by_id[i].get('dependencies',[]):
        if d['id'] in by_id:walk(d['id'])
    active.remove(i);seen.add(i)
for i in by_id:walk(i)
check('acyclic current graph',not cycles,cycles)
expected={
'candidates/search/theorem-only-v2.md':'bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124',
'candidates/search/proof-v1.md':'198c36bce9a73b87f2e1f5cf644d7e96b13cda063922f1ab10b0b2ee60114042',
'candidates/search/supplement-v1.md':'71752406e81e327b5c47d0d118ea9bc6aa0f87566d23345daf290a7b8322410a',
'coordinator/source-and-parameters-v1.md':'131e6a3feec87010007a30ddc1e37bdec44687648120bfe1e8c5187e6e779f50',
'coordinator/rectangular-completion-v1.md':'d66a1ea3e1c61990c77380de60c39b00a3097ab111407aedc610cfbe34c70163',
'criticism/RB1/blind-report-v1.md':'c95e83a3a53cd589d2f2bf731ead33b35857af33edea28f1f3a0f8b722061b2d',
'criticism/RS1/report-v1.md':'f04881cf65af51b7079fd59b785e9ca2d8cbc53fb710c06e0b823ae31cc20785',
'criticism/RF1/report-v1.md':'ff7a034fa2d8be726a0940801a45697f082c342e786d3fd47a7674bd87b91c64'}
errors=[]
for rel,h in expected.items():
    if digest(read(rel))!=h:errors.append(rel)
check('exact theorem, proofs and complete referee hashes',not errors,errors)
errors=[]
for rel in list(expected)[:3]:
    author=rel.replace('candidates/search/','workers/A1/')
    if read(author)!=read(rel):errors.append([author,rel])
check('delivery candidate equals reviewed author bytes',not errors,errors)
blind=obj('criticism/RB1/freeze-v1.json')
check('blind freeze declaration and theorem hash',blind['blind'] and not blind['proposed_proof_received_before_freeze'] and not blind['historical_objection_received_before_freeze'] and blind['candidate_sha256']==expected['candidates/search/theorem-only-v2.md'],{'frozen_at':blind['frozen_at']})
errors=[]
for item in blind['artifacts']:
    rel='criticism/RB1/'+item['path']
    if digest(read(rel))!=item['sha256']:errors.append(rel)
check('complete RB1 frozen-artifact hashes',not errors,errors)
rf=obj('criticism/RF1/artifact-manifest-v1.json');errors=[]
for rel,h in rf['artifacts'].items():
    full='criticism/RF1/'+rel
    if digest(read(full))!=h:errors.append(full)
check('complete RF1 frozen-artifact hashes',not errors,errors)
rs=obj('criticism/RS1/input-hashes.json');errors=[]
for entry in rs['files']:
    src=REPO/entry['path'];assert src.is_relative_to(RUN)
    rel=str(src.relative_to(RUN))
    if digest(read(rel))!=entry['sha256']:errors.append(rel)
check('RS1 review inputs equal delivered versions',not errors,errors)
for rel in ['criticism/RS1/delivery-verification.json','criticism/RS1/additional-input-hashes.json','coordinator/frozen-evidence.json','coordinator/frozen-inputs-v1.json','coordinator/check-artifacts-v1.py']:
    if (RUN/rel).is_file():read(rel)
if 'coordinator/frozen-evidence.json' in records:
    frozen=obj('coordinator/frozen-evidence.json');errors=[]
    for ent in frozen.get('files',[]):
        rel=ent['path']
        if not (RUN/rel).is_file() or digest(read(rel))!=ent['sha256']:errors.append(rel)
    check('coordinator frozen-evidence manifest',not errors,{'files':len(frozen.get('files',[])),'mismatches':errors})
errors=[]
for rel in ['final.md','resume.md','parameter-table.md','source-comparison.md','reconciliation.md']:
    for target in re.findall(r'\]\(([^)]+)\)',read(rel).decode()):
        target=target.strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):continue
        path=target.split('#',1)[0]
        if path and not (RUN/rel).parent.joinpath(path).exists():errors.append([rel,target])
check('delivery local Markdown link targets',not errors,errors)
errors=[]
for i,line in enumerate(read('claim-history.jsonl').decode().splitlines(),1):
    try:json.loads(line)
    except Exception as e:errors.append([i,str(e)])
check('claim history JSONL parses',not errors,errors)
errors=[]
for c in cs:
    if c.get('proof_sha256') and digest(read(c['proof']))!=c['proof_sha256']:
        errors.append([c['id'],'proof hash'])
    for receipt in c.get('reviews',[]):
        if digest(read(receipt['path']))!=receipt['sha256']:
            errors.append([c['id'],'review hash',receipt['path']])
check('per-claim proof and review receipt hashes',not errors,errors)
reg=obj('regressions.json');old=obj('imports/latest-regressions.json')
entries=reg.get('historical_application',[])
old_ids={e['id'] for e in old['controls']}
current_ids={e['id'] for e in entries}
rf_text=read('criticism/RF1/report-v1.md').decode()
errors=[]
for e in entries:
    if not e.get('current_application_rows') or not all(row in rf_text for row in e['current_application_rows']):
        errors.append(e['id'])
check('all imported historical regression IDs map to exact referee rows',old_ids==current_ids and not errors,{'imported':len(old_ids),'mapped':len(current_ids),'missing':sorted(old_ids-current_ids),'extra':sorted(current_ids-old_ids),'bad_rows':errors})
changed=[rel for rel,ent in records.items() if digest(Path(ent['source']).read_bytes())!=ent['sha256']]
check('read snapshot remained stable through check',not changed,changed)
result={'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Administrative byte/version/link checks only; mathematical and endpoint review is in RD1 report. No finite mathematical experiment or source-hardness test.','all_passed':all(c['passed'] for c in checks),'claim_statuses':{c['id']:{'version':c['version'],'status':c['status']} for c in cs},'checks':checks,'inputs':records}
(DEST/'manifest.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'snapshot':str(DEST),'all_passed':result['all_passed'],'checks':len(checks),'failures':[c for c in checks if not c['passed']],'inputs':len(records)},indent=2))
