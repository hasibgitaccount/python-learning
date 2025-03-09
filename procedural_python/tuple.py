# TUPLE
# tuple support both data structure and data types inside it.

# tuple support duplicate value

tuple1 = (1,1,1,1,2,6,45,6,7)
print(tuple1) # tuple is ordered like list. no changed have been made inside the tuple
print(type(tuple1))
print(len(tuple1))


'''
# tuple doesn't support item assingment

tuple2 = (19,29)
tuple2[1] = 22
print(tuple2) # it will give error'''

# tuple does not support any modification. the only way around is using nested list or set for modification.

tuple3 = (1,[2,3], {4,5}, 'hasib', 6.6, True)
print(type(tuple3[1]))
print(type(tuple3[2]))
tuple3[1][0] = 200 # this is the only way to do some modification
print(tuple3)
tuple3[1].append(400) # you can modify like this
print(tuple3)
