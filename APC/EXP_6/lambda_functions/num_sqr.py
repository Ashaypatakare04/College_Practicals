num = []
for i in range(5):
    num.append(int(input("element:")))
squares = list(map(lambda x: x **2, num))
print("Squares:", squares)
