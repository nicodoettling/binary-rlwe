import datetime as dt
import hashlib
import json
from pathlib import Path
import time

ROOT = Path('/home/nico/projects/research_projects/binaryRLWE')
OUT = ROOT / 'exploration/runs/brlwe-fixed-family-20261021-astra-ultra'
DD = ROOT / 'exploration/runs/brlwe-direct-decision-20261021-astra-ultra'

def atomic(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2) + '\n')
    tmp.replace(path)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

now = dt.datetime.now(dt.timezone.utc)
cap = json.loads((OUT / 'run.log.brlwe-fixed-family-20261021-astra-ultra.cap-status.json').read_text())
manifest = json.loads((OUT / 'launcher-run.json').read_text())
start = dt.datetime.fromisoformat(cap['started_at'])
deadlines = {'service_activation_utc': cap['started_at'], 'service_activation_monotonic': cap['started_monotonic'], 'recorded_at': now.isoformat(), 'observed_monotonic': time.monotonic(), 'clock_reset': False}
for minutes, label in [(45,'nonterminal_gate'),(90,'allocation_90'),(150,'allocation_150'),(210,'protected_end_discovery_cutoff'),(270,'consolidation_start'),(285,'workers_experiments_stop'),(295,'final_checkpoint')]:
    deadlines[label] = {'offset_minutes': minutes, 'utc': (start + dt.timedelta(minutes=minutes)).isoformat(), 'monotonic': cap['started_monotonic'] + 60*minutes}
for key in ['graceful_shutdown_at','scheduled_kill_at','hard_deadline_at']:
    deadlines[key] = cap[key]
