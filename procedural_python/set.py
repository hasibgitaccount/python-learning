# SET 
# set does not support data structure inside it 
set1 = {1,2,3}
print(set1)
print(type(set1))
print(len(set1))

#in terms of set duplicate value is not allowed. only the unique value is allowed.


set2 = {1,1,1,2,2,4,4,10,12}
print(set2)# the answer will be {1,2,4,10,12}. so only unique value.
#whereas, we could've able to print all those integers using list. lets give an example :
list1 = {1,1,1,2,2,4,4,10,12}
print(list1)


#multiple data type is supported in set. lets give a example:

set3 = {'hasib', 5, 7.12, True}
print(set3) # it will print all of those.
# the same goes for list as well. list also supports multiple data types. lets give some example :
list3 = ['chinku', True, 3, 4.23]
print(list3)



#indexing or slicing is not allowed in set. lets give an example :
set4 = {10,20}
#print(set1[1])  its going to give us a error
#so the only viable solution is to convert the set into a list. lets give an example :
list2 = list(set1)
print(list2)
print(list2[1])
# by that example we can easily get to the conclusion that list supports indexing and slicing

#you can also do this in list 
list4 = [10,30,20,40,50,60,70,80,90]
print(list4.index(30)) # this is index lookup. with it you can know the index of any element inside the list.
print(list4[1])# this is classic indexing.

#set is unordered. list is ordered. (user perspective). set has its own personal order.

list5 = [1,2,5,4,7,6,9,8]
print(list5)
set5 = {1,5,3,9,7,2,'a'}
print(set5)

# set does'nt support item assingment. list does.
'''set1 = {10.20,30}
set1[1] = 40
print(set1) # its going to give a error. 
'''

# both set and list support modification.

# ADD (it will add according to the sets own order system)

set6 = {10, 20, 30}
set6.add(40)
print(set6)

# ROMOVE (you just have to write the value and not the index)

set6.remove(20)
print(set6)

# UPDATE (to add multiple elements at a single time in a set.)

set6.update([50, 60, 70])
print(set6)

# POP (pop in set removes and returns(stores) a random element in a variable.)

set8 = {10,90,80,55}
removed = set8.pop()
print(set8)
print(removed)

# if you are not assinging new variable then it will just remove them randomly.

set6.pop()
print(set6)
set6.pop()
print(set6)

# CLEAR (clear everything like list and keeps the set itself.)

set7 = {10,2, 30}
set7.clear()
print(set7)

# DISCARD (discard removes an element from the set. but it wont raise the error if not found.)

set9 = {11,22,33,44,55}
set9.discard(55)
print(set9)
set9.discard(77)
print(set9)

# intersection and union

set10 = {12,23,34,45}
set11 = {13,24,35,45}
set12 = set10.intersection(set11)
print(set12)
set13 = set10.union(set11)
print(set13)
print(set10 - set11)
set14 = set10.difference(set11) # alternative of minus symbol(-)
print(set14)

# convert list to set.

list1 = [1,1,1,1,2,3,4,5,6,4]
print(list1)
set15 = set(list1)
print(set15)