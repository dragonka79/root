#A version

Months = ["január", "február", "március", "április", "május", "június", 
"július", "augusztus", "szeptember", "október", "november", "december"]

for month in Months:
    print(month)

# B version

import calendar

for month in calendar.month_name:
    print(month)