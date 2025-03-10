def multiplication_table(x):
    for i in range(1, 11):
        print(f'{x} x {i} = {x*i}')

while True:
    try:
        user_input = int(input(f'enter your multiplication number :'))

        multiplication_table(user_input)

        again = (input(f'do you want to do more (yes/no) :')).strip().lower()
        if again != 'yes':
            print('thank you! come again.')
            break
    except ValueError:
        print('please enter as per guidance')
        continue