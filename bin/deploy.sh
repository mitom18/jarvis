#!/bin/bash

start_script="bin/start.sh"
stop_script="bin/stop.sh"

/bin/bash $stop_script

git fetch
git checkout -f main
git reset --hard origin/main

/bin/bash $start_script
