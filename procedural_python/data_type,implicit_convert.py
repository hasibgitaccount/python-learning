# DATA TYPES
 
'''
1.string. string data type is any data wrapped around with quotation marks. whether it is (' or ")
2.integer. integer data type is any numeric data without decimal numbers
3. float. float data type is any numeric data with decimal numbers.
4. boolean. it only has two type. 1. True, 2. False
''' 


data_type = (10, 5.7, 'pretty_girl', True)
print(type(data_type[0]))# integer
print(type(data_type[1]))# float
print(type(data_type[2]))# string
print(type(data_type[3]))# boolean


# INT TO FLOAT IMPLICIT CONVERSION
print('BEFORE')
var = 5
print(type(var))
float_var = float(var) # stored the converted float in a new variable
print('AFTER')
print(float_var, type(float_var)) # called the variable and checked the type

# FLOAT TO INTEGER IMPLICIT CONVERSION
print('BEFORE')
var1 = 5.5
print(type(var1))
int_var = int(var1)
print('AFTER')
print(int_var, type(int_var))

# STRING TO INTEGER IMPLICIT CONVERSION
print('BEFORE')
var2 = "5"
print(type(var2))
int_var1 = int(var2)
print('AFTER')
print(int_var1, type(int_var1))

# INTEGER TO STRING IMPLICIT CONVERSION
print('BEFORE')
var3 = 5
print(type(var3))
int_var2 = str(var3)
print('AFTER')
print(int_var2, type(int_var2))


# STRING TO INTEGER IMPLICIT CONVERSION (inside the string is float)
print('BEFORE')
var4 = "5.5"
print(type(var4))
int_var3 = float(var4)
int_var3 = int(int_var3)
print('AFTER')
print(int_var3, type(int_var3))