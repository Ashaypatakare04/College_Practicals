def display_employees():
    file = open("employees.txt", "r")

    for line in file:
        emp_id, name, dept, salary = line.strip().split(",")
        print(emp_id, name, dept, salary)

    file.close()


def highest_paid():
    file = open("employees.txt", "r")
    employees = []

    for line in file:
        emp_id, name, dept, salary = line.strip().split(",")
        employees.append((emp_id, name, dept, float(salary)))

    file.close()

    employee = max(employees, key=lambda x: x[3])

    print("\nHighest Paid Employee:")
    print("ID:", employee[0])
    print("Name:", employee[1])
    print("Department:", employee[2])
    print("Salary:", employee[3])


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        emp_id, name, dept, salary = line.strip().split(",")
        total += float(salary)
        count += 1

    file.close()

    print("\nAverage Salary:", total / count)


def above_salary(amount):
    file = open("employees.txt", "r")

    print("\nEmployees earning above", amount)

    for line in file:
        emp_id, name, dept, salary = line.strip().split(",")

        if float(salary) > amount:
            print(emp_id, name, dept, salary)

    file.close()


# Function calls
print("All Employees:")
display_employees()

highest_paid()
average_salary()

salary = float(input("\nEnter salary limit: "))
above_salary(salary)