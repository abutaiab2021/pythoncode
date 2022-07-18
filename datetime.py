# import datetime module
import datetime
# use now method of datetime class in datetime module
datetime_obj = datetime.datetime()
print(datetime_obj)
# use today method of date class in datetime module
date_obj = datetime.date.today()
print(date_obj)
# use time class in datetime module
time_hour_obj = datetime.time(11,59, 30)
print(time_hour_obj)
# Python program to
# demonstrate date class

# import the date class
from datetime import date

# initializing constructor
# and passing arguments in the
# format year, month, date
my_date = date(1996, 12, 11)

print("Date passed as argument is", my_date)

# Uncommenting my_date = date(1996, 12, 39)
# will raise an ValueError as it is
# outside range

# uncommenting my_date = date('1996', 12, 11)
# will raise a TypeError as a string is
# passed instead of integer
