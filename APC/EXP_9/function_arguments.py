def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(func, a, b):
    return func(a, b)

print("Addition:", calculate(add, 10, 5))
print("Subtraction:", calculate(subtract, 10, 5))
print("Multiplication:", calculate(multiply, 10, 5))
print("Division:", calculate(divide, 10, 5))
