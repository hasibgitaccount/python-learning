# 14. Lambda Functions and Map/Filter

# C. Write a program that applies a lambda function to calculate the cube of each number in a list.

def cubing_motherfucker(x):
    return list(map(lambda i : i**3, x))
    # return [i**3 for i in x]

numbers = [2, 5, 7, 10, 12]
print(cubing_motherfucker(numbers))