def is_perfect_number(x):
    add = []
    for i in range(1, x):
        if x % i == 0:
            add.append(i)
    if sum(add) == x:
        return True
    else:
        return False
    
print(is_perfect_number(6))  
print(is_perfect_number(28))  
print(is_perfect_number(12))