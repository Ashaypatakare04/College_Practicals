def process_students(students):
    average = sum(map(lambda x: x[1], students)) / len(students)
    above_75 = list(filter(lambda x: x[1] > 75, students))
    sorted_students = sorted(students, key=lambda x: x[1])
    return average, above_75, sorted_students

def process_employees(employees):
    above_50000 = list(filter(lambda x: x[2] > 50000, employees))
    increased = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))
    sorted_employees = sorted(employees, key=lambda x: x[2])
    return above_50000, increased, sorted_employees

def process_products(products):
    values = list(map(lambda x: (x[0], x[1] * x[2]), products))
    above_1000 = list(filter(lambda x: x[1] > 1000, values))
    sorted_products = sorted(values, key=lambda x: x[1])
    return values, above_1000, sorted_products

def process_words(words):
    lengths = list(map(lambda x: len(x), words))
    long_words = list(filter(lambda x: len(x) > 5, words))
    sorted_words = sorted(words, key=lambda x: len(x))
    return lengths, long_words, sorted_words

students = [
    ("Amit", 80),
    ("Rahul", 65),
    ("Priya", 90),
    ("Neha", 75)
]

employees = [
    ("Amit", "IT", 60000),
    ("Rahul", "HR", 45000),
    ("Priya", "IT", 70000),
    ("Neha", "Sales", 50000)
]

products = [
    ("Laptop", 50000, 1),
    ("Mouse", 800, 2),
    ("Keyboard", 1500, 2),
    ("Headphones", 2000, 1)
]

words = ["apple", "banana", "cat", "elephant", "computer", "dog"]

student_result = process_students(students)
employee_result = process_employees(employees)
product_result = process_products(products)
word_result = process_words(words)

print("Student Average:", student_result[0])
print("Students Above 75:", student_result[1])
print("Students Sorted by Marks:", student_result[2])

print("Employees Earning Above 50000:", employee_result[0])
print("Employees After 10% Increase:", employee_result[1])
print("Employees Sorted by Salary:", employee_result[2])

print("Product Total Values:", product_result[0])
print("Products Above 1000:", product_result[1])
print("Products Sorted by Total Value:", product_result[2])

print("Word Lengths:", word_result[0])
print("Words Longer Than 5:", word_result[1])
print("Words Sorted by Length:", word_result[2])
