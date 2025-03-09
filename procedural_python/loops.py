# LOOPS
# to reduce the repetition. 
# instead of modifying every element in a data structure manually, loops can do that in one line.
loop1 = [3,4,5,6,7,8]

for i in loop1:
    print(i, i**2)

# another way of dong it 

loop2 = [3,4,5,6,7,8]
for i in loop2:
    loop2[loop2.index(i)] = loop2[loop2.index(i)] **2
print(loop2)

# another way

loop3 = [3,4,5,6,7,8]
for i in loop3:
    index = loop3.index(i)
    loop3[index] = loop3[index]**2
print(loop3)

loop4 = [3,4,5,6,7,8]
list1 = []
for i in loop4:
    list1.append(i)
print(list1)

# to iterate through all the element without giving everyoens index we use this
# for i in loop1:
#   loop1[loop1.index(i)]

# with .index you can you get the index and using it in list you can get the value
# loop1.index(6) = 3
# loop1[loop1.index(6)] = 6 # might seem confusing but understanding it is important

# then if you want to squear something then do it like this
loop5 = [3,4,5,6,7,8]
loop5[0] = loop5[0]**2
print(loop1)

# now we will learn the most optimal way of doing it is using range function.
# what is range function . it is simply a counting machine of index. if no input is given then it will count from 0 and if input is provided then it will count from there. if input is 2 then count will start from 2.
# its mainly to keep track of the element order.

list2 = [1,2,3,4,5]
print(list(range(2, len(list2))))

loop6 = [3,4,5,6,7,8]
for i in range(len(loop6)):
    loop6[i] = loop6[i]**2
print(loop6)

# now if you use the first way to do for loop and not use the range then sometimes you will face problems.
# since list supports duplicate value theats why it will give the first index of the same value.
a = [1,2,3,1]
print(a.index(1)) # there was another 1 in the 3rd index but it will only show the first one.

# you can solve it using range function

print(list(range(len(a)))) # it will give you all the index . so you modify any 1 later.

# only access the even number

a = [1,2,3,4,5,6]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)

# only access the odd number

c = [1,2,3,4,5,6]
d = []
for i in c:
    if i % 2 != 0:
        d.append(i)
print(d)