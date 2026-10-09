file = open("student.txt", "r")

content = file.read()
words = content.split()

print("Total number of words:", len(words))

file.close()