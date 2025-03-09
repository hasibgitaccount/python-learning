def convert_float_to_int(x):
    return int(x)

while True:
    try:
        user_input = float(input(f'please only put a float number :'))
    except ValueError:
        print('only enter float number')
        continue
        
    if user_input < 0:
        print('please enter valid numbers kindly')
        continue

    conversion = convert_float_to_int(user_input)
    print(f'the integer conversion of {user_input} is {conversion}')

    recursion = input(f'do you want to do another operation (yes/no) :').strip().lower()
    if recursion != 'yes':
        print('thank you for using our functionality')
        break