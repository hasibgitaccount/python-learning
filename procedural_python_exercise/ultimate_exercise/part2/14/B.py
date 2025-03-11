# 14. Lambda Functions and Map/Filter

# B. Use map() to square all numbers in a list.
def squaring(x):
    return list(map(lambda i: i**2, x))

dummy_data = [1, 4, 9, 16, 25]
print(squaring(dummy_data))