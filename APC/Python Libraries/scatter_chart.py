import matplotlib.pyplot as plt
x = [10, 20, 30, 40, 50]
y = [15, 35, 25, 45, 60]

plt.scatter(x, y, color='blue', marker='o')
plt.title("Scatterplot")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.show()