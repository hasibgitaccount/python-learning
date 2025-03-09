# data structures
'''
1. list.
2. set.
3. tuple.
4. dictionary.
'''

# LIST
# list support both data types and data structures.

#list support duplicate value
list15 = [1,1,1,2,3]
print(list15)
#it support multiple data types
list16 = ['hasib', True,5, 6.6]
print(list16)
#list support item assingment
list16[0] = 'ava max'
print(list16)

list1 = [0]
print(type(list))
print(len(list1)) # we can know the length of a list using len.'''

list2 = ['hasib', 5, 5.5, False] # a list can hold all data types
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])

# lists are mutable(modifiable).

# 1. add a element. -> APPEND, EXTEND, INSERT.
# 2. remove a element -> POP, REMOVE, DEL, CLEAR.

list3 = [10, 20, 30, 40, 50,60]

list3[2] = 3
print(list3)

#INSERT. 
'''
#insert is used like .insert(index, value) is used to add a element in a specific position of a list.
it does not replace an element, instead it shifts them to the right.
'''

list3.insert(len(list3), 60)
print(list3)
list3.insert(2, 30)
print(list3)

# APPEND

'''
 append adds an element to the end of a list. 
it modifies a list, does'nt create a new one.
'''

list4 = [10, 20, 30, 40]
list4.append(50)
print(list4)
list4.append('melon')
print(list4)
list4.append([50,60])
print(list4)

print(list3 + list4)

# EXTEND

# extend adds multiple elements to the element at the end unlike append who treats as a single element.

list5 = [11, 22, 33, 44]
list5.extend(list4)
print(list5)
list5.extend((55,66))
print(list5)
list5.extend([77,88])
print(list5)

# REMOVE

'''
remove(value) is used to delete the first occurence of a specific value.
if there are multiple values then the first one will be deleted, if there are only one then it will be deleted.
'''
list6 = [10,10,10,20]
print(sum(list6))
print(max(list6))
print(min(list6))
list6.remove(10)
print(list6)
list7 = [10,20]
list7.remove(20)
print(list7)

# CLEAR

'''
clear is used to remove all elements from a list, laeving it empty.
it does not delete the list, only the element inside.
'''

list8 = [1,2,3]
list8.clear()
print(list8)

# DEL

# del[] is used to remove an element or delete the entire element

list12 = ['shahrukh', 'salman', 'aamir']
print(list12)
del list12[2]
print(list12)


'''if you delete the whole list then you cant print it anymore.
del list12
print(list12)'''


# POP

'''
using .pop(index) will remove an element from an list and gives it back to you in another variable
if no index is provided then its going to remove the last item
'''

list9 = ['hasib', 'neha'] 

print(list9)
removed = list9.pop()
print(list9)
print(removed)

list0 = ['i', 'my_love']

print(list0)
removed1 = list0.pop(0)
print(list0)
print(removed1)

# if you dont want to store the value then everything will be same except it wont store it.
list10 = ['chinku', 'pinku']
print(list10)
list10.pop(1)
print(list10)

list11 = ['me', 'my bros']
print(list11)
list11.pop()
print(list11)

# LIST INDEXING, SLICING (POSITIVE, NEGATIVE)

# INDEXING

# positive indexing
list13 = [10, 20, 30, 40, 50]
print(list13[1])
print(list13.index(20)) # in .index your have to pass element not its index.


# negative indexing.
print(list13[-1])
print(-len(list13) + list13.index(20)) # pretty complicated lol


# SLICING

# positive slicing [s_index : e_index + 1]
print(list13[1:4])
print(list13[1:])# to the ending
print(list13[:4])# from the beginning
print(list13[:])# from first to last.
print(list13[: len(list13)])
print(list13[: len(list13)+1])


# negative slicing [s_index : e_index + 1]

print(list13[-4 : -1])
print(list13[: -1])
print(list13[-4 :])
print(list13[:len(list13)])

# stride slicing [s_index : e_index + 1 : gap + 1](positive)

list14 = [10, 'a', 20, 'b', 30, 'c', 40, 'd', 50]
print(list14[:len(list14): 2])
print(list14[1:len(list14): 2])

#stride slicing [s_index : e_index + 1 : -(gap + 1)](negative)
print(list14[:: -2])

# REVERSE SLICING [s_index_after_reversing: end_index_after_reversing -1: -1]
print(list14[6:2:-1])