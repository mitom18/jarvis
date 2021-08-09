#!/bin/bash

start_file='start.sh'
start_script="$(cd $(dirname \"$start_file\"); pwd)/$(basename $start_file)"

stop_file='stop.sh'
stop_script="$(cd $(dirname \"$stop_file\"); pwd)/$(basename $stop_file)"

/bin/bash $stop_script

git fetch
git checkout -f main
git reset --hard origin/main

/bin/bash $start_script
