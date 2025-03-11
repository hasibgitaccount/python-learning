# 1. Class Basics and Initialization:

# A. Create a Person class with attributes like name, age, and gender. Include methods to check if the person is an adult.

class Person:

    def __init__(self, name, gender, age = 0):
        self.name = name
        self.gender = gender
        self.age = age

    def adult_or_no(self):
        if self.age >= 18:
            return 'adult'
        else:
            return 'not adult'
        
    def __str__(self):
        return f'{self.name} whos gender is {self.gender} is {self.adult_or_no()} because the age is {self.age}.'

person1 = Person('Alice', 'Female', 25)
person2 = Person('Bob', 'Male', 15)

print(person1)
print(person2)