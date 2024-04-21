#!/usr/bin/bash

#tkMarker
#    A Markdown editor using tkinter
#Copyright (C) 2024 Gordon Zhang
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

tkMarker_dir=$(pwd)
src_dir="${tkMarker_dir}/src/"
dist_dir="${tkMarker_dir}/dist/main/"

#desktop_icon="
#[Desktop Entry]\nTerminal=false\nExec=$tkMarker_dir/dist/main/main\nName=tkMarker\nType=Application\nIcon=$tkMarker_dir/icon.png\n
#"
#sudo echo -e $desktop_icon > /usr/share/applications/tkmarker.desktop

sudo ln -s "${dist_dir}/main" /usr/bin/tkmarker
cd ~
mkdir .tkmarker/
