def how_often(x):
    new = {}
    for i in x:
        if i in new:
            new[i] += 1
        else:
            new[i] = 1
    return new

sample_list = [1, 2, 2, 3, 3, 3, 4]
print(how_often(sample_list))