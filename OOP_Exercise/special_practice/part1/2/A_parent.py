# 2. Inheritance:

# A. Create an Employee subclass with attributes for salary and a method to calculate yearly salary.

import csv

class Person:
    def __init__(self, salary = 0):

        assert salary >= 0, f'salary cant be less than zero' 

        self.salary = salary

    @classmethod
    def attributes_from_csv(cls):
        employees = []
        with open('OOP_Exercise/special_practice/part1/2/A.csv', mode= 'r') as csv_file:
            reader = csv.reader(csv_file)

            for i in reader:
                employees.append(cls(i[0].strip(), i[1].strip(), int(i[2].strip()), int(i[3].strip())))
        return employees

    def __str__(self):
        return f'the salary of employee_1 is {self.calculate_salary()}'


        