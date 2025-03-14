# 2. Abstract Classes and Interfaces:

# A. Create an abstract class Shape with an abstract method draw() and implement this method in subclasses (Circle, Rectangle).

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def draw(self):
        print(f'drawing a circle with radius {self.radius}')
    


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a Rectangle with width {self.width} and height {self.height}")
    


circle = Circle(5)
rectangle = Rectangle(10, 20)

circle.draw()       
rectangle.draw()     