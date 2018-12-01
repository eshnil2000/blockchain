#!/usr/bin/env sh

set -x
python blockchain.py &
sleep 1
echo $! > .pidfile
set +x
