import matplotlib.pyplot as plt

x = ['A1', 'B1', 'C1', 'D1']
y = [78, 87, 75, 92]

plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()