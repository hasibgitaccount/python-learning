# 5. Dunder Methods (Magic Methods):

# A. Implement __repr__() and __eq__() methods for string representation and comparison between Person objects.

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def __repr__(self):
        return f"Person(name='{self.name}' and age='{self.age}')"


    def __eq__(self, value):
        if not isinstance(value, Person):
            return False
        return self.name == value.name and self.age == value.age
    

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

# Check string representation
print(p1) 

# Check equality
print(p1 == p2)  
print(p1 == p3)