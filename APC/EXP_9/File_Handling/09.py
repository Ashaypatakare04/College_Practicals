file = open("student.txt", "r")

content = file.read()

vowels = 0
consonants = 0

for ch in content:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

file.close()