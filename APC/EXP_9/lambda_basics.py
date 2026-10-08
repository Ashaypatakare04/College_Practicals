q33_square = lambda x: x * x
q34_cube = lambda x: x ** 3
q35_even = lambda x: x % 2 == 0
q36_maximum = lambda a, b: a if a > b else b
q37_simple_interest = lambda p, r, t: p * r * t / 100

def q42_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(q33_square(5))
    print(q34_cube(5))
    print(q35_even(10))
    print(q36_maximum(10, 20))
    print(q37_simple_interest(10000, 5, 2))

    numbers = [1, 2, 3, 4, 5]

    q38_squares = list(map(lambda x: x ** 2, numbers))
    print(q38_squares)

    q39_cubes = list(map(lambda x: x ** 3, numbers))
    print(q39_cubes)

    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    q40_sum = list(map(lambda x, y: x + y, a, b))
    print(q40_sum)

    q41_even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(q41_even_numbers)

    q42_prime_numbers = list(filter(lambda x: q42_prime(x), numbers))
    print(q42_prime_numbers)

    mixed = [-5, 2, -1, 8, 0, 10]
    q43_positive = list(filter(lambda x: x > 0, mixed))
    print(q43_positive)

    values = [20, 60, 45, 80, 90, 30]
    q44_greater_50 = list(filter(lambda x: x > 50, values))
    print(q44_greater_50)

    words = ["apple", "banana", "cat", "elephant", "computer"]
    q45_long_words = list(filter(lambda x: len(x) > 5, words))
    print(q45_long_words)

    q46_sorted_words = sorted(words, key=lambda x: len(x))
    print(q46_sorted_words)

    students = [("Amit", 75), ("Rahul", 90), ("Priya", 85)]
    q47_sorted_students = sorted(students, key=lambda x: x[1])
    print(q47_sorted_students)

    employees = [("Amit", 40000), ("Rahul", 60000), ("Priya", 50000)]
    q48_sorted_employees = sorted(employees, key=lambda x: x[1])
    print(q48_sorted_employees)
