import csv

from .person_parent import Person

class Employee_1(Person):

    def __init__(self, name, gender, age, salary=0):
        super().__init__(salary)
        self.name = name
        self.gender = gender
        self.age = int(age)

    def calculate_salary(self):
        return self.salary * 12
    
    @classmethod
    def attributes_from_csv(cls, file_name):
        employees = []
        with open(file_name, mode= 'r') as csv_file:
            reader = csv.reader(csv_file)

            for i in reader:
                employees.append(cls(*i))
        return employees
    
    def __str__(self):
        return f'{self.name} ({self.gender}, {self.age} years old) earns {self.salary} per month. Yearly salary: {self.calculate_salary()}'
    