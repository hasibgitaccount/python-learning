def convert_float_to_int(x):
    return int(x)

try:
    user_input = float(input(f'please only put a float number :'))
except ValueError:
    print('only enter float number')
    exit()
conversion = convert_float_to_int(user_input)
print(f'the intrger conversion of {user_input} is {conversion}')