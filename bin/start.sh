#!/bin/bash

if [ -e ./temp ]
then
  pid=`cat temp`
  echo "Process already exists; $pid"
else
  file='../jarvis.py'
  script="$(cd $(dirname \"$file\"); pwd)/$(basename $file)"
  echo "starting $script with nohup"
  nohup python3 $script &
  echo $! > temp
fi
