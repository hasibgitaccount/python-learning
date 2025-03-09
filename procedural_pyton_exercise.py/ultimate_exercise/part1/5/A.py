import math
def factorial(x):
    return math.factorial(x)

while True:
    try:
        user_input = int(input(f'please provide us the number: '))
    
    except ValueError:
        print('only enter integer.')
        continue

    result = factorial(user_input)
    print(f' the factorial result of your number {user_input} is {result}')

    again = input(f'do you want to perform another one (yes/no) :').strip().lower()
    if again != 'yes':
        print('thank you!')
        break