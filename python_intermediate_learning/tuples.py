# in tuple the parenthesis is optional . so i can either use it or not.
tuple1 = 'hasib', True, 15, 122.4
print(type(tuple1))
# if you want to make a tupe where it containes only one element then add a coma at the end
tuple1 = ('chinku',)
print(type(tuple1))
# i can also create a build in function called tuple to create a tuple from anything
tuple1 = tuple(['hasib', True, 12])
print(type(tuple1))
# i can also assign the values of a tuple to a variable and then later call it
item = tuple1[0]
item1 = tuple1[-1]
print(item1)
print(item)
#for loop in tuple
for i in tuple1:
    print(i)
# if in statement
if 'hasib' in tuple1:
    print(True)
else:
    print(False)
# if we want to count any element inside our tuple
print(tuple1.count('hasib'))
# convert tuple to list
list1 = list(tuple1)
print(type(list1))
