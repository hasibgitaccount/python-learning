def greeting(x,y):
    return (f'Hello! How are you {x} and \n since your age is {y}.\n i wish you a long life!! always be happy')

while True:
    try:
        name = input(f'please enter your name :').lower().strip()
        age = int(input(f'please enter your age :'))
    except ValueError:
        print('Error: only enter integer value please')
        continue

    if age < 0:
        print('please enter a valid age')
        continue

    result = greeting(name, age)
    print(f'Greeting: {result}')

    again = input(f'do you like another greeting sir/maam (yes/no) :').strip().lower()
    if again != 'yes':
        break