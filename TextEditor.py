# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showerror


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.filename = None

<<<<<<< HEAD

def saveFile():
    global filename
    if filename is None:
        showerror(title="Error", message="Please use 'Save As' to specify a file path before saving.")
        return
=======
        self.setup_ui()
>>>>>>> 2157501c88d5c652b32784c7de22bb06f5090823

    def setup_ui(self):
        """
        Setup the UI of the text editor
        """
        self.text = Text(self.root, width=400, height=400)
        self.text.pack()

<<<<<<< HEAD
    
def saveAs():
    file = asksaveasfile(mode='w', defaultextension=".txt")
    if file is None:
        return  # �û����ȡ����ť
=======
        menubar = Menu(self.root)
        filemenu = Menu(menubar)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)
>>>>>>> 2157501c88d5c652b32784c7de22bb06f5090823

    def new_file(self):
        self.filename = "Untitled"
        self.text.delete(0.0, END)

    def save_file(self):
        if self.filename is None:
            showerror(
                title="Error",
                message="Please use 'Save As' to specify a file path before saving.",
            )
            return

        t = self.text.get(0.0, END)

        try:
            with open(self.filename, "w") as f:
                f.write(t)
        except Exception as e:
            showerror(title="Oops!", message=f"Unable to save file. Error: {e}")

    def save_as(self):
        file = asksaveasfile(
            mode="w",
            defaultextension=".txt",
            filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
        )
        if file is None:
            return

        t = self.text.get(0.0, END)

        try:
            file.write(t.rstrip())
        except Exception as e:
            showerror(title="Oops!", message=f"Unable to save file. Error: {e}")
        finally:
            file.close()

<<<<<<< HEAD
=======
    def open_file(self):
        file = askopenfile(mode="r")
        if file is None:
            return
>>>>>>> 2157501c88d5c652b32784c7de22bb06f5090823

        with file:
            t = file.read()
            self.text.delete(0.0, END)
            self.text.insert(0.0, t)


if __name__ == "__main__":
    root = Tk()
    root.title("TextEditor")
    root.minsize(width=400, height=400)
    root.maxsize(width=500, height=500)

    text_editor = TextEditor(root)

    root.mainloop()
