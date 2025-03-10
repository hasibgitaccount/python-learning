# 8. File I/O

# A. Write a program that reads data from a CSV file and prints the contents.

import csv

file_name = 'your_file.csv'

try:
    with open(file_name, mode= 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        header = next(csv_reader)
        print(f'Header: {header}')

        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print(f'the file "{file_name}" was not found.')
except Exception as e:
    print(f'An error occured: {e}')