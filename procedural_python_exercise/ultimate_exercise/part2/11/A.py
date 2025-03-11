# 11. Recursion

# A. Implement a recursive function to calculate the factorial of a number.
def calculate_factorial(x):

    if x == 0 or x == 1: # base case, tells when to stop
        return 1
    
    return x * calculate_factorial(x-1) # recursive case, keeps going until hits base case.

print(calculate_factorial(5))

