# a lambda function is a small line anonymous function that is defined without a name. first the lambda keyword, then some arguments then a colon and then an expression.
# example; lamba arguments: expression
# it will create a function with some arguments and it will evaluate the expression and return the result.
add10 = lambda x: x + 10 # lambda funtion
print(add10(5))
'''
argument: a value passed to a function or method. provides input to a function.print(10)-> 10 is a argument
expression: a combination of values, variables and operators that evaluates to a single value. produces a value when evaluated. print(2+3) -> 5 is an expression.
'''
def add10_func(x): # normal function
    return x + 10
print(add10_func(5))
# lambda funtions can also have multiple arguments.
mult = lambda x,y: x*y
print(mult(2,14))
# lambda functions are typically used when you nedd a simple function that is used only once in your code. or it is used as an argument to functions that take in other functions as arguments. for example they are used along with the functions like sorte, map , filters and reduce etx.
points2d = [(1,2),(15,1),(5,-1),(10,4)]
points_sorted = sorted(points2d)
print(points2d)
print(points_sorted) # by default this will sort out list by the first argument. 
# but if we want to sort it the seecond argument then we can give it a key argument and that should be a function. that function will be lambda.
points_sorted = sorted(points2d, key= lambda x: x[1])
print(points_sorted)
# we can also do it with a normal function,
def sort_by_y(x):
    return x[1] 
points_sorted = sorted(points2d, key= sort_by_y)
print(points_sorted)
# map funtion
# map funtion transforms each elements with a function. it has a function as a argument and then a sequence.
a = [1,2,3,4,5,6]
b = map(lambda x: x*2, a)
print(list(b)) # but you should use list comprehension.
# filter function also has a function and a sequence and it will return true or false. filter function will return all the elements for which the function evaluates to true.
b = filter(lambda x: x%2 == 0,a)
print(list(b)) # also dont use this, use list comprehension
# reduce function
# reduce funtion also takes function and sequence. and it repeatedly applies the function to the elements and returns a single value.
from functools import reduce
a=[1,2,3,4]
b = reduce(lambda x,y:x*y,a)
print(b)
