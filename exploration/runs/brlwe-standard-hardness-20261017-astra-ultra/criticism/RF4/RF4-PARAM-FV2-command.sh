#!/bin/bash
set -eu
cd /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/criticism/RF4
ulimit -t 10
ulimit -v 65536
/usr/bin/time -v -o RF4-PARAM-FV2.resources timeout 10s python3 RF4-PARAM-FV2.py > RF4-PARAM-FV2.stdout 2> RF4-PARAM-FV2.stderr
