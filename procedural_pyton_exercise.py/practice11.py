def counting(x):
    upper = 0
    lower = 0
    for i in x:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower

print(counting("Hello World!"))
