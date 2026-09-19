student = []
grade = []

def add():
    name = input("Enter name: ")
    g = int(input("Enter grade: "))
    student.append(name)
    grade.append(g)
    print("Name added successfully!\n")

def update():
    target = input("Enter student name to update: ")
    for i in range(len(student)):
        if student[i] == target:
            g = int(input("Enter updated grade: "))
            grade[i] = g
            print("Updated successfully!\n")
            return
    print("Student not found!\n")

def remove():
    target = input("Enter student name to remove: ")
    for i in range(len(student)):
        if student[i] == target:
            student.pop(i)
            grade.pop(i)
            print("Removed successfully!\n")
            return
    print("Student not found!\n")

def average():
    if not grade:
        print("No grades available to calculate average.\n")
        return
    avg = sum(grade) / len(grade)
    print("Average:", avg, "\n")

def minmax():
    if not grade:
        print("No grades available.\n")
        return
    print("Highest Grade:", max(grade))
    print("Lowest Grade:", min(grade), "\n")


add()
add()
average()
remove()
average()
minmax()
