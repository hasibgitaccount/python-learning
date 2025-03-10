def list_to_dict(x, y):
    combined_list = x + y
    return {combined_list[i] : i for i in range(len(combined_list))}

a = ['a','b','c','d']
b = [1,2,3,4]
print(list_to_dict(a, b))