from .shape_parent import Shape

class Square(Shape):

    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    
    def area(self):
        return self.side_length * self.side_length