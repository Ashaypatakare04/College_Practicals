s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = ''.join(s1.lower().split())
s2 = ''.join(s2.lower().split())

if sorted(s1) == sorted(s2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")
