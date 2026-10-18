#!/usr/bin/env bash
set -euo pipefail
ulimit -t 120
ulimit -v 262144
/usr/bin/time -v -o F-QFINITE-FV1.resources python3 -B F-QFINITE-FV1.py > F-QFINITE-FV1.stdout 2> F-QFINITE-FV1.stderr
