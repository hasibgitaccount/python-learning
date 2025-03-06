# in python programming language each data types is an object. that has been instantiated earlier by some class.
# so it would have been nicer if we can call and tell python that we want to create a datatype of our own. it will allow us to write a code that we can reuse in the future easily if needed.
# now each instance could have attributes to describe related information about it. and we could think about some good candidates for attributes we could have for our item datatypes like name, price or quantity.

# CLASS

# FIRST PART: creation of the class.

# so first of all, creating an instance and creating an object is the same thing. we will use it interchangably.

# to initiate a class we need to write class and follow it by giving it a name that i want to create. and finally a colon.

class Item:
    all = []
    pay_rate = 0.8 # pay rate after 20% discount.

# there are some very special methods starting and ending with underscore, called magic methods.
    def __init__(self, name: str, price: float, quantity = 0): # here the object is going to complain why name is not filled in item1 and etc.
        '''print(' i am created')''' # here it will print how many objects is in there.
        '''print(f"an instance created: {name}")'''

        # run validations to the recieve arguments.

        # assert statement. assert is a statement keyword that is used to check if there is a match between what is happening and my expectations. if we dont want the price and the quantity to be zero then, it is a great idea to validate that the price and quantity are both greater than or equal to zero.
        assert price >= 0, f"price{price} is less than zero" # it will help us understand the issue
        assert quantity >= 0, f"quantity{quantity} is less than zero"
        # using the assert statement could allow us to validate the arguments we recieve. also catch the bugs quickly.
        

        # assign to self object.
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)
        # now we know that self is actually the instance itself every time that it is being created.

# thats how to work with __init__ method. always take care of the attributes that i want to assign to an object inside the __init__ method. inside the constructor like self.name etc. constructor here is the __init__ method.

    """
notes when working with classes.
1. when we use __init__ method, this doesn't mean that we can't differentiate mandatory parameters and non mandatory parameters. so if you dont have the value of a parameter in the __init__ then give a default valie like price = 0 and ignore passing the value to the objets.
2. i can assign attributes to specific instances(object) individually.
3. in the method calculate_total_price() , it still recieves x and y as parameters. now why it still recieves those parameters. well, we could for sure not recieve those parameters. because as we know, for each method we design in classes, then the object itself is passed as an argements and that's why we recieve self. this means that, we could just return self.price muliply(*) self.quantify. it means we dont really have to recieve those parameters. because we assign those attributes, once the instance has been graded(created). it means we have access to those attributes through how the methods that we are going to add here in this class in the future.
"""

# here im assigning the attributes of 'name' to each instances(object) that is going to be created. and im making that to be equal to the name that is passed in to the instances(object). now i have a dynamic attribute assignment thanks to self.name = name

# the fact that we have self as a parameter here actually allow us assign the attributes from the init method. so that we will not have to assign the attributes for each of the instances we create. it means i can dynamically assign an attribute to an instance(object) to this magic method called __init__.

# now we can avoid coding the attributes individually, just give the arguments in the object.

# now when i go ahead and create an instance of a class(object), then python executes this __init__ function automatically, it means that since we have declared our class, python is going to run through that line. and since an instance(object) has been created and we have double underscore init method designed, then it is going to call the actions that are inside this __init__ method(function).


    def calculate_total_price(self):
        # calculate_total_price(self, x, y):
         # here the parameter 'self' is auto generated. python wants us recieve it intentionally. it happens because python passes the object itself as a first argument when you go ahead and call those methods.
        # we are gonna multiply price and quantity.        
        # now if i call this method: at line 25
        # return x * y  
        return self.price * self.quantity  

# now lets create a method to apply the discount.
    def apply_discount(self):
        self.price = self.price * self.pay_rate

# now if we need to specify a specific discount rate for a specific item then we need to assign the attributes directly to the instances that i would like to have a different discount amount.

# now what we can do now is returning a string that will be responsible to represent this object. now, obviously, we dont want to use something that is not unique for each of the instances. so we will return a string that will be unique for each instances.
    def __repr__(self):
        return f"Item('{self.name}','{self.price}', {self.quantity})"

# now that we have created our class, we are allowed to create soem instances(objects) for the class.
item1 =Item('phone', 100, 5) # this action is equivalent to creating an instance of a class.

item1.apply_discount()
'''print(item1.price)'''

# now we are going to assign some attributes to instances of a class(object). to create attributes we need to use dot sign right after the instances of a class(object)
# item1.name = 'phone'
# item1.price = 100
# item1.quantity = 5
'''print(item1.calculate_total_price(item1.price, item1.quantity))''' # but when you go ahead and call a method from an instance, then python passes the object itself as the first argument. that's why we are not allowed to create methods that will never recieve parameters.
# now when we gave two arguments and calls the method then in the background python passes 'item1' as the first argument 'self' and the other two as x and y.

