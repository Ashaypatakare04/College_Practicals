class Calculator:
    def add(self, a, b, c=0, d=0):
        return a + b + c + d


calc = Calculator()

print("2 numbers:", calc.add(10, 20))
print("3 numbers:", calc.add(10, 20, 30))
print("4 numbers:", calc.add(10, 20, 30, 40))
