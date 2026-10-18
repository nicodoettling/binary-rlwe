#!/usr/bin/env bash
set -eu
ulimit -v 262144
exec /usr/bin/time -v -o finite-controls-resources-v1.txt timeout 30s python3 finite-controls-v1.py > finite-controls-stdout-v1.txt 2> finite-controls-stderr-v1.txt
