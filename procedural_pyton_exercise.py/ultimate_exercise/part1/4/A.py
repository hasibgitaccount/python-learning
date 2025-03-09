def summing(x):
    return sum(x)

while True:
    try:
        user_input = input(f'please provide the list :')
        user_list = [int(i) for i in user_input.split(',')]
    except ValueError:
        print('this is not a proper list. enter again.')
        continue

    result = summing(user_list)
    print(f'the sum of your list numbers is {result}')

    again = input(f'do you have any more list (yes/no) :').strip().lower()
    if again != 'yes':
        print('thank you! come again!')
        break