def counting(x):
    return {i : x.count(i) for i in set(x)}

input_string = "hello"
result = counting(input_string)
print(result) 