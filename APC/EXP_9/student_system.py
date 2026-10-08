def total(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / 5

def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "F"

def process_students(students):
    results = []

    for name, roll, marks in students:
        t = total(marks)
        p = percentage(marks)
        g = grade(p)
        results.append((name, roll, t, p, g))

    class_average = sum(x[3] for x in results) / len(results)
    highest = max(results, key=lambda x: x[3])
    lowest = min(results, key=lambda x: x[3])

    return results, class_average, highest, lowest

students = [
    ("Amit", 1, [80, 85, 90, 75, 88]),
    ("Rahul", 2, [70, 75, 80, 72, 78]),
    ("Priya", 3, [90, 92, 88, 95, 91])
]

results, average, highest, lowest = process_students(students)

print("Student Results:")
for student in results:
    print(student)

print("Class Average:", average)
print("Highest Scorer:", highest)
print("Lowest Scorer:", lowest)
