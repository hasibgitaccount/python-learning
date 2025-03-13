# 2. Inheritance:

# A. Create an Employee subclass with attributes for salary and a method to calculate yearly salary.

import csv

class Person:
    def __init__(self, salary = 0): 

        self.salary = int(salary)


    def __str__(self):
        return f'the salary of employee_1 is {self.calculate_salary()}'


        