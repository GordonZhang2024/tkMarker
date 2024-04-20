#!/usr/bin/env python3

"""
Module get_help:
Get the help
"""

import tkinter
from tkinter import ttk
import webbrowser

"""
tkMarker
    A Markdown editor using tkinter
Copyright (C) 2024 Gordon Zhang

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

REPOS_URL = 'https://github.com/GordonZhang2024/tkMarker'


def show_project_info():
    """
    Function show_project_info()
    Show the project infomation
    """
    info_page = tkinter.Tk()
    info_page.title('About')
    label = ttk.Label(info_page, text='tkMarker')
    label.pack()

    github_repos = ttk.Button(
        info_page, text=REPOS_URL, command=open_github_repos)
    github_repos.pack()
    info_page.mainloop()


def open_github_repos():
    """
    Function open_github_repos()
    Open the GitHub repository
    """
    webbrowser.open_new(REPOS_URL)
