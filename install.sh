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

ln -s "${src_dir}editor.py" ~/.local/bin/tkmarker
cd ~
mkdir .tkmarker/
