#!/usr/bin/python3
import tkinter
from tkinter import ttk
import webbrowser
import os
from tkinter import filedialog, scrolledtext

from converter import convert

def load_preview():
    markdown_text_for_preview = text.get('1.0', 'end')
    preview_file = f'{home}/.tkmarker_preview'
    html = convert(markdown_text_for_preview, preview=True)
    with open(preview_file, 'w') as p:
        p.write(html)

    webbrowser.open_new(preview_file)

def refresh_preview(arg):
    markdown_text_for_preview = text.get('1.0', 'end')
    preview_file = f'{home}/.tkmarker_preview'
    html = convert(markdown_text_for_preview, preview=True)
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
    file_name = filedialog.askopenfilename(initialdir='~/Documents', filetypes=[('Markdown', '*.md'), ("All Files", "*.*")])
    with open(file_name) as f:
        t = f.read()
    text.delete(1.0, tkinter.END)
    text.insert(tkinter.END, t)
    editor.title(file_name)

def save():
    global file_name
    if file_name == 'New File':
        file_name = filedialog.asksaveasfilename(initialdir='~/Documents', filetypes=[('Markdown', '*.md'), ("All Files", "*.*")])
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

    file = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)

    global edit
    edit = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Edit', menu=edit)

    menubar.add_command(label='Preview', command=load_preview)

    global text
    text = scrolledtext.ScrolledText(editor, undo=True)
    text.pack(fill='both', expand=True)
    text.focus_set()

    file.add_command(label='Open...', command=open_file)
    file.add_command(label='Save', command=save)
    file.add_command(label='Convert to HTML', command=convert_to_html)

    edit.add_command(label='Paste', command=paste)
    edit.add_command(label='Copy', command=copy)
    edit.add_command(label='Cut', command=cut)
    editor.config(menu=menubar)
    editor.bind('<Button-3>', show_popup_menu)
    editor.bind('<KeyRelease>', refresh_preview)
    editor.bind('Control-C', copy)
    editor.bind('Control-V', paste)
    editor.bind('Control-S', save)
    editor.mainloop()
   
if __name__ == '__main__':
    home = os.path.expanduser('~')
    file_name = 'New File'
    new_file()

