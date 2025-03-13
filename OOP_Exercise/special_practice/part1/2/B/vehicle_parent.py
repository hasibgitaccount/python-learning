class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'Brand: {self.brand} while model: {self.model}'
        