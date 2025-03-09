def return_max_min(x):
    maximum = max(x)
    minimum = min(x)
    return maximum, minimum

a = [3,4,7,9,3,6,7]
result = return_max_min(a)
print(f'the maximum value in the list is {result[0]} and minimum value is {result[1]}')