def list_to_dict(x1, x2):
    new_list = x1 + x2

    return {value:index for index, value in enumerate(new_list)}

a = ['a', 'b', 'c', 'd']
b = [1,2,3,4]
result = list_to_dict(a, b)
print(result)