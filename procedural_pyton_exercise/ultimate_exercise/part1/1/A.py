'''def basic_calculator(x, y, z):
        if z == '+':
            return x + y
        elif z == '-':
            return x - y
        elif z == '*':
            return x * y
        elif z == '/':
            if y == 0:
                return 'error division by zero'
            return x / y
        else:
            return 'error message'
try:
    a = int(input(f'please give an number :'))
    b = int(input(f'please give an number :'))

except ValueError:
     print('Error: only int')
     exit() # immediately stops the code

c = input(f'only ("+,-,*,/"):')
print(basic_calculator(a,b,c))'''

def basic_calculator(x, y, z):
        if z == '+':
            return int(x + y)
        elif z == '-':
            return int(x - y)
        elif z == '*':
            return int(x * y)
        elif z == '/':
            if y == 0:
                return 'error division by zero'
            return (x / y)
        else:
            return 'error message'
while True:
    try:
        print('\n------Basic Calculator------')
        a = float(input(f'please give an number :'))
        b = float(input(f'please give an number :'))

    except ValueError:
        print(f'Error: only numbers')
        continue

    c = input(f'only ("+,-,*,/"):')
    result = basic_calculator(a,b,c)
    print(f'Result: {a} {c} {b} =  {result}')

    repeat = input(f'do you want to more calculations (yes/no) :').strip().lower()
    if repeat != 'yes':
         print('thank you for using our calculator')
         break