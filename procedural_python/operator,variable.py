
print('hello world')



# an operator in python is a symbol that performs an operation on values and variables.

#1. ARITHMETIC OPERATOR:

#a. additon.
print(2+2)  # here 2 is operand and the (+) symbol is the operator.
#b. substraction.
print(3-2) 
#c. multiply.
print(3*5)
#d. division.
print(6/3) 
#e.floor division.
print(10 / 3)  # will get the answer without any decimal.
#exponentiation
print(3**4) 
#modulus
print(15%2)  # will get only the decimal part but not in literal way but after the division, the amount that you cannot do division with as whole integer form.



# 2. COMPARISON OPERATOR.

# a. equal to.
print(2 == 3) 
# b. not equal to .
print(2 != 3)
# c. less than
print(2 < 3)
# d. greater than 
print(2 > 3)
# e. greater than or equal to
print(2 >= 3)
# f. less than or equal to
print(2 <= 3)



#variable: variable is a temporary container where we can store values.
my_first_variable = 2 # here we are storing values inside this container called variable.
print(my_first_variable) # we can check it using print function.

# how to name a variable
# 1. the first character has to be small or capital letter. - A, b
# 2. it cannot have number as the first lettr but after the first letter(small letter) - %$&*
# 3. first letter can have a underscore (_). - _my_variable
# 4. python reserved keywords, always try to use them as variable names.
# 5. case sensitive. python recognizes small and capital letter differently. try to keep that in mind. a, A
# 6. no space is allowed in the name of the variable.
# 7. alpha numeric is allowed but not special character in variable name.



# 3. ASSINGMENT OPERATOR
a = 5
print(a)

a += 2
print(a)

a -= 2
print(a)

a *= 2
print(a)

a /= 2
print(a)

a //= 2
print(a)

a %= 2
print(a)

a **= 2
print(a)


# 4. IDENTITY OPERATOR


# is -> == 
# is not -> !=

# identity operator is very similar to assingment operator . mainly (equal to) or (not equal to)

print(3 == 3) # True
#print( 3 is 3) # True

print(3 != 4) # True
#print(3 is not 4) # True

print(3 == 4) # False
#print(3 is 4) # False

print(3 != 3) # False
#print(3 is not 3) # False



# 5. LOGICAL OPERATORS


#a. OR
# at least single condition has to be valid to get output True.
print(2 > 3 or 3 > 2)  # True
print(2 < 3 or 3 < 4) # True
print(2 >3 or 3 > 4) # False

#b. AND
# both condition has to be valid to get output True.
print(2 > 3 and 3 > 2)# False 
print(2 > 3 and 3 > 4) # False
print(2 < 3 and 3 < 4) # True

#c. NOT
#not is going to make true to false and false to true
print(not(2 > 3 and 3 > 4)) # True
print(not 2 > 3 and 3 < 4 ) # first it worked on not operator, then on and operator.


# 6. MEMBERSHIP OPERATORS



print(3 in (3,4,5)) # True
print(3 in (4,5,6)) # False