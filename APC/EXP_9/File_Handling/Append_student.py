file = open("student.txt", "a")

info = input("Enter additional student information: ")

file.write(info + "\n")

file.close()

print("Information appended successfully.")
