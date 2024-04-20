#!/usr/bin/bash

cd ../src/

files=$(ls)
pylint $files

