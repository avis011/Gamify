from tkinter import *
import tkinter.messagebox as ty
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)


def openfile():
    global file
    file=askopenfilename(defaultextention=".txt",
                         filetypes=[("All Files","*.*"),("Text Document","*.txt")
                         ])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()



def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextention=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file=='':
            file=None
        else:
            f=open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")
            print("File Saved")
    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def info():
    a = ty.showinfo('Info', "This simple Notepad is made by Hardik")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    # Writing Area
    TextArea=Text(root,font="Lucicda 15")
    file=None
    TextArea.pack(fill=BOTH,expand=True)
    #Menubar
    Menubar=Menu(root)
    #
    Filemenu=Menu(Menubar,tearoff=0)
    #to open new file
    Filemenu.add_command(label="New",command=newfile)
    #to Open already existind file
    Filemenu.add_command(label="Open",command=openfile)
    #to save a file
    Filemenu.add_command(label="Save",command=savefile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command=quitapp)
    Menubar.add_cascade(label="File",menu=Filemenu)
    #

    #edit
    Edit=Menu(Menubar,tearoff=0)
    Edit.add_command(label="Cut",command=cut)
    Edit.add_command(label="Copy",command=copy)
    Edit.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=Edit)

    m2 = Menu(Menubar, tearoff=0)
    m2.add_command(labe="Info", command=info)
    Menubar.add_cascade(label="Info", menu=m2)

    root.config(menu=Menubar)
    #scrollbar
    scrollbar=Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)

    root.mainloop()
