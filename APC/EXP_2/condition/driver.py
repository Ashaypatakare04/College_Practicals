n=bool(input("Is driver married? (yes/no): "))
m=bool(input("Is driver male? (yes/no): "))
age=int(input("Enter driver's age: "))
if n:
    print("Driver is insured.")
else:
    if m and age>30:
        print("Driver is insured.")
    elif m!=True and age>25:
        print("Driver is insured.")
    else:
        print("Driver is not insured.")
