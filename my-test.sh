#!/usr/bin/env bash

if [ $# -gt 0 ]
then A=( "$@" )
else A=(
    /usr/local/python/python2.7/bin/python
    /usr/local/python/python3.6/bin/python
    )
fi

x=0
for python in "${A[@]}"
do (set -x; "$python" ./setup.py test); x=$(( x + $? ))
done

exit $x
