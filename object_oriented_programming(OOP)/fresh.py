class Item:
    all = []
    pay_rate = 0.8 # pay rate after 20% discount.


    def __init__(self, name: str, price: float, quantity = 0):

        # run validations to the recieve arguments.
        assert price >= 0, f"price{price} is less than zero" # it will help us understand the issue
        assert quantity >= 0, f"quantity{quantity} is less than zero"
        
        # assign to self object.
        self.name = name
        self.price = price
        self.quantity = quantity


        # actions to execute
        Item.all.append(self)


    def calculate_total_price(self):  
        return self.price * self.quantity 


    # now lets create a method to apply the discount.
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    
    def __repr__(self):
        return f"Item('{self.name}','{self.price}', {self.quantity})"


item1 =Item('phone', 100, 5)
item1.apply_discount()
print(item1.price)

item2 = Item('laptop', 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price) 

item3 = Item('cabel', 10 , 5)
item4 = Item('mouse', 50 , 5)
item5 = Item('keyboard', 75 , 5)

print(Item.all)

for instance in Item.all:
    print(instance.name)