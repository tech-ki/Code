# Python program to illustrate a stop watch
# using Tkinter
#importing the required libraries
from pickle import MARK
import tkinter as Tkinter
from datetime import datetime
import tkinter as tink

from matplotlib import markers
count = -1
run = False
def var_name(mark):
   def value():
      if run:
         global count
         # Just before starting
         if count == -1:
            show = "Starting"
         else:
            show = str(count)
         mark['text'] = show

         tt = datetime.fromtimestamp(count)
         string = tt.strftime("%H:%M:%S")
         display=string

         #Increment the count after
         #every 1 second
         mark.after(1, value)
         count += 1
   value()
# While Running
def Start(mark):
   global run
   run = True
   var_name(mark)
   start['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'
# While stopped
def Stop():
   global run
   start['state'] = 'normal'
   stop['state'] = 'disabled'
   reset['state'] = 'normal'
   run = False
# For Reset
def Reset(label):
   global count
   count = -1
   if run == False:
      reset['state'] = 'disabled'
      MARK['text'] = 'Welcome'
   else:
      MARK['text'] = 'Start'

root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")
root.mainloop()
