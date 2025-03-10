import csv

class Item:
    all = []
    pay_rate = 0.8 # pay rate after 20% discount.


    def __init__(self, name: str, price: float, quantity = 0):

        # run validations to the recieve arguments.
        assert price >= 0, f"price{price} is less than zero" # it will help us understand the issue
        assert quantity >= 0, f"quantity{quantity} is less than zero"
        
        # assign to self object.
        self.__name = name # for read only functionality
        self.__price = price
        self.quantity = quantity


        # actions to execute
        Item.all.append(self)


#                       ENCAPSULATION

# for having read only in name.
    @property # getter. used for getting a value 
    # property decorator = read only attribute
    def name(self):
        '''print('you are trying to get a value')'''
        return self.__name
    


    @name.setter # setter. to set the value.
    def name(self, value):
        if len(value) > 10:
            raise Exception ('the name is too long')
        else:
            '''print('trying to set')'''
            self.__name = value


    @property
    def price(self):
        return self.__price


    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value


    def calculate_total_price(self):  
        return self.__price * self.quantity 


    # now lets create a method to apply the discount.
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        with open('object_oriented_programming(OOP)/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)


        for item in items:
            '''print(item)'''
            Item(
                name= item.get('name'),
                price= float(item.get('price')),
                quantity= float(item.get('quantity'))
            )



    @staticmethod
    def is_int(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.price}', {self.quantity})"
    

#                        ABSTRACTION

    def __connect(self, smtp_sever):
        pass


    def __prepare_body(self):
        return f'''
        heloo, what's up!
        we have {self.name} {self.quantity} times.
        '''
    

    def __send(self):
        pass


    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()




