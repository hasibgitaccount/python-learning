def return_even(x):
    new_list = []
    for i in x:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

a = [ 1,2,3,4,5,6,7,8,9]
print(return_even(a))