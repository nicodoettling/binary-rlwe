#!/bin/bash
set -eu
TASK_DIR=/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/criticism/BT12
cd "$TASK_DIR"
timeout --signal=TERM --kill-after=5s 120s python3 fv1.py > fv1-stdout.txt 2> fv1-stderr.txt
