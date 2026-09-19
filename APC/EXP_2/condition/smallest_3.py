x=int(input("Enter a 1st number: "))
y=int(input("Enter a 2nd number: "))
z=int(input("Enter a 3rd number: "))
if x<y and x<z:
    print(x, "is the smallest number.")
elif y<x and y<z:
    print(y, "is the smallest number.")
else:
    print(z, "is the smallest number.")
