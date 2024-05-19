#!/usr/bin/env python3

"""
module main
The main program of tkMarker
"""
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import webbrowser
import os
from tkinter import filedialog
import uuid

from converter import convert
import get_help

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

# Availible filetypes for the file selection window
filetypes = [
    ('Markdown', '*.md'),
    ("All Files", "*.*")
]


def show_project_info():
    get_help.show_project_info()

def load_preview():
    # Load the preview
    markdown_text_for_preview = text.get('1.0', 'end')  # Get the text

    # Use uuid as the name of the preview file
    preview_file = f'{home}/.tkmarker/{file_uuid}'

    # Convert the Markdown document to HTML and write to the preview file
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
    # Open a file
    global filename
    filename = filedialog.askopenfilename(
        initialdir='~/Documents',
        filetypes=filetypes
    )

    with open(filename, encoding='utf-8') as f:
        t = f.read()

    # Insert the text into the editor
    text.delete(1.0, ttk.END)
    text.insert(ttk.END, t)
    editor.title(filename)


def save():
    # Save
    global filename
    if filename == 'New File':
        filename = filedialog.asksaveasfilename(
            initialdir='~/Documents',
            filetypes=filetypes
        )

        # Set the filename as the title of the window
        editor.title(filename)

    markdown_text = text.get('1.0', 'end')
    with open(filename, 'w+', encoding='utf-8') as f:
        f.write(markdown_text)


def new_file():
    # Open new file
    global filename
    filename = 'New File'
    global editor
    editor = ttk.Window(themename='lumen')
    editor.title(filename)
    editor.wm_title('tkMarker')

    # Set full screen
    #editor.geometry('1000x1000')
    menubar = ttk.Menu(editor)

    # Add the 'File' menubar
    file = ttk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)

    # Add the 'Edit' menubar
    global edit
    edit = ttk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Edit', menu=edit)

    # Add the 'Help' menubar
    help_menu = ttk.Menu(editor, tearoff=0)
    menubar.add_cascade(label='Help', menu=help_menu)

    # Add the 'Preview' button
    menubar.add_command(label='Preview', command=load_preview)

    # Add the text area
    global text
    text = ttk.ScrolledText(editor, undo=True, font=('Sans Mono', 15))
    text.pack(fill='both', expand=True)

    # Set focus
    text.focus_set()

    # Add the "file" menu
    file.add_command(label='Open...', command=open_file)
    file.add_command(label='Save', command=save)
    file.add_separator()
    file.add_command(label='Convert to HTML', command=convert_to_html)

    # Add the "edit" menu
    edit.add_command(label='Paste', command=paste)
    edit.add_command(label='Copy', command=copy)
    edit.add_command(label='Cut', command=cut)
    edit.add_separator()
    edit.add_command(label='Hide this menu')

    # Pack the menubar
    editor.config(menu=menubar)

    # Add the About menu
    help_menu.add_command(label='About', command=show_project_info)

    # Add keyboard shortcuts
    editor.bind('<Button-3>', show_popup_menu)
    editor.bind('Control-C', copy)
    editor.bind('Control-V', paste)
    editor.bind('Control-S', save)
    editor.bind('Control-P', load_preview)
    editor.bind('<F1>', show_project_info)

    # Refresh Automatically
    editor.bind('<KeyRelease>', refresh_preview)

    editor.mainloop()


if __name__ == '__main__':
    # Init
    home = os.path.expanduser('~')
    global file_uuid
    file_uuid = uuid.uuid1()

    # Start the editor
    new_file()
