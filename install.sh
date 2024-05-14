#!/usr/bin/bash

# tkMarker
#     A Markdown editor using tkinter
# Copyright (C) 2024 Gordon Zhang

echo -e "\x1b[36mInstalling tkMarker\x1b[0m ..."
echo -e "Website: https://gordonzhang.pythonanywhere.com/projects/tkMarker/"
echo -e "License: \x1b[1mMIT License\x1b[0m"


tkMarker_dir=$(pwd)
src_dir="${tkMarker_dir}/src/"

echo "Creating symbolic link (~/.local/bin/tkmarker)"
ln -s "${src_dir}editor.py" ~/.local/bin/tkmarker

echo "Creating .tkMarker directory"
cd ~
mkdir .tkmarker/

echo -e "\x1b[32mComplete!\x1b[0m"
