def fibonacci(x):
    new = [0,1]
    for i in range(2,x):
        new.append(new[-1] + new[-2])
    return new[:x]

print(fibonacci(5))
print(fibonacci(8))
    
    
