# the collections module implements special container data types and provides alternatives with some additional funcionality compared to the general purpose built-in containers, like dictionaries.
# here we will talk about five different topic in collection module.those are:
'''
1. counter
2. namedtuple
3. orderedDict
4. defaultDict
5. deque.
'''
# lets start with counter. the counter is a container that stores the elements as dictionary keys and their counts as dictionary values 
# but first we need to import it.
from collections import Counter

example = 'aaaaaabbbbbbcccccc'
my_counter = Counter(example)
'''print(my_counter) '''# so it basically counted how many times a element is in a variable.
# like any other normal dictionary we can look at the items , keys, values etc.
'''print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

'''
'''print(my_counter.most_common(2)) # it will show you upto your last number of elments . if 2 then first 2 elements. btw it is wrapped by a list with a tuple inside. to reach more inside we can use indexing.
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0]) # here a is the most common element in our string.
print(my_counter.most_common(1)[0][1])'''
# we can also convert all the elelment inside to a list. using list element method.
'''print(list(my_counter.elements()))'''

# NAMEDTUPLE
# of course first of all we have to import it.
from collections import namedtuple
# the namedtuple is an easy to create and lightweight object type. similar to a struct.
point = namedtuple('point', 'x,y') # here as the first argument we will give the variable name and as the second argument we use another string and use all the different fields we want seperated by comma or space.

# so what happened there was it created a class called point with the fields x and y.
# so now i can create this point.
pt = point(1, -4)
'''print(pt)
# i can also access the fields.
print(pt.x, pt.y)'''