print("Method 1:")
from mypackage import module1,module2
print("Add: ",module1.add(56,47))
print("Divide: ",module2.divide(87,45))

print("\nMethod 2:")
from mypackage.module2 import subtract
from mypackage.module1 import multiply

print("Subtraction: ",subtract(66,33))
print("Multiply: ",multiply(65,35))