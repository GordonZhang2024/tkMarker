#!/usr/bin/env python3

"""
module main
The main program of tkMarker
"""

import tkinter
import webbrowser
import os
from tkinter import filedialog, scrolledtext
import uuid

from converter import convert
from get_help import show_project_info

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

# filetypes
filetypes = [('Markdown', '*.md'), ("All Files", "*.*")]


def load_preview():
    # Load the preview
    markdown_text_for_preview = text.get('1.0', 'end')  # Get the text
    preview_file = f'{home}/.tkmarker/{file_uuid}'
    html = convert(markdown_text_for_preview, preview=True,
                   file_path=os.path.split(filename))
    with open(preview_file, 'w+', encoding='utf-8') as p:
        p.write(html)

    # Open the preview file in the webbrowser
    webbrowser.open_new(preview_file)


def refresh_preview(arg):
    # Refresh the preview
    markdown_text_for_preview = text.get('1.0', 'end')
    preview_file = f'{home}/.tkmarker/{file_uuid}'
    html = convert(markdown_text_for_preview, preview=True,
                   file_path=os.path.split(filename))

    with open(preview_file, 'w', encoding='utf-8') as p:
        p.write(html)


def convert_to_html():
    # Convert Markdown document to HTML
    markdown_text = text.get('1.0', 'end')
    output_file = filedialog.asksaveasfilename(filetypes=[('HTML', '*.html')])
    html = convert(markdown_text)
    with open(output_file, 'w', encoding='utf-8') as o_file:
        o_file.write(html)


def show_popup_menu(event):
    # Show the popup menu
    edit.post(event.x_root, event.y_root)


def paste():
    # Paste
    text.event_generate('<<Paste>>')


def copy():
    # Copy
    text.event_generate('<<Copy>>')


def cut():
    # Cut
    text.event_generate('<<Cut>>')


def open_file():
    # open a file
    global filename
    filename = filedialog.askopenfilename(
        initialdir='~/Documents', filetypes=filetypes)
    with open(filename, encoding='utf-8') as f:
        t = f.read()
    text.delete(1.0, tkinter.END)
    text.insert(tkinter.END, t)
    editor.title(filename)


def save():
    # Save
    global filename
    if filename == 'New File':
        filename = filedialog.asksaveasfilename(
            initialdir='~/Documents', filetypes=filetypes)
        editor.title(filename)

    markdown_text = text.get('1.0', 'end')
    with open(filename, 'w+', encoding='utf-8') as f:
        f.write(markdown_text)


def new_file():
    # pen new file
    global filename
    global editor
    editor = tkinter.Tk()
    editor.title(filename)

    # Set full screen
    width = editor.winfo_screenwidth()
    height = editor.winfo_screenheight()
    editor.geometry(f'{width}x{height}')
    menubar = tkinter.Menu(editor)

    # Add the 'File' menubar
    file = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)

    # Add the 'Edit' menubar
    global edit
    edit = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Edit', menu=edit)

    # Add the 'Help' menubar
    help_menu = tkinter.Menu(editor, tearoff=0)
    menubar.add_cascade(label='Help', menu=help_menu)

    # Add the 'Preview' button
    menubar.add_command(label='Preview', command=load_preview)

    global text
    text = scrolledtext.ScrolledText(editor, undo=True, font='Consolas')
    text.pack(fill='both', expand=True)
    text.focus_set()

    file.add_command(label='Open...', command=open_file)
    file.add_command(label='Save', command=save)
    file.add_separator()
    file.add_command(label='Convert to HTML', command=convert_to_html)

    edit.add_command(label='Paste', command=paste)
    edit.add_command(label='Copy', command=copy)
    edit.add_command(label='Cut', command=cut)

    editor.config(menu=menubar)

    help_menu.add_command(label='About', command=show_project_info)

    # Add keyboard shortcuts
    editor.bind('<Button-3>', show_popup_menu)
    editor.bind('Control-C', copy)
    editor.bind('Control-V', paste)
    editor.bind('Control-S', save)

    # Refresh Automatically
    editor.bind('<KeyRelease>', refresh_preview)

    editor.mainloop()


if __name__ == '__main__':
    # Init
    home = os.path.expanduser('~')
    filename = 'New File'
    global file_uuid
    file_uuid = uuid.uuid1()

    new_file()
