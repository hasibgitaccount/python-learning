def second_largest(x):
    x = list(set(x))
    if len(x) < 2:
        return None
    x.sort()
    return x[-2]

print(second_largest([1, 2, 3, 4, 5])) 
print(second_largest([5, 5, 5, 5]))     
print(second_largest([3]))