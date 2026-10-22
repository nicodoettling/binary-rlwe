from pathlib import Path
import json,datetime
O=Path(__file__).resolve().parents[1];now=datetime.datetime.now(datetime.timezone.utc).isoformat();rootid='01a15f93-e6bd-7fd2-953c-80af410308a1'
P=Path('/home/nico/.codex/sessions/2026/10/21');root=P/'rollout-2026-10-21T17-48-11-01a15f93-e6bd-7fd2-953c-80af410308a1.jsonl';calls={};records=[]
for line in root.open():
 try:x=json.loads(line)
 except:continue
 y=x.get('payload',{});typ=y.get('type')
 if typ=='function_call' and y.get('name') in ['spawn_agent','send_message','followup_task']:
  try:a=json.loads(y.get('arguments','{}'))
  except:a={}
  if y.get('name')=='spawn_agent':
   z={'timestamp':x.get('timestamp'),'call_id':y.get('call_id'),'tool':y.get('name'),'configuration':{k:a.get(k) for k in ['task_name','model','reasoning_effort','fork_turns']},'assignment':'Plaintext worker assignment is preserved separately; message payload intentionally not duplicated.'};calls[y['call_id']]=z;records.append(z)
  else:calls[y.get('call_id')]={'timestamp':x.get('timestamp'),'tool':y.get('name'),'target':a.get('target')}
 if typ=='function_call_output' and y.get('call_id') in calls:
  z=calls[y['call_id']];out=y.get('output')
  if z['tool']=='spawn_agent':z['actual_return']=out
  elif isinstance(out,str) and 'limit' in out.lower():records.append({**z,'actual_return':out,'policy':'No capacity bypass; root continues useful local work.'})
metadata=[]
for p in P.glob('*.jsonl'):
 try:
  with p.open() as f:first=json.loads(next(f));m=first.get('payload',{})
  if m.get('parent_thread_id')!=rootid and m.get('id')!=rootid:continue
  tc=None
  for line in p.open():
   x=json.loads(line)
   if x.get('type')=='turn_context':tc=x.get('payload',{});break
  metadata.append({'session_path':str(p),'thread_id':m.get('id'),'agent_path':m.get('agent_path','/root'),'parent_thread_id':m.get('parent_thread_id'),'model':(tc or {}).get('model'),'effort':(tc or {}).get('effort',(tc or {}).get('reasoning_effort')),'approval_policy':(tc or {}).get('approval_policy'),'service_tier_in_turn_context':(tc or {}).get('service_tier','NOT_PRESENT')})
 except (OSError,ValueError,StopIteration):continue
r={'at':now,'root_rollout':str(root),'actual_records':records,'configuration_metadata':metadata,'qualification':'Actual tool receipts and local configuration metadata, not backend billing telemetry. Root explicit default from launcher argv; children inherit, API exposes no tier field. No claim of aggregate memory containment.'}
p=O/'coordinator/spawn-receipts-all-v5.json';p.write_text(json.dumps(r,indent=2)+'\n');rv=json.loads((O/'coordinator/runtime-verification.json').read_text());rv['metadata_refresh_v5']={'at':now,'receipt':'coordinator/spawn-receipts-all-v5.json','actual_spawn_attempts':sum(z['tool']=='spawn_agent' for z in records),'metadata':metadata};rv['updated_at']=now;t=O/'coordinator/runtime-verification.json.tmp';t.write_text(json.dumps(rv,indent=2)+'\n');t.replace(O/'coordinator/runtime-verification.json');print({'at':now,'spawn_attempts':sum(z['tool']=='spawn_agent' for z in records),'metadata_threads':len(metadata),'other_limit_returns':sum(z['tool']!='spawn_agent' for z in records)})
