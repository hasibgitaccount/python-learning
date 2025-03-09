def is_anagram(x1, x2):
    return sorted(x1) == sorted(x2)

print(is_anagram("listen", "silent")) 
print(is_anagram("hello", "world"))