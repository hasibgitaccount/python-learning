class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage


    def drive_distance(self, kilo):
        self.mileage += kilo
        return self.mileage


    def display_info(self):
        return f'the  car brand is {self.brand}, while the model is {self.model}, also the year it was released is {self.year} and finally the mileage is {self.mileage}.'



    def __str__(self):
        return f'brand:{self.brand} model:{self.model} year({self.year}) mileage - {self.mileage}'
    


car1 = Car('toyota', 'corolla', 2020, 15000)
print(car1.drive_distance(200))
print(car1.display_info())
print(car1)