def q1_factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def q2_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def q3_greater(a, b):
    return a if a > b else b

def q4_simple_interest(p, r, t):
    return p * r * t / 100

def q5_is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def q6_area_circle(r):
    return 3.14 * r * r

def q7_natural_sum(n):
    return n * (n + 1) // 2

def q8_power(base, exponent):
    return base ** exponent

if __name__ == "__main__":
    print(q1_factorial(5))
    print(q2_even_odd(10))
    print(q3_greater(10, 20))
    print(q4_simple_interest(10000, 5, 2))
    print(q5_is_prime(17))
    print(q6_area_circle(5))
    print(q7_natural_sum(10))
    print(q8_power(2, 5))
