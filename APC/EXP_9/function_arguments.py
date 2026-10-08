def q32_add(a, b):
    return a + b

def q32_subtract(a, b):
    return a - b

def q32_multiply(a, b):
    return a * b

def q32_divide(a, b):
    return a / b

def q32_calculate(func, a, b):
    return func(a, b)

if __name__ == "__main__":
    print(q32_calculate(q32_add, 10, 5))
    print(q32_calculate(q32_subtract, 10, 5))
    print(q32_calculate(q32_multiply, 10, 5))
    print(q32_calculate(q32_divide, 10, 5))
