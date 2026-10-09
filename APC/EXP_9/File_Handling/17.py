# Read student records
file = open("students.txt", "r")

students = []

for line in file:
    roll, name, marks = line.strip().split(",")
    students.append((roll, name, int(marks)))

file.close()

# Display all records
print("All Student Records:")
for student in students:
    print(student[0], student[1], student[2])

# Find student with highest marks
highest = max(students, key=lambda x: x[2])

print("\nStudent with highest marks:")
print("Roll No:", highest[0])
print("Name:", highest[1])
print("Marks:", highest[2])

# Calculate average marks
total = sum(student[2] for student in students)
average = total / len(students)

print("\nAverage Marks:", average)

# Display students scoring more than 80
print("\nStudents scoring more than 80:")
for student in students:
    if student[2] > 80:
        print(student[0], student[1], student[2])