"""Save only the latest list_agents tool result, never arbitrary transcript data."""
from pathlib import Path
import json, datetime, hashlib, sys
O=Path(__file__).resolve().parents[1]
source=Path('/home/nico/.codex/sessions/2026/10/21/rollout-2026-10-21T17-48-11-01a15f93-e6bd-7fd2-953c-80af410308a1.jsonl')
last_call=None; result=None
with source.open() as stream:
    for number,line in enumerate(stream,1):
        try:record=json.loads(line)
        except json.JSONDecodeError:continue
        item=record.get('payload',{})
        if not isinstance(item,dict):continue
        if item.get('type')=='function_call' and item.get('name')=='list_agents':
            last_call={'call_id':item['call_id'],'timestamp':record['timestamp'],'line':number}
            result=None
        elif last_call and item.get('type')=='function_call_output' and item.get('call_id')==last_call['call_id']:
            output=item['output'];parsed=json.loads(output) if isinstance(output,str) else output
            assert isinstance(parsed,dict) and set(parsed)=={'agents'}, 'Unexpected tool result schema'
            assert all(set(e)=={'agent_name','agent_status'} for e in parsed['agents'])
            result={'at':record['timestamp'],'call':last_call,'result_line':number,
                    'result_line_sha256':hashlib.sha256(line.encode()).hexdigest(), 'tool_result':parsed}
assert result is not None, 'No completed list_agents result found'
now=datetime.datetime.now(datetime.timezone.utc)
observed=datetime.datetime.fromisoformat(result['at'].replace('Z','+00:00'))
assert 0 <= (now-observed).total_seconds() < 180, 'Call list_agents again for a fresh observation'
cap=json.loads((O/'run.log.brlwe-fixed-family-20261021-astra-ultra.cap-status.json').read_text())
children=[e for e in result['tool_result']['agents'] if e['agent_name']!='/root']
active=[e for e in children if not (isinstance(e['agent_status'],dict) and 'completed' in e['agent_status'])]
result.update({'captured_at':now.isoformat(),'source':str(source),'service_activation':cap['started_at'],
               'active_child_count':len(active),'scope':'Actual latest list_agents response only; not a process census. No arbitrary message, arguments, environment or encrypted-content fields extracted.'})
if '--require-complete' in sys.argv:assert not active, 'A child is still active'
dest=O/'coordinator'/sys.argv[1];assert not dest.exists()
tmp=dest.with_suffix(dest.suffix+'.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(dest)
print(json.dumps({'receipt':str(dest.relative_to(O)),'at':result['at'],'active_child_count':len(active),'source_result_line':result['result_line']}))
