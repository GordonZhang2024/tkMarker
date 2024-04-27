#!/usr/bin/env bash

cd ../src/

files=$(ls)
pylint $files
