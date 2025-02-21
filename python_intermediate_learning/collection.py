# the collections module implements special container data types and provides alternatives with some additional funcionality compared to the general purpose built-in containers, like dictionaries.
# here we will talk about five different topic in collection module.those are:
'''
1. counter
2. namedtuple
3. OrderedDict
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

# OrderedDict
# OrderedDict is like a regular dictionary but they remember the order the items were inserted. they have lose importance since normal dict has also function now.
from collections import OrderedDict
order_dict = OrderedDict()
order_dict['b'] = 3
order_dict['c'] = 4
order_dict['a'] = 2
'''print(order_dict) # as you can see it can remember its order .

normal_dict = {}
normal_dict['b'] = 3
normal_dict['c'] = 4
normal_dict['a'] = 2
print(normal_dict) '''# normal dictionary can also use so thats usecase has now become obsolete.

# defaultdict
# the defaultdict is also very similar to normal dict. the only difference is that it will have a default value if the key has not been set yet.
from collections import defaultdict
d_dict = defaultdict(int) # here as a argument we will give a default type
d_dict['a'] = 1.0
d_dict['b'] = 2
'''print(d_dict)
print(d_dict['c'])''' # here since 'c' key doesnt have a int value so it took the default int value 0. if it was float then it would give 0.0, list will give a empty list

# deque

from collections import deque
