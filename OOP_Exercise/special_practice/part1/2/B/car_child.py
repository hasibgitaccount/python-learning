from .vehicle_parent import Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, num_doors = 4):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} and Number of doors: {self.num_doors}'
    
        

    

    