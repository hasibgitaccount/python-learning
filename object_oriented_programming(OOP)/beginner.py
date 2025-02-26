# in python programming language each data types is an object. that has been instantiated earlier by some class.
# so it would have been nicer if we can call and tell python that we want to create a datatype of our own. it will allow us to write a code that we can reuse in the future easily if needed.
# now each instance could have attributes to describe related information about it. and we could think about some good candidates for attributes we could have for our item datatypes like name, price or quantity.

# CLASS

# FIRST PART: creation of the class.

# so first of all, creating an instance and creating an object is the same thing. we will use it interchangably.

# to initiate a class we need to write class and follow it by giving it a name that i want to create. and finally a colon.

class Item:

# there are some very special methods starting and ending with underscore, called magic methods.
    def __init__(self):
        print('i am created!')
# now when i go ahead and create an instance of a class(object), then python executes this __init__ function automatically, it means that since we have declared our class, python is going to run through that line. and since an instance(object) has been created and we have double underscore init method designed, then it is going to call the actions that are inside this __init__ method(function).

    def calculate_total_price(self, x, y):
         # here the parameter 'self' is auto generated. python wants us recieve it intentionally. it happens because python passes the object itself as a first argument when you go ahead and call those methods.
        # we are gonna multiply price and quantity.        
        # now if i call this method: at line 25
        return x * y    

# now that we have created our class, we are allowed to create soem instances(objects) for the class.
item1 =Item() # this action is equivalent to creating an instance of a class.

# now we are going to assign some attributes to instances of a class(object). to create attributes we need to use dot sign right after the instances of a class(object)
item1.name = 'phone'
item1.price = 100
item1.quantity = 5
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
item2 = Item()
item2.name = 'laptop'
item2.price = 1000
item2.quantity = 3
'''print(item2.calculate_total_price(item2.price, item2.quantity))'''
# that is how i can create a method.

# now the problem here is that we dont have a set of rules for the attributes that you would like to pass in order to instantiate an instance(object) successfully. it means that each item i want to go ahead and create , i need to hard code everything. it would be nicer if we could somehow declare in the class that in order to instantiate an instance(object) successfully, the name, price and quantity must be passed, otherwise the instance could not have been created successfully. it means that it could have been a great option if could somehow execute something in the background, the second we instantiate an instance(object). 

# the good news is we can do that by creating a special method, with a very unique name called '__init__', also called as constructor. basically that is a method with a unique name that you need to call it the way it is intentionally, in order to use its special features.

# now the next issue is we still hard code the attribute like .name, .price. to avoid hard coding those attributes in each of the instances 
# for each of the instances we create, it will go ahead and call the __init__ method or other method automatically. it means we can not only allow ourselves to recieve the self parameter, because this is a mandatory thing we should do, because python in the background passes the instance itself as the first argument. in addition, we could also take some more parameters and then do something with them. 





# SECOND PART: instantiate some objects of the class.