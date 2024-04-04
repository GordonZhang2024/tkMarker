#!/usr/bin/python3

"""
Module get_help:
Get the help
"""

import tkinter
from tkinter import ttk
import webbrowser

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

    github_repos = ttk.Button(info_page, text=REPOS_URL, command=open_github_repos)
    github_repos.pack()
    info_page.mainloop()

def open_github_repos():
    """
    Function open_github_repos()
    Open the GitHub repository
    """
    webbrowser.open_new(REPOS_URL)
