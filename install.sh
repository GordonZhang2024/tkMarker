#!/usr/bin/bash
tkMarker_dir=$(pwd)
src_dir="${tkMarker_dir}/src/"
dist_dir="${tkMarker_dir}/dist/main/"

#desktop_icon="
#[Desktop Entry]\nTerminal=false\nExec=$tkMarker_dir/dist/main/main\nName=tkMarker\nType=Application\nIcon=$tkMarker_dir/icon.png\n
#"
#sudo echo -e $desktop_icon > /usr/share/applications/tkmarker.desktop

sudo ln -s "${dist_dir}/main" /usr/bin/tkmarker

