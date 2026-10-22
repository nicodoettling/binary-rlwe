#!/usr/bin/env python3
import datetime,json,subprocess,time
from pathlib import Path
p=Path(__file__).resolve().parent
cmd=['/usr/bin/time','-v','-o',str(p/'exact-check-time.txt'),'timeout','--signal=TERM','--kill-after=5s','120s','prlimit','--as=536870912','--cpu=120','--','python3','-I',str(p/'independent_exact_check.py')]
start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
with (p/'exact-check-stdout.json').open('wb') as out,(p/'exact-check-stderr.txt').open('wb') as err:
    r=subprocess.run(cmd,stdout=out,stderr=err,cwd=p,check=False)
receipt={'command':cmd,'started_at':start,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t,'returncode':r.returncode,'timeout_seconds':120,'kill_after_seconds':5,'address_space_bytes':536870912,'cpu_seconds':120,'cleanup':'No child services, temporary files or persistent processes requested; timeout owns any experiment child.'}
(p/'exact-check-run-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
raise SystemExit(r.returncode)
