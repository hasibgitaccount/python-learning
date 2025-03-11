# 13. Working with Time and Dates

# B. Create a function that formats a date string into YYYY-MM-DD format.

from datetime import datetime

def lets_go(x):

    date_format = '%m-%d-%Y'

    date_1 = datetime.strptime(x, date_format)

    return date_1.strftime('%Y-%m-%d')

date1 = "03-01-2025"
print(lets_go(date1))