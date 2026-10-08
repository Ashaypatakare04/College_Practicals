def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def greater(a, b):
    return a if a > b else b

def simple_interest(p, r, t):
    return p * r * t / 100

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def area_circle(r):
    return 3.14 * r * r

def natural_sum(n):
    return n * (n + 1) // 2

def power(base, exponent):
    return base ** exponent

print("Factorial:", factorial(5))
print("Even or Odd:", even_odd(10))
print("Greater Number:", greater(10, 20))
print("Simple Interest:", simple_interest(10000, 5, 2))
print("Prime Number:", is_prime(17))
print("Circle Area:", area_circle(5))
print("Natural Numbers Sum:", natural_sum(10))
print("Power:", power(2, 5))
