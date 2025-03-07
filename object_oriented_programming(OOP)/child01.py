import csv

from parent import Item

class phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):

        # call to super function to have access to all the attributes / methods.
        super().__init__(
            name, price, quantity
        )

        # run validations to the recieve arguments.
        assert broken_phones >= 0, f"broken_phones{quantity} is less than zero"
        
        # assign to self object.
        self.broken_phones = broken_phones


        # actions to execute
        phone.all.append(self)