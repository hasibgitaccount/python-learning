# B. Create a program that handles division by zero errors gracefully.
def division():
    try:
        user_input_1 = float(input(f'please give us the first number :'))
        user_input_2 = float(input(f'please give us the second number :'))
        if user_input_1 <= 0 or user_input_2 < 0:
            raise ValueError('only positive integer numbers!')
        if user_input_2 == 0:
            raise ZeroDivisionError('zero cant be divided')
        
    except ValueError as e:
        print(f'try again with positive numbers.{e}')
        raise

    except ZeroDivisionError as e:
        print(f'your input {e} is not divisible. try again')
        raise

    except Exception as e:
        print(f'An unexpected error occured,{e}')
        raise
    return user_input_1 / user_input_2

try:
    print(f'the result of your division is {division()}')

except ValueError:
    print('it is for higher ups to handle it now')

except ZeroDivisionError:
    print('no zero please. user other numbers')

except Exception as e:
    print(f'an uncexpected error occured, {e}')