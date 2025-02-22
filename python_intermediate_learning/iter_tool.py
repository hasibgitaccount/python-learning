# the iter tools module is a collection of tools for handling iterator. simply puth iterators are data types that can be used in a for loop.
# the iter tools offer some advanced tools, those are:
'''
1. product
2. permutation
3. combination
4. accumulate
5. groupby
6. infinite iterators
'''
# PRODUCT

# first of all we have to import it
from itertools import product
import operator
from itertools import accumulate
from itertools import combinations, combinations_with_replacement
from itertools import combinations
from itertools import permutations
from itertools import product
a = [1, 2]
b = [3, 4]
# here the product will compute the cartesian product of the input iterables.
p = product(a, b)
print(list(p))
# we can also define a number of repition
b = [3]
p = product(a, b, repeat=2)
print(list(p))

# PERMUTATIONS

# permutations will return all possible orderings of an input
a = [1, 2, 3]
p = permutations(a)
print(list(p))
# we can also specify the length of the permutations as a second arguments. so if we want to have shorter or longer permutations then we just specify the arguments.
p = permutations(a, 2)
print(list(p))

# COMBINATIONS
# the combinations function will make all possible combinations with a specified length.
a = [1, 2, 3, 4]
c = combinations(a, 2)
print(list(c))
# NOTE: here we dont have combinations of the smae arguments meaning there is no repition. if we want that then we will use combinations_with_repititions function.
c_wr = combinations_with_replacement(a, 2)
print(list(c_wr))

# ACCUMULATE
# the accumulate function makes and iterator that returns accumulated sums or any other function that it will as input.
a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc))  # by default it will compute the sums.
# it can also multiply the elements. then we need to give an argument.
ac = accumulate(a, func=operator.mul)
print(list(ac))
# max
a = [1, 2, 5, 3, 4]
acc_max = accumulate(a, func=max)
print(list(acc_max))

# GROUPBY
# the groupby function makes an iterator that returns keys and groups from an iterable.


def smaller_than_3(x):
    return x < 3

from itertools import groupby
a = [1, 2, 3, 4]
# we also have to give a key, we can define it as a function also.
g = groupby(a, key=smaller_than_3)
for key, value in g:
    print(key, list(value))
# we can also use lambda function here.
# LAMBDA.
# lambda are small one line function that can have an input and will do some expression and then will return an output.
# we also have to give a key, we can define it as a function also.
g = groupby(a, key=lambda x: x < 4)
for key, value in g:
    print(key, list(value))

persons = [{'name': 'tom', 'age': 25}, {'name': 'chinku', 'age': 25},
           {'name': 'pinku', 'age': 27}, {'name': 'shingshing', 'age': 28}]
g = groupby(persons, key=lambda x: x['age'])
for key, value in g:
    print(key, list(value))

# INFINITE ITERATORS
# COUNT
from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break
# CYCLE
a = [1,2,3]
for i in cycle(a):
    '''print(i)''' # dont ever run it . it is infinite

# REPEAT
from itertools import repeat
for i in repeat(1):
    '''print(i)''' # dont run it
# i can also stop the repetition with a second argument
for i in repeat(1,4):
    '''print(i)'''
