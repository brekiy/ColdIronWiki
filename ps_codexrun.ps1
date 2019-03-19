#!/bin/bash

#if [ ! -f var/insta485.sqlite3 ]; then
#  echo + ./bin/insta485db create
#  ./bin/insta485db create
#fi

$env:FLASK_DEBUG="1"
$env:FLASK_APP="codex"
$env:CODEX_SETTINGS="config.py"

flask run --host 0.0.0.0 --port 8000
