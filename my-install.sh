#!/usr/bin/env bash

if [ $# -gt 0 ]
then A=( "$@" )
else A=( pip2 pip3 )
fi

for pip in "${A[@]}"
do (set -x; "$pip" install .)
done

echo
echo testing imports
( cd /tmp
  for i in python2 python3; do
      echo -n "$i: "
      $i -c "import nbayes; print('$i can import nbayes')"
  done
)
