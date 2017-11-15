#Erik Hansen
#11/15/2017
#displayDate.py - displays todays date

from calendar import weekday
from datetime import *

today = date.today()
day = date.today().day
month = date.today().month
year = date.today().year
weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdaynum = today.weekday()
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
print('Today is', weekday[weekdaynum], ',', months[month-1], day, year)


