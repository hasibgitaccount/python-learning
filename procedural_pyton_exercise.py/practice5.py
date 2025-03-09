def is_palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("racecar"))
