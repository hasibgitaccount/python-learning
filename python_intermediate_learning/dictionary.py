# dictionary is unordered 
# as you have guessed we can create dict with dict function
dict1 = dict(name='chinku', age=21, city= 'dhaka') # creating a dict from a tuple dont need quote in keys
dict1 = {'name': 'chinku', 'age': 21, 'city': 'dhaka'}
'''print(type(dict1))'''
# we can create new key value pair in dict
dict1['email'] = 'chinkupinku@gmail.com'
print(dict1)
# if in statement
'''if 'name' in dict1:
    print(dict1['name'])'''
# if i want to rmeove an item , we can use del or pop
'''del dict1['age']
print(dict1)'''
# try except method
'''try:
    print(dict1['email'])
except:
    print('error')'''
# if its not availabe
'''try:
    print(dict1['last_name'])
except:
    print('error')
'''
# for loop in dictionary
for i in dict1.keys():
    print(i)
for i in dict1.values():
    print(i)