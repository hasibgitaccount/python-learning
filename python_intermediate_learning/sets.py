# we can create an empty list by just giving an blank list
'''my_list = []
print(my_list)'''

# we can also put lists value in another variable.
'''list1 = [10,20,30]
item = list1[1]
print(item)
# we can also use negative indexing.
item = list1[-1]
print(item)'''

'''
for loops, using for loops we can tell python to execute a block for a predetermined amount of time up front without the need of a separate variable and conditional to check its value. its commonly used to iterate the items in a list.
'''

list2 = [1,2,3,4,5]
'''
for x in list2:
    print (x)'''

# or you can iterate a specific amount of time using the range function

'''for x in range(7):
    print(x)'''

# but what if we want the index function of a list

'''list1 = [1, 2, 3, 4, 5]
for x in enumerate(list1): # enumerate is a build in funcion that adds index with the elements.
    print(x)'''

# the other way to do it.

'''
for index, x in enumerate(list2):
    print(index, x)'''

# now we will check if an item is inside list2

'''if 10 in list2:
    print('yes')
else:
    print('no')'''

# if you want to order your list ascendingly then use sort()

list3 = [15,32,12,23]
'''list3.sort()
print(list3)'''

# by default if you use sort then its going to change your list order to ascention. so to not do that we need to use sorted funtion in a new variable to retain the unascending order in the main list.

'''new_list = sorted(list3)
print(new_list)
print(list3)'''

'''list3.reverse() # alternative of reverse slicing.
print(list3)'''

# so we can copy the content of a list and assign it to another list. but then if we modify the copy list then the real list will also modify. so we will use copy function.

'''list3_copy = list3.copy() 
list3_copy.append('hasib')
print(list3_copy)
print(list3)'''

#you can also do it using list method

'''list3_copy2 = list(list3)
list3_copy2.append('apple')
print(list3_copy2)
print(list3)'''

# you can also do it usng slicing methhod.

'''list3_copy3 = list3[:]
list3_copy3.append('banana')
print(list3_copy3)
print(list3)'''

# LIST COMPREHENSION
# its an elegant and fast way to create a new list from an existing list with one line.

'''normarl_list = [10,22,33]
list_comprehension = [i*i for i in normarl_list]
print(normarl_list)
print(list_comprehension)'''