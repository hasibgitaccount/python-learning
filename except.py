# a python program terminates as soon as it encounters an error and an error can be either a syntax error or an exception. now we will understand the difference between syntax error and exception error. the most common built-in exceptions errors. how to raise and handle exception errors and how to define exception errors.

# SYNTAX ERROR
# a syntax error occurs when the parser detects a syntactically incorrect statement.
# a = 5 print(a) # syntax error

# EXCEPTION
# even if a statement is syntactically correct, it may cause an error when it is executed. thats called exception error. there are several different error classes.
'''
1. trying to add a number and a string will raise an type error.
a = 5 + '10' 
print(a)

2. import error.
if i want to import some module from import that doesn't exist then it will 'module does not find' error which is a sub-class of import error.
import chinkupinku [error]

3. name error.
if i do not define a particular then it will exhibit this error.
a = b[error, b is not defined]

4. file not found error
so if i want to open a file but there is no existence of that file then it will show that error.
a = open(chinku.txt)

5. value error.
if happens if a function or an operation recieves an argument that has the right type but an inappropriate value
a = [1,2,3]
a.remove = [4] {value error. 4 is not in the a}

6. index error
if i give the index which is not inside the variable then it will give index error.
a =[1,2,3]
print(a][4]) # index error

7. key error. # very easy to understand
d = {'name':'hasib'}
print(d['age']) # key error.

8. zero division error # division by zero is not allowed
a = 5/0 # zero division error.
'''

# raising an exception
# if you want to force an exception when certain conditions are met. then we can do it with raise keyword.
x = -5
if x < 0:
    '''raise Exception('x should be positive')'''  # will give error
x = 5
if x < 0:
    raise Exception('x should be positive')

# in the second way we can use assert statement. the assert statement will throw an assertion error if your assertion is not true.
x = -5
'''assert(x >= 0), 'x is not positive'''  # will throw error.
x = 5
assert (x >= 0), 'x is not positive'

# now if we want to handle exception, then i can try exception with a try except block.
try:
    a = 10/0
except:
    print('not gonna execute')  # here if the code in try part is wrong then it will execute the except method.

# we can also catch the type of exceptions.
try:
    a = 10/0
except Exception as e:
    print(e)

# its good practice to specify the type of exception you want to catch. and therefore you have to know the possible errors.
try:
    a = 10 / 1
    b = a + 'b'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

# in the try except block we can also have else clause.
# an else is runned if no exception is occured.
try:
   a = 5
   b = 6
except TypeError as c:
    print(c)
except ZeroDivisionError as d:
    print(d)
else:
    print('everything is fine')

# finally clause 
# finally clause runs always no matter the exception or not and this is used for to make some cleanup operation
try:
   a = 5
   b = 6
except TypeError as c:
    print(c)
except ZeroDivisionError as d:
    print(d)
else:
    print('everything is fine')
finally:
    print('cleanup baby!!!!')

# how we can define our own exception.
# we can simply define our own error classes by sub classing from the base exception class.
class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
try:
    test_value(200)
except ValueTooHighError as d:
    print(d)


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(2)
except ValueTooHighError as d:
    print(d)
except ValueTooSmallError as f:
    print(f.message, f.value)
