from .shape_parent import Shape

class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    
    