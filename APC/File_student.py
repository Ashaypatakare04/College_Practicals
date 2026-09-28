file = open("student.txt", "w")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")

file.close()

print("Student information written to student.txt")
