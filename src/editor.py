#!/usr/bin/env python3

"""
module main
The main program of tkMarker
"""

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

import tkinter
import webbrowser
import os
from tkinter import filedialog, scrolledtext
import uuid

from converter import convert
from get_help import show_project_info

#filetypes
filetypes = [('Markdown', '*.md'), ("All Files", "*.*")]

def load_preview():
    #Load the preview
    markdown_text_for_preview = text.get('1.0', 'end') #Get the text
    preview_file = f'{home}/.tkmarker/{file_uuid}'
    html = convert(markdown_text_for_preview, preview=True, file_path=os.path.split(file_name))
    with open(preview_file, 'w+') as p:
        p.write(html)

    #Open the preview file in the webbrowser
    webbrowser.open_new(preview_file)

def refresh_preview(arg):
    markdown_text_for_preview = text.get('1.0', 'end')
    preview_file = f'{home}/.tkmarker/{file_uuid}'
    html = convert(markdown_text_for_preview, preview=True, file_path=os.path.split(file_name))
    with open(preview_file, 'w') as p:
        p.write(html)

def convert_to_html():
    markdown_text = text.get('1.0', 'end')
    output_file = filedialog.asksaveasfilename(filetypes=[('HTML', '*.html')])
    html = convert(markdown_text)
    with open(output_file, 'w') as o_file:
        o_file.write(html)

def show_popup_menu(event):
    edit.post(event.x_root,event.y_root)

def paste():
    text.event_generate('<<Paste>>')

def copy():
    text.event_generate('<<Copy>>')

def cut():
    text.event_generate('<<Cut>>')

def open_file():
    global file_name
    file_name = filedialog.askopenfilename(initialdir='~/Documents', filetypes=filetypes)
    with open(file_name) as f:
        t = f.read()
    text.delete(1.0, tkinter.END)
    text.insert(tkinter.END, t)
    editor.title(file_name)

def save():
    global file_name
    if file_name == 'New File':
        file_name = filedialog.asksaveasfilename(initialdir='~/Documents', filetypes=filetypes)
        editor.title(file_name)

    markdown_text = text.get('1.0', 'end')
    with open(file_name, mode='w+') as f:
        f.write(markdown_text)

def new_file():
    global file_name
    global editor
    editor = tkinter.Tk()
    editor.title(file_name)
    width= editor.winfo_screenwidth()
    height= editor.winfo_screenheight()
    editor.geometry("%dx%d" % (width, height))
    menubar = tkinter.Menu(editor)

    #Add the 'File' menubar
    file = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)

    #Add the 'Edit' menubar
    global edit
    edit = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Edit', menu=edit)

    #Add the 'Help' menubar
    help_menu = tkinter.Menu(editor, tearoff=0)
    menubar.add_cascade(label='Help', menu=help_menu)

    #Add the 'Preview' button
    menubar.add_command(label='Preview', command=load_preview)

    global text
    text = scrolledtext.ScrolledText(editor, undo=True)
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

    #Add keyboard shortcuts
    editor.bind('<Button-3>', show_popup_menu)
    editor.bind('Control-C', copy)
    editor.bind('Control-V', paste)
    editor.bind('Control-S', save)

    #Refresh Automatically
    editor.bind('<KeyRelease>', refresh_preview)
    
    editor.mainloop()

if __name__ == '__main__':
    #Init
    home = os.path.expanduser('~')
    file_name = 'New File'
    global file_uuid
    file_uuid = uuid.uuid1()

    new_file()