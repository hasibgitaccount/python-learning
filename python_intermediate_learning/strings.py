# strings are immutable
# for multiline string code we use triple quote
string1 = '''chinku 
pinky'''

print(string1)
# we cant use single quote if we are representing the string with single quote. then we need to use escape character or use double quote.
string1 = 'i\'m hasib'
print(string1)
# we can access character in string like lists , sets
access = string1[0]
print(access)
access = string1[-1]
print(access)
access = string1[1:4]
print(access)

# if we want space between two strings then use two single quote between them
str1 = 'hasib'
str2 = 'sunehera'
concete = str1 + ' ' + str2
print(concete)
# by default if you give wide space in string then it will print those wide spaces. to remove those we can use .strip(). but it wont remove the space between elements
space = '   hello world     '

print(space)
space = space.strip()
print(space)
useful = 'Hello World'
print(useful.upper())
print(useful.lower())
print(useful.startswith('Hel'))
print(useful.endswith('Hel'))

# for string anyone's index we need to use find function. if the word doesn't exist then it would return -1
print(useful.find('lo'))
print(useful.find('z'))
# i can also find how many tiems a word exsit in the string
print(useful.count('z'))
# we can also replace elements inside strings using .replace()
print(useful.replace('World', 'sunaiha')) # since i didnt assign the value to a variable so the value will be temporary.
print(useful)
# converting a string to a list, give a argument if you have any otherwise it will seperate element by space
main_string = 'how are you everyone'
main_list = main_string.split()

print(main_string)
print(main_list)
# now we have arguments
main_str1 = 'how, are , you, everyone'
print(main_str1)
main_list = main_str1.split(',')
print(main_list)
# now convert list to string using ''.join()method
new_string = ' '.join(main_list)
print(new_string)
# formatfing string using f-string

# string formatting in python allows you to insert values into string into more flexible and readable way. it enables you to construct string with dynamic content such as variable or expression.

var1 = 'hasib'
var2 = 'male'
combine = f'my name is {var1} and my gender is {var2}'
print(combine)