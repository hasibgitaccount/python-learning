def basic_calculator(x, y, z):
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
     exit()

c = input(f'only ("+,-,*,/"):')
print(basic_calculator(a,b,c))