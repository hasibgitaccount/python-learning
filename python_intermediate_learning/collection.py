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
print(my_counter)