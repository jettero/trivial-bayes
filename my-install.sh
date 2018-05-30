#!/usr/bin/env bash

if [ $# -gt 0 ]
then A=( "$@" )
else A=( pip2 pip3 )
fi

for pip in "${A[@]}"
do "$pip" install .
done
