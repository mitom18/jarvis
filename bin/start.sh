#!/bin/bash

if [ -e ./temp ]
then
  pid=`cat temp`
  echo "Process already exists; $pid"
else
  script='jarvis.py'
  echo "starting $script with nohup"
  nohup python3 $script &
  echo $! > temp
fi
