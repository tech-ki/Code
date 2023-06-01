'''
Created on Nov 18, 2021

@author: ciarraw
'''

#Testing clock
 
# importing strftime function to retrieve system's time
import tkinter as tk
from time import strftime
 
# creating tkinter window
root = tk.Tk()
root.title('Clock')
 
# This function is used to display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
    lbl.config(bg='yellow')
 
# Styling the label widget so that clock will look more attractive
lbl = tk.Label(root, font = ('arial', 40, 'bold'),
            background = 'black',
            foreground = 'yellow')
root.config(bg='yellow')
 
# Placing clock at the center of the tkinter window
lbl.pack(anchor = 'center')
time()
 
root.mainloop()

