# 11. Recursion

# B. Write a recursive function to reverse a string.
def recursion_reverse(x):
    if len(x) <= 1:
        return x
    
    return recursion_reverse(x[1:]) + x[0]

print(recursion_reverse("hello"))

