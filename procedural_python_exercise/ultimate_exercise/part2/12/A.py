# 12. String Manipulation

# A. Write a program that counts how many times a specific word appears in a given text file.
def repeatation(x):
    frequency = {}

    words = x.split()

    for i in words:
        if i in frequency:
            frequency[i] +=1
        else:
            frequency[i] = 1
    return frequency

text = "hello world hello hello python world python code hello"
print(repeatation(text))

def deeper(x):
    frequency = {}

    words = x.split()

    for i in words:
        for j in i:
            if j in frequency:
                frequency[j] += 1
            else:
                frequency[j] = 1

    return frequency

text = "hello world hello hello python world python code hello"
print(deeper(text))

def i_love_you_chatgpt(x):
    frequency = {}

    for i in x:
        if i == ' ':
            continue

        if i in frequency:
            frequency[i] += 1

        else:
            frequency[i] = 1

    return frequency

print(i_love_you_chatgpt(text))