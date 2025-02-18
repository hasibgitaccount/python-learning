# strings are immutable
# for multiline string code we use triple quote
string1 = '''chinku 
pinky'''
'''print(string1)'''
# we cant use single quote if we are representing the string with single quote. then we need to use escape character or use double quote.
'''string1 = 'i\'m hasib'
print(string1)'''
# we can access character in string like lists , sets
'''access = string1[0]
print(access)
access = string1[-1]
print(access)
access = string1[1:4]
print(access)
'''
# if we want space between two strings then use two single quote between them
str1 = 'hasib'
str2 = 'sunehera'
concete = str1 + ' ' + str2
print(concete)