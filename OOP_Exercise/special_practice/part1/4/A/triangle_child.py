from .shape_parent import Shape

class Triangle(Shape):
    
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height


    def area(self):
        return 0.5 * self.base * self.height
