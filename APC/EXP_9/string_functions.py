def q10_count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

def q11_reverse_string(s):
    return s[::-1]

def q12_palindrome(value):
    value = str(value)
    return value == value[::-1]

if __name__ == "__main__":
    print(q10_count_vowels("Python Programming"))
    print(q11_reverse_string("Python"))
    print(q12_palindrome("madam"))
    print(q12_palindrome(121))
