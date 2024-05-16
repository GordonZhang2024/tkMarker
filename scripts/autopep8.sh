#!/usr/bin/env bash

# This file is used to format the source files automatically

cd ../src
files=$(ls)

for i in $files; do
    if test -f $i; then
        autopep8 $i --in-place
    fi
done
