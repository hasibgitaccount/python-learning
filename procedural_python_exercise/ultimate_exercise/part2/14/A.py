# 14. Lambda Functions and Map/Filter

# A. Write a lambda function that filters out all numbers less than 10 from a list of integers.
def filtering(x):
    return list(filter(lambda i: i>10, x))

numbers = [3, 7, 1, 15, 9, 22, 5, 11, 30, 2, 8]
print(filtering(numbers))