def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(x ** .5) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime(7))  
print(is_prime(10)) 
print(is_prime(2))