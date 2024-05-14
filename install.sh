#!/usr/bin/bash

# tkMarker
#     A Markdown editor using tkinter
# Copyright (C) 2024 Gordon Zhang


echo -e "\x1b[1mtkMarker |  A Markdown editor\x1b[0m"
echo    "Copyright (C) 2024 Gordon Zhang"
echo    "Website: https://gordonzhang.pythonanywhere.com/projects/tkMarker/"
echo -e "License: \x1b[1mMIT License\x1b[0m"
echo

echo -e "\x1b[36mInstalling tkMarker\x1b[0m ..."

if test -f ~/.local/bin/tkmarker; then
    echo "It seems like you have already installed tkmarker."
else
    if test -f /usr/bin/python -o -f /bin/python -o -f ~/.local/bin/python; then
        tkMarker_dir=$(pwd)
        src_dir="${tkMarker_dir}/src/"

        echo "Creating symbolic link (~/.local/bin/tkmarker)"
        ln -s "${src_dir}editor.py" ~/.local/bin/tkmarker

        echo "Creating .tkMarker directory"
        cd ~
        mkdir .tkmarker/

        echo -e "\x1b[32mComplete!\x1b[0m"
        echo -e "Type command \x1b[3;4mtkmarker\x1b[0m to run it :)"
    else
        echo "Please install Python first."
    fi
fi

