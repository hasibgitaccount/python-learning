# Implement a function that writes a list of dictionaries to a CSV file, each representing a row.

import csv

file_name = 'procedural_python_exercise/ultimate_exercise/part2/8/B.csv'
data = [
    {'Name': 'Alice', 'Age': 25, 'Occupation': 'Engineer'},
    {'Name': 'Bob', 'Age': 30, 'Occupation': 'Data Scientist'},
    {'Name': 'Charlie', 'Age': 28, 'Occupation': 'Teacher'},
    {'Name': 'David', 'Age': 35, 'Occupation': 'Doctor'},
    {'Name': 'Eva', 'Age': 22, 'Occupation': 'Student'},
    {'Name': 'Frank', 'Age': 40, 'Occupation': 'Artist'},
    {'Name': 'Grace', 'Age': 26, 'Occupation': 'Nurse'},
    {'Name': 'Hannah', 'Age': 32, 'Occupation': 'Marketing Specialist'},
    {'Name': 'Ian', 'Age': 29, 'Occupation': 'Photographer'},
    {'Name': 'John', 'Age': 38, 'Occupation': 'Chef'}
]

try:
    with open(file_name, mode= 'w', newline='') as csv_file:
        fieldnames = data[0].keys()

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(data)

    print(f'data successfully written to {file_name}')

except FileNotFoundError:
    print(f'the file {file_name} is not found.')
except Exception as e:
    print(f'An error occurred {e}')
