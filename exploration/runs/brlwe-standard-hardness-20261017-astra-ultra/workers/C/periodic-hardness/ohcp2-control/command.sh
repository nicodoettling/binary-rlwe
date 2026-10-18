#!/usr/bin/env bash
set -u
ulimit -v 262144
ulimit -t 25
cd /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/workers/C/periodic-hardness/ohcp2-control
/usr/bin/timeout --signal=KILL 30s /usr/bin/time -v -o resources.txt python3 control.py > stdout.json 2> stderr.txt
run_status=$?
python3 - "$run_status" <<'PY'
import sys,json,datetime
from pathlib import Path
Path('exit-status.json').write_text(json.dumps({'exit_code':int(sys.argv[1]),'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wall_limit_seconds':30,'address_space_limit_bytes':256*1024**2},indent=2)+'\n')
PY
exit "$run_status"
