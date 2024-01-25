# Program to display calendar of the given month and year

# importing calendar module
import calendar
from datetime import  datetime

yy = 2022  # year
mm = 12    # month
now = datetime.now() #year-month-day hour:min:sec.ms
nnow = now.date()
daymin = 1440 
hour = datetime.now().hour
nowmin = datetime.now().minute #current minutes out of hour
day = datetime.now().day #current day of the month
birth = datetime(1995, 4, 30)
birthd = birth.date()
agem =  (now - datetime(1995, 4, 30))
aged =  (now - datetime(1995, 4, 30)).days


day_of_year = (now - datetime(now.year, 1, 1)).days + 1

# display the calendar
#print(calendar.month(yy, mm))
# I declare ø as the symbol of measurement of time.
print((hour*60)+nowmin,"minutes out of 1400 minutes. \nWhich is", hour ,"hours and", nowmin, "minutes long.")
print("It is currently \n",day,"day of the month \n",day_of_year,"days out of 365 for this year.")
print('My age is',aged,"days old.")
print("My age is",'ø {:,.2f}'.format(aged/7),"weeks old.")
print("My age is",'ø {:,.2f}'.format(aged/365),"years old.")
print("My age is",'ø {:,.2f}'.format(aged*24*60),"minutes old.")
print("My energy is",'e {:,.2f}'.format(11))

print(datetime(now.year,now.month,now.day).date())
print(now.date())
