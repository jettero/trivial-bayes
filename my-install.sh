#!/usr/bin/env bash

echo
echo $'\e'"[1;35m""test phase"$'\e'"[m"
echo

DIR="$(dirname "$0")"
"$DIR"/my-test.sh || exit 1

echo
echo $'\e'"[1;35m""test phase complete"$'\e'"[m"
echo $'\e'"[1;35m""installing"$'\e'"[m"
echo

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
