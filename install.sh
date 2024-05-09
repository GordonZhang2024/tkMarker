#!/usr/bin/bash

#tkMarker
#    A Markdown editor using tkinter
#Copyright (C) 2024 Gordon Zhang

tkMarker_dir=$(pwd)
src_dir="${tkMarker_dir}/src/"

ln -s "${src_dir}editor.py" ~/.local/bin/tkmarker
cd ~
mkdir .tkmarker/
