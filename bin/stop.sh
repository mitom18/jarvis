#!/bin/bash

if [ -e ./temp ]
then
  pid=`cat temp`
  echo "killing $pid"
  kill $pid
  rm temp
else
  echo "Process not started"
fi
