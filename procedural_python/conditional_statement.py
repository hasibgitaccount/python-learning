# CONDITIONAL STATEMENT
# if else statement is very similar to comparative operator.
# it has mainly three statements.
'''
1. if - to check a condition
2. elif - next option with a condition
3. else - last option, when all failed
'''
a = 5
if a > 10:
    print('A is greater')
else:
    print('A is smaller')

# we can also do nested if else statement inside else statement
if a > 10:
    print('A is humongous')
else:
    if a == 5:
        print('A is mid-range')
    else:
        if a > 12:
            print('shut up')
        else:
            print('bad boy')        
# so every if statement is a seperate block . 
if a > 3:
    print('A is strong')
if a > 5:
    print('A is very strong') # two statements will print
else:
    print('meh')
# we should use elif statement instead of just nesting the extra condition
if a > 5:
    print('chinku')
elif a == 5:
    print('pinku')
else:
    print('sungsung')