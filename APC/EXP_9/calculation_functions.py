def q17_fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def q18_percentage_grade(m1, m2, m3, m4, m5):
    percentage = (m1 + m2 + m3 + m4 + m5) / 5
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade

def q19_electricity_bill(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 500 + (units - 100) * 7
    return 1200 + (units - 200) * 10

def q20_gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

def q21_total_bill(prices, quantities, discount):
    total = 0
    for i in range(len(prices)):
        total += prices[i] * quantities[i]
    return total - total * discount / 100

if __name__ == "__main__":
    print(q17_fibonacci(10))
    print(q18_percentage_grade(85, 90, 80, 88, 92))
    print(q19_electricity_bill(250))
    print(q20_gross_salary(30000))
    print(q21_total_bill([100, 200, 300], [2, 1, 3], 10))
