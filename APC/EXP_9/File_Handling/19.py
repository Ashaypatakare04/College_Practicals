file = open("attendance.txt", "r")

print("Students with attendance below 75%:")

for line in file:
    roll, name, attended, total = line.strip().split(",")

    attended = int(attended)
    total = int(total)

    percentage = (attended / total) * 100

    print(name, "Attendance:", percentage, "%")

    if percentage < 75:
        print("Below 75%:", name)

file.close()