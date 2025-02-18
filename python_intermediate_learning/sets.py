# an easy way to create set from any data type or data structures.
set1 = set ([1,2,3])

print(type(set1))
set1 = set('hello')
print(set1) # if you look closely then you'll see that it didint print the 'l' word two but instead one time.
# how to create a emply set
empty_dict = {} # by default it will classify its class as dict 
# to classify it as set we need set functioin
empty_set = set()
print(type(empty_set))
# for loops
for i in set1:
    print(i)
# if in statement
if 4 in set1:
    print('exist')
else:
    print('cease to exist')
# to get the elements of a set that doesn't match with the other set we will use difference function
set2 = {3,4,5}

print(set1.difference(set2))
# the other one is called symetric_difference but it will give both sets unique element instead of one.
print(set1.symmetric_difference(set2))
'''
disjoint means  two sets all elements are indifferent to each other 
subset means one sets all the values is in another set.
superset means both sets have same values
'''
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))
# copying a set
set3 = {9,8,7}
set4 = set(set3)
set4.add(6)
print(set3)
print(set4)
set4 = set3.copy()
set4.add(5)
print(set3)
print(set4)
# unlike set who is mutable, a frozenset is immutable.but i can intersec, union, differe, symetric_diff
frozen = frozenset([1,2,3])
print(frozen)
frozen1 = frozenset([3,4,5])
print(frozen1)
print(frozen.union(frozen1))