# now here's the big difference, whats's the difference between the random variables we used to create and these 4 lines up there ? well, here we actually have a relationship between those 4 lines because each one of the attributes are assigned to one instance of the class(object).

# we can also check the type
'''print(type(item1.name)) # str
print(type(item1.price)) # int
print(type(item1.quantity)) # int
print(type(item1))''' # data type is, item

# how to create methods and execute them on our instances(objects).

random_str = 'aaa'
'''print(random_str.upper())'''
# here we grabbed the instance(object) of a string named random_str and then i print them in the upper case using upper method.

# now the qustion is how we can design some methods that are going to be allowed to execute on our instances(objects). the answer is inside our class, so we will go inside our class which we are right now and write some methods that will be accessible from our instances(objects). we are going to create a method(function) in line 14. now we are going to create just one more instance(object) of this item.
item2 = Item('laptop', 1000, 3)
item2.pay_rate = 0.7
# here, for item2 it will find the attribute of pay_rate in the instance level. so item2 does not have to go to the class level and bring back the value of pay_rate.
item2.apply_discount()
'''print(item2.price)''' 

# item2.name = 'laptop'
#item2.price = 1000
# item2.quantity = 3
item2.has_numpad = False
'''print(item2.calculate_total_price(item2.price, item2.quantity))'''
# that is how i can create a method.

# now the problem here is that we dont have a set of rules for the attributes that you would like to pass in order to instantiate an instance(object) successfully. it means that each item i want to go ahead and create , i need to hard code everything. it would be nicer if we could somehow declare in the class that in order to instantiate an instance(object) successfully, the name, price and quantity must be passed, otherwise the instance could not have been created successfully. it means that it could have been a great option if could somehow execute something in the background, the second we instantiate an instance(object). 

# the good news is we can do that by creating a special method, with a very unique name called '__init__', also called as constructor. basically that is a method with a unique name that you need to call it the way it is intentionally, in order to use its special features.

# now the next issue is we still hard code the attribute like .name, .price. to avoid hard coding those attributes in each of the instances 
# for each of the instances we create, it will go ahead and call the __init__ method or other method automatically. it means not only we can allow ourselves to recieve the self parameter, because this is a mandatory thing we should do, because python in the background passes the instance itself as the first argument. in addition, we could also take some more parameters and then do something with them. 

'''print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)'''

'''print(item1.calculate_total_price())
print(item2.calculate_total_price())'''


# consdier a situation where i will want to make use of an attribute that is going to be global or  across all the instances. called a class attribute. not the instance attribute.  
# a class attribute is an attribute that is going to be belong to the class itself. however, i can also access this attribute from the instance level as well.

# i will try to access to the reference of the class itself. so im not going to create an instance. besides im just going to bring in the reference to the class level itself. then im going to access this class attribute.
'''print(Item.pay_rate)'''

# we can also access those class attributes from the instance level.
'''print(item1.pay_rate)
print(item2.pay_rate)'''

# there is something we need to understand when we work with instances(object) in python. so when we have an instance on our hand then at first the instance tries to bring the attribute from the instance level at the first stage, but if it doesn't find it there, then it is going to try to bring that attribute from the class level.

# there is a build in magic attribute called __dict__, that you can go ahead and see all the attributes that are belonging to that specific object. this will go ahead and bring you all the attributes that are belonging to the object that you apply this attribute and want to see its content.
'''print(Item.__dict__) # all the attributes for class level
print(item1.__dict__)''' # all the attributes for instance level.

item3 = Item('cabel', 10 , 5)
item4 = Item('mouse', 50 , 5)
item5 = Item('keyboard', 75 , 5)

# now what is problematic with our class right now is that we don't have any resource where we can just access all the items that we have in our shop right now. now it could have been nicer if we could somehow have a list with all the item instances(object) that have been created up until now and in near future. but currently there is not an approach that will give us a list with elements where each element will represent an instance of a class. and there is a wonderful candidate for creating a class attribute that we can name 'all'. now we need to figure out how we are going to add our instances(object) for each time that we are going to create an instance. now if we remember, the __init__ method is being called immediately once the instance has been graded(created). so we need to go inside the __init__ method and use a code that will be responsible for appending to that list every time we create an instance(object)
    

'''print(Item.all)''' # here the way the object is being represented is not too friendly. it could have been nicer if could change the way that the object is being represented in this list here. to achive that, we will use a magic method inside our class called __repr__. this stands for representing my object. by using this i will have the control to display my objects when im printing them in my console. 

# its going to be very useful if i want to do something with only one of the attributes of my instacnes(objects). so if i want to print only the name of all of my instances then i can use forloop to achieve such tasks.
for instance in Item.all:
    '''print(instance.name)''' 

# SECOND PART: instantiate some objects of the class.