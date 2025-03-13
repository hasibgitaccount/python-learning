import csv

from .vehicle_parent import Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, num_doors = 4):
        super().__init__(brand, model)
        self.num_doors = int(num_doors)

    @classmethod
    def load_from_csv(cls, file_path):
        new_list = []
        with open(file_path, mode= 'r') as csv_file:
            reader = csv.reader(csv_file)

            for i in reader:
                new_list.append(cls(*i))

        return new_list

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} and Number of doors: {self.num_doors}'
    
        

    

    