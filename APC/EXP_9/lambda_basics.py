square = lambda x: x * x
cube = lambda x: x ** 3
even = lambda x: x % 2 == 0
maximum = lambda a, b: a if a > b else b
simple_interest = lambda p, r, t: p * r * t / 100

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Square:", square(5))
print("Cube:", cube(5))
print("Even Check:", even(10))
print("Maximum:", maximum(10, 20))
print("Simple Interest:", simple_interest(10000, 5, 2))

numbers = [1, 2, 3, 4, 5]

print("Squares using map:", list(map(lambda x: x ** 2, numbers)))
print("Cubes using map:", list(map(lambda x: x ** 3, numbers)))

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print("Sum of Corresponding Elements:", list(map(lambda x, y: x + y, a, b)))

print("Even Numbers:", list(filter(lambda x: x % 2 == 0, numbers)))
print("Prime Numbers:", list(filter(lambda x: prime(x), numbers)))

mixed = [-5, 2, -1, 8, 0, 10]
print("Positive Numbers:", list(filter(lambda x: x > 0, mixed)))

values = [20, 60, 45, 80, 90, 30]
print("Numbers Greater Than 50:", list(filter(lambda x: x > 50, values)))

words = ["apple", "banana", "cat", "elephant", "computer"]
print("Words Longer Than 5:", list(filter(lambda x: len(x) > 5, words)))
print("Words Sorted by Length:", sorted(words, key=lambda x: len(x)))

students = [("Amit", 75), ("Rahul", 90), ("Priya", 85)]
print("Students Sorted by Marks:", sorted(students, key=lambda x: x[1]))

employees = [("Amit", 40000), ("Rahul", 60000), ("Priya", 50000)]
print("Employees Sorted by Salary:", sorted(employees, key=lambda x: x[1]))
