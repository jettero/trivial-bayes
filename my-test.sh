#!/usr/bin/env bash

if [ $# -gt 0 ]
then A=( "$@" )
else A=( python2 python3 )
fi

x=0
for python in "${A[@]}"
do (set -x; "$python" ./setup.py test); x=$(( x + $? ))
done

exit $x
