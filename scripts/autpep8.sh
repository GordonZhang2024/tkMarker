#!/usr/bin/env bash

cd ../src
files=$(ls)

for i in $files; do
    if test -f $i; then
        autopep8 $i --in-place
    fi
done