atomic(OUT/'coordinator/deadlines.json', deadlines)
atomic(OUT/'coordinator/startup-cap-snapshot.json', cap)
atomic(OUT/'coordinator/startup-manifest-snapshot.json', manifest)
atomic(OUT/'coordinator/runtime-verification.json', {
    'recorded_at':now.isoformat(), 'requested_total_agents':3, 'reported_concurrency_slots':3,
    'observed_list_agents_receipt':{'agents':[{'agent_name':'/root','agent_status':'running'},{'agent_name':'/root/ff1','agent_status':'running'},{'agent_name':'/root/sv','agent_status':'running'}]},
    'root_model_evidence':{'source':'launcher-run.json/codex_command','argv':manifest['codex_command'],'requested_model':'gpt-6-astra','requested_reasoning_effort':'ultra','explicit_service_tier':'default','backend_billing_telemetry':'unavailable'},
    'spawn_receipts':[{'requested_task_name':'ff1','requested_model':'gpt-6-astra','requested_reasoning_effort':'ultra','fork_turns':'none','actual_receipt':{'task_name':'/root/ff1'}},{'requested_task_name':'sv','requested_model':'gpt-6-astra','requested_reasoning_effort':'ultra','fork_turns':'none','actual_receipt':{'task_name':'/root/sv'}}],
    'child_tier':{'configuration':'inherit root explicit default; assignments prohibit tier changes','spawn_api_service_tier_field':False,'available_receipts_do_not_report_tier':True,'backend_telemetry':'not verified'},
    'model_catalog_note':'Tool catalogue labels Astra priority availability, but spawn accepts no tier field. No requested change from root default; this discrepancy is disclosed and requires available metadata inspection, not silent tier selection.',
    'fast_mode':'true enables serialization; no Fast selection requested', 'os_process_observation':'Tool sandbox PID namespace does not expose enclosing Codex argv; manifest argv is launch configuration evidence only'
})
src=DD/'regressions.json'; registry=json.loads(src.read_text()); refs=[]
for group in ['inherited_entries','new_entries']:
    for i,entry in enumerate(registry[group]):
        refs.append({'id':entry['id'],'source_registry':str(src.relative_to(ROOT)),'source_registry_sha256':digest(src),'json_pointer':f'/{group}/{i}','entry_sha256':hashlib.sha256(json.dumps(entry,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'source_scope_disposition':entry.get('scope_disposition'),'source_review':entry.get('current_review'),'effective_status':'INHERITED-EXACT-SCOPE-REFERENCE','current_applicability':'PENDING changed-claim audit; historical rejection and guards remain binding','check_depth':'reference import and ID/count integrity; no recertification'})
assert len(refs)==203 and len({e['id'] for e in refs})==203
atomic(OUT/'regressions.json',{'schema_version':1,'created_at':now.isoformat(),'inherited_count':203,'inherited_entries':refs,'new_entries':[],'CP-1':'Mandatory support/normalization control; no sequential product from marginal probabilities','scope':'Exact references preserve all DD entries; per-new-claim applicability is pending'})
atomic(OUT/'claims.json',{'schema_version':1,'updated_at':now.isoformat(),'claims':[{'id':'FF-OBJECTIVE-v1','status':'OPEN','statement':'One target family fixed before all PPT sample and advantage exponents','dependencies':[]},{'id':'SV-OBJECTIVE-v1','status':'OPEN','statement':'Reviewed substantive algorithmic classification or compatible established hardness connection at the actual delivered source parameters','dependencies':[]},{'id':'HARDNESS-FOUNDATION','status':'OPEN','statement':'Independent established hardness premise connected by effective exact-parameter map','dependencies':[]}], 'inherited_graph':{'source':str((DD/'coordinator/acceptance-v1.json').relative_to(ROOT)),'sha256':digest(DD/'coordinator/acceptance-v1.json'),'check_depth':'intake in progress; exact version evidence controls stale provisional banners'}})
atomic(OUT/'experiments/registry.json',{'schema_version':1,'jobs':[],'limits':{'wall_default_seconds':120,'wall_max_seconds':300,'address_space_max_bytes':17179869184,'max_simultaneous_jobs':2,'max_heavy_jobs':1},'aggregate_memory_containment_claim':False})
atomic(OUT/'coordinator/protected-period-compliance.json',{'status':'IN_PROGRESS','protected_end_utc':deadlines['protected_end_discovery_cutoff']['utc'],'scientific_termination_allowed_before_end':False,'cooperative_not_os_productivity_enforcement':True,'records':[{'at':now.isoformat(),'roles':{'root':'FF2 alternatives and synthesis','ff1':'joint-law transfer','sv':'actual radius and source classification'},'finding':'Intake and assignments started; no scientific acceptance'}]})
atomic(OUT/'coordinator/checkpoints/000-startup.json',{'at':now.isoformat(),'service_elapsed_seconds':time.monotonic()-cap['started_monotonic'],'goal_status':'active','agent_roles':{'root':'FF2','ff1':'FF1','sv':'SV'},'frontier':'Inherited fixed theorem depends on sample and inverse advantage via noise. New universal fixed-family obligation OPEN. Actual source classification OPEN.','evidence':['coordinator/goal-creation-receipt.json','coordinator/deadlines.json','coordinator/runtime-verification.json','regressions.json'],'resume':'Read cap and current time; keep protected programme meaningful; reconstruct exact inherited interfaces then FF2 alternatives. Do not reset clock or create another goal.'})
for name,content in {
 'progress.md':'# Progress\n\nStartup: exact inherited intake and three-agent exploration active. Fixed-family reduction, source diagnostic and hardness foundation are OPEN.\n',
 'resume.md':'# Resume\n\nRead live cap, coordinator/deadlines.json, latest checkpoint, claims.json and programme-decisions.md. Existing native goal is active; never create a second goal. Research writes only here. No scientific termination before 21:18:10.636448 UTC. Root plus two active Astra ultra workers maximum, inherited default service.\n',
 'programme-decisions.md':'# Programme decisions\n\nStartup: FF1 investigates the full joint modulus-transfer law; SV reconstructs actual source radius and algorithmic regimes; root explores fixed-modulus selected-functional and controlled-hybrid alternatives. Initial failures redirect, not terminate. All new scientific claims remain open/provisional until exact full and blind reviews.\n',
 'reduction-attempts.md':'# Reduction attempts\n\nFF1 transfer, FF2 fixed-modulus functionals/hybrids and SV source classification are active. Each outcome will be evidence-linked and scoped; no exhaustion verdict.\n',
 'parameter-table.md':'# Parameter table\n\nInherited FIXED-MAIN-v2 requires sigma0 >= 8*k0*n*(n/2+2)/epsilon_*. This excludes the current fixed-family quantifier order. Exact source-radius reconstruction is assigned to SV.\n',
 'source-comparison.md':'# Source comparison\n\nPending actual-radius comparisons. Wide DGS simulation is not automatically a BDD algorithm. Failed sufficient conditions are not hardness.\n',
 'reconciliation.md':'# Reconciliation\n\nInherited exact acceptance is distinct from this new objective. No new acceptance yet. Same-model reviewers are correlated; no formal verification claim.\n',
 'coordinator/audit-ledger.jsonl':json.dumps({'at':now.isoformat(),'event':'STARTUP','status':'ACTIVE','FF':'OPEN','SV':'OPEN','hardness':'OPEN'})+'\n'
}.items():
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True)
    if not p.exists():p.write_text(content)
print(json.dumps({'at':now.isoformat(),'elapsed_minutes':(now-start).total_seconds()/60,'regressions':len(refs),'protected_end':deadlines['protected_end_discovery_cutoff']['utc']}))
