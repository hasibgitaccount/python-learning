def check(x):
    if x < 0 :
        return ' a negative number'
    elif x > 0 :
        return ' a positive number'
    elif x == 0 :
        return ' zero'

while True:
    try :
        user_input = int(input(f'please enter the number :'))
    
    except ValueError:
        print(f'your input value is not a number')
        continue

    result = check(user_input)
    print(f'the number that you have given is {result}')

    recommence = input(f'do you want to do another operation (yes / no) :').strip().lower()
    if recommence != 'yes':
        print('come back agian!')
        break