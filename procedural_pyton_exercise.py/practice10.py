def is_vowels(x):
    vowel = ['a','e','i','o','u']
    count = 0
    for i in x:
        if i.lower() in vowel:
            count += 1
    return count

print(is_vowels("HEllo"))  # Output: 2
print(is_vowels("world"))