def q23_total(marks):
    return sum(marks)

def q23_percentage(marks):
    return sum(marks) / 5

def q23_grade(percentage):
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

def q23_process_students(students):
    results = []
    for name, roll, marks in students:
        total = q23_total(marks)
        percentage = q23_percentage(marks)
        grade = q23_grade(percentage)
        results.append({
            "name": name,
            "roll": roll,
            "total": total,
            "percentage": percentage,
            "grade": grade
        })

    class_average = sum(x["percentage"] for x in results) / len(results)
    highest = max(results, key=lambda x: x["percentage"])
    lowest = min(results, key=lambda x: x["percentage"])

    return results, class_average, highest, lowest

if __name__ == "__main__":
    students = [
        ("Amit", 1, [80, 85, 90, 75, 88]),
        ("Rahul", 2, [70, 75, 80, 72, 78]),
        ("Priya", 3, [90, 92, 88, 95, 91])
    ]

    results, average, highest, lowest = q23_process_students(students)

    for student in results:
        print(student)

    print("Class Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
