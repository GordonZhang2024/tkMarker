import tkinter
import webbrowser
import os
from tkinter import filedialog, scrolledtext
from converter import convert

def load_preview():
    markdown_text_for_preview = text.get('1.0', 'end')
    preview_file = f'{home}/.tkmarker_preview'
    html = convert(markdown_text_for_preview)
    with open(preview_file, 'w') as p:
        p.write(html)

    webbrowser.open(preview_file)

def open_file():
    pass

def save():
    global file_name
    if file_name == 'New File':
        file_name = filedialog.asksaveasfilename(initialdir='~/Documents')
        editor.title(file_name)
        
    markdown_text = text.get('1.0', 'end')
    with open(file_name, mode='w+') as f:
        f.write(markdown_text)
        
def new_file():
    global file_name
    global editor
    editor = tkinter.Tk()
    editor.title(file_name)
    menubar = tkinter.Menu(editor)
    file = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    menubar.add_command(label='Preview', command=load_preview)
    
    global text
    text = scrolledtext.ScrolledText(editor)
    text.grid()

    #file.add_command(label='New File')
    #file.add_command(label='Open...')
    file.add_command(label='Save', command=save)

    editor.config(menu=menubar)
    editor.mainloop()

home = os.path.expanduser('~')
file_name = 'New File'
new_file()
