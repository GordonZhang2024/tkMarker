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

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

REPOS_URL = 'https://github.com/GordonZhang2024/tkMarker'
ISSUE_URL = 'https://github.com/GordonZhang2024/tkMarker/issues'


def show_project_info():
    """
    Function show_project_info()
    Show the project infomation
    """
    info_page = tkinter.Tk()
    info_page.title('About')
    info_page.config(cursor='star')
    label = ttk.Label(
        info_page,
        text='tkMarker\nA Markdown editor using tkinter'
    )
    label.pack()

    github_repos = ttk.Button(
        info_page,
        text='GitHub',
        command=open_github_repos
    )
    issue_tracker = ttk.Button(
        info_page,
        text='Report an issue',
        command=open_issue_url
    )
    github_repos.pack()
    issue_tracker.pack()
    info_page.mainloop()


def open_github_repos():
    """
    Function open_github_repos()
    Open the GitHub repository
    """
    webbrowser.open_new(REPOS_URL)


def open_issue_url():
    # Open the issue tracker
    webbrowser.open_new(ISSUE_URL)
