from tkinter import *
from tkinter.ttk import *
from time import strftime
import pyfiglet

fig = pyfiglet.figlet_format("Avi's program",font="slant")
print(fig)
root=Tk()
root.title('Clock')
def time():
    string=strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000,time)
lbl=Label(root,font=('slant',40,'bold'),
          background='black',foreground='white')
lbl.pack(anchor='center')
time()
mainloop()

