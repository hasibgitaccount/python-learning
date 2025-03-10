# A. Write a function that reads an integer from the user and raises an exception if the input is not a valid integer.
def error():
    try:
        user_input = int(input(f'only enter integer value please :'))
        if user_input <= 0:
            raise ValueError('we only deal with positive numbers')

    except ValueError as e:
        print(f'your input {e} is wrong!')
        raise
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        raise
    return user_input

try:
    print(f'the value you have printed is {error()}')

except ValueError:
    print('waiting for the higher ups to check')