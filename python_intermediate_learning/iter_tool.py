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

# COMBINATIONS
# the combinations function will make all possible combinations with a specified length.
from itertools import combinations
a = [1,2,3,4]
c = combinations(a, 2)
'''print(list(c))'''
# NOTE: here we dont have combinations of the smae arguments meaning there is no repition. if we want that then we will use combinations_with_repititions function.
from itertools import combinations, combinations_with_replacement
c_wr = combinations_with_replacement(a, 2)
'''print(list(c_wr))'''

# ACCUMULATE
#
from itertools import accumulate

