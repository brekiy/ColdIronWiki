#!/bin/bash

#if [ ! -f var/insta485.sqlite3 ]; then
#  echo + ./bin/insta485db create
#  ./bin/insta485db create
#fi

export FLASK_DEBUG=True
$env:FLASK_APP="codex"
export CODEX_SETTINGS=config.py

flask run --host 0.0.0.0 --port 8000
