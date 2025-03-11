# 13. Working with Time and Dates

# A. Write a program that calculates the number of days between two dates.
from datetime import datetime

def days_between_dates(x1,x2):

    date_format = '%m-%d-%Y'

    date_1 = datetime.strptime(x1, date_format)
    date_2 = datetime.strptime(x2, date_format)

    difference = abs((date_2 - date_1).days)

    return difference

date1 = "03-01-2025"
date2 = "05-11-2025"

print("Number of days between:", days_between_dates(date1, date2))