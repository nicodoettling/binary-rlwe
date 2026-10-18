#!/usr/bin/env bash
set -eu
ulimit -v 524288
cd /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/workers/G/planted-information-review
/usr/bin/time -v timeout 120s python3 -B finite-control-v1.py > finite-control-v1.stdout.json 2> finite-control-v1.stderr.txt
