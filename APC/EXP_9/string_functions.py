def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

def reverse_string(s):
    return s[::-1]

def palindrome(value):
    value = str(value)
    return value == value[::-1]

print("Vowel Count:", count_vowels("Python Programming"))
print("Reversed String:", reverse_string("Python"))
print("String Palindrome:", palindrome("madam"))
print("Number Palindrome:", palindrome(121))
