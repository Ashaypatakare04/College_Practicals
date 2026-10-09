file = open("student.txt", "r")

content = file.read()
print("Total number of characters:", len(content))

file.close()