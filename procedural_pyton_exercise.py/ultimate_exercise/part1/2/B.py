def convert_string_to_int(x):

    new_list = x.split(',')
    main_list = []

    for i in new_list:
        i = i.strip()

        try:
            main_list.append(int(i))

        except ValueError:
            print(f' your number {i} is incorrect')
            continue
        
    return main_list
        
while True:
        user_inpit = input(f'enter comma-seperated number :')
        result = convert_string_to_int(user_inpit)
        print(f' the list of numbers is : {result}')

        recursion = input(f'do you want to another one (yes/no) :')
        if recursion != 'yes':
            print('thank you for everything')
            break

    