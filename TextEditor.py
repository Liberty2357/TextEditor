# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showerror

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0,END)


def saveFile():
    global filename
    if filename is None:
        showerror(title="Error", message="Please use 'Save As' to specify a file path before saving.")
        return

    t = text.get(0.0, END)
    
    try:
        f = open(filename, 'w')
        f.write(t)
        f.close()
    except Exception as e:
        showerror(title="Oops!", message=f"Unable to save file. Error: {e}")

    
def saveAs():
    file = asksaveasfile(mode='w', defaultextension=".txt")
    if file is None:
        return  # �û����ȡ����ť

    t = text.get(0.0, END)
    
    try:
        if file.writable():
            file.write(t.rstrip())
        else:
            showerror(title="Oops!", message="Unable to save file. File is not writable.")
    except Exception as e:
        showerror(title="Oops!", message=f"Unable to save file. Error: {e}")


def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

root = Tk()
root.title("TextEditor")
root.minsize(width=400,height=400)
root.maxsize(width=500,height=500)

text = Text(root,width=400,height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save As",command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
root.mainloop()