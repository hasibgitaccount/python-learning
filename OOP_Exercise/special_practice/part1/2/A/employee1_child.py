import csv

from A_parent import Person

class Employee_1(Person):

    def __init__(self, name, gender, age, salary=0):
        super().__init__(salary)
        self.name = name
        self.gender = gender
        self.age = age

    def calculate_salary(self):
        return self.salary * 12
    
    def __str__(self):
        return f'{self.name} ({self.gender}, {self.age} years old) earns {self.salary} per month. Yearly salary: {self.calculate_salary()}'
    