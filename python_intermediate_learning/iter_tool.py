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
a = [1,2]
b = [3,4]
p = product(a,b) # here the product will compute the cartesian product of the input iterables.
'''print(list(p))'''
# we can also define a number of repition
b = [3]
p = product(a,b, repeat = 2)
'''print(list(p))'''

# PERMUTATIONS

# permutations will return all possible orderings of an input
from itertools import permutations
a = [1,2,3]
p = permutations(a)
'''print(list(p))'''
# we can also specify the length of the permutations as a second arguments. so if we want to have shorter or longer permutations then we just specify the arguments.
p = permutations(a, 2)
'''print(list(p))'''
