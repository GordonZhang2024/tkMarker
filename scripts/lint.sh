#!/usr/bin/env bash

# This file is used to lint the source files

cd ../src/

files=$(ls)
pylint $files
