#!/usr/bin/env bash

if [ $# -gt 0 ]
then A=( "$@" )
else A=( python2 python3 )
fi

for python in "${A[@]}"
do "$python" ./setup.py test
done