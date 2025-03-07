from parent import Item

item1 = Item('myitem', 750)
item1.name = 'otheritem'
'''print(item1.name)'''
# here the name attibute is being overwritten. but what if we want to restrict our users to change the attribute of name, meaning once the name has been set up in the initialization it won't change. that is something we want to achieve for critical attributes like for the name of your instance. for that we could create a 'read only' so called attribute. means, we only have one opportunity to set up the name of our item and then we can't touch the value of that anymore. it's known as 'encapsulation'. now after creating the read only file if we try to access the property and not the attribute
'''print(item1.read_only_name)'''

# but now if i try to assign a new value to the read_only_name then it will give error.
# read_ony_name = 'bbb'