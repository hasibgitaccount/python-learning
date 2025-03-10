def leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return 'a leap year'
            else:
                return 'not a leap year'
        else:
            return 'a leap year'
    else:
        return 'not a leap year'

while True:
    try:
        user_input = int(input(f'please pass the year :'))
    
    except ValueError:
        print('please give a proper year')
        continue

    result = leap_year(user_input)
    print(f'the year you have given is {result}')

    again = input(f'do you have another in mind that you want to check (yes / no) :').strip().lower()
    if again != 'yes':
        print('thank you! come again!')
        break
