
list1 = [3,4,5,6,7,8]

for i in list1:
    index = list1.index(i)
    list1[index] = list1[index]**2

print(list1)


for i in list1:
    'list1.index[i] = list1.index[i]**2'


'''list1[list1.index(i)] = list1[list1.index(i)]**2'''