#comment
#Dec 12.08.2020 (Tuesday)
# 2020. 12. 08 (2)
#Goal open a new window

import tkinter as tk
from tkinter import *

def createNewWindow(): #def is a function not a class
    newWindow = tk.Toplevel(app)
    newWindow.geometry('500x500') #windowsize

app = tk.Tk()
buttonEx = tk.Button(app,
                     text="Create new window" ,
                     command=createNewWindow)
buttonEx.pack()


#testing input (top)

top = tk.Tk()
L1 = Label(top, text="Hour")
L1.pack( side = LEFT)
E1 = Entry(top, bd =0)
E1.pack(side = RIGHT)




top.mainloop()
app.mainloop()


##Reference Sheet
#@(1) Creating Window ~ https://www.delftstack.com/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
#@(2) Input ~ 
