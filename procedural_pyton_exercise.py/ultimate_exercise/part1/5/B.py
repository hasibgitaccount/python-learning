def blah(x):
    new_list = []
    a = 0
    b = 1
    for i in range(x):
        new_list.append(a)
        a, b = b, a + b

    return new_list

n_terms = 10
fib_seq = blah(n_terms)

print(f"The first {n_terms} terms of the Fibonacci sequence are:")
print(fib_seq)
        