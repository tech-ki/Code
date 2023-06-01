'''
Created on September 20, 2021

@author: ciarraw
'''
from datetime import datetime

if __name__ == '__main__':
    pass
# ^^^^^^^^^ HEADER ^^^^^^^^^ 

now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")
current_day = now.strftime("%a. %b. %d. %Y")

print("The current time is: ", current_time)
print("The current day is: ", current_day)
print("The current day and time is: ", current_day , "@" , current_time)

## ----- Notes ---------------------------------
# comment: 12 hour formatting is %I
# 12 hour formatting (am / pm) is %p 
# PySimpleGUI is great for pop-ups 

## ----- Progress ---------------------------------
# Created: (Monday) [September] 09.20.2021
# 8:44pm - Done displaying current time


## ----- References ---------------------------------
# https://www.programiz.com/python-programming/datetime/current-time @CurrentTime

